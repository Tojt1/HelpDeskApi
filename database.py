import psycopg2
def create_connection():
    return psycopg2.connect("dbname=HelpDesk user=postgres host=localhost password=2910")

def create_tables():

    con = create_connection()
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                   "name TEXT NOT NULL,"
                   "email Varchar(255) UNIQUE NOT NULL,"
                   "password TEXT NOT NULL,"
                   "role TEXT CHECK (role IN ('CUSTOMER', 'ADMIN')) NOT NULL,"
                   "active boolean DEFAULT true,"
                   "created timestamptz DEFAULT now())")

    cursor.execute("CREATE TABLE IF NOT EXISTS tickets (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                   "title TEXT NOT NULL,"
                   "description TEXT,"
                   "status TEXT CHECK (status IN ('OPEN', 'IN_PROGRESS', 'CLOSED')) NOT NULL,"
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
                   "agent_id INTEGER,"
                   "created timestamptz)")

    con.commit()
    cursor.close()
    con.close()