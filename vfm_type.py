def vfm_type(vfm_row, feature):
    """
    VFM_TYPE   Unpacks a VFM row
        [vfm_class] = VFM_TYPE(vfm_row, feature) takes a vfm_row and extracts
        the bits of a feature flag. vfm_row is a VFM uint16 array (either packed
        or unpacked by vfm_expand()). feature is a string specifying the name of
        the feature classification flag, and can be one of the following:
        
           'type',
           'typeqa',
           'phase',
           'phaseqa',
           'aerosol',
           'cloud',
           'psc',
           'subtype',
           'subtypeqa', 
           'averaging'
        
        vfm_class is a structure that contains information about the vfm flag
        returned, and contains the following fields:
        
           'Data', the feature flag data (int16)
           'FieldDescription', the feature flag name 
           'Vmin' and 'Vmax', the limits of the feature flag
           'ByteTxt', descriptors of the feature flag
        
        History: 
           2021-may-24 Translated from Matlab to Python

           2021-apr-20 Returns data and metadata in the same object.
        
           2021-apr-09 Added max/min values for each feature, help string and
                       extra comments.  Removed unused features.
           
           2005-mar-28 Original code by Ralph Kuehn shared on CALIPO's
                       website, from 2005/03/28.
        
    """

    import numpy as np
    import sys
    
    umask3 = np.uint16(7)
    umask2 = np.uint16(3)
    umask1 = np.uint16(1)

    feature = feature.lower()
    
    if feature.lower() == 'type':
        # bits 1-3 Feature Type 
        # 0 = invalid (bad or missing data)
        # 1 = "clear air"
        # 2 = cloud
        # 3 = aerosol
        # 4 = stratospheric feature
        # 5 = surface
        # 6 = subsurface
        # 7 = no signal (totally attenuated)
        vfm_flag = np.bitwise_and(umask3,vfm_row)
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Feature Type',
                     'Vmin':0, 'Vmax':7,
                     'ByteTxt':['N/A','clear air','cloud','trop. aerosol','strat. aerosol',
                                'surface','subsurface','no signal']}
        
    elif feature.lower() == 'typeqa':
        # bits 4-5 Feature Type QA 
        # 0 = none
        # 1 = low
        # 2 = medium
        # 3 = high
        vfm_flag = np.bitwise_and(umask3,vfm_row)
        not_clear_air = ((vfm_flag == 0) | (vfm_flag == 2) | (vfm_flag == 3) | (vfm_flag ==4))
        a = np.right_shift(vfm_row,3)
        vfm_flag = np.bitwise_and(umask2,a)
        vfm_flag = vfm_flag + np.uint16(not_clear_air)
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Feature Type QA',
                     'Vmin':0, 'Vmax':3,
                     'ByteTxt':['Clear Air','No','Low','Medium','High']}
        
    elif feature.lower() == 'phase':
        # 6-7 Ice/Water Phase
        # -1 = region of the VFM not classified as cloud
        # 0 = unknown / not determined
        # 1 = randomly oriented ice
        # 2 = water
        # 3 = horizontally oriented ice        
        a = np.right_shift(vfm_row,5)
        vfm_flag = np.int16(np.bitwise_and(umask2,a))
        # mark regions where there are no clouds
        vfm_feature = np.bitwise_and(umask3,vfm_row)
        vfm_flag[vfm_feature != 2] = -1
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Ice/Water Phase',
                     'Vmin':-1, 'Vmax':3,
                     'ByteTxt':['N/A', 'unknown','ice','water','oriented ice']}
    
    elif feature.lower() == 'phaseqa':
        # 8-9 Ice/Water Phase QA 
        # 0 = none
        # 1 = low
        # 2 = medium
        # 3 = high
        a = np.right_shift(vfm_row,7)
        vfm_flag = np.bitwise_and(umask2,a)
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Ice/Water Phase QA',
                     'Vmin':0, 'Vmax':3,
                     'ByteTxt':['None','Low','Medium','High']}
    
    elif feature.lower() == 'aerosol':
        # 10-12 Feature Sub-type
        # If feature type = aerosol, bits 10-12 will specify the aerosol type
        # 0 = not determined
        # 1 = clean marine
        # 2 = dust
        # 3 = polluted continental
        # 4 = clean continental
        # 5 = polluted dust
        # 6 = smoke
        # 7 = other
        a = np.right_shift(vfm_row,9)
        vfm_flag = np.int16(np.bitwise_and(umask3,a))
        print(np.unique(vfm_flag))
        # mark regions where there are no aerosols
        vfm_feature = np.bitwise_and(umask3,vfm_row)
        vfm_flag[vfm_feature != 3] = -1
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Aerosol Sub-Type',
                     'Vmin':-1, 'Vmax':7,
                     'ByteTxt':['N/A','unknown','clean marine','dust','poll. cont.','clean cont.',
                                'poll. dust','smoke','dusty marine']}
    
    elif feature.lower() == 'cloud':
        # 10-12 Feature Sub-type
        # If feature type = cloud, bits 10-12 will specify the cloud type.
        # 0 = low overcast, transparent
        # 1 = low overcast, opaque
        # 2 = transition stratocumulus
        # 3 = low, broken cumulus
        # 4 = altocumulus (transparent)
        # 5 = altostratus (opaque)
        # 6 = cirrus (transparent)
        # 7 = deep convective (opaque)
        a = np.right_shift(vfm_row,9)
        vfm_flag = np.int16(np.bitwise_and(umask3,a))
        # mark regions where there are no aerosols
        vfm_feature = np.bitwise_and(umask3,vfm_row)
        vfm_flag[vfm_feature != 2] = -1
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Cloud Sub-Type',
                     'Vmin':-1, 'Vmax':7,
                     'ByteTxt':['N/A','Low, over, thin','Low, over, thick','Trans. Sc','Low Broken',
                                'Ac','As','Ci','Cb']}
    
    elif feature.lower() == 'psc':
        # 10-12 Feature Sub-type
        # If feature type = Polar Stratospheric Cloud, bits 10-12 will specify PSC classification.
        # 0 = not determined
        # 1 = non-depolarizing PSC
        # 2 = depolarizing PSC
        # 3 = non-depolarizing aerosol
        # 4 = depolarizing aerosol
        # 5 = spare
        # 6 = spare
        # 7 = other
        a = np.right_shift(vfm_row,9)
        vfm_flag = np.int16(np.bitwise_and(umask3,a))
        # mark regions where there are no aerosols
        vfm_feature = np.bitwise_and(umask3,vfm_row)
        vfm_flag[vfm_feature != 4] = -1
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'PSC Sub-Type',
                     'Vmin':-1, 'Vmax':4,
                     'ByteTxt':['N/A','invalid','PSC aerosol','volcanic ash',
                                'sulfate/other','elevated smoke']}
        #             'ByteTxt':['Not Determined','Non-Depol. PSC','Depol. PSC',
        #                        'Non-Depol Aerosol','Depol. Aerosol','spare','spare','Other']}
        
    elif feature.lower() == 'subtype':
        # Returns just subtype number
        a = np.right_shift(vfm_row,9)
        vfm_flag = np.int16(np.bitwise_and(umask3,a))
        # mark regions where there are no aerosols
        vfm_feature = np.bitwise_and(umask3,vfm_row)
        vfm_flag[(vfm_feature < 2) | (vfm_feature > 4) ] = -1
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Sub-Type',
                     'Vmin':-1, 'Vmax':7,
                     'ByteTxt':['N/A', 'Zero','One','Two','Three','Four','Five',
                                'Six','Seven']}
        
    elif feature.lower() == 'subtypeqa':
        # 13 Cloud / Aerosol /PSC Type QA 
        # 0 = not confident
        # 1 = confident
        a = np.right_shift(vfm_row,12)
        vfm_flag = np.int16(np.bitwise_and(umask1,a))
        # mark regions where there are no aerosols
        vfm_feature = np.bitwise_and(umask3,vfm_row)
        vfm_flag[(vfm_feature < 2) | (vfm_feature > 4) ] = -1
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Sub-Type QA',
                     'Vmin':-1, 'Vmax':1,
                     'ByteTxt':['N/A','Not Confident','Confident']}
        
    elif feature.lower() == 'averaging':
        # 14-16 Horizontal averaging required for detection
        # (provides a coarse measure of feature backscatter intensity)
        # 0 = not applicable
        # 1 = 1/3 km
        # 2 = 1 km
        # 3 = 5 km
        # 4 = 20 km
        # 5 = 80 km
        a = np.right_shift(vfm_row,13)
        vfm_flag = np.bitwise_and(umask3,a)
        vfm_class = {'Data':vfm_flag,
                     'FieldDescription':'Averaging Required for Detection',
                     'Vmin':0, 'Vmax':5,
                     'ByteTxt':['N/A','1/3 km','1 km','5 km','20 km','80 km']}
        
    else:
        sys.exit('Unknown type specifier. Check input')
        vfm_flag = np.nan
        vfm_class = {'Data':np.nan,
                     'FieldDescription':'empty',
                     'Vmin':np.nan, 'Vmax':np.nan,
                     'ByteTxt':['empty']}
    
    return (vfm_class)
