import pandas as pd
from .basic import exists, makeDir
from .io_tool import getFilePath


def readCSV(nameOrPath: str, split=","):
    """
    读取 CSV 数据列表 readCSV('example.csv')
    """
    path = getFilePath(nameOrPath)
    if exists(path):
        return pd.read_csv(path, sep=split)


def writeCSV(datas: pd.DataFrame, nameOrPath: str, split=","):
    """
    写入 CSV 数据列表
    """
    path = getFilePath(nameOrPath)
    makeDir(filePath=path)
    datas.to_csv(
        path,
        sep=split,
        index=False,
    )
