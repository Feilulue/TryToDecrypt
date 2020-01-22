# Text 4

* Each character is encrypt to 2 hex values
* the second hex is larger than the first hex depending the position of the original char (*e.g. plaintext=1 encrypted=2526 where 26 is 1 larger than 25*)
* Get each char by calculating the difference between each 2 hex numbers of each pair
