import psycopg2
from access import host, user, password, db_name

connection = None

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    # the cursor for performing database operations
    # cursor = connection.cursor()

    # create a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE info_table(
            id serial PRIMARY KEY,
            language varchar(50),
            topic varchar(50),
            explanation varchar(250));
            """
        )
        print("[INFO] Table created successfully")

    # insert data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO info_table (data) VALUES
    #         ;"""
    #     )
    #     print("[INFO] Data was successfully inserted")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT data FROM  WHERE ;"""
    #     )
    #     print(cursor.fetchone())

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
