import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br')
except:
    print('Deu erro')
else:
    print('TUDO OK')
    print(site.read())