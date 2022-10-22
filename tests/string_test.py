from mengzi_fine_tuning.utils.string_tool import (
    readString,
    readLines,
    writeString,
    writeLines,
)

kStrPath = "./tests/data/string/test.txt"

# 读取行
print(">>> 读取行")
lines = readLines(kStrPath)
print("\n".join(lines))

# 追加行
print(">>> 追加行")
writeLines(kStrPath, lines, append=True)
string = readString(kStrPath)
print(string)

# 覆盖行
print(">>> 覆盖行")
writeLines(kStrPath, lines)
string = readString(kStrPath)
print(string)

# 覆盖文字
print(">>> 覆盖文字")
writeString(kStrPath, "hello world")
string = readString(kStrPath)
print(string)

# 追加文字
print(">>> 追加文字")
writeString(kStrPath, "\nhello world", append=True)
string = readString(kStrPath)
print(string)

writeLines(kStrPath, lines)
