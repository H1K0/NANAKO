# NANAKO crypt

**Nanako** is an XML-based binary crypt for the lists of integers developed by me. Especially for the lists of *big* integers.

## How it works

<big>※NOTE:</big> works only with natural numbers.

Nanako is a Japanese name that contains Japanese word 七 *nana* meaning "seven".

Because, in short, Nanako crypt represents numbers using 7 digits binary block.

It's quite simple: first of all, we translate the integer into binary. Then, while the length of the number is more than 7 digits, we cut out the first 7 digits of the number, add the digit **1** to them at the beginning and so get one byte. The frame is closed with the remainder, which is obviously less than 128 so it's byte starts from **0** as a marker of the end of the frame, and the length of the remainder in the last byte.

Examples:

- 54     -> `00110110 00000110`
- 128    -> `11000000 00000000 00000001`
- 1024   -> `11000000 00000000 00000100`
- 999999 -> `11111010 10001000 00111111 00000110`