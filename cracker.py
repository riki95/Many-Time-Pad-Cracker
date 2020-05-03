#!/usr/bin/env python3

from typing import List
import binascii
import argparse

SPACE = ord(' ')


def main():
	parser = argparse.ArgumentParser(description='Many-time Pad Cracker')
	parser.add_argument(
		'--filename',
		type=str,
		help='Name of the file containing the ciphertexts (default: ciphertexts.txt)',
		default='ciphertexts.txt'
	)
	parser.add_argument(
		'-K', '--getkey',
		action='store_true',
		help='Print cracked key instead of cracked cleartexts.'
	)
	parser.add_argument(
		'-k', '--key',
		help='Encrypt messages with provided key.',
		default=''
	)
	args = parser.parse_args()
	try:
		with open(args.filename) as file:
			ciphertexts = [binascii.unhexlify(line.rstrip()) for line in file]
	except Exception as e:
		print('Cannot crack {} --- {}'.format(args.filename, e))
		raise SystemExit(-1)
	cleartexts = [bytearray(b'?' * len(line)) for line in ciphertexts]

	if args.key:
		decrypt(ciphertexts, cleartexts, args.key)
	else:
		crack(ciphertexts, cleartexts, args.getkey)


def decrypt(ciphertexts: List[bytes], cleartexts: List[bytearray], input_key: str) -> None:
	""" Decrypt ciphertexts using provided key and print cleartexts """
	key = binascii.unhexlify(input_key.rstrip())
	for row in range(len(ciphertexts)):
		for column in range(len(ciphertexts[row])):
			cleartexts[row][column] = ciphertexts[row][column] ^ key[column % len(key)]
		print(cleartexts[row].decode('ascii'))


def crack(ciphertexts: List[bytes], cleartexts: List[bytearray], getkey: bool) -> None:
	""" Try to decrypt ciphertexts and print cleartexts or key """
	max_length = max(len(line) for line in ciphertexts)
	key = bytearray(max_length)
	key_mask = [False] * max_length
	for column in range(max_length):  # go over characters from the beginning of lines
		pending_ciphers = [line for line in ciphertexts if len(line) > column]
		for cipher in pending_ciphers:
			if is_space(pending_ciphers, cipher[column], column):
				key[column] = cipher[column] ^ SPACE
				key_mask[column] = True
				i = 0
				for clear_row in range(len(cleartexts)):
					if len(cleartexts[clear_row]) != 0 and column < len(cleartexts[clear_row]):
						result = cipher[column] ^ pending_ciphers[i][column]
						if result == 0:
							cleartexts[clear_row][column] = SPACE
						elif chr(result).isupper():  # XOR with space return letter with swapped case
							cleartexts[clear_row][column] = ord(chr(result).lower())
						elif chr(result).islower():  # XOR with space return letter with swapped case
							cleartexts[clear_row][column] = ord(chr(result).upper())
						i += 1
				break
	if getkey:
		for pos in range(max_length):
			if key_mask[pos]:
				print('{0:02x}'.format(key[pos]), end='')
			else:
				print('__', end='')
		print()
	else:
		print('\n'.join(line.decode('ascii') for line in cleartexts))


def is_space(rows: List[bytes], current: int, column: int) -> bool:
	"""
	Return whether the current byte is encrypted space
	If the current byte is space, XORing with other bytes should return alpha char or zero (when space)
	"""
	for row in rows:
		result = row[column] ^ current
		if not (chr(result).isalpha() or result == 0):
			return False
	return True


if __name__ == '__main__':
	main()
