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

#MAIN_CTA = "Get Uncomfortable"
MAIN_CTA = "Reshape your team"

PATH = 'content'
DISPLAY_PAGES_ON_MENU = True
PAGE_ORDER_BY = 'pageindex'
DISPLAY_CATEGORIES_ON_MENU = False

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


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static files
STATIC_PATHS = ['images', 'pdf', 'root', '_headers', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'},
    'root/apple-app-site-association': {'path': 'apple-app-site-association'}
}


LINKS = (('Privacy Policy', '/pages/privacy.html'), 
    ('Terms of Use', '/pages/legal.html'))

PRODUCTS = (('EQ Nudge', '/pages/products.html#nudge'), 
    ('EQ Words', '/pages/products.html#words'),
    ('EQ Daily', '/pages/products.html#daily'))

NEST_COPYRIGHT = "© 2020 EQ Labs, Inc. All rights reserved."