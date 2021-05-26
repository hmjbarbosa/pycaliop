def CreateColorMap(ColorMap, NumColors = 0):
    #CREATECOLORMAP   Creates a colormap 
    #   [red,grn,blu] = CREATECOLORMAP(ColorMap) takes a ColorMap name (string)
    #   and returns float arrays of red, green and blue colors (0-1) that
    #   compose the map. ColorMap can be one of the following:
    #
    #      'Feature Type'
    #      'Feature Type QA'
    #      'Ice/Water Phase'
    #      'Ice/Water Phase QA'
    #      'Aerosol Sub-Type'
    #      'Cloud Sub-Type'
    #      'PSC Sub-Type'
    #      'Sub-Type'
    #      'Sub-Type QA'
    #      'Averaging Required for Detection'
    #
    #   These correspond to ClassText.FieldDescription returned by
    #   vfm_type(), and have a fixed number of colors to match exactly the
    #   colors used on the CALIPSO website to show these feature flags.
    #
    #   [red,grn,blu] = CREATECOLORMAP(ColorMap, NumColors) works the same
    #   way, but allows one to choose the number of colors. In this case,
    #   only generic linear colormaps are available, which are named:
    #  
    #      'Rainbow' or 'default'
    #      'BlackWhite'
    #      'BlackGold'
    #
    #   History: 
    #      2021-mar-09 Added names for all colormaps associated with standard
    #                  feature flags. NumColors is now the 2nd parameter, and 
    #                  only used for linear colormaps. Colors now match those
    #                  used on the CALIPSO website.
    #      
    #      2005-mar-28 Original code by Ralph Kuehn shared on CALIPO's
    #                  website, from 2005/03/28.
    #

    import numpy as np
    import sys
    import matplotlib as mpl
    
    if (ColorMap == 'Feature Type'):
        red = np.array([255,   0,   0, 255, 250,   0, 192,   0])/255
        grn = np.array([255,  38, 220, 160, 255, 255, 192,   0])/255 
        blu = np.array([255, 255, 255,   0,   0, 110, 192,   0])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'Feature Type QA'):
        red = np.array([ 230, 0, 230, 255,    0, 255])/255
        grn = np.array([ 230, 0,   0, 255,  200,   0])/255
        blu = np.array([ 230, 0,   0,   0,    0, 255])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'Ice/Water Phase'):
        red = np.array([ 192, 255,  255,   0, 169])/255
        grn = np.array([ 255,   0,  255,   0, 169])/255
        blu = np.array([ 168,   0,  255, 255, 169])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'Ice/Water Phase QA'):
        red = np.array([ 192, 255,  255,   0, 169])/255
        grn = np.array([ 255,   0,  255,   0, 169])/255
        blu = np.array([ 168,   0,  255, 255, 169])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'Aerosol Sub-Type'):
        red = np.array([ 198,   0, 250, 255,   0, 174, 0, 255])/255
        grn = np.array([ 198,   0, 255,   0, 128,  87, 0,   0])/255 
        blu = np.array([ 198, 255,   0,   0,   0,   0, 0, 255])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)
                                         
    if (ColorMap == 'Cloud Sub-Type'):
        red = np.array([  0,   0,   0, 144, 255, 255, 192, 255, 255])/255
        grn = np.array([  0,   0, 255, 255, 255, 159, 192, 255,   0])/255 
        blu = np.array([  0, 144, 255, 111,   0,   0, 192, 255, 255])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'PSC Sub-Type'):
        red = np.array([255,   0,   0, 144, 255, 255, 192, 255, 255])/255
        grn = np.array([  0,   0, 255, 255, 255, 159, 192, 255,   0])/255 
        blu = np.array([  0, 144, 255, 111,   0,   0, 192, 255, 255])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'Sub-Type'):
        red = np.array([255,   0,   0, 144, 255, 255, 192, 255, 255])/255
        grn = np.array([  0,   0, 255, 255, 255, 159, 192, 255,   0])/255 
        blu = np.array([  0, 144, 255, 111,   0,   0, 192, 255, 255])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)
                                         
    if (ColorMap == 'Sub-Type QA'):
        red = np.array([ 0, 180, 255])/255
        grn = np.array([ 0, 180, 255])/255
        blu = np.array([ 0, 180, 255])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if (ColorMap == 'Averaging Required for Detection'):
        red = np.array([ 202, 244,   0, 255,   0,   0])/255
        grn = np.array([ 202, 104, 255, 255, 125,   0])/255 
        blu = np.array([ 255,  12,   0,   0,  63, 128])/255 
        cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
        return(cmap)

    if NumColors == 0:
        sys.exit('Advanced colormaps require the NumColors as a parameter.')
        return(null)

    if (ColorMap == 'Rainbow') | (ColorMap == 'default'):
        print('Using Rainbow colormap')
        start_hsv = [300, 1000, 1000]
        final_hsv = [ 15, 1000, 1000]
    elif (ColorMap == 'BlackWhite'):
        print('Using Black and White colormap')
        start_hsv = [0, 0, 1000]
        final_hsv = [0, 0,    0]
    elif (ColorMap == 'BlackGold'):
        print('Using Black and Gold colormap')
        start_hsv = [59, 1000,    0]
        final_hsv = [39,  730, 1000]
    else:
        sys.exit(['Unknown ColorMap. Check input', ColorMap])
        return(cmap)

    Dhue = (final_hsv[0] - start_hsv[0])/NumColors
    Dsat = (final_hsv[1] - start_hsv[1])/NumColors
    Dval = (final_hsv[2] - start_hsv[2])/NumColors

    hue = start_hsv[0]
    sat = start_hsv[1]
    val = start_hsv[2]

    if (ColorMap == 'Rainbow') | (ColorMap == 'default'):
        R = np.zeros((NumColors,1))
        G = np.zeros((NumColors,1))
        B = np.zeros((NumColors,1))
        bluStep = 4
        grnStep = 3.2
        i = 0
        while (hue >= final_hsv[0]):
            [R[i], G[i], B[i]] = HSVtoRGB(round(hue),round(sat),round(val))
            # ColorValue(i)=red*65536+grn*256+blu
            if (hue <= 254) & (hue >= 222):
                hue = hue + Dhue*bluStep
            elif (hue <= 140) & (hue >= 85):
                hue = hue + Dhue*grnStep
            else:
                hue = hue + Dhue
            i = i + 1

        # Copy color info to new array of correct size 
        red = np.ones((i+1,1)) * R[0:i]
        grn = np.ones((i+1,1)) * G[0:i]
        blu = np.ones((i+1,1)) * B[0:i]

    else:
        red = np.zeros((NumColors,1))
        grn = np.zeros((NumColors,1))
        blu = np.zeros((NumColors,1))
        for i in range(NumColors):
            [red[i],grn[i],blu[i]] = HSVtoRGB(round(hue),round(sat),round(val))
            # ColorValue(i)=red*65536+grn*256+blu
            hue = hue + Dhue
            sat = sat + Dsat
            val = val + Dval
            if (hue < 0.0):
                hue = hue + 360
            if (hue > 360.0):
                hue = hue - 360
            # Should use a better convention below because
            # there would be a discontinuity in the colormap
            # if we jump from ~0 to ~1000.
            if (sat < 0.0):
                sat = sat + 1000
            if (sat > 1000):
                sat = sat - 1000
            if (val < 0.0):
                val = val + 1000
            if (val > 1000.0):
                val = val + 1000

    red[0] = 0
    grn[0] = 0
    blu[0] = 0

    red[i] = 1 
    grn[i] = 1
    blu[i] = 1


