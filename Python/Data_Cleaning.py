import pandas as pd

df = pd.read_csv("Nike_Sales_Uncleaned.csv")     #reading file
print("Orignial Dataset Shape:")
print(df.shape)

df = df.drop_duplicates(subset='Order_ID')      #removing duplicates based on Order ID

important_columns = [
    'Units_Sold',
    'MRP',
    'Discount_Applied',
    'Order_Date'
]

df = df.dropna(subset=important_columns)       #removing null values based on the specific columns

df = df[df['Units_Sold'] > 0]                  #negative units sold

df = df = df[df['MRP'] > 0]                    #remove MRP


df = df[df['Discount_Applied'] <= 1]           #remove dsicounts greater than 100%


df['Order_Date'] = pd.to_datetime(             #Converting Order_Date to datetime format 
    df['Order_Date'],
    errors='coerce'
)

df = df.dropna(subset=['Order_Date'])           # Remove rows where date conversion failed


df['Order_Date'] = df['Order_Date'].dt.strftime('%Y-%m-%d')   # Format date as YYYY-MM-DD


df['Region'] = df['Region'].replace({                       # Cleaning common city typos
    'Delhii': 'Delhi',
    'Banglore': 'Bangalore'
})


df['Expected_Revenue'] = (                                  # Calculating Expected Revenue
    df['Units_Sold'] *
    df['MRP'] *
    (1 - df['Discount_Applied'])
)


df['Expected_Revenue'] = df['Expected_Revenue'].round(2)   # Rounding off Expected revenue


output_file = "cleaned_nike_sales_data.xlsx"                #saving processed data

df.to_excel(output_file, index=False)

print("\nData cleaning completed successfully!")
print(f"Cleaned file saved as: {output_file}")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
