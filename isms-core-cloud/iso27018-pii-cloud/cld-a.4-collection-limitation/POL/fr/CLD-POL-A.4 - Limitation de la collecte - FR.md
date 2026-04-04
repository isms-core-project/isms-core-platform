<!-- ISMS-CORE:POLICY:CLD-POL-A.4-FR:cloud:POL:a.4 -->
**CLD-POL-A.4 — Limitation de la collecte**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Limitation de la collecte |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-POL-A.4 |
| **Auteur du document** | RSSI / Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Cloud** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / DPD | Politique initiale pour la mise en œuvre d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors d'un changement réglementaire ou de modèle de service significatif)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : RSSI / Responsable Sécurité Cloud
- Secondaire : Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection des données et protection des DCP)
- CLD-POL-A.3 (Légitimité et spécification des finalités)
- CLD-POL-A.5 (Minimisation des données)
- CLD-POL-A.6 (Limitation de l'utilisation, de la conservation et de la divulgation)
- ISO/IEC 27018:2025 Annex A, Section A.4 (Limitation de la collecte — principe)
- ISO/IEC 27701:2025 Contrôles A.2.4.2 (sous-traitant — fichiers temporaires) et A.2.4.3 (sous-traitant — retour, transfert ou élimination des DCP)
- RGPD Article 5(1)(c) (principe de minimisation des données) ; Article 28(3)(a) (traitement sur instruction uniquement)
- LPD suisse Article 6(2) (proportionnalité) ; Article 9 (obligations du sous-traitant)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en tant que sous-traitant de DCP en cloud public en matière de limitation de la collecte — spécifiquement l'obligation de traiter uniquement le minimum de DCP nécessaire à la prestation du service contractuel, et de gérer tout excédent de DCP collecté dans le cadre de la prestation du service — conformément à ISO/IEC 27018:2025 Annex A, Section A.4.

**Périmètre** : Toutes les DCP collectées, reçues ou autrement obtenues par [Organisation] dans le cadre de la prestation de services cloud aux responsables du traitement des DCP.

**Note sur le principe** : La Section A.4 opère au niveau des principes. Cette politique traduit ce principe en obligations opérationnelles spécifiques pour les services cloud de [Organisation]. Les méthodes techniques de minimisation des données — incluant l'anonymisation, la pseudonymisation et la gestion des fichiers temporaires — sont traitées dans CLD-POL-A.5.

---

# Périmètre et applicabilité

## ISO/IEC 27018:2025 — Section A.4

**Section A.4 — Limitation de la collecte (principe)**

La Section A.4 établit le principe qu'un sous-traitant de DCP en cloud public ne doit collecter que les DCP nécessaires au service contractuel, documenter ses pratiques de collecte et traiter rapidement tout excédent de DCP survenant dans le cadre de la prestation du service.

## Ce que cette politique ne couvre PAS

- Déterminer quelles DCP un responsable du traitement peut licitement collecter auprès des personnes concernées — c'est la responsabilité du responsable du traitement
- Les méthodes techniques d'anonymisation et d'effacement des fichiers temporaires — traitées dans CLD-POL-A.5

## Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per PRIV-POL-00) :

- **RGPD UE** : Article 5(1)(c) (minimisation des données — adéquates, pertinentes et limitées à ce qui est nécessaire) ; Article 28(3)(a) (le sous-traitant ne traite que sur instruction — pas de collecte excessive)
- **LPD suisse** : Article 6(2) (proportionnalité — le traitement des données personnelles doit être proportionné à la finalité)
- **ISO/IEC 27018:2025** : Principe de la Section A.4

---

# Dispositions de la politique : Limitation de la collecte (A.4)

## Collecte du minimum nécessaire

[Organisation] DOIT collecter, conserver ou autrement traiter uniquement le minimum de DCP nécessaire pour fournir le service cloud contractuel. [Organisation] NE DOIT PAS :

- Demander ou accepter des catégories de DCP du responsable du traitement des DCP au-delà de ce qui est nécessaire à la prestation du service
- Stocker des DCP dans des composants système, des journaux ou des bases de données opérationnelles au-delà de la nécessité opérationnelle du traitement
- Répliquer des DCP dans des environnements (développement, test, pré-production, production) à des fins autres que la prestation et la résilience du service sans autorisation explicite du responsable du traitement

## Documentation des pratiques de collecte

[Organisation] DOIT documenter les pratiques de collecte de DCP pour chaque service cloud, incluant :

- Les catégories de DCP collectées ou reçues durant la prestation du service
- La justification opérationnelle de chaque catégorie de DCP
- Les composants système, journaux et emplacements de stockage où des DCP peuvent être présentes
- Les périodes de conservation applicables à chaque type de collecte

Cette documentation DOIT être maintenue dans le système de gestion des documents SGSI (ou la plateforme GRC désignée), révisée annuellement et mise à jour lors de changements matériels à l'architecture du service. Le RSSI est le propriétaire désigné de la documentation des pratiques de collecte.

## DCP excédentaires

Lorsque [Organisation] détermine que des DCP ont été collectées qui dépassent le périmètre du service contractuel (ex. un responsable du traitement télécharge un jeu de données contenant des catégories de DCP au-delà du périmètre du service), [Organisation] DOIT :

1. Notifier le responsable du traitement des DCP de l'excédent de DCP dans les 3 jours ouvrables suivant l'identification
2. Convenir avec le responsable du traitement si les DCP excédentaires doivent être retournées ou supprimées de manière sécurisée
3. Compléter l'action convenue dans le délai convenu avec le responsable du traitement
4. Documenter l'événement et son résultat

## Environnements de développement et de test

[Organisation] DEVRAIT utiliser des données anonymisées ou synthétiques dans les environnements hors production chaque fois que cela est techniquement faisable, et DOIT traiter l'utilisation de DCP de production comme un dernier recours. Les DCP des environnements de production NE DOIVENT PAS être utilisées dans des environnements de développement, de test ou de pré-production sans autorisation écrite explicite du responsable du traitement des DCP. Lorsque l'autorisation du responsable du traitement est obtenue, le minimum nécessaire de DCP DOIT être utilisé, les mêmes contrôles de sécurité applicables en production DOIVENT s'appliquer (conformément à CLD-POL-A.11) et l'accès DOIT être limité au minimum de personnel requis pour la finalité spécifique.

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI / Responsable Sécurité Cloud** | Veille à ce que l'architecture du service collecte le minimum nécessaire de DCP ; maintient la documentation de collecte ; examine le périmètre de collecte lors de la conception et des modifications du service |
| **Délégué à la Protection des Données (DPD)** | Examine la documentation de collecte annuellement ; conseille sur les évaluations de proportionnalité ; surveille les événements de collecte excessive |
| **Prestation de services cloud / Ingénierie** | Met en œuvre une architecture de collecte minimale ; signale rapidement les événements de collecte excessive au RSSI et au DPD |
| **Responsable Juridique/Conformité** | Conseille sur les obligations de proportionnalité et de minimisation en vertu du RGPD et de la LPD |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Documentation des pratiques de collecte | Catégories de DCP documentées, justifications et emplacements par service | En cours + versions précédentes pendant 3 ans |
| Enregistrements de révision annuelle | Enregistrements signés des révisions annuelles des pratiques de collecte | 3 ans |
| Enregistrements d'événements de DCP excédentaires | Documentation de tout événement de DCP excédentaires, notifications des responsables du traitement et résolution | Durée du contrat + 3 ans |
| Enregistrements d'autorisation pour développement/test | Autorisations écrites des responsables du traitement pour toute utilisation de DCP de production dans des environnements hors production | Durée d'utilisation + 3 ans |

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-POL-A.4 doivent s'attendre à trouver :

- Des enregistrements de pratiques de collecte documentés pour chaque service cloud avec les catégories de DCP et les justifications
- Des preuves de révisions annuelles des pratiques de collecte
- Aucune catégorie de DCP dans les systèmes opérationnels dépassant le périmètre du service contractuel
- Tout événement de DCP excédentaires documenté avec notification du responsable du traitement et enregistrements de résolution
- Aucune DCP de production dans les environnements de développement ou de test sans autorisation documentée du responsable du traitement

---

<!-- QA_VERIFIED: 2026-04-04 -->
