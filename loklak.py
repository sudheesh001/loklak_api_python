#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import copy
import math
import sys
import time
from collections import namedtuple
import requests

class Loklak (object):
	baseUrl = 'http://loklak.org/api/'

	def __init__(self):
		print "You haven't called a function yet, but looks like you've created an object"
	


def main():
	"""
		Command line interface
	"""
	import argparse
	import os
	import multiprocessing

	parser = argparse.ArgumentParser(description="Python wrapper around the loklak API.")
	parser.add_argument('-s', '--search', action='store_true', help='Search API Wrapper which helps to query loklak for JSON results.')
	parser.add_argument('-t', '--status', action='store_true', help='Status API Wrapper for the loklak status check.')
	parser.add_argument('-st', '--suggest', action='store_true', help='Suggestions API Wrapper , Works better with local loklak instance.')
	parser.add_argument('-c', '--crawler', action='store_true', help='Crawler API Wrapper on Loklak to crawl for tweets for a particular crawl depth.')
	parser.add_argument('-h', '--hello' , action='store_true', help='Loklak status check API.')
	parser.add_argument('-g', '--geocode', action='store_true', help='Geocode API for geolocation based information.')
	parser.add_argument('-p', '--peers', action='store_true', help='Loklak API for peers connected on the distributed network.')
	parser.add_argument('-pg', '--pushgeojson', action='store_true', help='Public API to push geojson objects to the loklak server.')
	parser.add_argument('-u', '--user', action='store_true', help='User API to show twitter user information.')
	parser.add_argument('-m', '--map', action='store_true', help='Map Visualization render using Loklak service.')
	parser.add_argument('-md', '--markdown', action='store_true', help='Markdown conversion API to render markdown as image using Loklak.')
	args = parser.parse_args()
