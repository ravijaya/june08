"""process pool"""

import multiprocessing
import requests
from smtplib import SMTP
from email.mime.text import MIMEText

SMTP_SERVER_ADDR = 'localhost'  # mail.citrix.com


def send_alert_mail(from_addr, to_addr, subject, message, debug_flag=False):
    mesg = MIMEText(message)
    mesg['From'] = from_addr
    mesg['To'] = to_addr
    mesg['Subject'] = subject
    smtp = SMTP(SMTP_SERVER_ADDR)
    # smtp.login()
    smtp.debuglevel = debug_flag
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(url):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        # url = q.get()  # blocked call

        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as error:
        subject = f'{p_name}: {url}: failed http request'
        send_alert_mail('ravijaya@localhost', 'training@localhost', subject, str(error))


def main():
    """parent"""

    list_of_urls = ['http://linux.org', 'http://kernel.org', 'http://python.org', 'http://golang.org',
                    'http://perllang.org']

    with multiprocessing.Pool(processes=3) as pool: # reusing the process
        pool.map(web_crawler, list_of_urls)


if __name__ == '__main__':
    main()
