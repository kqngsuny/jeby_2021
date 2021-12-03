@echo off

cd d:/workspace/jeby_2021/mysite

python manage.py migrate %1 --settings=config.settings.local