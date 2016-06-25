#Tornado Libraries
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous, removeslash
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task, coroutine

#Other Libraries

import json
import time
import bson
import datetime
import urllib
import requests
import os
import urllib2
import hashlib
from bson.objectid import ObjectId
import re
import pymongo
from bson import json_util
from motor import MotorClient


db = MotorClient('mongodb://brsrc:brsrc@ds028559.mlab.com:28559/brosource')['brosource']