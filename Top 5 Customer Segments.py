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
# SQL Query to fetch top 5 customer segments by revenue
query = """
SELECT TOP(5) cc.CustomerCategoryName, SUM(i.TotalDryItems + 
i.TotalChillerItems) as Revenue
FROM Sales.Customers c
JOIN Sales.Invoices i ON c.CustomerID = i.CustomerID
JOIN Sales.CustomerCategories cc ON c.CustomerCategoryID = 
cc.CustomerCategoryID
GROUP BY cc.CustomerCategoryName
ORDER BY Revenue DESC
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
# Plotting the data as a funnel chart
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(df['CustomerCategoryName'], df['Revenue'], color='purple')
plt.xlabel('Revenue')
plt.ylabel('Customer Segment')
plt.title('Top 5 Customer Segments by Revenue')
plt.gca().invert_yaxis() # Invert y-axis for better funnel visualization
plt.show()
# Close the connection
connection.close()