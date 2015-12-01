import email
from imaplib import IMAP4_SSL

# log in and select the inbox
mail = IMAP4_SSL('imap.mail.ru')
mail.login('tormentor_bts@mail.ru', 'starfish')
mail.select('TORRENTS')

# get uids of all messages
_, data = mail.uid('search', None, 'ALL')
uids = data[0].split()

# read messages
for i in uids:
    _, data = mail.uid('fetch', i, '(RFC822)')
    m = email.message_from_string(data[0][1])

    if m.get_content_maintype() == 'multipart':  # multipart messages only
        for part in m.walk():
            # find the attachment part
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            # save the attachment in the program directory
            filename = part.get_filename()
            with open(filename, 'wb') as f:
                f.write(part.get_payload(decode=True))
            print '%s saved!' % filename
    mail.uid('store', i, '+FLAGS', '\\Deleted')
    mail.expunge()
    print 'Done!'
