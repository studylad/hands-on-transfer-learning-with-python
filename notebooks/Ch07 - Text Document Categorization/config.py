# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:06:03 2018

@author: tghosh
"""


import pandas as pd
import numpy as np
import os

TEXT_DATA_DIR = 'PATH/TO/DATA_ROOT'

#Dataset from http://ai.stanford.edu/~amaas/data/sentiment/
IMDB_DATA = f'{TEXT_DATA_DIR}aclImdb'
IMDB_DATA_CSV = f'{TEXT_DATA_DIR}imdb_csv'

PROCESSED_20_NEWS_GRP = f'{TEXT_DATA_DIR}20newsgrp'

AMAZON_TRAIN_DATA = f'{TEXT_DATA_DIR}amazonreviews/train.ft'
AMAZON_TEST_DATA = f'{TEXT_DATA_DIR}amazonreviews/test.ft'

GLOVE_DIR = f'{TEXT_DATA_DIR}glove.6B'
WORD2VEC_DIR = f'{TEXT_DATA_DIR}word2vec'

MODEL_DIR = 'PATH/TO/MODELDIR'
