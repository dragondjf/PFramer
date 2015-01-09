#!/usr/bin/python
# -*- coding: utf-8 -*-


__version__ = '2.6'


def _get_publish():
    fd = open("config/settings.json", "r")
    settings_str = fd.read()
    fd.close()
    import json
    settings_obj = json.loads(settings_str)
    return settings_obj['publish']

isPublished = _get_publish()
