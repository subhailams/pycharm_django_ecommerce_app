# PyCharm Django E-Commerce App - TEAM HOPE

Video Demo : https://youtu.be/Rr4EOIpiMnM

Techmoto is an E-commerce Application built using the Python Django 2.8.8 and PyCharm

Available Features

- [x] Lists products and categories.
- [x] Filter products based on different categories.
- [x] Functionality to search for items by name.
- [x] Multiple sort features based on rating, price, etc.
- [x] Adding products to the Shopping Cart
- [x] Mail Integration using twilio SendGrid
- [x] Secure Payment Gateway (Card, UPI, Paytm)
- [x] Package application in a Docker container (subhailamathy/techmoto:latest)
- [x] Heroku Deployment [View App](https://tech--moto2020.herokuapp.com/)

Technology Used:
* Backend - Python, Javascript,  Django, Django REST API, DbSQLite, Ngnix, Gunicorn, Docker
* Frontend - HTML, CSS, Bootstrap, Javascript


You can view a working version of this app [here](https://tech--moto2020.herokuapp.com/)
Admin Username : narmusanjay@gmail.com
      Password : Narmadha@1926

Running this app on your local machine in development will work as
well by following the steps below:


```
mkdir django_app
cd django_app
git clone https://github.com/subhailams/pycharm_django_ecommerce_app.git
```

Open the Project in Pycharm Professional Edition and create virtual environment

```
cd pycharm_django_ecommerce_app/
pip install -r requirements.txt
```
Create Superuser as admin with username and password
```
python manage.py createsuperuser
```

Now run the server using below command
```
python manage.py runserver
```

Starting development server at http://127.0.0.1:8000/

```
python manage.py createsuperuser
```

Products can be added to the database using http://127.0.0.1:8000/admin/

Project Structure
```
├───accounts
│   ├───migrations
│   ├───passwords
│   ├───templates
│   │   └───accounts
│   │       ├───registeration
│   │       └───snippets
│   │           └───emails
├───addresses
│   ├───migrations
│   │   
│   ├───templates
│   │   └───addresses
│   
├───analytics
│   ├───migrations
├───billing
│   ├───migrations
│   ├───templates
│   │   └───billing
├───cart
│   ├───migrations
│   ├───templates
│   │   └───carts
│   │       └───snippets
├───ecommerce
│   ├───aws
│   ├───migrations
│   ├───settings
├───orders
│   ├───migrations
│   ├───templates
│   │   └───orders
├───products
│   ├───fixtures
│   ├───migrations
│   ├───templates
│   │   └───products
│   │       └───snippets
├───search
│   ├───migrations
│   ├───templates
│   │   └───search
├───socialapp
│   ├───migrations
│   ├───templates
│   │   └───socialapp
├───static_my_proj
│   ├───css
│   ├───ecomjs
│   ├───images
│   └───js
└───templates
    ├───base
    ├───registeration
    │   └───emails
    ├───Rock_Salt
    └───temp
|__ manage.py
|__ requirements.txt
|__ Dockerfile
|__ Readme.md
```
## Licensing

This library is BSD-licensed.

