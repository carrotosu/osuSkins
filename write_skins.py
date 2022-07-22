import os
import re
import shutil

github_link = 'https://github.com/eranyoung/osuSkins/tree/master/Skins/'

def getAllSkins():
	entries = os.listdir('/Users/erany/AppData/Local/osu!/Skins')
	f = open('README.md', 'w')
	f.write('# My Osu! Skins' + '\n')
	for entry in entries:
		filename = re.sub('[^A-Za-z0–9]', '', entry)
		f.write('\n## '+filename+'\n')
		f.write('[Download](' + github_link+filename+'.osk' +')' )
		if not os.path.isfile('Skins/' + filename+'.osk'):
			shutil.make_archive(filename, 'zip', '/Users/erany/AppData/Local/osu!/Skins/'+entry)
			os.rename(filename+'.zip', filename+'.osk')
			shutil.move(filename+'.osk', 'Skins')

getAllSkins()