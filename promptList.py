search_query_generator = """
# MISSION
You are a search query generator for student in terminal class. You will be given a specific query or problem by the USER and you are to generate a JSON list of at most 5 questions that will be used to search the internet. Make sure you generate comprehensive search queries that will help the student fully understand all around the question he ask and query must be usable for the domains. Employ everything you know about information foraging and information literacy to generate the best possible questions,.
If the specific query is not a question that need search don't output this :
{
"search":"OUI"
}

# REFINE QUERIES
You might be given a first-pass information need, in which case you will do the best you can to generate "naive queries" (uninformed search queries). However the USER might also give you previous search queries or other background information such as accumulated notes. If these materials are present, you are to generate "informed queries" - more specific search queries that aim to zero in on the correct information domain. Do not duplicate previously asked questions. Use the notes and other information presented to create targeted queries and/or to cast a wider net.

# OUTPUT FORMAT
In all cases, your output must be a simple JSON list of strings.  Always write in french.
OUTPUT EXEMPLE
{
"search1":"search query",
"search2":"search query"
...
}
"""

hypothesis_generator = """
# MISSION
You are an information needs hypothesis generator. 
You will be given a main information need or user query as well as a variety of materials, such as search results, previous hypotheses, and notes. 
Whatever information you receive, your output should be a revised, refined, or improved hypothesis. 
In this case, the hypothesis is a comprehensive answer to the user query or information need. To the best of your ability. Do not include citations in your hypothesis, as this will all be record via out-of-band processes (e.g. the information that you are shown will have metadata and cataloging working behind the scenes that you do not see). Even so, you should endeavour to write everything in complete, comprehensive sentences and paragraphs such that your hypothesis requires little to no outside context to understand. 
Your hypothesis must be relevant to the USER QUERY or INFORMATION NEED.
Always write in french.
Ask if the user understand and, ask him question to test if he understand.
"""

exercice_facile = """
Créez un exercice facile et clair comprenant deux questions simples en respectant le programme donné. Assurez-vous de ne pas inclure des concepts qui ne sont pas abordés dans le programme. Voici le format que vous devez suivre :

Exemple format output : 
#Exercice Facile :

Ici tu écris l'énoncé de l'exercice
1. Question 1 :
   - Instructions pour répondre à la question 1.

2. Question 2 :
   - Instructions pour répondre à la question 2.

Veillez à fournir uniquement les informations nécessaires sans ajouter d'informations supplémentaires.
"""

exercice_moyen = """
Créez un exercice moyennement difficile comprenant quatres questions en respectant le programme donné. Assurez-vous de ne pas inclure des concepts qui ne sont pas abordés dans le programme. Voici le format que vous devez suivre :

Exemple format output
#Exercice Facile :
Enoncé de l'exercice (exemple X=12 et V ....)

1. Question 1 :
   - Instructions pour répondre à la question 1.

2. Question 2 :
   - Instructions pour répondre à la question 2.

3. Question 3 :
   - Instructions pour répondre à la question 3.

4. Question 4 :
   - Instructions pour répondre à la question 4.

Veillez à fournir uniquement les informations nécessaires sans ajouter d'informations supplémentaires.

"""

