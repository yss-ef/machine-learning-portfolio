# Modèle de Régression Linéaire par Méthode Matricielle

Ce projet a été réalisé dans le cadre du module d'Analyse des Données Multidimensionnelles. Il contient un script Python permettant de calculer les coefficients d'un modèle de régression linéaire simple ($Y = aX + b$) à partir de données fournies dans un fichier Excel.

L'approche utilisée est la méthode des moindres carrés via l'équation normale, qui s'appuie sur des opérations d'algèbre linéaire (matrices).

---

### Fonctionnalités 

* **Lecture de données** depuis un fichier Excel (`.xlsx`).
* **Calcul automatique** des coefficients de la régression : la pente `a` et l'ordonnée à l'origine `b`.
* **Implémentation pure** de la formule matricielle sans utiliser de bibliothèques de machine learning comme Scikit-learn.
* **Affichage clair** du modèle de régression final.

---

### Prérequis 

Pour exécuter ce script, vous devez avoir Python installé sur votre machine, ainsi que les deux bibliothèques suivantes :

* **Pandas** : Pour la lecture et la manipulation des données du fichier Excel.
* **NumPy** : Pour les calculs numériques et matriciels.

Vous pouvez les installer avec la commande suivante :
```bash
pip install pandas numpy openpyxl
```
---

Comment l'utiliser 
1. Préparez votre fichier de données :

    * Créez un fichier Excel (par exemple, donnees.xlsx).

    * La première colonne doit contenir vos données pour la variable dépendante (Y).

    * La deuxième colonne doit contenir vos données pour la variable indépendante (X).

    * Le fichier ne doit pas contenir d'en-têtes.

2. Modifiez le nom du fichier dans le script :

    * Ouvrez le fichier de script Python.

    * À la fin du fichier, modifiez la ligne chemin_fichier = 'donnees_projet.xlsx' pour indiquer le nom de votre propre fichier Excel.

3. Exécutez le script :

    * Ouvrez un terminal dans le dossier du projet et lancez la commande suivante :
   ```bash
   python ModRegression-1.py
   ```
   
4. Consultez les résultats :
   * Le script affichera la pente (a) et l'ordonnée à l'origine (b) calculées, ainsi que l'équation finale de votre modèle de régression.
   
---

### Explication de la Méthode 

Le calcul est basé sur l'**équation normale**, qui fournit une solution analytique au problème des moindres carrés. La formule est la suivante :

$$\hat{\beta} = (X^T X)^{-1} X^T Y$$

Où :
* $\hat{\beta}$ est le vecteur contenant les coefficients `b` et `a`.
* $Y$ est le vecteur des valeurs de la variable dépendante.
* $X$ est la **matrice de design**, composée d'une colonne de `1` (pour l'intercept) et d'une colonne avec les valeurs de la variable indépendante.


