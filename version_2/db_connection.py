import psycopg2
from access import HOST, USER, PASSWORD, DB_NAME

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
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO info_table (language, topic, explanation) VALUES ('Python', 'str', 'In Python,
    #         the str (string) is a built-in data type that represents a sequence of characters. It is used to store
    #         and manipulate textual data, such as words, sentences, and paragraphs. Strings are one of the fundamental
    #         data types in Python and are treated as objects.Strings can be defined using single or double
    #         quotes.Strings in Python are immutable, meaning once created, their contents cannot be changed. However,
    #         you can create new strings by manipulating existing ones.Some common string operations and methods
    #         include:1.Concatenation, 2.Indexing, 3.Slicing, 4.String methods');"""
    #     )
    # print("[INFO] Data was successfully inserted")

    # select data
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT explanation FROM info_table  WHERE language = 'Python' AND topic = 'str';"""
        )
        print(cursor.fetchone())

    # Delete data
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DELETE FROM info_table
    #         WHERE language = 'Python';"""
    #     )

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

a = 'In Python, the str (string) is a built-in data type that represents a sequence of characters. It is used to ' \
    'store and manipulate textual data, such as words, sentences, and paragraphs. Strings are one of the fundamental ' \
    'data types in Python and are treated as objects.Strings can be defined using single or doublequotes.Strings in ' \
    'Python are immutable, meaning once created, their contents cannot be changed. However, you can create new ' \
    'strings by manipulating existing ones.Some common string operations and methods include:1. Concatenation, ' \
    '2. Indexing, 3. Slicing, 4. String methods '
count = 0
for i in a:
    count += 1
print(count)