#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This package implements community detection.
Package name is community but refer to python-louvain on pypi
"""

from .louvain_local import (
    partition_at_level,
    modularity,
    get_clusters,
    best_partition,
    generate_dendrogram,
    induced_graph,
    load_binary,
)

__version__ = "0.1"
__author__ =  """Duc Nguyen (ducnt4@vng.com.vn)"""
#    Copyright (C) 2018 by
#    Duc Nguyen (ducnt4@vng.com.vn)
#    All rights reserved.
#    BSD license.
