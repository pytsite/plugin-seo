"""PytSite SEO Plugin.
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, assetman, permissions, settings, events
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='seo')
    assetman.register_package(__name__, alias='seo')

    # Permissions
    permissions.define_permission('seo.manage', 'seo@manage_seo', 'app')

    # Settings
    settings.define('seo', _settings_form.Form, 'seo@seo', 'fa fa-suitcase', 'seo.manage')

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)


_init()
