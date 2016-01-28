
================================================
Documentation de collective.behavior.textcaptcha
================================================
.. _IUEM: http://www-iuem.univ-brest.fr
.. _DocPlone: http://docs.plone.org/about/documentation_styleguide_addons.html
.. _Sphinx: http://sphinx-doc.org/
.. _captchas: https://fr.wikipedia.org/wiki/CAPTCHA

Documentation de ``collective.behavior.textcaptcha`` dévéloppé à l'`IUEM`_.

Voir les recommandations pour la documentation à `DocPlone`_

Voir aussi Sphinx : `Sphinx`_


Installation
============
Ajouter *collective.behavior.textcaptcha* à la liste definie par la variable ``eggs`` dans la
section ``[instance]`` du fichier *buildout.cfg*

et la source dans la section ``[sources]``::

   collective.behavior.textcaptcha = git gitiuem:collective.behavior.textcaptcha.git



Usage
=====

Le module collective.behavior.textcaptcha a pour fonction de remplacer les `captchas`_
ordinaires qui font généralement appel à des images dont on doit recopier le textes.

Le principe est simple :

* on crée une liste de mots qui contiennent des caractères comme des espaces, le tiret (``-``)
  ou *underscore* (``_``). Cette liste mise en place par le *Control Panel* de l'instance plone

* on utilise ce *behavior* comme champ complémentaire d'un type de contenu *dexterity*

Dans le formulaire, qui est créé par *dexterity*, deux champs texte apparaissent :

* le champ contenant le captcha à recopier. Par exemple : ``b re-ta_gn e``. Ce champ
  est *Read Only*

* un champ texte où l'utilisateur doit saisir ``bretagne``. Si la saisie n'est
  pas correcte le formulaire ne peut pas être envoyé.


Ce module est utilisé dans les applications suivantes :

* ``ueb.thesesenbretagne``

* ``iuem.proposal``

Pour ces deux applications, des contenus sont créés par des utilisateurs anonymes,
et les formulaires doivent être *protégés* contre les robots.

Le mécanisme de captcha utilisé ici est très simple... peut-être même simpliste,
mais est léger, simple à installer et à configurer.


Toute la documentation
======================

.. toctree::
    :maxdepth: 2

    Le behavior <behavior>
