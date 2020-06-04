# import pandas as pd 
import pandas as pd 
# load the data with pd.read_csv 
# input file should contain tacacs administration log in csv format
# Date,Time,User-Name,Group-Name,cmd,priv-lvl,service,NAS-Portname,task_id,NAS-IP-Address,reason
record = pd.read_csv('combined_csv.csv') 
print(record.groupby(['User-Name'])['cmd'].count().reset_index(name='Commands_count').sort_values(['Commands_count'], ascending=False))
