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

    text = 'In Python, inheritance is a core concept in OOP. It allows a subclass to inherit attributes and methods ' \
           'from a superclass. Key points: 1. Superclass and Subclass: Superclass provides, and subclass inherits. ' \
           'Subclass can modify inherited elements. 2. Code Reuse: Promotes code reuse by defining shared ' \
           'attributes/methods in the superclass. 3. Method Overriding: Subclasses can customize inherited methods. ' \
           '4. "is-a" Relationship: Models "is-a" relationships (e.g., Car is a Vehicle). 5. Base Class Features: ' \
           'Subclasses inherit but can add specific elements. Inheritance organizes code, encourages reuse, ' \
           'and models class relationships. '

    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    # count = 0
    # for i in text:
    #     count += 1
    # print(count)
    # print("=====================================")
    # print(cleaned_text)
    language = 'Python'
    topic = 'inheritance'
    # print("=====================================")
    # print(text)
    #
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO info_table (language, topic, explanation) VALUES (%s, %s, %s); """, (language, topic,
                                                                                                cleaned_text))
    print("[INFO] Data was successfully inserted")

    # select data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT explanation FROM info_table  WHERE language = 'Python' AND topic = 'str';"""
    #     )
    #     print(cursor.fetchone())

    # Delete data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM info_table
    #         WHERE language = 'Python' AND topic = 'while' ;"""
    #     )
    # print("[INFO] DATA successfully deleted!")

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