exercice_difficile = """
Créez un problèmes difficile pour tester les connaissances de l'élèves comprenant six questions en respectant le programme donné. Assurez-vous de ne pas inclure des concepts qui ne sont pas abordés dans le programme. Voici le format que vous devez suivre :
Exemple format ouput
#Exercice Facile :
Enoncé de l'exercice (exemple il y a un tableau et ....)

1. Question 1 :
   - Instructions pour répondre à la question 1.

2. Question 2 :
   - Instructions pour répondre à la question 2.

3. Question 3 :
   - Instructions pour répondre à la question 3.

4. Question 4 :
   - Instructions pour répondre à la question 4.

5. Question 5 :
   - Instructions pour répondre à la question 5.

6. Question 6 :
   - Instructions pour répondre à la question 6.

Veillez à fournir uniquement les informations nécessaires sans ajouter d'informations supplémentaires.

"""
exoFormat = """
    Repond toujours en français.
    Un exercice te sera fourni avec les résultats, ta tâche sera d'explication sans faire les calculer juste d'expliquer étape par étape les calculs à faire et de donner des conseils sur comment bien faire, puis à la fin de chaque question donne le resultat final fourni.
    Voici un exemple :
    Exercice
    Soit X une variable aléatoire suivant une loi binomiale B(n, p) avec n = 5 et p = 0.4.

    1. Calculer la probabilité que X prenne la valeur 3.
    2. Calculer l'espérance mathématique de X.
    3. Calculer la variance de X.

    Resultat : 
    1. La probabilité que la variable aléatoire X prenne la valeur 3 est \( 0.2304 \) ou \( 23.04\% \).

2. L'espérance mathématique de X est \( 2.0 \).

3. La variance de X est \( 1.2 \).
    Solution         
    # Exercice sur la Loi Binomiale

    Soit `X` une variable aléatoire suivant une loi binomiale `B(n, p)` avec `n = 5` et `p = 0.4`.

    ## 1. Calculer la Probabilité que X Prende la Valeur 3

    - **Étape 1** : Calculer le coefficient binomial `(5 choose 3)`.
    - **Explication** : Ce coefficient représente le nombre de façons de choisir 3 succès parmi 5 épreuves.
    - **Étape 2** : Calculer `p^3`, c'est-à-dire `0.4^3`.
    - **Explication** : Cela représente la probabilité d'obtenir exactement 3 succès.
    - **Étape 3** : Calculer `(1 - p)^(n - 3)`, soit `(1 - 0.4)^(5 - 3)`.
    - **Explication** : Cela représente la probabilité d'obtenir 2 échecs (puisque n - 3 = 2 dans ce cas).
    - **Étape 4** : Multiplier les résultats des étapes 1, 2 et 3 pour obtenir `P(X = 3)`.
    - **Explication** : La multiplication de ces trois valeurs donne la probabilité totale d'avoir exactement 3 succès en 5 essais.
    ** Resultat final : \( 0.2304 \) ou \( 23.04\% \)

    ## 2. Calculer l'Espérance Mathématique de X

    - **Étape unique** : Multiplier `n` par `p`, soit `5 * 0.4` pour obtenir `E(X)`.
    - **Explication** : L'espérance mathématique est la moyenne pondérée des succès possibles. Ici, c'est le nombre moyen de succès attendus.
    ** Resultat final : \( 2.0 \)

    ## 3. Calculer la Variance de X

    - **Étape 1** : Calculer `n * p`, soit `5 * 0.4`.
    - **Explication** : Cela donne l'espérance mathématique de `X`.
    - **Étape 2** : Calculer `1 - p`, soit `1 - 0.4`.
    - **Explication** : Cela représente la probabilité d'un échec.
    - **Étape 3** : Multiplier les résultats des étapes 1 et 2 pour obtenir `Var(X)`.
    - **Explication** : La variance est calculée en multipliant l'espérance mathématique de `X` par la probabilité d'un échec, ce qui donne une mesure de la dispersion des valeurs de `X`.
    ** Resultat final : \( 1.2 \).
    """

def SystemUserAnswer(userInfo):
    system="""
    Tu es un assistant, tu te nomme LND-Assistant, ta tâche est d'être serviable pour l'utilisateur.
    Refere toi à l'utilisateur par son nom si on te le fourni et tu dois savoir que l'utilisateur est un élève de BAC au Mali.
    Voici d'autre information sur l'utilisateur:
    """ + userInfo

    return system

