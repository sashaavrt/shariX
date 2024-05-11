# ShariX Open Webapp Base

The base Django project of a service web application to which other modules are connected.

## Installation

Download or clone repository. For the initial configuration, run *bin/install.sh*.

## Configuration

For basic project configuration when deploying, use the *core/settings_vars.py*. This file is automatically created during the installation script execution, in case this file has not been created yet. It is a copy of *core/_settings_vars.py* and contains some default settings that allow the project to run locally and is more suitable for development.

Be careful when adding new settings during development and remember to add them to *core/_settings_vars.py*, as *core/settings_vars.py* is ignored by Git for security reasons.

You can also change the settings in *bin/install.cfg*. This file contains the links to repositories required for the project to work.

## Launch 

To start the web application, run *bin/start.sh*.
