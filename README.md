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

post json  
```
{
    "user": {
        "telegram_username": "username",
        "password": "secretpassword"
    }
}
```  

- ```/api/users/set_phone/```  
sets phone number  
post json with Authorization header.  
Header: 
```
{'Authorization' : 'Token token123'}
```  
request:  
```
"phone_number": "+79584621001"
```

- ```/api/users/me/```  
get information about user  
works only if phone number is set  

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
