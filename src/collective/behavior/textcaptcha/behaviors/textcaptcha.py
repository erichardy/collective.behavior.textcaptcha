import logging

from five import grok
from datetime import datetime
from zope.interface import implements, alsoProvides, Interface
from zope.interface import invariant, Invalid
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from plone.i18n.normalizer.interfaces import INormalizer

from string import join
from random import choice

from zope import schema
from plone.directives import form
from collective.behavior.textcaptcha.controlpanel import ITextCaptchaSettingsForm
from collective.behavior.textcaptcha import MessageFactory as _

logger = logging.getLogger('textcaptcha')



class CaptchaNotValid(Invalid):
    __doc__ = _(u"Please, enter the good value here !")

class ITextCaptchaMarker(Interface):
    """Marker interfacer
    """

class ITextCaptcha(form.Schema):
    """add text captcha to the content type
    """
    captcha_value = schema.TextLine(
                title = _(u"Here, the word to be copied"),
                description = _(u"without spaces and without the chars - _"),
                default = u"toto titi",
                )
    # form.mode(captcha_value='display')
    
    captcha_input = schema.TextLine(
                title = _(u"Enter the text above"),
                description = _(u"without spaces and without the chars - _"),
                # constraint = charsRemoved,
                )
    @invariant
    def charsRemoved(self):
        captcha_value = self.captcha_value
        captcha_input = self.captcha_input
        registry = getUtility(IRegistry)
        chars = registry["collective.behavior.textcaptcha.controlpanel.ITextCaptchaSettingsForm.chars_to_remove"]
        goodResultList = [c for c in list(self.captcha_value) if c not in list(chars) ]
        goodResult = join(goodResultList, sep='')
        # logger.info(goodResult)
        if goodResult != self.captcha_input:
            raise CaptchaNotValid(_(u"The value entered is not correct !"))
        return True
    
alsoProvides(ITextCaptcha, form.IFormFieldProvider)

@form.default_value(field=ITextCaptcha['captcha_value'])
def randomCaptcha(self):
    registry = getUtility(IRegistry)
    captchas = registry["collective.behavior.textcaptcha.controlpanel.ITextCaptchaSettingsForm.captchas"]
    newCaptcha = choice(captchas)
    return newCaptcha

class textCaptcha(object):
    """.
    """
    implements(ITextCaptcha)
    
    def __init__(self, context):
        self.context = context
