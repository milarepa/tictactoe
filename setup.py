#!/usr/bin/python3

"""
Setup file for Project
"""
try:
  from setuptools import setup
except ImportError:
  from distutils.com import setup

config = {
  'name': 'Unbeatable Tick Tack Toe',
  'description': 'Unbeatable Tick Tack Toe',
  'author': 'Benjamin Lehman',
  'URL' : 'https://github.com/milarepa/tictactoe',
  'download URL': 'https://github.com/milarepa/tictactoe',
  'author email': 'resonancetech@gmail.com',
  'version': '0.1',
  'install requires': ['nose'],
  'packages': ['game', 'tests'],

  'scripts': [],
  }

setup(**config)
