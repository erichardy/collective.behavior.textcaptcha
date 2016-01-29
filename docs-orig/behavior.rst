

===========================================
Le behavior collective.behavior.textcaptcha
===========================================

Configuration zcml
------------------

Le point de départ, le fichier ``configure.zcml`` qui contient d'une part la
déclaration de la vue du control panel::

   <browser:page
     name="textcaptcha-settings"
     for="Products.CMFPlone.interfaces.IPloneSiteRoot"
     class=".controlpanel.TextCaptchaSettingsFormSettingsControlPanel"
     permission="cmf.ManagePortal"
   />

d'autre part l'appel à un autre fichier zcml::

   <include file="behaviors.zcml" />

qui contient la déclaration du behavior lui-même::

    <plone:behavior
        title="text captcha"
        description="Provides a new field: a captcha text field"
        provides=".behaviors.textcaptcha.ITextCaptcha"
        factory=".behaviors.textcaptcha.textCaptcha"
        marker=".behaviors.textcaptcha.ITextCaptchaMarker"
        />


Le code
-------


.. automodule:: collective.behavior.textcaptcha.behaviors.textcaptcha
   :members:
   :undoc-members:

   
   