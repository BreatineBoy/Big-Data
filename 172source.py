import sqlite3

books = "C:\\Users\\sagec\\OneDrive\\Desktop\\Hw12\\books.db"

connection = sqlite3.connect(books)

import pandas as pd

pd.options.display.max_columns = 10

authors = pd.read_sql('SELECT * FROM authors',connection,index_col=['id'])
print(authors)

titles = pd.read_sql('SELECT * FROM titles', connection)
print(titles)

df = pd.read_sql('SELECT * FROM author_ISBN', connection)
print(df.head())

specific_columns = pd.read_sql('SELECT first, last FROM authors',connection)
print(specific_columns)

where_2016 = pd.read_sql("""SELECT title, edition, copyright
FROM titles
WHERE copyright > 2016""",connection)
print(where_2016)

authors_startw_D = pd.read_sql("""SELECT id, first, last
FROM authors
WHERE last LIKE 'D%'""",connection,index_col=['id'])
print(authors_startw_D)

second_charB = pd.read_sql("""SELECT id, first, last
FROM authors
WHERE first LIKE '_b%'""", connection, index_col=['id'])
print(second_charB)

order_by_clause = pd.read_sql('SELECT title FROM titles ORDER BY title ASC',
                              connection)
print(order_by_clause)

sort_mult_col = pd.read_sql("""SELECT id, first, last
FROM authors
ORDER BY last, first""",connection,index_col=['id'])
print(sort_mult_col)

sort_mult_colASC = pd.read_sql("""SELECT id, first, last
FROM authors
ORDER BY last DESC, first ASC""",connection,index_col=['id'])
print(sort_mult_colASC)

where_and_order = pd.read_sql("""SELECT isbn, title, edition, copyright
FROM titles
WHERE title LIKE '%How to Program'
ORDER BY title""", connection)
print(where_and_order)

inner_join = pd.read_sql("""SELECT first, last, isbn
FROM authors
INNER JOIN author_ISBN
    ON authors.id = author_ISBN.id
ORDER BY last, first""",connection)
print(inner_join.head())

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
VALUES ('Sue', 'Red')""")
insert = pd.read_sql('SELECT id, first, last FROM authors',
                     connection, index_col=['id'])
print(insert)

cursor = cursor.execute("""UPDATE authors SET last='Black'
WHERE last='Red' AND first='Sue'""")
update = pd.read_sql('SELECT id, first, last FROM authors',
                     connection,index_col=['id'])
print(update)

cursor = cursor.execute('DELETE FROM authors WHERE id=6')
print(pd.read_sql('SELECT id, first, last FROM authors',
                  connection,index_col=['id']))
