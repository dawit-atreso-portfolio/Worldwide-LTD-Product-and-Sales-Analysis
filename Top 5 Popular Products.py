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

query = """
SELECT TOP 5 StockItemID, COUNT(*) as Frequency
FROM Sales.OrderLines
GROUP BY StockItemID
ORDER BY COUNT(*) DESC
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
# Print the data to verify
print(df) 
# Plotting the data as a bar chart using Seaborn
sns.barplot(x='StockItemID', y='Frequency', data=df)
plt.title('Top 5 Popular Products')
plt.show()

# close the connection
connection.close()