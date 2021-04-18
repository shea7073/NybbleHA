# Implementation of NybbleHA in python

def nybble(message, iv):
    blocks = []
    hashes = []
    for i in range(0, len(message), 2):
        block = '0x' + message[i] + message[i+1]
        hex_block = hex(int(block, 16))
        blocks.append(hex_block)
    hexIV = hex(int('0x' + iv, 16))
    e = hex(int(blocks[0], 16) % int(hexIV, 16))
    hi = hex(int(e, 16) ^ int(hexIV, 16))
    hashes.append(hi)

    for block in blocks[1:]:
        if hi == 1:
            # xor will always result in c (xor of 1 and d)
            # no need to calculate
            hi = '0xc'
            hashes.append(hi)
        elif hi == 0:
            hi = '0xd'
            hashes.append(hi)
        else:
            block = int(block, 16)
            hi = int(str(hi), 16)
            e = block % hi
            if hi > 9:
                hi = hex(hi)
            hi = int(str(e), 16) ^ int(str(hi), 16)
            hashes.append(hex(hi))

    print('The results from each step are {} '.format(str(hashes)))
    print('That means the final tag is {} '.format(str(hashes[-1])))


nybble('B345AD1F', 'D')

