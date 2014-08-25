#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'chris'
SITENAME = u'Christopher Thomson'
SITEURL = 'https://christopherthomson.github.io'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

TAGLINE = 'Writings and other morsels...'

LOGO_URL = SITEURL + '/theme/img/giraffe2.png'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll

# Social
TWITTER_USERNAME = 'c_thomson'


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

THEME = 'pelican-foundation'
TYPOGRIFY = True

# Plugins
#PLUGIN_PATH = 'plugins/'
#PLUGINS = ('gist', )

# Footer
FOOTER_MESSAGE = 'Powered by <a href="http://getpelican.com/">Pelican</a> and <a href="https://github.com/kfr2/pelican-foundation">Pelican-Foundation</a>. And giraffes. Because we like giraffes.'
