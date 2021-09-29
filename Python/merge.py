# 多个csv文件合并成一个
import glob
import os
import pandas as pd

path = "D:\Microsoft\Project\log files\第8周"

all_files = glob.glob(os.path.join(path, "*.csv"))


df = pd.read_csv(all_files[0])
df.to_csv("merge.csv", encoding='utf_8_sig', index=False)

for i in range(1, len(all_files)):
    df = pd.read_csv(all_files[i])
    df.to_csv("merge.csv", encoding='utf_8_sig', index=False, header=False, mode="a+")

