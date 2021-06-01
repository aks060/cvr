# cvr
CVR

    Last Tested: 31 May 2021
    Semi-Automatic. Requires only captcah. Not for selling. Use Legally.
    
# Requirements  (For Linux)
    1. Ubuntu or any Deb Distro
    2. Install firefox, espeak, python in Linux
    3. Internet and Terminal
    
    
# Steps
    1. Open Terminal and set it to `Keep above others`
    2. Assign your dist in main.py `district` and put pincode you want to ok in `pincodes`
    3. Run `python3 otp.py -m <Your Mobile Number>`  Enter OTP  you will get auth token.
    4. Run `python3 main.py -t <Auth Token you get>
    5. IF VACCINE AVAILABLE in given PINCODES  it will open CAPTCHA in Firefox. Enter CAPTCHA.
    
    6. Done!!!!
    
    
# Things to keep in mind.
    1. Session time out is 15 min.
    2. Time diff b/w each request should be min 5 sec. Otherwise IP will block.
    3. If tried sending OTP within 2 min of previous otp. <YOU WILL NOT RECIEVE NEW ONE. USE THAT OLD ONE AGAIN. SMS charges Rs 0.5 ;)> 
    4. Don't share this to Govt. People. They will definitely <NOT> like it.
