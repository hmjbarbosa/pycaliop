def vfm_expand(vfm_rows):
    """
    VFM_EXPAND   Unpacks a VFM
       [vfm_block] = VFM_ROWS2BLOCK(vfm_rows) unpacks all vfm_rows creating a
       vfm_block. A vfm_rows array has a size of ntimes x 5515, and the resulting
       vfm_block will have a size of nzlev (545) x total_times (ntimes x 15). 
    
       Low altitude data (< 8km) is returned as in the input data: 15 profiles
       with 30m vertical by 333m horizontal, corresponding to 290x15 = 4350
       values.  Higher altitude data is over-sampled in horizontal
       dimension.
    
       For 8-20km, returned data has 200x15 = 3000 rather than 200x5 = 1000.
       For 20-30km, returned data has 55x15 = 825, rather than 55x3 = 165.
    
       Type of vfm_block is the same as vfm_rows, hence this function could be
       colled on the bit-compressed or the bit-uncompressed VFM data.
    
       This function is 5-10 times faster than the original vfm_row2block.m
       shared on the Calipso website (written by Ralph Kuehn in 2005). 
      
       History 
          2021-mar-09 Optimized version 
    
          2021-mar-07 First version, looking at Calipso Data user's guide
          and Kuehn's function. 
    
    
    """

    import sys
    import numpy as np
    
    # Check dimensions, it should be: ntimes x 5515
    if vfm_rows.ndim != 2:
        sys.exit('Input data should have 2 dimensions.')

    [ntimes, rowlen] = vfm_rows.shape

    if rowlen != 5515:
        if ntimes == 5515:
            # Try to transpose
            print('Consider transposing input data.')
            vfm_rows = vfm_rows.transpose()
            [ntimes, rowlen] = vfm_rows.shape
        else:
            # Something wrong
            sys.exit('Could not find a dimension with length 5515.')

    # Allocate memory for speed
    vfm_block = np.zeros([ntimes, 15, 290+200+55], dtype=vfm_rows.dtype)

    # Create the blocks
    for i in range(ntimes):
        line = vfm_rows[i,:]
        bk1 = np.reshape(line[    :165 ],[ 3, 55])
        bk2 = np.reshape(line[ 165:1165],[ 5,200])
        bk3 = np.reshape(line[1165:    ],[15,290])
  
        # the 15 compressed profiles vary (in time) faster than ntimes
        for j in range(15):
            vfm_block[i, j,    :55 ] = bk1[np.int(np.floor(j/5)), :]
            vfm_block[i, j,  55:255] = bk2[np.int(np.floor(j/3)), :]
            vfm_block[i, j, 255:   ] = bk3[j, :]

    # Last 2 dimensions are "times", so let's make just one
    vfm_block = np.reshape(vfm_block, [15*ntimes, 545])

    return(vfm_block.transpose())
#
