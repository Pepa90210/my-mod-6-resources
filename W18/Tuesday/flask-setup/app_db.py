import sqlite3

DB_FILE = "dev.db"

# with sqlite3.connect(DB_FILE) as conn:
#   curs = conn.cursor()
#   curs.execute(
#     """
#     CREATE TABLE joke(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     joke_body VARCHAR(250),
#     punchline VARCHAR(250),
#     rating VARCHAR(15)
#     );
#     """
#   )

def create_joke(joke_body, punchline, rating):
  with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute(
      """
      INSERT INTO jokes(joke_body, punchline, rating)
      VALUE(:joke_body, :punchline, :rating)
      """,
      {
        "joke_body": joke_body,
        "punchline": punchline,
        "rating": rating
      }
    )

# create_joke(
#   "Why did the scarecrow get a promotion?",
#   "He was outstanding in his field",
#   "G"
# )

def get_all_jokes():
  with sqlite3.connect(DB_FILE) as conn:
    curs = conn.cursor()
    curs.execute(
      """
      SELECT *
      FROM jokes;
      """
    )
    results = curs.fetchall()
    print(results)
