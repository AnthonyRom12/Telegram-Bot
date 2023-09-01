import psycopg2
from access import HOST, USER, PASSWORD, DB_NAME


def get_info_from_db(language, topic: str):
    connection = None
    try:
        connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        cursor = connection.cursor()
        cursor.execute(
            f"SELECT explanation FROM info_table WHERE language = %s AND topic = %s;", (language, topic)
        )
        info = cursor.fetchone()
        cursor.close()
        return info[0] if info else None
    except Exception as ex:
        print("[INFO] Error while working with DataBase", ex)
        return None
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")
