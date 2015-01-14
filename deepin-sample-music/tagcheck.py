#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eyed3

audiofile = eyed3.load("郭一凡_说走就走的旅行.mp3")
print(audiofile.tag.artist)
print(audiofile.tag.title)
print(audiofile.tag.album)
print(audiofile.tag.album_artist)
print(audiofile.tag.track_num)
print(dir(audiofile.tag))
