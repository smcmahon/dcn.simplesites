from Acquisition import aq_inner
from zope.component import getMultiAdapter
from zope.interface import implements
from zope.viewlet.interfaces import IViewlet

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode


class AnalyticsViewlet(BrowserView):
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(AnalyticsViewlet, self).__init__(context, request)

        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

        self.site = getMultiAdapter(
            (aq_inner(self.context), self.request),
            name='ssiteroot'
            )

    def update(self):
        pass

    def render(self):
        """render the webstats snippet"""
        if self.site.in_simple_site():
            return self.site.analytics_code() or ''
        else:
            ptool = getToolByName(self.context, "portal_properties")
            snippet = safe_unicode(ptool.site_properties.webstats_js)
            return snippet
