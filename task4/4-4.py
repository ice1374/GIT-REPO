command1	=	'switchport	trunk	allowed	vlan	1,3,10,20,30,100'
command2	=	'switchport	trunk	allowed	vlan	1,3,100,200,300'

ar1 = set(command1.strip("'").split('	')[-1].split(','))
ar2 = set(command2.strip("'").split('	')[-1].split(','))

#print (ar1)


print(ar1.intersection(ar2))
