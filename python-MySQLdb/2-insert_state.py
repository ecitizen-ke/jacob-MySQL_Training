#!/usr/bin/env python3

# insert a new state into the `states` table

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

# Execute the query to order states in ascending order
query = "INSERT INTO states (name, abbreviation,capital,population,year_admitted) VALUES (%s,%s,%s,%s,%s)"
cursor.execute(query, (argv[4], argv[5],"CITY",0,800))

if cursor.rowcount:
    conn.commit()
    print("success")
else:
    print("error")

# Fetch all the results of the query
states = cursor.fetchall()

# Print the results
for state in states:
        print(state)

# Close the cursor and database connection
cursor.close()
conn.close()


