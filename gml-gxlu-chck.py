#!/usr/bin/python

# This Program check if gmail address exist
# Author @BELARBI Samy https://github.com/0x539-Samy
# informations about this exploit found here https://www.4hou.com/posts/xG6B


import argparse
import requests

def check_email(email):
    url = "https://mail.google.com/mail/gxlu?email={0}".format(email)
    r = requests.get(url)
    try:
        if(r.headers['set-cookie'] != ''):
            return email
    except:
            return

#Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--address", help="insert 1 email address ")
args = parser.parse_args()

#check if gmail address exist
if args.address:
    results = check_email("%s" % (args.address))
    if results is None:
        print "%s address not valid" % (args.address)
    else:
        print "%s address valid" % (args.address)