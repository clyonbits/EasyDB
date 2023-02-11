EXTENSION = "easydb"
class EasyDB:
    def __init__(self, name):
        self.name = name
        self.filename = f"{self.name}.{EXTENSION}"
    def post(self, key, value):
        with open(self.filename, "w") as db:
            db.write(f"{key}:{value}")
    def get(self, key):
        with open(self.filename) as db:
            db_content = db.readlines()
            for line in db_content:
                if line.split(":")[0] == key:
                    return line.split(":")[1]
                else:
                    return None