#!/usr/bin/env python3

from collections import Iterable

from . import hookimpl


@hookimpl
def set_header(message, key, value):
    print('utf8 received', key, value)
    try:
        if isinstance(value, Iterable):
            for v in value:
                value.encode('ascii')
        else:
            value.encode('ascii')
    except UnicodeEncodeError:
        message.charset = 'utf8'
    except AttributeError:
        pass
    return message, key, value
