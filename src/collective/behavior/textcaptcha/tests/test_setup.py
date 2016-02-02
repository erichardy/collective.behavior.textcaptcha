# -*- coding: utf-8 -*-

"""
Code de test très largement inspiré de
https://github.com/collective/collective.behavior.banner
"""
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from plone.app.testing import setRoles, TEST_USER_ID
from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
from plone.dexterity.fti import DexterityFTI
from plone.testing.z2 import Browser
import transaction

from collective.behavior.textcaptcha.testing import\
    TEXTCAPTCHA_FIXTURE_INTEGRATION_TESTING


behav = 'collective.behavior.textcaptcha.'
behav += 'behaviors.textcaptcha.ITextCaptcha'

t1 = u"un premier titre court"
id1 = "un-premier-titre-court"
t2 = 'collective.behavior.textcaptcha behaviors/textcaptcha.py:42:class '
t2 += 'ITextCaptchaMarker(Interface)'
id2 = 'collective-behavior-textcaptcha-behavior'
id3 = id2 + '-1'


class TestExample(unittest.TestCase):

    layer = TEXTCAPTCHA_FIXTURE_INTEGRATION_TESTING

    behaviors = (behav,
                 "plone.app.content.interfaces.INameFromTitle",
                 "plone.app.dexterity.behaviors.metadata.IBasic"
                 )
    portal_type = 'SomeDocument'

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        setRoles(self.portal, TEST_USER_ID, ['Manager', ])

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product
            installed
        """
        pid = 'collective.behavior.textcaptcha'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        # print installed
        self.assertTrue(pid in installed,
                        'package appears not to have been installed')

    def test_textcaptcha(self):
        # self.browser.open(self.portal.absolute_url())
        fti = DexterityFTI(self.portal_type)
        self.portal.portal_types._setObject(self.portal_type, fti)
        fti.klass = 'plone.dexterity.content.Item'
        fti.behaviors = self.behaviors
        # self.portal.invokeFactory(self.portal_type, 'doc1')
        transaction.commit()
        self.browser = Browser(self.app)
        self.browser.open(self.portal.absolute_url() + '/login_form')
        self.browser.getControl(name='__ac_name').value = SITE_OWNER_NAME
        self.browser.getControl(name='__ac_password'
                                ).value = SITE_OWNER_PASSWORD
        self.browser.getControl(name='submit').click()
        self.browser.addHeader(
            'Authorization',
            'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
        )
        setRoles(self.portal, TEST_USER_ID, ['Manager', ])
        self.browser.open(self.portal.absolute_url() + '/++add++SomeDocument')
        self.browser.getControl(name="form.widgets.IBasic.title").value = t1
        # import pdb;pdb.set_trace()
        self.browser.getControl(name="form.buttons.save").click()
        self.assertTrue("Required input is missing" in self.browser.contents)

        captcha_input = "form.widgets.ITextCaptcha.captcha_input"
        self.browser.getControl(name=captcha_input).value = ' blablablabalbl'
        self.browser.getControl(name="form.buttons.save").click()
        incorrect = "The value entered is not correct !"
        self.assertTrue(incorrect in self.browser.contents)

        captcha_value = "form.widgets.ITextCaptcha.captcha_value"
        value = self.browser.getControl(name=captcha_value).value
        val_ok = ''.join([c for c in value if c not in [' ', '-', '_']])
        self.browser.getControl(name=captcha_input).value = val_ok
        self.browser.getControl(name="form.buttons.save").click()
        # print self.browser.contents
        cont = '<span id="breadcrumbs-current">un premier titre court</span>'
        self.assertTrue(cont in self.browser.contents)
        self.assertTrue(id1 in self.portal.keys())
        # import pdb;pdb.set_trace()
