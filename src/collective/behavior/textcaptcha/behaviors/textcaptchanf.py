# -*- coding: utf-8 -*-

import logging

from five import grok
# from datetime import datetime
from zope.interface import implements, alsoProvides, Interface
from zope.interface import Invalid
from z3c.form.interfaces import IAddForm
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from string import join
from random import choice

from zope import schema
from z3c.form.form import Form
from z3c.form import validator

from plone.directives import form
# from plone.supermodel import model

from collective.behavior.textcaptcha import MessageFactory as _

logger = logging.getLogger('textcaptchanf')
captcha_value_desc = u"without spaces and without the chars - _"
captcha_input_desc = captcha_value_desc


class CaptchaNotValid(Invalid):

    __doc__ = _(u"Please, enter the good value here !")


class ITextCaptchaNfMarker(Interface):
    """Marker interfacer
    """


class ITextCaptchanf(form.Schema):
    """add text captcha to the content type
    """
    captcha_value = schema.TextLine(title=_(u"Here, the word to be copied"),
                                    description=_(captcha_value_desc),
                                    default=u"th_es e_s",
                                    required=False,
                                    )
    # form.mode(captcha_value='display')

    captcha_input = schema.TextLine(title=_(u"Enter the text above"),
                                    description=_(captcha_input_desc),
                                    )
    form.omitted('captcha_value', 'captcha_input',)
    form.no_omit(IAddForm, 'captcha_value', 'captcha_input',)


alsoProvides(ITextCaptchanf, form.IFormFieldProvider)


class textCaptchanf(Form):
    """La classe du formulaire lui-même, composé seulement de deux champs
    texte, ``captcha_value`` (read only) et ``captcha_input``
    """
    implements(ITextCaptchanf)
    title = _(u"text captcha")
    description = _(u"Provides a new field: a captcha text field")
    ignoreContext = True

    def __init__(self, context):
        self.context = context


class SampleValidator(validator.SimpleFieldValidator):

    def validate(self, value):
        """
        :param value: la chaine contenue dans le champ ``captcha_input``
        :type value: str
        :returns: True ou lève l'exception ``CaptchaNotValid``
        """
        super(SampleValidator, self).validate(value)
        # import pdb;pdb.set_trace()
        form = self.request.form
        captcha_value = form['form.widgets.ITextCaptchanf.captcha_value']
        captcha_input = form['form.widgets.ITextCaptchanf.captcha_input']
        registry = getUtility(IRegistry)
        i = "collective.behavior.textcaptcha.controlpanel"
        i += ".ITextCaptchaSettingsForm.chars_to_remove"
        chars = registry[i]
        goodResultList = [c for c in list(captcha_value)
                          if c not in list(chars)]
        goodResult = join(goodResultList, sep='')
        # logger.info(goodResult)
        if goodResult != captcha_input:
            raise CaptchaNotValid(_(u"The value entered is not correct !"))
        return True


validator.WidgetValidatorDiscriminators(SampleValidator,
                                        field=ITextCaptchanf['captcha_input'])
grok.global_adapter(SampleValidator)


@form.default_value(field=ITextCaptchanf['captcha_value'])
def randomCaptcha(self):
    """
    :returns: un des choix possibles de captcha mis dans le control panel
    """
    registry = getUtility(IRegistry)
    i = "collective.behavior.textcaptcha.controlpanel"
    i += ".ITextCaptchaSettingsForm.captchas"
    captchas = registry[i]
    newCaptcha = choice(captchas)
    return newCaptcha
