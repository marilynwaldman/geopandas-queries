#  
# http://localhost:5000/map?map=california_kerncounty.html
# ?page=1&sort=title
# point within https://stackoverflow.com/questions/60328417/geopandas-not-recognizing-point-in-polygon

import geopandas as gpd
import pandas as pd
from flask import Flask, request
from flask import jsonify
from shapely.geometry import Point, Polygon
from utilities import point_to_df, df_to_geodf

congress_gdf = gpd.read_file('2021_Final_Approved_Congressional_Plan.zip')
county_gdf = gpd.read_file('Colorado_County_Boundaries')

def list_of_polygons_pt_is_in(lat, lon, gdf):

#  lat - latitude - float
#  lon - longtitude - float
#  gdf_utm10 - geopandas df with geometry to test - 
#  return - list of rows of gdf containing the point
    
    #convert point to dataframe    
    point_df = point_to_df(lat,lon) 
    # coerce it to a GeoDataFrame
    # transform to EPSG:26910
    point_gdf_utm10 = df_to_geodf(point_df)
    gdf_utm10 = gdf.to_crs("epsg:26910")
    polygons_containing_point = gpd.sjoin(gdf_utm10,point_gdf_utm10 , op='contains')
    
    return polygons_containing_point



app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(response_value_1=1,response_value_2="value")

  

@app.route('/district', methods=['GET', 'POST'])
#http://localhost:8000/district?lat=37.209 &lon=-107.788
def get_district():
    args = request.args
    lat = float(args['lat'])
    lon = float(args['lon'])

    if lat == None or lon == None:
        return jsonify(polygons=[], msg="latitutde or longtitude not defined")
    
    polygons = list_of_polygons_pt_is_in(lat, lon, congress_gdf)

    return jsonify(district=polygons['LONGNAME'].tolist(), msg="District Found")
     
@app.route('/county', methods=['GET', 'POST'])
#http://localhost:8000/county?lat=37.209 &lon=-107.788
def get_county():
    args = request.args
    lat = float(args['lat'])
    lon = float(args['lon'])

    if lat == None or lon == None:
        return jsonify(polygons=[], msg="latitutde or longtitude not defined")
    
    polygons = list_of_polygons_pt_is_in(lat, lon, county_gdf)

    return jsonify(county=polygons['FULL'].tolist(), msg="County Found")
     

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    
