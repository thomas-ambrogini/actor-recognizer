from google_images_download import google_images_download
import urllib.request
from urllib.request import urlopen
import bs4 as bs


response = google_images_download.googleimagesdownload() 

def imbd_function(num_actors):
    num_pages = num_actors // 50
    print(num_pages)
    names_list = []
    
    for page in range(num_pages):
        my_url = 'https://www.imdb.com/search/name/?match_all=true&start={}&ref_=rlm'.format(page * 50 + 1)
        imdb = urlopen(my_url)

        bsobj = bs.BeautifulSoup(imdb.read(),'html.parser')

        pic = bsobj.findAll('img')

        for img in pic:
            name = img.get('alt')
            names_list.append(name)

    return names_list
  
  
def download_actor_images(query):
    directory_name = query.replace(" ", "_")
    
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":20,
                 "print_urls":True,
                 "image_directory": "{}".format(directory_name),
                 "size": "medium",
                 "aspect_ratio":"panoramic"}
    try:
        response.download(arguments)
         
    except: 
        print("impossibile scaricare immagine")

def download_images(num_images):
    names_list = imbd_function(num_images)
    print(names_list)

    for name in names_list:
        download_actor_images(name)
        print()

    

download_images(200)
