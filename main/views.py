from django.shortcuts import render
from .models import Payment
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

# Создаем линейный график
def create_linear_graph(payments):
    #Заполняем необходимые для работы парметры
    dates = [p.pay_date.strftime('%Y-%m-%d') for p in payments]
    amounts = [float(p.amount) for p in payments]

    # Создаем график
    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts)

    # Подписываем график
    plt.title('Платежи по датам')
    plt.xlabel('Дата')
    plt.ylabel('Сумма платежа')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.2)

    # Сохраняем
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Превращаем в текст для вставки в html 
    imgbase = base64.b64encode(buffer.getvalue()).decode()

    buffer.close()
    plt.close()

    return imgbase

# Создаем гистограмму (Аналогично с линейным графиком)
def create_histogram(payments):
    names = [f'{p.payer.last_name} {p.payer.first_name}' for p in payments]
    amounts = [float(p.amount) for p in payments]

    plt.figure(figsize=(10,5))
    plt.bar(names, amounts)

    plt.title('Платежи по плательщикам')
    plt.xlabel('Плательщик')
    plt.ylabel('Сумма')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    imgbase = base64.b64encode(buffer.getvalue()).decode()

    buffer.close()
    plt.close()

    return imgbase

def payments_data(request):
    payments = Payment.objects.select_related('payer').order_by('pay_date')

    linear_graph = create_linear_graph(payments)

    histogram = create_histogram(payments)

    return render(request, 'main/index.html', {'linear_graph': linear_graph,
                                                'histogram': histogram, 
                                              })  