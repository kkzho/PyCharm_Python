import os
import pandas as pd
excels = [
    pd.read_excel(fname)
    for fname in os.listdir("./")
    if ".xlsx" in fname
]
df = pd.concat(excels)
df.to_excel("合并结果.xlsx",index=False)