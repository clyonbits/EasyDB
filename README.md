# EasyDB
a simple key-value db
---
initialize a db:
```python
from easydb import EasyDB
db = EasyDB("database")
```
---
get a value from key:
```py
value = db.read("key")
print(value)
```
---
create a key:
```py
db.create("key", "value")
```
