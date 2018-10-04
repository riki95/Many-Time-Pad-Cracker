# Many Time Pad Cracker
A One Time Pad is secure when the key is used once. If we intercept multiple messages encoded with the same key, it is possible to retrieve the original text.

This is what this code does. Given some ciphertexts in input, that you find inside the ciphertext.txt file, the cracker.py decodes them.

## Getting Started

To download my repo:

```
git clone https://github.com/riki95/Many-Time-Pad-Cracker
```

Then just run the cracker.py with a ciphertext.txt file with some chipertext in it. You will find the decoded message on the terminal but you can also export it into a txt output file.

## Note

1) Cleartext messages contain only letters and spaces
2) The key idea to crack this code is considering what happens when a space is XORed with a (uppercase/lowercase) letter. This is what we actually do inside the for cycle

## Authors

* **Riccardo Basso** - *Università degli studi di Genova*
