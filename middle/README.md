# middle decrypt

**All the easy decryptions can be solved with this script**

* first two can still be solved with the script used in easy
* third one need to be reversed which is an option in the easy script as well

* the rest ones will change the encoded value depends on the position of the character in the plaintext
* I started to guess each character of the string by order by the api provided
* Each character at certain position will encoded to a fixed hex number, so there are only 70*textlength possibilities. Can immediately know once a character is correct, so no need to repeat the guessing of the previous characters.
