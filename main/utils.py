import json

def open_json():

    """формирование списка словарей"""

    with open('operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
    return operations


def executed_operations(operations):

    """функция выбирает из списика только валидные операции"""

    executed_data = []
    for i in operations:
        if "state" in i and i["state"] == "EXECUTED":
            executed_data.append(i)
    return executed_data


def sorted_operations(executed_data):

    """сортирует операции по дате"""

    sorted_data = sorted(executed_data, key=lambda x:x["date"], reverse=True)
    return sorted_data


def secure_to(number):

    """скрывает часть счёта получателя под **"""

    secure_number_to = int(number[-4:])
    return secure_number_to


def secure_from(number):

    """скрывает часть счёта отправителя под ** ****"""

    number_to_change = number[-10:-4]
    secure_number = list(number.replace(number_to_change, "** ****"))
    secure_number_from = secure_number.insert(-4, ' ')
    secure_number_from = secure_number.insert(-14, ' ')
    return ''.join(secure_number)

if __name__ == "__main__":
    print(open_json())