#!/usr/bin/python
import requests
import json
import sys
import urllib2
import urllib
from mpd import MPDClient

client_id= "DDLsThHvDfYJe2fNerOXijYeQDrfual8VlYBD0JuM0C3e87eK1D1Bvc0fM1kN4iI"
secret_key = "6IGbdtdRd21N_MOfXHzQffn_9KHM667SHdArlbIdcJMcIEIuunBFr08bqpf1DM1Pnn2buC43e3MgnQO0pla8DQ"
ACCESS_TOKEN = "eJpal9fCWxXHbtppnRNT4rxb9YHunOiLEg0u5gWiEEJsw9FgpVdpqsqrKkP_leTk"

auth_url = "https://api.genius.com/oauth/authorize?\\
            client_id=DDLsThHvDfYJe2fNerOXijYeQDrfual8VlYBD0JuM0C3e87eK1D1Bvc0fM1kN4iI\\
            response_type=code"

API_BASE = "https://api.genius.com/"
SEARCH_BASE = API_BASE+"artists/"
SONG_BASE = API_BASE+"songs/"
URL_PARAM_ENCODER = urllib.quote_plus
RESPONSE_KEY = "response"
SEARCH_RESULTS_ARRAY_KEY = "hits"
ARTIST_KEY = "artist"
SONG_KEY = "song"
TEXT_FORMAT = "?text_format=plain"  # TODO - make customizable.
                                    # Genius formats: plain, html, DOM
PLAINTEXT_DESCRIPTION_KEY = "plain"

def build_opener(access_token = ACCESS_TOKEN):
    opener = urllib.build_opener()
    opener.addheaders = [("Authorization", "Bearer "+access_token)]
    #opener.addheaders = [("User-Agent", "curl/7.50.1")]



