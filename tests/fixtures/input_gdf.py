import pytest

from shapely.geometry import LineString

import geojson
import geopandas as gpd


def build_gdf(features):
    all_geojson_features = []
    for feature in features:
        feature["properties"]["bounds"] = ", ".join(
            map(str, feature["geometry"].bounds)
        )
        feature = geojson.Feature(
            geometry=feature["geometry"], properties=feature["properties"]
        )
        all_geojson_features.append(feature)
    return gpd.GeoDataFrame.from_features(all_geojson_features)


@pytest.fixture
def gdf_linestrings():
    all_features = [
        {
            "geometry": LineString(
                [
                    (4.07114907206, 46.0376034527),
                    (4.07091681769, 46.03699538217),
                    (4.07079583285, 46.03660928470),
                ]
            ),
            "properties": {"a": 42, "b": "hello"},
        },
        {
            "geometry": LineString(
                [
                    (4.07079583285, 46.036609284706),
                    (4.07085925751, 46.036602948616),
                    (4.07086909165, 46.036677933937),
                    (4.07093731600, 46.036749231456),
                    (4.07103135497, 46.036703133922),
                    (4.07098587207, 46.036623231531),
                ]
            ),
            "properties": {"a": 52, "b": "coucou"},
        },
    ]
    output_gdf = build_gdf(all_features)

    return output_gdf
