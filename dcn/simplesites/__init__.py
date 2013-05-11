from zope.i18nmessageid import MessageFactory

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('dcn.simplesites')

# token, value, title
# tokens are what's saved;
# values are the html option values
# titles are presented to user;
# if value is missing, it is taken from token

skins_vocab = SimpleVocabulary([
    SimpleTerm('Sunburst Theme', 'flex', title=u'Flexible Layout'),
    SimpleTerm('Plone Classic Theme', 'fixed', title=u'Fixed Layout'),
])

license_vocab = SimpleVocabulary([
    SimpleTerm('None', title=u'None'),
    SimpleTerm('CC BY', title=u'Creative Commons Attribution'),
    SimpleTerm('CC BY-SA', title=u'Creative Commons Attribution, Share-Alike'),
    SimpleTerm('CC BY-NC', title=u'Creative Commons Attribution, Non-Commercial'),
    SimpleTerm('CC BY-NC-SA', title=u'Creative Commons Attribution, Non-Commercial, Share-Alike'),
])
