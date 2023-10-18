#!/bin/bash

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
update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-tickets.git" "tickets" "master"
update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-backend.git" "metaservicesynced" "metasynced_module"
update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-settings.git" "conf" "master"
update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-webapp-design-template.git" "design_template" "unstable"
update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-webservice-running.git" "webservice_running" "unstable"
update_repository "https://git.sharix-app.org/ShariX_Open/sharix-open-landing.git" "landing" "landing_module"
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
python manage.py makemigrations SharixAdmin metaservicesynced tickets webservice_running landing
python manage.py migrate
python manage.py collectstatic -l --no-input

#cp conf/sharix_open.service /etc/systemd/system/