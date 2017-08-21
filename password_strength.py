import argparse
import getpass
import re
import os

def get_bad_passwords_list(filepath):
    if not os.path.isfile(filepath):
        bad_passwords = []
        return bad_passwords
    with open(filepath, 'r', encoding = 'utf-8') as content:
        bad_passwords = content.read()
        return bad_passwords #str

def get_password_strength(password):
    checks = [r'[a-z]',
              r'[A-Z]',
              r'\d'
              r'[^0-9a-zA-Z]'
              r'\S{5,}',
              r'\S{10,}',
              r'\S{15,}',





            ]




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file with blacklist passwords')
    namespace = parser.parse_args()

    get_bad_passwords_list(namespace.path)

    #password = getpass.getpass()

