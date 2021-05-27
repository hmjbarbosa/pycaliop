def map_plot(lat, lon, world=1, pad=20, map=[1,1,1,0,0,1], imgSize=[600,400], dpi=96):
    """MAP_PLOT Creates a map showing the calipso track [fig, ax, gl] =
        MAP_PLOT(lat, lon) takes calipson track coordinates and plot
        on the world map. lat and lon are single column arrays of the
        same length. The function returns handlers to the figure, axis
        and gridlines.

        MAP_PLOT(..., world=1, pad=20) uses optional keywords to
        specify the region of the map to be shown. world=1 (default)
        means the whole world (90S-90N 180W-180E). If 0 < world < 1,
        only a fraction of the world will be shown and centered on the
        calipso track. If world=0, the map bondary will be given by
        the limits of lat,lon with a padding around it.

        MAP_PLOT(..., map=[1,1,1,0,0,1]) controls whether coastlines,
        country borders, states limits, rivers, lakes and ocean are
        drawn (=1) or not drawn (=0).

        MAP_PLOT(..., imgSize=[600,400], dpi=96) change the default
        image size and resolution.

        History: 
           2021-may-27 First working version

    """
    import matplotlib.pyplot as plt
    import numpy as np
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature

    fig = plt.figure(figsize=np.float64(imgSize)/dpi, dpi=dpi, clear=True)
    ax = plt.axes(projection=ccrs.PlateCarree())

    if world == 1:
        minlat, maxlat, minlon, maxlon = -90, 90, -180, 180
        pad = 0

    if (world > 0.) & (world < 1.):
        lat0, lon0 = np.mean(lat), np.mean(lon)
        minlat, maxlat = max(lat0-90*world,-90), min(lat0+90*world,90)
        minlon, maxlon = lon0-180*world, lon0+180*world
        pad = 0
        
    else: 
        minlat, maxlat, minlon, maxlon = min(lat), max(lat), min(lon), max(lon)

    ax.set_extent([minlon - pad, maxlon + pad, minlat - pad, maxlat + pad])

    # plot calipso track
    plt.plot(lon, lat, '-b')

    # add map
    if map[0]:
        ax.add_feature(cfeature.COASTLINE, linewidth=1.5, linestyle='-', edgecolor='black', alpha=.8)
    if map[1]:
        ax.add_feature(cfeature.BORDERS, linewidth=1.5, linestyle='-', edgecolor='black', alpha=.8)
    if map[2]:
        ax.add_feature(cfeature.STATES, linewidth=1.5, linestyle='-', edgecolor='gray', alpha=.5)
    if map[3]:
        ax.add_feature(cfeature.RIVERS, linewidth=1, linestyle='-', edgecolor='blue', alpha=.5)
    if map[4]:
        ax.add_feature(cfeature.LAKES, linewidth=1, linestyle='-', edgecolor='green', alpha=.5)
    if map[5]:
        ax.add_feature(cfeature.OCEAN, facecolor='lightblue', zorder=0)
    
    #plt.scatter(-67.8076, -9.974, s=30, c='m', marker='o')
    gl = ax.gridlines(draw_labels=True,linewidth=1, color='gray', alpha=0.5, linestyle=':')
    #gl.top_labels = False
    #gl.right_labels = False
    #gl.xlocator = mticker.FixedLocator([-80, -75, -70, -65, -60, -55, -50, -45, -40])
    #gl.ylocator = mticker.FixedLocator([-20, -15, -10, -5, 0])

    return([fig, ax, gl])
