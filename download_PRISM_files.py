#A script for downloading mean temperature data at a 4-km spatial scale from PRISM, for the years 1981-2020:

import requests

base_url = 'http://services.nacse.org/prism/data/public/4km/'
data_type = 'tmean/'

for year in range(1981, 2020):
	year = str(year)
	for month in [3, 4, 8, 9, 10, 11]:
		print('Downloading year={}, month={}...'.format(year, month))
		month = str(month).zfill(2)
		print(base_url + data_type + year + month)
		r = requests.get(base_url + data_type + year + month, allow_redirects=True)
		filename = r.headers['content-disposition'].replace('\"', '').replace('filename=', '')
		open(filename, 'wb').write(r.content)
		print('Success')

