import pyodbc
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
# Establish connection to the AdventureWorks2022 database using pyodbc
connection = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'  # Specifies the ODBC driver to use
    r'SERVER=DESKTOP-G1HPGDT\SQLEXPRESS;'       # Specifies the SQL Server instance
    r'DATABASE=WideWorldImporters;'            # Specifies the database name
    r'Trusted_Connection=yes;'                 # Enables Windows Authentication
    r'TrustServerCertificate=yes;'             # Allows untrusted certificates (use carefully in production)
)
# SQL Query to fetch the top 3 products sold each month
query = """
WITH MonthlyProductSales AS (
 SELECT FORMAT(o.OrderDate, 'yyyy-MM') as Month, ol.StockItemID, 
SUM(ol.Quantity * ol.UnitPrice) as Revenue
 FROM Sales.Orders o
 JOIN Sales.OrderLines ol ON o.OrderID = ol.OrderID
 GROUP BY FORMAT(o.OrderDate, 'yyyy-MM'), ol.StockItemID
), 
RankedMonthlySales AS (
 SELECT Month, StockItemID, Revenue,
 RANK() OVER(PARTITION BY Month ORDER BY Revenue DESC) as 
Rank
 FROM MonthlyProductSales
)
SELECT Month, StockItemID, Revenue
FROM RankedMonthlySales
WHERE Rank <= 3
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
# Pivot the DataFrame for stacked area chart
df_pivot = df.pivot(index='Month', columns='StockItemID', 
values='Revenue').fillna(0)
# Plotting the data as a stacked area chart
plt.stackplot(df_pivot.index, df_pivot.T)
plt.legend(df_pivot.columns, loc='upper left')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Top 3 Products Sold Each Month by Revenue')
plt.xticks(rotation='vertical') # Rotate month labels vertically
plt.show()
# close the connection
connection.close()