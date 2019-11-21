#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _validate_mail(email):
    name_domain=email.split('@')
    if len(name_domain)!=2:
        return False
    name, domain=name_domain
    # al least 1 character in the name and 4 in the domain, i.e.  a@b.it
    if  len(name)<1 or len(domain)<4:
        return False
    return True


class Contact():
    #@staticmethod
    #def _validate_mail(email):

    def __init__(self, name, email):
        self.name=name
        if _validate_mail(email):
            self.email=email
        else:
            self.email='(missing email)'

    def who_I_am(self):
        return self.name + ' ' + self.email

class Supplier(Contact):
    def order(self,anOrder):
        print("this is your order: ", anOrder)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
