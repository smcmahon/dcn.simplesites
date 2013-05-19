from Acquisition import aq_inner
from zope.component import getMultiAdapter
from Products.Five.browser import BrowserView

from plone.app.layout.navigation.root import getNavigationRootObject

import dcn.simplesites
from dcn.simplesites.simple_site import ISimpleSite


class SiteRootView(BrowserView):
    """
    Expose properties of simplesite root object that are useful
    in viewlets of contained objects.
    """

    def __init__(self, context, request):
        super(SiteRootView, self).__init__(context, request)

        self.portal_state = getMultiAdapter(
            (aq_inner(self.context), self.request),
            name='plone_portal_state'
        )
        self.nav_root = getNavigationRootObject(
            context,
            self.portal_state.portal()
        )
        self.is_simple_site = ISimpleSite.providedBy(self.nav_root)

    def in_simple_site(self):
        return self.is_simple_site

    def site_title(self):
        if self.is_simple_site:
            return self.nav_root.Title
        else:
            return self.portal_state.portal_title()

    def enable_tweet(self):
        return getattr(self.nav_root, 'enable_tweet', False)

    def enable_fblike(self):
        return getattr(self.nav_root, 'enable_fblike', False)

    def public_contact(self):
        return getattr(self.nav_root, 'public_contact', False)

    def license(self):
        lic = getattr(self.nav_root, 'license', u'None')
        if lic == u'None':
            return u''
        return dcn.simplesites.license_display.get(lic, '')

    def analytics_code(self):
        return getattr(self.nav_root, 'analytics_code', u'')

    def page_footer(self):
        footer = getattr(self.nav_root, 'page_footer', None)
        if footer:
            return footer.output
        else:
            return u''

    def site_credit(self):
        credit = getattr(self.nav_root, 'credit_dcn', None)
        if credit:
            return dcn.simplesites.site_credit
        else:
            return u''

    def dbOrgId(self):
        return getattr(self.nav_root, 'dbOrgId', 0)

    def hideLogin(self):
        # should we display the log-in prompt?

        if not getattr(self.nav_root, 'show_login', True):
            if getToolByName(self.context, "portal_membership").isAnonymousUser():
                return True
        return False
