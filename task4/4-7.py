MAC = 'AAAA:BBBB:CCCC'

ar = MAC.replace(':','')

#ar1 = [bin(int(symbol,16)) for symbol in ar]
ar1 = ['{:08b}'.format(int(symbol,16)) for symbol in ar]



print (' '.join(ar1))
#print ('{:8b}'.format(s for s in ar1))