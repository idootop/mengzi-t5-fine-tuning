import pandas as pd
from .io_tool import exists, makeDir, getFilePath


def readCSV(nameOrPath: str, split=","):
    """
    读取 CSV 数据列表

    ```python
    readCSV('example.csv') # 需要指定文件后缀名
    ```
    """
    path = getFilePath(nameOrPath)
    if exists(path):
        return pd.read_csv(path, sep=split)


def writeCSV(nameOrPath: str, datas: pd.DataFrame, split=","):
    """
    写入 CSV 数据列表

    ```python
    writeCSV(datas, 'example.csv') # 需要指定文件后缀名
    ```
    """
    path = getFilePath(nameOrPath)
    makeDir(filePath=path)
    datas.to_csv(
        path,
        sep=split,
        index=False,
    )
