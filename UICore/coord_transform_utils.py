import time

import click
import os

from osgeo import ogr, osr, gdal

from UICore.DataFactory import workspaceFactory
from UICore.Gv import DataType, DataType_dict, srs_dict
from UICore.common import launderName, overwrite_cpg_file, helmert_para, is_already_opened_in_write_mode
from UICore.log4p import Log
from UICore.Gv import SpatialReference

log = Log(__file__)

@click.command()
@click.option(
    '--inpath', '-i',
    help='Input path, also means the workspace of spatial data. For example, d:/res/data/ or d:/res/data.gdb',
    type=str,
    required=True)
@click.option(
    '--inlayer',
    help='input layer name.',
    type=str,
    required=True)
@click.option(
    '--insrs',
    help='Input srs. sz_Local = 2435, gcs_2000 = 4490, pcs_2000 = 4547, pcs_2000_zone = 4526, wgs84 = 4326, bd09 = -1, '
         'gcj02 = -2, gcs_xian80 = 4610, pcs_xian80 = 2383, pcs_xian80_zone = 2363. The in layer\'s srs will be used to the default',
    type=int,
    default='-99',
    required=False)
@click.option(
    '--outpath', '-o',
    help='Input path, also means the workspace of spatial data. For example, d:/res/data/ or d:/res/data.gdb',
    type=str,
    default=-1,
    required=False)
@click.option(
    '--outlayer',
    help='Output layer name, which is shown in the result workspace.',
    type=str,
    required=True)
@click.option(
    '--outsrs',
    help='Output srs. sz_Local = 0, gcs_2000 = 1, pcs_2000 = 2, pcs_2000_zone = 3, wgs84 = 4, bd09 = 5, '
         'gcj02 = 6, gcs_xian80 = 7, pcs_xian80 = 8, pcs_xian80_zone = 9.',
    type=int,
    required=True)
def main(inpath, inlayer, insrs, outpath, outlayer, outsrs):
    """spatial coordinate transformation program"""

    if inpath[-1] == os.sep:
        inpath = inpath[:-1]
    if outpath[-1] == os.sep:
        outpath = outpath[:-1]

    in_format = get_suffix(inpath)
    in_wks = workspaceFactory().get_factory(in_format)

    if in_wks is None:
        return False

    in_wks.openFromFile(inpath)
    in_layer = in_wks.openLayer(inlayer)

    checked_insrs = check_srs(insrs, in_layer)
    if checked_insrs == -2435:
        log.error("输入的空间参考在ESPG中不存在!")
        return False
    elif checked_insrs == -4547:
        log.error("不支持输入空间数据的坐标转换!")
        return False

    checked_outsrs = check_srs(outsrs, outlayer)
    if checked_outsrs == -2435:
        log.error("输出的空间参考在ESPG中不存在!")
        return False
    elif checked_outsrs == -4547:
        log.error("不支持输出空间数据的坐标转换!")
        return False

        # out_srs = osr.SpatialReference()
    # out_srs.ImportFromEPSG(outsrs)

    out_format = get_suffix(outpath)

    tfer = Transformer(out_format, inpath, outpath, outlayer)
    tfer.transform(checked_insrs, checked_outsrs)

    print("ok")


def check_srs(srs, in_layer):
    if srs not in SpatialReference.lst():
        return -4547

    if srs > 0 or srs == -99:
        srs_epsg = get_srs(in_layer)
        in_srs = osr.SpatialReference()
        if srs_epsg is None:
            try:
                in_srs.ImportFromEPSG(srs)
                return srs
            except:
                return -2435
        else:
            return srs_epsg
    elif srs == -1 or srs == -2:
        pass
    else:
        return -4547

def get_srs(layer):
    try:
        srs = layer.GetSpatialRef()
        if srs is not None:
            srs_wkt = osr.SpatialReference(srs.ExportToWkt())
            srs_epsg = srs_wkt.GetAttrValue("AUTHORITY", 1)
            return int(srs_epsg)
        else:
            return None
    except:
        return None


