from restocks.client import Client

def get_restocks_sales(restocks_user, restocks_password):
    # Initialize client
    restocks_client = Client()
    restocks_client.login(restocks_user, restocks_password)

    # Get history sales
    sales_history = restocks_client.get_sales_history()
    history_filtered = [sale for sale in sales_history if sale.date.year >= 2022]
    return history_filtered