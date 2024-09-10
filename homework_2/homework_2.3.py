# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    num_to_str = str(num)
    num_length = len(num_to_str)
    num_digits = []

    for i, num_digit in enumerate(num_to_str):
        if num_digit != '0':
            zeroes_in_num = num_length - i - 1
            num_digits.append(num_digit + '0' * zeroes_in_num)

    return ' + '.join(num_digits)

user_input = int(input("Enter a number: "))
print(expanded_form(user_input))


