import sqlite3

CREATE_TABLE = "CREATE TABLE dependencies (entity TEXT PRIMARY KEY, count INTEGER, heads TEXT)"
SELECT_WHERE = "SELECT * FROM dependencies WHERE entity=?"
SELECT = "SELECT * FROM dependencies"
INSERT = "INSERT INTO dependencies VALUES (?, ?, ?)"


class DatabaseConnection(object):

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename, check_same_thread=False)

    def create_schema(self):
        try:
            self.connection.execute(CREATE_TABLE)
        except sqlite3.OperationalError:
            print("Warning: 'dependencies' table was already created, ignoring...")

    def get(self, entity=None):
        cursor = (self.connection.execute(SELECT_WHERE, (entity,))
                  if entity is not None else self.connection.execute(SELECT))
        return cursor.fetchall()

    def add(self, entity, count, heads):
        try:
            self.connection.execute(INSERT, (entity, count, heads))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Warning: '%s' is already in the database, ignoring..." % entity)
            self.connection.rollback()