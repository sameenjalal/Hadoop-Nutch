#!/usr/bin/env python
 

import sys, re
from string import join
 
DEFAULT_RACK = '/rack0'
OTHER_RACK = '/rack1'

 
if len(sys.argv)==1:
    print DEFAULT_RACK
else:
	for i in sys.argv[1:]:
		num = re.compile('.*hadoop([0-9]{2}).*')
		res = num.match(i)
		if res and int(res.group(1))>25:
			print OTHER_RACK
		else:
			print i
