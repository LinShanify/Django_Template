# A Basic Django Template: Blog

A basic Django template with Bootstrap 4, SQlite include user registry, login, forgot password.

This template follow Corey Schafer's youtube tutorials [Link](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

### __Setup__
* `git clone https://github.com/LinShanify/Django_Template.git` or download the zip
* `pip install -r requirements.txt`

### __Email Setting__
Edit the ``~/.bash_profile` file with your email address and password
```bash
export EMAIL_USER="yourgmail@gmail.com"
export EMAIL_PASS="yourpassword"
export DJANGO_SECRET_KEY="keys"
```

### __Runing__
```bash
cd django_template 
python manage.py runserver 
```
open http://localhost:8000
