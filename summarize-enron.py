# -*- coding: utf-8 -*-
"""

@author: latec
"""
import matplotlib.pyplot as plt
import pandas as pd
emails = pd.read_csv('enron-event-history-all.csv',names=['time', 'id', 'sender', 'receive', 'content','email'])


emails=emails.drop(['content','email'], axis=1)

emails=emails.dropna() 

rows = []

for i in range(emails.shape[0]):
    row=[]
    z=emails.iloc[i,3].split("|")
    row.append(emails.iloc[i,0])
    row.append(emails.iloc[i,1])
    row.append(emails.iloc[i,2])
    row.append(emails.iloc[i,2])
 
    for k in range(len(z)): 
        row[3]=z[k]
        rows.append(row.copy())
 
receivers=pd.DataFrame(rows) 
receivers.columns=['time', 'id', 'sender', 'receive']

esend=emails.groupby('sender').count()
ereceive=receivers.groupby('receive').count()


df1=esend
df1.columns=['times', 'ids', 'receives']
df2=ereceive
df2.columns=['timer', 'idr', 'senderr']
df3=df1.join(df2, how='outer')

final_df = df3.sort_values(by=['times'], ascending=False)
df=emails

prolific=final_df.drop(['ids','receives','idr','senderr'], axis=1)
prolific.to_csv('prolific.csv', header=False, sep=',')

#create histograms of 5 most prolific senders
for k in range(5):
    dfm1=df.loc[df['sender'] == final_df.index.values[k]]
    dfm1.plot.hist(grid=True, bins=80,color='red')
    plt.show()
    print(final_df.index.values[k])