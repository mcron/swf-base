# for localized messages
from . import _
from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console
from Screens.InputBox import InputBox
from Screens.MessageBox import MessageBox 
from Components.Input import Input
from Components.Language import language
from Components.config import config, ConfigSubsection, ConfigYesNo, ConfigLocations, ConfigText, ConfigSelection, getConfigListEntry, ConfigInteger
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext
import os

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os_environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("NeutrinoHD2", resolveFilename(SCOPE_PLUGINS, "Extensions/NeutrinoHD2/locale"))

def _(txt):
	t = gettext.dgettext("NeutrinoHD2", txt)
	if t == txt:
		print "[NeutrinoHD2] fallback to default translation for", txt
		t = gettext.gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)


def runboot(session, result):
	if result:
		session.open(Console, title = _("Boot Neutrino"),cmdlist = [_("sh '/usr/lib/enigma2/python/Plugins/Extensions/NeutrinoHD2/nhd2boot.sh' en_EN")])

def main(session, **kwargs):
	session.openWithCallback(lambda r: runboot(session, r), MessageBox, _("Do you want to boot Neutrino as default?\n"), MessageBox.TYPE_YESNO, timeout = 20, default = True)

def mainconf(menuid):
    if menuid != "setup":
        return [ ]
    return [(_("Boot Neutrino"), main, "bootneutrino", None)]

def Plugins(**kwargs):
	return [PluginDescriptor(name = _("Boot Neutrino"),
                        description = _("Boot Neutrino as default"),
                        where = PluginDescriptor.WHERE_MENU,
                        fnc = mainconf)]

