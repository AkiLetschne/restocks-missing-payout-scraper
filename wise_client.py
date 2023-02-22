import imaplib
import email


def get_wise_mails(user, password, wise_mail):
    # setup imap
    imap_url = 'imap.gmail.com'
    my_mail = imaplib.IMAP4_SSL(imap_url)
    my_mail.login(user, password)
    my_mail.select('Inbox')

    key = 'FROM'
    value = wise_mail
    _, data = my_mail.search(None, key, value)

    mail_id_list = data[0].split()  # IDs of all emails that we want to fetch

    msgs = []  # empty list to capture all messages
    # Iterate through messages and extract data into the msgs list
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns whole message (BODY fetches just body)
        msgs.append(data)

    raw_mail_text = []
    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg = email.message_from_bytes((response_part[1]))
                print("_________________________________________")
                print("subj:", my_msg['subject'])
                for part in my_msg.walk():
                    if part.get_content_type() == 'text/html':
                        raw_text = str(part.get_payload())
                        raw_mail_text.append(raw_text)

    return raw_mail_text
