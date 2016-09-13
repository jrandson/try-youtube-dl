from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

import youtube_dl
from subprocess import call
from  django.utils import timezone

import gzip
import zipfile, os, fnmatch
import shutil
from os import path, listdir

from .forms import UploadFileForm


# Create your views here.

def index(request):
	upl_form = UploadFileForm()

	context = {
		'upload_form' : upl_form,
	}
	
	return render(request,'tryYoutubeDl/index.html',context)


def download_from_url(request):

	if request.method == 'POST':

		url = request.POST['url']
		file_type = request.POST['file_type']

		download([url],file_type)

		return render(request,'tryYoutubeDl/download.html',{})

	return redirect('tryYoutubeDl:index')


def download_from_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file_name']
            file_type = request.FILES['file_type']
            urls = []
            for url in f:
            	if len(url.strip()) > 0:	        		
	        		urls.append(url)
	        		print url

	        
	        if len(urls) == 0:
	        	raise Error('give at the least an valid url')

	        if not path.exists('files'):
				os.mkdir('files')

	        content = download(urls, file_type)
	      
            context = {
            	'urls' : urls,
            	'content': content,
            }            

            #return HttpResponse('Successfull download')
            return render(request,'tryYoutubeDl/download.html',context)

    else:
        form = UploadFileForm()
    
    
    content  ={
    	'upload_form' : form,
    }

    return render(request, 'tryYoutubeDl/index.html', content)

def download(urls, file_type='mp4'):

	if file_type == 'mp3':
		options = {
				    'format': 'bestaudio/best', # choice of quality
				    'extractaudio' : True ,      # only keep the audio
				    'audioformat' : 'mp3',      # convert to mp3 
				    'outtmpl': '%(id)s',        # name the file the ID of the video
				    'noplaylist' : True,        # only download single song, not playlist
				}
	else:
		options = {}		

	with youtube_dl.YoutubeDL(options) as ydl:
	    ydl.download(urls)

	content = get_content_dir()	

	return content

def get_url_from_file(url_file):
	try:
		if not self.syst.exists(url_file):
			raise Error('File not found')

		f = open(url_file,'r')
		urls = []
		for url in f:
			if url :
				urls.append(url)
		f.close()		
		
		return urls
	except Error, e:
		print 'An error has ocurred', e.value
		return None

def compress_all_files(directory = None):
	
	if directory == None:
		directory = '.'

	file_name = 'download' + str(timezone.now())+'.zip'

	contents = get_content_dir(directory)

	musics= zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED )	
	
	for content in contents:
		path_content = path.join(directory,content)
		print path_content
		musics.write(path_content)
	
	musics.close()

	return file_name

def zip_file(file_name):

	zip_file = zipfile.ZipFile( 'zip_file.zip', 'w', zipfile.ZIP_DEFLATED )
	zip_file .write(file_name)
	zip_file .close()

def get_meta_info(url):

	with youtube_dl.YoutubeDL({}) as ydl:
	    
		meta = ydl.extract_info(url, download=False)

	return meta

#---------------------------------------------------


def split_full_path(path):

	parent, name = path.split(path)
	if parent == "":
		return name
	else:
		 return split_full_path(name) +  parent

def get_extension(file_name):
	return path.splitext(file_name)[1]

def write_file():
	a = open('file.txt','a')
	a.write('\n and another')
	a.close()	
	
def createfile():
	content = "Lots of content here"
	with gzip.open('file.gz', 'wb') as f:
		f.write(content)	

def get_content_dir(path_dir = None):
	if path_dir == None:
		path_dir = '.'

	if path.exists(path_dir):
		return listdir(path_dir)
	else:
		return []

def get_content_from_current_directory():
	return listdir('.')

def get_full_path(dir_path):
	for path_name in listdir(dir_path):
		print path.join(dir_path,path_name)

def print_tree(dir_path):
	for name in os.listdir(dir_path):
		full_path  = os.path.join(dir_path, name)
		print full_path
		if path.isdir(full_path):
			print_tree(full_path)

def get_size(file_name):
	return path.getsize(file_name)

def rename_copy_remove():
	shutil.move(file_name, new_name)
	shutil.copy(source, destine)
	shutil.remove(file_name)

	os.mkdir('dir_name')
	#create many directory at once
	os.makedirs('dir_parent/another_dir/more_one/dir_name')
	#the dir must be empy first
	os.rmdir('dir_name')

	#ddanger: remove everything
	shutil.rmtree('some_dir')






