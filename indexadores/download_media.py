import requests
#response = requests.get('https://us02web.zoom.us/rec/download/ev8n3ssttZZ8uOfKGgup9Ig7Wij9mfJddAX-H4c1XsBX0WomVrs3Ncn6Py6YtZ61NNzMP-njj-PFXnE-.SKAZimgEU8y8NOb4')
#print(response.status_code)
#print(len(response.content))

#In: https://stackoverflow.com/questions/30953104/download-video-from-url-in-python

#import urllib.request
#url = 'https://www.youtube.com/watch?v=v-F2QeL6Cxc'
#urllib.request.urlretrieve(url, "Teste.mp4")

#from urllib.request import urlopen 
#dwn_link = 'https://us02web.zoom.us/rec/download/ev8n3ssttZZ8uOfKGgup9Ig7Wij9mfJddAX-H4c1XsBX0WomVrs3Ncn6Py6YtZ61NNzMP-njj-PFXnE-.SKAZimgEU8y8NOb4'
#
#file_name = 'trial_video.mp4' 
#rsp = urlopen(dwn_link)
#with open(file_name,'wb') as f:
#    f.write(rsp.read())
#    f.close()

#import urllib
##import re
#from BeautifulSoup import BeautifulSoup
#
#""" 
#Download this file in html version 
#https://docs.google.com/spreadsheet/ccc?key=0AsKzpC8gYBmTcGpHbFlILThBSzhmZkRhNm8yYllsWGc&hl=en#gid=0"
#"""
#url = "The URL of above file" # url = "file:///home/jay/Downloads/index.html"
#
#proxy = {"http":"http://user:pass@proxy:port/","https":"https://http://user:pass@proxy:port/"}
#Proxy = urllib.ProxyHandler(proxy)
#opener = urllib.build_opener(Proxy)
#urllib.install_opener(opener)
#page=urllib.urlopen(url)
#soup=BeautifulSoup(page.read())
#
#links=[]
#hrefs = soup.findAll("a",{"target":True,"href":True,"style":True})
#for link in hrefs:
#    #print link.contents
#    links.append(link.contents[0])
#for vids in links:
#    page = urllib.urlopen(vids)
#    soup = BeautifulSoup(page.read())
##print soup.prettify()
#    vid_link = soup.find("meta",{"property":"og:video","content":True})["content"]
#    print (vid_link)
#    print ("Downloading",vid_link.split("/")[-1])
#    f = open(vid_link.split("/")[-1],"wb")
#    f.write(opener.open(vid_link).read())
#    f.close()
#
##In: https://gist.github.com/jayrambhia/2015497

  
#import urllib.request
##url = input("Enter the Youtube-url\n")
##name = input("Enter the name for the video\n")
##name=name+".mp4"
#try:
#    print("Downloading starts...\n")
##    urllib.request.urlretrieve(url, name)
#    urllib.request.urlretrieve("https://us02web.zoom.us/rec/download/ev8n3ssttZZ8uOfKGgup9Ig7Wij9mfJddAX-H4c1XsBX0WomVrs3Ncn6Py6YtZ61NNzMP-njj-PFXnE-.SKAZimgEU8y8NOb4", "Teste.mp4")
#    print("Download completed..!!")
#except Exception as e:
#    print(e)
#
#In: https://github.com/ankitjain28may/pythonResources/blob/master/Download%20video%20from%20cmd%20using%20python/run.py


def download_video_series(video_links): 

    #for link in video_links: 

        '''iterate through all links in video_links 
        and download them one by one'''

        # obtain filename by splitting url and getting  
        # last string 
        #file_name = link.split('/')[-1]    
#
        #print ("Downloading file:%s"%file_name) 

        # create response object 
        r = requests.get(video_links, stream = True) 

        # download started 
        with open("Teste.mp4", 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 

#        print ("%s downloaded!\n"%file_name) 

 #   print ("All videos downloaded!")
         # return

download_video_series("https://us02web.zoom.us/rec/download/ev8n3ssttZZ8uOfKGgup9Ig7Wij9mfJddAX-H4c1XsBX0WomVrs3Ncn6Py6YtZ61NNzMP-njj-PFXnE-.SKAZimgEU8y8NOb4")