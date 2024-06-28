# count the number of states within
# a given population between 1,000,000 and 5,000,000 people

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

# SQL query to count the number of states with
# a population between 1,000,000 and 5,000,000 people
query = """
        SELECT COUNT(*)
        FROM states
        WHERE population BETWEEN %s AND %s
        """
cursor.execute(query, (argv[4],argv[5]))

results = cursor.fetchone()
print(results[0])
    
cursor.close()
conn.close()


