# PyCharm Django E-Commerce App

Techmoto is an E-commerce Application built using the Python Django 2.8.8 and PyCharm

Available Features

- [x] Lists products and categories.
- [x] Filter products based on different categories.
- [x] Functionality to search for items by name.
- [x] Multiple sort features based on rating, price, etc.
- [x] Adding products to the Shopping Cart
- [x] Mail Integration using twilio SendGrid
- [x] Secure Payment Gateway (Card, UPI, Paytm)
- [x] Package application in a Docker container
- [ ] Heroku Deployment

You can view a working version of this app
[here](https://youtu.be/Rr4EOIpiMnM)

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

## Licensing

This library is BSD-licensed.

