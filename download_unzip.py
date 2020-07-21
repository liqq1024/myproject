

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

#method2: Shutil and tempfilePermalink. In previous solution we went into the trouble of saving the temporary 
#file in /tmp folder. But there is an easy way around in Python Python has a inbuild module called tempfile 
#that can make a temporary file or folder for and do auto cleanup afterwards. We will use shutil module instead 
#of zipfile in this example

from tempfile import NamedTemporaryFile
from shutil import unpack_archive
from urllib.request import urlopen
# Download the file from the URL
zipurl = 'http://zju-capg.org/myo/data/dbb-preprocessed-001.zip'
with urlopen(zipurl) as zipresp, NamedTemporaryFile() as tfile:
    tfile.write(zipresp.read())
    tfile.seek(0)
    unpack_archive(tfile.name, 'data', format='zip')
    
#method3: Unzipping without saving the zipPermalink. 
#Now this method will not create and save any files. It will directly save the extracted file

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://zju-capg.org/myo/data/dbb-preprocessed-001.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('data')














