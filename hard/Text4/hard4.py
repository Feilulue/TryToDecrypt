import string

li = string.digits+string.ascii_lowercase+string.ascii_uppercase+'-_.,;:?! '


s = '32632E3149844B82115794BA78AD87C36DA01148707080C65459255C2C6487B02851'
result = ''
for i in range(0,len(s),4):
  a = s[i:i+2]
  b = s[i+2:i+4]
  hexa = int(a,16)
  hexb = int(b,16)
  dif = hexb-hexa
  result += li[dif]
print(result)


