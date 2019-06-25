import sys
vow1='aeiouAEIOU'
t='BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
c=input()
if c in vow1:
  print("Vowel")
elif c in t:
  print("Consonant")
else:
  print("invalid")
  
