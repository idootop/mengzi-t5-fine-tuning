from mengzi_fine_tuning.utils import readCSV, writeCSV

datas = readCSV("test")
print(datas)
writeCSV(datas, "copy/itx")
writeCSV(datas, "copy/it.csv")
