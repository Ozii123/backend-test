# backend-test

### Python Version
```
Python 3.7
```


### Instructions
- Clone the repository
    ``` cd backedn-test ``` 
- create virtual environment and run
    ``` pipenv shell ```

### Install the dependencies
```
pip install -r requirment.txt
```
### GET Request 
``` 
curl --location --request GET 'http://localhost:8000/sections' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "title":"title of section 1111111111111",
    "body" : " body of section 0 313210 32132.0",
    "parent": "668e0edf-a691-4290-8d42-67e57cdce811"
}'
```
### POST Request
```
curl --location --request POST 'http://localhost:8000/sections/' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "title":"title of section",
    "body" : " body of section",
    "parent": "fbe9f5bc-91e0-4586-9b10-f8b2b4353878"
}'
```

### PUT Request
``` 
curl --location --request PUT 'http://localhost:8000/sections/fbe9f5bc-91e0-4586-9b10-f8b2b4353878' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "title":"title of section",
    "body" : " body of section",
    "parent": "fbe9f5bc-91e0-4586-9b10-f8b2b4353878"
}'
```

### DELETE Request
``` 
curl --location --request DELETE 'http://localhost:8000/sections/fbe9f5bc-91e0-4586-9b10-f8b2b4353878' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "title":"title of section 1111111111111",
    "body" : " body of section 0 313210 32132.0",
    "parent": "668e0edf-a691-4290-8d42-67e57cdce811"
}'
```
