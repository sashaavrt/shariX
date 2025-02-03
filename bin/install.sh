#!/bin/bash

if [ -f bin/install.cfg ]; then
    echo "File install.cfg already exists"
else
    attempts=0
    max_attempts=3

    while [ $attempts -lt $max_attempts ]; do
        read -p "File install.cfg does not exist. Do you want to create it? (y/n) [default: y]: " answer

        if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
            cp bin/install.cfg.example bin/install.cfg
            echo "File install.cfg was successfully created"
            exit 0
        elif [[ "$answer" == "n" || "$answer" == "N" ]]; then
            echo "Error: You need to create the file manually and then continue."
            echo "cp /bin/install.cfg.example to /bin/install.cfg with your settings."
            exit 1
        else
            attempts=$((attempts + 1))
            echo "Invalid input. Please enter 'y' or 'n'. Attempt $attempts of $max_attempts."
        fi
    done

    echo "Exceeded maximum attempts. Exiting."
    exit 1
fi

source bin/install.cfg

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
update_repository "$TICKETS"            "tickets"            "$TICKETS_BRANCH"
update_repository "$BACKEND"            "dbsynce"            "$BACKEND_BRANCH"
update_repository "$CONFIG"             "conf"               "$CONFIG_BRANCH"
update_repository "$DESIGN_TEMPLATE"    "design_template"    "$DESIGN_TEMPLATE_BRANCH"
update_repository "$WEBSERVICE_RUNNING" "webservice_running" "$WEBSERVICE_RUNNING_BRANCH"
update_repository "$LANDING"            "landing"            "$LANDING_BRANCH"
update_repository "$USER_MODEL"         "user"               "$USER_MODEL_BRANCH"
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
    echo "Write the connection settings for the PostgreSQL database."
    exit
fi

# Run Django migrations and other commands
python manage.py makemigrations dbsynce tickets webservice_running landing user
python manage.py migrate
python manage.py collectstatic -l --no-input

#cp conf/sharix_open.service /etc/systemd/system/