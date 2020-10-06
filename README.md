# Volunteerio Web API

## Development Instructions
### Create file name Secrets.py in API/ containing
```py
import os

dbpathl = os.path.join(os.path.abspath(os.path.dirname(__file__))).split("\\")
dbpath = ""
for sect in dbpathl[:-1]:
    dbpath += sect + "\\"

SecretKey = "VerySecret"

DatabaseURI = 'sqlite:///' + dbpath + '\\app.db'

SECURITY_PASSWORD_SALT = "This Is Your Salt"

```

