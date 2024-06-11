import smtplib
import datetime as dt
import random

my_email = "sahid123@gmail.com"
my_password = "sjncedj12314"

now = dt.datetime()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    print(quote)

    # email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,msg=f"Subject:Monday Motivation/n/n{quote}")


