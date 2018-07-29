"""PytSite SEO Plugin Settings Form.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings


class TagsWidget(_widget.container.MultiRow):
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
