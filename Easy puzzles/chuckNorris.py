import binascii

output = ''
message = input()
messageBin = ''.join([bin(ord(i))[2:].zfill(7) for i in message])
isZero = not (messageBin[0] == '0')

for c in messageBin:
    if c == '0' and not isZero:
        isZero = not isZero
        output += ' 00 '
    elif c == '1' and isZero:
        isZero = not isZero
        output += ' 0 '
    output += '0'

print(output.strip())