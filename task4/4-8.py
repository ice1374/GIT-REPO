IP = '192.168.3.1'

ar1 = IP.split('.')
ar2 = [int(ar) for ar in ar1]
ar1.clear()

tmpl = '''
{0:>8} {1:>8} {2:>8} {3:>8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print (tmpl.format(ar2[0],ar2[1],ar2[2],ar2[3]))
