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

## Resultate

### Version 1

In der ersten Version haben wir ein gewöhnliches CNN mit 10 Layern verwendet. Wir haben vorerst darauf verzichtet, weil wir eine Performance als Benchmark für weitere Versionen haben wollten.<br>
Das Modell performt zwar mit dem Trainingsset sehr gut, jedoch besteht ein markanter Unterschied zum Testset. Das deutet darauf hin, dass wir ein Overfitting im Modell haben.<br>
Dieses Overfitting wollen wir in der nächsten Version des Modells reduzieren.

#### Model Summary
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
rescaling (Rescaling)        (None, 180, 180, 3)       0         
_________________________________________________________________
conv2d (Conv2D)              (None, 180, 180, 16)      448       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 90, 90, 16)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 90, 90, 32)        4640      
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 45, 45, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 45, 45, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 22, 22, 64)        0         
_________________________________________________________________
flatten (Flatten)            (None, 30976)             0         
_________________________________________________________________
dense (Dense)                (None, 128)               3965056   
_________________________________________________________________
dense_1 (Dense)              (None, 5)                 645       
=================================================================
Total params: 3,989,285
Trainable params: 3,989,285
Non-trainable params: 0
_________________________________________________________________

```
![grafik](https://user-images.githubusercontent.com/72079017/120203757-570ecc00-c228-11eb-98c8-2dbf7ff0ab00.png)



### Version 2

In der zweiten Verion unseres Modells wollten wir das Overfitting der ersten Version reduzieren. Dazu haben wir Data Augmentation, Dropout und Regularization ins Modell eingeführt.<br>
Damit konnten wir zwar das Overfitting reduzieren, allerding leidet die Genauigkeit des Modells darunter.<br>
Wir möchten nun unser Modell verbessern indem wir weitere Layer hinzufügen.

#### Model Summary
```
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sequential_1 (Sequential)    (None, 180, 180, 3)       0         
_________________________________________________________________
rescaling_1 (Rescaling)      (None, 180, 180, 3)       0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 180, 180, 16)      448       
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 90, 90, 16)        0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 90, 90, 32)        4640      
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 45, 45, 32)        0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 45, 45, 64)        18496     
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 22, 22, 64)        0         
_________________________________________________________________
dropout (Dropout)            (None, 22, 22, 64)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 30976)             0         
_________________________________________________________________
dense_2 (Dense)              (None, 128)               3965056   
_________________________________________________________________
dense_3 (Dense)              (None, 5)                 645       
=================================================================
Total params: 3,989,285
Trainable params: 3,989,285
Non-trainable params: 0
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120203798-6130ca80-c228-11eb-9e7b-716b7c48e740.png)

### Version 3
In dieser Version haben wir weitere Layer hinzugefügt. <br>
Damit konnten wir die Performance marginal steigern. Wir möchten nun unser Modell mit einem State-of-the-Art Modell vergleichen, um einen Eindruck von der Performance zu erhalten.

#### Model Summary
```
Model: "sequential_8"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sequential_2 (Sequential)    (None, 180, 180, 3)       0         
_________________________________________________________________
rescaling_8 (Rescaling)      (None, 180, 180, 3)       0         
_________________________________________________________________
conv2d_30 (Conv2D)           (None, 180, 180, 16)      448       
_________________________________________________________________
max_pooling2d_25 (MaxPooling (None, 90, 90, 16)        0         
_________________________________________________________________
conv2d_31 (Conv2D)           (None, 90, 90, 16)        2320      
_________________________________________________________________
max_pooling2d_26 (MaxPooling (None, 45, 45, 16)        0         
_________________________________________________________________
dropout_13 (Dropout)         (None, 45, 45, 16)        0         
_________________________________________________________________
conv2d_32 (Conv2D)           (None, 45, 45, 32)        4640      
_________________________________________________________________
max_pooling2d_27 (MaxPooling (None, 22, 22, 32)        0         
_________________________________________________________________
dropout_14 (Dropout)         (None, 22, 22, 32)        0         
_________________________________________________________________
conv2d_33 (Conv2D)           (None, 22, 22, 32)        9248      
_________________________________________________________________
max_pooling2d_28 (MaxPooling (None, 11, 11, 32)        0         
_________________________________________________________________
conv2d_34 (Conv2D)           (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_29 (MaxPooling (None, 5, 5, 64)          0         
_________________________________________________________________
dropout_15 (Dropout)         (None, 5, 5, 64)          0         
_________________________________________________________________
flatten_7 (Flatten)          (None, 1600)              0         
_________________________________________________________________
dense_15 (Dense)             (None, 64)                102464    
_________________________________________________________________
dense_16 (Dense)             (None, 5)                 325       
=================================================================
Total params: 137,941
Trainable params: 137,941
Non-trainable params: 0
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120203938-8c1b1e80-c228-11eb-8352-9b500bbcb0d4.png)

### ResNet V2 50

Wir vergleichen unser Modell mit dem ResNet V2 50. Dieses erzielt sehr konstante Werte zwischen Training- und Testsets.<br>
Auch bezüglich der Genauigkeit übertrifft es unser Modell, allerdings ist zu beachten, dass unser Modell bloss 12 Layer verwendet, während ResNet in dieser Version 50 Layer verwendet und einzelne überspringt, um bessere Resultate zu erzielen.
#### Model Summary
```
Model: "sequential_4"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
keras_layer (KerasLayer)     (None, 2048)              23564800  
_________________________________________________________________
dropout_1 (Dropout)          (None, 2048)              0         
_________________________________________________________________
dense_4 (Dense)              (None, 5)                 10245     
=================================================================
Total params: 23,575,045
Trainable params: 10,245
Non-trainable params: 23,564,800
_________________________________________________________________
```
![grafik](https://user-images.githubusercontent.com/72079017/120203839-6c83f600-c228-11eb-8969-1092ebc55a90.png)
![grafik](https://user-images.githubusercontent.com/72079017/120203858-7279d700-c228-11eb-9b4e-fa53d0765691.png)



## Schlussfolgerungen

**Limitierungen**<br>
Durch die Limitierung von GitHub, dass auf einer Repo maximal 100MB gespeichert werden können, haben wir uns entschlossen die Bilder nicht in voller Auflösung herunterzuladen. Dadurch können wir immerhin rund 5000 Bilder für unser Modell verwenden.<br>
Besteht der Bedarf nach mehr Bildern, können die Bilder lokal gespeichert und eingelesen werden.

**Datenqualität**<br>
Da auf Flickr jeder eigene Bilder hochladen und beschriften kann, kann das die Qualität negativ beeinflussen. Wir haben dem entgegengewirkt, indem wir zufällige Bilder heruntergeladen haben. So verringern wir die Wahrscheinlichkeit, dass Bilder vom gleichen User und der gleichen Landschaft mehrfach verwendet werden.

## Quellen
<li>Vorlesungsunterlagen Applied Data Science</li>
<li>https://www.tensorflow.org/tutorials/images/classification</li>
<li>https://www.flickr.com/services/apps/create/apply</li>
[Tensorflow Tutorial](https://www.tensorflow.org/tutorials/images/classification){:target="_blank"}
<br><br><br><br><br>




Bilder von Flicker downloaden via API <br>
zB Suche nach Bergen, Wald, Fluss) <br>
Datenaufbereitung via Tensorflow / Keras <br>
CNN laufen lassen -> Klassifizierung <br>
Verwendung von Cloud Service via Google Collab <br>
Begründungen wieso was gemacht wurde oder wieso nicht eine Alternative zB in ein paar PP Folien

