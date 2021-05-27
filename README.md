# ADS - Landscape Classifier

## Inhaltsverzeichnis
<ol>
  <li><a href="#about">About</a></li>
  <li><a href="#reproduction">Reproduction</a></li>
  <li><a href="#resultate">Resultate</a></li>
  <li><a href="#schlussfolgerungen">Schlussfolgerungen</a></li>
  <li><a href="#quellen">Quellen</a></li>
</ol>
  
## About
Wir haben für unsere Semesterarbeit im Modul Applied Data Science ein Model entwickelt, um Landschaften zu klassifizieren. <br>
Dazu haben wir von Flickr Bilder von unterschiedlichen Lanschaften heruntergeladen und in [diesem Ordner](photos.zip) zur Verfügung gestellt. <br>
<br>
Wir haben uns dazu entschieden den Code über Google Colab anstatt einer lokalen Jupyter Instanz zu schreiben, weil wir dadurch die Möglichkeit haben ohne zusätzliche Kosten die GPU bzw. TPU von Google zu verwenden. So können wir unser Modell schneller trainieren als auf unseren eigenen Rechnern. <br>
Das Notebook ist unter https://colab.research.google.com/github/amkobee/ADS/blob/main/ADS.ipynb zu finden.<br>
<br>
Um unser Modell zu validieren, laden wir 5 zufällige Bilder von http://www.reddit.com/r/earthporn herunter und klassifizieren diese mit unserem Modell.


## Reproduction
Um unsere Resultate zu reproduzieren müssen vorab einige kleine Anpasssungen am Code gemacht werden

**FlickrAPI**<br>
Um die FlickrAPI zu nutzen, muss zuvor ein Account erstellt und die Anleitung auf https://www.flickr.com/services/apps/create/apply/ befolgt werden, um den public und secret key zu erhalten.<br>
Dazu müssen die folgenden zwei Variablen angepasst werden:

```python
FLICKR_PUBLIC = your_public_key
FLICKR_SECRET = your_secret_key
```

**Variable download_new_photos**<br>
Standardmässig werden keine neue Bilder heruntergeladen, weil es, je nach Anzahl Bilder, sehr lange dauern kann. Dazu kann die folgende Variable angepasst werden:

```python
# download new photos
download_new_photos = True
  
# don't download new photos
download_new_photos = False
```

## Resultate


## Schlussfolgerungen

**Limitierungen**<br>
Durch die Limitierung von GitHub, dass auf einer Repo maximal 100MB gespeichert werden können, haben wir uns entschlossen die Bilder nicht in voller Auflösung herunterzuladen. Dadurch können wir immerhin rund 5000 Bilder für unser Modell verwenden.<br>
Besteht der Bedarf nach mehr Bildern, können die Bilder lokal gespeichert und eingelesen werden.

**Datenqualität**<br>
Da auf Flickr jeder eigene Bilder hochladen und beschriften kann, kann das die Qualität negativ beeinflussen. Wir haben dem entgegengewirkt, indem wir zufällige Bilder heruntergeladen haben. So verringern wir die Wahrscheinlichkeit, dass Bilder vom gleichen User und der gleichen Landschaft mehrfach verwendet werden.

## Quellen
<li>Slides from Applied Data Science lectures></li>
<li>https://www.tensorflow.org/tutorials/images/classification</li>
<li>https://www.flickr.com/services/apps/create/apply</li>
<br><br><br><br><br>




Bilder von Flicker downloaden via API <br>
zB Suche nach Bergen, Wald, Fluss) <br>
Datenaufbereitung via Tensorflow / Keras <br>
CNN laufen lassen -> Klassifizierung <br>
Verwendung von Cloud Service via Google Collab <br>
Begründungen wieso was gemacht wurde oder wieso nicht eine Alternative zB in ein paar PP Folien

