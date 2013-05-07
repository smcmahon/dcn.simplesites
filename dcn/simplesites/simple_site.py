from Acquisition import aq_inner
from five import grok
from zope.component import getMultiAdapter
from plone.directives import dexterity, form

from plone.app.layout.navigation.root import getNavigationRootObject

from Products.CMFCore.utils import getToolByName

from plone.namedfile.interfaces import IImageScaleTraversable

# from zope import schema
# from zope.schema.interfaces import IContextSourceBinder
# from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# from zope.interface import invariant, Invalid

# from z3c.form import group, field

# from plone.namedfile.field import NamedImage, NamedFile
# from plone.namedfile.field import NamedBlobImage, NamedBlobFile

# from plone.app.textfield import RichText

# from z3c.relationfield.schema import RelationList, RelationChoice
# from plone.formwidget.contenttree import ObjPathSourceBinder

# from dcn.simplesites import MessageFactory as _


class ISimpleSite(form.Schema, IImageScaleTraversable):
    """
    Simple SubSite
    """

    form.model("models/simple_site.xml")


class SimpleSite(dexterity.Container):
    grok.implements(ISimpleSite)

    # Add your class methods and properties here


class View(grok.View):
    grok.context(ISimpleSite)
    grok.require('zope2.View')

    def __init__(self, context, request):
        super(View, self).__init__(context, request)
        self.count = 5
        self.state = 'published'
        context = aq_inner(self.context)
        self.portal_state = getMultiAdapter((context, self.request), name='plone_portal_state')

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
