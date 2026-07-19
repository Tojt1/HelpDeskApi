import psycopg2

connection = psycopg2.connect("dbname=HelpDesk user=postgres host=localhost password=2910" )
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
               "email Varchar(255) UNIQUE NOT NULL,"
               "password TEXT,"
               "role TEXT CHECK (role IN ('CUSTOMER', 'ADMIN')),"
               "active boolean DEFAULT true,"
               "created timestamptz DEFAULT now())")

cursor.execute("CREATE TABLE IF NOT EXISTS tickets (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
               "title TEXT,"
               "description TEXT,"
               "status TEXT CHECK (status IN ('OPEN', 'IN_PROGRESS', 'CLOSED')),"
               "priority INTEGER, "
               "category TEXT,"
               "author_id INTEGER,"
               "agent_id INTEGER, "
               "created timestamptz DEFAULT now(),"
               "updated timestamptz,"
               "closed timestamptz, "
               ""
               "FOREIGN KEY (author_id) REFERENCES users(id),"
               "FOREIGN KEY (agent_id) REFERENCES users(id) )")

cursor.execute("CREATE TABLE IF NOT EXISTS comment (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, "
               "content TEXT,"
               "ticket_id INTEGER,"
               "agent_id INTEGER,"
               "created timestamptz)")

connection.commit()
cursor.close()
connection.close()