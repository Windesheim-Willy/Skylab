#import modules
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import pairwise_distances_argmin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
import json

import sqlalchemy
from sqlalchemy import create_engine

import operator
import scipy
import subprocess as sp
import datetime
import sys
from IPython.display import clear_output
from tqdm import tqdm_notebook as tqdm
from string import punctuation
import nltk

import re
from copy import deepcopy
import os
import configparser
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




def keuzemenu_2(keuze1, terug1, keuze2, terug2):
    # Keuzemenu voor twee mogelijkheden
    Starten = True
    while Starten:
        actie = input(" 1 voor " + keuze1 + " of 2 voor " + keuze2 + " :\n ")

        if actie == "1":
            actie = terug1
            Starten = False
        elif actie == "2":
            actie = terug2
            Starten = False
        else:
            Starten = True
            clear_output(wait=True)
            print('Onjuiste keuze\n')

    clear_output(wait=True)
    print('Gekozen voor: ' + actie)
    return actie

