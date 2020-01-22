import string

li = string.digits+string.ascii_lowercase+string.ascii_uppercase+'-_.,;:?! '


s = '5F70017FDD92B75AA6668648B404223663157787B35686FA165A8193E5075777F'
result = ''
part = s[13::]
for i in range(0,len(part),4):
  a = part[i:i+2]
  b = part[i+2:i+4]
  hexa = int(a,16)
  hexb = int(b,16)
  dif = hexb-hexa
  result += li[dif]
print(result)


