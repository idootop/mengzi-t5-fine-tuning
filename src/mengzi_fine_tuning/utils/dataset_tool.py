from datasets import load_dataset

from .string_tool import readLines


def loadCSVDataset(subdir: str):
    """
    加载 data 目录下的 CSV 数据集
    """
    columnNames = [
        line.split(" #")[0] for line in readLines(f"./data/{subdir}/index.sh")
    ]
    return load_dataset(
        engine="python",
        path="csv",
        delimiter="｜",
        column_names=columnNames,
        data_files={
            "train": f"./data/{subdir}/train.csv",
            "test": f"./data/{subdir}/test.csv",
        },
    )
