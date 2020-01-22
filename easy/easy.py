import string
import requests

URL = "http://api.trytodecrypt.com/encrypt?key=xxxxxxxxxxxxxxx&id="
submit = "http://api.trytodecrypt.com/solve?key=xxxxxxxxxxxxxxxxxxx&id="

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


print("Getting the encode pattern...")
percentage = 0
for i in li:
    print("In progress..."+str(percentage)+"/70\r",end='')
    encoded = dec(i)
    encoded_dict[i] = encoded
    percentage += 1

print("Finished...\n")
#print(encoded_dict)

step = int(input("How many chars each char encrypt to: "))
enc = input("text to decrypt: ")
result = ''


for i in range(0,len(enc),step):
    h = enc[i:i+step]
    for key in encoded_dict:
        if h == encoded_dict[key]:
            result+=key
            break




go(result)