savoir_savoirFaire_Arithmetique ="""
Voici le programme pour l'arithmetique sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :


# Mathématiques: Arithmétique

## 1. DIVISIBILITÉ DANS ℤ

### SAVOIRS
- Multiples d’un entier relatif.

### SAVOIR-FAIRE
- Démontrer qu’un entier est divisible par un entier donné.
- Notation n ℤ.
- Diviseurs d’un entier relatif.
- Déterminer l’ensemble des diviseurs d’un entier naturel non nul.

## 2. DIVISION EUCLIDIENNE

### SAVOIRS
- Division euclidienne dans ℕ.

### SAVOIR-FAIRE
- Déterminer le quotient et le reste de la division euclidienne d’un entier relatif par un entier naturel non nul.
- Division euclidienne dans ℤ.

## 3. CONGRUENCE MODULO n

### SAVOIRS
- Définition.
- Propriété de conformité avec les opérations.

### SAVOIR-FAIRE
- Utiliser les propriétés des congruences pour résoudre des problèmes de divisibilités.

## 4. NOMBRES PREMIERS

### SAVOIRS & SAVOIR-FAIRE
- Définition.
- L’ensemble des nombres premiers est infini.
- Décomposition d’un entier naturel en produit de facteurs premiers.
- Démontrer qu’un nombre est premier.
- Déterminer l’ensemble des diviseurs d’un entier naturel non nul.
- Décomposer un entier en produit de facteurs premiers.

## 5. PGCD, PPCM

### SAVOIRS & SAVOIR-FAIRE
- Définition et propriétés.
- Algorithme d’Euclide.
- Nombres premiers entre eux.
- Théorème de Bézout.
- Théorème de Gauss.
- Déterminer le PGCD de deux nombres :
  - à l’aide de l’algorithme d’Euclide ;
  - à l’aide de la décomposition en produit de facteurs premiers.
- Déterminer le PPCM de deux nombres :
  - à l’aide de la décomposition en produit de facteurs premiers ;
  - à l’aide du PGCD.
- Utiliser le théorème de Bézout pour démontrer que des entiers sont premiers entre eux.
- Utiliser le théorème de Gauss pour résoudre des problèmes d’arithmétique.
"""

savoir_savoirFaire_Barycentres= """
Voici le programme pour les Barycentres sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :

section*SAVOIRS
Barycentre de n points pondérés
Réduction de : $sum_{i=1}^{n} alpha_i M_i$
Réduction de : $sum_{i=1}^{n} alpha_i MA_i^2$
Ligne de niveau de l'application : $M mapsto text{Mes} (M'A; MB)$
  définition
  Propriétés
  end{itemize}

SAVOIR-FAIRE
Réduire $sum_{i=1}^{n} alpha_i M_i$
Réduire $sum_{i=1}^{n} alpha_i MA_i^2$
Déterminer les lignes et surfaces de niveaux des applications du type : $M mapsto sum_{i=1}^{n} alpha_i MA_i^2$
Construire dans le plan les lignes de niveau de l'application : $M mapsto sum_{i=1}^{n} alpha_i MA_i^2$
Déterminer et construire une ligne de niveau de l'application : $M mapsto text{Mes} (M'A; MB)$
"""

savoir_savoirFaire_Conique = """
Voici le programme pour les Coniques sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :

# SAVOIRS

- **Définition géométrique**:
  - Définition par foyer et directrice.
  - Vocabulaire : foyers, directrices, excentricité, sommets, axe focal.
  - Définition bifocale de l’ellipse et de l’hyperbole.

# SAVOIR-FAIRE

- Déterminer l’équation réduite d’une conique.
- **Équations cartésiennes**:
  - Équations réduites d’une parabole, d’une ellipse et d’une hyperbole.
  - Éléments remarquables : paramètre, sommets, axe focal, foyers, directrices, asymptotes, demi-distance focale.
- Représentation graphique des coniques.
- Conique détermination:
  - À l’aide de la définition par foyer et directrice.
  - À l’aide de la définition bifocale.
  - Par un changement de repère (l’équation étant de la forme \( ax^2 + by^2 + cx + dy + e = 0 \)).
- Connaissant l’équation réduite d’une conique, déterminer ses éléments remarquables.
- Représenter graphiquement une conique à l’aide de ses éléments remarquables.
"""

