from zope.i18nmessageid import MessageFactory

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('dcn.simplesites')

# token, value, title
# tokens are what's saved;
# values are the html option values
# titles are presented to user;
# if value is missing, it is taken from token
# if title is missing, it is taken from value

skins_vocab = SimpleVocabulary([
    SimpleTerm('Sunburst Theme', 'flex', title=u'Flexible Layout'),
    SimpleTerm('Plone Classic Theme', 'fixed', title=u'Fixed Layout'),
])

license_vocab = SimpleVocabulary([
    SimpleTerm('None', title=u'None'),
    SimpleTerm('CC BY', title=u'Creative Commons Attribution'),
    SimpleTerm('CC BY-ND', title=u'Creative Commons Attribution, No-Derivatives'),
    SimpleTerm('CC BY-SA', title=u'Creative Commons Attribution, Share-Alike'),
    SimpleTerm('CC BY-NC', title=u'Creative Commons Attribution, Non-Commercial'),
    SimpleTerm('CC BY-NC-ND', title=u'Creative Commons Attribution, Non-Commercial, No-Derivatives'),
    SimpleTerm('CC BY-NC-SA', title=u'Creative Commons Attribution, Non-Commercial, Share-Alike'),
])

license_display = {
    'None': u'',
    'CC BY': """<a rel="license" href="http://creativecommons.org/licenses/by/3.0/us/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/us/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/us/deed.en_US">Creative Commons Attribution 3.0 United States License</a>.""",
    'CC BY-ND': """<a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/us/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nd/3.0/us/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/us/deed.en_US">Creative Commons Attribution-NoDerivs 3.0 United States License</a>.""",
    'CC BY-SA': """<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/us/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/us/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/us/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 United States License</a>.""",
    'CC BY-NC': """<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/us/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc/3.0/us/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/us/deed.en_US">Creative Commons Attribution-NonCommercial 3.0 United States License</a>.""",
    'CC BY-NC-ND': """<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/us/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-nd/3.0/us/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/us/deed.en_US">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 United States License</a>.""",
    'CC BY-NC-SA': """<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/us/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-nd/3.0/us/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/us/deed.en_US">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 United States License</a>.""",
}

site_credit = """This site provided with the assistance of the <a href="http://www2.dcn.org/dcn">Davis Community Network</a>."""