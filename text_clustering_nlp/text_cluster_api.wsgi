#! /usr/bin/python

import sys
sys.path.insert(0, "/var/www/text_cluster_api")
sys.path.insert(0, "/opt/conda/lib/python3.7/site-packages")
sys.path.insert(0, "/opt/conda/bin/")

import os
os.environ["PYTHONPATH"] = "/opt/conda/bin/python"

from text_cluster_api import app as application