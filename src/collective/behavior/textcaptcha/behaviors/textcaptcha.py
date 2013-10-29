import logging

from five import grok

from zope.interface import alsoProvides, Interface
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import INormalizer

from zope import schema
from plone.directives import form

from collective.behavior.textcaptcha import MessageFactory as _

logger = logging.getLogger('textcaptcha')

class ITextCaptchaMarker(Interface):
    """Marker interfacer
    """

class ITextCaptcha(Interface):
    """add text captcha to the content type
    """
    captcha_input = schema.TextLine(
                                    title = _u("Enter the text above"),
                                    description = _u("without spaces and without the chars - _"),
                                    )
    
alsoProvides(ITextCaptcha)

class textCaptcha(form.Schema):
    """.
    """
    grok.implements(ITextCaptcha)
    grok.context(ITextCaptchaMarker)
    
    def __init__(self, context, event):
        self.context = context
        
