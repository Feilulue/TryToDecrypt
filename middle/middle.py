import string
import requests

URL = "http://api.trytodecrypt.com/encrypt?key=xxxxxxxxxxxxxxxxxxxxxxxx&id="
submit = "http://api.trytodecrypt.com/solve?key=xxxxxxxxxxxxxxxxxxxxxxxx&id="

li = string.digits+string.ascii_lowercase+string.ascii_uppercase+'-_.,;:?! '

encoded_dict = {}

def dec(ch):
    u = URL+ch
    r = requests.get(url=u,)
    data=r.text
    return data

def go(plaintext):
    print("plaintext sloved this time:",plaintext)
    solve = submit + plaintext
    r = requests.get(url=solve)
    correct = r.text
    if correct == '0':
        print("answer is wrong")
        reverse = input("try reversed one? [Y/N]")
        if reverse == 'Y':
            go(plaintext[::-1])
    if correct == '1':
        print("Got it!")




textid = input("encrypt id: ")
submit += textid + "&solution="
URL = URL + textid + "&text="

step = int(input("How many chars each char encrypt to: "))
enc = input("text to decrypt: ")
guess = ''
result = ''
num = int(len(enc)/step)


print("Guessing...\r",end='')
for i in range(num):
    for letter in li:
        temp = guess
        temp += letter
        tempdec = dec(temp)
        if tempdec == enc[0:(i+1)*step]:
            guess = temp
            print("Guessing...",guess,"\r",end='')
            break
print("Finished...\n")


result = guess
go(result)












