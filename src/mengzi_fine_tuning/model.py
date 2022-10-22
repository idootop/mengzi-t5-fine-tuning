from transformers import T5Tokenizer, T5ForConditionalGeneration

kMaxLength = 512
kModelName = "Langboat/mengzi-t5-base-mt"


class MengziZeroShot:
    def __init__(self):
        # 加载模型
        self.tokenizer = T5Tokenizer.from_pretrained(kModelName)
        self.model = T5ForConditionalGeneration.from_pretrained(kModelName)

    def prompt(self, inputs: str):
        return f"聊天内容：【{inputs.strip()}】\n题目：请总结聊天内容。答："

    def tokenDecode(self, s):
        return self.tokenizer.decode(s, skip_special_tokens=True)

    def inference(self, inputs: list[str]):
        # 构造 prompt
        prompts = [self.prompt(input) for input in inputs]
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
            attention_mask=encodings["attention_mask"],
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
