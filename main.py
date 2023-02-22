import csv
import yaml
from pathlib import Path
from restocks_client import get_restocks_sales
from wise_client import get_wise_mails


def create_csv(restocks_sales, wise_mails):
    missing_payout_count = 0
    with open(Path("output.csv"), "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "PAYOUT"])

        for sale in restocks_sales:
            payout = any(str(sale.id) in str(mail) for mail in wise_mails)
            if payout:
                writer.writerow([sale.id, "True"])
            else:
                writer.writerow([sale.id, "False"])
                missing_payout_count += 1

    return missing_payout_count


if __name__ == "__main__":
    # Get credentials from file
    with open(Path("credentials.yml")) as f:
        my_credentials = yaml.safe_load(f)
        user = my_credentials["user"]
        password = my_credentials["password"]
        restocks_user = my_credentials["restocks_user"]
        restocks_password = my_credentials["restocks_password"]
        wise_mail = my_credentials["wise_mail"]

    wise_mails = get_wise_mails(user, password, wise_mail)
    restocks_sales = get_restocks_sales(restocks_user, restocks_password)

    # Create CSV and get missing payout count
    missing_payout_count = create_csv(restocks_sales, wise_mails)

    # Print false count
    print(f"\nNumber of missing payouts: {missing_payout_count}")
