#! /usr/bin/python

import sys
sys.path.insert(0, "/var/www/flask_RF")
sys.path.insert(0, "/opt/conda/lib/python3.7/site-packages")
sys.path.insert(0, "/opt/conda/bin/")

import os
os.environ["PYTHONPATH"] = "/opt/conda/bin/python"

from flask_RF import app as application