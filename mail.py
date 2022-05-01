# ライブラリをインポート
from logging import NullHandler
import os
import smtplib
import sys
from email import message

from dotenv import load_dotenv
load_dotenv()

# 環境変数を取得
main_server = os.getenv('MAIL_SERVER')
mail_server_port = os.getenv('MAIL_SERVER_PORT')
account = os.getenv('ACCOUNT')
password = os.getenv('PASSWD')

def main():
    to_mail = sys.argv[1]
    msg = message.EmailMessage()
    msg.set_content(sys.argv[3]);
    msg['Subject'] = sys.argv[2]
    msg['From'] = account
    msg['To'] = to_mail
    server = smtplib.SMTP(main_server, mail_server_port, timeout=10)
    server.login(account, password)
    # result = server.send_message(msg)
    server.quit()
    # print(result)

if __name__ == '__main__':
    main()
