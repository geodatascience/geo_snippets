

def split_line_to_points(input_gdf):
    """
    split each linestring row from a geodataframe to point

    :param input_gdf: your geodataframe containing linestrings
    :type input_gdf: Geopandas.GeoDataframe
    :return: your geodataframe exploded containing points
    :rtype: Pandas.Dataframe
    """

    from shapely.geometry import Point

    # prepare indexed columns
    columns_index = input_gdf.columns.tolist()
    # without geometry column.. because we want explode it
    columns_index.remove("geometry")

    # convert the linestring to a list of points
    input_gdf["geometry"] = input_gdf["geometry"].apply(lambda x: [Point(f) for f in x.coords])
    # set index with columns_index variable (without geometry)
    input_gdf.set_index(columns_index , inplace=True)
    output = input_gdf["geometry"].explode().reset_index()
    #TODO convert to geodataframe
    return output
