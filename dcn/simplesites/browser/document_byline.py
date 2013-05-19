from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import plone.app.layout.viewlets.content


class DocumentBylineViewlet(
    plone.app.layout.viewlets.content.DocumentBylineViewlet
    ):

    index = ViewPageTemplateFile("document_byline.pt")
