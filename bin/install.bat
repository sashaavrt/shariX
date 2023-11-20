@echo off

REM Update repositories
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git" "tickets" "master"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git" "metaservicesynced" "metasynced_module"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-config.git" "conf" "master"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-webapp-design-template.git" "design_template" "unstable"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-webservice-running.git" "webservice_running" "unstable"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-landing.git" "landing" "landing_module"
git pull

REM Create a Python virtual environment and activate it
python -m venv venv
call venv\Scripts\activate

REM Upgrade pip and install requirements
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Checking for core/settings_vars.py
if exist core\settings_vars.py (
    echo File settings_vars.py already exists
) else (
    copy core\_settings_vars.py core\settings_vars.py
    echo File settings_vars.py was successfully created
)

REM Run Django migrations and other commands
python -m manage.py makemigrations SharixAdmin metaservicesynced tickets webservice_running landing
python -m manage.py migrate
python -m manage.py collectstatic --clear --no-input

goto :eof

REM Function to check if a repository exists and perform git pull or git clone
:update_repository
setlocal
set "repo_url=%~1"
set "repo_dir=%~2"
set "repo_branch=%~3"

if exist "%repo_dir%" (
    rem If the directory exists, then do a git pull
    echo Updating %repo_dir%...
    cd "%repo_dir%" || exit /b
    git pull
    cd ..
) else (
    rem If the directory does not exist, then do a git clone
    echo Cloning %repo_url% into %repo_dir%...
    git clone -b %repo_branch% %repo_url% %repo_dir%
)
endlocal
goto :eof