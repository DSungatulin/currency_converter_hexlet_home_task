# 1. Приветствие
# 2. Мануал
# 3. Вывод списка валют
# 4. Запрос имеющейся валюты
# 5. Количество валюты
# 6. Необходимая валюта
# 7. Вывод расчета

from onlinerequests import response


CURRENCIES = response.json()['data']

# 1.
print('Добро пожаловать в конвертер валют')

# 2.
print('''
Наша программа поможет Вам конвертировать валюту.
1. Введение имеющейся валюты
2. Количество этой валюты
3. Выбор валюты для конвертации
''')

while True:
# 3.
    repeat = input('Желаете провести конвертацию? Если да, введите "Yes", если нет, введите "No": ')
    if repeat.upper() != 'YES' and repeat.upper() != 'NO':
        print('Неверный ввод. Попробуйте еще раз')
        continue
    elif repeat.upper() == 'YES':
        def offer_currencies():
            print('Вам предложены следующие валюты:')
            key_counter = 1
            for key in CURRENCIES:
                print(f'{key_counter}. {key}')
                key_counter += 1
        offer_currencies()

        # 4.
        def recieve_data():
            while True:
                user_currency = input('Введите имеющуюся валюту: ')
                if user_currency.upper() in CURRENCIES.keys():
                    break
                else:
                    print('Неверное значение. Выберите валюту из представленных вариантов')

        # 5.
            while True:
                try:
                    current_amount = float(input('Введите имеющуюся сумму: '))
                    if type(current_amount) == float:
                        break
                except:
                    print('Неверное значение. Введите числовое значение')

        # 6.
            while True:
                conversion_currency = input('Выберете валюту для конвертации: ')
                if conversion_currency.upper() in CURRENCIES.keys():
                    break
                else:
                    print('Неверное значение. Выберите валюту из представленных вариантов')
            return user_currency, current_amount, conversion_currency
        recieved_data = recieve_data()
        # 7.
        def calculate_amount():
            converted_amount = CURRENCIES.get(recieved_data[2].upper()) / CURRENCIES.get(recieved_data[0].upper())\
                                * recieved_data[1]
            return converted_amount
        print(f'Сумма в конвертированной валюте {round(calculate_amount(), 2)} {recieved_data[2].upper()}')
    else:
        print('До свидания! Жду Вас снова!')
        break
