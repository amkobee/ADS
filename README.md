# ADS - Landscape Classifier

## Inhaltsverzeichnis
<ol>
  <li><a href="#about">About</a></li>
  <li><a href="#reproduction">Reproduction</a></li>
  <li><a href="#beispielbilder">Beispielbilder</a></li>
  <li><a href="#resultate">Resultate</a></li>
  <li><a href="#schlussfolgerungen">Schlussfolgerungen</a></li>
  <li><a href="#quellen">Quellen</a></li>
</ol>
  
## About
Wir haben für unsere Semesterarbeit im Modul Applied Data Science ein Modell entwickelt, um Landschaften zu klassifizieren. <br>
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
## Beispielbilder
![overview](https://user-images.githubusercontent.com/72079017/120895030-8011d100-c61b-11eb-9f3b-55d2e43f848e.png)

### Data Augmentation
![grafik](https://user-images.githubusercontent.com/72079017/120895090-bc453180-c61b-11eb-8cc1-fe5436746b7d.png)



## Resultate
Wir haben uns entschieden unser Notebook so zu organisieren, dass alle Anpassungen, die am Modell vorgenommen wurden in einem neuen Abschnitt aufgeführt werden. <br>
Damit wollen wir sehen, wie sich unser Modell entwickelt und wie es im Vergleich zum Vorgänger performt.

### Version 1
Das Resultat des ersten Modells ist einigermassen akzeptabel. Die Genauigkeit des Trainingset ist mit knapp 95% extrem hoch, wobei die des Validationset nur bei rund 50% liegt. Das ist ein klares Anzeichen für Overfitting, was wir in der nächsten Iteration mit Hilfe von Dropout, Regularization und Data Augmentation verringern wollen.

#### Model Summary
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
rescaling_20 (Rescaling)     (None, 180, 180, 3)       0         
_________________________________________________________________
conv2d_111 (Conv2D)          (None, 180, 180, 16)      448       
_________________________________________________________________
max_pooling2d_111 (MaxPoolin (None, 90, 90, 16)        0         
_________________________________________________________________
conv2d_112 (Conv2D)          (None, 90, 90, 32)        4640      
_________________________________________________________________
max_pooling2d_112 (MaxPoolin (None, 45, 45, 32)        0         
_________________________________________________________________
conv2d_113 (Conv2D)          (None, 45, 45, 64)        18496     
_________________________________________________________________
max_pooling2d_113 (MaxPoolin (None, 22, 22, 64)        0         
_________________________________________________________________
flatten_20 (Flatten)         (None, 30976)             0         
_________________________________________________________________
dense_43 (Dense)             (None, 128)               3965056   
_________________________________________________________________
dense_44 (Dense)             (None, 5)                 645       
=================================================================
Total params: 3,989,285
Trainable params: 3,989,285
Non-trainable params: 0
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120895045-8e5fed00-c61b-11eb-9893-77c3406b8da5.png)




### Version 2
Wir waren in der Lage das Overfitting sehr zu reduzieren. Weiter konnten wir die Genauigkeit marginal erhöhen, sind damit aber noch nicht ganz zufrieden.<br>
In der nächsten Iteratino wollen wir durch da Hinzufügen von weiteren Layern die Genauigkeit erhöhen.

#### Model Summary
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sequential_31 (Sequential)   (None, 180, 180, 3)       0         
_________________________________________________________________
rescaling_21 (Rescaling)     (None, 180, 180, 3)       0         
_________________________________________________________________
conv2d_114 (Conv2D)          (None, 180, 180, 16)      448       
_________________________________________________________________
max_pooling2d_114 (MaxPoolin (None, 90, 90, 16)        0         
_________________________________________________________________
conv2d_115 (Conv2D)          (None, 90, 90, 32)        4640      
_________________________________________________________________
max_pooling2d_115 (MaxPoolin (None, 45, 45, 32)        0         
_________________________________________________________________
conv2d_116 (Conv2D)          (None, 45, 45, 64)        18496     
_________________________________________________________________
max_pooling2d_116 (MaxPoolin (None, 22, 22, 64)        0         
_________________________________________________________________
dropout_37 (Dropout)         (None, 22, 22, 64)        0         
_________________________________________________________________
flatten_21 (Flatten)         (None, 30976)             0         
_________________________________________________________________
dense_45 (Dense)             (None, 128)               3965056   
_________________________________________________________________
dense_46 (Dense)             (None, 5)                 645       
=================================================================
Total params: 3,989,285
Trainable params: 3,989,285
Non-trainable params: 0
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120895056-9750be80-c61b-11eb-9b83-b482a5c88d0f.png)


### Version 3
Wir konnten die Genauigkeit mit mehr Layern nicht signifikant erhöhen. Um unser Modell weiter zu verbessern, müssten wir ein Recurrent Neural Network aufbauen.<br>
Deshalb verwenden wir in der nächsten Iteration ResNet V2 50 um es mit unseren Daten zu trainieren.<br>
Anschliessend möchten wir unser Modell mit einem State-of-the-Art Modell vergleichen.

#### Model Summary
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sequential_31 (Sequential)   (None, 180, 180, 3)       0         
_________________________________________________________________
rescaling_22 (Rescaling)     (None, 180, 180, 3)       0         
_________________________________________________________________
conv2d_117 (Conv2D)          (None, 180, 180, 16)      448       
_________________________________________________________________
max_pooling2d_117 (MaxPoolin (None, 90, 90, 16)        0         
_________________________________________________________________
conv2d_118 (Conv2D)          (None, 90, 90, 16)        2320      
_________________________________________________________________
max_pooling2d_118 (MaxPoolin (None, 45, 45, 16)        0         
_________________________________________________________________
conv2d_119 (Conv2D)          (None, 45, 45, 16)        2320      
_________________________________________________________________
max_pooling2d_119 (MaxPoolin (None, 22, 22, 16)        0         
_________________________________________________________________
conv2d_120 (Conv2D)          (None, 22, 22, 16)        2320      
_________________________________________________________________
max_pooling2d_120 (MaxPoolin (None, 11, 11, 16)        0         
_________________________________________________________________
dropout_38 (Dropout)         (None, 11, 11, 16)        0         
_________________________________________________________________
conv2d_121 (Conv2D)          (None, 11, 11, 32)        4640      
_________________________________________________________________
max_pooling2d_121 (MaxPoolin (None, 5, 5, 32)          0         
_________________________________________________________________
dropout_39 (Dropout)         (None, 5, 5, 32)          0         
_________________________________________________________________
conv2d_122 (Conv2D)          (None, 5, 5, 32)          9248      
_________________________________________________________________
max_pooling2d_122 (MaxPoolin (None, 2, 2, 32)          0         
_________________________________________________________________
conv2d_123 (Conv2D)          (None, 2, 2, 64)          18496     
_________________________________________________________________
max_pooling2d_123 (MaxPoolin (None, 1, 1, 64)          0         
_________________________________________________________________
flatten_22 (Flatten)         (None, 64)                0         
_________________________________________________________________
dense_47 (Dense)             (None, 64)                4160      
_________________________________________________________________
dense_48 (Dense)             (None, 5)                 325       
=================================================================
Total params: 44,277
Trainable params: 44,277
Non-trainable params: 0
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120895066-a8013480-c61b-11eb-854a-dde3938efdf4.png)


### ResNet V2 50
Das ResNet V2 50 erzielt eine 10-15% höhere Genauigkeit als unser Modell. Dieses Resultat haben wir auch durch die höhere Komplexität des Modells erwartet. <br>
In der nächsten Iteration wollen wir noch das gesamte ResNet V2 mit allen 152 Layern prüfen.
The ResNet V2 50 model outperforms our model by approx. 10-15% in accuracy.
#### Model Summary
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
keras_layer_4 (KerasLayer)   (None, 2048)              23564800  
_________________________________________________________________
dropout_41 (Dropout)         (None, 2048)              0         
_________________________________________________________________
dense_50 (Dense)             (None, 5)                 10245     
=================================================================
Total params: 23,575,045
Trainable params: 10,245
Non-trainable params: 23,564,800
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120895165-03cbbd80-c61c-11eb-947d-252052ced354.png)


### ResNet V2 152
Das ResNet V2 152 performt ähnlich wie die Variante mit bloss 50 Layern.<br>
Wir vermuten, dass das Modell mit 152 Layern ein Problem mit der geringen Anzahl Daten hat. Es bräuchte wohl mindestens 10000 Bilder statt bloss rund 6000.<br>
Wir empfehlen deshalb das ganze Modell mit einer lokalen GPU zu trainieren, weil es da auch kein Problem gibt mit Speicherbegrenzungen.


#### Model Summary
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
keras_layer_5 (KerasLayer)   (None, 2048)              58331648  
_________________________________________________________________
dropout_42 (Dropout)         (None, 2048)              0         
_________________________________________________________________
dense_51 (Dense)             (None, 5)                 10245     
=================================================================
Total params: 58,341,893
Trainable params: 10,245
Non-trainable params: 58,331,648
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120895715-8b1a3080-c61e-11eb-92b8-7dc82ee4132e.png)


## Schlussfolgerungen

**Limitierungen**<br>
Durch die Limitierung von GitHub, dass auf einer Repo maximal 100MB gespeichert werden können, haben wir uns entschlossen die Bilder nicht in voller Auflösung herunterzuladen. Dadurch können wir immerhin rund 5000 Bilder für unser Modell verwenden.<br>
Besteht der Bedarf nach mehr Bildern, können die Bilder lokal gespeichert und eingelesen werden.

**Datenqualität**<br>
Da auf Flickr jeder eigene Bilder hochladen und beschriften kann, kann das die Qualität negativ beeinflussen. Wir haben dem entgegengewirkt, indem wir zufällige Bilder heruntergeladen haben. So verringern wir die Wahrscheinlichkeit, dass Bilder vom gleichen User und der gleichen Landschaft mehrfach verwendet werden.<br>
Weiter ordnen Menschen die gleichen Bilder unterschiedlich ein. Ein Fluss, der durch einen Wald verläuft, kann schliesslich als beides klassifiziert werden. Sind noch Berge zu sehen, kommt eine Klasse dazu.

## Quellen
<li>Vorlesungsunterlagen Applied Data Science</li>
<li>https://www.tensorflow.org/tutorials/images/classification</li>
<li>https://www.flickr.com/services/apps/create/apply</li>
