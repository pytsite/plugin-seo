"""PytSite SEO Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_uwsgi():
    from pytsite import lang, router
    from plugins import settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)

    # Settings
    settings.define('seo', _settings_form.Form, 'seo@seo', 'fa fa-suitcase')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
