"""
Python 学习笔记
"""

# mypy: ignore-errors

from math import inf
from typing import (
    ClassVar,
    Mapping,
    Optional,
    MutableMapping,
    Any,
    Union,
    Callable,
)

# Async
import asyncio


async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


asyncio.run(main())

# Assert
x = inf
assert x is not None, "x不能为空"
assert isinstance(x, str), "x不是字符串"

# Types
x: Any = None  # any, void | null | undefined
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"
x: list[int] = [1]
x: set[int] = {6, 7}
x: dict[str, float] = {"key": "value"}
x: Mapping[str, float] = {"key": "value"}  # 不可变
x: MutableMapping[str, float] = {"key": "value"}  # 不可变
x: tuple[str, str, float] = ("x", "y", 7.5)
x: tuple[int, ...] = (1, 2, 3)
x: Optional[str] = None  # 可空
x: Union[int, str] = [1, "str", []]  # int | string

Vector = list[float]  # 类型别名

# Functions
def addFloat(num1: int, num2: float = 1.0) -> float:
    print(f"{num1} + {num2} = {num1+num2}")
    return num1 + num2


addFloat(1, 2)
addFloat(num2=1.0, num1=2)
x: Callable[[int, float], float] = addFloat  # Callable 👉 function

# Class
class MyClass:
    # static 静态变量
    prefix: ClassVar[str] = "Hello"

    # static 静态方法
    @staticmethod
    def getPrefix() -> str:
        return MyClass.prefix

    def __init__(self) -> None:
        # class 实例变量
        self.inited: bool = True
        # 双下划线，私有变量
        self.__secret: str = "秘密"
        print(f"{MyClass.prefix} World!")

    # class 实例方法
    def test(self) -> None:
        MyClass.getPrefix()


x: MyClass = MyClass()

# 多态继承
class People:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"姓名：{self.name}")


class Student(People):
    def __init__(self, name, age=18):
        # 调用父类构造函数
        People.__init__(self, name)
        self.age: int = age

    # 覆写父类的方法
    def speak(self):
        print(f"姓名：{self.name}，年龄：{self.age}")
