from celery import shared_task
from .models import Customer

@shared_task
def count_customers_by_city():
    data = {}

    for customer in Customer.objects.all():
        city = customer.city
        data[city] = data.get(city, 0) + 1

    print("Customer count by city:", data)
    return data
