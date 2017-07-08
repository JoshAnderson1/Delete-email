#deletes email from outlook
import imaplib

print("use outlook username and password")
username = input("username ")
password = input("password ")
sender = input("which sender to delete ")

mail = imaplib.IMAP4_SSL("imap-mail.outlook.com" , "993")
mail.login(username, password)
mail.select("Inbox", False)
typ, data = mail.search(None, "From", sender)
for num in data[0].split():
    mail.store(num, "+FLAGS", '\\Deleted')
mail.expunge()
print("Emails Deleted")
mail.close()
mail.logout()
