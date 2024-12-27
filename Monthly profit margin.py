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
# SQL Query to fetch monthly profit margins
query = """
SELECT FORMAT(i.InvoiceDate, 'yyyy-MM') as Month,
 SUM(il.LineProfit) / SUM(il.ExtendedPrice) * 100 as 
ProfitMargin
FROM Sales.Invoices i
JOIN Sales.InvoiceLines il ON i.InvoiceID = il.InvoiceID
GROUP BY FORMAT(i.InvoiceDate, 'yyyy-MM')
ORDER BY Month
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
# Plotting the data as a line chart
plt.plot(df['Month'], df['ProfitMargin'], marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Profit Margin (%)')
plt.title('Monthly Profit Margins')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
# Close the connection
connection.close()
