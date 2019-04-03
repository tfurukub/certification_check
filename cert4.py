import pandas as pd
import sys
from collections import OrderedDict

pd.set_option("display.max_rows", 1000)

df = pd.read_csv(sys.argv[1])
df1 = df[['Account Name','Certificate Name']].dropna().sort_values('Account Name')

account = df1['Account Name'].unique()
fl = ['NCP-5','NCSE-L1','NCSR-L1','NCSR-L2','NCSR-L3']
cert_check = {}
for item in account:
    cert_check[item] = {}
    for f in fl:
        cert_check[item][f] = 0 

for index,row in df1.iterrows():
    acc = row['Account Name']
    cer = row['Certificate Name']
    if cer in fl:
        cert_check[acc][cer] += 1
#        print(acc,cer,cert_check[acc])

print("Account",end=":")
for f in fl:
    print(f,end=":")
print("")

for key in cert_check.keys():
    print(key,end=":")
    for f in fl:
        print(cert_check[key][f],end=":")
    print("")
