# Number Classification API
This API takes a number and returns interesting mathematical properties and a fun fact.
https://hng.tech/hire/python-developers

### Parameters
number: An integer (positive or negative values accepted)

### Responses
**200 OK**

'''json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": "11,  // sum of its digits"
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API"
}
'''

**400 Bad Request**

'''json
{
    "number": "alphabet",
    "error": true
}
'''

## Deployment
The API is deployed on "https://dukpe.pythonanywhere.com/"

## Requirements

## Usage
To run the API locally follow this step
1. Clone the repository: https://github.com/dany-gaga/HNG12_task1
2. go to the directory: cd HNG12_task1/number_classifier
3. in your terminal run: python manage.py runserver  


# Endpoint
https://dukpe.pythonanywhere.com/api/classify-number/?number={number}`
example: https://dukpe.pythonanywhere.com/api/classify-number/?number=371



