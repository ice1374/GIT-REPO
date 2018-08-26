CONFIG	=	'switchport	trunk	allowed	vlan	1,3,10,20,30,100'
varConfig = CONFIG.split(' ')[-1].split(',') # comment
print (CONFIG)
vlans = [int(vlan) for vlan in varConfig if vlan.isdigit()]
print (vlans)