# OruxMaps

Ce répertoire contient des notes et des ressources pour l'ajout de cartes IGN sur OruxMaps. Lisez attentivement jusqu'à la fin avant de commencer à apporter des modifications.

## Introduction

Pour ajouter des cartes IGN sur OruxMaps, il faut ajouter des entrées `<onlinemapsource>` au fichier `onlinemapsources.xml` à la racine du système Android. Cela est souvent problématique car il faut accéder des fichiers restreints dans son téléphone. Il est donc conseillé de le faire depuis un ordinateur avec le téléphone branché en mode de transfert de fichiers, où le système Android n'est pas capable d' empêcher l'accès à ces fichiers.

Le fichier `onlinemapsources.xml` se trouve sous `Android/data/com.orux.oruxmapsDonate/files/oruxmaps/mapfiles` dans les configurations du logiciel. Un fichier XML est un fichier text avec des entrées (*tags*) qui structurent les données de façon à les rendre facilement lisibles par un logiciel quelconque. Étant un ficher text, nous pouvons utiliser le *Bloc Notes* classique de Windows pour le lire et modifier. Pour ceux plus à l'aise avec le monde de la programmation, un éditeur de code avec coloration syntaxique est préférable, permetant facilement l'identification des erreurs.

La structure de `onlinemapsources.xml` est très simple: en haut nous avons un *en-tête* `<?xml version="1.0" encoding="utf-8"?>` qui indique au logiciel le lisant qu'il s'agit d'un fichier XML et quel encodage utiliser. Ensuite nous avons une entrée *racine* `onlinemapsources` qui englobe toutes les autres entrées sous forme d'une liste. Nous pouvons ajouter des commentaires au fichier en englobant un bloc de text avec `<!-- ... -->`, tel qu'utilisé dans l'exemple ci-dessous.


```xml
<?xml version="1.0" encoding="utf-8"?>
<onlinemapsources>

	<onlinemapsource uid="1">
		<name>Geoplateforme IGN SCAN25</name>
		<url><![CDATA[https://data.geopf.fr/private/wmts?Service=WMTS&apikey=ign_scan_ws&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN25TOUR&Style=normal&TileMatrixSet=PM&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={$z}&TileCol={$x}&TileRow={$y}]]></url>
		<website><![CDATA[<a href="https://www.ign.fr/geoplateforme" target="_blank">Géoplateforme IGN</a>]]></website>
		<minzoom>2</minzoom>
		<maxzoom>16</maxzoom>
		<projection>MERCATORESFERICA</projection>
		<servers></servers>
		<httpparam name="User-Agent">{om}</httpparam>
		<cacheable>1</cacheable>
		<downloadable>1</downloadable>
		<maxtilesday>0</maxtilesday>
		<maxthreads>0</maxthreads>
		<xop></xop>
		<yop></yop>
		<zop></zop>
		<qop></qop>
		<sop></sop>
	</onlinemapsource>

    <!-- autres entrées ici ... -->

</onlinemapsources>
```

Le plus important quand ajoutant des nouvelles entrées, ce'quel que ces cartes doivent avoir un identifiant (uid) différent chacune. La numérotation des `uid` est arbitraire (bonne pratique à suivre: utiliser une séquence de valeurs). Si vous le fusionnez avec un autre fichier, faire attention à adapter les `uid` au besoin, autrement OruxMaps ne pourrait pas les identifier et donc ne les afficherait pas.

## Tutoriel

1. Branchez votre téléphone Android à votre ordinateur en mode de partage de fichiers; identifiez le disque correspondant à votre appareil sous **Ce PC**:

![partage](media/step-01.png)

2. Naviguez jusquà `Android` en suivant l'exemple ci-dessous:

![partage](media/step-02.png)

3. Poursuivez la navigation dans le sous-dossier `data` pour arriver à `Android/data/com.orux.oruxmapsDonate/`

![partage](media/step-03.png)

4. Finalement, dans ce dossier naviguez vers `files/oruxmaps/mapfiles` où se trouve `onlinemapsources.xml`.

![partage](media/step-04.png)

5. Il n'est pas possible/conseillé de modifier ce fichier sur place; faites deux copies (`onlinemapsources.xml` et `onlinemapsources.xml.bak`) de ce fichier à un endroit de votre choix, souvent le Desktop. Éffacez le fichier `onlinemapsources.xml` présent dans le dossier `mapfiles` de votre téléphone.

6. Ouvrez `onlinemapsources.xml` avec un éditeur (clic droit, ouvrir avec..., choisir Bloc Notes si vous n'avez pas un editeur de code), reperez la ligne `<onlinemapsources>` et ajoutez les entrées de votre choix juste après cette ligne.

7. Vérifiez bien que toutes les entrées ont un `uid` différent de ceux déjà existants et que les tags sont correctement formés.

8. Sauvegardez `onlinemapsources.xml` et copiez-le dans le dossier `files/oruxmaps/mapfiles` du téléphone (veillez à bien avoir supprimé le fichier avan comme indiqué ci-dessus, coller par dessus ne marche pas ici).

9. Débranchez votre téléphone, relancez OruxMaps sur le téléphone (forcer l'arrêt et relancer). Ouvrez l'application et testez les nouvelles cartes.

Le fichier avec des entrées utiles se trouve [ici](onlinemapsources.xml); en général pour une pratique en montagne, les trois premières cartes sont suffisantes (IGN SCAN25, IGN Pentes, IGN Courbes de niveaux). Si vous voulez, vous pouvez remplacer votre `onlinemapsources.xml` par celui-ci directement (la majorité des entrées présentes sous le fichier fourni avec OruxMaps est inutile pour un usage en France).

## Références

- [Forum OruxMaps](https://oruxmaps.org/forum/index.php?topic=44755.0)
- [Tyber Randos](https://rando.tybern.fr/telechargements/CartesEnLigne/)
