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
value = db.get("key")
print(value)
```
---
create a value:
```py
db.create("key", "value")
```
