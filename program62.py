s=raw_input()
c=0
d=0
for p in s:
      if p=='0' or p== '1':
            c+=1
      else:
      	d+=1
if c>0 and d==0:
       print "yes"
else:
       print "no"
