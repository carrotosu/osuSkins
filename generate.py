import os
import re
import shutil

github_link = 'https://github.com/eranyoung/osuSkins/tree/master/Skins/'
osu_folder = '/Users/erany/AppData/Local/osu!'
skins_dir = osu_folder + '/Skins'

def generate():
	entries = os.listdir(skins_dir)
	f = open('README.md', 'w')
	f.write('# My Osu! Skins' + '\n')
	for entry in entries:
		filename = re.sub('\W+', '', entry)
		f.write('\n## '+filename+'\n')
		f.write('[Download](' + github_link+filename+'.osk' +')' )
		if not os.path.isfile('Skins/' + filename+'.osk'):
			shutil.make_archive(filename, 'zip', skins_dir + '/' + entry)
			os.rename(filename+'.zip', filename+'.osk')
			shutil.move(filename+'.osk', 'Skins')

generate()