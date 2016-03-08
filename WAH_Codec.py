import math
def getList(x): return [int(i) for i in list(str(x))]

def getGroups(bitlist, wordlength): return [bitlist[i*wordlength : min((i+1)*wordlength, len(bitlist))] for i in range(0,int(math.ceil((len(bitlist)-1)/(wordlength+0.0))))]

def groupCode(group): 
    if (sum(group) == 0): return 0
    elif (sum(group) == len(group)): return 1
    return -1  #mixed group

def conv2bin(x, totlen):
    binnum = [int(i) for i in list(bin(x))[2:]]
    return [0]*(totlen-len(binnum)) + binnum

def doWAHencode(wordlength, bitlist):
    U = getGroups(bitlist, wordlength-1)
    code = []
    run = 0; rundigit = -1
    for i in U[0:-1]:
        if groupCode(i) == -1:
            if run > 0 and rundigit in [0,1]:
                code += [1] + [rundigit] + conv2bin(run, wordlength-2)
            code += [0] + i #literal. no compression
            run = 0
        elif groupCode(i) == 0:
            run += 1; rundigit = 0
        else:
            run += 1; rundigit = 1
    if (run > 0 and rundigit in [0,1]):
        code += [1] + [rundigit] + conv2bin(run, wordlength-2)
    code += U[-1]
    print code
    return ''.join([str(i) for i in code])

def conv2dec(x): #x is a list of 0 and 1s
    return int(''.join([str(i) for i in x]),2)
    
def doWAHdecode(wordlength, bitlist):
    U = getGroups(bitlist, wordlength)
    bitstring = []
    for i in U:
        if i[0] == 1: 
            bitstring += [i[1]] * conv2dec(i[2:]) * (wordlength-1)#compressed 
        else: bitstring += i[1:]
    print bitstring
    return ''.join([str(i) for i in bitstring])

print doWAHencode(16, getList('100000000000000000000000000000000000000000000000000000000000100001100110011111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000100000111'))

print doWAHencode(8, getList('00000000000000000000111110001111111100000000000000000000'))

print doWAHdecode(8, getList('100000100000000101111000110000010100000010000010'))

print doWAHencode(8, getList('1111111111111111010101000000000000001111111100000000'))
#input string
#1111111 1111111 1101010 1000000 0000000 0111111 1100000 000

#encoded string
#11000010
#01101010
#01000000
#10000001
#00111111
#01100000
#000

