<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.4-5-11-FR:framework:POL:a.7.4-5-11 -->
**ISMS-POL-A.7.4-5-11 — Sécurité de l'infrastructure physique**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de sécurité de l'infrastructure physique |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.7.4-5-11 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique consolidée initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel (ou lors de changements importants des installations, d'incidents de sécurité ou de mises à jour réglementaires)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Responsable des installations
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.7.1-3 (Contrôle d'accès physique)
- ISMS-POL-A.5.19-23 (Services cloud)
- ISMS-POL-A.5.24-28 (Gestion des incidents)
- ISMS-POL-A.5.30-8.13-14 (Continuité des activités)
- ISMS-IMP-A.7.4-5-11-S1-UG/TG (Évaluation de la surveillance physique)
- ISMS-IMP-A.7.4-5-11-S2-UG/TG (Mise en œuvre de la protection environnementale)
- ISMS-IMP-A.7.4-5-11-S3-UG/TG (Mise en œuvre de la résilience des utilités)
- ISMS-IMP-A.7.4-5-11-S4-UG/TG (Évaluation des installations)
- ISO/IEC 27001:2022 Contrôles A.7.4, A.7.5, A.7.11

---

# Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de sécurité de l'infrastructure physique pour protéger les actifs informationnels par une surveillance complète, une protection environnementale et une résilience des utilités, conformément aux Contrôles A.7.4, A.7.5 et A.7.11 de la norme ISO/IEC 27001:2022.

**Objet** : Définir les exigences organisationnelles de gouvernance de la sécurité de l'infrastructure physique. Cette politique établit QUELLE protection de sécurité physique est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées dans ISMS-IMP-A.7.4-5-11.

**Approche par contrôles combinés** : Ces trois contrôles sont mis en œuvre comme un Cadre unifié de sécurité de l'infrastructure physique car ils opèrent sur la même infrastructure physique, créent des interdépendances et partagent des processus d'évaluation communs. Chaque contrôle conserve des exigences distinctes à des fins de Déclaration d'applicabilité (DdA).

---

# Périmètre

## Dans le périmètre

**Installations** :

- Centres de données sur site et sites de reprise après sinistre
- Salles serveurs et armoires de télécommunications
- Bureaux d'entreprise (siège social, régionaux, agences)
- Installations de colocation (avec modèle de responsabilité partagée)
- Installations distantes et temporaires où des équipements de [Organisation] sont localisés

**Personnel** :

- Gestion des installations, Opérations de sécurité, Opérations IT
- Tous les employés accédant aux installations physiques
- Contractants, fournisseurs et visiteurs

## Organisations 100 % cloud

Les organisations opérant intégralement dans des environnements cloud sans installations de traitement de l'information sur site peuvent marquer les Contrôles A.7.4, A.7.5 et A.7.11 comme « Non applicable » dans la Déclaration d'applicabilité.

**Exigences de la décision d'applicabilité** : La détermination « Non applicable » DOIT être documentée dans la Déclaration d'applicabilité avec une justification comprenant :
- Référence à l'inventaire des actifs confirmant l'absence d'installations sur site (ISMS-IMP-A.5.9)
- Vérification de la sécurité physique du fournisseur cloud par révision SOC 2 Type II (ISMS-IMP-A.5.19-23)
- Confirmation de révision annuelle que le statut 100 % cloud demeure exact

La sécurité physique du fournisseur cloud DOIT être évaluée dans le cadre de la gestion des fournisseurs (Contrôle A.5.19-23).

## Installations de colocation

Lors de l'utilisation d'espaces de colocation, les responsabilités d'infrastructure physique sont partagées entre le prestataire de colocation et [Organisation]. Une matrice de responsabilités formelle DOIT être documentée dans le contrat de colocation et maintenue dans le Registre de gestion des fournisseurs (ISMS-POL-A.5.19-23) pour un suivi centralisé. Les contrôles du prestataire DOIVENT être vérifiés annuellement par des rapports d'audit (SOC 2 Type II ou certification ISO 27001), avec la révision documentée dans les dossiers d'évaluation des fournisseurs.

## Hors périmètre

- Sécurité physique des appareils portables (couverte par A.7.7, A.8.1)
- Sécurité du transport des équipements (couverte par A.7.13)
- Stockage des supports de sauvegarde hors site (couvert par A.8.13)
- Sécurité du personnel et vérification des antécédents (couverts par A.6.1-6.4)

---

# Énoncés de politique

## Surveillance de la sécurité physique (A.7.4)

> *Les locaux devraient être surveillés en permanence contre les accès physiques non autorisés.*

**Objectif du contrôle** : Détecter et répondre aux tentatives d'accès physique non autorisé par une surveillance complète.

[Organisation] DOIT :

1. **Contrôle d'accès** : Mettre en œuvre un contrôle d'accès électronique à tous les points d'entrée/sortie des installations avec authentification, journalisation et intégration à la gestion des identités
2. **Détection d'intrusion** : Déployer des systèmes de détection d'intrusion adaptés à la criticité des installations et à l'évaluation des risques
3. **Vidéosurveillance** : Assurer une couverture CCTV des entrées des installations, des zones restreintes et de l'infrastructure critique
4. **Gestion des visiteurs** : Exiger que tous les visiteurs s'enregistrent, reçoivent une identification temporaire et soient escortés dans les zones restreintes
5. **Révision des accès** : Effectuer des révisions périodiques des accès pour identifier et révoquer les droits d'accès périmés ou non autorisés
6. **Intégration sécurité** : Intégrer les événements de sécurité physique au SIEM (ISMS-POL-A.8.16) pour la corrélation avec les événements de sécurité logique et la réponse aux incidents

**Preuves de conformité** : La conformité à la surveillance de la sécurité physique est démontrée par ISMS-IMP-A.7.4-5-11-S1 (Évaluation de la surveillance physique), qui génère des classeurs mensuels contenant :
- Journaux de contrôle d'accès électronique avec taux de succès/échec d'authentification
- Vérification de la disponibilité et de la couverture du système CCTV
- Alertes du système de détection d'intrusion et délais de réponse
- Dossiers de gestion des visiteurs avec conformité aux escortes
- Résultats des révisions des accès avec actions de révocation

## Protection environnementale (A.7.5)

> *La protection contre les menaces physiques et environnementales devrait être conçue et mise en œuvre.*

**Objectif du contrôle** : Protéger les installations de traitement de l'information contre les menaces physiques et environnementales, notamment l'incendie, les inondations et les conditions climatiques.

[Organisation] DOIT :

1. **Évaluation des menaces** : Effectuer une évaluation des risques de menaces environnementales en tenant compte de la localisation géographique et des caractéristiques des installations
2. **Protection incendie** : Mettre en œuvre des systèmes de détection et d'extinction d'incendie adaptés au type d'installation et aux exigences réglementaires
3. **Protection contre l'eau** : Installer des systèmes de détection d'eau et mettre en œuvre des mesures d'atténuation des inondations basées sur l'évaluation des risques
4. **Contrôle climatique** : Maintenir la température et l'humidité dans des plages acceptables pour les équipements de traitement de l'information
5. **Protection structurelle** : Assurer l'intégrité du bâtiment et mettre en œuvre des barrières physiques adaptées aux menaces identifiées
6. **Réponse d'urgence** : Documenter et tester les procédures de réponse d'urgence pour les incidents environnementaux

**Preuves de conformité** : La conformité à la protection environnementale est démontrée par ISMS-IMP-A.7.4-5-11-S2 (Évaluation de la protection environnementale), qui génère des classeurs trimestriels contenant :
- Résultats des tests du système incendie et certificats d'inspection
- Journaux du système de détection d'eau et dossiers de maintenance
- Données de surveillance de la température/humidité avec conformité aux seuils
- Révisions de l'évaluation des menaces environnementales (annuelle)
- Dossiers d'exercices de réponse d'urgence et constats

## Résilience des utilités (A.7.11)

> *Les installations de traitement de l'information devraient être protégées contre les pannes d'alimentation et autres perturbations causées par des défaillances des utilités de soutien.*

**Objectif du contrôle** : Assurer la continuité du traitement de l'information par une infrastructure d'utilités résiliente comprenant l'alimentation électrique, le refroidissement et les télécommunications.

[Organisation] DOIT :

1. **Protection électrique** : Mettre en œuvre des systèmes d'alimentation sans interruption (ASI) de capacité adaptée à la criticité des installations
2. **Alimentation de secours** : Fournir une capacité de génération de secours pour les installations critiques afin d'assurer la continuité d'exploitation lors de pannes prolongées
3. **Résilience du refroidissement** : Mettre en œuvre des systèmes de refroidissement redondants adaptés à la criticité des installations
4. **Télécommunications** : Assurer la connectivité des télécommunications avec la redondance adaptée à la criticité des installations
5. **Surveillance des utilités** : Surveiller les systèmes d'utilités en temps réel avec alertes en cas de défaillances ou dépassements de seuil
6. **Tests de défaillance** : Effectuer des tests réguliers des systèmes de résilience des utilités selon le calendrier suivant :
   - Tests de basculement ASI : Trimestriels
   - Test en charge du groupe électrogène de secours : Semestriel
   - Vérification de la redondance du refroidissement : Trimestrielle
   - Basculement des télécommunications : Annuel

**Preuves de conformité** : La conformité à la résilience des utilités est démontrée par ISMS-IMP-A.7.4-5-11-S3 (Évaluation de la résilience des utilités), qui génère des classeurs trimestriels contenant :
- Journaux de tests ASI avec résultats de basculement (succès/échec)
- Rapports de tests en charge du groupe électrogène avec vérification de la consommation de carburant
- Dossiers de vérification de la redondance du refroidissement
- Résultats des tests de basculement des télécommunications
- Historique des alertes de surveillance des utilités et délais de réponse

## Niveaux de criticité des installations

Les installations DOIVENT être classifiées en niveaux de criticité sur la base de l'Analyse d'impact sur les activités :

| Niveau | Définition | Surveillance | Environnement | Utilités | Fréquence de révision |
|--------|------------|-------------|---------------|----------|----------------------|
| **Niveau 1 – Critique** | Centres de données, salles serveurs principales, sites de reprise | Surveillance SOC 24h/24 7j/7, SLA de réponse < 15 min, détection d'intrusion obligatoire | Extinction + détection incendie, détection eau toutes zones, température 18-27 °C ±2 °C | ASI N+1 (deux unités, 30 min d'autonomie chacune), groupe électrogène (48 h de carburant), double voie de refroidissement | Vérification manuelle mensuelle |
| **Niveau 2 – Standard** | Bureaux d'entreprise, agences, salles serveurs non critiques | Surveillance 8h/5j, réponse le jour ouvrable suivant, détection d'intrusion optionnelle | Détection incendie (extinction si valeur équipements > CHF 500 k), détection eau zones à haut risque uniquement, température 18-27 °C ±5 °C | ASI unique (15 min d'autonomie minimum), groupe électrogène non requis, refroidissement simple | Vérification manuelle trimestrielle |

**Critères de classification des niveaux** : Les installations DOIVENT être classifiées sur la base de l'Analyse d'impact sur les activités (ISMS-POL-A.5.30-8.13-14) en tenant compte :
- Criticité des systèmes : Applications Niveau 1/2 hébergées
- Classification des données : Traitement de données CONFIDENTIELLES = Niveau 1
- Objectifs de délai de reprise : DTR < 4 h = Niveau 1, DTR > 4 h = Niveau 2

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | Responsabilité globale du cadre de sécurité de l'infrastructure physique ; approbation de la politique ; allocation budgétaire ; reporting exécutif |
| **Responsable des installations** | Opérations quotidiennes de l'infrastructure physique ; maintenance des systèmes environnementaux et d'utilités ; gestion des fournisseurs |
| **Responsable des opérations de sécurité** | Mise en œuvre de la surveillance de la sécurité physique ; gestion du contrôle d'accès ; opérations CCTV ; coordination de la réponse aux incidents |
| **Propriétaires de systèmes** | Exigences de sécurité physique pour les systèmes détenus ; coordination du placement des équipements ; participation aux incidents |
| **Opérations IT** | Intégration sécurité physique-logique (SIEM) ; infrastructure réseau pour les systèmes de sécurité ; tableaux de bord de surveillance |
| **Audit interne** | Audit annuel de conformité à la sécurité physique ; tests des contrôles ; révision des preuves |
| **Gestion des risques** | Évaluation des risques de sécurité physique ; évaluation des menaces environnementales ; maintien du registre des risques |
| **Responsable conformité** | Suivi de la conformité réglementaire ; collecte des preuves ; liaison réglementaire |

---

# Gouvernance et conformité

## Référentiel d'évaluation

[Organisation] DOIT effectuer des évaluations régulières conformément à la méthodologie ISMS-IMP-A.7.4-5-11 :

- **En continu** : Surveillance et alertes en temps réel
- **Mensuel** : Collecte automatisée de données depuis les systèmes de sécurité physique
- **Trimestriel** : Vérification manuelle et révision de la conformité aux tests
- **Annuel** : Audit complet avec vérification externe

## Notation de conformité

| Plage de score | Évaluation | Action requise |
|----------------|-----------|----------------|
| > 90 % | Excellent | Maintenir les contrôles actuels |
| 75-89 % | Bon | Traiter les lacunes lors du prochain cycle de révision |
| 60-74 % | Acceptable | Élaborer un plan de remédiation dans les 30 jours |
| < 60 % | Non conforme | Remédiation immédiate requise, escalade vers le RSSI |

**Méthodologie de notation** : Le score de conformité est calculé à partir des indicateurs du Tableau de bord récapitulatif suivis dans les classeurs d'évaluation de l'infrastructure physique selon des indicateurs pondérés :

| Indicateur | Pondération | Source de mesure |
|-----------|-------------|-----------------|
| Disponibilité du système de contrôle d'accès | 20 % | Journaux du système de contrôle d'accès |
| Conformité des paramètres environnementaux (temp./humidité dans les seuils) | 20 % | Système de surveillance environnementale |
| Taux de réussite des tests de résilience des utilités | 15 % | Dossiers de tests (classeur S3) |
| Statut opérationnel des systèmes de détection incendie/eau | 15 % | Dossiers d'inspection |
| Respect des délais de réponse aux incidents de sécurité | 15 % | Système de gestion des incidents |
| Conformité à la gestion des visiteurs | 10 % | Registres visiteurs |
| Achèvement de la formation à la sécurité physique | 5 % | Dossiers LMS |

La méthodologie de calcul détaillée et les définitions des indicateurs sont documentées dans ISMS-IMP-A.7.4-5-11-S4.

## Gestion des exceptions

Les exigences de sécurité de l'infrastructure physique peuvent être dispensées par un processus formel d'exception :

- **Scénarios valides** : Infaisabilité technique, coût disproportionné, dérogation temporaire lors de transitions
- **Autorité d'approbation** : Responsable des opérations de sécurité (faible risque), RSSI (risque moyen), Direction générale (risque élevé)
- **Exigences** : Justification documentée, évaluation des risques, contrôles compensatoires, durée définie (maximum 6 mois)
- **Révision** : Réévaluation à l'expiration, lors de changements d'installations ou d'incidents

## Remédiation des lacunes

Les déficiences de contrôle de l'infrastructure physique identifiées lors des évaluations DOIVENT être gérées comme suit :

**1. Documentation** : Les déficiences DOIVENT être enregistrées dans les dossiers d'évaluation de la sécurité physique (suivis via le Tableau de bord récapitulatif de chaque classeur d'évaluation) avec :
- Description de la lacune et contrôle(s) affecté(s) (A.7.4, A.7.5, A.7.11)
- Gravité du risque (Critique/Élevé/Moyen/Faible conformément à la Classification des incidents)
- Responsable assigné et date de clôture cible
- Contrôles compensatoires (le cas échéant)
- Statut (Ouvert/En cours/Clôturé)

**2. Suivi** : Le Registre des lacunes DOIT être révisé :
- Mensuellement : Révision par le Responsable des opérations de sécurité avec suivi des responsables
- Trimestriellement : Révision par le RSSI avec escalade exécutive pour les lacunes Critiques/Élevées en retard
- Annuellement : Vérification par l'Audit interne des preuves de clôture

**3. Clôture** : Les lacunes ne peuvent être clôturées qu'après :
- Remédiation mise en œuvre et vérifiée
- Preuves documentées (par ex., bon de réception du système, résultats de tests)
- Validation par le Responsable des opérations de sécurité (Faible/Moyen) ou le RSSI (Élevé/Critique)

**4. Escalade** : Les lacunes ouvertes au-delà de la date cible DOIVENT être escaladées conformément à ISMS-POL-A.5.24-28 (Gestion des incidents).

## Classification des incidents

| Gravité | Exemples | Réponse |
|---------|----------|---------|
| **Critique** | Accès non autorisé à des zones restreintes ; violation physique ; vol ; événement environnemental majeur | Réponse immédiate conformément à ISMS-POL-A.5.24-28 |
| **Élevé** | Tentatives répétées d'accès échouées ; talonnage ; badges perdus ; alertes environnementales | Investigation et réponse le jour même |
| **Moyen** | Porte maintenue ouverte ; fausses alarmes fréquentes ; dépassements environnementaux mineurs | Documenté et investigué |
| **Faible** | Échec d'accès unique ; violations mineures de politique | Journalisé pour analyse des tendances |

## Révision de la politique

- **Fréquence** : Annuelle ou lors d'un événement déclencheur significatif
- **Événements déclencheurs** : Changements d'installations, incidents de sécurité, mises à jour réglementaires, changements technologiques
- **Participants** : RSSI, Responsable des installations, Responsable des opérations de sécurité, Responsable conformité
- **Approbation** : RSSI (modifications mineures), Direction générale (modifications importantes)

---

# Applicabilité réglementaire

## Conformité obligatoire (Niveau 1)

| Réglementation | Exigences clés |
|----------------|----------------|
| **nLPD suisse** | Art. 8 – Mesures techniques et organisationnelles pour la sécurité physique |
| **RGPD de l'UE** | Art. 32 – Sécurité du traitement incluant les mesures physiques |
| **ISO/IEC 27001:2022** | Contrôles A.7.4, A.7.5, A.7.11 – Politique documentée et mise en œuvre |

## Conformité conditionnelle (Niveau 2)

| Réglementation | Condition de déclenchement |
|---------------|---------------------------|
| **Circulaire FINMA 2023/1** | Établissement financier réglementé en Suisse |
| **DORA (UE) 2022/2554** | Entité de services financiers UE |
| **Directive NIS2 (UE) 2022/2555** | Entité essentielle/importante dans l'UE |

Se référer à ISMS-POL-00 (Cadre d'applicabilité réglementaire) pour la catégorisation réglementaire complète.

---

# Documents connexes

## Références internes au SMSI

| Document | Relation |
|----------|----------|
| ISMS-POL-00 | Cadre d'applicabilité réglementaire |
| ISMS-POL-A.7.1-3 | Contrôle d'accès physique (prérequis) |
| ISMS-POL-A.5.19-23 | Services cloud (évaluation du prestataire cloud) |
| ISMS-POL-A.5.24-28 | Gestion des incidents (réponse aux incidents) |
| ISMS-POL-A.5.30-8.13-14 | Continuité des activités (intégration BC/DR) |

## Orientations de mise en œuvre

| Document | Objet |
|----------|-------|
| ISMS-IMP-A.7.4-5-11-S1 | Évaluation de la surveillance physique |
| ISMS-IMP-A.7.4-5-11-S2 | Évaluation de la protection environnementale |
| ISMS-IMP-A.7.4-5-11-S3 | Évaluation de la résilience des utilités |

## Normes externes

- ISO/IEC 27001:2022 – Systèmes de management de la sécurité de l'information
- ISO/IEC 27002:2022 – Contrôles de sécurité de l'information
- NIST SP 800-53 Rév. 5 – Protection physique et environnementale (PE)
- Normes de niveau Uptime Institute – Classification des centres de données
- TIA-942 – Norme d'infrastructure des télécommunications pour les centres de données

---

# Intégration dans le SMSI

## Déclaration d'applicabilité

| Contrôle | Statut | Référence de mise en œuvre |
|----------|--------|---------------------------|
| **A.7.4 – Surveillance de la sécurité physique** | Applicable | Cette politique, ISMS-IMP-A.7.4-5-11-S1 |
| **A.7.5 – Protection contre les menaces physiques et environnementales** | Applicable | Cette politique, ISMS-IMP-A.7.4-5-11-S2 |
| **A.7.11 – Utilités de soutien** | Applicable | Cette politique, ISMS-IMP-A.7.4-5-11-S3 |

## Contrôles connexes

| Contrôle | Relation |
|----------|----------|
| **A.7.1-3** | Contrôle d'accès physique (prérequis pour la surveillance) |
| **A.7.8-9** | Emplacement des équipements et sécurité hors site |
| **A.5.19-23** | Évaluation de la sécurité physique du fournisseur cloud |
| **A.5.24-28** | Gestion des incidents pour les événements de sécurité physique |
| **A.5.30-8.13-14** | Intégration de la continuité des activités |
| **A.8.16** | Intégration SIEM pour la corrélation physique-logique |

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Surveillance de la sécurité physique** | Surveillance et détection continues des tentatives d'accès physique et des conditions environnementales |
| **Menace environnementale** | Risques naturels ou anthropiques susceptibles d'endommager les installations (incendie, inondation, températures extrêmes, événements sismiques) |
| **Utilités de soutien** | Services d'infrastructure nécessaires au fonctionnement des installations (alimentation électrique, refroidissement, télécommunications) |
| **Niveau de criticité des installations** | Classification des installations selon l'impact sur les activités et le niveau de protection requis |
| **Redondance N+1** | Configuration dans laquelle une unité supplémentaire est disponible au-delà des exigences minimales |
| **Registre des lacunes** | Liste documentée des déficiences de contrôle avec suivi de la remédiation |
| **SOC 2 Type II** | Rapport d'audit de contrôle des organisations de services démontrant l'efficacité des contrôles dans le temps |

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.7.4-5-11 v1.0)
- ✅ Signatures d'approbation du RSSI, Responsable des installations, Direction générale
- ✅ Exigences de surveillance de la sécurité physique documentées (Énoncés de politique)
- ✅ Exigences de protection environnementale documentées (Énoncés de politique)
- ✅ Exigences de résilience des utilités documentées (Énoncés de politique)
- ✅ Niveaux de criticité des installations définis (Niveaux de criticité des installations)
- ✅ Rôles et responsabilités attribués (Rôles et responsabilités)
- ✅ Méthodologie de notation de la conformité documentée (Gouvernance et conformité)
- ✅ Processus de remédiation des lacunes documenté (Remédiation des lacunes)

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

**Référentiel des preuves et génération** :

| Type de preuve | Emplacement dans le référentiel | Méthode de génération | Responsable | Conservation |
|----------------|--------------------------------|----------------------|-------------|-------------|
| Classeur de surveillance physique | [Plateforme GRC] – Module sécurité physique | Collecte automatisée mensuelle via ISMS-IMP-A.7.4-5-11-S1 | Responsable opérations sécurité | 3 ans |
| Évaluation de la protection environnementale | [Plateforme GRC] – Module sécurité physique | Évaluation trimestrielle via ISMS-IMP-A.7.4-5-11-S2 | Responsable des installations | 3 ans |
| Évaluation de la résilience des utilités | [Plateforme GRC] – Module sécurité physique | Tests trimestriels via ISMS-IMP-A.7.4-5-11-S3 | Responsable des installations | 3 ans |
| Registre des lacunes de sécurité physique | [Plateforme GRC] – Registre des risques | Suivi continu, révision mensuelle | Responsable opérations sécurité | Actif + 2 ans |
| Journaux de contrôle d'accès | [Système de contrôle d'accès physique] | Journalisation automatique | Opérations sécurité | 12 mois |
| Enregistrements CCTV | [Système de gestion vidéo] | Enregistrement continu | Opérations sécurité | 30-90 jours selon politique |
| Données de surveillance environnementale | [GTB/Système de surveillance environnementale] | Données de capteurs en continu | Responsable des installations | 12 mois |
| Dossiers de tests des utilités | [GMAO/Système de maintenance] | Selon le calendrier de tests | Responsable des installations | 5 ans |
| Dossiers d'exceptions | [Plateforme GRC] – Registre des exceptions | Selon les demandes d'exception | RSSI | Actif + 2 ans |

**Accessibilité des preuves** : Toutes les preuves DOIVENT être accessibles aux auditeurs sur demande dans les 2 jours ouvrables.

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date à définir] |
| **Responsable des installations** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de [Organisation] en matière de sécurité de l'infrastructure physique. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.7.4-5-11 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
