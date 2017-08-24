import argparse
import getpass
import re
import os


def get_bad_passwords(filepath):
    if not os.path.isfile(filepath):
        bad_passwords = []
        return bad_passwords
    with open(filepath, 'r', encoding = 'utf-8') as content:
        bad_passwords = content.read()
        return bad_passwords #str

def get_password_strength(password):
    checks = [r'[a-z]', #any lower case character
              r'[A-Z]', #any upper case character
              r'\d',    #any digit #r'[0-9]'
              r'[\w\s]', #any special symbol except whitespace #r'[^0-9a-zA-Z,^\s]' or r'[^0-9a-zA-Z^\s]'
              r'[?!(\S)\1{3,}]'
              r'.{5,}',
              r'\S{10,}',
              r'\S{15,}']

    password_rate = 0

    if password not in get_bad_passwords(namespace.path):
        password_rate += 1
        print("Not in black list")

    for template in checks:
        if re.search(template, password):
            password_rate += 1
            print(template, "Passed this check")
        else:
            print(template, "Какая-то ерунда")



    return password_rate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file with blacklist passwords')
    namespace = parser.parse_args()

    password = input("Введи пароль")
    #password = getpass.getpass()
    print(get_password_strength(password))

