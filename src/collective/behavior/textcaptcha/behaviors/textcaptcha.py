import logging

from five import grok
from datetime import datetime
from zope.interface import implements, alsoProvides, Interface
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import INormalizer

from zope import schema
from plone.directives import form

from collective.behavior.textcaptcha import MessageFactory as _

logger = logging.getLogger('textcaptcha')

class ITextCaptchaMarker(Interface):
    """Marker interfacer
    """

class ITextCaptcha(form.Schema):
    """add text captcha to the content type
    """
    captcha_value = schema.TextLine(
                                    title = _(u"Here, the word to be copied"),
                                    description = _(u"without spaces and without the chars - _"),
                                    default = u"un texte a copier",
                                    )
    # form.mode(captcha_value='display')
    
    captcha_input = schema.TextLine(
                                    title = _(u"Enter the text above"),
                                    description = _(u"without spaces and without the chars - _"),
                                    )
    
    
alsoProvides(ITextCaptcha, form.IFormFieldProvider)

class textCaptcha(object):
    """.
    """
    implements(ITextCaptcha)
    
    def __init__(self, context):
        self.context = context
        
