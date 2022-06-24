import requests
import urllib.parse
from datetime import datetime

adres = input("Adresinizi giriniz:\n")

# Meteorolojik durumların sözlüğü

durumsözlük = {
    "snow": "Kar yağışı var.",
    "rain": "Yağmur yağıyor.",
    "frzr": "Dondurucu yağmur var.",
    "icep": "Dolu yağıyor.",
    "none": "Şu anlık hiçbir şey yok."
}

# Adresten enlem ve boylam alma
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(adres) +'?format=json'
adresrequest = requests.get(url).json()
boylam = adresrequest[0]["lon"]
enlem = adresrequest[0]['lat']

# Hava durumu alma
resp = f"https://www.7timer.info/bin/astro.php?lon={boylam}&lat={enlem}&ac=0&unit=metric&output=json&tzshift=3"
bilgi = requests.get(resp).json()["dataseries"]
yakınlaştırma = [i * 3 for i in range(9)][round(datetime.now().hour / 3)] # Şu anki zamanı hava durumunun ölçülmüş zamanlarına yuvarlama.

print("Hissedilen " + str(bilgi[yakınlaştırma]["temp2m"]) + " derece.")
print(durumsözlük[bilgi[yakınlaştırma]["prec_type"]])
