from django.contrib import admin
from .models import Client, Payment


@admin.register(Client) # Декоратор для регистрации клиента
class ClientAdmin(admin.ModelAdmin): # Наследуем ModelAdmin для отображения в админ панели
    
    # Указываю какие поля показывать в списке записей
    list_display = ['id', 'first_name', 'last_name', 'country']

    # Добавляю поле поиска и указываю по каким полям его можно осуществлять 
    search_fields = ['first_name', 'last_name']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'payer', 'amount', 'percent', 'pay_date']

    # Добавляю фильтр
    list_filter = ['percent']

    # Добавляю навигацию по дате платежа
    date_hierarchy = 'pay_date'
