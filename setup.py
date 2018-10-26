"""
Tketris

Tetris using tkinter

Author:  Anshul Kharbanda
Created: 10 - 11 - 2018
"""
from distutils.core import setup

# Setup function
setup(name='tketris',
      version='1.0',
      description='Tetris written in python and tkinter',
      author='Anshul Kharbanda',
      author_email='akanshul97@gmail.com',
      homepage='http://github.com/andydevs/tketris',
      packages=[
        'tketris',
        'tketris.game',
        'tketris.view',
        'tketris.view.side_menu'
      ],
      install_requires=['numpy'])
