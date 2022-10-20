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
