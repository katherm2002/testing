import mariadb
print(mariadb.__version__)

connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="metropolia12",
    database="duckburg",
    autocommit=True
)
print("Connection established successfully")

def get_duckburger_by_last_name(connection, last_name):
    sql = "SELECT * FROM duckburger WHERE LastName = Ankka "
    cursor = connection.cursor()
    cursor.execute(sql, (last_name,))
    result = cursor.fetchall()
    if result:
        for a in result:
            print(f"{a[0]} is {a[1]}")