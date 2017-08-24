import argparse
import getpass
import re
import os

def get_bad_passwords(filepath):
    if not os.path.isfile(filepath):
        bad_passwords = []
    else:
        with open(filepath, 'r', encoding = 'utf-8') as content:
            bad_passwords = [content.read()]
    return bad_passwords

def get_password_strength(password):
    checks = [r'[a-z]', 
              r'[A-Z]', 
              r'\d',    
              r'\W', 
              r'^(?!\S*(\S)\1{3,})',
              r'\S{5,}',
              r'\S{8,}',
              r'\S{10,}']

    password_rate = 0

    if get_bad_passwords(namespace.blacklist_filepath) and\
    password not in get_bad_passwords(namespace.blacklist_filepath):
        password_rate += 2
        print("Not in black list")

    for template in checks:
        if re.findall(template, password):
            password_rate += 1
            print(template, "Passed")
        else:
            print(template, "Not passed")

    return password_rate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('blacklist_filepath', nargs='?', default ='blacklist.txt')
    namespace = parser.parse_args()
    password = input("Password: ")
    #password = getpass.getpass("\nType password to chech its strength: ")
    print("Your password is rated at {} point(s) on a 10-point scale"\
    .format(get_password_strength(password)))

