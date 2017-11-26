"""PytSite SEO Plugin Event Handlers.
"""
from pytsite import metatag as _metatag
from plugins import settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    for tag in _settings.get('seo.global_metatags', []):
        _metatag.t_set(tag['name'], tag['content'])
