EXTENSION = "easydb"
class EasyDB:
    def __init__(self, name):
        self.name = name
        self.filename = f"{self.name}.{EXTENSION}"
    def create(self, key, value):
        with open(self.filename, "w") as db:
            db.write(f"{key}:{value}")
    def read(self, key):
        with open(self.filename) as db:
            db_content = db.readlines()
            for line in db_content:
                if line.split(":")[0] == key:
                    return line.split(":")[1].rstrip()
                else:
                    return None