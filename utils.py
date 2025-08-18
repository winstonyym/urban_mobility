import h3
from shapely.geometry import Point, Polygon, MultiPolygon

def swap_lat_lon(geom):
    if geom.geom_type == 'Point':
        lat, lon = geom.coords[0]
        return Point(lon, lat)
    elif geom.geom_type == 'Polygon':
        return Polygon([(lon, lat) for lat, lon in geom.exterior.coords])
    elif geom.geom_type == 'MultiPolygon':
        return MultiPolygon([Polygon([(lon, lat) for lat, lon in poly.exterior.coords]) for poly in geom.geoms])
    else:
        return geom


def gdf_to_h3_hexagons(gdf, resolution=9):
    """
    Given a GeoDataFrame, returns a GeoDataFrame of H3 hexagons covering its geometry.
    The output GeoDataFrame has columns 'hex_id' and 'geometry' (with correct lon/lat order).
    """
    # Get hexagon ids
    hexagon_ids = h3.geo_to_cells(gdf.__geo_interface__, resolution)
    # Polygonise with correct (lon, lat) order
    def polygonise(hex_id):
        return Polygon([(lon, lat) for lat, lon in h3.cell_to_boundary(hex_id)])
    hex_gdf = gdf.GeoDataFrame(
        {'hex_id': list(hexagon_ids), 'geometry': [polygonise(hid) for hid in hexagon_ids]},
        crs="EPSG:4326"
    )

    hex_gdf['geometry'] = hex_gdf['geometry'].apply(swap_lat_lon)

    return hex_gdf