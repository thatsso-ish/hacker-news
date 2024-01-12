import sqlite3

class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    @classmethod
    def find(cls, post_id):
        sql_query = 'SELECT * FROM posts WHERE id = ?'
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute(sql_query, (post_id,))
        result = cursor.fetchone()
        connection.close()
        return None if not result else cls.build_record(result)

    @classmethod
    def all(cls):
        sql_query = 'SELECT * FROM posts'
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        connection.close()
        return [cls.build_record(result) for result in results]

    @classmethod
    def build_record(cls, row):
        return cls(row[0], row[1], row[2])

def create_table():
    DB.execute("DROP TABLE IF EXISTS `posts`;")
create_statement = "
    CREATE TABLE `posts` (
      `id`  INTEGER PRIMARY KEY AUTOINCREMENT,
      `title` TEXT,
      `url` TEXT,
      `votes`  INTEGER
    );"

def insert_post(post):
    DB.execute(create_statement)
DB.execute("INSERT INTO `posts` (title, url, votes) VALUES ('Le Wagon', 'www.lewagon.com', '9000')");
DB.execute("INSERT INTO `posts` (title, url, votes) VALUES ('GitHub', 'www.github.com', '1600')");
DB.execute("INSERT INTO `posts` (title, url, votes) VALUES ('Slack', 'www.slack.com', '4000')");
DB.execute("INSERT INTO `posts` (title, url, votes) VALUES ('Mozilla', 'www.mozilla.org', '3000')");
DB.execute("INSERT INTO `posts` (title, url, votes) VALUES ('Stackoverflow', 'www.stackoverflow.com', '4300')");
