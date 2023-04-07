from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
import requests

# Create your views here.


def index(request):
    return render (request, "handler/index.html")


def find_product(request):
    if request.method == 'POST':
        # создаем экземпляр формы и заполняем его данными из запроса
        form = ProductForm(request.POST)
        if form.is_valid():
            # извлекаем данные из формы
            article = form.cleaned_data['article']

            headers = {
            'authority': 'parts.renault.ua',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=020d83a65d78528e04c0d9c2e7ec5e8c; _ga=GA1.2.1782834077.1680813695; _gid=GA1.2.1022058263.1680813695',
            'origin': 'https://parts.renault.ua',
            'referer': 'https://parts.renault.ua/',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

            data = {
                'search_parts[code]': f'{article}',
                'search_parts[region]': '',
                'search_parts[diler]': '',
            }

            response = requests.post('https://parts.renault.ua/showbycode', headers=headers, data=data)


            # выполняем запрос на другой сайт, передавая артикул в параметрах
            response = requests.get('https://example.com/api/product', params={'article': article})

            # проверяем статус-код ответа, если все ок, возвращаем результат
            if response.status_code == 200:
                result = response.json()
                print(response.content)
                return render(request, 'result.html', {'result': result})
            else:
                error_message = 'Произошла ошибка при запросе: {}'.format(response.status_code)
        else:
            error_message = 'Форма невалидна, пожалуйста, исправьте ошибки.'
    else:
        form = ProductForm()
        error_message = None

    # возвращаем шаблон с формой и возможной ошибкой
    return render(request, 'form.html', {'form': form, 'error_message': error_message})
