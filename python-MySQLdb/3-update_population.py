#!/usr/bin/env python3

# # update the population of a state in the`states` table
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

    # Execute the query update population
query="UPDATE states SET population = %s WHERE id = %s"
cursor.execute(query, (argv[4], argv[5]))
    # print(cursor.rowcount)
conn.commit()
# Fetch all the results of the query50
states = cursor.fetchall()

# Print the results
for state in states:
    print(state)

# Close the cursor and database connection
cursor.close()
conn.close()










# import sys
# import MySQLdb

# # updates the population of a state in the
# # `states` table in the database `US_States`

# if __name__ == "__main__":
#     username = sys.argv[1]
#     password = sys.argv[2]
#     dbname = sys.argv[3]
#     state_id = sys.arg[4]
#     new_population = sys.argv[5]

# db = MySQLdb.connect(
#     host = "localhost",
#     user = "root",
#     password= "password",
#     db = "US_States"
# )

# cursor = db.cursor()

# cursor.execute("UPDATE")

# results = cursor.fetchall()

# for result in results:
#     print(result)
    
# cursor.close()
# db.close()