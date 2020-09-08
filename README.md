# NANAKO encoding

**Nanako** is an XML-based binary encoding for the lists of integers developed by me. Especially for the lists of *big* integers.

## How it works

Nanako is a Japanese female name that contains Japanese word 七 *nana* meaning "seven".

Because, in short, the Nanako encoding represents numbers using 7 digits binary block.

It's quite simple: first of all, we translate the integer into binary. Then, while the length of the number is more than 7 digits, we cut out the first 7 digits of the number, add the digit *1* to them at the beginning and so get one byte. The frame is closed with the remainder, which is obviously less than 128 so it's byte starts from *0* as an end-of-frame marker. The length of the remaining part and the sign of the number are stored in the last byte as follows: if the byte value is less than 128, then the encoded number is positive (otherwise, as quite logical, negative), and the remainder of dividing the byte value by 128 is the length of the remainder in the end-of-frame byte.

Examples:

- 54      => `00110110 00000110`
- 127     => `01111111 00000111`
- 128     => `11000000 00000000 00000001`
- 1024    => `11000000 00000000 00000100`
- -999999 => `11111010 10001000 00111111 10000110`