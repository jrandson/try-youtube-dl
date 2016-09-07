import youtube_dl
from subprocess import call

import gzip
import zipfile, os, fnmatch
import shutil
from os import path, listdir


class System():

	def __ini__(self):
		pass

	def split_full_path(self,path):

		parent, name = path.split(path)
		if parent == "":
			return name
		else:
			 return split_full_path(name) +  parent

	def get_extension(self,file_name):
		return path.splitext(file_name)[1]

	def exists(self,path_dir):
		return path.exists(path_dir)

	def write_file(self):
		a = open('file.txt','a')
		a.write('\n and another')
		a.close()	
		
	def createfile(self):
		content = "Lots of content here"
		with gzip.open('file.gz', 'wb') as f:
			f.write(content)	

	def get_content_dir(self,path_dir = None):
		if path_dir == None:
			path_dir = '.'

		if self.exists(path_dir):
			return listdir(path_dir)
		else:
			return []
	
	def get_content_from_current_directory(self):
		return listdir('.')

	def get_full_path(self, dir_path):
		for path_name in listdir(dir_path):
			print path.join(dir_path,path_name)

	def print_tree(self, dir_path):
		for name in os.listdir(dir_path):
			full_path  = os.path.join(dir_path, name)
			print full_path
			if path.isdir(full_path):
				self.print_tree(full_path)
	
	def get_size(self, file_name):
		return path.getsize(file_name)

	def rename_copy_remove(self):
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



class YoutubeDl():

	def __init__(self):
		self.syst = System()

	def download_music_from_url(self, url):
		os.mkdir('tmp')
		os.chdir('tmp')

		command = "youtube-dl --extract-audio --audio-format mp3 "
		command += url + " -c"
		print "downloading " + url
		call(command.split(), shell=False)

		content = self.syst.get_content_dir()
		if len(content) > 1:
			file_name = self.compress_all_mp3_files()
			shutil.move(file_name,'..')
		else:
			shutil.copy(content[0],'..')
	
		os.chdir('..')
		shutil.rmtree('tmp')
	
	def download_musics_from_file_list(self, file_list):		
		
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
		
	def compress_all_mp3_files(self, directory =None):		

		if directory == None:
			directory = '.'

		file_name = 'donwload.zip'

		musics= zipfile.ZipFile( file_name, 'w', zipfile.ZIP_DEFLATED )		

		contents = self.syst.get_content_dir(directory)
		for content in contents:
			if self.syst.get_extension(content) == '.mp3':
				path_content = path.join(directory, content)			
				print path_content
				musics.write(path_content)
		
		musics.close()	

		return file_name	

	def compress_all_files(self, directory = None):
		
		if directory == None:
			directory = '.'

		file_name = 'download.zip'

		contents = self.syst.get_content_dir(directory)

		musics= zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED )	
		
		for content in contents:
			path_content = path.join(directory,content)
			print path_content
			musics.write(path_content)
		
		musics.close()

		return file_name

	def zip_file(self, file_name):

		zip_file = zipfile.ZipFile( 'zip_file.zip', 'w', zipfile.ZIP_DEFLATED )
		zip_file .write(file_name)
		zip_file .close()


syst = System()
ytd = YoutubeDl()

ytd.download_music_from_url('https://www.youtube.com/watch?v=2oHyOe1tlC8&list=PL8n8VJudkeOEOXYEhwlJDZUfJiNgGhmQb')
#ytd.download_musics_from_file_list('lista.txt')

