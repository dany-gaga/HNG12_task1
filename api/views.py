from django.shortcuts import render

# Create your views here.
import requests  # to make HTTP requests and to fetch fun facts from the Numbers API.
from rest_framework.decorators import api_view  # converts a standard view function into a Django REST Framework (DRF) view
from rest_framework.response import Response  # class that helps you return an HTTP response in DRF
from rest_framework import status  # module that contains HTTP status codes for use in the responses

""" The function 'is_prime' checks whether a number n is a prime number.
As such first, only numbers greater than 1 are considered, 
and they cannot be exactly divided by any whole number 
other than themselves and 1 """ 

def is_prime(n):  
    if n <= 1:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

"""An Armstrong number or narciccistic number is a positive 
integer that is equal to  the sum of its digits, each raised to the power of the number 
of digits in the number. 
Thus, is_armstrong return false for all negative numbers, 
do the sum of each digit and return True if the sum
equals the number given"""

def is_armstrong(n):  
    if n < 0:    
        return False  
    num_str = str(n)  
    num_length = len(num_str)  
    return sum(int(digit) ** num_length for digit in num_str) == n  

"""the function my_digit_sum calculate 
the absolute value of the number given"""
def my_digit_sum(n):  
    return sum(int(digit) for digit in str(abs(n)))  # Use absolute value for digit sum  

@api_view(['GET'])  
def classify_number(request):  
    number_str = request.GET.get('number')  

    # Input validation  
    if not number_str.lstrip('-').isdigit():  # to allow negative numbers  
        return Response({"number": number_str, "error": True}, status=status.HTTP_400_BAD_REQUEST)  

    number = int(number_str)  
    properties = []  # to store the properties of the number

    # Check for Armstrong number only for non-negative integers  
    if is_armstrong(number):  
        properties.append("armstrong")  

    # Classify as even or odd (negative numbers included)  
    if number % 2 == 0:  
        properties.append("even")  
    else:  
        properties.append("odd")  

    # Checking for primality  
    if number < 0:  
        is_prime_result = False  # Negative numbers are not prime  
    else:  
        is_prime_result = is_prime(number)  

    fun_fact = get_fun_fact(abs(number))  # Use absolute value to fetch fun fact  

    response_data = {  
        "number": number,  
        "is_prime": is_prime_result,  
        "is_perfect": False,  # Placeholder for perfect number check  
        "properties": properties,  
        "digit_sum": my_digit_sum(number),  
        "fun_fact": fun_fact  
    }  

    return Response(response_data, status=status.HTTP_200_OK)  

def get_fun_fact(number):  
    response = requests.get(f"http://numbersapi.com/{number}/math")  
    return response.text if response.status_code == 200 else "No fun fact available."
