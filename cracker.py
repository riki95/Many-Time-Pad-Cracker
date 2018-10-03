#!/usr/bin/env python3

import binascii
import argparse

SPACE = ord(' ')


def main():
    parser = argparse.ArgumentParser(description="Many-time Pad Cracker")
    parser.add_argument("--filename", type=str,
                        help="Name of the file containing the ciphertexts (default: ciphertexts.txt)",
                        default="ciphertexts.txt")
    args = parser.parse_args()
    try:
        with open(args.filename) as f:
            ciphertexts = [binascii.unhexlify(line.rstrip()) for line in f]
        cleartexts = [bytearray(b'?' * len(c)) for c in ciphertexts]
    except Exception as e:
        print("Cannot crack {} --- {}".format(args.filename, e))
        raise SystemExit(-1)
    for k in range(max(len(c) for c in ciphertexts)):
        cts = [c for c in ciphertexts if len(c) > k]
        #TODO
        for rowCTS in cts:
            #print("",current)
            if isSpace(cts,rowCTS[k],k):
                i=0;
                for currentRow in range(len(cleartexts)):
                    if(len(cleartexts[currentRow])!=0 and k<len(cleartexts[currentRow])):
                        result = XOR(rowCTS[k], cts[i][k])
                        if (result==0):
                            cleartexts[currentRow][k]=SPACE
                        elif (chr(result).isupper()):
                            cleartexts[currentRow][k] = ord(chr(result).lower())
                        elif (chr(result).islower()):
                            cleartexts[currentRow][k] = ord(chr(result).upper())
                        i += 1
                break
    
    print("\n".join(c.decode('ascii') for c in cleartexts))

def isSpace(rows,current,coloumn):
    for row in rows:
        result = XOR(current,row[coloumn])
        if not (chr(result).isalpha() or result==0):
            return False
    return True

def XOR(s1,s2):
    return ord(s1)^ord(s2)

if __name__ == "__main__":
    main()

