#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Optimal Colour Stimuli - MacAdam Limits
=======================================

Defines objects related to optimal colour stimuli computations.

See Also
--------
`Optimal Colour Stimuli - MacAdam Limits IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/\
blob/master/notebooks/volume/macadam_limits.ipynb>`_
"""

from __future__ import division, unicode_literals

import numpy as np
from scipy.spatial import Delaunay

from colour.models import xyY_to_XYZ
from colour.volume import ILLUMINANTS_OPTIMAL_COLOUR_STIMULI

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['is_within_macadam_limits']

_XYZ_OPTIMAL_COLOUR_STIMULI_CACHE = {}
_XYZ_OPTIMAL_COLOUR_STIMULI_TRIANGULATIONS_CACHE = {}


def _XYZ_optimal_colour_stimuli(illuminant):
    """
    Returns given illuminant optimal colour stimuli in *CIE XYZ* tristimulus
    values and caches it if not existing.

    Parameters
    ----------
    illuminant : unicode
        Illuminant.

    Returns
    -------
    tuple
        Illuminant optimal colour stimuli.
    """

    optimal_colour_stimuli = ILLUMINANTS_OPTIMAL_COLOUR_STIMULI.get(illuminant)

    if optimal_colour_stimuli is None:
        raise KeyError(
            '"{0}" not found in factory optimal colour stimuli: "{1}".'.format(
                illuminant, sorted(ILLUMINANTS_OPTIMAL_COLOUR_STIMULI.keys())))

    cached_ocs = _XYZ_OPTIMAL_COLOUR_STIMULI_CACHE.get(illuminant)
    if cached_ocs is None:
        _XYZ_OPTIMAL_COLOUR_STIMULI_CACHE[illuminant] = cached_ocs = (
            xyY_to_XYZ(optimal_colour_stimuli) / 100)
    return cached_ocs


def is_within_macadam_limits(xyY, illuminant, tolerance=None):
    """
    Returns if given *CIE xyY* colourspace array is within MacAdam limits of
    given illuminant.

    Parameters
    ----------
    xyY : array_like
        *CIE xyY* colourspace array.
    illuminant : unicode
        Illuminant.
    tolerance : numeric, optional
        Tolerance allowed in the inside-triangle check.

    Returns
    -------
    bool
        Is within MacAdam limits.

    Notes
    -----
    -   Input *CIE xyY* colourspace array is in domain [0, 1].
    -   This definition requires *scipy* to be installed.

    Examples
    --------
    >>> is_within_macadam_limits(np.array([0.3205, 0.4131, 0.51]), 'A')
    array(True, dtype=bool)
    >>> a = np.array([[0.3205, 0.4131, 0.51],
    ...               [0.0005, 0.0031, 0.001]])
    >>> is_within_macadam_limits(a, 'A')
    array([ True, False], dtype=bool)
    """

    optimal_colour_stimuli = _XYZ_optimal_colour_stimuli(illuminant)
    triangulation = _XYZ_OPTIMAL_COLOUR_STIMULI_TRIANGULATIONS_CACHE.get(
        illuminant)
    if triangulation is None:
        _XYZ_OPTIMAL_COLOUR_STIMULI_TRIANGULATIONS_CACHE[illuminant] = \
            triangulation = Delaunay(optimal_colour_stimuli)

    simplex = triangulation.find_simplex(xyY_to_XYZ(xyY), tol=tolerance)
    simplex = np.where(simplex >= 0, True, False)

    return simplex
