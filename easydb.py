EXTENSION = "easydb"
class EasyDB:
    def __init__(self, name):
        self.name = name
        self.filename = f"{self.name}.{EXTENSION}"
    
    def create(self, key, value):
        with open(self.filename, "a") as db:
            db.write(f"{key}:{value}\n")
    
    def read(self, key):
        with open(self.filename, "r") as db:
            if key == None:
                return "".join(db.readlines()).rstrip()
            for line in db:
                if line.split(":")[0] == key:
                    return line.split(":")[1].strip()
        return None

    def update(self, key, new_value):
        lines = []
        with open(self.filename, "r") as db:
            for line in db:
                if line.split(":")[0] == key:
                    lines.append(f"{key}:{new_value}\n")
                else:
                    lines.append(line)
        
        with open(self.filename, "w") as db:
            db.writelines(lines)
    
    def delete(self, key):
        with open(self.filename) as db:
            lines = db.readlines()
        for line in lines:
            if line.split(":")[0] == key:
                lines.remove(line)
        with open(self.filename, "w") as db:
            db.write("".join(lines))