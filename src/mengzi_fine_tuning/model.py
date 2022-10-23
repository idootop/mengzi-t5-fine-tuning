from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    TrainingArguments,
    default_data_collator,
    Trainer,
)

from .utils.dataset_tool import loadCSVDataset

kBatchSize = 100
kMaxLength = 512


class MengziZeroShot:
    @staticmethod
    def __defaultPrompt(inputs: str):
        return inputs

    def __init__(
        self,
        modelName="Langboat/mengzi-t5-base-mt",
        modelSubDir=None,
        dataSubdir="default",
        promptBuilder=None,
    ):
        self.dataSubdir = dataSubdir
        self.promptBuilder = (
            promptBuilder if promptBuilder else MengziZeroShot.__defaultPrompt
        )
        # 加载模型
        useLocal = bool(modelSubDir)
        self.modelPath = f"./model/{modelSubDir}" if useLocal else modelName
        self.tokenizer = T5Tokenizer.from_pretrained(
            self.modelPath, local_files_only=useLocal
        )
        self.model = T5ForConditionalGeneration.from_pretrained(
            self.modelPath, local_files_only=useLocal
        )

    def __tokenizeDatasets(self, dataSubdir: str):
        datasets = loadCSVDataset(dataSubdir)

        def encoding(data):
            prompts = [self.promptBuilder(data) for data in data["inputs"]]
            tokenizedInputs = self.tokenizer(
                prompts,
                padding=True,
                truncation=True,
                max_length=kMaxLength,
                return_tensors="pt",
            )
            tokenizedOutputs = self.tokenizer(
                text_target=[str(out) for out in data["outputs"]],
                padding=True,
                truncation=True,
                max_length=kMaxLength,
                return_tensors="pt",
            )
            tokenizedInputs["labels"] = tokenizedOutputs["input_ids"]
            return tokenizedInputs

        return datasets.map(
            encoding, batched=True, remove_columns=datasets["train"].column_names
        )

    def saveOriginModel(self):
        self.model.save_pretrained("./model/origin")
        self.tokenizer.save_pretrained("./model/origin")

    def train(self):
        tokenizedDatasets = self.__tokenizeDatasets(self.dataSubdir)
        dataCollator = default_data_collator
        tarinerConfig = TrainingArguments(
            self.modelPath,
            evaluation_strategy="epoch",
            learning_rate=2e-5,
            per_device_train_batch_size=kBatchSize,
            per_device_eval_batch_size=kBatchSize,
            num_train_epochs=3,
            weight_decay=0.01,
        )
        trainer = Trainer(
            self.model,
            tarinerConfig,
            train_dataset=tokenizedDatasets["train"],
            eval_dataset=tokenizedDatasets["validation"],
            data_collator=dataCollator,
            tokenizer=self.tokenizer,
        )
        trainer.train()
        trainer.save_model()

    def inference(self, inputs: list[str]):
        # 构造 prompt
        prompts = [self.promptBuilder(input) for input in inputs]
        # 编码
        encodings = self.tokenizer(
            prompts,
            padding=True,
            truncation=True,
            max_length=kMaxLength,
            return_tensors="pt",
        )
        # 推理
        outputs = self.model.generate(
            encodings["input_ids"],
            max_length=kMaxLength,
            num_beams=1,
        )
        # 解码
        results = [
            self.tokenizer.decode(output, skip_special_tokens=True)
            for output in outputs
        ]
        for i, inputStr in enumerate(inputs):
            print(f">>> 输入：\n{inputStr}\n")
            # print(f"### Prompts：\n{prompts[i]}\n")
            print(f"<<< 输出：\n{results[i]}\n")
        return results