def HSVtoRGB( h, s, v):
    import numpy as np
    # int i, f
    # int p, q, t
    # s = (s * 0xff) / 1000
    # v = (v * 0xff) / 1000
    ff = 255
    s = (s * ff) / 1000
    v = (v * ff) / 1000
    if (h == 360):
        h = 0
    if (s == 0):
        h = 0
        r = v
        g = v
        b = v
    i = np.floor(h / 60)
    f = np.mod(h,60)
    # p = v * (0xff - s) / 0xff
    # q = v * (0xff - s * f / 60) / 0xff
    # t = v * (0xff - s * (60 - f) / 60) / 0xff
    p = v * (ff - s) / ff
    q = v * (ff - s * f / 60) / ff
    t = v * (ff - s * (60 - f) / 60) / ff
    if i == 0:
      r = v
      g = t
      b = p 
    elif i == 1:
      r = q
      g = v
      b = p 
    elif i == 2:
      r = p
      g = v
      b = t 
    elif i == 3: 
      r = p
      g = q
      b = v
    elif i == 4:
      r = t
      g = p
      b = v
    elif i == 5: 
      r = v
      g = p
      b = q
    else:
      r = ff
      g = ff
      b = ff

    r = r/ff
    g = g/ff
    b = b/ff
  
    return ([r,g,b])
#
