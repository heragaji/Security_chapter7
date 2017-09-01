# -*- coding: utf-8 -*-

import os

def run(**args):
    print "[*] In encironment module."
    return str(os.environ)