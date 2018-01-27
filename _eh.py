"""PytSite SEO Plugin Event Handlers.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import metatag as _metatag, reg as _reg


def router_dispatch():
    for tag in _reg.get('seo.global_metatags', []):
        _metatag.t_set(tag['name'], tag['content'])