savoir_savoirFaire_Dénombrement_Probabilité_VariableAléatiure_LoiNinomiale_EpreuveDeBernoullie ="""
Voici le programme pour les Dénombrement Probabilité Variable Aléatiure Loi Binomiale Epreuve De Bernoullie sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :


#PROABILITES

## SAVOIRS
- Vocabulaire.

## SAVOIR-FAIRE
- Dénombrer, dans le cas d'une équiprobabilité.
- Définition d'une probabilité dans le cas d'une expérience conduisant à un nombre fini d'éventualités :
  - Les cas possibles d'une expérience.
  - Les cas favorables d'un événement.
- Calculer la probabilité d'un événement.
- Démontrer que deux événements sont indépendants.
- Evénements indépendants :
  - Définition.
  - Propriétés.

# 2. VARIABLES ALEATOIRES

## SAVOIRS
- Définition.
- Loi de probabilité.
- Fonction de répartition.
- Espérance mathématique.
- Variance ; écart type.

## SAVOIR-FAIRE
- Une variable aléatoire étant donnée :
  - Déterminer sa loi de probabilité et sa fonction de répartition.
  - Construire sa fonction de répartition.
  - Calculer son espérance mathématique.
  - Calculer sa variance et son écart type.

# 3. LOI BINOMIALE

## SAVOIRS
- Probabilité d’obtenir k succès dans une suite de n épreuves Bernoulli.
- \( E(X) = np \).
- \( V(X) = np(1-p) \).

## SAVOIR-FAIRE
- Calculer la probabilité d’obtenir k succès dans une suite de n épreuves de Bernoulli (\(0 \leq k \leq n\)).

"""

savoir_savoirFaire_Equations_différentielle = """
Voici le programme pour les équation différentielle sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :


# SAVOIRS

- Équation différentielle du type \( y' = \ldots \)

# SAVOIR-FAIRE

- Résoudre une équation différentielle du type \( y' = \ldots \)
- Équation différentielle du type \( y''= 0 \)
- Équation différentielle du type \( y'' = \ldots \)
- Équation différentielle du type \( y'' = 0 \)
- Équation différentielle du type \( y''= \ldots \)

"""

savoir_savoirFaire_Fonctions_exponentielle = """
Voici le programme pour les fonctions exponentielle sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :


# SAVOIR

## Fonction exponentielle népérienne :
- Définitions, notation, propriétés, représentation graphique.
- Limite de référence.
- Primitive de \( u e^u \).
- Définition de la fonction exponentielle de base \( a \) (\( a \in \mathbb\{R\}_+^* \)):
  - Définition de la fonction puissance d'exposant réel non nul.
- Primitive de \( u' x^n \) (\( n \in \mathbb\{R\} \setminus \{-1\} \)).
- Croissance comparée des fonctions logarithme népérien, exponentielle et puissances.
- Dérivées de fonctions du type expo, \( u^a \) (\( a \in \mathbb{R}^* \)).

# SAVOIR-FAIRE

- Étant donnée une fonction faisant intervenir la fonction exponentielle népérienne ou une fonction puissance, l'étudier et la représenter graphiquement.
- Résoudre des équations ou inéquations faisant intervenir des fonctions exponentielles.
- Déterminer les primitives d’une fonction du type :
  - \( u' x^n \) (\( n \in \mathbb{R} \setminus \{-1\} \)).
  - \( u' e^u \).
- Utiliser les limites sur la croissance comparée pour calculer d’autres limites.

"""

savoir_savoirFaire_Fonction_Logarithmes_Neperiens = """
Voici le programme pour les fonctions logarithmes neperiens sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :


# Savoirs et savoir-faire

## SAVOIR

### Fonction logarithme népérien :
- Définition, notation, propriétés, représentation graphique.
- Limite de référence.
- Primitives de \( \\frac{u'}{u} \).

### Logarithme décimal :
- Définition.
- Dérivée des fonctions du type \( \ln(\lvert u \rvert) \) et \( \log(\lvert u \rvert) \).

## SAVOIR-FAIRE

- Résoudre des équations ou inéquations faisant intervenir la fonction logarithme népérien.
- Déterminer les primitives d'une fonction du type \( \frac{u'}{u} \).
- Étant donnée une fonction \( f \) faisant intervenir la fonction logarithme népérien :
  - Trouver les limites de \( f \) aux bornes de son ensemble de définition.
  - Étudier les variations de \( f \).
  - Représenter graphiquement \( f \).

"""

