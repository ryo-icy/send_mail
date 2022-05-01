# send mail
メールを送信するPythonスクリプト

## 使い方

1. `.env`ファイルにデータを入力する。

example
```
MAIL_SERVER = hoge.com
MAIL_SERVER_PORT = 587

ACCOUNT = hogehoge@hoge.com
PASSWD = passwordhogehuga
```

2. 下記コマンドを実行する。
```
python mail.py <宛先アドレス> <件名> <本文>
```
