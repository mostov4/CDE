import pymysql
from pymysql import cursors
​
def create_connection():
    connection = pymysql.connect(host='localhost',
                            user='qG744OmI8A',
                            password='root',
                            database='Books',
                            cursorclass=pymysql.cursors.DictCursor)
    return connection    
​
# create new table using execute command
# table query
query = '''CREATE TABLE `names` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB
AUTO_INCREMENT=1 ;'''
​
connection = create_connection()
​
with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
​
records = [
    ("Abid","abid@gmail.com"),
    ("Sher Zaman","sher@gmail.com")]
# insert records  
connection = create_connection()
with connection:
        with connection.cursor() as cursor:
            query = "INSERT INTO `names` (`name`, `email`) VALUES  (%s, %s)"
            cursor.executemany(query, records)
            print(f'The query affected {cursor.rowcount} rows')
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
​
connection = create_connection()
​
with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `names`"
            cursor.execute(sql)
            print(f'The query affected {cursor.rowcount} rows')
​
            rows = cursor.fetchall()
            print(f'{rows}')