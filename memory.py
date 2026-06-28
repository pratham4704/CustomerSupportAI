import sqlite3

DATABASE = "database/memory.db"


def initialize_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS conversation(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer TEXT,

        query TEXT,

        response TEXT

    )

    """)

    conn.commit()

    conn.close()


initialize_database()


def save_conversation(customer, query, response):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO conversation(

        customer,

        query,

        response

    )

    VALUES(?,?,?)

    """,

    (

        customer,

        query,

        response

    )

    )

    conn.commit()

    conn.close()


def get_previous_issue(customer):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT query

    FROM conversation

    WHERE customer=?

    ORDER BY id DESC

    LIMIT 1

    """,

    (

        customer,

    )

    )

    row = cursor.fetchone()

    conn.close()

    if row:

        return row[0]

    return "No previous support issue found."