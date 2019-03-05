#!/usr/bin/env python3

from . import hookimpl


@hookimpl
def set_header(message, key, value):
    print('modify received', key, value)
    return message, key, 'changed'
