from Acquisition import aq_inner
from five import grok
from zope.component import getMultiAdapter
from plone.directives import dexterity, form

from plone.app.layout.navigation.root import getNavigationRootObject

from Products.CMFCore.utils import getToolByName

from plone.namedfile.interfaces import IImageScaleTraversable

# from dcn.simplesites import MessageFactory as _


class ISimpleSite(form.Schema, IImageScaleTraversable):
    """
    Simple SubSite
    """

    form.model("models/simple_site.xml")


class SimpleSite(dexterity.Container):
    grok.implements(ISimpleSite)

    # class methods and properties

    @property
    def site_css_page_bg(self):
        return self.page_bg.encode('utf-8', 'ignore')

    @property
    def site_css_contrast_bg(self):
        return self.contrast_bg.encode('utf-8', 'ignore')

    @property
    def site_css_contrast_fg(self):
        return self.contrast_fg.encode('utf-8', 'ignore')

    @property
    def site_css_alternate_bg(self):
        return self.alternate_bg.encode('utf-8', 'ignore')

    @property
    def site_css_alternate_fg(self):
        return self.alternate_fg.encode('utf-8', 'ignore')

    @property
    def site_css_custom(self):
        return self.custom_css.encode('utf-8', 'ignore')

    # @property
    def site_hides(self):
        hides = []
        if not self.show_search:
            hides.append('#portal-searchbox')
        if not self.show_nav:
            hides.append('#portal-globalnav')
        if not self.show_breadcrumbs:
            hides.append('#portal-breadcrumbs')
        if not self.show_lastmod:
            hides.append('body.userrole-anonymous span.documentModified')
        if not self.show_login:
            portal_membership = getToolByName(self, 'portal_membership')
            if portal_membership.isAnonymousUser():
                hides.append('#portal-personaltools')

        return "%s {display:none}\n" % ', '.join(hides)


class View(grok.View):
    grok.context(ISimpleSite)
    grok.require('zope2.View')

    def __init__(self, context, request):
        super(View, self).__init__(context, request)
        self.count = 5
        self.state = 'published'
        self.portal_state = getMultiAdapter(
            (aq_inner(self.context), self.request),
            name='plone_portal_state'
            )

    def all_news_link(self):
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        if 'news' in getNavigationRootObject(context, portal).objectIds():
            return '%s/news' % self.portal_state.navigation_root_url()
        return None

    def published_news_items(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        path = self.portal_state.navigation_root_path()
        limit = self.count
        state = self.state
        return catalog(portal_type='News Item',
                       review_state=state,
                       path=path,
                       sort_on='Date',
                       sort_order='reverse',
                       sort_limit=limit)[:limit]
