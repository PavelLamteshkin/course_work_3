import utils
from datetime import datetime


if __name__ == "__main__":
    operations = utils.open_json()
    executed_data = utils.executed_operations(operations)
    sorted_data = utils.sorted_operations(executed_data)
    count = 1
    for i in sorted_data:
        date_str = i['date']
        date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        correct_date = date.strftime("%d.%m.%Y")
        if count <= 5:
            print(f"{correct_date} {i['description']}")
            if 'from' not in i:
                print(f"**{utils.secure_to(i['to'])}")
            else:
                print(f"{utils.secure_from(i['from'])} -> **{utils.secure_to(i['to'])}")
            print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
            count += 1
            print()
