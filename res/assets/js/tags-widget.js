$(window).on('pytsite.widget.init:plugins.seo._settings_form.TagsWidget', function(e, widget) {
    $(window).trigger('pytsite.widget.init:pytsite.widget._base.MultiRow', [widget]);
});
