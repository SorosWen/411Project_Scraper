# 411 Project

## How to run
### Install dependencies
You need suffiently updated python3 and pip to run this project.
In the desired place where you want to place this project, run these commands:
```
git clone https://github.com/SorosWen/411project
cd 411project
pip install -r requirements.txt
```

### Run the server
```
cd prototype
python manage.py runserver
```

It will show the address and port number of the local server, likely http://127.0.0.1:8000/

Copy the address to your browser, and add products after it

For example, http://127.0.0.1:8000/products

Note: we encountered issues when using localhost as a synonym for 127.0.0.1, so we recommend
NOT to use localhost