# find the most populous state 
#checks if script is being run as the main module, prevents the code from being executed when imported
if __name__ == "__main__":
    import mysql.connector
    from sys import argv

# Establish a database connection
conn = mysql.connector.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL query to list all states admitted between 1750 and 1850, and after the given year
query = """
        SELECT name, year_admitted
        FROM states
        WHERE year_admitted BETWEEN 1750 AND 1850
        ORDER BY states.year_admitted ASC
        """
        
cursor.execute(query)

results = cursor.fetchall()

for result in results:
    print(result)
    
cursor.close()
conn.close()


