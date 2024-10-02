from splitwise import Splitwise
import logging
import json
import configparser
import os



config = configparser.ConfigParser()

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the config file located one level up
config_file_path = os.path.join(current_dir, '..', 'config', 'config.ini')

# Read the configuration file
config.read(config_file_path)

# Access values from the configuration file
consumer_key = config.get('splitwise', 'consumer_key')
consumer_secret = config.get('splitwise', 'consumer_secret')
api_key = config.get('splitwise', 'api_key')
oauth_token = config.get('splitwise', 'oauth_token')
oauth_verifier = config.get('splitwise', 'oauth_verifier')

print(consumer_key)
print(consumer_secret)
print(api_key)
print(oauth_token)
print(oauth_verifier)

sObj = Splitwise(consumer_key,consumer_secret,api_key)
url, secret = sObj.getAuthorizeURL()

print(secret)

#access_token = sObj.getAccessToken(oauth_token,secret,oauth_verifier)

#print(access_token)

#current = sObj.getCurrentUser()

#json_str = json.dumps(current, indent=4)

#print(json_str)

