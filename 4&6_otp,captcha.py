#4_digit otp

import random

def otp_4():
    otp=''
    for i in range(4):
        otp+=str(random.randint(0,9))
    return(otp)
otp_4()
        
#6_digit otp
def otp_6():
    otp=''
    for i in range(6):
        otp+=str(random.randint(0,9))
    return(otp)
otp_6()


#captcha

import string

def  captcha():
    out=''
    characters=string.ascii_letters + string.digits
    for i in range(random.randint(4,6)):
        out+=random.choice(characters)
    return out
