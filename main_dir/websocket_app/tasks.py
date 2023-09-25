import requests

from celery import shared_task

from .models import BTCModel


def check_btc_history():
    pass


@shared_task()
def debug_task():
    """
    Task to retrieve information about BTC via coincap API
    """
    if check_btc_history():
        pass
    response = requests.get('https://api.coincap.io/v2/assets/bitcoin')
    print(response.status_code)
