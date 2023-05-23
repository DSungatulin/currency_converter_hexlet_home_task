import requests

API_KEY = '3MgY8Vcy8Cp3pQKR7tSHeMdYne34ICZ8qTzqpaVL'

HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=EUR%2CUSD%2CGBP%2CRUB'

response = requests.get(HOST)

# current_amount = (input('Введите имеющуюся сумму: '))

# print(type(current_amount))