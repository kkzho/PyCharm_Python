
import pandas as pd
import os

dfs = []

# read all excel 's sheet append to dfs
for fname in os.listdir("./"):  #判断格式为Excel
    if fname.endswith(".xlsx") and fname != 'final.xlsx':
        df = pd.read_excel(
            fname,  #Excel的文件名
          # header=None,  #不设置标题
            sheet_name=None # (None:所以sheet):
                            # (0:第一个sheet,字符串,[0,2],["sheet1","sheet2"])
        )
        dfs.extend(df.values())

# concat
result = pd.concat(dfs)

# output excel
result.to_excel("./final.xlsx",index=False)