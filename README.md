# Many Time Pad Cracker
A One Time Pad is secure when the key is used once. If we intercept multiple messages encoded with the same key, it is possible to retrieve the original text.

This is what this code does. Given some ciphertexts in input, that you find inside the ciphertext.txt file, the cracker.py decodes them.

## Getting Started

Clone or download my repository.
Then run the `cracker.py` using **Python 3.6** or greater with a ciphertext.txt file with some chipertext in it. Program will print the decoded message on standard output.

```
usage: cracker.py [-h] [--filename FILENAME] [-K] [-k KEY]

Many-time Pad Cracker

optional arguments:
  -h, --help           show this help message and exit
  --filename FILENAME  Name of the file containing the ciphertexts (default:
                       ciphertexts.txt)
  -K, --getkey         Print cracked key instead of cracked cleartexts.
  -k KEY, --key KEY    Encrypt messages with provided key.
```

## Note

1) Cleartext messages contain only letters and spaces
2) The key idea to crack this code is considering what happens when a space is XORed with a (uppercase/lowercase) letter. This is what we actually do inside the for cycle
3) Ciphertexts in the input and key on the output is raw hexadump of original data where each byte is represented by two ascii symbols [0-f].

## Authors

* **Riccardo Basso** - *Università degli studi di Genova*
* **Vladan Kudláč** - *Brno University of Technology*
