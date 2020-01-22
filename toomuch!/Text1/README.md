# Text 1

* Each character is encrypt to 5 chars of hex
* The first of each is separate from the other 4 and it is at the beginning of the encryptedtext
* The other 4 chars are 2 hex values which the second hex is larger than the first hex depending the position of the original char (*e.g. plaintext=1 encrypted=64445 where 45 is 1 larger than 44*)
* The first char of each encrypted char is placed at the front of the encrypted text, the other 4 is after all the first ones (*e.g. plaintext=0 encrypted=A1111, plaintext=1 encrypted=A2223, plaintext=01 encrypted=AA11112223*)
* Count the length of the encrypted text and dived by 5 to get the length *x* of the plaintext
* Get rid of the first *x* chars in the encrypted text
* Get each char by calculating the difference between each 2 hex numbers of each pair
