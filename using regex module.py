import re
mynumregex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = mynumregex.search(' number is 888-888-8888.')
print( mo.group(3))
