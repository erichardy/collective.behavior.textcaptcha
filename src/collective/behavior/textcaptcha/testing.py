# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
# from plone.app.testing import applyProfile
# from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone import api

from plone.testing import z2

# from zope.configuration import xmlconfig


class ITextCaptchaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.behavior.textcaptcha
        self.loadZCML(package=collective.behavior.textcaptcha)
        """
        xmlconfig.file(
            'configure.zcml',
            collective.behavior.textcaptcha,
            context=configurationContext
        )
        """
        # Install products that use an old-style initialize() function
        # z2.installProduct(app, 'Products.PloneFormGen')
        # z2.installProduct(app, 'collective.behavior.textcaptcha')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        self.installer = api.portal.get_tool('portal_quickinstaller')
        product = 'collective.behavior.textcaptcha'
        self.installer.installProduct(product)
        """
        applyProfile(portal,
                     'collective.behavior.textcaptcha:testing')
        """

TEXTCAPTCHA_FIXTURE = ITextCaptchaLayer()
TEXTCAPTCHA_FIXTURE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TEXTCAPTCHA_FIXTURE,),
    name="ITextCaptchaLayer:Integration"
)
