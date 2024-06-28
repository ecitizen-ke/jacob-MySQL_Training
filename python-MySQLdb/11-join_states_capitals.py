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

query = """
        SELECT states.name, capitals.capital_name
        FROM states
        JOIN capitals ON states.id = capitals.state_id
        ORDER BY states.id ASC
        """
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

cursor.close()
conn.close()


