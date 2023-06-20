# ShariX Open Admin

Admin system implemented as a Django application.

## How install?

1) Download or clone repository
```bash
git clone http://git.sharix-app.org/ShariX_Open/sharix-open-webapp-base.git name_project
```
1) Set up a configuration file
```python
#Create file config.py with this setting or rename this file to config.py

#BASE
DEBUG=True
SECRET_KEY='secret-key(absolutely any character)'
ALLOWED_HOSTS = ['127.0.0.1']
CSRF_TRUSTED_ORIGINS = []
API_URL = "127.0.0.1"
#DRIVE=2;ASSIST=1
SERVICE_ID = 1
#DATABSE
DB_NAME=None
DB_USER=None
DB_PASSWORD=None
DB_HOST=None

#GUNICORN
BIND = "127.0.0.1:8000"
WORKERS = 2
THREADS = 4

#STATIC
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
[BASE_DIR / "SharixAdmin/static/", BASE_DIR / "tickets/static/", BASE_DIR /"design_template/static"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
3) Run a **install_win.bat**
4) The system will prompt you to create a superuser
```
#Example
7987654321
admin
pa$$w0rd
pa$$w0rd
```
### Ready!

## Server instalation
1) Download or clone repository
```bash
git clone http://git.sharix-app.org/ShariX_Open/sharix-open-webapp-base.git name_project
```
2) Set up a configuration file ```nano core/config_template.py```
```python
#Create file config.py with this setting or rename this file to config.py

#BASE
DEBUG=True
SECRET_KEY='secret-key(absolutely any character)'
ALLOWED_HOSTS = ['127.0.0.1']
CSRF_TRUSTED_ORIGINS = []

#DATABSE
DB_NAME=None
DB_USER=None
DB_PASSWORD=None
DB_HOST=None

#GUNICORN
BIND = "127.0.0.1:8000"
WORKERS = 2
THREADS = 4

#STATIC
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "SharixAdmin/static/", BASE_DIR / "tickets/static/"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
3) Run a **install_linux.sh**
4) The system will prompt you to create a superuser
```
#Example
7987654321
admin
pa$$w0rd
pa$$w0rd
```
5) Set up the **bin/webuser.sh** file with valid paths
```bash
#!/bin/bash
cd /path/to/project
exec /path/to/project/env/bin/gunicorn core.wsgi:application -c core/conf_gunicorn.py
```
6) It remains to configure Nginx conf and start the daemon

## Settings

Optional configuration params, which can be added to your project settings:

```python

```

## Utilities

Utilities provides important functionality to web-application, so it is important to know and understand how they work. They are stored in *core/utils*.

### AuthAPI

That class provides the ability to authenticate an application account through the
API and store these authentication tokens.

Modules using the API should log in ShariX system using this class.

#### Setting up

```python
# core/config.py

# ...
#API
# The URL where it is possible to access the API.
API_URL = 'http://127.0.0.1:8000'
# ...
```

```python
# <module>/apps.py

# ...
from core.utils.AuthAPI import AuthAPI
api = AuthAPI("<module_login>", "<module_password>")
# ...
```

#### Usage example

```python
# <module>/<file>.py

import requests
from <module>.apps import api
from core.config import API_URL

# You can use api.headers to get the corret authorization header in your requests.
requests.get(f"{API_URL}/tickets/api/tickets/", headers=api.headers)

# Or you can get just token.
print(api.token)
```