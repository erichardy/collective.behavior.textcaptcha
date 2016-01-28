# -*- coding: utf-8 -*-

from plone.directives import form
from zope import schema
from plone.app.registry.browser import controlpanel

from collective.behavior.textcaptcha import MessageFactory as _


class ITextCaptchaSettingsForm(form.Schema):
    captchas = schema.List(
        title=_(u"list of captchas"),
        description=_(u"one per line"),
        default=[u't o-t_o', u'_t-it--i'],
        value_type=schema.TextLine(),
        )
    chars_to_remove = schema.TextLine(
        title=_(u"chars to remove"),
        description=_(u"The chars which have to be removed"),
        default=u' -_.?;:,',
        )


class TextCaptchaSettingsForm(controlpanel.RegistryEditForm):
    schema = ITextCaptchaSettingsForm
    label = _(u"Captchas Settings")
    description = _(u"Text captchas settings")

    def updateFields(self):
        super(TextCaptchaSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(TextCaptchaSettingsForm, self).updateWidgets()

cpnwp = controlpanel.ControlPanelFormWrapper


class TextCaptchaSettingsFormSettingsControlPanel(cpnwp):
    form = TextCaptchaSettingsForm
