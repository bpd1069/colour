#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Shows some **Color** package color *transformations* related examples.
"""

from numpy import matrix
import color

# From wavelength to *CIE XYZ* colorspace.
print(color.wavelength_to_XYZ(480,
                              color.STANDARD_OBSERVERS_COLOR_MATCHING_FUNCTIONS["Standard CIE 1931 2 Degree Observer"]))

# From relative spectral power distribution data to *CIE XYZ* colorspace.
RELATIVE_SPD_DATA = {340: 0.0000,
                     345: 0.0000,
                     350: 0.0000,
                     355: 0.0000,
                     360: 0.0000,
                     365: 0.0000,
                     370: 0.0000,
                     375: 0.0000,
                     380: 0.0000,
                     385: 0.0000,
                     390: 0.0000,
                     395: 0.0000,
                     400: 0.0641,
                     405: 0.0650,
                     410: 0.0654,
                     415: 0.0652,
                     420: 0.0645,
                     425: 0.0629,
                     430: 0.0605,
                     435: 0.0581,
                     440: 0.0562,
                     445: 0.0551,
                     450: 0.0543,
                     455: 0.0539,
                     460: 0.0537,
                     465: 0.0538,
                     470: 0.0541,
                     475: 0.0547,
                     480: 0.0559,
                     485: 0.0578,
                     490: 0.0603,
                     495: 0.0629,
                     500: 0.0651,
                     505: 0.0667,
                     510: 0.0680,
                     515: 0.0691,
                     520: 0.0705,
                     525: 0.0720,
                     530: 0.0736,
                     535: 0.0753,
                     540: 0.0772,
                     545: 0.0791,
                     550: 0.0809,
                     555: 0.0833,
                     560: 0.0870,
                     565: 0.0924,
                     570: 0.0990,
                     575: 0.1061,
                     580: 0.1128,
                     585: 0.1190,
                     590: 0.1251,
                     595: 0.1308,
                     600: 0.1360,
                     605: 0.1403,
                     610: 0.1439,
                     615: 0.1473,
                     620: 0.1511,
                     625: 0.1550,
                     630: 0.1590,
                     635: 0.1634,
                     640: 0.1688,
                     645: 0.1753,
                     650: 0.1828,
                     655: 0.1909,
                     660: 0.1996,
                     665: 0.2088,
                     670: 0.2187,
                     675: 0.2291,
                     680: 0.2397,
                     685: 0.2505,
                     690: 0.2618,
                     695: 0.2733,
                     700: 0.2852,
                     705: 0.0000,
                     710: 0.0000,
                     715: 0.0000,
                     720: 0.0000,
                     725: 0.0000,
                     730: 0.0000,
                     735: 0.0000,
                     740: 0.0000,
                     745: 0.0000,
                     750: 0.0000,
                     755: 0.0000,
                     760: 0.0000,
                     765: 0.0000,
                     770: 0.0000,
                     775: 0.0000,
                     780: 0.0000,
                     785: 0.0000,
                     790: 0.0000,
                     795: 0.0000,
                     800: 0.0000,
                     805: 0.0000,
                     810: 0.0000,
                     815: 0.0000,
                     820: 0.0000,
                     825: 0.0000,
                     830: 0.0000}

# Spectral power distribution, standard observer color matching functions and illuminant shapes must be aligned.
spd = color.SpectralPowerDistribution(name="", spd=RELATIVE_SPD_DATA)
cmfs = color.STANDARD_OBSERVERS_COLOR_MATCHING_FUNCTIONS["Standard CIE 1931 2 Degree Observer"]
illuminant = color.ILLUMINANTS_RELATIVE_SPD["A"]

# Aligning Spectral power distribution and illuminant shapes.
spd = spd.resparse(*cmfs.shape)
illuminant = illuminant.resparse(*cmfs.shape)

print(color.spectral_to_XYZ(spd,
                            cmfs,
                            illuminant))

# Calculating *A* illuminant chromaticity coordinates under *Standard CIE 1931 2 Degree Observer*.
print(color.XYZ_to_xy(color.spectral_to_XYZ(illuminant,
                                            cmfs)))

# Displaying explicit *A* illuminant chromaticity coordinates under *Standard CIE 1931 2 Degree Observer*.
print(color.ILLUMINANTS.get("Standard CIE 1931 2 Degree Observer").get("A"))

# From *CIE XYZ* colorspace to *CIE xyY* colorspace.
print(color.XYZ_to_xyY(matrix([[11.80583421], [10.34], [5.15089229]])))

# Any definitions accepting 3 x 1 matrices will accept a tuple / list input.
print(color.XYZ_to_xyY([11.80583421, 10.34, 5.15089229]))

# Default reference illuminant in case X == Y == Z == 0 is *D50*.
print(color.XYZ_to_xyY(matrix([[0], [0], [0]])))

# Using an alternative illuminant.
print(color.XYZ_to_xyY(matrix([[0], [0], [0]]), color.ILLUMINANTS["Standard CIE 1931 2 Degree Observer"]["D60"]))

# From *CIE xyY* colorspace to *CIE XYZ* colorspace.
print(color.xyY_to_XYZ(matrix([[0.4325], [0.3788], [10.34]])))

# From chromaticity coordinates to *CIE XYZ* colorspace.
print(color.xy_to_XYZ((0.25, 0.25)))

# From *CIE XYZ* colorspace to chromaticity coordinates.
print(color.XYZ_to_xy(matrix([[0.97137399], [1.], [1.04462134]])))

# From *CIE XYZ* colorspace to *RGB* colorspace.
# From *CIE XYZ* colorspace to *sRGB* colorspace.
print(color.XYZ_to_RGB(matrix([[11.51847498], [10.08], [5.08937252]]),
                       color.ILLUMINANTS["Standard CIE 1931 2 Degree Observer"]["D50"],
                       color.sRGB_COLORSPACE.whitepoint,
                       "Bradford",
                       color.sRGB_COLORSPACE.from_XYZ,
                       color.sRGB_COLORSPACE.transfer_function))

# From *RGB* colorspace to *CIE XYZ* colorspace.
# From *sRGB* colorspace to *CIE XYZ* colorspace.
print(color.RGB_to_XYZ(matrix([[3.40552203], [2.48159742], [2.11932818]]),
                       color.sRGB_COLORSPACE.whitepoint,
                       color.ILLUMINANTS["Standard CIE 1931 2 Degree Observer"]["D50"],
                       "Bradford",
                       color.sRGB_COLORSPACE.to_XYZ,
                       color.sRGB_COLORSPACE.inverse_transfer_function))

# From *CIE xyY* colorspace to *RGB* colorspace.
# From *CIE xyY* colorspace to *sRGB* colorspace.
print(color.xyY_to_RGB(matrix([[0.4316], [0.3777], [10.08]]),
                       color.ILLUMINANTS["Standard CIE 1931 2 Degree Observer"]["D50"],
                       color.sRGB_COLORSPACE.whitepoint,
                       "Bradford",
                       color.sRGB_COLORSPACE.from_XYZ,
                       color.sRGB_COLORSPACE.transfer_function))

# From *RGB* colorspace to *CIE xyY* colorspace.
# From *sRGB* colorspace to *CIE xyY* colorspace.
print(color.RGB_to_xyY(matrix([[3.40552203], [2.48159742], [2.11932818]]),
                       color.sRGB_COLORSPACE.whitepoint,
                       color.ILLUMINANTS["Standard CIE 1931 2 Degree Observer"]["D50"],
                       "Bradford",
                       color.sRGB_COLORSPACE.to_XYZ,
                       color.sRGB_COLORSPACE.inverse_transfer_function))

# From *CIE XYZ* colorspace to *CIE UVW* colorspace.
print(color.XYZ_to_UVW(matrix([[0.92193107], [1.], [1.03744246]])))

# From *CIE UVW* colorspace to *CIE XYZ* colorspace.
print(color.UVW_to_XYZ(matrix([[0.61462071], [1.], [1.55775569]])))

# From *CIE UVW* colorspace to *uv* chromaticity coordinates.
print(color.UVW_to_uv(matrix([[0.61462071], [1.], [1.55775569]])))

# From *CIE UVW* colorspace *uv* chromaticity coordinates to *xy* chromaticity coordinates.
print(color.UVW_uv_to_xy((0.19374142046952561, 0.31522110680182841)))

# From *CIE XYZ* colorspace to *CIE Luv* colorspace.
print(color.XYZ_to_Luv(matrix([[0.92193107], [1.], [1.03744246]])))

# From *CIE Luv* colorspace to *CIE XYZ* colorspace.
print(color.Luv_to_XYZ(matrix([[100.], [-20.04304247], [-19.81676035]])))

# From *CIE Luv* colorspace to *uv* chromaticity coordinates.
print(color.Luv_to_uv(matrix([[100.], [-20.04304247], [-19.81676035]])))

# From *CIE Luv* colorspace *uv* chromaticity coordinates to *xy* chromaticity coordinates.
print(color.Luv_uv_to_xy((0.19374142100850045, 0.47283165896209456)))

# From *CIE Luv* colorspace to *CIE LCHuv* colorspace.
print(color.Luv_to_LCHuv(matrix([[100.], [-20.04304247], [-19.81676035]])))

# From *CIE LCHuv* colorspace to *CIE Luv* colorspace.
print(color.LCHuv_to_Luv(matrix([[100.], [28.18559104], [224.6747382]])))

# From *CIE XYZ* colorspace to *CIE Lab* colorspace.
print(color.XYZ_to_Lab(matrix([[0.92193107], [1.], [1.03744246]])))

# From *CIE Lab* colorspace to *CIE XYZ* colorspace.
print(color.Lab_to_XYZ(matrix([[100.], [-7.41787844], [-15.85742105]])))

# From *CIE Lab* colorspace to *CIE LCHab* colorspace.
print(color.Lab_to_LCHab(matrix([[100.], [-7.41787844], [-15.85742105]])))

# From *CIE LCHab* colorspace to *CIE Lab* colorspace.
print(color.LCHab_to_Lab(matrix([[100.], [17.50664796], [244.93046842]])))