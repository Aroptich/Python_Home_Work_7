import re


def input_first_name() -> str:
    '''Функция возвращает имя типа str'''
    try:
        first_name = input('Введите имя: ')
        name =''.join(re.findall(r'[а-яА-Яa-zA-Z]{1,}', first_name))
        if first_name == name:
            return first_name.capitalize()
    except ValueError:
        print('Имя не должно содержать служебных символов (,./*-+)\n'
              'Повторите ввод заново')
        return input_first_name()

def input_last_name() -> str:
    '''Функция возвращает фамилию типа str'''
    try:
        last_name = input('Введите фимилию: ')
        name =''.join(re.findall(r'[а-яА-Яa-zA-Z]{1,}', last_name))
        if last_name == name:
            return last_name.capitalize()
    except ValueError:
        print('Имя не должно содержать служебных символов (,./*-+)\n'
              'Повторите ввод заново')
        return input_last_name()
def input_number_phone() -> str:
    '''Функция возвращает номер телефона типа str'''
    try:
        number_phone = input('Введите номер телефона: ')
        number = re.findall("^(\+7|7|8)?(\s|-)?([0-9]{3})(\s|-)?([0-9]{3})(\s|-)?([0-9]{2})(\s|-)?([0-9]{2})", number_phone)
        valid_number = ''.join([num for num in number[0]])
        if valid_number == number_phone:
            return number_phone
    except ValueError as err:
        print('Номер телефона введен не коректно!\n'
              'Пример ввода: +7хххххххххх или 8хххххххххх')
        return input_number_phone()


