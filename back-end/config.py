# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-16

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')


class Config(object):
    pass
