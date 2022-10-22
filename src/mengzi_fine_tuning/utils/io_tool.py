from pathlib import Path

from .basic import isNotEmpty


# 数据存放路径
kDataRoot = "./data"


def exists(path: str):
    """
    判断文件路径是否存在
    """
    return Path(path).exists()


def makeDir(_dir="", filePath=""):
    """
    自动补全文件所在的文件夹路径，如果父级文件夹不存在
    """
    if isNotEmpty(_dir):
        Path(_dir).mkdir(parents=True, exist_ok=True)
    else:
        Path(filePath).parent.mkdir(parents=True, exist_ok=True)


def getFilePath(nameOrPath: str):
    """
    获取文件路径，默认目录为 `./data`

    ```python
    - getFilePath('test.csv') # ./data/test.csv
    - getFilePath('subdir/test.csv') # ./data/subdir/test.csv
    - getFilePath('./data/test.csv') # ./data/test.csv
    - getFilePath('/Users/desktop/test.csv') # /Users/desktop/test.csv
    - getFilePath('C:\\Users\\desktop\\test.csv') # C:\\Users\\desktop\\test.csv
    ```
    """
    splits = nameOrPath.split(".")
    suffix = splits[-1] if len(splits) > 1 else ""
    nameOrPath = nameOrPath.replace("\\", "/").replace(f".{suffix}", "")
    suffix = f".{suffix}" if isNotEmpty(suffix) else ""
    isPath = (
        nameOrPath.startswith("/") or nameOrPath.startswith("./") or ":/" in nameOrPath
    )
    if isPath:
        path = f"{nameOrPath}{suffix}"
    else:
        path = f"{kDataRoot}/{nameOrPath}{suffix}"
    return path