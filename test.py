from getpass import getpass 
from mysql.connector import connect, Error
try:
    with connect(
        host = '127.0.0.1',
        user = 'root',
        password = '123456',
        db = 'SOCIAL_NETWORK',   
    ) as connection:
        query = 'SELECT * FROM USER'
        
        with connection.cursor() as cursor:
            cursor.execute(query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)
    
print("test")