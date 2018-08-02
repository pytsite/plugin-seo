"""PytSite SEO Plugin Settings Form.
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings


class TagsWidget(_widget.container.MultiRow):
    def _get_widgets(self):
        return [
            _widget.input.Text(
                uid='name',
                label='Name',
                label_hidden=True,
                rules=_validation.rule.Regex(pattern='^[^"]+$', msg_id='seo@field_cannot_contain_quotes'),
                required=True,
            ),
            _widget.input.Text(
                uid='content',
                label='Content',
                label_hidden=True,
                rules=_validation.rule.Regex(pattern='^[^"]+$', msg_id='seo@field_cannot_contain_quotes'),
            ),
        ]


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(TagsWidget(
            uid='setting_global_metatags',
            label=_lang.t('seo@global_metatags'),
        ))

        super()._on_setup_widgets()
