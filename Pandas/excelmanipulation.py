#adding all the excels files with sub-headers in a directory into a single excel file

import glob
import pandas as pd

all_data = pd.DataFrame()
print("hello")
for f in glob.glob("C:/Users/sbiswas149/Applications/data/PoC data/Australia/Final Output/*.xlsx"):
    df = pd.read_excel(f, header=[0,1])
    all_data = all_data.append(df,ignore_index=True)
    
all_data.to_excel("C:/Users/sbiswas149/Applications/data/PoC data/Australia/output.xlsx")
