import sys
import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "sam-pson12",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "library")

    cursor = connection.cursor()
    f = open('schema.sql', 'r')
    reader = str(f.read())
    commands = reader.split('**')
    for command in commands:
        cursor.execute(command)


    # open seeding file and add records
    ff = open("seeder.sql","r")
    seeder_reader = str(ff.read())
    seeder_commands = seeder_reader.split('**')
    for command in seeder_commands:
        cursor.execute(command)


    cursor.close()
    #commit the changes
    connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