savoir_savoirFaire_Fonction_numérique_dune_variable_reelle = """
Voici le programme pour les numérique d'une variable réelle sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :


# Savoirs

- Limites :
  - Limite d'une fonction composée.
  - Limite d'une fonction monotone sur un intervalle ouvert.

- Branches paraboliques de direction (OI) et (OJ) dans un repère (O, I, J).

- Continuité sur un intervalle :
  - Opérations, composée (propriétés admises).
  - Image d'un intervalle.

- Fonction continue et strictement monotone sur un intervalle :
  - Théorème 1 : si f est une fonction continue et strictement monotone sur un intervalle I, alors f est une bijection de I sur f(I). Sa bijection réciproque f^{-1} est continue et de même sens de variation que la fonction f.
  - Théorème 2 : si f est une fonction continue et strictement monotone sur un intervalle I, alors pour tout m appartenant à f(I), l'équation f(x) = m admet une unique solution dans I.

- Corollaire : soit f une fonction continue et strictement monotone sur [a, b]. Si f(a) et f(b) sont des signes contraires, alors l'équation f(x) = 0 admet une unique solution dans l'intervalle ouvert ]a, b[.

- Fonctions du type :
  - x ↦ √x, (né IR*)
  - x ↦ x^r (r ∈ Q, x ∈ IR*+).

- Définitions ; notions p/q
- Propriétés des puissances d'exposants rationnels

# Savoir-faire

- Déterminer la limite d'une fonction :
  - en utilisant les limites de référence ou une expression conjuguée ;
  - en ayant recours à la définition d’un nombre dérivé.

- Déterminer la limite d’une fonction composée.

- Interpréter graphiquement :
  - lim (f(x)/x) quand x tend vers +∞ = 0, lim (f(x)/x) quand x tend vers -∞ = +∞ (resp. –∞)
  - lim (f(x)/x) quand x tend vers -∞ = 0 et lim (f(x)/x) quand x tend vers +∞ = +∞ (resp. –∞)

- Démontrer qu’une courbe admet une branche parabolique de direction (OI) (resp. (OJ))

- Déterminer l'image d’un intervalle par une fonction continue :
  - en utilisant le tableau de variations ;
  - en utilisant une méthode algébrique.

- Démontrer qu’une fonction réalise une bijection d’un intervalle I sur un intervalle J dans le cas où f est une fonction continue, déterminer f^{-1}(x).

- Prouver l’existence d’une unique solution de l’équation : f(x) = m sur un intervalle I.

"""

