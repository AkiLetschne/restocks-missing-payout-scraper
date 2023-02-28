from restocks.client import Client
from restocks import exceptions

def get_restocks_sales(restocks_user, restocks_password):
    # Initialize client
    restocks_client = Client()
    restocks_client.login(restocks_user, restocks_password)

    # get all sales from all pages
    page = 1
    sales_history_total = []
    while True:
        try:
            sales_history = restocks_client.get_sales_history(page=page)
            sales_history_total += sales_history
            page += 1
        except exceptions.SessionException as e:
            if not str(e) == 'no sales found':
                print(f'Error retrieving sales data from Restocks.net. The following error occurred: {str(e)}')
            break

    history_filtered = [sale for sale in sales_history_total if sale.date.year >= 2022]
    return history_filtered
