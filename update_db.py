import json
import time
import mysql.connector

# Database connection setup

def update_db():
    db_config = {
    'database': 'detox_db_1',
    'user': 'ak_user',
    'password': 'ytterbium',
    'host': 'localhost',
    'port': 3306,
}
    # Load JSON data
    with open('activities.json', 'r') as file:
        data = json.load(file)

    # Connect to the MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Iterate over activities and update or insert into the database
    ignore = ["","\n"]
    for activity in data['activities']:
        appname = activity['name']
        if appname in ignore:
            continue
        timespent = activity['time_entries'][-1]['total_seconds']
        ondate = activity['time_entries'][-1]['date']
        
        # Check if the record exists
        check_query = """
        SELECT COUNT(*) FROM tracker_userdata
        WHERE appname = %s AND ondate = %s
        """
        cursor.execute(check_query, (appname, ondate))
        record_exists = cursor.fetchone()[0]
        
        if record_exists:
            # Update the existing record
            update_query = """
            UPDATE tracker_userdata
            SET timespent = %s
            WHERE appname = %s AND ondate = %s
            """
            cursor.execute(update_query, (timespent, appname, ondate))
        else:
            # Insert a new record
            insert_query = """
            INSERT INTO tracker_userdata (uid_id, appname, timespent, ondate)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (2, appname, timespent, ondate))  # Assuming uid is auto-incremented

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Database updated successfully.")

if __name__ == '__main__':
    while True:
        try:
            update_db()
            time.sleep(10)

        except KeyboardInterrupt:
            print("Stopping..")
            break

        except Exception as e:
            print(e)
            break
        
    print("Application closed")