savoir_savoirFaire_Nombre_Complexe = """

Voici le programme pour les nombres complexes sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :

# 1) ENSEMBLE DES NOMBRES COMPLEXES

## SAVOIRS
- Forme algébrique d’un nombre complexe.
- Partie réelle (Re), partie imaginaire (Im).
- Conjugué d’un nombre complexe, propriétés.
- Somme, produit, quotient de deux nombres complexes.
- Formule du binôme.
- Égalité de deux nombres complexes.

## SAVOIR-FAIRE
- Déterminer la partie réelle, la partie imaginaire d’un nombre complexe.
- Calculer la somme, le produit et le quotient de deux nombres complexes donnés sous forme algébrique.
- Développer \( (a + bi)^n \).
- Déterminer le conjugué d’un nombre complexe.
- Module et argument d’un nombre complexe.
- Module et argument du produit, de l’inverse, du quotient et de la puissance entière d’un nombre complexe.
- Forme trigonométrique.
- Affixe d’un point, d’un vecteur.
- Point image et vecteur image d’un nombre complexe.
- Forme exponentielle \( z = re^{i\\theta} \).
- Déterminer le module et un argument d’un nombre complexe non nul donnés sous forme algébrique.
- Représenter graphiquement un nombre complexe donné sous forme algébrique.
- Calculer le produit et le quotient de deux nombres complexes écrits sous formes trigonométrique.
- Passer de la forme trigonométrique à la forme algébrique et inversement.

# 2) NOMBRES COMPLEXES ET TRIGONOMÉTRIE

## SAVOIR
- Formule de Moivre, formule d’Euler.

## SAVOIR-FAIRE
- Utiliser les formules de Moivre et d’Euler pour retrouver des formules trigonométriques.
- Linéariser des puissances de cos et sin à l’aide des nombres complexes.

# 3) ÉQUATIONS DANS ℂ

## SAVOIR
- Racines carrées d’un nombre complexe non nul.
- Équation du second degré dans ℂ.
- Racine \( n^{ème} \) d’un nombre complexe non nul.
- Racine \( n^{ème} \) de l’unité ; interprétation graphique.

## SAVOIR-FAIRE
- Déterminer les racines carrées d’un nombre complexe écrit sous forme algébrique.
- Résoudre une équation du second degré dans ℂ ou une équation s’y ramenant.
- Déterminer sous forme trigonométrique les racines \( n^{ème} \) d’un nombre complexe et les représenter graphiquement.

# 4) NOMBRES COMPLEXES ET GÉOMÉTRIE

## SAVOIR
- L'argument \( \\text{arg} \left( \\frac{z_2 - z_1}{z_3 - z_1} \\right) \) est une mesure de l'angle \( \\vec{AB} \wedge \\vec{AC} \).

## SAVOIR-FAIRE
- Caractérisations complexes d’un cercle, d’une droite.
- Déterminer que des points sont cocycliques.
- Démontrer que des points sont alignés.
- Utiliser les caractérisations complexes pour justifier une propriété géométrique.
- Déterminer des lieux géométriques.

"""

savoir_savoirFaire_primitive_intégrale_calculs_daires = """
Voici le programme pour les primitive intégrale calculs d'aires sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :

# Savoirs et savoir-faire

## SAVOIR

- Définition d’une primitive.
- Existence de primitives d’une fonction continue sur un intervalle (admis).
- Ensemble des primitives d’une fonction continue.
- Unicité de la primitive d’une fonction prenant une valeur donnée en un point donné.
- Primitives des fonctions de référence.
- Primitive de \( u + v \), \( \lambda u \) (\( \lambda \in \mathbb{/R} \)), \( u'v \) et \( u'v' \) (\( n \\neq -1 \)).

## SAVOIR-FAIRE

- Déterminer les primitives d’une fonction en utilisant les primitives des fonctions de référence.
- Déterminer la primitive d’une fonction qui prend une valeur donnée en un point donné.
- Déterminer les primitives d’une fonction du type :
  - \( \\alpha u + \\beta v \), (\( \\alpha, \\beta \in \mathbb{R}^2 \));
  - \( v' \\times (u' \\text{ ou } v) \);
  - \( u'v'' \) (\( n \\neq -1 \)).
"""

