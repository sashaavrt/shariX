# ShariX Open Webapp Base

The base Django project of a service web application to which other modules are connected.

## Installation / Upgrade

1. Download or clone repository.
2. Make a copy of configuration file (cp bin/install.cfg.example bin/install.cfg) and modify it for your service (check paths).
3. For the initial/update project configuration, run *bin/install.sh*.

### Test Users

During the installation/upgrade, you can pass the `TEST_USERS=true` is set
in the `install.cfg` file to automatically create test users. These users
will be assigned to the **TEST** group. Additionally, if the `DEBUG`
setting is enabled (`DEBUG=True` in *core/settings_vars.py*), these test
users will be marked as active and can log in. If `DEBUG` is disabled
(`DEBUG=False`), the users will be inactive and unable to log in.

#### Properties

- **Username:** `test-<group_name>-<ordinal_number_in_group>`.
- **Phone number:** `<group_id>0<ordinal_number_in_group>`.
- **Password:** All test users share the same password: `sharix-open-test`.

```bash
TEST_USERS=true
```

## Configuration

For basic project configuration when deploying, use the *core/settings_vars.py*. This file is automatically created during the installation script execution, in case this file has not been created yet. It is a copy of *core/_settings_vars.py* and contains some default settings that allow the project to run locally and is more suitable for development.

Be careful when adding new settings during development and remember to add them to *core/_settings_vars.py*, as *core/settings_vars.py* is ignored by Git for security reasons.

You can also change the settings in *bin/install.cfg*. This file contains the links to repositories required for the project to work.

## Launch 

To start the web application, run *bin/start.sh*.
