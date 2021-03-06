import cgi

from Acquisition import aq_inner
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


class LogoViewlet(ViewletBase):
    index = ViewPageTemplateFile('logo.pt')

    def update(self):
        super(LogoViewlet, self).update()

        context = aq_inner(self.context)

        portal_state = getMultiAdapter(
            (context, self.request),
            name='plone_portal_state'
        )
        portal = portal_state.portal()
        nav_root = getNavigationRootObject(
            context,
            portal
        )

        logoTitle = portal_state.navigation_root_title()
        self.navigation_root_title = logoTitle

        logo = nav_root.page_banner_image
        if logo is None:
            self.logo_tag = """%s""" % cgi.escape(logoTitle)
        else:
            self.logo_tag = """<img
            src="%s/@@images/page_banner_image"
            alt="%s"
            title="%s"
            />""" % (nav_root.absolute_url(), logoTitle, logoTitle)

        # if ISimpleSite.providedBy(nav_root):
        #     logo = nav_root.page_banner_image
        #     if logo is None:
        #         self.logo_tag = """%s""" % logoTitle
        #     else:
        #         self.logo_tag = """<img
        #         src="%s/@@images/page_banner_image"
        #         alt="%s"
        #         title="%s"
        #         />""" % (nav_root.absolute_url(), logoTitle, logoTitle)
        # else:
        #     logoName = 'logo.jpg'
        #     self.logo_tag = portal.restrictedTraverse(logoName).tag(title=logoTitle, alt=logoTitle)
