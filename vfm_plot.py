def vfm_plot(vfm, xs, y, imgSize = [1300, 667], dpi=96):

    import matplotlib as mpl
    import matplotlib.ticker as mtk
    import matplotlib.pyplot as plt
    import numpy as np
    import sys

    # Determine or set image size
    if len(imgSize) != 2:
        sys.error('imgSize is not of a usable size. Must be of length 2, it is ' + np.shape(imgSize));

    axpos = [0.062, 0.121, 0.837, 0.788];

    # Create Figure & set size
    plt.figure(num=1, figsize=np.float64(imgSize)/dpi, dpi=dpi, clear=True);
    plt.gca().set_position(pos=axpos)

    ##[r,g,b]=CreateColorMap(vfm.FieldDescription);
    
    red = np.array([255,   0,   0, 255, 250,   0, 192,   0])/255
    grn = np.array([255,  38, 220, 160, 255, 255, 192,   0])/255 
    blu = np.array([255, 255, 255,   0,   0, 110, 192,   0])/255 
    cmap = mpl.colors.ListedColormap(np.array([red, grn, blu]).transpose())

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
    plt.xlabel('Lat', fontdict=fd)
    plt.gca().xaxis.set_label_coords(-0.045, -0.03)

    # axis ticks
    dx = (max(xs[0])-min(xs[0]))/8.
    ticks = np.arange(min(xs[0]), max(xs[0]) + dx, dx)
    plt.gca().xaxis.set_ticks(ticks)
    plt.gca().xaxis.set_major_formatter('{x:5.2f}')

    #dx = (max(xs[1])-min(xs[1]))/8.
    #ticks = np.arange(min(xs[1]), max(xs[1]) + dx, dx)

    plt.xticks(fontsize=12,fontweight='bold')
    plt.yticks(fontsize=12,fontweight='bold')
    #plt.gca().xaxis.set_minor_locator(mtk.AutoMinorLocator(4))
    plt.gca().yaxis.set_minor_locator(mtk.AutoMinorLocator(5))
    plt.gca().yaxis.set_ticks_position('both')
    plt.gca().tick_params(which='major',length=8)
    plt.gca().tick_params(which='minor',length=5)
    
    # colorbar 
    cb = plt.colorbar()
    cb.ax.tick_params(length=0)

    # fixes axes positions after ploting the colorbar
    plt.gca().set_position(pos=axpos)
    cb.ax.set_position(pos=[0.919, 0.121, 0.021, 0.788])

    # Create bottom caption for flag's values
    typelabel = '';
    for i, txt in enumerate(vfm['ByteTxt']):
        typelabel += '%d - %s    '%(vfm['Vmin']+i, txt)
    
    #th = annotation('textbox',[0.062 0.0 0.837 0.04],'string',typelabel);
    plt.gcf().text(0.06, 0.01, typelabel, fontsize=12, fontweight='bold', fontfamily='verdana')
    #set(th,...
    #    'HorizontalAlignment','Center',...
    #    'VerticalAlignment','Middle');
    #
    ## Display warning messages when image is larger than figure window (in pixels)
    ## this is to let you know that you're trying to display more information than what
    ## is there and that small/thin feature may be missing. If you use the zoom tool that
    ## data will be visible.
    #Isize = get(fig,'Position');
    #if  (Isize(3) < size(vfm.Data,2)) && (Isize(4) < size(vfm.Data,1)):
    #    disp('Warning: Image is bigger than the current figure widow'); 
    #    disp('         not all pixels may be visible'); 
    #elif  (Isize(3) < size(vfm.Data,2)):
    #    disp('Warning: Image is wider than the current figure widow'); 
    #    disp('         not all pixels may be visible'); 
    #elif Isize(4) < size(vfm.Data,1):
    #    disp('Warning: Image is taller than the current figure widow'); 
    #    disp('         not all pixels may be visible'); 

    return(0)
#[fig, ax, cb, th]
