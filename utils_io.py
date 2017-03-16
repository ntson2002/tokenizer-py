#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import codecs
import json
import logging


def save_object(obj, filename, type="json"):
    if type == "pickle":
        with open(filename, 'wb') as output:
            pickle.dump(obj, output)

    if type == "json":
        with open(filename, 'w') as fp:
            json.dump(obj, fp)


def load_object(path, type="json"):
    '''

    :param filename:
    :param type: {pickle, json}
    :return:
    '''
    if type == "pickle":
        with open(path, 'rb') as input:
            return pickle.load(input)

    if type == "json":
        with codecs.open(path, encoding='utf8') as f:
            return json.load(f)


def get_all_lines(file):
    with open(file) as f:
        return f.readlines()




def create_logger():
    logger = logging.getLogger('myapp')
    hdlr = logging.FileHandler('log.txt')
    # formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    # formatter = logging.Formatter('%(levelname)s %(message)s')
    formatter = logging.Formatter('%(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.WARNING)
    return logger


logger = create_logger()

def get_logger():
    global logger
    return logger