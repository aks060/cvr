# cvr
CVR

    Last Tested: 31 May 2021
    Semi-Automatic. Requires only captcah. Not for selling. Use Legally.
    
# Requirements  (For Linux)
    1. Ubuntu or any Deb Distro
    2. Install firefox, espeak, python in Linux
    3. Internet and Terminal
    
    
# Steps
        VOLUME FULL
    1. Open Terminal and set it to `Keep above others`
    2. Assign your dist in main.py `district` and put pincode you want to book in `pincodes`
    3. Run `python3 otp.py -m <Your Mobile Number>`  Enter OTP  you will get auth token.
    4. Run `python3 main.py -b <Your Position in your cowin account (0, 1, 2, 3) > -t <Auth Token you get>
    5. IF VACCINE AVAILABLE in given PINCODES  it will open CAPTCHA in Firefox. Enter CAPTCHA.
    
    6. Done!!!!
    
    
# Things to keep in mind.
    1. Session time out is 15 min.
    2. Time diff b/w each request should be min 5 sec. Otherwise IP will block.
    3. If tried sending OTP within 2 min of previous otp. <YOU WILL NOT RECIEVE NEW ONE. USE THAT OLD ONE AGAIN. SMS charges Rs 0.5 ;)> 
    4. Don't share this to Govt. People. They will definitely <NOT> like it.
    5. For Mac Please change Line 137 in main.py

# Response Codes:
    400 : Either is already booked or something else is wrong
    401 : Unauthorised or Session Expired
    409 : Center is Full, No slot left
    500 : Not your issue. They will manage.
