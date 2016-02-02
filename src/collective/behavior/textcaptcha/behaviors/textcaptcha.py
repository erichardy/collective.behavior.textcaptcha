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
from plone.supermodel import model

from collective.behavior.textcaptcha import MessageFactory as _

logger = logging.getLogger('textcaptcha')
captcha_value_desc = u"without spaces and without the chars - _"
captcha_input_desc = captcha_value_desc


class CaptchaNotValid(Invalid):

    __doc__ = _(u"Please, enter the good value here !")


class ITextCaptchaMarker(Interface):
    """Marker interfacer
    """
# class ITextCaptcha(form.SchemaAddForm):


class ITextCaptcha(form.Schema):
    """add text captcha to the content type
    """
    model.fieldset(
        'captcha',
        label=_(u"captcha"),
        fields=['captcha_value', 'captcha_input']
        )
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


alsoProvides(ITextCaptcha, form.IFormFieldProvider)

"""
def randomCaptchaLabel():
    registry = getUtility(IRegistry)
    i = "collective.behavior.textcaptcha.controlpanel."
    i += "ITextCaptchaSettingsForm.captchas"
    captchas = registry[i]
    newCaptcha = choice(captchas)
    return newCaptcha
"""


class textCaptcha(Form):
    """La classe du formulaire lui-même, composé seulement de deux champs
    texte, ``captcha_value`` (read only) et ``captcha_input``
    """
    implements(ITextCaptcha)
    title = _(u"text captcha")
    description = _(u"Provides a new field: a captcha text field")
    ignoreContext = True

    def __init__(self, context):
        self.context = context

"""
@form.validator(field=ITextCaptcha['captcha_input'],
                context=ITextCaptcha['captcha_value'])
def charsRemovedOK(context):
    # captcha_value = self.captcha_value
    # captcha_input = self.captcha_input
    import pdb;pdb.set_trace()
    registry = getUtility(IRegistry)
    chars = registry["collective.behavior.textcaptcha.controlpanel.\
            ITextCaptchaSettingsForm.chars_to_remove"]

    goodResultList = [c for c in list(self.captcha_value) if c not \
    in list(chars) ]
    goodResult = join(goodResultList, sep='')
    # logger.info(goodResult)
    if goodResult != captcha_input:
        raise CaptchaNotValid(_(u"The value entered for \
        the captcha is not correct !"))

    raise CaptchaNotValid(_(u"The value entered for \
    the captcha is not correct !"))
    return True
"""
"""
NB: Je n'ai pas pu utiliser le processus ci-dessous pourtant decrit a :
http://developer.plone.org/reference_manuals/active/schema-driven-forms/\
customising-form-behaviour/validation.html
au paragraphe : Advanced field widget validators
ca semble marcher en retirant le parametre : view=textCaptcha ...???
"""


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
        captcha_value = form['form.widgets.ITextCaptcha.captcha_value']
        captcha_input = form['form.widgets.ITextCaptcha.captcha_input']
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
                                        field=ITextCaptcha['captcha_input'])
grok.global_adapter(SampleValidator)


@form.default_value(field=ITextCaptcha['captcha_value'])
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
