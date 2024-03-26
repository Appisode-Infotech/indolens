import pymysql.cursors

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    db="2_indolens_db",
    cursorclass=pymysql.cursors.DictCursor
)