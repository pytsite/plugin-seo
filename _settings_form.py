"""PytSite SEO Plugin Settings Form.
"""
from pytsite import widget as _widget, lang as _lang, settings as _settings, validation as _validation

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class TagsWidget(_widget.MultiRow):
    def __init__(self, uid: str, **kwargs):
        super().__init__(uid, **kwargs)

        self.assets.append('seo@js/tags-widget.js')

    def _get_headers_row(self):
        return 'Name', 'Content'

    def _get_widgets_row(self):
        return [
            _widget.input.Text(
                uid='name',
                rules=[
                    _validation.rule.NonEmpty(),
                    _validation.rule.Regex(pattern='^[^"]+$', msg_id='seo@field_cannot_contain_quotes')
                ],
            ),
            _widget.input.Text(
                uid='content',
                rules=_validation.rule.Regex(pattern='^[^"]+$', msg_id='seo@field_cannot_contain_quotes'),
            ),
        ]


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(TagsWidget(
            uid='setting_global_metatags',
            weight=10,
            label=_lang.t('seo@global_metatags'),
        ))

        super()._on_setup_widgets()
