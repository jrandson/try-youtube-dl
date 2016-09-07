from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

import youtube_dl
from subprocess import call

import gzip
import zipfile, os, fnmatch
import shutil
from os import path, listdir

import youtubedl

# Create your views here.

def index(request):

	return render(request,'tryYoutubeDl/index.html',{})



def download_from_url(request):

	if request.method == 'POST':

		url = request.POST['url']
		file_type = request.POST['file_type']

		download_by_url(url,file_type)

		return render(request,'tryYoutubeDl/download.html',{})

	return redirect('tryYoutubeDl:index')

def download_from_file(request):

	if request.method == 'POST':

		url = request.POST['url']
		file_type = request.POST['file_type']

		if file_type == 'mp3':
			download_music_from_url(url)
		elif file_type == 'mp4':
			download_video_from_url(url)
		
		#ytd.download_musics_from_file_list('lista.txt')

		return render(request,'tryYoutubeDl/download.html',{})

	return redirect('tryYoutubeDl:index')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def download_by_url(url, type_file):
	os.chdir('files')
	if path.exists('tmp'):
		shutil.rmtree('tmp')

	os.mkdir('tmp')
	os.chdir('tmp')

	command = "youtube-dl "
	if type_file == 'mp3':
		command += "--extract-audio --audio-format mp3 "	

	command += url + " -c"
	call(command.split(), shell=False)

	content = get_content_dir()
	if len(content) > 1:
		file_name = compress_all_files()
		shutil.move(file_name,'..')
	else:
		shutil.copy(content[0],'..')

	os.chdir('..')
	shutil.rmtree('tmp')
	os.chdir('..')

def download_by_filelist(url):
	try:
		if not self.syst.exists(file_list):
			raise Error('File not found')

		f = open(file_list,'r')

		for url in f:
			if url :
				command = "youtube-dl --extract-audio --audio-format mp3 "
				command += url + " -c"
				print "downloading " + url
				call(command.split(), shell=False)			

		f.close()		
		
	except Error, e:
		print 'An error has ocurred', e.value

def compress_all_files(directory = None):
	
	if directory == None:
		directory = '.'

	file_name = 'download.zip'

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






