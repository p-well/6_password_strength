# Password Strength Calculator

The scripts checks strength of your password and rates it on a 10-points scale.

Password's strength estimates by criterions like as following:
- the use of both upper-case and lower-case letters (case sensitivity)
- inclusion of one or more numerical digits
- inclusion of special characters, such as @, #, $
- prohibition of words found in a password blacklist
- password lenght
- absence of repeated symbols more than 2 time

# Quickstart

Python 3 should be already installed.

To run the script clone this repo on your machine and run ```python password_strength.py``` in CLI.
By default script uses list of prohibited passwords stored in ```blacklist.txt```.

You may build your own list of bad passwords. In this case you have to specify filepath as an additional agrument when call script:
```C:\projects\devman\6_password_strength\user_bad_passwords.txt```

Your bad passwords must be stored in *.txt file, each password on a new line.

You may not user this check at all: do no download ```blacklist.txt``` or not prepare own blacklist. The scripts will skip this check,
but your password will not be rated higher than 8 points.

# Example of Script Launch

```
C:\projects\devman\6_password_strength>python password_strength.py

Type password to check its strength:

Your password is rated at 7 point(s) on a 10-point scale

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
