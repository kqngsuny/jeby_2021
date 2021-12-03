@echo off

cd d:/workspace/jeby_2021/mysite

python manage.py makemigrations %1 --settings=config.settings.local