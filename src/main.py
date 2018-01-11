import pymesh
import json

with open("mock_building.json",'r') as f:
    MOCK_BUILDING = json.load(f)

#load footprints and height of a building from shp
def load_building_geojson():
    return MOCK_BUILDING

def read_footpoints2(building_geojson):
    '''得到建筑的脚点坐标列表 形如[[x0,y0], [x1,y1],...]'''
    geometry = building_geojson['geometry']
    assert geometry['type'] == 'Polygon', f'{geometry}的类型不是 Polygon'
    return geometry['coordinates'][0]

def augment_footpoints2to3(footpoints2):
    '''补z坐标，0'''
    return [[x[0], x[1], 0] for x in footpoints2]

def get_footpoints3(building_geojson):
    footpoints2 = read_footpoints2(building_geojson)
    #print(footpoints2)
    footpoints3 = augment_footpoints2to3(footpoints2)
    return footpoints3

def read_height(building_geojson):
    '''每个建筑的高度，不同来源的数据可能不同，这里是最简单的一个值'''
    return building_geojson["properties"]["VALUE"]

def get_headpoints3(footpoints3, height):
    return [[x[0], x[1], height] for x in footpoints3]

# build mesh model
def build_3d_model_from_footpoints3_and_height(footpoints3, height):
    
    #屋顶3d坐标
    headpoints3 = get_headpoints3(footpoints3, height)
    #建筑全部顶点
    vertex = footpoints3.extend(headpoints3)
    return None
# save to .obj format 

def shp2obj():
    building1_geo_json = load_building_geojson()
    footpoints3 = get_footpoints3(building1_geo_json)
    height = read_height(building1_geo_json)
    model = build_3d_model_from_footpoints3_and_height(footpoints3, height)
    print(footpoints3, height)
    print('haha')


if __name__ =='__main__':
    shp2obj()
