#dictionary definition
shelf = {
    "box1": "password1",
    "box2": "password2",
    "box3": "password3"
}
#the user enter the password
password = input("please enter your password:")
#if password correct,prin correct password
if password == shelf:
    print("correct password,please take your bag")
#if thepassword is not correct,print incorrect password,re-enter password
elif password != shelf:
    print("incorrect password,please re-enter your password:")

