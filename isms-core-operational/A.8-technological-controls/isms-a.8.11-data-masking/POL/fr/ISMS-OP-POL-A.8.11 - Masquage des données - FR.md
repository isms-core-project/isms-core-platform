<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.11-FR:operational:OP-POL:a.8.11 -->
**ISMS-OP-POL-A.8.11 — Masquage des données**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Masquage des données |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.11 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Usage interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.11 — Masquage des données

**Politiques internes associées** :

- Politique de classification et de traitement de l'information
- Politique de contrôle d'accès
- Politique de vie privée et de protection des DCP
- Politique d'utilisation de la cryptographie
- Politique de développement sécurisé
- Politique de suppression des informations

**Contrôles Annexe A associés** :

| Contrôle | Relation avec le masquage des données |
|----------|---------------------------------------|
| A.5.12 Classification de l'information | La classification des données conditionne les exigences de masquage selon le niveau de sensibilité |
| A.5.15 Contrôle d'accès | Le masquage apporte une défense en profondeur au-delà des contrôles d'accès |
| A.5.34 Vie privée et protection des DCP | La pseudonymisation et l'anonymisation comme mesures de protection de la vie privée |
| A.8.3 Restriction de l'accès aux informations | Les utilisateurs à privilèges peuvent accéder aux données non masquées avec supervision |
| A.8.10 Suppression des informations | La suppression est distincte du masquage ; les deux réduisent l'exposition |
| A.8.24 Utilisation de la cryptographie | Le chiffrement protège les données au repos/en transit ; le masquage obscurcit les données en cours d'utilisation |
| A.8.25 Cycle de vie du développement sécurisé | Les développeurs utilisent des données masquées dans les environnements hors production |

---

# Politique de masquage des données

## Objet

La présente politique a pour objet d'assurer l'utilisation appropriée du masquage des données pour protéger les informations sensibles — notamment les données à caractère personnel (DCP), les données financières et les identifiants — en obscurcissant les données lorsque la visibilité complète n'est pas requise pour des finalités métier légitimes.

Cette politique soutient la nLPD suisse (revDSG) art. 7 (protection des données dès la conception et par défaut) et art. 8 (sécurité des données par des mesures techniques et organisationnelles). Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, le RGPD art. 25 (protection des données dès la conception et par défaut) et art. 32 (sécurité du traitement, incluant la pseudonymisation) s'appliquent également. Le masquage des données est une mesure technique essentielle pour démontrer la conformité aux obligations de minimisation des données dans les deux cadres.

## Champ d'application

La présente politique s'applique à :

