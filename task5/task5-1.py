#!/usr/bin/env python3

ip_address = input('Enter IP: ')

ipAr = ip_address.replace('/','.').split('.')

arMask = ['1' for i in range(int(ipAr[4]))] + ['0' for i in range(32 - int(ipAr[4]))]
oktet1 = "".join(arMask[0:8])
oktet2 = "".join(arMask[8:16])
oktet3 = "".join(arMask[16:24])
oktet4 = "".join(arMask[24:32])

#print (int(oktet1,2))
#print (int(oktet2,2))
#print (int(oktet3,2))
#print (int(oktet4,2))




tmpl = '''
{0:>8} {1:>8} {2:>8} {3:>8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print ('Network:\n')
print (tmpl.format(int(ipAr[0]),int(ipAr[1]),int(ipAr[2]),int(ipAr[3])))
print ('Network:\n')
print (tmpl.format(int(oktet1,2),int(oktet2,2),int(oktet3,2),int(oktet4,2)))

