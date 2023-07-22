Create Django Project:
----------------------
django-admin.py startproject project_name (. for creating in root directory otherwise it creates as a seperate directory).
 or
python -m django startproject profiles_projects

================================================================================================================================
Create Django Application or Api:
---------------------------------
python manage.py startapp profiles_api

================================================================================================================================
To enable tha application:
--------------------------
Open the settings.py file of the root project (profiles_projects) and add the following under installed apps:
rest_framework
rest_framework.authtoken
profiles_api

================================================================================================================================
Run django project:
-------------------
python manage.py runserver (0.0.0.0:8000 specify the server and port)

================================================================================================================================