- Toutes les catégories de données sensibles : DCP, données financières, informations de santé, identifiants d'authentification, informations métier propriétaires et toutes données classifiées Confidentielles ou Restreintes.
- Tous les environnements : production (lorsqu'opérationnellement approprié), test/assurance qualité, développement, analytique, formation, bac à sable et systèmes de sauvegarde/archivage.
- Tous les cas d'utilisation du masquage : provisionnement de données hors production, génération de rapports, partage de données avec des tiers, développement et test d'applications, analytique et entraînement de modèles d'apprentissage automatique.
- Tous les employés, prestataires et fournisseurs de services tiers manipulant des données sensibles.

Les données classifiées Publiques selon le schéma de classification de l'organisation sont hors périmètre. La protection des données chiffrées est couverte par A.8.24 (Utilisation de la cryptographie). La suppression et la destruction des données sont couvertes par A.8.10 (Suppression des informations).

## Principe

Le masquage des données est appliqué selon le principe de minimisation des données : le personnel ne doit avoir accès aux données sensibles réelles que lorsque cela est strictement nécessaire à son rôle et à sa tâche. Dans tous les autres cas, les données sont masquées, pseudonymisées ou anonymisées dans la mesure où l'utilité métier est préservée.

Seules les techniques et outils de masquage approuvés par l'organisation sont utilisés. La sélection de la technique de masquage prend en compte la sensibilité des données, les exigences réglementaires, les besoins de réversibilité, la préservation du format et l'intégrité référentielle.

---

## Classification des données et exigences de masquage

Les exigences de masquage sont déterminées par le schéma de classification des informations de l'organisation (conformément au contrôle A.5.12). Le tableau suivant définit l'obligation de masquage par niveau de classification :

| Classification | Exigence de masquage | Justification |
|----------------|----------------------|---------------|
| **Restreinte** | Masquage obligatoire dans TOUS les environnements hors production | Sensibilité la plus élevée — l'exposition cause un préjudice grave |
| **Confidentielle** | Masquage obligatoire hors production ; basé sur les risques en production | Haute sensibilité — l'exposition cause un préjudice substantiel |
| **Usage interne** | Masquage basé sur les risques lorsque des DCP ou des exigences réglementaires s'appliquent | Sensibilité modérée — masquage sélectif basé sur le contenu |
| **Publique** | Aucun masquage requis | Aucune exigence de confidentialité |

### Catégories de données sensibles nécessitant une évaluation

| Catégorie | Exemples | Classification habituelle |
|-----------|----------|--------------------------|
| **Données à caractère personnel (DCP)** | Nom, AVS/NAS, numéro de passeport, courriel, téléphone, adresse | Restreinte / Confidentielle |
| **Données financières** | Numéro de carte de crédit (PAN), IBAN, solde de compte, salaire, NIF | Restreinte / Confidentielle |
| **Informations de santé** | Numéro de dossier médical, diagnostics, prescriptions, résultats de laboratoire | Restreinte |
| **Identifiants d'authentification** | Mots de passe, clés API, jetons, clés privées, chaînes de connexion | Restreinte |
| **Données métier propriétaires** | Secrets commerciaux, stratégies tarifaires, contrats clients | Confidentielle |
| **Données de catégorie spéciale** (RGPD art. 9 / données sensibles nLPD) | Origine raciale/ethnique, opinions politiques, croyances religieuses, données biométriques | Restreinte |

### Découverte et inventaire des données

L'organisation maintient un inventaire des données sensibles nécessitant un masquage, comprenant :

- Systèmes et bases de données contenant des données sensibles.
- Éléments de données (tables, colonnes, champs) nécessitant un masquage.
- Classification des données par élément et exigences réglementaires applicables.
- Propriétaire des données responsable des décisions de masquage.

La découverte des données est automatisée pour tous les environnements contenant des données Restreintes ou Confidentielles, en utilisant [Outil de découverte de données] ou équivalent. La découverte automatisée analyse les schémas de données sensibles connus (schémas DCP, numéros de carte de crédit, formats AVS/NAS, identifiants de santé) au moins trimestriellement. L'inventaire manuel est acceptable pour les organisations avec un patrimoine de données limité et sans données Restreintes, mais doit être complété par une découverte automatisée à mesure que le patrimoine de données s'accroît.

Les Propriétaires de données sont responsables de la classification des données dans leurs domaines, de la détermination des exigences de masquage, de l'approbation des techniques de masquage pour leurs données et de la validation de l'efficacité du masquage.

---

## Techniques de masquage approuvées

Les techniques de masquage suivantes sont approuvées pour usage organisationnel :

| Technique | Description | Réversibilité | Cas d'utilisation principaux |
|-----------|-------------|---------------|------------------------------|
| **Masquage statique des données (MSD)** | Remplacement permanent des données dans les bases de données hors production avant que les données quittent l'environnement de production | Irréversible | Environnements hors production, partage de données externe |
| **Masquage dynamique des données (MDD)** | Masquage en temps réel au moment de la requête sur la base du rôle utilisateur ; les données originales restent inchangées dans le stockage | S.O. (original inchangé) | Accès basé sur les rôles en production, règles d'affichage de conformité |
| **Caviardage / Nullification** | Suppression complète ou remplacement par des caractères de remplacement (par exemple `****`, `[MASQUÉ]`) | Irréversible | Rapports, exports, captures d'écran, affichage interface |
| **Substitution** | Remplacement par des données fictives réalistes préservant le format et la distribution | Irréversible | Génération de données de test, maintien de l'utilité des données |
| **Tokenisation** | Remplacement par des jetons non sensibles ; données originales stockées dans un coffre de jetons sécurisé | Réversible (avec accès au coffre) | Systèmes de paiement, intégrité référentielle, PCI DSS |
| **Pseudonymisation** | Remplacement par des pseudonymes ; ré-identifiable uniquement avec une clé conservée séparément | Réversible (avec la clé) | Conformité RGPD/nLPD, recherche, analytique |
| **Anonymisation** | Suppression irréversible de toutes les informations d'identification ; aucune clé ni correspondance conservée | Irréversible | Publication de données publiques, analyse statistique, jeux de données ouverts |

### Critères de sélection de la technique

Lors de la sélection d'une technique de masquage, les facteurs suivants sont pris en compte :

1. **Sensibilité des données** : une sensibilité plus élevée nécessite un masquage plus fort, moins réversible.
2. **Exigences réglementaires** : RGPD pseudonymisation (art. 32, art. 89), PCI DSS masquage à l'affichage (Req. 3.4–3.5), nLPD minimisation des données (art. 6).
3. **Cas d'utilisation métier** : développement/test, analytique, partage externe ou formation.
4. **Besoin de réversibilité** : existence d'un besoin légitime de récupérer les données originales.
5. **Préservation du format** : nécessité que l'application maintienne le format des données.
6. **Intégrité référentielle** : nécessité que les relations entre tables et les clés étrangères restent valides.
7. **Impact sur les performances** : surcharge du MDD en temps réel par rapport au traitement par lots du MSD.

Les nouvelles techniques de masquage ou les modifications significatives des techniques approuvées sont proposées à l'équipe sécurité, soumises à une revue et des tests de sécurité, et approuvées par le RSSI avant utilisation.

### Pseudonymisation vs. Anonymisation (distinction réglementaire)

Dans le cadre du RGPD et de la nLPD, les données pseudonymisées restent des données personnelles car la ré-identification est possible avec la clé conservée séparément. Les données anonymisées — pour lesquelles la ré-identification n'est plus raisonnablement possible — sortent du champ d'application de la réglementation sur la protection des données. L'organisation s'assure que la technique correcte est appliquée selon que les données doivent rester dans le périmètre de la protection des données (pseudonymisation) ou peuvent en être entièrement retirées (anonymisation).

**Évaluation de l'utilité des données anonymisées** : Avant d'appliquer l'anonymisation, le Propriétaire des données évalue si les données anonymisées conservent une utilité métier suffisante pour leur finalité. L'évaluation prend en compte :

- Si les propriétés statistiques (distributions, corrélations, tendances) sont préservées.
- Si les données anonymisées soutiennent le cas d'utilisation d'analyse, d'entraînement ou de test prévu.
- Si une généralisation ou suppression excessive rend les données inutilisables.
- Les compromis entre la protection de la vie privée (k-anonymat plus élevé) et l'utilité des données (moins de généralisation).

Lorsque l'anonymisation réduit excessivement l'utilité des données, la pseudonymisation avec des contrôles d'accès appropriés peut constituer une alternative préférable.

Les clés de pseudonymisation sont stockées séparément des données pseudonymisées, avec les exigences de séparation suivantes :

- **Séparation physique ou logique** : Les clés sont stockées dans un système, une base de données ou un domaine de sécurité différent des données pseudonymisées. La co-localisation des clés et des données sur le même serveur ou dans la même base de données est interdite.
- **Séparation des accès** : Le personnel ayant accès aux données pseudonymisées ne doit pas avoir accès aux clés de ré-identification, sauf autorisation spécifique pour une finalité documentée. Un double contrôle (autorisation à deux personnes) est requis pour la ré-identification des données Restreintes.
- **Journalisation des ré-identifications** : Tous les événements de ré-identification sont journalisés avec l'identité du demandeur, la justification, le périmètre des données et la référence d'approbation.

La gestion des clés suit la Politique d'utilisation de la cryptographie (A.8.24).

---

## Pratiques interdites

Les éléments suivants ne sont PAS acceptables comme techniques de masquage :

| Pratique interdite | Raison |
|-------------------|--------|
| **ROT13 ou chiffre de César** | Trivialement réversible ; non sécurisé cryptographiquement |
| **Encodage réversible uniquement** (Base64, encodage URL, hexadécimal) | Pas du masquage — juste de l'encodage ; facilement inversé par quiconque |
| **Simple substitution de caractères** (A=1, B=2) | Motif prévisible ; trivialement réversible |
| **Masquage côté client uniquement** (JavaScript / couche interface) | Contournable — les données restent non masquées dans le backend |
| **« Chiffrement » autoproduit** | Sécurité non validée ; non accepté pour la conformité |
| **Données de production en environnement hors production sans aucun masquage** | Violation de politique fondamentale |
| **Utilisation indéfinie du même jeu de données masquées sans actualisation** | Données obsolètes ; risque de contournement au fil du temps |

Ces pratiques donnent une apparence de sécurité sans protection réelle. Elles ne sont acceptables en aucune circonstance, et aucune exception ne peut être accordée pour leur utilisation.

---

## Exigences de couverture des environnements

Les données sensibles sont masquées dans les environnements où la visibilité complète n'est pas requise pour les opérations métier légitimes.

| Environnement | Exigence de masquage | Justification |
|---------------|----------------------|---------------|
| **Production** | Basé sur les risques ; appliquer le MDD lorsque opérationnellement réalisable | Les opérations métier peuvent nécessiter certaines données réelles ; documenter la justification des données non masquées |
| **Test / Assurance qualité** | Obligatoire pour les données Restreintes et Confidentielles | Aucun besoin métier de données sensibles réelles pour les tests |
| **Développement** | Obligatoire pour les données Restreintes et Confidentielles | Les développeurs n'ont pas besoin de données sensibles réelles |
| **Analytique / BI** | Obligatoire sauf si les données sont agrégées ou anonymisées | L'analytique peut fonctionner avec des données masquées ou agrégées |
| **Formation / Démonstration** | Obligatoire pour TOUTES les données sensibles — sans exception | Les environnements de formation doivent utiliser des données non sensibles |
| **Bac à sable / Expérimental** | Obligatoire pour TOUTES les données sensibles — sans exception | Les environnements non contrôlés sont à haut risque |
| **Sauvegarde / Archivage** | Même protection que l'environnement source | Les sauvegardes reflètent la sensibilité des données source |

### Exigences de mise en œuvre du MSD

- Le MSD est appliqué AVANT que les données quittent l'environnement de production.
- Le MSD maintient l'intégrité référentielle entre les tables liées. Lorsque des relations multi-tables existent, le masquage est appliqué de manière cohérente en utilisant la même clé ou correspondance de masquage pour préserver les relations de clés étrangères, l'intégrité des jointures et les règles métier inter-tables. L'intégrité référentielle est validée par des tests automatisés après chaque cycle de masquage.
- Le MSD préserve le format des données pour la compatibilité applicative. Note : la préservation du format peut réduire l'entropie du masquage (nombre de valeurs masquées possibles), ce qui augmente le risque de ré-identification. Pour les données Restreintes, l'organisation évalue si le masquage préservant le format offre une sécurité suffisante ou si des techniques non préservant le format avec adaptation au niveau applicatif sont requises.
- Les données masquées doivent être suffisamment réalistes pour les tests applicatifs.
- **Actualisation des données masquées** : Les environnements hors production utilisant le MSD sont actualisés avec des données nouvellement masquées à une fréquence définie — au minimum trimestriellement pour les environnements de développement actifs et semestriellement pour les environnements moins actifs. La fréquence d'actualisation tient compte des changements de données de production susceptibles d'affecter la validité des tests et de la réduction du risque de contournement du masquage par accumulation de connaissance de jeux de données masquées obsolètes.

### Exigences de mise en œuvre du MDD

- Le MDD est appliqué au niveau de la base de données ou de la couche applicative — pas côté client.
- Les règles MDD sont basées sur les rôles utilisateurs documentés et le moindre privilège.
- Le MDD ne doit pas être contournable par des utilisateurs sans autorisation appropriée. Les contrôles de prévention des contournements comprennent :
  - L'accès direct à la base de données (contournant la couche applicative) est restreint aux administrateurs de base de données autorisés.
  - Les règles MDD sont appliquées au niveau du moteur de base de données lorsque cela est pris en charge, pas uniquement au niveau de la couche applicative.
  - Les tentatives d'interrogation des données non masquées sous-jacentes via des vues, des procédures stockées ou des chemins d'accès alternatifs sont bloquées ou journalisées et alertées.
  - Des tests périodiques vérifient que le MDD ne peut être contourné par injection SQL, élévation de privilèges ou manipulation de schéma.
- L'impact sur les performances est évalué et maintenu dans des seuils définis :
  - **Latence des requêtes** : Le MDD ne doit pas ajouter plus de 15 % de latence aux temps de réponse de référence pour les requêtes standard.
  - **Débit** : Le MDD ne doit pas réduire le débit de la base de données de plus de 10 % dans des conditions de fonctionnement normales.
  - **Mesure de référence** : Des bases de référence de performance sont établies avant le déploiement du MDD et remesurées trimestriellement.
  - **Escalade** : Lorsque le MDD dépasse les seuils de performance, l'équipe sécurité évalue des approches de masquage alternatives (pré-traitement MSD, masquage au niveau applicatif ou optimisation des règles MDD).

### Exigences de tokenisation

- Le coffre de jetons est sécurisé par des contrôles d'accès et un chiffrement. Les clés de chiffrement du coffre :
  - Sont générées et stockées dans un module de sécurité matérielle (MSM) ou [KMS] lorsque disponible.
  - Sont renouvelées au minimum annuellement, avec un renouvellement automatisé privilégié.
  - Sont sauvegardées et récupérables conformément aux procédures de gestion des clés de l'organisation (A.8.24).
  - Ont des accès contrôlés séparément des données tokenisées — les administrateurs du coffre ne doivent pas avoir accès direct aux jeux de données tokenisés, et vice versa.
- Les jetons préservent le format lorsque requis (par exemple format de carte de crédit pour PCI DSS).
- La détokenisation nécessite une autorisation explicite et est journalisée. L'accès à la détokenisation est révisé trimestriellement dans le cadre des revues d'accès à privilèges.
- La gestion des clés du coffre suit la Politique d'utilisation de la cryptographie (A.8.24).

---

## Tests et validation

Les implémentations de masquage sont testées avant déploiement et après tout changement de configuration du masquage.

| Type de test | Objet | Quand requis |
|--------------|-------|--------------|
| **Test d'efficacité** | Vérifier que les données originales ne sont pas récupérables à partir du résultat masqué | Avant déploiement ; après changements |
| **Test d'intégrité référentielle** | Vérifier que les relations inter-tables sont préservées | Avant déploiement |
| **Test de validation du format** | Vérifier que les données masquées passent les règles de validation applicatives | Avant déploiement |
| **Test de performances** | Vérifier que la surcharge MDD est dans les limites acceptables | Avant déploiement MDD |
| **Évaluation du risque de ré-identification** | Vérifier que les données anonymisées/pseudonymisées ne peuvent être ré-identifiées | Annuellement ; après changements de structure des données |
| **Tests de régression** | Vérifier que le masquage continue de fonctionner après les changements système | Après changements de configuration du masquage |

### Méthodes de validation

- Inspection d'échantillons de données : comparaison manuelle des données masquées et non masquées.
- Détection automatisée de motifs : analyse des environnements hors production pour les motifs de données sensibles non masquées (par exemple numéros de carte de crédit, numéros AVS, adresses courriel).
- Tentatives d'ingénierie inverse : tentatives de récupération des données originales à partir du résultat masqué.
- Pour l'anonymisation : analyse statistique avec des seuils basés sur les risques :
  - **Données Restreintes** : k-anonymat >= 20, l-diversité >= 5 le cas échéant.
  - **Données Confidentielles** : k-anonymat >= 10, l-diversité >= 3 le cas échéant.
  - **Données Usage interne** : k-anonymat >= 5 minimum.
  - Lorsque les seuils de k-anonymat ne peuvent être atteints, l'utilité des données est évaluée par rapport au risque de ré-identification, et des techniques alternatives (généralisation, suppression, ajout de bruit) sont appliquées pour atteindre le seuil cible.

### Critères d'acceptation

Le masquage est acceptable lorsque :

- Les valeurs de données sensibles originales ne sont PAS présentes dans les jeux de données masquées.
- Le format des données et l'intégrité référentielle sont préservés.
- Les fonctionnalités applicatives ne sont pas altérées.
- L'impact sur les performances est dans les limites acceptables.
- Les exigences réglementaires sont satisfaites.

Lorsque les tests identifient des défaillances, la mise en œuvre est corrigée avant usage en production, la cause profonde est documentée et les tests sont réitérés.

### Fréquence d'évaluation

- **Évaluation complète** : annuellement (alignée sur le programme d'audit interne).
- **Vérification périodique** : trimestriellement pour les systèmes à haut risque et les environnements récemment modifiés.
- **Évaluation déclenchée** : dans les 30 jours suivant un incident significatif d'exposition de données, un changement majeur de système affectant les données sensibles, le déploiement d'une nouvelle solution de masquage ou un changement d'exigence réglementaire.

---

## Journalisation et supervision

Les événements liés au masquage suivants sont journalisés lorsque techniquement réalisable :

- Exécution du processus de masquage (démarrage, achèvement, erreurs).
- Changements de configuration du masquage (changements de technique, mises à jour des règles). Les changements de configuration suivent le processus de gestion des changements de l'organisation : demandés par du personnel autorisé, révisés par l'équipe sécurité, testés dans un environnement hors production, approuvés par le Propriétaire des données et le Responsable de l'équipe sécurité avant déploiement en production, et journalisés avec les états de configuration avant/après.
- Exceptions et contournements du masquage (approuvés ou tentés).
- Application des politiques de masquage dynamique (qui a accédé à quelles données avec quelle règle de masquage).
- Défaillances du masquage (processus n'ayant pas abouti).

**Conservation des journaux** :

| Type d'événement | Conservation minimale |
|------------------|-----------------------|
| Journaux du processus de masquage | 90 jours |
| Changements de configuration | 12 mois |
| Événements d'exception et de contournement | 12 mois |
| Journaux d'accès au masquage dynamique | 90 jours (Confidentiel+) |

Une conservation prolongée s'applique lorsque les exigences réglementaires imposent des délais plus longs.

L'organisation surveille les défaillances des processus de masquage, les tentatives répétées de contournement, les changements de configuration non autorisés et la dégradation des performances MDD. Les alertes sont intégrées au programme de supervision de la sécurité de l'organisation.

**Détection des tentatives de ré-identification** : L'organisation met en œuvre une supervision pour détecter les tentatives potentielles de ré-identification, notamment :

- Schémas de requêtes inhabituels sur des jeux de données pseudonymisées ou anonymisées (par exemple énumération systématique, recoupement avec des sources de données externes).
- Extraction en masse de données depuis des environnements contenant des données masquées.
- Tentatives d'accès aux clés de pseudonymisation ou aux coffres de jetons par du personnel non autorisé.
- Requêtes de corrélation joignant des jeux de données masquées avec des données de référence non masquées.

Les tentatives de ré-identification détectées sont traitées comme des incidents de sécurité de gravité Élevée et font l'objet d'une enquête immédiate.

---

## Réponse aux incidents liés aux défaillances du masquage

Les incidents de sécurité liés au masquage des données comprennent :

| Type d'incident | Gravité | Réponse |
|----------------|---------|---------|
| Données sensibles non masquées découvertes hors production | Élevée | Endiguement dans l'heure — arrêt du flux de données, suppression des données exposées, notification du Propriétaire des données |
| Défaillance du processus de masquage exposant des données sensibles | Critique | Endiguement dans les 15 minutes — arrêt de l'exposition, isolation des systèmes concernés, notification du RSSI |
| Ré-identification réussie de données masquées | Élevée | Évaluer la faiblesse de la technique, renforcer le masquage |
| Tentative de contournement du masquage | Élevée | Enquêter, prévenir la récidive |
| Accès non autorisé au coffre de jetons ou aux clés de pseudonymisation | Critique | Réponse à la compromission des clés conformément à A.8.24 |
| Exfiltration de données depuis un environnement insuffisamment masqué | Critique | Réponse complète aux incidents, évaluation de la notification de violation |

### Processus de réponse

1. **Détecter et signaler** : via la supervision, les signalements des utilisateurs ou les tests.
2. **Classifier** : gravité basée sur la sensibilité des données et l'étendue de l'exposition.
3. **Endiguer** : arrêter le flux de données, isoler les systèmes, prévenir toute exposition supplémentaire.
4. **Enquêter** : analyse des causes profondes, détermination du périmètre, évaluation de l'impact.
5. **Remédier** : corriger le masquage, valider l'efficacité, prévenir la récidive.
6. **Notifier** : escalade interne ; évaluer les exigences de notification de violation réglementaire.
7. **Réviser** : enseignements tirés, améliorations des contrôles.

### Évaluation de la notification de violation

Les incidents d'exposition de données sont évalués pour les exigences de notification de violation :

- **nLPD suisse** : Notification au PFPDT en cas de risque élevé pour la personnalité ou les droits fondamentaux (art. 24).
- **RGPD (le cas échéant)** : Notification dans les 72 heures en cas de risque pour les droits et libertés (art. 33–34).
- **Sectoriels** : Notification de violation PCI DSS, notification de violation HIPAA (le cas échéant).

Le DPD et le service juridique/conformité participent à toutes les décisions de notification de violation.

---

## Gestion des exceptions

Les exceptions aux exigences de masquage des données nécessitent :

- Justification métier documentée expliquant pourquoi le masquage ne peut être mis en œuvre.
- Évaluation des risques couvrant la probabilité et l'impact de l'exposition des données.
- Contrôles compensatoires (contrôles d'accès renforcés, chiffrement, supervision).
- Durée définie et chemin vers la pleine conformité.
- Approbation du Propriétaire des données pour le domaine de données concerné.
- Approbation du RSSI pour les exceptions concernant des données Confidentielles/Restreintes.

| Type d'exception | Approbation requise | Durée maximale |
|-----------------|---------------------|----------------|
| Système unique (faible sensibilité) | Responsable de l'équipe sécurité + Propriétaire des données | 12 mois, avec revue d'étape à 6 mois |
| Système unique (haute sensibilité) | RSSI + Propriétaire des données | 6 mois, avec revue d'étape à 3 mois |
| Exception à l'échelle de l'environnement | RSSI + Propriétaire des données | 6 mois, avec rapport mensuel d'avancement |
| Dérogation au masquage de production | RSSI + Direction générale | Réapprobation annuelle, avec revues d'étape trimestrielles |
| Contournement de technique interdite | NON AUTORISÉ | S.O. |

Les exceptions actives sont révisées trimestriellement, révoquées si la justification métier change et expirent automatiquement à la fin de la durée approuvée (pas de renouvellement implicite).

---

## Optionnel : Contrôles des données de cartes de paiement (PCI DSS)

*Applicable uniquement si des données de cartes de paiement sont traitées et si le périmètre PCI existe.*

Si le périmètre PCI existe, les exigences supplémentaires de masquage des données suivantes s'appliquent :

- Les Numéros de Compte Principaux (PAN) doivent être rendus illisibles partout où ils sont stockés, conformément à PCI DSS Req. 3.4 (tokenisation, troncation, hachage ou chiffrement fort).
- Lors de l'affichage des PAN, le masquage doit afficher au maximum les six premiers et les quatre derniers chiffres, conformément à PCI DSS Req. 3.5.1.
- Les PAN complets ne doivent pas être présents dans les environnements hors production à moins que l'environnement hors production ne satisfasse à tous les contrôles PCI DSS applicables. Le MSD ou la tokenisation est appliqué avant que les données quittent l'environnement des données des titulaires de cartes.
- L'utilisation de données de cartes de paiement hors production est régie par une politique d'utilisation des données documentée conformément à PCI DSS Req. 12.3.

---

## Formation et sensibilisation

**Tout le personnel** reçoit une formation annuelle de sensibilisation à la sécurité comprenant :

- L'obligation d'utiliser des données masquées dans les environnements hors production.
- Comment reconnaître et signaler des données sensibles non masquées.
- L'interdiction de tenter de ré-identifier des données masquées, pseudonymisées ou anonymisées.

**Le personnel technique** (Équipe sécurité, Opérations informatiques, développeurs) reçoit une formation sur :

- Les techniques de masquage approuvées et l'utilisation des outils.
- Les procédures de test et de validation.
- La réponse aux incidents liés aux défaillances du masquage.

**Les Propriétaires de données** sont informés sur :

- Les responsabilités en matière de classification des données et de décisions de masquage.
- Les critères d'évaluation et d'approbation des demandes d'exception.
- La validation de l'efficacité du masquage pour leurs domaines de données.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Anonymisation** | Suppression irréversible de toutes les informations d'identification telle que la ré-identification n'est plus possible. Les données anonymisées ne sont plus des données personnelles au sens du RGPD/nLPD. |
| **Masquage des données** | Processus d'obscurcissement des données originales avec un contenu modifié pour protéger les informations sensibles tout en maintenant le format et l'utilisabilité des données. |
| **Masquage dynamique des données (MDD)** | Masquage en temps réel appliqué au moment de l'accès aux données sur la base du rôle ou du contexte utilisateur. Les données originales restent inchangées dans le stockage. |
| **Pseudonymisation** | Remplacement des identifiants directs par des pseudonymes de sorte que les données ne puissent identifier les individus sans informations supplémentaires (clé) conservées séparément. Les données pseudonymisées restent des données personnelles. |
| **Ré-identification** | Processus de détermination de l'identité originale d'une personne concernée à partir de données masquées, pseudonymisées ou anonymisées. |
| **Intégrité référentielle** | Maintien des relations valides entre les données liées entre tables ou jeux de données après masquage. |
| **Masquage statique des données (MSD)** | Remplacement permanent des données sensibles par des valeurs masquées dans les bases de données hors production. Les données originales sont remplacées de manière irréversible. |
| **Tokenisation** | Remplacement des données sensibles par des jetons non sensibles ; données originales stockées dans un coffre de jetons sécurisé permettant une réversibilité contrôlée. |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Direction générale** | Approuver la politique de masquage des données ; assurer les ressources adéquates ; accepter le risque résiduel lorsque le masquage n'est pas réalisable |
| **RSSI** | Responsabilité de l'efficacité de la politique et du programme de masquage ; approbation des exceptions à haut risque et des nouvelles techniques ; révision annuelle de la politique |
| **DPD** | Conseiller sur la conformité RGPD/nLPD pour les implémentations de masquage ; revoir les techniques de pseudonymisation et d'anonymisation pour l'adéquation réglementaire |
| **Propriétaires de données** | Classifier les données ; déterminer les exigences de masquage ; approuver les techniques et exceptions pour leurs domaines de données ; valider l'efficacité du masquage |
| **Équipe sécurité** | Mettre en œuvre la politique de masquage ; évaluer et sélectionner les outils ; configurer et maintenir les solutions ; conduire les tests d'efficacité |
| **Opérations informatiques** | Déployer et maintenir l'infrastructure de masquage ; exécuter les traitements par lots MSD et la configuration MDD ; surveiller les performances des processus de masquage |
| **Équipes de développement** | Utiliser des données masquées hors production ; mettre en œuvre le MDD dans les applications lorsque requis ; signaler les problèmes de masquage ; interdit de contourner les contrôles |
| **Ensemble du personnel** | Se conformer à la politique de masquage ; signaler les données sensibles non masquées suspectées hors production ; interdit de tenter la ré-identification |

---

## Preuves

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | Inventaire des données sensibles (systèmes, éléments de données, classification, statut de masquage) | Propriétaires de données / Équipe sécurité | Révision annuelle, mise à jour continue | 3 ans |
| 2 | Inventaire des techniques de masquage (techniques approuvées, outils, configurations) | Équipe sécurité | Révision annuelle | 3 ans |
| 3 | Évaluation de la couverture des environnements (environnements masqués, lacunes, exceptions) | Équipe sécurité | Annuel, trimestriel pour les systèmes à haut risque | 3 ans |
| 4 | Résultats des tests d'efficacité du masquage (inspections d'échantillons, analyses de motifs) | Équipe sécurité | Avant déploiement ; après changements | 3 ans |
| 5 | Registre des exceptions (exceptions actives, approbations, contrôles compensatoires, dates d'expiration) | RSSI / Équipe sécurité | Révision trimestrielle | 3 ans |
| 6 | Journaux des processus de masquage et enregistrements des changements de configuration | Opérations informatiques | Continu | Selon le tableau de conservation des journaux |
| 7 | Enregistrements des incidents liés aux défaillances du masquage | Équipe sécurité | Par incident | 3 ans |
| 8 | **Accords de partage de données avec des tiers** (exigences de masquage, interdiction de ré-identification, droits d'audit) | Juridique / Équipe sécurité | Par arrangement de partage ; révision annuelle | Actif + 3 ans |
| 9 | **Résultats des évaluations du risque de ré-identification** (mesures de k-anonymat, l-diversité, évaluations de l'utilité des données) | Équipe sécurité / Propriétaires de données | Annuellement ; après changements de structure des données | 3 ans |
| 10 | **Enregistrements des changements de configuration du masquage** (demandes de changement, approbations, états avant/après, résultats des tests) (SOC 2 : CC8.1) | Équipe sécurité / Opérations informatiques | Par changement | 3 ans |
| 11 | **Enregistrements de supervision des performances MDD** (mesures de référence, rapports de performances trimestriels, alertes de seuils) | Opérations informatiques | Trimestriel | 12 mois |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifie la conformité à la présente politique par diverses méthodes, notamment l'analyse automatisée des environnements hors production pour détecter les données sensibles, les tests d'efficacité du masquage, les revues du registre des exceptions, les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique est approuvée et enregistrée par le Responsable de la sécurité de l'information au préalable, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie. Les exceptions sont communiquées à l'équipe de revue de direction. Les techniques interdites ne peuvent faire l'objet d'exceptions en aucune circonstance.

## Non-conformité

Tout employé reconnu coupable d'avoir enfreint la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Les tentatives délibérées de contourner les contrôles de masquage ou de ré-identifier des données masquées sont traitées comme des violations graves de sécurité.

## Exigences de partage de données avec des tiers

Lorsque l'organisation partage des données masquées, pseudonymisées ou anonymisées avec des tiers (fournisseurs, partenaires, chercheurs, clients) :

- **Exigences contractuelles** : Les accords de partage de données précisent :
  - La technique de masquage appliquée et la classification des données originales.
  - L'interdiction de tenter de ré-identifier les données masquées, pseudonymisées ou anonymisées.
  - Les obligations de retour ou de destruction à la résiliation de l'arrangement de partage.
  - Des dispositions de droit d'audit pour vérifier les pratiques de traitement des données du tiers.
  - Des obligations de notification de violation si le tiers découvre que les données ont été ré-identifiées ou exposées.
- **Évaluation des risques** : Une évaluation des risques de partage de données est effectuée avant tout partage initial, évaluant le risque de ré-identification, la maturité de la gestion des données du tiers et les implications réglementaires.
- **Supervision continue** : Les arrangements de partage de données sont révisés annuellement et lors de changements importants dans l'environnement du tiers ou le périmètre des données partagées.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions prennent en compte les évolutions des réglementations sur la protection des données, les techniques de ré-identification émergentes, les nouvelles technologies de masquage, les conclusions des audits et les enseignements tirés des incidents de masquage.

---

# Domaines de la norme ISO 27001 couverts

Politique de masquage des données — Correspondance des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.12 Classification de l'information |
| Clause 6.1 Actions pour traiter les risques | 5.15 Contrôle d'accès |
| Clause 6.2 Objectifs de sécurité de l'information | 5.34 Vie privée et protection des DCP |
| Clause 7.3 Sensibilisation | 8.3 Restriction de l'accès aux informations |
| | 8.10 Suppression des informations |
| | **8.11 Masquage des données** |
| | 8.24 Utilisation de la cryptographie |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence | Applicabilité |
|-------|-----------|---------------|
| nLPD suisse (revDSG) | Art. 7 — Protection des données dès la conception et par défaut ; Art. 8 — Sécurité des données (mesures techniques et organisationnelles) | Obligatoire |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales de sécurité des données | Obligatoire |
| RGPD (le cas échéant) | Art. 25 — Protection des données dès la conception et par défaut ; Art. 32 — Sécurité du traitement (pseudonymisation) ; Art. 89 — Garanties pour la recherche/statistiques | Lorsque des données personnelles UE/EEE sont traitées |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.11 — Masquage des données | Périmètre de certification |
| ISO/IEC 27002:2022 | Section 8.11 — Recommandations de mise en œuvre pour les contrôles de masquage des données | Recommandations |
| PCI DSS v4.0 | Req. 3.4–3.5 — Masquage du PAN et rendu illisible ; Req. 12.3 — Politiques de données hors production | Si des données de cartes de paiement sont traitées |
| Règle de confidentialité HIPAA | §164.514 — Normes de dé-identification (Détermination d'expert / Sphère de sécurité) | Si des données de santé américaines (ePHI) sont traitées |
| FINMA | Protection des données clients ; gestion des risques d'externalisation (Circulaire 2018/3) | Si établissement financier suisse réglementé |

---

<!-- QA_VERIFIED: 2026-03-29 -->
