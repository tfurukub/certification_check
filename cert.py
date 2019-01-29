import pandas as pd
pd.set_option("display.max_rows", 1000)

df = pd.read_csv("report.csv")
df1 = df[['Account Name','Certificate Name']].dropna()
#df1 = df1.drop_duplicates().sort_values('Account Name')
df1 = df1.sort_values('Account Name')
#print(df1)

account = df1['Account Name'].unique()
print("Account:","NCP-5:","NCSE-L1:","NCSR-L1:","NCSR-L2:","NCSR-L3:","CCIC")
for name in account:
    df_temp = df1[df1['Account Name'] == name]
    cert_array = df_temp['Certificate Name'].values
    cert = [" :"] * 6
    flag_L1 = 0
    flag_L2 = 0
    flag_L3 = 0
    for temp in cert_array:
        if(temp == "NCP-5"):
            cert[0] = "OK:"
        elif(temp == "NCSE-L1"):
            cert[1] = "OK:"
        elif(temp == "NCSR-L1"):
            flag_L1 = flag_L1 + 1
            if(flag_L1 == 1):
                cert[2] = "1:"
            elif(flag_L1 == 2):
                cert[2] = "OK:"
        elif(temp == "NCSR-L2"):
            flag_L2 = flag_L2 + 1
            if(flag_L2 == 1):
                cert[3] = "1:"
            elif(flag_L2 == 2):
                cert[3] = "OK:"
        elif(temp == "NCSR-L3"):
            flag_L3 = flag_L3 + 1
            if(flag_L3 == 1):
                cert[4] = "1:"
            elif(flag_L3 == 2):
                cert[4] = "OK:"
        elif(temp == "CCIC"):
            cert[5] = "OK"

    print(name,end="	")
    for t in cert:
        print(t,end="")
    print("")
        
