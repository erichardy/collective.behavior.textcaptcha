#!/bin/sh
PRODUCTNAME='collective.behavior.textcaptcha'
I18NDOMAIN=$PRODUCTNAME

if [ $USER = 'peretjatko' ]
then
	export PATH="/home/peretjatko/dev-python/mypythontools/bin:$PATH"
fi

if [ $USER = 'hardy' ]
then
	export PATH="/Users/hardy/Dev/mypythontools/bin:$PATH"
fi
# Synchronise the .pot with the templates.
i18ndude rebuild-pot --pot locales/${PRODUCTNAME}.pot --create ${I18NDOMAIN} .

# Synchronise the resulting .pot with the .po files
i18ndude sync --pot locales/${PRODUCTNAME}.pot locales/*/LC_MESSAGES/${PRODUCTNAME}.po
