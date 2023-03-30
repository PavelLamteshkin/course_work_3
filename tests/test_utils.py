from main.utils import executed_operations, secure_to, secure_from, sorted_operations


def test_secure_to():
    assert secure_to("Счет 64686473678894779589") == 9589


def test_secure_from():
    assert secure_from("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_executed_operations():
    assert executed_operations([{'id': 441945886, 'state': 'EXECUTED'}, {'id': 743628025, 'state': 'CANCELED'}]) == [{'id': 441945886, 'state': 'EXECUTED'}]


def test_sorted_operations():
    assert sorted_operations([{'id': 441945886, 'date': '2019-08-26T10:50:58.294041'}, {'id': 634356296, 'date': '2018-01-21T01:10:28.317704'}, {'id': 949194534, 'date': '2019-08-15T01:48:10.042554'}]) == [{'id': 441945886, 'date': '2019-08-26T10:50:58.294041'}, {'id': 949194534, 'date': '2019-08-15T01:48:10.042554'}, {'id': 634356296, 'date': '2018-01-21T01:10:28.317704'}]
