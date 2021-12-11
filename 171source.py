import sqlite3

books = "books.db"

connection = sqlite3.connect(books)

import pandas as pd

"""
    a) select authors last names descending order
    b) book titles in ascending order
    c) INNER JOIN to select books of specific author. Include title,
        copyright, isbn. Order alphabetically
    d) insert new author into authors table
    e) insert a new title for an author. must have author_ISBN entry,
        and an entry in titles table
"""

a = pd.read_sql("""SELECT last FROM authors
ORDER BY last DESC""", connection)
print(a)

b = pd.read_sql("""SELECT *
FROM titles
ORDER BY title ASC""", connection)
print(b)


c = pd.read_sql("""SELECT titles.title, titles.copyright, author_isbn.isbn
FROM titles INNER JOIN author_isbn ON titles.isbn = author_ISBN.isbn
INNER JOIN authors ON authors.id = author_ISBN.id
WHERE authors.first = 'Paul' AND authors.last = 'Deitel'
ORDER BY titles.title ASC""", connection)
print(c)

def d():
    d = connection.cursor()
    d.execute("""INSERT INTO authors(first,last) VALUES('Sage', 'Cooper')""")
    insert = pd.read_sql('SELECT * FROM authors',connection)
    print(insert)
d()

def e():
    e = connection.cursor()
    e.execute('INSERT INTO author_isbn(id,isbn) VALUES(6,0123456789)')
    e.execute("""INSERT INTO titles(isbn,title,edition,copyright) VALUES(0123456789, 'Sages Book', 1, 2021)""")
    pd.read_sql('SELECT * FROM titles', connection)
e()