#!/usr/bin/python
""" tweet_up.py is a Python program to upload a image and status in your twitter account """
import sys
from twython import * 
"""``twython`` is the premier Python library providing an easy (and up-to-date) way to access Twitter data. Actively maintained and featuring support for Python 2.6+ and Python 3
"""
def tweet_pic():
  OAUTH_TOKEN = "570688369-Sy7T4dcFEz0nBbjojcuUWKa5w5dqBi4mCWLVSKeo12M0"  # Access Token from twitter app
	OAUTH_TOKEN_SECRET = "rkh8KZF6rfR3LcEbeBplfkrolAJQhiCRJMUYbq2QpoOABnPc"	# Access Secret Token from twitter app
	CONSUMER_KEY = "qYp9N8otRB3dNlDRB2AWLPRFlQ"				# Consumer key of app
	CONSUMER_SECRET = "1bYAvQGrHHD9ye4xGIQMCLOfKhaVurULlIv8qSbcF3DY"	# Consumer Secret of app
	
	pic = open(sys.argv[1], "rb")		# Opening Image in raw bytes 
	try :
		t  = Twython(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) # Access to Twitter Account 
		t.update_status_with_media(media = pic , status = sys.argv[2])		  # Uploading Image along with Status
	
	except:
		print "Authentication Failed"	
if __name__=='__main__':
	main()
