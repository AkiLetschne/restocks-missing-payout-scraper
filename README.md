# Restocks.net missing payout scraper

This script creates a table (CSV file) that lists your sales from restock.net and shows which ones you are still missing the payout for.
I have tried this script with German payouts and don't know if it works with other regions.

If you just want to use the script, I recommend just using the exe. Then you don't need to install Python. Just fill the credentials.yxl and start the exe.

## setup
### requirements
**If you want to use the exe, you can skip this part and go directly to *credential file*.**

You need at least python version 3.11 and have to install the requirements.txt.
It is also necessary that the emails have been sent from wise to a gmail.
```
pip install -r requirements.txt
```

### credential file
You have to activate IMAP in the gmail settings and set a [Gmail App Password](https://www.youtube.com/watch?v=hXiPshHn9Pw) (as shown in the video) for the script to access your mails.
To use this script, you need to add your Gmail address and the App Password, as well as your Restocks login credentials to the credentials.yml file.
If your email address from wise should be different, then you can replace it there as well.

## run the script
###run the exe
The exe can simply be executed with a double click and the script begins.

### run the python script
To execute the script, execute the following command:
```
python main.py
```
When the script is finished, you will get the status of your sales in the output.csv file.

## important
Make sure you are using at least version 0.1.3 of the restocks-client.
To update the package use the following command.
```
pip install -U restocks-client
```

## Credits

The following resources were used in the creation of this project:
- [restocks-api-wrapper](https://github.com/AkiLetschne/restocks_api_wrapper) - Used to retrieve sales data from Restocks.net.
- [PyYAML](https://pypi.org/project/PyYAML/) - Used to read and parse the YAML configuration file.
- [Python's built-in csv module](https://docs.python.org/3/library/csv.html) - Used to read and write CSV files.
- [Python's built-in pathlib module](https://docs.python.org/3/library/pathlib.html) - Used to create a Path object for the output file.
- [Python's built-in imaplib module](https://docs.python.org/3/library/imaplib.html) - Used to connect to and interact with the IMAP email server.
- [Python's built-in email module](https://docs.python.org/3/library/email.html) - Used to parse email messages and extract their content.
