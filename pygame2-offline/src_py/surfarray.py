##    pygame - Python Game Library
##    Copyright (C) 2007 Marcus von Appen
##
##    This library is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.
##
##    This library is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Library General Public License for more details.
##
##    You should have received a copy of the GNU Library General Public
##    License along with this library; if not, write to the Free
##    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##
##    Marcus von Appen
##    mva@sysfault.org

"""pygame module for accessing surface pixel data using array interfaces

Functions to convert between NumPy arrays and Surface objects. This module
will only be functional when pygame can use the external NumPy package.
If NumPy can't be imported, surfarray becomes a MissingModule object.

Every pixel is stored as a single integer value to represent the red,
green, and blue colors. The 8bit images use a value that looks into a
colormap. Pixels with higher depth use a bit packing process to place
three or four values into a single number.

The arrays are indexed by the X axis first, followed by the Y
axis. Arrays that treat the pixels as a single integer are referred to
as 2D arrays. This module can also separate the red, green, and blue
color values into separate indices. These types of arrays are referred
to as 3D arrays, and the last index is 0 for red, 1 for green, and 2 for
blue.
"""


from pygame.pixelcopy import (
    array_to_surface,
    surface_to_array,
    map_array as pix_map_array,
    make_surface as pix_make_surface,
)
import numpy
from numpy import (
    array as numpy_array,
    empty as numpy_empty,
    uint32 as numpy_uint32,
    ndarray as numpy_ndarray,
)

import warnings  # will be removed in the future


# float96 not available on all numpy versions.
numpy_floats = []
for type_name in "float32 float64 float96".split():
    if hasattr(numpy, type_name):
        numpy_floats.append(getattr(numpy, type_name))
# Added below due to deprecation of numpy.float. See issue #2814
numpy_floats.append(float)

# Pixel sizes corresponding to NumPy supported integer sizes, and therefore
# permissible for 2D reference arrays.
_pixel2d_bitdepths = {8, 16, 32}


__all__ = [
    "array2d",
    "array3d",
    "array_alpha",
    "array_blue",
    "array_colorkey",
    "array_green",
    "array_red",
    "array_to_surface",
    "blit_array",
    "get_arraytype",
    "get_arraytypes",
    "make_surface",
    "map_array",
    "pixels2d",
    "pixels3d",
    "pixels_alpha",
    "pixels_blue",
    "pixels_green",
    "pixels_red",
    "surface_to_array",
    "use_arraytype",
]


def blit_array(surface, array):
    return None


def make_surface(array):
    return None


def array2d(surface):
    return None


def pixels2d(surface):
    return None


def array3d(surface):
    return None


def pixels3d(surface):
    return None


def array_alpha(surface):
    return None


def pixels_alpha(surface):
    return None


def pixels_red(surface):
    return None


def array_red(surface):
    return None


def pixels_green(surface):
    return None


def array_green(surface):
    return None


def pixels_blue(surface):
    return None


def array_blue(surface):
    return None


def array_colorkey(surface):
    return None


def map_array(surface, array):
    return None


def use_arraytype(arraytype):
    """pygame.surfarray.use_arraytype(arraytype): return None

    DEPRECATED - only numpy arrays are now supported.
    """
    warnings.warn(
        DeprecationWarning(
            "only numpy arrays are now supported, "
            "this function will be removed in a "
            "future version of the module"
        )
    )
    arraytype = arraytype.lower()
    if arraytype != "numpy":
        raise ValueError("invalid array type")


def get_arraytype():
    """pygame.surfarray.get_arraytype(): return str

    DEPRECATED - only numpy arrays are now supported.
    """
    warnings.warn(
        DeprecationWarning(
            "only numpy arrays are now supported, "
            "this function will be removed in a "
            "future version of the module"
        )
    )
    return "numpy"


def get_arraytypes():
    """pygame.surfarray.get_arraytypes(): return tuple

    DEPRECATED - only numpy arrays are now supported.
    """
    warnings.warn(
        DeprecationWarning(
            "only numpy arrays are now supported, "
            "this function will be removed in a "
            "future version of the module"
        )
    )
    return ("numpy",)
