# little_lemon_restaurant_backend
Website Backend for A Restaurant called Little Lemon

## Commands that Usually Used (On Windows OS)
### Virtual Enviroment
**Install the Virtual Environment:** pip3 install virtualenv <br />
**Init Vritual Environment:** python -m venv **your_project_name** <br />
**Activate Virtual Environment:** .\your_project_name\Scripts\Activate.ps1 <br />
**Deactivate Virtual Environment:** deactivate <br />

### Django Related
**Install Django:** pip3 install django <br />
**Create a Django Project:** django-admin startproject project_name <br />
**Create an App:** python manage.py startapp app_name <br />
**Run Django Server:** python manage.py runserver <br />
**Open Django Shell in Cmdline:** python manage.py shell <br />

### Database Related
**Add a New Model or Effect Changes:** python manage.py makemigrations <br />
**Migrating Models of Installed Apps(Apply the Tasks in the Migration File):** python manage.py migrate <br />
**Revert Back to a Specific Version:** python manage.py migrate app_name migration_file_name <br />
**There are Two Unmigrated Changes in the Model, Run:** python manage.py showmigrations <br />
**Shows the SQL Query or Queries Executed:** python manage.py sqlmigrate app_name migration_file_name