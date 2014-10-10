import re
flat_list=lambda l:[int(i) for i in re.split('[\\[\\],]',str(l)) if i.strip() and i.strip()!=',']