savoir_savoirFaire_Suite_Numerique = """
Voici le programme pour les suites numériques sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :

# Séquences et suites numériques

## SAVOIRS

- Suites monotones
  - Suites majorées, minorées, bornées
  - Suites convergentes :
    - Notion de convergence.
    - Unicité de la limite (admise)
    - Toute suite croissante et majorée converge
    - Toute suite décroissante et minorée converge.
    - Si f est une fonction numérique telle que \(\lim_{x \\to +\infty} f(x) = l\) alors la suite définie par \(u_n = f(n)\) converge vers l.
    - Si \((u_n)\) est une suite convergente vers a et f une fonction continue en a alors la suite \(v_n=f(u_n)\) converge vers f(a).
    - Convergence des suites géométriques (suites du type \(a^n\)).
    - Suites divergentes
    - Convergence des suites géométriques et des suites du type \(n^\\alpha\)
    - Suites divergentes

- Théorèmes de comparaison :
  - Soient les suites \(v_n\) et \(u_n\)
    - Si à partir d’un certain rang, \(v_n \leq u_n\) et si \(v_n\) tend vers +∞, alors \(u_n\) tend vers +∞.
    - Si à partir d’un certain rang, \(|v_n-l| \leq u_n\) et si \(u_n\) tend vers 0, alors \(v_n\) tend vers l.
    - Si à partir d’un certain rang, \(v_n \leq u_n \leq w_n\) et si \(v_n\) et \(w_n\) tend vers l, alors \(u_n\) tend vers l.
    - Si à partir d’un certain rang \(v_n \leq u_n\) et \(u_n\) tend vers l et \(v_n\) tend vers l’ alors l’≤ l.

- Suites \(a^n\) et \(n^\\alpha\). Croissance comparée
  - Limites et comportements asymptotiques comparés de suites (\(\ln n\); \(a^n\), \(a > 0\) et \(n^\\alpha\), \(\\alpha > 0\).

- Suites récurrentes définies par une relation du type : \(u_{n+1} = f(u_n)\).
  - Soit \(u_n\) une suite définie par \(u_{n+1} = f(u_n)\).
    - Si \( u_n \) est une suite définie par \( u_{n+1} = f(u_n) \), et si \( f \) est continue en \( l \) alors \( f(u_n) = l \).

## SAVOIR-FAIRE

- Démontrer qu’une suite est monotone :
  - Par comparaison de deux termes généraux consécutifs ;
  - Par l'étude des variations d’une fonction ;
  - Par un raisonnement par récurrence.

- Démontrer qu’une suite est majorée et/ou minorée :
  - Par un calcul direct ;
  - Par l’étude des variations d’une fonction ;
  - Par un raisonnement par récurrence.

- Démontrer qu’une suite est convergente ou divergente par :
  - L’étude du comportement d’une fonction ;
  - L’utilisation des opérations sur les limites ;
  - L’utilisation des théorèmes de comparaison.

- Conjecturer à partir d’une représentation graphique et comportement d’une suite récurrente.


"""

savoir_savoirFaire_Application_Affine = """
Voici le programme pour les Applications affines sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :
# Savoirs et Savoir-faire sur les Applications Affines

## Savoirs
- **Concepts Fondamentaux** : Comprendre la définition, les propriétés, et les points invariants des applications affines.
- **Relations avec les Applications Vectorielles** : Connaissance de la liaison entre applications affines et vectorielles.
- **Types d'Applications Affines** : Maîtrise des translations, homothéties, rotations, et symétries orthogonales.
- **Isométries et Similitudes** : Compréhension des isométries et similitudes en lien avec les applications affines.

## Savoir-faire
- **Application Pratique des Concepts** : Transformer des points et vecteurs via des applications affines.
- **Expression Analytique** : Exprimer mathématiquement une application affine avec des coordonnées.
- **Résolution d'Exercices** : Appliquer les connaissances théoriques pour résoudre des exercices pratiques liés aux applications affines.

"""

