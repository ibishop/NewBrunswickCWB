import geopandas as gpd

"""
This file is used to quickly load shapefiles
As well, it contains a few helper methods
"""

def cd_shape(path = 'shapefiles/census_division/census_divisions.shp'):
    '''

    :param path: The path to the census division shape file
    :return: GeoDataFrame, containing the desired shape
    '''
    return gpd.read_file(path)


def csd_shape(path = 'shapefiles/census_subdivsion_bound/census_subdivision_b.shp'):
    '''

    :param path: The path to the bounded census subdivision shape file
    :return: GeoDataFrame, containing the desired shape
    '''
    return gpd.read_file(path)

def hr_shape(path = 'shapefiles/health_regions/health_region.shp'):
    '''

    :param path: The path to the health region shape file
    :return: GeoDataFrame, containing the desired shape
    '''
    return gpd.read_file(path)

def nb_mun_shape(path = ''):
    '''

    :param path: The path to the municipality shape file
    :return: GeoDataFrame, containing the desired shape
    '''
    return gpd.read_file(path)

def nb_prop_shape(path = 'shapefiles/nb_property/nb_properties.shp'):
    '''

    :param path: The path to the properties shape file
    :return: GeoDataFrame, containing the desired shape
    '''
    return gpd.read_file(path)

def filter_prov(df,id):
    '''
    Filters DataFrame to contain only provinces with the specified id

    :argument df: dataframe, with column 'PRUID'
    :argument id: string
        '10' = NFLD
        '11' = PEI
        '12' = NS
        '13' = NB
    :return:
    '''

    if not isinstance(id, str):
        raise ValueError("ID is not a string")

    return df.loc[ df['PRUID'] == id ]


def reproject(df , crs = "EPSG:4326"):
    '''
    Projects dataframe to designated CRS, by default WGS lat-long (EPSG:4326)
    :param df: GeoDataFrame
    :param crs: CRS to re-project the dataframe
    :return: the reprojected dataframe
    '''
    return df.to_crs(crs)

