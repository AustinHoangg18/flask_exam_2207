# THIS IS AN EXAMPLE API DOCUMENTATION
## INTRODUCTION
- Create a demo complete api for <b>summing up a list of integers</b> sent from user
- This api running on localhost

## INSTALLATION
- python 3.10
- flask library (more details in [here](https://flask.palletsprojects.com/en/3.0.x/))

## API USAGE
### 1. API structure
- app url: ```http:127.0.0.1:3003/sum```
- method: POST
- headers: Yes
- authentication: yes
### 2. Request parameters
- sample: 
    ``` python
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'your_access_token_here'
    }
    ```
    ```python
    payload = {
        'args': [1,2,3]
    }    
    ```

### 3. Response parameters

- sample:
    ``` python
    {
        'status':"status message",
        'response':{
            'datetime': "2024-01-01 00:00:00" 
            'args': [1,2,3],
            'sum': 6
        }
    }
    ```
## LICENSE
