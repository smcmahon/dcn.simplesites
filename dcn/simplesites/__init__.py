from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('dcn.simplesites')

available_skins = {
    u'Flexible Layout': 'Sunburst Theme',
    u'Fixed Layout': 'Plone Classic Theme',
}