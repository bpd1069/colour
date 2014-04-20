#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**sLog.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines **Color** package *S-Log* colorspace.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***    External imports.
#**********************************************************************************************************************
import math
import numpy

#**********************************************************************************************************************
#***	Internal Imports.
#**********************************************************************************************************************
import color.derivation
import color.exceptions
import color.illuminants
import color.verbose
from color.colorspaces.colorspace import Colorspace

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER",
		   "S_LOG_PRIMARIES",
		   "S_LOG_WHITEPOINT",
		   "S_LOG_TO_XYZ_MATRIX",
		   "XYZ_TO_S_LOG_MATRIX",
		   "S_LOG_TRANSFER_FUNCTION",
		   "S_LOG_INVERSE_TRANSFER_FUNCTION",
		   "S_LOG_COLORSPACE"]

LOGGER = color.verbose.installLogger()

#**********************************************************************************************************************
#*** *S-Log*
#**********************************************************************************************************************
# http://pro.sony.com/bbsccms/assets/files/mkt/cinema/solutions/slog_manual.pdf
S_LOG_PRIMARIES = numpy.matrix([0.73, 0.28,
								0.14, 0.855,
								0.10, -0.05]).reshape((3, 2))

S_LOG_WHITEPOINT = color.illuminants.ILLUMINANTS.get("Standard CIE 1931 2 Degree Observer").get("D65")

S_LOG_TO_XYZ_MATRIX = color.derivation.getNormalizedPrimaryMatrix(S_LOG_PRIMARIES, S_LOG_WHITEPOINT)

XYZ_TO_S_LOG_MATRIX = S_LOG_TO_XYZ_MATRIX.getI()

def __sLogTransferFunction(RGB):
	"""
	Defines the *S-Log* colorspace transfer function.

	:param RGB: RGB Matrix.
	:type RGB: Matrix (3x1)
	:return: Companded RGB Matrix.
	:rtype: Matrix (3x1)
	"""

	RGB = map(lambda x: (0.432699 * math.log10(x + 0.037584) + 0.616596) + 0.03, numpy.ravel(RGB))
	return numpy.matrix(RGB).reshape((3, 1))

def __sLogInverseTransferFunction(RGB):
	"""
	Defines the *S-Log* colorspace inverse transfer function.

	:param RGB: RGB Matrix.
	:type RGB: Matrix (3x1)
	:return: Companded RGB Matrix.
	:rtype: Matrix (3x1)
	"""

	RGB = map(lambda x: (math.pow(10., ((x - 0.616596 - 0.03) / 0.432699)) - 0.037584), numpy.ravel(RGB))
	return numpy.matrix(RGB).reshape((3, 1))

S_LOG_TRANSFER_FUNCTION = __sLogTransferFunction

S_LOG_INVERSE_TRANSFER_FUNCTION = __sLogInverseTransferFunction

S_LOG_COLORSPACE = Colorspace("S-Log",
							  S_LOG_PRIMARIES,
							  S_LOG_WHITEPOINT,
							  S_LOG_TO_XYZ_MATRIX,
							  XYZ_TO_S_LOG_MATRIX,
							  S_LOG_TRANSFER_FUNCTION,
							  S_LOG_INVERSE_TRANSFER_FUNCTION)