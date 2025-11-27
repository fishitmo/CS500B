import sqlite3

conn = sqlite3.connect("sales.db")
conn.execute(
"CREATE TABLE Sales (salesperson text, "
"amt currency, year integer, model text, new boolean)"
)

# Insert data into the Sales table
conn.execute("INSERT INTO Sales VALUES" "('Tim', 16000, 2010, 'Honda Fit', 'true')")
conn.execute("INSERT INTO Sales VALUES" "('Tim', 9000, 2006, 'Ford Focus', 'false')")
conn.execute("INSERT INTO Sales VALUES" "('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
conn.execute("INSERT INTO Sales VALUES" "('Gayle', 28000, 2009, 'Ford Mustang', 'true')")
conn.execute("INSERT INTO Sales VALUES" "('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
conn.execute("INSERT INTO Sales VALUES" "('Don', 20000, 2008, 'Toyota Prius', 'false')")

# Commit the changes and close the connection
conn.commit()
conn.close()

