##from pygal.maps.world import COUNTRIES
#for x,y in  COUNTRIES.items():
    #print(x,y) 顯示各國代碼
import pygal.maps.world
worldmap=pygal.maps.world.World()
worldmap.title='China/Japan/Thailand'
worldmap.add('Asia',['cn','jp','th'])#國家代碼
worldmap.render_to_file('taiwan.svg')
##渲染地圖到svg檔案 可網頁打開世界地圖