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

# SQL Query to fetch the number of orders per customer
query = """SELECT CustomerID, COUNT(*) as NumberOfOrders FROM 
Sales.Orders GROUP BY CustomerID"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
print(df)
# Plotting the data as a bar chart
plt.bar(df['CustomerID'], df['NumberOfOrders'])
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.title('Orders per Customer')
plt.show()

# Close the connection
connection.close()