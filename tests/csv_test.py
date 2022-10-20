from mengzi_fine_tuning.utils import read_csv, writeCSV

datas = read_csv("test")
print(datas)
writeCSV(datas, "copy/itx")
writeCSV(datas, "copy/it.csv")
