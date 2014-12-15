#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /Users/Saleh/src/ios/SwiftReminder/Salawat.txt
# print open('/Users/Saleh/src/ios/SwiftReminder/Salawat.txt').read().decode('string-escape').decode("utf-8")
# sed -i 's/;/ /g'

num_lines = sum(1 for line in open("/Users/Saleh/src/0xack13/pyedit/Salawat.txt"))

# if line.rstrip())
num_lines_empty = sum(1 for line in open("/Users/Saleh/src/0xack13/pyedit/Salawat.txt") if line.rstrip())

print num_lines, " Empty: ", num_lines_empty

with open("/Users/Saleh/src/ios/SwiftReminder/Salawat.txt") as f:
    content = f.readlines()	
y = [unicode(i, "utf8") for i in content]
#print y

