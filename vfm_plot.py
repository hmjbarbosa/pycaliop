def vfm_plot(vfm, xs, y, imgSize = [1300, 667], dpi=96):

    import matplotlib as mpl
    import matplotlib.ticker as mtk
    import matplotlib.pyplot as plt
    import numpy as np
    import sys
    import imp
    import CreateColorMap
    imp.reload(CreateColorMap)

    # Determine or set image size
    if len(imgSize) != 2:
        sys.error('imgSize is not of a usable size. Must be of length 2, it is ' + np.shape(imgSize));

    axpos = np.array([0.062, 0.121, 0.837, 0.788])

    # Create Figure & set size
    #fig = plt.figure(num=1, figsize=np.float64(imgSize)/dpi, dpi=dpi, clear=True)
    fig = plt.figure(figsize=np.float64(imgSize)/dpi, dpi=dpi, clear=True)
    ax0 = fig.add_subplot(111)
    ax0.set_position(pos=axpos)

    cmap = CreateColorMap.CreateColorMap(vfm['FieldDescription'])
    #cmap = CreateColorMap.CreateColorMap('Feature Type QA')
    #cmap = CreateColorMap.CreateColorMap('Ice/Water Phase')
    #cmap = CreateColorMap.CreateColorMap('Ice/Water Phase QA')
    #cmap = CreateColorMap.CreateColorMap('Aerosol Sub-Type')
    #cmap = CreateColorMap.CreateColorMap('Cloud Sub-Type')
    #cmap = CreateColorMap.CreateColorMap('PSC Sub-Type')
    #cmap = CreateColorMap.CreateColorMap('Sub-Type')
    #cmap = CreateColorMap.CreateColorMap('Sub-Type QA')
    #cmap = CreateColorMap.CreateColorMap('Averaging Required for Detection')
    
    #red = np.array([255,   0,   0, 255, 250,   0, 192,   0])/255
    #grn = np.array([255,  38, 220, 160, 255, 255, 192,   0])/255 
    #blu = np.array([255, 255, 255,   0,   0, 110, 192,   0])/255 
    #cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())
    
    ## We should set the y-axis limits of the colorbar. Because we are
    ## plotting integer numbers, and we want them centered with the colors in
    ## the colorbar, the range has to be +-0.5 wider than the actual range
    plt.pcolormesh(xs[0], y, np.float64(vfm['Data']), edgecolors='none', shading='auto',
                   cmap=cmap,vmin=vfm['Vmin']-0.5, vmax=vfm['Vmax']+0.5)
    plt.ylim([-2., 30.])
    
    # Title
    plt.title(vfm['FieldDescription'], fontdict={'fontsize': 18})

    # axis labels
    fd = {'fontsize': 12, 'fontweight': 'bold', 'fontfamily': 'verdana'}
    plt.ylabel('Altitude (km)', fontdict=fd)

    # axis ticks (latitude)
    dx = (max(xs[0])-min(xs[0]))/8.
    ticks = np.arange(min(xs[0]), max(xs[0]) + dx, dx)
    ax0.xaxis.set_ticks(ticks)
    ax0.xaxis.set_major_formatter('{x:5.2f}')
    ax0.set_xlabel('Lat', fontdict=fd)
    ax0.xaxis.set_label_coords(-0.045, -0.03)

    plt.xticks(fontsize=12)#,fontweight='bold')
    plt.yticks(fontsize=12)#,fontweight='bold')
    #ax0.xaxis.set_minor_locator(mtk.AutoMinorLocator(4))
    ax0.yaxis.set_minor_locator(mtk.AutoMinorLocator(5))
    ax0.yaxis.set_ticks_position('both')
    ax0.tick_params(which='major',length=8)
    ax0.tick_params(which='minor',length=5)
    
    # axis ticks (longitude)
    # we need to create a new axis
    ax1 = ax0.twiny()
    ax1.set_position(pos=axpos - [0, 0.1, 0, 0])
    ax1.xaxis.set_ticks_position("bottom")
    ax1.xaxis.set_label_position("bottom")
    ax1.spines["bottom"].set_position(("axes", -0.062))
    ax1.set_frame_on(False)

    dx = (max(xs[1])-min(xs[1]))/8.
    ticks = np.arange(min(xs[1]), max(xs[1]) + dx, dx)
    ax1.xaxis.set_ticks(ticks)
    ax1.xaxis.set_major_formatter('{x:5.2f}')
    ax1.set_xlabel('Lon', fontdict=fd)
    ax1.xaxis.set_label_coords(-0.045, -0.068)
    ax1.set_xlim([xs[1][0], xs[1][-1]])
    ax1.tick_params(which='both',length=0)
    plt.xticks(fontsize=12)#,fontweight='bold')
    
    # colorbar 
    cb = plt.colorbar()
    cb.ax.tick_params(length=0)

    # fixes axes positions after ploting the colorbar
    ax0.set_position(pos=axpos)
    cb.ax.set_position(pos=[0.919, 0.121, 0.021, 0.788])

    # Create bottom caption for flag's values
    typelabel = '';
    for i, txt in enumerate(vfm['ByteTxt']):
        typelabel += '%d - %s    '%(vfm['Vmin']+i, txt)
    
    #th = annotation('textbox',[0.062 0.0 0.837 0.04],'string',typelabel);
    fig.text(0.5, 0.015, typelabel, fontsize=12, fontweight='bold', fontfamily='verdana',
             ha='center', va='center')
    #set(th,...
    #    'HorizontalAlignment','Center',...
    #    'VerticalAlignment','Middle');
    #
    # Display warning messages when image is larger than figure window (in pixels)
    # this is to let you know that you're trying to display more information than what
    # is there and that small/thin feature may be missing. If you use the zoom tool that
    # data will be visible.
    if  (imgSize[0] < vfm['Data'].shape[1]) & (imgSize[1] < vfm['Data'].shape[0]):
        print('Warning: Image is bigger than the current figure widow')
        print('         not all pixels may be visible')
    elif  (imgSize[0] < vfm['Data'].shape[1]):
        print('Warning: Image is wider than the current figure widow')
        print('         not all pixels may be visible')
    elif (imgSize[1] < vfm['Data'].shape[0]):
        print('Warning: Image is taller than the current figure widow')
        print('         not all pixels may be visible')

    return(0)
#[fig, ax, cb, th]
