import pandas as pd
df0=pd.read_csv('data/daily_sales_data_0.csv')
df1=pd.read_csv('data/daily_sales_data_1.csv')
df2=pd.read_csv('data/daily_sales_data_2.csv')
df=pd.concat([df0,df1,df2])
df=df[df['product']=='pink morsel']
df['price']=df['price'].str.replace('$','',regex=False)
df['price']=pd.to_numeric(df['price'])
df['sales']=df['quantity']*df['price']
df=df[['sales','date','region']]
df.to_csv('processed_data.csv',index=False)
print("Data processing complete!")
print(df.head())