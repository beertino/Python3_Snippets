# Modified from https://www.dev2qa.com/how-to-download-image-file-from-url-use-python-requests-or-wget-module/
# Import requests, shutil python module.
import requests
import shutil
import time 

for i in range(1,5):
    # This is the image url.
    image_url = "http://game-a1.granbluefantasy.jp/assets_en/img/sp/assets/comic/episode/episode_"+str(i)+".jpg"
    
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(image_url, stream=True)
    
    # Open a local file with wb ( write binary ) permission.
    local_file = open("episode_"+str(i)+".jpg", 'wb')
    
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True
    
    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)
    
    # Remove the image url response object.
    del resp
    
    # Need to close the file so we can delete
    local_file.close()
    
    # Loop is run every 5 seconds to not spam the server
    time.sleep(5) 
