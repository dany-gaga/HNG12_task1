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
    if not number_str.lstrip('-').isdigit():  
        return Response({"number": number_str, "error": True}, status=status.HTTP_400_BAD_REQUEST)  

    number = int(number_str)  
    properties = []  

    # Check for Armstrong number  
    if is_armstrong(number):  
        properties.append("armstrong")  

    # Classify as even or odd  
    if number % 2 == 0:  
        properties.append("even")  
    else:  
        properties.append("odd")  

    # Check for primality  
    is_prime_result = is_prime(number) if number >= 0 else False  

    # Calculate digit sum  
    digit_sum_value = my_digit_sum(number)  

    # Generate the fun fact correctly for Armstrong numbers or get from API  
    if is_armstrong(number):  
        num_str = str(number)  
        num_digits = len(num_str)  
        # Generate the power and summation string  
        power_terms = [f"{digit}^{num_digits}" for digit in num_str]  
        fun_fact = f"{number} is an Armstrong number because " + " + ".join(power_terms) + f" = {number} // gotten from the numbers API"  
    else:  
        fun_fact = get_fun_fact(abs(number))  

    # Creating the response data and including the note for digit_sum  
    response_data = {  
        "number": number,  
        "is_prime": is_prime_result,  
        "is_perfect": False,  # Placeholder  
        "properties": properties,  
        "digit_sum": f"{digit_sum_value} // sum of its digits",  # Include the note  
        "fun_fact": fun_fact  # Use the formatted fun fact  
    }  

    return Response(response_data, status=status.HTTP_200_OK)  

def get_fun_fact(number):  
    response = requests.get(f"http://numbersapi.com/{number}/math")  
    if response.status_code == 200:  
        return response.text + " // gotten from the numbers API"  # Append the note directly  
    return "No fun fact available."