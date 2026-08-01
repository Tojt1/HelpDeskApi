from psycopg2.pool import ThreadedConnectionPool
import config
import exceptions

pool = ThreadedConnectionPool(
    minconn= 2,
    maxconn=5,
    host=config.HOST,
    database=config.NAME,
    user = config.USER,
    password = config.PASSWORD
)


def create_tables():
    con = pool.getconn()
    try:
        with con.cursor() as cursor:

            cursor.execute("CREATE TABLE IF NOT EXISTS users (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                           "name TEXT NOT NULL,"
                           "email Varchar(255) UNIQUE NOT NULL,"
                           "password TEXT NOT NULL,"
                           "role TEXT CHECK (role IN ('CUSTOMER', 'ADMIN')) DEFAULT 'CUSTOMER'  NOT NULL,"
                           "active boolean DEFAULT true,"
                           "created timestamptz DEFAULT now())")

            cursor.execute("CREATE TABLE IF NOT EXISTS tickets (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                           "title TEXT NOT NULL,"
                           "description TEXT,"
                           "status TEXT CHECK (status IN ('OPEN', 'IN_PROGRESS', 'CLOSED')) DEFAULT 'OPEN' NOT NULL,"
                           "priority INTEGER, "
                           "category TEXT,"
                           "author_id INTEGER NOT NULL,"
                           "agent_id INTEGER, "
                           "created timestamptz DEFAULT now(),"
                           "updated timestamptz,"
                           "closed timestamptz, "
                           ""
                           "FOREIGN KEY (author_id) REFERENCES users(id),"
                           "FOREIGN KEY (agent_id) REFERENCES users(id) )")

            cursor.execute("CREATE TABLE IF NOT EXISTS comment (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, "
                           "content TEXT,"
                           "ticket_id INTEGER NOT NULL,"
                           "author_id INTEGER,"
                           "created timestamptz DEFAULT now(),"
                           ""
                           "FOREIGN KEY (author_id) REFERENCES users(id) )")

            con.commit()
    except Exception:
        con.rollback()
        raise exceptions.CreatinTablesError("Wystąpił błąd podczas tworzenia tabel")
    finally:
        pool.putconn(con)