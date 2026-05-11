class Config:
    DBNAME = "test_db"
    USER = "postgres"
    PASSWORD = "m0rg3n"

    def __init__(self, dbname="test_db",
                 user="postgres",
                 password="m0rg3n"):
        self.USER = user
        self.PASSWORD = password
        self.DBNAME = dbname