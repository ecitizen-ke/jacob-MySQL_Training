#!/usr/bin/env python3

# # searche for a state by name
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

# Define the query (case-insensitive search)
query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
cursor.execute(query, ([argv[4]]))

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()


