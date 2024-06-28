#!/usr/bin/env python3

# lists all states from the database `US_States`

#checks if script is being run as the main module, prevents the code from being executed when imported
if __name__ == "__main__":
    import mysql.connector
    from sys import argv

    # Establish a database connection
    db = mysql.connector.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to order states in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results of the query
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
    
    
