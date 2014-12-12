# /Users/Saleh/src/ios/SwiftReminder/Salawat.txt
# print open('/Users/Saleh/src/ios/SwiftReminder/Salawat.txt').read().decode('string-escape').decode("utf-8")
# sed -i 's/;/ /g'
with open("/Users/Saleh/src/ios/SwiftReminder/Salawat.txt") as f:
    content = f.readlines()	
y = [unicode(i, "utf8") for i in content]
print y