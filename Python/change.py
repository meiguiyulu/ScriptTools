# 修改文件后缀名
import os

filename = "Kusto query result for Edgeformfill"
suffix = ".html"


files = os.listdir(".")
for file in files:
    # os.path.splitext(file)
    if file == filename:
        os.rename(filename, filename + suffix)
