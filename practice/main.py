import pandas as pd
import numpy as np
data = pd.read_csv(r'sales_data.csv')
df = pd.DataFrame(data)
print(df.head())

results = df.groupby("Region").agg(
    salesman_count=("Salesman", "nunique"),
    total_sales=("Sales", "sum")
).reset_index()
print(results)

hierarchy = df.groupby("Manager")["Salesman"].apply(list).reset_index()
hierarchy.columns = ["manager", "list_of_salesman"]

print(hierarchy)