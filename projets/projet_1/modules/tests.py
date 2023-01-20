# -*- coding : utf-8 -*-
#! /usr/bin/env python3

import re

str_regrex = ''

REGREX_NAME = re.compile(r'^[a-zA-Z]{2,}[a-zA-Z]$')
REGREX_CALL = re.compile(r'^\+[0-9]{1,3}[ ]?([0-9]{2}[- ]?){4}$')
REGREX_MAIL = re.compile(r'^[a-zA-Z][a-zA-Z0-9-_]+(@){1}[a-zA-Z0-9]{2,}(.){1}[a-zA-Z]{2,4}$')
REGREX_PASSWORD_A = re.compile(r'^[a-zA-Z0-9-_]+$')


def control(regrex, value):
    statu = regrex.search(value)
    return statu is not None

def isName(value):
    return control(REGREX_NAME, value)

def isCall(value):
    return control(REGREX_CALL, value)

def isMail(value):
    return control(REGREX_MAIL, value)

def isPassword_A(value):
    return control(REGREX_PASSWORD_A, value)