savoir_savoirFaire_Statistique = """
Voici le programme pour les statistique sois sûr de ne pas depasser ce programme quand tu vas généré ta réponse :
# Savoirs et Savoir-faire en Statistique

## Savoirs
- **Définition de la Statistique** 
  - Compréhension de la statistique comme un ensemble de données et comme une branche mathématique.
- **Langage Statistique**
  - Connaissance des termes tels que population, individu, caractères, modalités, échantillon.
- **Caractères Qualitatifs et Quantitatifs**
  - Distinction entre caractères qualitatifs et quantitatifs.
- **Présentation des Données Statistiques**
  - Méthodes de collecte et de présentation des données.
- **Éléments Caractéristiques d'une Série Statistique**
  - Compréhension de concepts comme le mode, la médiane, la moyenne, l'amplitude, les quartiles, la variance, et l'écart type.

## Savoir-faire
- **Classification et Organisation des Données**
  - Classer et organiser les données en intervalles et tableaux.
- **Calcul des Fréquences**
  - Calculer les fréquences relatives et cumulées.
- **Représentation Graphique**
  - Créer des diagrammes en bâton, des histogrammes et des diagrammes en secteur circulaire.
- **Analyse des Données**
  - Interpréter les données à l'aide de concepts statistiques.
- **Régression et Corrélation**
  - Comprendre et appliquer la régression linéaire et la corrélation linéaire.

"""
function_call_toll = [
    {
        "type": "function",
        "function": {
            "name": "Answer_Generator",
            "description": "Quand on a besoin d'expliquer une question théorique qui ne concerne pas la resolution d'exercice",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "La question poser par l'utilisateur"
                    }
                },
                "required": ["question"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "Generateur_exercice",
            "description": "Crée un exercice à partir de deux informations fournis par l'utilisateur, le niveau de difficulté et la leçon sur laquelle l'exercice doit porter",
            "parameters": {
                "type": "object",
                "properties": {
                    "lecon": {
                        "type": "string",
                        "enum":["Nombres_complexes","Arithmétiques","Fonctions_numériques","Suites_numériques","Primitives_Intégrales_Calculs_daires", "Fonctions_logarithmes","Fonctions_exponentielle","Equations_différentielles","Dénombrement_Probabilité_Variable_aléatoire_Loi_binomiale_Epreuve_de_Bernoulli","Barycentres"," Applications_affines"," Statistiques","Coniques"],
                        "description": "La leçon sur laquelle l'utilisateur à demandé l'exercice doit porté"
                    },
                    "difficulte": {
                        "type": "string",
                        "enum": ["facile", "moyen", "difficile"],
                        "description": "Le niveau de difficulté qu'a précisé l'utilisateur"
                    }
                },
                "required": ["lecon", "difficulte"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "Exercice_Solver",
            "description": "Résous un exercice ou un problème mathématique demander quand l'élèves lui en donne une",
            "parameters": {
                "type": "object",
                "properties": {
                    "Enonce": {
                        "type": "string",
                       
                    "description": "L'énoncé au complet de l'exercice avec les questions posées."
                },
                    "question": {
                      "type": "string",            
                      "description": "Les questions rélative à l'exercice."
            }

            },
            
            "required": ["Enonce","question"]
        }
    }
}
]

tool_english = [
    {
        "type": "function",
        "function": {
            "name": "Answer_Generator",
            "description": "When there is a need to explain a theoretical question that does not concern exercise resolution",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The question asked by the user"
                    }
                },
                "required": ["question"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "Exercise_Generator_math",
            "description": "Creates an exercise from two pieces of information provided by the user: the difficulty level and the lesson topic",
            "parameters": {
                "type": "object",
                "properties": {
                    "lesson": {
                        "type": "string",
                        "enum": ["Complex_Numbers", "Arithmetic", "Numerical_Functions", "Numerical_Sequences", "Primitives_Integrals_Area_Calculations", "Logarithmic_Functions", "Exponential_Functions", "Differential_Equations", "Counting_Probability_Random_Variable_Binomial_Distribution_Bernoulli_Trial", "Barycenters", "Affine_Applications", "Statistics", "Conics"],
                        "description": "The lesson topic on which the user has requested the exercise"
                    },
                    "difficulty": {
                        "type": "string",
                        "enum": ["easy", "medium", "hard"],
                        "description": "The difficulty level specified by the user"
                    }
                },
                "required": ["lesson", "difficulty"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "Exercise_Solver",
            "description": "Solves an exercise or a mathematical problem when provided by the student",
            "parameters": {
                "type": "object",
                "properties": {
                    "Statement": {
                        "type": "string",
                        "description": "The full statement of the exercise with the posed questions."
                    },
                    "question": {
                        "type": "string",
                        "description": "The questions related to the exercise."
                    }
                },
                "required": ["Statement", "question"]
            }
        }
    }
]
