#!/usr/bin/env python

import argparse, HTMLParser, re
from urllib2 import urlopen, URLError

errorstring = 'Something is wrong! They\'ve got four more developers working on the program. They got us working in shifts!'

parser = argparse.ArgumentParser(description='Get some filler text to tie your websites together, man!')

parser.add_argument('-p', '--paragraphs', dest='paragraphs', default=3, type=int, help='Number of paragraphs to generate (default: 3)')
parser.add_argument('-c', '--no-cussin', dest='cussin', action='store_false', help='Keep it squeaky clean for client work (default: false)')
parser.add_argument('-l', '--lebowskiipsum', dest='lebowskiipsum', action='store_true', help='Start the first paragraph with "Lebowski Ipsum" (default: false)')
parser.add_argument('-t', '--tags', dest='html', action='store_true', help='Wrap your filler text in zee HTML tacs, OK? (default: false)')
parser.add_argument('-m', '--mixed', dest='mixed', action='store_true', help='Mix Lebowski quotes with old fashioned Lorem Ipsum (default: false)')

args = parser.parse_args()

url = 'http://lebowskiipsum.com/dude/generate/' \
		'paragraphs/{0:d}/' \
		'cussin/{1}/' \
		'mixed/{2}' \
		'/startleb/{3}/' \
		'html/{4}/' \
		'characters/all'.format(
			args.paragraphs,
			str(args.cussin).lower(),
			str(args.mixed).lower(),
			str(args.lebowskiipsum).lower(),
			str(args.html).lower()
		)


print url

try: 
	data = urlopen(url)

except URLError, e:
	print errorstring
	if hasattr(e, 'reason'):
		print 'Reason: ', e.reason
	elif hasattr(e, 'code'):
		print 'Error code: ', e.code

else:
	html = data.read()
	text = re.search('<textarea(?:.*)id="lebowskiIpsum"(?:\s*)>([\s\S]*)<\/textarea>', html)
	p = HTMLParser.HTMLParser()
	
	try:
		lipsum = p.unescape(text.group(1).decode('utf-8', 'replace'))
	
	except IndexError:
		print errorstring
		print 'Reason: We couldn\'t find the damn text'

	else :
		print lipsum