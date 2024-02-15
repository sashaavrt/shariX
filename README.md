# ShariX Open Webapp Base

The base Django project of a service web application to which other modules are connected.

## Installation

Download or clone repository. For the initial configuration, run *bin/install.sh*.

## Configuration

For basic project configuration when deploying, use the *core/settings_vars.py*. This file is automatically created during the installation script execution, in case this file has not been created yet. It is a copy of *core/_settings_vars.py* and contains some default settings that allow the project to run locally and is more suitable for development.

Be careful when adding new settings during development and remember to add them to *core/_settings_vars.py*, as *core/settings_vars.py* is ignored by Git for security reasons.

Also you need to make this things with _config file. This file includes basic links for ShariXOpen.

## Utilities

Utilities provides important functionality to web-application, so it is important to know and understand how they work. They are stored in *core/utils*.

### AuthAPI

That class provides the ability to authenticate an application account through the
API and store these authentication tokens.

Modules using the API should log in ShariX system using this class.

#### Setting up

```python
# core/settings_vars.py

API_URL = 'http://127.0.0.1:8000'
```

```python
# <module>/apps.py

from core.utils.AuthAPI import AuthAPI
auth_api = AuthAPI("<module_login>", "<module_password>")
```

#### Usage example

```python
# <module>/<file>.py

import requests
from <module>.apps import auth_api 
from core.settings import API_URL

# You can use api.headers to get the corret authorization header in your requests.
requests.get(f"{API_URL}/tickets/api/tickets/", headers=auth_api.headers)

# Or you can get just token.
print(auth_api.token)
```

## Launch 

To start the web application, run *bin/start.sh*.
