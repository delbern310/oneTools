import base64
import json
import math
import os
import re
import sys
import time
from enum import Enum


class Dock(Enum):
    left = 0
    right = 1
    up = 2
    down = 3


class SplitterState(Enum):
    collapsed = 0
    expanded = 1


class SpatialReference:
    sz_Local = 2435
    gcs_2000 = 4490
    pcs_2000 = 4547
    pcs_2000_zone = 4526
    wgs84 = 4326
    bd09 = -2
    gcj02 = -1
    gcs_xian80 = 4610
    pcs_xian80 = 2383
    pcs_xian80_zone = 2362

    @staticmethod
    def lst():
        return [2435, 4490, 4547, 4526, 4326, -1, -2, 4610, 2383, 2362]


class DataType(Enum):
    shapefile = 0
    geojson = 1
    cad_dwg = 2
    fileGDB = 3
    csv = 4


DataType_dict = {
    DataType.shapefile: "ESRI Shapefile",
    DataType.geojson: "geojson",
    DataType.fileGDB: "FileGDB",
    DataType.cad_dwg: "CAD"
}

def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton

srs_dict = {
    SpatialReference.sz_Local: "深圳独立",
    SpatialReference.gcs_2000: "CGCS2000地理",
    SpatialReference.pcs_2000: "CGCS2000投影",
    SpatialReference.pcs_2000_zone: "CGCS2000投影(包含带号)",
    SpatialReference.wgs84: "WGS84",
    SpatialReference.bd09: "百度地理",
    SpatialReference.gcj02: "火星",
    SpatialReference.gcs_xian80: "西安80地理",
    SpatialReference.pcs_xian80: "西安80投影",
    SpatialReference.pcs_xian80_zone: "西安80投影(包含带号)"
}

# epsg_dict = {
#     SpatialReference.sz_Local: 2435,
#     SpatialReference.gcs_2000: 4490,
#     SpatialReference.pcs_2000: 4547,
#     SpatialReference.pcs_2000_zone: 4526,
#     SpatialReference.wgs84: 4326,
#     SpatialReference.gcs_xian80: 4610,
#     SpatialReference.pcs_xian80: 2383,
#     SpatialReference.pcs_xian80_zone: 2363
# }

srs_list = ["深圳独立", "CGCS2000投影", "WGS84", "百度地理", "火星", "CGCS2000地理",
            "CGCS2000投影(包含带号)", "西安80地理", "西安80投影", "西安80投影(包含带号)"]



