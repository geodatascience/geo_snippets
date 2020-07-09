from geo_snippets.geopandas import split_line_to_points

def test_split_line_to_points(gdf_linestrings):

    assert gdf_linestrings.shape[0] == 2
    assert gdf_linestrings.shape[-1] == 4

    output = split_line_to_points(gdf_linestrings)

    assert output.shape[0] == 9
    assert output.shape[-1] == 4
