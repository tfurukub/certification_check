import pandas as pd
import sys
pd.set_option("display.max_rows", 1000)

df = pd.read_csv(sys.argv[1])
df1 = df[['Account Name','Certificate Name']].dropna()
#df1 = df1.drop_duplicates().sort_values('Account Name')
df1 = df1.sort_values('Account Name')
#print(df1)

account = df1['Account Name'].unique()
fl = {'NCP-5':0,'NCSE-L1':0,'NCSR-L1':0,'NCSR-L2':0,'NCSR-L3':0,'CCIC':0,}
print("Account:","NCP-5:","NCSE-L1:","NCSR-L1:","NCSR-L2:","NCSR-L3:","CCIC")
for name in account:
    df_temp = df1[df1['Account Name'] == name]
    cert_array = df_temp['Certificate Name'].values
    cert = [" :"] * 6
    flag_L1 = 0
    flag_L2 = 0
    flag_L3 = 0
    fl = {'NCP-5':0,'NCSE-L1':0,'NCSR-L1':0,'NCSR-L2':0,'NCSR-L3':0,'CCIC':0,}
    for temp in cert_array:
        if(temp == "NCP-5"):
            fl['NCP-5'] = fl['NCP-5'] + 1
            cert[0] = str(fl['NCP-5'])+":"
        elif(temp == "NCSE-L1"):
            fl['NCSE-L1'] = fl['NCSE-L1'] + 1
            cert[1] = str(fl['NCSE-L1'])+":"
        elif(temp == "NCSR-L1"):
            fl['NCSR-L1'] = fl['NCSR-L1'] + 1
            cert[2] = str(fl['NCSR-L1'])+":"
        elif(temp == "NCSR-L2"):
            fl['NCSR-L2'] = fl['NCSR-L2'] + 1
            cert[3] = str(fl['NCSR-L2'])+":"
        elif(temp == "NCSR-L3"):
            fl['NCSR-L3'] = fl['NCSR-L3'] + 1
            cert[4] = str(fl['NCSR-L3'])+":"
        elif(temp == "CCIC"):
            fl['CCIC'] = fl['CCIC'] + 1
            cert[5] = str(fl['CCIC'])+":"

    print(name,end="	")
    for t in cert:
        print(t,end="")
    print("")
        
