# pygame - Python Game Library
# Copyright (C) 2000-2003  Pete Shinners
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Pete Shinners
# pete@shinners.org
"""sysfont, used in the font module to find system fonts"""

import os
import sys
import warnings
from os.path import basename, dirname, exists, join, splitext

from pygame.font import Font

if sys.platform != "emscripten":
    if os.name == "nt":
        import winreg as _winreg
    import subprocess


OpenType_extensions = frozenset((".ttf", ".ttc", ".otf"))
Sysfonts = {}
Sysalias = {}

is_init = False


def _simplename(name):
    """create simple version of the font name"""
    # return alphanumeric characters of a string (converted to lowercase)
    return "".join(c.lower() for c in name if c.isalnum())


def _addfont(name, bold, italic, font, fontdict):
    """insert a font and style into the font dictionary"""
    if name not in fontdict:
        fontdict[name] = {}
    fontdict[name][bold, italic] = font


def initsysfonts_win32():
    return {}


def _parse_font_entry_win(name, font, fonts):
    """
    Parse out a simpler name and the font style from the initial file name.

    :param name: The font name
    :param font: The font file path
    :param fonts: The pygame font dictionary
    """
    true_type_suffix = "(TrueType)"
    mods = ("demibold", "narrow", "light", "unicode", "bt", "mt")
    if name.endswith(true_type_suffix):
        name = name.rstrip(true_type_suffix).rstrip()
    name = name.lower().split()
    bold = italic = False
    for mod in mods:
        if mod in name:
            name.remove(mod)
    if "bold" in name:
        name.remove("bold")
        bold = True
    if "italic" in name:
        name.remove("italic")
        italic = True
    name = "".join(name)
    name = _simplename(name)

    _addfont(name, bold, italic, font, fonts)


def _parse_font_entry_darwin(name, filepath, fonts):
    """
    Parses a font entry for macOS

    :param name: The filepath without extensions or directories
    :param filepath: The full path to the font
    :param fonts: The pygame font dictionary to add the parsed font data to.
    """

    name = _simplename(name)

    mods = ("regular",)

    for mod in mods:
        if mod in name:
            name = name.replace(mod, "")

    bold = italic = False
    if "bold" in name:
        name = name.replace("bold", "")
        bold = True
    if "italic" in name:
        name = name.replace("italic", "")
        italic = True

    _addfont(name, bold, italic, filepath, fonts)


def _font_finder_darwin():
    locations = [
        "/Library/Fonts",
        "/Network/Library/Fonts",
        "/System/Library/Fonts",
        "/System/Library/Fonts/Supplemental",
    ]

    username = os.getenv("USER")
    if username:
        locations.append(f"/Users/{username}/Library/Fonts")

    strange_root = "/System/Library/Assets/com_apple_MobileAsset_Font3"
    if exists(strange_root):
        strange_locations = os.listdir(strange_root)
        for loc in strange_locations:
            locations.append(f"{strange_root}/{loc}/AssetData")

    fonts = {}

    for location in locations:
        if not exists(location):
            continue

        files = os.listdir(location)
        for file in files:
            name, extension = splitext(file)
            if extension in OpenType_extensions:
                _parse_font_entry_darwin(name, join(location, file), fonts)

    return fonts


def initsysfonts_darwin():
    return {}


# read the fonts on unix
def initsysfonts_unix(path="fc-list"):
    return {}


def _parse_font_entry_unix(entry, fonts):
    """
    Parses an entry in the unix font data to add to the pygame font
    dictionary.

    :param entry: A entry from the unix font list.
    :param fonts: The pygame font dictionary to add the parsed font data to.

    """
    filename, family, style = entry.split(":", 2)
    if splitext(filename)[1].lower() in OpenType_extensions:
        bold = "Bold" in style
        italic = "Italic" in style
        oblique = "Oblique" in style
        for name in family.strip().split(","):
            if name:
                break
        else:
            name = splitext(basename(filename))[0]

        _addfont(_simplename(name), bold, italic or oblique, filename, fonts)


def create_aliases():
    """Map common fonts that are absent from the system to similar fonts
    that are installed in the system
    """
    alias_groups = (
        (
            "monospace",
            "misc-fixed",
            "courier",
            "couriernew",
            "console",
            "fixed",
            "mono",
            "freemono",
            "bitstreamverasansmono",
            "verasansmono",
            "monotype",
            "lucidaconsole",
            "consolas",
            "dejavusansmono",
            "liberationmono",
        ),
        (
            "sans",
            "arial",
            "helvetica",
            "swiss",
            "freesans",
            "bitstreamverasans",
            "verasans",
            "verdana",
            "tahoma",
            "calibri",
            "gillsans",
            "segoeui",
            "trebuchetms",
            "ubuntu",
            "dejavusans",
            "liberationsans",
        ),
        (
            "serif",
            "times",
            "freeserif",
            "bitstreamveraserif",
            "roman",
            "timesroman",
            "timesnewroman",
            "dutch",
            "veraserif",
            "georgia",
            "cambria",
            "constantia",
            "dejavuserif",
            "liberationserif",
        ),
        ("wingdings", "wingbats"),
        ("comicsansms", "comicsans"),
    )
    for alias_set in alias_groups:
        for name in alias_set:
            if name in Sysfonts:
                found = Sysfonts[name]
                break
        else:
            continue
        for name in alias_set:
            if name not in Sysfonts:
                Sysalias[name] = found


def initsysfonts():
    return


def font_constructor(fontpath, size, bold, italic):
    return None


# the exported functions


def SysFont(name, size, bold=False, italic=False, constructor=None):
    return None


def get_fonts():
    return []


def match_font(name, bold=False, italic=False):
    return None
