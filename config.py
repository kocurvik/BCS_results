# -*- coding: utf-8 -*-

"""
For which systems the evaluation should be done.
It needs to be in the results dir defined in dataset_info.py
"""

RUN_FOR_SYSTEMS = ( "Transform3D_480_270_VP2VP3",
                    "Transform3D_640_360_VP2VP3",
                    "Transform3D_960_540_VP2VP3",
                    "Transform3D_270_480_VP1VP2",
                    "Transform3D_360_640_VP1VP2",
                    "Transform3D_540_960_VP1VP2",
                    "Transform2D_640_360_VP2VP3",
                    "Transform2D_360_640_VP1VP2",
                    "Orig2D_640_360",
                    "MaskRCNN3D_1024_576")
                    
"""
For which video the evaluation should be done. 
You can use keys A,B or C.
See dataset_info.py for more information and 
training videos for each splitting
"""
RUN_FOR_VIDEOS = SPLIT_TEST_VIDEOS["C"]


"""
Defines systems and thresholds
If a speed estmiation error for a system in the set is larger
then the threshold, the trajectory is shown
WARNING: You need to delete the cached results (or use -rc argument)
"""
SHOW_BAD_FOR_SYSTEMS = set()
SHOW_BAD_THRESHOLD = 30


"""
If true, vehicles' trajectories for which the computation
of intersections wihh measurement lines failes are shown
WARNING: You need to delete the cached results (or use -rc argument)
"""
SHOW_ERRORS = False



#%%
"""
##############################################################
################### PRESENTATION HELPER FUNCTIONS ############
##############################################################
"""

"""
Conversions for plotting and printing statistics
"""
def labelConversion(systemId):
    return systemId

"""
Styles for cumulative histograms
"""
def plotStyleCumulativeHist(systemId):
    styleDict = {"linewidth":2}
    return styleDict


"""
Styles for error histograms
"""
def plotStyleErrorHist(systemId):
    styleDict = {"linewidth":2}
    return styleDict
    
