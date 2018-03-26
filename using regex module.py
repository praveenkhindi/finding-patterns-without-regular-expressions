import re
mynumregex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = mynumregex.search('my number is 886-175-0782.')
print( mo.group(3))
                        
