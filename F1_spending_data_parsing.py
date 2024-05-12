import requests
import json

# Заголовки для запроса, который будет отправлен на сервер
headers = {
    'Sec-Fetch-Site': 'same-site',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://www.f1budgetcap.com',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'ru',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'admin.f1budgetcap.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15',
    'Referer': 'https://www.f1budgetcap.com/',
    'Connection': 'keep-alive',
}

# Запрос для данных за 2023 год
params_2023 = {
    'startDate': '2024-01-01',
    'endDate': '2024-12-31',
    'selectedYear': '2023',
}
# Отправляем гет запрос на сервер для данных за 2023 год
response_2023 = requests.get('https://admin.f1budgetcap.com/api/team-details-report', params=params_2023, headers=headers)

# Запрос для данных за 2022 год
params_2022 = {
    'startDate': '2023-01-01',
    'endDate': '2023-12-31',
    'selectedYear': '2022',
}
# Отправляем гет запрос на сервер для данных за 2022 год
response_2022 = requests.get('https://admin.f1budgetcap.com/api/team-details-report', params=params_2022, headers=headers)

# Обязтаельно проверяем успешность выполнения запросов
if response_2023.status_code == 200 and response_2022.status_code == 200:
    # Объединяем данные за 2023 и 2022 годы
    combined_data = {
        '2023': response_2023.json(),
        '2022': response_2022.json()
    }

    # Сохраняем объединенные данные в json файл
    with open('data/team_details_report.json', 'w') as file:
        json.dump(combined_data, file, indent=4)
    print('Данные успешно сохранены в файл team_details_report.json')
else:
    print('Произошла ошибка при выполнении запроса.')