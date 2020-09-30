import pandas as pd
import glob
"""
This file is for automatically loading tabular datasets
It will not open shapefiles. 
It presumes that it is run from the root directory.

"""

def census(year):
    '''Returns the unclean community profiles from the Census Datasets'''
    if year == 2001:
        return pd.read_csv('data/census_data/census_2001.csv')

    if year == 2006:
        return pd.read_csv('data/census_data/census_2006.csv')

    if year == 2011:
        return pd.read_csv('data/census_data/census_2011.csv')

    if year == 2016:
        return pd.read_csv('data/census_data/census_2016.csv')


def census_unclean(year):
    '''Returns the unclean community profiles from the Census Datasets, merging those in seperate parts'''
    if year == 2001:
        return pd.concat([ pd.read_csv(path,skiprows=2,skipfooter=134,engine='python',index_col=False) for path in glob.glob('data/census_profiles_unclean/Census_2001/*')])

    if year == 2006:
        return pd.concat([ pd.read_csv(path,skiprows=2,skipfooter=140,engine='python',index_col=False) for path in glob.glob('data/census_profiles_unclean/Census_2006/*')])

    if year == 2011:
        return pd.concat([ pd.read_csv(path, encoding='cp1252',index_col=False) for path in glob.glob('data/census_profiles_unclean/Census_2011/*')])

    if year == 2016:
        return pd.read_csv('data/census_profiles_unclean/census_2016.csv',index_col=False)

def census_profiles():
    '''

    :return:
    '''
    df = pd.read_csv("data/census_data/total_census_profiles.csv", index_col=0)
    return

def comm_well_being(year):
    '''

    :param year:
    :return:
    '''
    if year == 2016:
        return pd.read_csv('data/community_well_being/CWB_' + str(year)  + '.csv',index_col=0,encoding='cp1252')
    if year == 2011:
        return pd.read_csv('data/community_well_being/CWB_' + str(year)  + '.csv',index_col=0,encoding='cp1252')
    if year == 2006:
        return pd.read_csv('data/community_well_being/CWB_' + str(year)  + '.csv', index_col=0,encoding='cp1252')
    if year == 2001:
        return pd.read_csv('data/community_well_being/CWB_' + str(year)  + '.csv', index_col=0,encoding='cp1252')
    if year == "all":
        df = pd.concat([comm_well_being(2001),comm_well_being(2006),comm_well_being(2011),comm_well_being(2016)],axis=1)
        df.index.name = 'CSD Code'
        return df



    raise ValueError("Year invalid, could not be int or wrong year")

def temp_census(path = 'data/census_temp/temp.csv'):
    '''

    :return:
    '''
    return pd.read_csv(path)

def property_values():
    '''

    :return:
    '''

    return pd.read_csv("data/nb_property_values/nb_properties.csv",index_col=0)

def cwb_filter_prov(df,prov):
    '''
    Filter CWB DataFrame by province
    (Filters using first 2 digits of index column)
    :param prov: A string denoting the province
        'NFLD' = 10
        'PEI' = 11
        'NS' = 12
        'NB' = 13

    :return: dataframe containing only the desired rows
    '''
    if df.index.name is None:
        raise ValueError('df is not CWB dataframe (index.name is NoneType)')
    if 'CSD Code' not in df.index.name:
        raise ValueError('df is not CWB dataframe (index.name does not contain \'CSD Code\')')
    if prov not in ['NB','NS','NFLD','PEI']:
        raise ValueError("prov is not valid")

    # Create Series of first two digits
    index = pd.Series(df.index,index=df.index).div(100000).apply(lambda x: int(x))

    if prov is 'NB':
        return df.loc[index == 13]
    if prov is 'NS':
        return df.loc[index == 12]
    if prov is 'PEI':
        return df.loc[index == 11]
    if prov is 'NFLD':
        return df.loc[index == 10]
