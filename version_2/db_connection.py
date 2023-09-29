import psycopg2
from access import HOST, USER, PASSWORD, DB_NAME
import re

connection = None

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    connection.autocommit = True

    # the cursor for performing database operations
    # cursor = connection.cursor()

    # create a new table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE info_table(
    #         id serial PRIMARY KEY,
    #         language varchar(50),
    #         topic varchar(50),
    #         explanation varchar(900));
    #         """
    #     )
    #     print("[INFO] Table created successfully")

    # insert data
    text = ('')
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    # count = 0
    # for i in text:
    #     count += 1
    # print(count)

    language = ''
    topic = ''

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO info_table (language, topic, explanation) VALUES (%s, %s, %s); """, (language, topic,
                                                                                                cleaned_text))
    print("[INFO] Data was successfully inserted")

    # select data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT explanation FROM info_table  WHERE language = 'Java' AND topic = 'str';"""
    #     )
    #     print(cursor.fetchone())

    # Delete data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM info_table
    #         WHERE language = 'Java' AND topic = 'bool' ;"""
    #     )
    # print("[INFO] DATA successfully deleted!")

    # Delete table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE info_table"""
    #     )
    # print("[INFO] Table was deleted")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")

