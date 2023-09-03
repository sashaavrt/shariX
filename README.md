# ShariX Open Webapp Base

The base Django project of a service web application to which other modules are connected.

## Installation

Download or clone repository.

For the initial configuration, run:

- *bin/install.sh* - on Unix.
- *bin/install.bat* - on Windows.

## Configuration

After executing the installation script, the file *core/_config.py* will be copied to the *core/config.py* (only if *core/config.py* does not exist yet). It contains default settings of all modules and applications used in Django project in the form of classes, where each attribute represents one setting. These classes are then used to apply all the necessary settings inside their own configuration files using the setup() function. 

For example, this is how all the customizations for Gunicorn are defined in the *core/config.py* file:

```python
# core/config.py

class ConfigGunicorn:
    bind = "127.0.0.1"
    workers = 2
    worker_class = "sync"
    threads = 4
    timeout = 30
    max_requests = 1000
    capture_output = True
```

And this is how these settings are applied in the *core/gunicorn.py* configuration file used when starting Gunicorn:

```python
# core/gunicorn.py

from core.utils import setup
from core.config import ConfigGunicorn

setup(locals(), ConfigGunicorn)
```

This approach provides more convenient project configuration and allows you to store settings for development and production use.

To configure special settings, such as changing the database type or specifying domain names for deployment in production that do not match the default settings for the web application, make changes to the *core/config.py* file. If these changes later become necessary for the basic installation of the web application, they should also be made in *core/_config.py*.

To apply your own classes with configurations, follow the usage example above.

## Launch 

To start the web application on Unix, run *bin/start.sh*.
