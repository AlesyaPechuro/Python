import json

# # преобразовали json-строку в словарь
# string = '{"id":765, "email":"ivanov@mail.ru", "surname":"Ivanov", "age":45, "admin":false, "friends":[123,456,789]}'
# data = json.loads(string)
# print(data["email"])
# print(data["surname"])
# print(data["admin"])
# print(data["friends"])
#
#
# # читаем json-данные из файла и преобразуем в словарь
# with open('data.json', encoding='utf-8') as file:
#     data = json.load(file)
# print(data["email"])
# print(data["surname"])
# print(data["admin"])
# print(data["friends"])

data = {"id": 765, "email": "ivanov@mail.ru", "surname": "Иванов", "age": 45, "admin": False,
        "friends": [123, 456, 789]}
# преобразуем словарь в json-строку (будет Иванов символами юникода)
string = json.dumps(data)
print(string)
# преобразуем словарь в json-строку (добавляем параметр для записи кирилицы)
string = json.dumps(data, ensure_ascii=False)
print(string)
# преобразуем словарь в json и записываем в файл
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
