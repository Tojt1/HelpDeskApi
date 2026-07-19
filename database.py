import psycopg2

connection = psycopg2.connect("dbname=HelpDesk user=postgres host=localhost password=2910" )
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
               "email Varchar(255) UNIQUE NOT NULL,"
               "password TEXT,"
               "role TEXT CHECK (role IN ('CUSTOMER', 'ADMIN')),"
               "active boolean DEFAULT true,"
               "created timestamptz DEFAULT now())")

connection.commit()
cursor.close()
connection.close()