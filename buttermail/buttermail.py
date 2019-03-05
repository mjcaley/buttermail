#!/usr/bin/env python3

import sys

import pluggy

from . import utf8_charset, modify_header_value
from . import spec


# Internet Message Format RFC 5322: https://tools.ietf.org/html/rfc5322
# MIME RFC 2045, RFC 2046, RFC 2047, RFC 4288, RFC 4289 and RFC 2049
# Maybe even RFC 2045-2049

# API replaces (or supplements?) the built-in email API

# Headers:
# To [required]
# Date [required] - spec: https://tools.ietf.org/html/rfc5322#section-3.3
#   [ day-of-week "," ] day month year


# Requirements:
#   Python 3.4
#   Arrow : better datetime library


pm = pluggy.PluginManager('buttermail')
pm.add_hookspecs(spec)
pm.register(utf8_charset)


class MessageBase:
    def __init__(self, hooks=pm.hook):
        self.hooks = hooks
        self.headers = dict()

        self.body = None
        self.content_type = None

    def set_header(self, key, value):
        _, key, value = self.hooks.set_header(message=self, key=key, value=value)[-1]
        self.headers[key] = value


class Message(MessageBase):
    def __init__(self):
        super().__init__()

    # Common headers
    def date(self, date):
        self.set_header('Date', date)
        return self

    def from_(self, address):
        self.set_header('From', address)
        return self

    def to(self, *addresses):
        self.set_header('To', addresses)
        return self

    def cc(self, *addresses):
        self.set_header('Cc', addresses)
        return self

    def bcc(self, *addresses):
        self.set_header('Bcc', addresses)
        return self

    def subject(self, subject):
        self.set_header('Subject', subject)
        return self

    def sender(self, address):
        self.set_header('Sender', address)
        return self

    def reply_to(self, address):
        self.set_header('Reply-To', address)
        return self

    # Convenience methods
    def add_body(self, data, content_type=None):
        self.body = data
        if content_type:
            self.content_type = content_type

    def add_attachment(self, data, content_type=None):
        pass



class CompatibilitySerializer:
    pass


class DefaultSerializer:
    pass


class SubjectMixin:
    def set_date(self, date):
        self.date_ = date
        return self

    @property
    def date(self):
        return self.date_

    @date.setter
    def date(self, date):
        self.set_date(date)



class Part:
    pass
