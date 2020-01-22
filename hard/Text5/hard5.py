import string

li = string.digits+string.ascii_lowercase+string.ascii_uppercase+'-_.,;:?! '


s = '5D2EAF346C9271B7489BBA3A52326752248C2255826771378D741E48205A'
half = int(len(s)/2)
s1 = s[0:half]
s2 = s[half::]
result = ''

for i in range(0,half,2):
  a = s1[i:i+2]
  b = s2[i:i+2]
  hexa = int(a,16)
  hexb = int(b,16)
  dif = hexa-hexb
  result += li[dif]
print(result)


