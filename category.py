# import csv
# import mysql.connector


# def chunk_data(data, chunk_size):
#     """
#     Chunks the data into smaller chunks.

#     Args:
#         data (list): The data to chunk.
#         chunk_size (int): The size of each chunk.

#     Returns:
#         list: A list of chunks.
#     """

#     chunks = []
#     i = 0
#     while i < len(data):
#         chunk = data[i:i + chunk_size]
#         chunks.append(chunk)
#         i += chunk_size

#     return chunks


# def main():
#     """
#     Main function.
#     """

#     # Open the CSV file in read mode
#     with open('/Volumes/roshan_1T/MAC/Documents/del_test/Nepaltoday23/databases_backup/output_directory/articles.csv', 'r') as csvfile:

#         # Create a reader object
#         reader = csv.reader(csvfile, delimiter=',')

#         # Skip header
#         next(reader, None)

#         # Initialize MySQL connection
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='password',
#             database='abc'
#         )

#         # Create a cursor
#         cursor = connection.cursor()

#         # Chunk the data
#         data = list(reader)
#         chunks = chunk_data(data, 1000)

#         # Iterate over the chunks
#         for chunk in chunks:

#             # Insert the data into the MySQL database
#             cursor.executemany(
#                 'INSERT INTO articles (id, category_id, title, article, image, visible, archieve, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
#                 chunk
#             )

#             # Commit the changes to the database
#             connection.commit()

#         # Close the cursor
#         cursor.close()

#         # Close the connection
#         connection.close()


# if __name__ == '__main__':
#     main()


import csv
import mysql.connector
csv.field_size_limit(1048576)


# Open the CSV file in read mode
with open('/Volumes/roshan_1T/MAC/Documents/del_test/Nepaltoday23/databases_backup/output_directory/sqlite_sequence.csv', 'r') as csvfile:

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
            'INSERT INTO sqlite_sequence (name,seq) VALUES (%s,%s)',
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
