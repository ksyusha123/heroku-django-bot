# Template for backend course  

App is working on ```https://heroku-django-bot.herokuapp.com```  
Bot ```@django_2tapp_bot```  

## How to run  
server: 
```python src/manage.py runserver ```   
bot: 
```python src/manage.py run_bot```

## Endpoints  
- ```/api/users/```  
register new user

post json  
```
{
    "user": {
        "telegram_username": "username",
        "telegram_id": "1234567890"
        "password": "secretpassword"
    }
}
```  

- ```/api/users/login/```  
authorize user  
return info and token  
works only if phone number is set  

post json  
```
{
    "user": {
        "telegram_username": "username",
        "password": "secretpassword"
    }
}
```  

- ```/api/users/me/```  
get information about user  

get request with Authorizaion header.  
Header: 
```
{'Authorization' : 'Token token123'}
```

## Bot commands  
- /start \<password>   
register you  
- /set_phone \<phone number>   
save your phone number  
- /me     
get info about you  
