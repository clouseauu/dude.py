#!/usr/bin/env python

import argparse, HTMLParser, re
from urllib2 import urlopen, URLError

# Preface al errors with this, man
errorstring = 'Something is wrong! They\'ve got four more developers working on the program. They got us working in shifts!'

# Aguments
parser = argparse.ArgumentParser(description='Get some filler text to tie your projects together, man!')

parser.add_argument(
	'-p', 
	'--paragraphs',
	dest='paragraphs',
	default=3,
	type=int,
	help='Number of paragraphs to generate (default: 3)'
)

parser.add_argument(
	'-c',
	'--no-cussin',
	dest='cussin',
	action='store_false',
	help='Keep it squeaky clean for client work (default: false)'
)

parser.add_argument(
	'-l',
	'--lebowskiipsum',
	dest='lebowskiipsum',
	action='store_true',
	help='Start the first paragraph with "Lebowski Ipsum" (default: false)'
)

parser.add_argument(
	'-t',
	'--tags',
	dest='html',
	action='store_true',
	help='Wrap your filler text in zee HTML tacs, OK? (default: false)'
)

parser.add_argument(
	'-m',
	'--mixed',
	dest='mixed',
	action='store_true',
	help='Mix Lebowski quotes with old fashioned Lorem Ipsum (default: false)'
)

parser.add_argument(
	'-w',
	'--who',
	dest='who',
	default='all',
	nargs='+',
	help='Specify the characters, separated by spaces. Possible options: dude, walter, stranger, donnie, lebowski, brandt, bunny, jesus, maude, others (default: all)'
)

args = parser.parse_args()

# Cast of characters!
characters =  {
	'dude'		: '1',
	'walter' 	: '2',
	'stranger'	: '3',
	'donnie'	: '4',
	'lebowski'	: '5',
	'brandt'	: '6',
	'bunny'		: '7',
	'jesus'		: '8',
	'maude'		: '9',
	'others'	: '10,11,12,13,14,15,16,17',
}

cast = ','.join([characters[x] for x in args.who if x in characters])

# Form the URL
url = 'http://lebowskiipsum.com/dude/generate/' \
		'paragraphs/{0:d}/' \
		'cussin/{1}/' \
		'mixed/{2}' \
		'/startleb/{3}/' \
		'html/{4}/' \
		'characters/{5}'.format(
			args.paragraphs,
			str(args.cussin).lower(),
			str(args.mixed).lower(),
			str(args.lebowskiipsum).lower(),
			str(args.html).lower(),
			'all' if not len(cast) else cast,
		)

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
