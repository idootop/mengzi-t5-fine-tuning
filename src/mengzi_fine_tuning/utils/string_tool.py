import os

from .basic import isNotEmpty
from .io_tool import exists, getFilePath

# 特殊字符(删除)
kSpecialCharacters = ["\ufeff", "\xa0", "\u3000"]


def textPreProcessing(text: str):
    """
    文本预处理：
    1. 去除前后空格
    2. 去除特殊字符
    """
    # 去除前后空格
    text = text.strip()
    # 去除特殊字符
    for char in kSpecialCharacters:
        text = text.replace(char, "")
    return text


def readString(nameOrPath: str):
    path = getFilePath(nameOrPath)
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def writeString(nameOrPath: str, text: str, append=False):
    path = getFilePath(nameOrPath)
    # 文件读写模式参考 https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
    mode = "a" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.write(text)


def readLastLine(nameOrPath: str):
    path = getFilePath(nameOrPath)
    if not exists(path):
        return ""
    with open(path, "rb") as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                # 向上找到换行符号
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            # 如果只有 1 行，或内容为空，则回到文件开头
            f.seek(0)
        lastLine = f.readline().decode(encoding="utf-8")
    return lastLine


def readLines(nameOrPath: str):
    path = getFilePath(nameOrPath)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def writeLines(nameOrPath: str, lines: list[str], append=False):
    path = getFilePath(nameOrPath)
    mode = "a" if append else "w"
    lastLine = readLastLine(nameOrPath)
    shouldEnterNextLine = isNotEmpty(lastLine) and not lastLine.endswith("\n")
    with open(path, mode, encoding="utf-8") as f:
        # 如果文件内容非空，自动换行
        if shouldEnterNextLine:
            f.write("\n")
        f.writelines(f"{line.strip()}\n" for line in lines)