def get_suffix(path):
    suffix = None
    basename = os.path.basename(path)
    if basename.find('.') > 0:
        suffix = basename.split('.')[1]

    if suffix.lower() == 'shp':
        return DataType.shapefile
    elif suffix.lower() == 'geojson':
        return DataType.geojson
    elif suffix.lower() == 'gdb':
        return DataType.fileGDB
    elif suffix.lower() == 'dwg':
        return DataType.cad_dwg
    else:
        return None


class Transformer(object):
    def __init__(self, out_format, inpath, outpath, outlayername):
        self.out_format = out_format
        self.lco = []

        if out_format == DataType.shapefile:
            self.lco = ["ENCODING=GBK"]
            self.out = outpath
        elif out_format == DataType.fileGDB:
            self.lco = ["FID=FID"]
            self.out = os.path.join(outpath, outlayername)

        self.inpath = inpath
        self.outpath = outpath
        self.outlayername = outlayername

    def transform(self, srcSRS, dstSRS):
        start = time.time()

        if srcSRS == SpatialReference.sz_Local and dstSRS == SpatialReference.pcs_2000:
            self.sz_local_to_pcs_2000(self.inpath, self.outpath, self.outlayername, self.out_format)
        elif srcSRS == SpatialReference.pcs_2000 and dstSRS == SpatialReference.sz_Local:
            self.pcs_2000_to_sz_local(self.inpath, self.outpath, self.outlayername, self.out_format)
        elif srcSRS == SpatialReference.sz_Local and dstSRS == SpatialReference.gcs_2000:
            self.sz_local_to_gcs_2000(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.gcs_2000 and dstSRS == SpatialReference.sz_Local:
            self.gcs_2000_to_sz_local(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.sz_Local and dstSRS == SpatialReference.wgs84:
            self.sz_local_to_wgs84(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.wgs84 and dstSRS == SpatialReference.sz_Local:
            self.wgs84_to_sz_local(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.sz_Local and dstSRS == SpatialReference.pcs_2000_zone:
            self.sz_local_to_pcs_2000_zone(self.inpath, self.outpath, self.outlayername, self.out_format)
        elif srcSRS == SpatialReference.pcs_2000_zone and dstSRS == SpatialReference.sz_Local:
            self.pcs_2000_zone_to_sz_local()
        elif srcSRS == SpatialReference.wgs84 and dstSRS == SpatialReference.pcs_2000:
            self.wgs84_to_pcs_2000()
        elif srcSRS == SpatialReference.pcs_2000 and dstSRS == SpatialReference.wgs84:
            self.pcs_2000_to_wgs84()
        elif srcSRS == SpatialReference.wgs84 and dstSRS == SpatialReference.pcs_2000_zone:
            self.wgs84_to_pcs_2000_zone()
        elif srcSRS == SpatialReference.pcs_xian80 and dstSRS == SpatialReference.sz_Local:
            self.pcs_xian80_to_sz_local(self.inpath, self.outpath, self.outlayername, self.out_format)
        elif srcSRS == SpatialReference.pcs_xian80 and dstSRS == SpatialReference.pcs_2000:
            self.pcs_xian80_to_pcs_2000(self.inpath, self.outpath, self.outlayername, self.out_format)
        elif srcSRS == SpatialReference.pcs_xian80 and dstSRS == SpatialReference.gcs_2000:
            self.pcs_xian80_to_gcs_2000(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.pcs_xian80 and dstSRS == SpatialReference.pcs_2000_zone:
            self.pcs_xian80_to_pcs_2000_zone()
        elif srcSRS == SpatialReference.gcs_xian80 and dstSRS == SpatialReference.sz_Local:
            self.gcs_xian80_to_sz_local()
        elif srcSRS == SpatialReference.gcs_xian80 and dstSRS == SpatialReference.pcs_2000:
            self.gcs_xian80_to_pcs_2000(self.inpath, self.outpath, self.outlayername, self.out_format)
        elif srcSRS == SpatialReference.gcs_xian80 and dstSRS == SpatialReference.gcs_2000:
            self.gcs_xian80_to_gcs_2000()
        elif srcSRS == SpatialReference.pcs_xian80_zone and dstSRS == SpatialReference.sz_Local:
            self.pcs_xian80_zone_to_sz_local()
        elif srcSRS == SpatialReference.pcs_xian80_zone and dstSRS == SpatialReference.pcs_2000:
            self.pcs_xian80_zone_to_pcs_2000()
        elif srcSRS == SpatialReference.pcs_xian80 and dstSRS == SpatialReference.wgs84:
            self.pcs_xian80_to_wgs84(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.pcs_xian80_zone and dstSRS == SpatialReference.gcs_2000:
            self.pcs_xian80_zone_to_gcs_2000(srcSRS, dstSRS)
        elif srcSRS == SpatialReference.pcs_xian80_zone and dstSRS == SpatialReference.wgs84:
            self.pcs_xian80_zone_to_wgs84(srcSRS, dstSRS)
        else:
            log.error("不支持从{}到{}的转换!".format(srs_dict[srcSRS], srs_dict[dstSRS]))
            return False

        if self.out_format == DataType.shapefile:
            out_path = os.path.dirname(self.outpath)
            out_file, suffix = os.path.splitext(os.path.basename(self.outpath))

            overwrite_cpg_file(out_path, out_file, 'GB2312')

        end = time.time()

        log.info("坐标转换完成! 共耗时{}秒. 数据存储至{}.".format("{:.2f}".format(end-start), self.out))

    def sz_local_to_pcs_2000(self, inpath, outpath, outlayer, outformat):
        para_sz_to_pcs_2000 = helmert_para(SpatialReference.sz_Local, SpatialReference.pcs_2000)

        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2435)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4547)

        out_format = DataType_dict[outformat]

        if outformat == DataType.geojson:
            translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                           coordinateOperation=para_sz_to_pcs_2000,
                                                           layerName=outlayer)
        else:
            translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                           coordinateOperation=para_sz_to_pcs_2000,
                                                           accessMode="overwrite", layerName=outlayer,
                                                           layerCreationOptions=self.lco)

        gdal.VectorTranslate(outpath, inpath, options=translateOptions)

    def pcs_2000_to_sz_local(self, inpath, outpath, outlayer, outformat):
        # order0 = get_axis_order(in_srs)

        para_pcs_2000_to_sz = helmert_para(SpatialReference.pcs_2000, SpatialReference.sz_Local)

        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4547)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(2435)

        out_format = DataType_dict[outformat]

        if outformat == DataType.geojson:
            translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                           coordinateOperation=para_pcs_2000_to_sz,
                                                           layerName=outlayer)
        else:
            translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                           coordinateOperation=para_pcs_2000_to_sz,
                                                           accessMode="overwrite", layerName=self.outlayername,
                                                           layerCreationOptions=self.lco)

        gdal.VectorTranslate(outpath, inpath, options=translateOptions)

    def sz_local_to_gcs_2000(self, srcSRS, dstSRS):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(srcSRS)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(dstSRS)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(4547)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_4547.geojson")
        tmp_outpath = launderLayerName(tmp_outpath)
        self.sz_local_to_pcs_2000(self.inpath, tmp_outpath, "temp_layer_4547", DataType.geojson)

        out_format = DataType_dict[self.out_format]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=temp_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, tmp_outpath, options=translateOptions)

    def gcs_2000_to_sz_local(self, srcSRS, dstSRS):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(srcSRS)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(dstSRS)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(4547)

        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs,
                                                       layerName="temp_layer_4547")
        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_4547.geojson")
        tmp_outpath = launderLayerName(tmp_outpath)
        gdal.VectorTranslate(tmp_outpath, self.inpath, options=translateOptions)

        self.pcs_2000_to_sz_local(tmp_outpath, self.outpath, self.out_format, self.outlayername)

    def sz_local_to_wgs84(self, srcSRS, dstSRS):
        self.sz_local_to_gcs_2000(srcSRS, dstSRS)

    def wgs84_to_sz_local(self, srcSRS, dstSRS):
        self.gcs_2000_to_sz_local(srcSRS, dstSRS)

    def sz_local_to_pcs_2000_zone(self, inpath, outpath, outlayer, outformat):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2435)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4526)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(4547)

        tmp_outpath = os.path.join(os.path.dirname(outpath), "temp_layer_4547.geojson")
        tmp_outpath = launderLayerName(tmp_outpath)
        self.sz_local_to_pcs_2000(inpath, tmp_outpath, "temp_layer_4547", DataType.geojson)

        out_format = DataType_dict[outformat]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=temp_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=outlayer,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(outpath, tmp_outpath, options=translateOptions)

    def pcs_2000_zone_to_sz_local(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4526)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(2435)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(4547)

        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs,
                                                       layerName="temp_layer_4547")
        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_4547.geojson")
        tmp_outpath = launderLayerName(tmp_outpath)
        gdal.VectorTranslate(tmp_outpath, self.inpath, options=translateOptions)

        self.pcs_2000_to_sz_local(tmp_outpath, self.outpath, self.out_format, self.outlayername)

    def wgs84_to_pcs_2000(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4490)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4547)

        out_format = DataType_dict[self.out_format]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, self.inpath, options=translateOptions)

    def pcs_2000_to_wgs84(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4547)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4326)

        out_format = DataType_dict[self.out_format]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, self.inpath, options=translateOptions)

    def wgs84_to_pcs_2000_zone(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4490)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4526)

        translateOptions = gdal.VectorTranslateOptions(format=self.out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, self.inpath, options=translateOptions)

    def pcs_2000_zone_to_wgs84(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4526)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4326)

        translateOptions = gdal.VectorTranslateOptions(format=self.out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, self.inpath, options=translateOptions)

    def pcs_xian80_to_sz_local(self, inpath, outpath, outlayer, outformat):
        para_pcs_xian80_to_sz = helmert_para(SpatialReference.pcs_xian80, SpatialReference.sz_Local)

        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2383)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(2435)

        out_format = DataType_dict[outformat]

        if outformat == DataType.geojson:
            translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                           coordinateOperation=para_pcs_xian80_to_sz,
                                                           layerName=outlayer)
        else:
            translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=in_srs, dstSRS=out_srs,
                                                           coordinateOperation=para_pcs_xian80_to_sz,
                                                           accessMode="overwrite", layerName=self.outlayername,
                                                           layerCreationOptions=self.lco)

        gdal.VectorTranslate(outpath, inpath, options=translateOptions)

    def pcs_xian80_to_pcs_2000(self, inpath, outpath, outlayer, outformat):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2383)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4547)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(2435)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_2435.geojson")
        # tmp_outpath = launderLayerName(tmp_outpath)
        self.pcs_xian80_to_sz_local(inpath, tmp_outpath, "temp_layer_2435", DataType.geojson)
        self.sz_local_to_pcs_2000(tmp_outpath, outpath, outlayer, outformat)

    def pcs_xian80_to_gcs_2000(self, srcSRS, dstSRS):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(srcSRS)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(dstSRS)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(4547)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_4547.geojson")
        self.pcs_xian80_to_pcs_2000(self.inpath, tmp_outpath, "temp_layer_4547", DataType.geojson)

        out_format = DataType_dict[self.out_format]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=temp_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, tmp_outpath, options=translateOptions)

    def pcs_xian80_to_pcs_2000_zone(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2383)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4526)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(2435)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_2435.geojson")
        self.pcs_xian80_to_sz_local(self.inpath, tmp_outpath, "temp_layer_2435", DataType.geojson)
        self.sz_local_to_pcs_2000(tmp_outpath, self.outpath, self.outlayername, self.out_format)

    def gcs_xian80_to_sz_local(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4610)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(2435)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(2383)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_2383.geojson")
        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs,
                                                       layerName="temp_layer_2383")
        gdal.VectorTranslate(tmp_outpath, self.inpath, options=translateOptions)

        self.pcs_xian80_to_sz_local(tmp_outpath, self.outpath, self.outlayername, self.out_format)

    def gcs_xian80_to_pcs_2000(self, inpath, outpath, outlayer, outformat):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4610)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4547)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(2383)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_2383.geojson")
        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs,
                                                       layerName="temp_layer_2383")
        gdal.VectorTranslate(tmp_outpath, inpath, options=translateOptions)

        self.pcs_xian80_to_pcs_2000(tmp_outpath, outpath, outlayer, outformat)

    def gcs_xian80_to_gcs_2000(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(4610)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4490)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(4547)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_4547.geojson")
        self.gcs_xian80_to_pcs_2000(self.inpath, tmp_outpath, self.outlayername, DataType.geojson)

        out_format = DataType_dict[self.out_format]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=temp_srs, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(self.outpath, tmp_outpath, options=translateOptions)

    def pcs_xian80_zone_to_sz_local(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2362)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(2435)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(2383)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_2383.geojson")
        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs,
                                                       layerName="temp_layer_2383")
        gdal.VectorTranslate(tmp_outpath, self.inpath, options=translateOptions)

        self.pcs_xian80_to_sz_local(tmp_outpath, self.outpath, self.outlayername, self.out_format)

    def pcs_xian80_zone_to_pcs_2000(self):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(2362)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(4547)
        temp_srs = osr.SpatialReference()
        temp_srs.ImportFromEPSG(2383)

        tmp_outpath = os.path.join(os.path.dirname(self.outpath), "temp_layer_2383.geojson")
        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs,
                                                       layerName="temp_layer_2383")
        gdal.VectorTranslate(tmp_outpath, self.inpath, options=translateOptions)

        self.pcs_xian80_to_pcs_2000(tmp_outpath, self.outpath, self.outlayername, self.out_format)

    def pcs_xian80_to_wgs84(self, srcSRS, dstSRS):
        self.pcs_xian80_to_gcs_2000(srcSRS, dstSRS)

    def pcs_xian80_zone_to_gcs_2000(self, srcSRS, dstSRS):
        in_srs = osr.SpatialReference()
        in_srs.ImportFromEPSG(srcSRS)
        out_srs = osr.SpatialReference()
        out_srs.ImportFromEPSG(dstSRS)
        temp_srs1 = osr.SpatialReference()
        temp_srs1.ImportFromEPSG(2383)

        tmp_outpath1 = os.path.join(os.path.dirname(self.outpath), "temp_layer_2383.geojson")
        translateOptions = gdal.VectorTranslateOptions(format="geojson", srcSRS=in_srs, dstSRS=temp_srs1,
                                                       layerName="temp_layer_2383")
        gdal.VectorTranslate(tmp_outpath1, self.inpath, options=translateOptions)

        tmp_outpath2 = os.path.join(os.path.dirname(self.outpath), "temp_layer_2383.geojson")
        self.pcs_xian80_to_pcs_2000(tmp_outpath2, tmp_outpath1, self.outlayername, self.out_format)

        temp_srs2 = osr.SpatialReference()
        temp_srs2.ImportFromEPSG(4547)
        out_format = DataType_dict[self.out_format]
        translateOptions = gdal.VectorTranslateOptions(format=out_format, srcSRS=temp_srs2, dstSRS=out_srs,
                                                       accessMode="overwrite", layerName=self.outlayername,
                                                       layerCreationOptions=self.lco)
        gdal.VectorTranslate(tmp_outpath1, self.inpath, options=translateOptions)

    def pcs_xian80_zone_to_wgs84(self, srcSRS, dstSRS):
        self.pcs_xian80_to_gcs_2000(srcSRS, dstSRS)


def launderLayerName(path):
    if is_already_opened_in_write_mode(path):
        return launderName(path)
    else:
        return path


# 获取axis order，先北后东还是先东后北
def get_axis_order(srs):
    srs_wkt = osr.SpatialReference(srs.ExportToWkt())
    order0 = srs_wkt.GetAttrValue("AXIS", 1)
    return order0


if __name__ == '__main__':
    main()
