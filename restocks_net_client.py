from restocks_client.client import RestocksClient


def get_restocks_sales(restocks_user, restocks_password):
    # Initialize client
    restocks_client = RestocksClient()
    restocks_client.email = restocks_user
    restocks_client.password = restocks_password
    restocks_client.login()

    # get all sales from all pages
    sales_history_total = restocks_client.get_history_sales()

    history_filtered = [sale for sale in sales_history_total if sale.date.year >= 2022]
    return history_filtered
