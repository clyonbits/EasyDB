# EasyDB
a simple key-value db
---
initialize a db:
```python
from easydb import EasyDB
db = EasyDB("database")
```
---
create a key:
```py
db.create("key", "value")
```
---
read a value from key:
```py
value = db.read("key")
print(value)
```
---
update a key:
```py
db.update("key", "new value")
```
---
delete a key:
```py
db.delete("key")
```