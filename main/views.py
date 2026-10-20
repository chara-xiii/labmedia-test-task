from django.shortcuts import render
from .models import Payment
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64


def create_linear_graph(payments):
    dates = [p.pay_date.strftime('%Y-%m-%d') for p in payments]
    amounts = [float(p.amount) for p in payments]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, amounts)

    plt.title('Платежи по датам')
    plt.xlabel('Дата')
    plt.ylabel('Сумма платежа')
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.2)

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

    return render(request, 'main/index.html', {'linear_graph': linear_graph})
