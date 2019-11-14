#adding all the excels files with sub-headers in a directory into a single excel file

import glob
import pandas as pd

all_data = pd.DataFrame()
print("hello")
for f in glob.glob("C:/Users/sbiswas149/Applications/data/PoC data/Australia/Final Output/*.xlsx"):
    df = pd.read_excel(f, header=[0,1])
    all_data = all_data.append(df,ignore_index=True)
    
all_data.to_excel("C:/Users/sbiswas149/Applications/data/PoC data/Australia/output.xlsx")



#adding multiple sheet into a single excel file
import glob
import pandas as pd

all_data1 = pd.DataFrame()
all_data2 = pd.DataFrame()
print("hello")
for f in glob.glob("C:/Users/sbiswas149/Applications/data/PoC data/Australia/Final Output/*"):
    df1 = pd.read_excel(f, header=[0,1], sheet_name = 'Details')
    df2 = pd.read_excel(f, header=[0], sheet_name = "Log File")
    all_data1 = all_data1.append(df1, ignore_index=True)
    all_data2 = all_data2.append(df2, ignore_index=True)
    
with pd.ExcelWriter('C:/Users/sbiswas149/Applications/data/PoC data/Australia/output.xlsx') as writer:
    all_data1.to_excel(writer, sheet_name='Details')
    all_data2.to_excel(writer, sheet_name='Log File')
    
#all_data1.to_excel("C:/Users/sbiswas149/Applications/data/PoC data/Australia/output.xlsx", sheet_name = "Details")
#all_data2.to_excel("C:/Users/sbiswas149/Applications/data/PoC data/Australia/output.xlsx", sheet_name = "Log File")
print("done")
