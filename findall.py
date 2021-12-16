import re

fh = open('ips.txt','r')
fstring = fh.readlines()
valid,invalid=[],[]
pat = re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}''')
for line in fstring:
    ip = re.findall( r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line )
    result = pat.search(str(ip[0]))
    if result:
        valid.append(str(ip[0]))
    else:
        invalid.append(str(ip[0]))

print("valid ips",valid)
print("not valid ips",invalid)

