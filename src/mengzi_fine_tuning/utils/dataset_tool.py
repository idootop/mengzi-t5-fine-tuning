from datasets import load_dataset


def loadCSVDataset(subdir: str):
    """
    加载 data 目录下的 CSV 数据集
    """
    return load_dataset(
        engine="python",
        path="csv",
        delimiter="｜",
        column_names=["inputs", "outputs"],
        data_files={
            "train": f"./data/{subdir}/train.csv",
            "validation": f"./data/{subdir}/validation.csv",
        },
    )
