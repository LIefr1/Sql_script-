import mysql.connector
from mysql.connector import Error

def create_connection(host_name,db_name, user_name, user_passsword):
    conn = None
    try:
        conn = mysql.connector.connect(
            host = host_name,
            database = db_name,
            user = user_name,
            passwd = user_passsword
        )
        print("Connection Ok")
    except Error as e:
        print(f"Error '{e}' has occurred")
    return conn

def execte_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}' has occurred")


connection = create_connection('5.183.188.132',"db_vgu_test" , 'db_vgu_student', "thasrCt3pKYWAYcK")
select_category= "SELECT * FROM category"
affiliate = execte_read_query(connection, select_category)

for a in affiliate:
    print(a)