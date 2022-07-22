import os
import re
import shutil
import subprocess

github_link = 'https://github.com/eranyoung/osuSkins/tree/master/Skins/' #change this to your github website
osu_folder = '/Users/erany/AppData/Local/osu!' #change this to your osu! directory
skins_dir = osu_folder + '/Skins'

subprocess.call('C:/Users/erany/OneDrive/Desktop/osuskinthumbnailcreator/main.py', shell='True') #experimental, for generating images automatically, delete this line for just links

def generate():
	entries = os.listdir(skins_dir)
	f = open('README.md', 'w')
	f.write('# My Osu! Skins' + '\n')
	for entry in entries:
		filename = re.sub('\W+', '', entry)
		f.write('\n## '+filename)
		f.write(' [Download](' + github_link+filename+'.osk' +')' )
		f.write('\n ![Screenshoot](Screenshots/' + filename + '.webp)')
		if not os.path.isfile('Skins/' + filename+'.osk'):
			print('writing ' + filename + "...")
			shutil.make_archive(filename, 'zip', skins_dir + '/' + entry)
			os.rename(filename+'.zip', filename+'.osk')
			shutil.move(filename+'.osk', 'Skins')

generate()
print('done')