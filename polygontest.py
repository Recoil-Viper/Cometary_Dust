import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

#filenames/folders - will be generalised later
filedir = r'C:\PhD\IDL\IDL_workingdir'
dataname = 'c2012f6_2013_04_21_0345_Rhemann_test'
filebase = os.path.join(filedir, dataname)

#opening ra and dec of pixels and colors 
#will generalise to process from raw FITS later
ra = np.genfromtxt(filebase + '_ra.csv', delimiter=',')
dec = np.genfromtxt(filebase + '_dc.csv', delimiter=',')

#opening color data and converting to int
colr = np.genfromtxt(filebase + '_colr.csv', delimiter=',')
colr = colr.astype(int)
colg = np.genfromtxt(filebase + '_colg.csv', delimiter=',')
colg = colg.astype(int)
colb = np.genfromtxt(filebase + '_colb.csv', delimiter=',')
colb = colb.astype(int)

sheight = ra.shape[0]
swidth = ra.shape[1]

ramin = np.amin(ra)
ramax = np.amax(ra)
decmin = np.amin(dec)
decmax = np.amax(dec)

pixheight = 800
pixwidth = pixheight*swidth/sheight
border = 100

rascale = pixwidth/(ramax - ramin)
decscale = pixheight/(decmax - decmin)


test = Image.new('RGBA', (pixwidth+(2*border),pixheight+(2*border))\
,(0,0,0,0))
d = ImageDraw.Draw(test)
a = d.polygon([(border,border),(border+pixwidth,border), \
(border+pixwidth,border+pixheight),(border,border+pixheight)], \
outline = (255,255,255,128))
for x in xrange(0, sheight-2):
    for y in xrange(0, swidth-2):
        ra1 = border + (ra[x,y]-ramin)*rascale
        ra2 = border + (ra[x+1,y]-ramin)*rascale
        ra3 = border + (ra[x+1,y+1]-ramin)*rascale
        ra4 = border + (ra[x,y+1]-ramin)*rascale
        dec1 = pixheight + border - (dec[x,y]-decmin)*decscale
        dec2 = pixheight + border - (dec[x+1,y]-decmin)*decscale
        dec3 = pixheight + border - (dec[x+1,y+1]-decmin)*decscale
        dec4 = pixheight + border - (dec[x,y+1]-decmin)*decscale
        a = d.polygon([(ra1,dec1),(ra2,dec2),(ra3,dec3),(ra4,dec4)] ,\
        fill=(colr[x,y],colg[x,y],colb[x,y],128))
test.show()






#imgname = 'doge.png'
#imgfull = os.path.join(filedir, imgname)
#
#base = Image.open(imgfull).convert('RGBA')
#txt = Image.new('RGBA', base.size, (255,255,255,0))
#txt.show()