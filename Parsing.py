import re
import webbrowser
import platform
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = 'https://www.rarlab.com'

html = urlopen(URL).read()
soup = BeautifulSoup(html, features="html.parser")

# get version
version = soup.find('b').get_text()
last_updated = soup.find(string=re.compile("updated"))
print("Release " + version.split(‘ ‘)[3] + last_updated)
get_rar_latest = soup.find(string=re.compile("Russian"))
download_version = soup.select('a[href$="ru.exe"]')
print(get_rar_latest[3:10])
#function get architecture & download link
def os_arc_download():
    arc_ver = platform.machine()
    ver64 = download_version[1]
    ver32 = download_version[0]
    lnk64=ver64['href']
    lnk32=ver32['href']
    download_lnk_x64 = URL + lnk64
    download_lnk_x32 = URL + lnk32
    if arc_ver == "AMD64":
        print(download_lnk_x64)
        webbrowser.open_new(download_lnk_x64)
    else:
        print(download_lnk_x32)
        webbrowser.open_new(download_lnk_x32)
os_arc_download()
