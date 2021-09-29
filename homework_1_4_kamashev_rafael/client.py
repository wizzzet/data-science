import requests


# Создаем словарь dict с параметрами
data = {
    'key1': 0,
    'key2': 1,
    'key3': 1,
    'key4': 0,
    'key5': 1,
    'key6': 1,
    'key7': 0,
    'key8': 1,
    'key9': 1,
    'key10': 1
}

# Запрашиваем Web-сервис, передаем в запрос параметры
r = requests.get('http://127.0.0.1:5000/predict', params=data)
print(r.text)
