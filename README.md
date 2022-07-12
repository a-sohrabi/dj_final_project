# Django online shop
A shopping website using Django, Django Rest Framework and Vue.js


## Django setup
 Clone the Project
* `git clone https://github.com/a-sohrabi/dj_final_project.git`

 Create a Virtual Environment(You can choose any name instead of "venv").
* `virtualenv venv`

 Activate the Interpreter of the Virtual Environment
* Windows: `venv\Script\activate`
* Linux: `source venv/bin/activate`

 Install the Requirements
* `pip install -r requirements.txt`

 Adjust the Data Base Amount in `settings.py` File in `final_project` Directory

 Write the Following Command to Create Media Directory
* `mkdir media`

 Write the Following Command to Create Your Tables
* `python manage.py migrate`

 Write the Following Command to Create a Superuser
* `python manage.py createsuperuser`

 Write the Following Command to Run the Server
* `python manage.py runserver`


### Vue setup

```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


