
import csv
import mysql.connector
csv.field_size_limit(1048576)


# Open the CSV file in read mode
with open('/Volumes/roshan_1T/MAC/Documents/del_test/Nepaltoday23/databases_backup/output_directory/categories.csv', 'r') as csvfile:

    # Create a reader object
    reader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(reader, None)

    # Initialize MySQL connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='abc'
    )

    # Create a cursor
    cursor = connection.cursor()

    # Iterate over the CSV file in chunks
    chunk_size = 1000
    i = 0
    for chunk in iter(lambda: reader, []):

        # Initialize data list
        data = list(chunk)

        # Convert data to tuple
        data = tuple(data)

        # Insert the data into the MySQL database
        cursor.executemany(
            'INSERT INTO categories (id, category_type_id, name, description, image, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            data
        )
        
        # cursor.executemany(
        #     'INSERT INTO categories (id, category_id, title, article, image, visible, archieve, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
        #     data
        # )

        # Commit the changes to the database
        connection.commit()
        i = i + 1
        if i == 10:
            break

    # Close the cursor
    cursor.close()

    # Close the connection
    connection.close()
