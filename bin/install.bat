@echo off

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

REM Update repositories
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git" "tickets" "master"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git" "metaservicesynced" "metasynced_module"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-webadmin.git" "SharixAdmin\templates\SharixAdmin" "webinterface"
call :update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-config.git" "conf" "master"

git pull

REM Create a Python virtual environment and activate it
python -m venv venv
.\venv\Scripts\activate

REM Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

REM Checking for core/config.py
if exist core\config.py (
    echo File config.py already created
) else (
    copy core\_config.py core\config.py
    echo File config.py was successfully created
)

REM Run Django migrations and other commands
python manage.py makemigrations SharixAdmin metaservicesynced tickets
python manage.py migrate
python manage.py collectstatic --clear --no-input