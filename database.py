import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'mulamuua1',
    'db': 'backend_test',
}

# Create a connection to the database
conn = MySQLdb.connect(**db_config)
