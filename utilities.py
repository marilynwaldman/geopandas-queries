import pandas as pd
import geopandas as gpd

def point_to_df(lat, lon):


    mydict = {'Y': lat,
             'X': lon }
             
    df = pd.DataFrame()
    df = df.append(mydict, ignore_index=True)
    return df

def df_to_geodf(point_df):
    point_gdf = gpd.GeoDataFrame(point_df, 
                               geometry=gpd.points_from_xy(point_df.X, point_df.Y))
    # define its unprojected (EPSG:4326) CRS
    point_gdf.crs = "epsg:4326"
    # transform to EPSG:26910
    point_gdf_utm10 = point_gdf.to_crs( "epsg:26910")
    return point_gdf_utm10    