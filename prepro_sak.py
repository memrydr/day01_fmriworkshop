#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:33 2017

@author: saraappleton-knapp
"""

import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
#Do something cool
    print('Hello data in the path '+basedir)
def main():
#load in all the global variables prepro needs, right now this is just the path to the data
    basedir='/Users/sappleton-knapp/fMRI_workshop/'
    prepro(basedir) #call prepro to do cool things
    
main()
