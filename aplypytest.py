#testing some features of APLYpy

import os
import aplpy

filebase1 = 'C:\PhD\IDL\Comet_data\Comet_Lemmon_C2012F6\Gallery'
filestring1 = 'c2012f6_2013_04_21_0345_Rhemann.fits'
filename1 = os.path.join(filebase1, filestring1)

#fig1 = aplpy.FITSFigure(filename1)

filebase2 = 'C:\PhD\IDL\Comet_data\Comet_Kohoutek_C1973E1\Gallery'
#filestring2 = 'c1973e1_1974_01_13_0302_palomar.fits'
filestring2 = 'c1973e1_1974_01_16_0312_stonyridge_solved.fits'
filename2 = os.path.join(filebase2, filestring2)

fig2 = aplpy.FITSFigure(filename2)
fig2.show_grayscale()
