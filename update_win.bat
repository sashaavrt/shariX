@echo off
git pull
cd design_template && git pull && cd ..
cd tickets && git pull && cd ..
cd metaservicesynced && git pull && cd ..
cd webservice_running && git pull && cd .. 