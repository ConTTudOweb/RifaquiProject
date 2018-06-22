from django.utils.safestring import mark_safe


class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return mark_safe(u"<a href='%s'>visualizar</a>" % obj.get_absolute_url())
    view_on_site.allow_tags = True
    view_on_site.short_description = u"Visualizar"
