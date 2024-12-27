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
# SQL Query to fetch customer geographic distribution based on total 
# SQL Query to fetch employee sales performance
query = """
SELECT p.FullName, SUM(i.TotalDryItems + i.TotalChillerItems) as 
Sales
FROM Sales.Invoices i
JOIN Application.People p ON i.SalespersonPersonID = p.PersonID
GROUP BY p.FullName
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
print(df)
# Plotting the data as a pie chart
plt.figure(figsize=(10, 8))
plt.pie(df['Sales'], labels=df['FullName'], autopct='%1.1f%%', 
startangle=90)
plt.title('Employee Sales Performance')
plt.axis('equal') # Equal aspect ratio ensures the pie chart is circular
plt.show()
# Close the connection
connection.close()
# Close the connection
connection.close()
