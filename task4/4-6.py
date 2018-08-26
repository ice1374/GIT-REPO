ospf_route	=	'O	10.0.24.0/24	[110/41]	via	10.0.13.3,	3d18h,	FastEthernet0/0'

ar = ospf_route.replace(',','').split('	')

print (ar)

ip_template = ''' 

Protocol:             {0:<8}
Prefix:               {1:<8}
AD/Metric:            {2:<8}
Next-Hop:             {3:<8}
Last Update:          {4:<8}
Outbound Interface:   {5:<8}

'''

print (ip_template.format(ar[0].replace('O','OSPF'),ar[1],ar[2],ar[4],ar[5],ar[6]))

