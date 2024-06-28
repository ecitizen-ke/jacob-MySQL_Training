# deletes a state from the `states` table in the
# database `US_States`
if __name__ == "__main__":
    import mysql.connector
    from sys import argv

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user=argv[1],
    password=argv[2],
    database=argv[3],
    port=3306
    )
    
    # Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the SQL query to delete the state
query = "DELETE FROM states WHERE id = %s"
cursor.execute(query, ([argv[4]]))
        
# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()


