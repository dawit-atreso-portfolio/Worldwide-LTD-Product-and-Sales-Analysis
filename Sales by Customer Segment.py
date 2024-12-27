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
SELECT cs.CustomerCategoryName, SUM(ol.Quantity * ol.UnitPrice) as 
TotalRevenue
FROM Sales.Customers c
JOIN Sales.Orders o ON c.CustomerID = o.CustomerID
JOIN Sales.OrderLines ol ON o.OrderID = ol.OrderID
JOIN Sales.CustomerCategories cs ON c.CustomerCategoryID = 
cs.CustomerCategoryID
GROUP BY cs.CustomerCategoryName
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
print(df)
# Plotting the data as a bar chart
plt.barh(df['CustomerCategoryName'], df['TotalRevenue'], 
color='orange')
plt.ylabel('Customer Segment')
plt.xlabel('Total Revenue (In Millions)')
plt.title('Sales Revenue by Customer Segment')
plt.xticks(rotation=45)
plt.show()
# close the connection
connection.close()