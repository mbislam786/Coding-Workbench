import pandas as pd

df1 = pd.read_csv("Sales_January_2019.csv")
df1['Month']='January'
print ("\nOriginal File1 Shape:")
print (df1.shape)

###---------------------------------------------------------------###

df2 = pd.read_csv("Sales_February_2019.csv")
df2['Month']='February'
print ("\nOriginal File 2 Shape:")
print (df2.shape)

df3 = pd.concat([df1,df2], ignore_index=True)
print ("\nFile have been merged:")
print (df3.shape)


df3 = df3.drop_duplicates(subset="Order ID")
print ("\nDuplicates removed:")
print (df3.shape)


important_columns = [
    'Order ID',
    'Product',
    'Quantity Ordered',
    'Order Date',
    'Price Each',
    'Purchase Address'
]

df3 = df3.dropna(subset=important_columns)
print("\nNull values removed from file2:")
print (df3.shape)


df3.to_excel("Data_Merging_Output.xlsx", index=False)
print ("\nFinal Merged file:")
print (df3.shape)
print(df3.head())