#!/usr/bin/python3
import requests, json, os
from hashlib import sha256
import sys

mobile='9898989898'
arg=sys.argv
for i in arg:
    if i == '-m':
        ind=arg.index('-m')+1
        mobile=arg[ind]
s=requests.session()

head={
        # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; Nexus One Build/FRF50)',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Origin': 'https://selfregistration.cowin.gov.in',
        'Referer': 'https://selfregistration.cowin.gov.in/'
}
host='https://cdn-api.co-vin.in/api'

def login():
    global s, head
    dt={
        'mobile': mobile,
        'secret': 'U2FsdGVkX1+927iXIEfioc/xdfULU6iVyh+a5IQPxsKeeogQxkRwRqlAhS0rsT35N8eDsNel0K+OjPNE0epL/g==',
        #'secret': 'U2FsdGVkX1+Ol0WJ6HsqZ9SxoATLbzjK78QlcetDkYDJCxljh3mKTj1pQiWS6wi/XRhI7B5Au4rwRwQVE8TYfw=='
    }
    res=s.post(host+'''/v2/auth/generateMobileOTP''', headers=head, data=json.dumps(dt))
    if res.status_code==200:
        cont=json.loads(res.content.decode())
        txnID=cont['txnId']
        otp=input('Enter OTP: ')
        # os.popen('espeak OTP')
        otp= sha256(otp.encode('utf-8')).hexdigest()
        dt2={
            "otp": str(otp),
            "txnId": txnID
        }

        res1=s.post(host+'''/v2/auth/validateMobileOtp''', headers=head, data=json.dumps(dt2))
        if res1.status_code==200:
            cont=json.loads(res1.content.decode())
            print("\n\n")
            print(cont['token'])
        else:
            print('in otp')
            print(res1.content.decode())
    else:
        print('OTP Error')

login()