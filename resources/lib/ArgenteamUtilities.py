# -*- coding: utf-8 -*-

import xbmc
import urllib2, ssl
#import re

def log(module, msg):
    xbmc.log((u"### [%s] - %s" % (module, msg,)).encode('utf-8'), level=xbmc.LOGDEBUG)


def geturl(url):
    log(__name__, "Getting url: %s" % url)
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False  
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib2.Request(url, headers={"User-Agent": "Kodi-Addon"}, context=ctx)
        response = urllib2.urlopen(req)
        content = response.read()
        #Fix non-unicode characters in movie titles
        #strip_unicode = re.compile("([^-_a-zA-Z0-9!@#%&=,/'\";:~`\$\^\*\(\)\+\[\]\.\{\}\|\?<>\\]+|[^\s]+)")
        #content = strip_unicode.sub('', content)
        return_url = response.geturl()
    except:
        log(__name__, "Failed to get url: %s" % url)
        content = None
        return_url = None
    return content, return_url
