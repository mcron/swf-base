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
from os import path, path as os_path, system as os_system, system, popen, unlink, stat, mkdir, rmdir, makedirs, remove, rename, listdir, environ, walk as os_walk
from Screens.Console import Console
import gettext
import os


def runboot(session, result):
	if result:
		session.open(Console, title = _("Boot Neutrino"),cmdlist = [_("sh '/usr/lib/enigma2/python/Plugins/Extensions/NeutrinoHD2/nhd2boot.sh' en_EN")])

def main(session, **kwargs):
	session.openWithCallback(lambda r: runboot(session, r), MessageBox, _("Do you want to boot Neutrino as default?\n"), MessageBox.TYPE_YESNO, timeout = 20, default = False)


def mainconf(menuid):
    if menuid != "setup":
        return [ ]
    return [(_("Boot Neutrino"), main, "bootneutrino", None)]

def Plugins(**kwargs):
	return [PluginDescriptor(name = _("Boot Neutrino"),
                        description = _("Boot Neutrino as default"),
                        where = PluginDescriptor.WHERE_MENU,
                        fnc = mainconf)]

