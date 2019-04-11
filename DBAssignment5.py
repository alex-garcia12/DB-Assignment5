import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Imawesome12!',
                             db='ART_GALLERY',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `Fname`, `Lname` FROM `ARTIST` ORDER BY Fname"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("ARTIST Table of Fname and Lname sorted by Fname:")
        print(result)

finally:
    connection.close()