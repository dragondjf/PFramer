#!/usr/bin/python
# -*- coding: utf-8 -*-


class ObjectDict(dict):
    """
    A ObjectDict object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.
    
        >>> o = ObjectDict(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'
    
    """


    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k
    
    def __setattr__(self, key, value): 
        self[key] = value
    
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k
    
    def __repr__(self):     
        return '<ObjectDict ' + dict.__repr__(self) + '>'


class ObjectDict(dict):

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class ObjectDict(dict):

    '''
        Makes a dictionary behave like an object.
    '''

    def __init__(self, *args, **kw):
        dict.__init__(self, *args, **kw)
        self.__dict__ = self
