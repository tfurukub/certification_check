import pandas as pd
import sys
pd.set_option("display.max_rows", 1000)

df = pd.read_csv(sys.argv[1])
df1 = df[['Account Name','Certificate Name']].dropna()
#df1 = df1.drop_duplicates().sort_values('Account Name')
#df1 = df1.sort_values('Account Name')
#print(df1)
account = df1['Account Name'].unique()
fl = {'NCP-5','NCSE-L1','NCSR-L1','NCSR-L2','NCSR-L3'}
cert_check = {}
for item in account:
    cert_check[item] = {'NCP-5':0,'NCSE-L1':0,'NCSR-L1':0,'NCSR-L2':0,'NCSR-L3':0}

for index,row in df1.iterrows():
    acc = row['Account Name']
    cer = row['Certificate Name']
    if cer in fl:
        cert_check[acc][cer] += 1
#        print(acc,cer,cert_check[acc])

print("Account:","NCP-5:","NCSE-L1:","NCSR-L1:","NCSR-L2:","NCSR-L3:")
for key in cert_check.keys():
    print(key,end=":")
    for item in cert_check[key].values():
        print(item,end=":")
    print("")
