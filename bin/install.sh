#!/bin/bash

source bin/install.cfg

# Command line argument handler
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --test-users) 
            export TEST_USERS=true
            echo "Test users flag set"
            shift ;;
        *) 
            echo "Unknown parameter: $1"
            shift ;;
    esac
done

# Function to check if a repository exists and perform git pull or git clone
update_repository() {
    local repo_url="$1"
    local repo_dir="$2"
    local repo_branch="$3"

    if [ -d "$repo_dir" ]; then
        # If the directory exists, then do a git pull
        echo "Updating $repo_dir..."
        cd "$repo_dir" || exit
        git pull
        cd - || exit
    else
        # If the directory does not exist, then do a git clone
        echo "Cloning $repo_url into $repo_dir..."
        git clone -b "$repo_branch" "$repo_url" "$repo_dir"
    fi
}

# Update repositories
update_repository "$TICKETS" "tickets" "master"
update_repository "$BACKEND" "dbsynce" "metasynced_module"
update_repository "$CONFIG" "conf" "master"
update_repository "$DESIGN_TEMPLATE" "design_template" "unstable"
update_repository "$WEBSERVICE_RUNNING" "webservice_running" "unstable"
update_repository "$LANDING" "landing" "landing_module"
update_repository "$USER_MODEL" "user" "master"
update_repository "$WEBAPP_BASE" "design_template" "unstable"
git pull

# Create a Python virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Checking for core/settings_vars.py
if [ -f core/settings_vars.py ]; then
    echo "File settings_vars.py already exists"
else
    cp core/_settings_vars.py core/settings_vars.py
    echo "File settings_vars.py was successfully created"
fi

# Run Django migrations and other commands
python manage.py makemigrations dbsynce tickets webservice_running landing user
python manage.py migrate
python manage.py collectstatic -l --no-input

#cp conf/sharix_open.service /etc/systemd/system/