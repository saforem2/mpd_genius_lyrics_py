#!/usr/bin/python
import requests
import json
import sys
import urllib2
import urllib
from keys import client_id, secret_key, ACCESS_TOKEN
from mpd import MPDClient


root_url = "https://api.genius.com/oauth/authorize?"
test_song_id = "15953433"



