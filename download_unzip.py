

#method1: the most basic way is using /tem folder to stroe the zip file downloded from online

from zipfile import ZipFile
from urllib.request import urlopen
# Download the file from the URL
zipurl = 'http://zju-capg.org/myo/data/dbb-preprocessed-001.zip'
zipresp =  urlopen(zipurl)
# Create a new file on the hard drive
tempzip = open("data/tempfile.zip", "wb")
# Write the contents of the downloaded file into the new file
tempzip.write(zipresp.read())
# Close the newly-created file
tempzip.close()
# Re-open the newly-created file with ZipFile()
zf = ZipFile("data/tempfile.zip")
# Extract its contents into <extraction_path>
# note that extractall will automatically create the path
zf.extractall(path = 'data')
# close the ZipFile instance
zf.close()
