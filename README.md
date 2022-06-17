[![Django 4.0](https://bs-uploads.toptal.io/blackfish-uploads/components/blog_post_page/content/cover_image_file/cover_image/936807/retina_1708x683_cover-Redesign-DjangoMistakes-Luke_Newsletter-583fce40c721c48192c477deff31dc42-68f8b5b282f890fd6c1888a8e381f130.png)](https://www.codingforentrepreneurs.com/projects/try-django-22)


### Getting Started

#### Requirements
- Python 3.6 & up
- Virtual Environment (pipenv or virtualenv)

#### Recommended Prerequisites
- Coding with macOS (course)
    - https://cfe.sh/courses/coding-with-macOS
- 30 Days of Python (project)
    - https://cfe.sh/projects/30-days-python
- Getting Started with HTML & CSS (project)
    - https://cfe.sh/projects/getting-started-html-css
- Bootstrap Basics (project)
    - https://cfe.sh/projects/bootstrap-basics-v4-3


#### 1. Setup your System
- Windows: https://kirr.co/6r8wr9
- Mac: https://kirr.co/386c7f
- Linux: https://kirr.co/c3uvuu


#### 2. Create Virtual Environment & Install Django
```
cd /path/to/dev/folder
mkdir project_django
cd project_django
pipenv --python 3.8.3 install django==4.0
pipenv shell

OPTIONAL: 
pipenv install
```

#### 3. Create Django Project
```
cd /path/to/dev/folder
mkdir src
cd src
django-admin startproject try_django .
```

#### 4. Start the server
```
cd /path/to/dev/folder
cd src
python manage.py runserver
```

#### 5. Migration(s) to solidify it
```
cd /path/to/dev/folder
python manage.py migrate

python manage.py createsuperuser
```

#### 6. Create new superuser
```
cd /path/to/dev/folder/src
python manage.py migrate
python manage.py createsuperuser
```