from bs4 import BeautifulSoup as bs
import requests
import urllib
from PIL import Image 

#define website and station
station_id = 44008 
root_path = 'https://www.ndbc.noaa.gov'
station_path = '/station_page.php?station='

#takes path and returns html
def get_html(r_p, s_p, sta_id):
    try:
        filepath = r_p + s_p + '{}' .format(sta_id)
        r = requests.get(url = filepath)
        assert r.status_code == 200
        r.raise_for_status()
        html = r.content
        return html
    except:
        raise ValueError('Could not retrieve HTML')
        
#takes soup/html returns src attribute
def get_src_attr(soup, sta_id):
    try:
        img = soup.findAll('img', {'alt': 'Photos from Buoy Camera at station {}' .format(sta_id)})
        src_attr = img[0]['src']
        return src_attr
    except:
        raise ValueError('Could not retrieve src attribute')
        
#takes image path and saves image to file with timestamp name
def save_img(img_path, src):
    try:
        raw_img = requests.get(url = img_path, stream = True)
        raw_img.raise_for_status()
        raw_img.raw.decode_content = True
        timestamp = str(src).split('/')
        with Image.open(raw_img.raw) as img:
            img.save('Test_Images/{}' .format(timestamp[-1]), 'JPEG') #JPEG
            img.save('Temp_Img/{}' .format(timestamp[-1]), 'JPEG') #JPEG
        raw_img.close() 
    except:
        raise ValueError('Could not save image')

#gets takes station id, retrives, then saves image
def retrieve_image(sta_id):
    try:
        html = get_html(root_path, station_path, sta_id)
        soup = bs(html, 'html5lib')
        src_attr = get_src_attr(soup, sta_id)   
        img_path = root_path + src_attr 
        save_img(img_path, src_attr)

    except ValueError as err:
        raise err
        #print(err.args)