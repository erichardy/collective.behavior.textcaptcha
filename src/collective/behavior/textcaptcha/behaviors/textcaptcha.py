import logging

from five import grok

from zope.interface import alsoProvides, Interface
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import INormalizer

from collective.behavior.textcaptcha import MessageFactory as _

logger = logging.getLogger('textcaptcha')

class ITextCaptchaMarker(Interface):
    """Marker interfacer
    """

class ITextCaptcha(Interface):
    """object Id will be shortened if it is too long
    """
    
alsoProvides(ITextCaptcha)

class textCaptcha(object):
    """.
    """
    grok.implements(ITextCaptcha)
    grok.context(ITextCaptchaMarker)
    
    def __init__(self, context, event):
        self.context = context
        event_type = str(type(event))
        if event_type == "<class 'zope.lifecycleevent.ObjectCreatedEvent'>":
            self.setShortId(context)
        
    def setShortId(self, context):
        normalizer = getUtility(INormalizer)
        completeId = normalizer.normalize(context.title, locale = 'fr')
        newId = completeId
        if len(completeId) > 40:
            newId = completeId[:40]
            
        context.id = newId
