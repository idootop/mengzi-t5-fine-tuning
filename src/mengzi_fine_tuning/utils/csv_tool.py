import pandas as pd
from .basic import exists, makeDir


def getCSVPath(nameOrPath: str):
    defaultRoot = "./data"
    nameOrPath = nameOrPath.replace(".csv", "")
    if "/" in nameOrPath:
        path = f"{nameOrPath}.csv"
    else:
        path = f"{defaultRoot}/{nameOrPath}.csv"
    return path


def readCSV(nameOrPath: str, split=","):
    """
    读取 CSV 数据列表
    """
    path = getCSVPath(nameOrPath)
    if exists(path):
        return pd.read_csv(path, sep=split)


def writeCSV(datas: pd.DataFrame, nameOrPath: str, split=","):
    """
    写入 CSV 数据列表
    """
    path = getCSVPath(nameOrPath)
    makeDir(filePath=path)
    datas.to_csv(
        path,
        sep=split,
        index=False,
    )
