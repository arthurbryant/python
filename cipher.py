#!/usr/bin/env python
encoded_phrase = ''
print "Enter the sentence to encrypt:",
phrase = raw_input();
print "Enter the shift value:",
shift = input()
result = ''
for c in phrase:
    ascii_code = ord(c)
    if(65 <= ascii_code <=90):
        ascii_code = (ascii_code-65+shift)%26+65
    elif(97 <= ascii_code <=122):
        ascii_code = (ascii_code-97+shift)%26+97
    result += chr(ascii_code)
print "The encoded phrase is:", result

