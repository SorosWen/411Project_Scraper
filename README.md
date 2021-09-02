# 411 Project

## Project Description:
This is a Amazon/eBay product scrapper created for CS411. The scrapping functionality of the project is primarily done through APIs. 

## How to run
### Install dependencies
You need suffiently updated python3 and pip to run this project.
In the desired place where you want to place this project, run these commands:
```
git clone https://github.com/SorosWen/411project
cd 411project
pip install -r requirements.txt
```

###
To let the API work, 
create a file named keys.json 
under the path: prototype/configs/
In the file, copy the following code: (if the file doesn't exist under this path yet)
```
{
    "googleKey": "a1e40b3f204f9896d55206cd1f3fd273",
    "ebayKey": "E09581872ED647DFA5BCF7A1E9B35EF9",
    "amazonKey": "0C6E9C7C5918437BBD940542C02F9D53"
}
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



### Project Video
The link to the project video: https://youtu.be/Ij9fArTmjE0
