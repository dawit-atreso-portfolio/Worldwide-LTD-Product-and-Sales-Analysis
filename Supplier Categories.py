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
# SQL Query to fetch the number of suppliers in each category
query = """
SELECT sc.SupplierCategoryName, COUNT(*) as NumberOfSuppliers
FROM Purchasing.Suppliers as s
JOIN Purchasing.SupplierCategories as sc ON s.SupplierCategoryID = 
sc.SupplierCategoryID
GROUP BY sc.SupplierCategoryName
"""
# Execute the query and store the result in a DataFrame
df = pd.read_sql(query, connection)
print(df)
# Plotting the data as a donut chart
plt.pie(df['NumberOfSuppliers'], labels=df['SupplierCategoryName'], 
autopct='%1.1f%%', startangle=90, pctdistance=0.85)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal') 
plt.title('Distribution of Suppliers by Category')
plt.show()

# close the connection
connection.close()