# ShariX Open Admin

Admin system implemented as a Django application.

## How install?

1) Download or clone repository

```bash
git clone http://git.sharix-app.org/ShariX_Open/sharix-open-webapp-base.git name_project
```

2) Install with install_win.bat (for Windows) or install_linux.sh (for Linux)

If the installation is successful, the system will prompt you to create a superuser
1. Enter your phone number (required field)
2. Username (required field)
3. Email (optional)
4. Password (required field)
5. Repeat password (required field)
6. y - to agree if the password is too simple

3) To manually install the project, open the .bat file with a text editor and try these commands in the terminal

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
