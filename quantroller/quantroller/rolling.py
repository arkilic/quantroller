import pandas as pd
import numpy as np


def roll(dframe, window, min_periods, index=None, floor=None):
    """Get indexes for the rolling windows on the dataframe """
    start, end, _, _, _, _ = pd._window.get_window_indexer(dframe.values,
                                                           window,
                                                           min_periods,
                                                           index,
                                                           floor,
                                                           use_mock=False)
    return [np.arange(s, e) for s, e in zip(start, end)]


def get_rolled(dframe, ix):
    """Provide a list of dataframes that are chunks of the rolled dataframe"""
    res = []
    for i in range(dframe.shape[0]):
        res.append(dframe.iloc[ix[i], list(range(dframe.shape[1]))])
    return res