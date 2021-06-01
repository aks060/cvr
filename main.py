#!/usr/bin/python3
import os, sys, requests
import json, time
arg=sys.argv
age=18
day=int(os.popen('date +%d').read())
month=int(os.popen('date +%m').read())
year=int(os.popen('date +%Y').read())
district=702  #Haridwar
#district=139 #Due
# district=623 #Aligarh
pincodes=[
    249403,
    249402,
    249407,
    249408
]
s=requests.session()
ben_id=0

# token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJmOTA4ZDZjMC00ZTc5LTRkYjMtODdhZi1jZmM5ZDE5N2QwMTIiLCJ1c2VyX2lkIjoiZjkwOGQ2YzAtNGU3OS00ZGIzLTg3YWYtY2ZjOWQxOTdkMDEyIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5ODc3Njk3OTM3LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjc0Nzc0NDkyODk3NDcwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoWDExOyBVYnVudHU7IExpbnV4IHg4Nl82NDsgcnY6ODguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC84OC4wIiwiZGF0ZV9tb2RpZmllZCI6IjIwMjEtMDUtMjBUMTM6NDA6NDEuNDU5WiIsImlhdCI6MTYyMTUxODA0MSwiZXhwIjoxNjIxNTE4OTQxfQ.AHGQjwUfGcfzKdGsTRdR3FEQD04DVR0cSYkBdW5MbWU'
#token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIwOTQ4ZjgxNC0xZTk3LTQ1YjQtOGE0Yi00ZjFmZTdkMWJhYjciLCJ1c2VyX2lkIjoiMDk0OGY4MTQtMWU5Ny00NWI0LThhNGItNGYxZmU3ZDFiYWI3IiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo4NjMwNTEzMzA4LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjkwMjc2MzYzMjY4MjIwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoWDExOyBVYnVudHU7IExpbnV4IHg4Nl82NDsgcnY6ODguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC84OC4wIiwiZGF0ZV9tb2RpZmllZCI6IjIwMjEtMDUtMjBUMDk6MDM6MzUuMzY4WiIsImlhdCI6MTYyMTUwMTQxNSwiZXhwIjoxNjIxNTAyMzE1fQ.zwLT9jylJ2JtWsW6FcBg-PTK2xitOt3koctW5d6Zrow'
token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJMb2dpbnw3ODMwNTUwNzA5IiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjoiNzgzMDU1MDcwOSIsInNlY3JldF9rZXkiOiJiNWNhYjE2Ny03OTc3LTRkZjEtODAyNy1hNjNhYTE0NGYwNGUiLCJzb3VyY2UiOiJjb3dpbiIsInVhIjoiTW96aWxsYS81LjAgKFgxMTsgVWJ1bnR1OyBMaW51eCB4ODZfNjQ7IHJ2Ojg4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvODguMCIsImRhdGVfbW9kaWZpZWQiOiIyMDIxLTA1LTMxVDA3OjI2OjM0Ljg1MVoiLCJpYXQiOjE2MjI0NDU5OTQsImV4cCI6MTYyMjQ0Njg5NH0.HDg_9vITEYQkzZfjCXf6oUnslrnG98o0shXSVFCkZuo'
host='https://cdn-api.co-vin.in/api'
for i in arg:
    if i == '-a':
        ind=arg.index('-a')+1
        age=int(arg[ind])
    if i == '-d':
        ind=arg.index('-d')+1
        day=int(arg[ind])
    if i == '-m':
        ind=arg.index('-m')+1
        month=int(arg[ind])
    if i == '-y':
        ind=arg.index('-y')+1
        year=int(arg[ind])
    if i == '-dis':
        ind=arg.index('-dis')+1
        district=int(arg[ind])
    if i == '-t':
        ind=arg.index('-t')+1
        token=arg[ind]
    if i == '-b':
        ind=arg.index('-b')+1
        ben_id=int(arg[ind])

head={
        # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; Nexus One Build/FRF50)',
        'Authorization': 'Bearer '+token
    }

def getVaccine(age, day, month, year, district):
    global s
    res=s.get('''https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='''+str(district)+'&date='+str(day)+'-'+str(month)+'-'+str(year), headers=head).content.decode()
    #print(res)
    js_res=json.loads(res)
    if 'centers' not in js_res:
        return 0
    js_res = js_res['centers']
    for i in js_res:
        #print(i)
        if len(i['sessions'])!=0:
            if i['pincode'] not in pincodes:
                continue
            ses=i['sessions']
            for j in ses:
                if j['min_age_limit'] <= age:
                    #print('capacity: '+str(j['available_capacity']))
                    if j['available_capacity'] > 0:
                        #os.popen('espeak available')
                        mssg=i['name']+' ('+i['fee_type']+'), '+i['block_name']+', '+i['district_name']+' : ('+str(j['available_capacity'])+') at '+j['date']
                        vaccinedone=getBenef(j['session_id'], j['slots'][1])
                        if vaccinedone==1:
                            for i in range(0, 5):
                                os.popen('espeak Done')
                                time.sleep(1)
                            return 5
                        print(mssg)
                    # else:
                    #     mssg=i['name']+' ('+i['fee_type']+'), '+i['block_name']+', '+i['district_name']+' : (Booked) at '+j['date']
                    #os.popen('notify-send "Vaccine for your age available" "'+mssg+'" ')
    return 1


def getBenef(session_id, slot):
    global s, token, head, ben_id
    res=s.get(host+'''/v2/appointment/beneficiaries''', headers=head)
    if res.status_code!=200:
        print('Unsuccessfull')
        os.popen('espeak "failed at beneficiaries"')
    cont=res.content.decode()
    # print('here: '+cont)
    try:
        contjs=json.loads(cont)
        ben=contjs['beneficiaries']
        ben_id=ben[ben_id]['beneficiary_reference_id']
        getcaptcha()
        sys.stdout.flush()
        captcha=input('Enter Captcha(0 for retry): ')
        while captcha=='0':
            getcaptcha()
            sys.stdout.flush()
            captcha=input('Enter Captcha(0 for retry): ')
        slotbook={
        "dose": 1,
        "session_id": session_id,
        "slot": slot,
        "captcha": captcha,
        "beneficiaries": [
            ben_id      
        ]
        }
        res=s.post(host+'''/v2/appointment/schedule''', headers=head, data=json.dumps(slotbook))
        if res.status_code==200:
            print(res.content.decode())
            return 1
        else:
            print(res)
            return 0
    except:
        print('Error in data')
        print(cont)
        return 0
    
def getcaptcha():
    global s, token, head
    os.popen('espeak captcha')
    # head['Authorization'] ='Bearer '+token
    res=s.post(host+'''/v2/auth/getRecaptcha''', headers=head).content.decode()
    #os.popen('echo text.html')
    js=json.loads(res)
    f=open('cap.html', 'w')
    f.write(js['captcha'])
    f.close()
    os.popen('firefox cap.html')
    #FOR MAN CHANGE IT TO  'open -a firefox cap.html'


days=day
counter=1
while True:
    print("running "+str(counter)+" times")
    ret=getVaccine(age, days, month, year, district)
    if ret==5:
        break
    counter+=1
    time.sleep(5)
