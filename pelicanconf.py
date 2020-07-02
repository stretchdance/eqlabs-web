#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Joshua McKenty'
SITENAME = 'EQ Labs'
# SITEURL = 'https://dev.eqlabs.io'
SITEURL = ''
# THEME = "/Users/joshuamckenty/pelican-themes/Flex"
THEME = "nest"

NEST_HEADER_LOGO = '/images/logo.png'
NEST_HEADER_IMAGES = 'pxfuel.com.jpg'
NEST_INDEX_HEAD_TITLE = 'Tools for Inclusive Workplaces'
NEST_INDEX_HEADER_TITLE = 'Overcome Bias in the Workplace'
NEST_INDEX_HEADER_SUBTITLE = 'PRACTICAL TOOLS FOR MANAGERS'

PATH = 'content'
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'pageindex'
DISPLAY_CATEGORIES_ON_MENU = False
# MENUITEMS = (('Extra Item', '/extra'),)

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NEST_SITEMAP_COLUMN_TITLE = 'Sitemap here'
EQ_PRIMARY_ADDRESS = '4326 3rd Ave NW<br/>Seattle, WA<br/>98107'

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}

NEST_COPYRIGHT = "© 2020 EQlabs. All rights reserved."