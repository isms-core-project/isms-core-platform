<!-- ISMS-CORE:REF:ISMS-REF-PCI-DSS-FR-pci-dss-requirements-reference:framework:REF:pci-dss -->
**ISMS-REF-PCI-DSS — Référence des exigences de la Norme de Sécurité des Données de l'Industrie des Cartes de Paiement (PCI DSS)**
**Exigences de sécurité des données de paiement par carte (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des exigences PCI DSS |
| **Type de document** | Interne — Référence technique (Non-SMSI) |
| **Identifiant du document** | ISMS-REF-PCI-DSS |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur Général (PDG) |
| **Approuvé par** | RSSI (Référence technique — Aucune approbation de la Direction générale requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Équipe Sécurité des Paiements | Référence technique initiale pour PCI DSS v4.0.1 |

**Cycle de révision** : Annuel (ou lors de mises à jour des versions PCI DSS)
**Prochaine date de révision** : [Date + 12 mois]
**Approbateurs** : RSSI / Responsable Sécurité des Paiements (référence technique, aucune approbation SMSI requise)

**Distribution** : Équipe de traitement des paiements, RSSI, Conformité, Opérations informatiques (pour les organisations traitant des cartes de paiement)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement.

- Ce document ne fait PAS partie du Système de Management de la Sécurité de l'Information (SMSI).
- Ce document ne définit PAS d'exigences obligatoires à moins que [Organisation] ne traite des cartes de paiement.
- Ce document n'établit PAS d'exigences contraignantes, de délais, de KPI ou de SLA pour les entités ne traitant pas de cartes.
- Ce document n'impose PAS l'adoption des exigences PCI DSS aux organisations ne traitant pas de cartes de paiement.
- Ce document ne remplace ni n'étend aucune politique du SMSI.

**Détermination de l'applicabilité** :
Les exigences PCI DSS s'appliquent UNIQUEMENT SI [Organisation] :

- Stocke, traite ou transmet des données du titulaire de carte (DTC)
- A accès à l'Environnement des Données du Titulaire de Carte (EDTC)
- Est un commerçant acceptant les paiements par carte de crédit/débit
- Est un prestataire ou processeur de services de paiement
- Est désignée par les marques de paiement (Visa, Mastercard, etc.) comme devant être conforme

Pour toutes les autres organisations, ce document sert uniquement de :

- Référence technique pour les exigences PCI DSS potentielles
- Contexte pour le développement commercial vers le traitement des paiements
- Sensibilisation aux normes de sécurité des cartes de paiement
- **Ce document ne doit pas être utilisé comme preuve d'audit à moins que [Organisation] ne soit conforme à PCI DSS**

L'utilisation de ce document n'implique pas l'applicabilité de PCI DSS, des obligations de conformité ou un statut de traitement des cartes de paiement.

**Déclaration de positionnement critique** :
Ce document fournit intentionnellement des détails réglementaires au-delà de ce qui s'applique à la plupart des organisations. Son objectif est la sensibilisation uniquement pour les organisations susceptibles de devenir soumises à PCI DSS, ou qui fournissent des services aux commerçants ou aux processeurs de paiement. Aucune conclusion d'audit ne doit être tirée de la présence, de l'absence ou du statut de mise en œuvre de toute exigence PCI DSS énumérée ici, à moins que [Organisation] ne traite explicitement des cartes de paiement.

---

# Objet et périmètre du document

## Objet

Ce document fournit une vue d'ensemble technique des exigences de la Norme de Sécurité des Données de l'Industrie des Cartes de Paiement (PCI DSS) v4.0.1. Il vise à soutenir :

- La sensibilisation aux exigences PCI DSS pour les entités traitant des cartes de paiement
- La compréhension des 12 exigences PCI DSS regroupées en 6 objectifs de contrôle
- Le contexte pour les organisations envisageant d'accepter des cartes de paiement
- L'évaluation d'une applicabilité future potentielle
- La mise en correspondance des exigences PCI DSS avec les contrôles ISO 27001:2022

## Ce que ce document n'est PAS

Ce document ne :

- N'établit PAS d'exigences obligatoires pour les organisations ne traitant pas de cartes de paiement
- Ne définit PAS les obligations de conformité de [Organisation] (voir POL-00 pour l'applicabilité réglementaire)
- Ne crée PAS de critères d'audit à moins que [Organisation] ne traite des cartes de paiement
- Ne remplace PAS les orientations d'un Évaluateur de Sécurité Qualifié (QSA)
- Ne constitue PAS un avis juridique ou de conformité sur PCI DSS
- Ne couvre PAS toutes les variantes de Questionnaire d'Auto-Évaluation (SAQ)
- N'établit PAS de procédures de mise en œuvre ou de processus de validation

## Relation avec le SMSI

Ce document est une **référence technique non contraignante** SAUF si [Organisation] traite des cartes de paiement (telle que déterminée dans ISMS-POL-00 Section 3.4).

**Si [Organisation] traite DES cartes de paiement :**

- Les exigences PCI DSS deviennent Niveau 1 (Conformité obligatoire) selon POL-00
- Ce document fournit des orientations de mise en œuvre
- Les contrôles du SMSI doivent démontrer la conformité PCI DSS
- Une validation annuelle est requise (Rapport de Conformité ou Questionnaire d'Auto-Évaluation)

**Si [Organisation] ne traite PAS de cartes de paiement :**

- PCI DSS reste Niveau 3 (Référence informative) selon POL-00
- Ce document est fourni à titre de sensibilisation uniquement
- Aucune obligation de conformité PCI DSS n'existe
- Les contrôles du SMSI suivent uniquement ISO 27001:2022

## Organisation du contenu

Cette référence organise les exigences PCI DSS par :

- Applicabilité et niveaux de commerçants
- 12 exigences regroupées en 6 objectifs de contrôle
- Définition du périmètre de l'Environnement des Données du Titulaire de Carte (EDTC)
- Méthodes de validation (Rapport de Conformité vs. Questionnaire d'Auto-Évaluation)
- Mise en correspondance avec les contrôles de l'Annexe A de l'ISO 27001:2022
- Nouvelles exigences et calendriers de PCI DSS v4.0.1

---

# Aperçu et applicabilité de PCI DSS

## Qu'est-ce que PCI DSS ?

La **Norme de Sécurité des Données de l'Industrie des Cartes de Paiement (PCI DSS)** est une norme mondiale de sécurité de l'information conçue pour protéger les données des cartes de paiement.

**Organisme de gouvernance** : PCI Security Standards Council (PCI SSC)

- Fondé par les principales marques de paiement (Visa, Mastercard, American Express, Discover, JCB)
- Développe et maintient PCI DSS
- Certifie les Évaluateurs de Sécurité Qualifiés (QSA)

**Version actuelle** : **PCI DSS v4.0.1** (publiée en mars 2024)

- En vigueur : 31 mars 2024
- Période de transition depuis v3.2.1 terminée : 31 mars 2024
- Nouvelles exigences introduites progressivement jusqu'au 31 mars 2025

**Objectif** :

- Protéger les données du titulaire de carte contre le vol et la fraude
- Établir des exigences de sécurité minimales
- Standardiser les contrôles de sécurité dans l'ensemble de l'écosystème des paiements
- Réduire le risque de violations de données

## Qui doit se conformer à PCI DSS ?

**Toute organisation qui stocke, traite ou transmet des données du titulaire de carte** :

| Type d'entité | Description | Exemples |
|---------------|-------------|----------|
| **Commerçants** | Acceptent les cartes de paiement comme moyen de paiement | Détaillants, e-commerce, restaurants, hôtels |
| **Prestataires de services** | Traitent, stockent ou transmettent des DTC pour le compte des commerçants | Passerelles de paiement, processeurs, hébergeurs, services de sécurité gérés |
| **Établissements financiers** | Émettent des cartes de paiement ou acquièrent des transactions | Banques, coopératives de crédit, réseaux de paiement |
| **Fournisseurs de points de vente (PDV)** | Fournissent des systèmes ou applications de PDV | Éditeurs de logiciels PDV, fabricants de terminaux |

**Principe clé** : Si vous touchez aux données du titulaire de carte, PCI DSS s'applique.

## Niveaux de commerçants

Les marques de paiement (Visa, Mastercard, etc.) classifient les commerçants en niveaux selon le volume de transactions :

**Niveaux de commerçants Visa** :

| Niveau | Volume de transactions (annuel) | Exigence de validation |
|--------|----------------------------------|------------------------|
| **Niveau 1** | > 6 millions de transactions Visa | Rapport de Conformité (ROC) annuel par QSA + Analyses réseau trimestrielles |
| **Niveau 2** | 1 à 6 millions de transactions Visa | Questionnaire d'Auto-Évaluation (SAQ) annuel + Analyses réseau trimestrielles |
| **Niveau 3** | 20 000 à 1 million de transactions e-commerce Visa | SAQ annuel + Analyses réseau trimestrielles |
| **Niveau 4** | < 20 000 transactions e-commerce Visa OU < 1 million de transactions Visa au total | SAQ annuel + Analyses réseau trimestrielles (selon la banque acquéreuse) |

**Note** : Les autres marques de paiement (Mastercard, Amex, Discover) ont des définitions de niveaux similaires mais légèrement différentes. Les organisations doivent vérifier les exigences avec leur banque acquéreuse.

## Données du Titulaire de Carte (DTC) et Données d'Authentification Sensibles (DAS)

**Données du Titulaire de Carte (DTC)** :

- **Numéro de Compte Principal (PAN)** : Le numéro de carte de paiement à 13–19 chiffres
- **Nom du Titulaire de Carte** : Nom figurant sur la carte
- **Date d'Expiration** : Date d'expiration de la carte
- **Code de Service** : Code à 3 chiffres sur la piste magnétique

**Données d'Authentification Sensibles (DAS)** — NE DOIVENT PAS être stockées après autorisation :

- **Données complètes de la piste magnétique** (Piste 1, Piste 2 ou données de puce équivalentes)
- **Code/Valeur de Vérification de Carte** (CVV/CVC/CVV2/CID — code à 3 ou 4 chiffres)
- **NIP/Code PIN** : Numéro d'Identification Personnel

**Règle critique** : Les DAS ne doivent JAMAIS être stockées après la finalisation de l'autorisation de la transaction, même si chiffrées.

## Environnement des Données du Titulaire de Carte (EDTC)

**Définition** : Les personnes, processus et technologies qui stockent, traitent ou transmettent des données du titulaire de carte ou des DAS, y compris les systèmes connectés.

**Composantes de l'EDTC** :

- **Systèmes dans le périmètre** : Systèmes qui stockent, traitent ou transmettent des DTC
- **Systèmes connectés** : Systèmes qui fournissent des services de sécurité aux systèmes dans le périmètre ou pouvant avoir un impact sur la sécurité de l'EDTC
- **Systèmes hors périmètre** : Systèmes correctement segmentés sans impact sur l'EDTC

**Stratégies de réduction du périmètre** :

- **Tokenisation** : Remplacer le PAN par un jeton non sensible
- **Chiffrement point à point (P2PE)** : Chiffrer au point d'entrée, déchiffrer en dehors de l'environnement du commerçant
- **Segmentation du réseau** : Isoler l'EDTC du reste du réseau
- **Réduction du stockage des données** : Ne pas stocker les DTC si inutile
- **Externalisation** : Utiliser des processeurs de paiement validés (réduit le périmètre du commerçant)

## Détermination de l'applicabilité

**PCI DSS s'applique à [Organisation] SI** :

| Critère | Statut | Preuve |
|---------|--------|--------|
| Stocke des données du titulaire de carte (PAN) | ⬜ Oui ⬜ Non | [Description du stockage] |
| Traite des données du titulaire de carte (PAN) | ⬜ Oui ⬜ Non | [Description du traitement] |
| Transmet des données du titulaire de carte (PAN) | ⬜ Oui ⬜ Non | [Description de la transmission] |
| A des systèmes connectés à l'EDTC | ⬜ Oui ⬜ Non | [Description des connexions] |
| Fournit des services aux entités traitant des DTC | ⬜ Oui ⬜ Non | [Type de prestataire de services] |

**Si UN « Oui » quelconque** : Les exigences PCI DSS sont **Niveau 1 (Conformité obligatoire)** selon POL-00 Section 3.4

**Si TOUS « Non »** : Les exigences PCI DSS restent **Niveau 3 (Référence informative)** selon POL-00

**Volume de transactions** (le cas échéant) : [Volume annuel] → Niveau de commerçant : [1/2/3/4]

---

# Structure PCI DSS — 6 objectifs de contrôle et 12 exigences

```
┌─────────────────────────────────────────────────────────────────┐
│              STRUCTURE PCI DSS v4.0.1                           │
├─────────────────────────────────────────────────────────────────┤
│  CONSTRUIRE ET MAINTENIR UN RÉSEAU ET DES SYSTÈMES SÉCURISÉS    │
│    1. Installer et maintenir des contrôles de sécurité réseau   │
│    2. Appliquer des configurations sécurisées à tous les        │
│       composants des systèmes                                   │
├─────────────────────────────────────────────────────────────────┤
│  PROTÉGER LES DONNÉES DU TITULAIRE DE CARTE                     │
│    3. Protéger les données de compte stockées                   │
│    4. Protéger les données du titulaire de carte avec une       │
│       cryptographie robuste lors de la transmission sur des     │
│       réseaux publics ouverts                                   │
├─────────────────────────────────────────────────────────────────┤
│  MAINTENIR UN PROGRAMME DE GESTION DES VULNÉRABILITÉS           │
│    5. Protéger tous les systèmes et réseaux contre les          │
│       logiciels malveillants                                    │
│    6. Développer et maintenir des systèmes et logiciels         │
│       sécurisés                                                 │
├─────────────────────────────────────────────────────────────────┤
│  METTRE EN ŒUVRE DES MESURES ROBUSTES DE CONTRÔLE DES ACCÈS     │
│    7. Restreindre l'accès aux données du titulaire de carte     │
│       selon les besoins métier                                  │
│    8. Identifier les utilisateurs et authentifier l'accès aux   │
│       composants des systèmes                                   │
│    9. Restreindre l'accès physique aux données du titulaire     │
│       de carte                                                  │
├─────────────────────────────────────────────────────────────────┤
│  SURVEILLER ET TESTER RÉGULIÈREMENT LES RÉSEAUX                 │
│   10. Journaliser et surveiller tous les accès aux composants   │
│       des systèmes et aux données du titulaire de carte         │
│   11. Tester régulièrement la sécurité des systèmes et réseaux  │
├─────────────────────────────────────────────────────────────────┤
│  MAINTENIR UNE POLITIQUE DE SÉCURITÉ DE L'INFORMATION           │
│   12. Soutenir la sécurité de l'information par des politiques  │
│       et programmes organisationnels                            │
└─────────────────────────────────────────────────────────────────┘
```

---

# Exigences détaillées

## Exigence 1 : Installer et maintenir des contrôles de sécurité réseau

**Objectif** : Les pare-feux et routeurs sont essentiels pour la sécurité du réseau, contrôlant le trafic entre les réseaux non fiables et l'EDTC.

**Sous-exigences clés** :

**1.1 Processus et mécanismes pour l'installation et la maintenance des contrôles de sécurité réseau**

- Processus des contrôles de sécurité réseau documentés
- Rôles et responsabilités attribués
- Révision et mise à jour annuelles

**1.2 Contrôles de sécurité réseau (CSR) configurés et maintenus**

- **1.2.1** : Standards de configuration pour les CSR définis et mis en œuvre
- **1.2.2** : Jeux de règles pare-feu de type « tout refuser, autoriser par exception »
- **1.2.3** : Trafic entrant et sortant restreint au nécessaire
- **1.2.4** : Règles documentées et justifiées (besoin métier)
- **1.2.5** : Règles pare-feu révisées au moins tous les 6 mois
- **1.2.6** : Modifications des jeux de règles CSR approuvées
- **1.2.7** : Configurations révisées pour les paramètres de sécurité

**1.3 Accès réseau vers et depuis l'EDTC restreint**

- **1.3.1** : Trafic entrant vers l'EDTC restreint
- **1.3.2** : Trafic sortant de l'EDTC autorisé
- **1.3.3** : CSR installés entre les réseaux sans fil et l'EDTC

**1.4 Connexions réseau entre réseaux fiables et non fiables contrôlées**

- **1.4.1** : CSR mis en œuvre pour contrôler le trafic
- **1.4.2** : Configurations alignées sur le principe « tout refuser »
- **1.4.3** : Mesures anti-usurpation mises en œuvre
- **1.4.4** : Les composants des systèmes ne divulguent pas les adresses IP internes
- **1.4.5** : Applications Web accessibles depuis Internet protégées (WAF ou équivalent) — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**

**1.5 Risques pour l'EDTC provenant des appareils informatiques pouvant se connecter à la fois aux réseaux non fiables et à l'EDTC gérés**

- **1.5.1** : Logiciel pare-feu personnel ou contrôles équivalents déployés

**Correspondance ISO 27001:2022** :

- A.8.20 : Sécurité des réseaux
- A.8.21 : Sécurité des services réseau
- A.8.22 : Cloisonnement des réseaux
- A.8.23 : Filtrage Web

---

## Exigence 2 : Appliquer des configurations sécurisées à tous les composants des systèmes

**Objectif** : Les acteurs malveillants ciblent les comptes et paramètres par défaut. Des configurations sécurisées doivent être appliquées.

**Sous-exigences clés** :

**2.1 Processus et mécanismes pour l'application de configurations sécurisées**

- Standards de configuration documentés
- Révisions régulières des configurations

**2.2 Composants des systèmes configurés et gérés de manière sécurisée**

- **2.2.1** : Paramètres par défaut des fournisseurs modifiés avant mise en production
- **2.2.2** : Mots de passe par défaut des fournisseurs modifiés (ou désactivés)
- **2.2.3** : Les fonctions principales nécessitant des niveaux de sécurité différents sont gérées par des composants séparés (p. ex. serveurs Web, serveurs de bases de données séparés)
- **2.2.4** : Services, protocoles et démons non sécurisés supprimés ou désactivés
- **2.2.5** : Services et paramètres de sécurité configurés
- **2.2.6** : Paramètres de sécurité des systèmes configurés pour prévenir les abus
- **2.2.7** : Accès administratif non sur console chiffré avec une cryptographie robuste

**2.3 Environnements sans fil configurés et gérés de manière sécurisée**

- **2.3.1** : Paramètres par défaut sans fil des fournisseurs modifiés
- **2.3.2** : Réseaux sans fil sécurisés avec une cryptographie robuste (WPA2/WPA3)

**Correspondance ISO 27001:2022** :

- A.8.9 : Gestion des configurations
- A.8.19 : Installation de logiciels sur des systèmes en exploitation
- A.8.1 : Terminaux des utilisateurs

---

## Exigence 3 : Protéger les données de compte stockées

**Objectif** : Les données du titulaire de carte stockées constituent une cible principale. Des méthodes de protection doivent être en place.

**Sous-exigences clés** :

**3.1 Processus et mécanismes pour protéger les données de compte stockées**

- Politiques de conservation et d'élimination des données
- Documentation des emplacements de stockage des DTC

**3.2 Stockage des données de compte réduit au minimum**

- **3.2.1** : Stockage des données de compte minimisé
- Les politiques de conservation des données limitent la quantité stockée et la durée de conservation

**3.3 Données d'Authentification Sensibles (DAS) non stockées après autorisation**

- **3.3.1** : DAS non conservées après autorisation — **RÈGLE CRITIQUE**
- **3.3.2** : DAS rendues irrécupérables si stockées avant autorisation
- **3.3.3** : PAN non affichés quand inutile (masquage)

**3.4 Accès aux affichages du PAN complet restreint**

- **3.4.1** : PAN masqué à l'affichage (6 premiers et 4 derniers chiffres au maximum)
- **3.4.2** : Contrôles techniques imposant le masquage — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**

**3.5 Numéro de Compte Principal (PAN) sécurisé partout où il est stocké**

- **3.5.1** : PAN rendu illisible (chiffrement, troncature, hachage, tokenisation)
- **3.5.1.1** : Les hachages utilisent un hachage avec clé (HMAC) et la clé est sécurisée — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **3.5.1.2** : PAN sécurisés avec chiffrement au niveau du disque ou de la partition — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **3.5.1.3** : Cryptopériodes définies et mises en œuvre

**3.6 Clés cryptographiques utilisées pour protéger les données de compte stockées sécurisées**

- **3.6.1** : Procédures de gestion des clés définies et mises en œuvre
- **3.6.2** : Clés stockées de manière sécurisée (moins d'emplacements, stockage chiffré)
- **3.6.3** : Gestion des clés limitée à un petit nombre de dépositaires
- **3.6.4** : Gestion des clés cryptographiques ayant atteint la fin de leur cryptopériode
- **3.6.5** : Accusé de réception des dépositaires de clés
- **3.6.6** : Distribution sécurisée des clés cryptographiques
- **3.6.7** : Prévention de la substitution non autorisée des clés
- **3.6.8** : Exigence pour les dépositaires de clés de reconnaître formellement la compréhension de leurs responsabilités

**3.7 Là où la cryptographie est utilisée pour protéger les données de compte stockées, des processus et procédures de gestion des clés sont mis en œuvre**

- **3.7.1** : Politiques et procédures de gestion des clés maintenues
- **3.7.2** : Gestion des clés cryptographiques
- **3.7.3** : Processus de révocation des clés
- **3.7.4** : Retrait ou destruction des clés
- **3.7.5** : Changement des clés lorsque l'intégrité est compromise
- **3.7.6** : Partages de clés stockés de manière sécurisée (pour la gestion manuelle des clés)
- **3.7.7** : Prévention de la substitution non autorisée
- **3.7.8** : Les dépositaires de clés reconnaissent formellement leurs responsabilités
- **3.7.9** : Inventaire matériel et logiciel des appareils cryptographiques — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**

**Correspondance ISO 27001:2022** :

- A.8.24 : Utilisation de la cryptographie
- A.8.10 : Suppression de l'information
- A.8.11 : Masquage des données

---

## Exigence 4 : Protéger les données du titulaire de carte avec une cryptographie robuste lors de la transmission

**Objectif** : Les données du titulaire de carte transmises sur des réseaux publics doivent être chiffrées.

**Sous-exigences clés** :

**4.1 Processus et mécanismes pour protéger les données du titulaire de carte avec une cryptographie robuste lors de la transmission**

- Inventaire des points de transmission des DTC
- Politiques et procédures de cryptographie

**4.2 PAN protégé avec une cryptographie robuste lors de la transmission**

- **4.2.1** : Une cryptographie robuste et des protocoles de sécurité protègent le PAN lors de la transmission sur des réseaux publics ouverts
- **4.2.1.1** : Inventaire des clés et certificats de confiance — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **4.2.2** : PAN non envoyé via les technologies de messagerie des utilisateurs finaux

**Correspondance ISO 27001:2022** :

- A.8.24 : Utilisation de la cryptographie
- A.5.14 : Transfert de l'information

**Standards de chiffrement** :

- TLS 1.2 minimum (TLS 1.3 préféré)
- Suites de chiffrement robustes (aucun algorithme obsolète)
- Pas de SSL, ni de versions TLS anciennes

---

## Exigence 5 : Protéger tous les systèmes et réseaux contre les logiciels malveillants

**Objectif** : Les logiciels malveillants exploitent les vulnérabilités. Des protections anti-malware doivent être déployées.

**Sous-exigences clés** :

**5.1 Processus et mécanismes pour protéger tous les systèmes et réseaux contre les logiciels malveillants**

- Plan de déploiement des solutions anti-malware
- Mises à jour et révisions régulières

**5.2 Les logiciels malveillants sont prévenus, détectés et traités**

- **5.2.1** : Solutions anti-malware déployées sur tous les systèmes (couramment affectés par les logiciels malveillants)
- **5.2.2** : Mécanismes anti-malware maintenus (à jour, en fonctionnement, journalisant)
- **5.2.3** : Mécanismes anti-malware ne pouvant être désactivés ou modifiés

**5.3 Les mécanismes anti-hameçonnage protègent les utilisateurs contre les attaques de hameçonnage**

- **5.3.1** : Processus mis en œuvre pour détecter et protéger le personnel contre les attaques de hameçonnage
- **5.3.2** : Mécanismes anti-hameçonnage maintenus et périodiquement évalués — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **5.3.3** : Mécanismes anti-hameçonnage protégeant contre les menaces — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**

**5.4 Les mécanismes et processus anti-malware sont actifs et maintenus**

- **5.4.1** : Journaux anti-malware conservés et révisés

**Correspondance ISO 27001:2022** :

- A.8.7 : Protection contre les logiciels malveillants
- A.5.7 : Renseignements sur les menaces

---

## Exigence 6 : Développer et maintenir des systèmes et logiciels sécurisés

**Objectif** : Les vulnérabilités dans les systèmes et logiciels permettent aux attaquants de compromettre les DTC.

**Sous-exigences clés** :

**6.1 Processus et mécanismes pour développer et maintenir des systèmes et logiciels sécurisés**

- Cycle de développement sécurisé
- Procédures de contrôle des changements

**6.2 Logiciels personnalisés et sur mesure développés de manière sécurisée**

- **6.2.1** : Logiciels personnalisés et sur mesure développés de manière sécurisée
- **6.2.2** : Personnel de développement de logiciels formé aux pratiques de codage sécurisé
- **6.2.3** : Revues de code pour les logiciels personnalisés et sur mesure avant mise en production — **[Mis à jour v4.0.1]**
- **6.2.4** : Techniques d'ingénierie logicielle en développement pour prévenir les vulnérabilités courantes

**6.3 Vulnérabilités de sécurité identifiées et traitées**

- **6.3.1** : Vulnérabilités de sécurité identifiées et évaluées selon des méthodologies acceptées par l'industrie
- **6.3.2** : Inventaire des logiciels personnalisés/sur mesure et des composants tiers
- **6.3.3** : Tous les composants et logiciels protégés contre les vulnérabilités connues (correctifs appliqués)
- **6.3.4** : Correctifs et mises à jour de sécurité pertinents examinés et déployés dans les délais définis

**Délais de correctifs** (6.3.4) :

- **Vulnérabilités critiques** : 30 jours maximum
- **Vulnérabilités élevées** : Selon la classification de risque organisationnel (généralement 30 à 90 jours)
- **Autres vulnérabilités** : Selon l'approche basée sur les risques

**6.4 Applications Web accessibles depuis Internet protégées contre les attaques**

- **6.4.1** : Applications Web accessibles depuis Internet protégées (solution technique automatisée, revue manuelle, WAF)
- **6.4.2** : Techniques d'intégrité des scripts de pages de paiement — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **6.4.3** : En-têtes HTTP inclus pour protéger contre les attaques

**6.5 Modifications de tous les composants des systèmes gérées de manière sécurisée**

- **6.5.1** : Modifications gérées selon les procédures de contrôle des changements
- **6.5.2** : Modifications des systèmes révisées pour l'impact sur la sécurité
- **6.5.3** : Modifications des logiciels personnalisés/sur mesure révisées avant déploiement
- **6.5.4** : Données et comptes de test supprimés avant mise en production
- **6.5.5** : Procédures de contrôle des changements documentées
- **6.5.6** : Données de production non utilisées pour les tests/le développement

**Correspondance ISO 27001:2022** :

- A.8.8 : Gestion des vulnérabilités techniques
- A.8.25 : Cycle de développement sécurisé
- A.8.26 : Exigences de sécurité des applications
- A.8.27 : Principes d'architecture et d'ingénierie des systèmes sécurisés
- A.8.28 : Codage sécurisé
- A.8.29 : Tests de sécurité dans le développement et l'acceptation
- A.8.30 : Développement externalisé
- A.8.31 : Séparation des environnements de développement, de test et de production
- A.8.32 : Gestion des changements
- A.8.33 : Informations de test

---

## Exigence 7 : Restreindre l'accès aux données du titulaire de carte selon les besoins métier

**Objectif** : L'accès aux DTC doit être restreint à ceux qui en ont besoin dans le cadre de leur emploi.

**Sous-exigences clés** :

**7.1 Processus et mécanismes pour restreindre l'accès aux composants des systèmes et aux données du titulaire de carte**

- Politiques de contrôle des accès définies
- Rôles et responsabilités

**7.2 Accès aux composants des systèmes et aux données défini et attribué de manière appropriée**

- **7.2.1** : Accès accordé selon la classification et la fonction du poste (besoin de savoir)
- **7.2.2** : Accès attribué selon le principe du moindre privilège
- **7.2.3** : Privilèges requis approuvés par le personnel autorisé
- **7.2.4** : Droits d'accès révisés au moins une fois tous les 6 mois
- **7.2.5** : Comptes à privilèges attribués à un utilisateur spécifique — **[Mis à jour v4.0.1]**
- **7.2.6** : Tout accès des utilisateurs aux référentiels de DTC stockés restreint

**7.3 Accès aux composants des systèmes et aux données géré via des systèmes de contrôle des accès**

- **7.3.1** : Systèmes de contrôle des accès en place pour les composants des systèmes
- **7.3.2** : Systèmes de contrôle des accès configurés pour imposer les permissions (principe « tout refuser »)
- **7.3.3** : Systèmes de contrôle des accès configurés pour prévenir l'élévation de privilèges

**Correspondance ISO 27001:2022** :

- A.5.15 : Contrôle des accès
- A.5.18 : Droits d'accès
- A.8.2 : Droits d'accès à privilèges
- A.8.3 : Restriction de l'accès à l'information

---

## Exigence 8 : Identifier les utilisateurs et authentifier l'accès aux composants des systèmes

**Objectif** : L'authentification garantit que les utilisateurs sont bien ceux qu'ils prétendent être avant d'accéder aux systèmes.

**Sous-exigences clés** :

**8.1 Processus et mécanismes pour identifier les utilisateurs et authentifier l'accès**

- Politiques d'identification et d'authentification des utilisateurs

**8.2 Identification des utilisateurs et comptes associés gérés de manière stricte**

- **8.2.1** : Identifiant unique attribué avant que l'accès ne soit accordé
- **8.2.2** : Comptes partagés interdits (sauf approbation explicite)
- **8.2.3** : Comptes génériques utilisés uniquement si nécessaire (approuvés, contrôlés)
- **8.2.4** : Personnel des prestataires de services avec accès distant disposant d'identifiants uniques
- **8.2.5** : Comptes partagés des prestataires utilisent l'AMF — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **8.2.6** : Comptes d'applications et de systèmes gérés pour prévenir les abus
- **8.2.7** : Comptes utilisateurs ajoutés, supprimés ou modifiés dans les délais impartis
- **8.2.8** : Tentatives d'authentification invalides entraînant un verrouillage de compte (après 10 tentatives maximum)

**8.3 Authentification robuste pour les utilisateurs et administrateurs établie et gérée**

- **8.3.1** : AMF pour tous les accès dans l'EDTC
- **8.3.2** : AMF pour tous les accès au réseau de l'entité (distant et interne)
- **8.3.3** : Systèmes AMF configurés pour prévenir les abus
- **8.3.4** : AMF requise pour tous les accès administratifs
- **8.3.5** : AMF pour tous les accès à l'EDTC utilisant des facteurs dans deux catégories différentes — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **8.3.6** : AMF résistante au hameçonnage pour le personnel avec accès administratif — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **8.3.7** : AMF pour les comptes d'applications et de systèmes utilisés pour exécuter des commandes à privilèges — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **8.3.8** : AMF pour les prestataires de services avec accès distant aux systèmes de l'entité — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **8.3.9** : Authentification cryptographique robuste utilisée pour l'accès administratif non sur console
- **8.3.10** : Méthodes d'authentification des utilisateurs appropriées à l'environnement de l'entité

**8.5 Mots de passe et phrases de passe satisfaisant aux exigences minimales de robustesse**

- **8.5.1** : Mots de passe/phrases de passe minimum 12 caractères (ou 8 si le système ne supporte pas 12) — **[Mis à jour v4.0.1]**

**8.6 Utilisation des comptes d'applications et de systèmes et des facteurs d'authentification associés gérée de manière stricte**

- **8.6.1** : Comptes d'applications et de systèmes sécurisés (pas de connexion interactive, ne peuvent pas être utilisés pour une connexion interactive)
- **8.6.2** : Mots de passe/phrases de passe modifiés lors d'une compromission suspectée ou connue
- **8.6.3** : Mots de passe/phrases de passe gérés pour prévenir les abus

**Correspondance ISO 27001:2022** :

- A.5.16 : Gestion des identités
- A.5.17 : Informations d'authentification
- A.8.5 : Authentification sécurisée

---

## Exigence 9 : Restreindre l'accès physique aux données du titulaire de carte

**Objectif** : L'accès physique aux systèmes et médias contenant des DTC doit être contrôlé.

**Sous-exigences clés** :

**9.1 Processus et mécanismes pour restreindre l'accès physique aux données du titulaire de carte**

- Politiques et procédures de sécurité physique

**9.2 Contrôles d'accès physique gérant l'entrée dans les installations et systèmes contenant des données du titulaire de carte**

- **9.2.1** : Contrôles d'accès physique en place pour restreindre l'accès aux systèmes dans l'EDTC
- **9.2.2** : Contrôles d'accès logiques et physiques garantissant que seul le personnel autorisé a accès
- **9.2.3** : Accès physique du personnel révoqué immédiatement à la cessation d'emploi
- **9.2.4** : Procédures d'accès visiteurs et système de badges visiteurs
- **9.2.5** : Contrôles d'accès physique pour les points d'accès sans fil
- **9.2.6** : Journaux d'accès physique révisés au moins une fois tous les 3 mois
- **9.2.7** : Caméras vidéo ou mécanismes de contrôle d'accès surveillant les zones sensibles

**9.3 Accès physique pour le personnel et les visiteurs autorisé et géré**

- **9.3.1** : Visiteurs autorisés et escortés dans les zones contenant des DTC
- **9.3.2** : Système de badges visiteurs distinguant les visiteurs du personnel
- **9.3.3** : Badges visiteurs remis ou désactivés avant de quitter les locaux

**9.4 Médias contenant des données du titulaire de carte stockés, consultés, distribués et détruits de manière sécurisée**

- **9.4.1** : Médias contenant des DTC stockés dans un endroit sécurisé (sauvegardes hors site sécurisées)
- **9.4.2** : Médias classifiés selon leur sensibilité
- **9.4.3** : Médias envoyés par courrier sécurisé (suivi utilisé)
- **9.4.4** : Approbation de la direction pour les médias quittant la zone sécurisée
- **9.4.5** : Inventaire des médias au moins annuellement
- **9.4.6** : Médias détruits quand plus nécessaires (déchiquetage transversal, incinération, purge/démagnétisation des médias magnétiques)
- **9.4.7** : Médias contenant des DTC détruits quand plus nécessaires pour les activités ou raisons légales

**9.5 Appareils de Point d'Interaction (PDI) protégés contre la falsification et la substitution non autorisée**

- **9.5.1** : Appareils PDI protégés contre la falsification (joints inviolables, etc.)
- **9.5.2** : Procédures pour détecter et signaler la falsification/substitution
- **9.5.3** : Formation du personnel pour être conscient des tentatives de falsification/substitution

**Correspondance ISO 27001:2022** :

- A.7.1 : Périmètres de sécurité physique
- A.7.2 : Contrôle de l'accès physique
- A.7.3 : Sécurisation des bureaux, salles et installations
- A.7.4 : Surveillance de la sécurité physique
- A.7.7 : Bureau propre et écran propre
- A.7.8 : Emplacement et protection des équipements
- A.7.10 : Supports de stockage
- A.7.14 : Mise au rebut ou réutilisation sécurisée des équipements

---

## Exigence 10 : Journaliser et surveiller tous les accès aux composants des systèmes et aux données du titulaire de carte

**Objectif** : Les mécanismes de journalisation et la capacité à suivre les activités des utilisateurs sont essentiels pour prévenir, détecter ou minimiser l'impact d'une compromission des données.

**Sous-exigences clés** :

**10.1 Processus et mécanismes pour la journalisation et la surveillance de tous les accès aux composants des systèmes et aux données du titulaire de carte**

- Politiques de journalisation et de surveillance définies

**10.2 Journaux d'audit mis en œuvre pour soutenir la détection des anomalies et activités suspectes**

- **10.2.1** : Journaux d'audit activés et actifs pour les composants des systèmes
- **10.2.2** : Les journaux d'audit capturent : ID utilisateur, type d'événement, date/heure, succès/échec, origine, identité/nom des données/composants affectés

**10.3 Journaux d'audit protégés contre la destruction et les modifications non autorisées**

- **10.3.1** : Accès en lecture aux fichiers journaux limité aux personnes ayant un besoin professionnel
- **10.3.2** : Fichiers journaux protégés contre les modifications non autorisées
- **10.3.3** : Fichiers journaux sauvegardés rapidement vers un serveur de journaux centralisé sécurisé
- **10.3.4** : Surveillance de l'intégrité des fichiers ou logiciel de détection des changements utilisé sur les journaux d'audit

**10.4 Journaux d'audit révisés pour identifier les anomalies ou activités suspectes**

- **10.4.1** : Politiques et procédures de sécurité identifiant les anomalies et activités suspectes
- **10.4.1.1** : Mécanismes automatisés alertant le personnel en cas d'anomalies ou d'activités suspectes — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **10.4.2** : Journaux d'audit révisés au moins une fois par jour
- **10.4.3** : Exceptions et anomalies identifiées lors des révisions traitées

**10.5 Historique des journaux d'audit conservé et disponible pour analyse**

- **10.5.1** : Historique des journaux d'audit conservé pendant au moins 12 mois (minimum 3 mois immédiatement accessibles)

**10.6 Mécanismes de synchronisation temporelle soutenant des paramètres horaires cohérents sur tous les systèmes**

- **10.6.1** : Horloges des systèmes synchronisées via une technologie de synchronisation temporelle
- **10.6.2** : Technologies de synchronisation temporelle configurées de manière cohérente
- **10.6.3** : Serveurs de temps critiques acceptant l'heure de sources externes (Stratum 0 ou 1)

**10.7 Défaillances des systèmes de contrôle de sécurité critiques détectées, signalées et traitées rapidement**

- **10.7.1** : Exigence supplémentaire pour les prestataires de services uniquement — Défaillances détectées et signalées — **[Nouveau v4.0.1]**
- **10.7.2** : Exigence supplémentaire pour les prestataires de services uniquement — Défaillances traitées rapidement — **[Nouveau v4.0.1]**
- **10.7.3** : Exigence supplémentaire pour les prestataires de services uniquement — Défaillances incluant la restauration des fonctions de sécurité — **[Nouveau v4.0.1]**

**Correspondance ISO 27001:2022** :

- A.8.15 : Journalisation
- A.8.16 : Activités de surveillance

---

## Exigence 11 : Tester régulièrement la sécurité des systèmes et réseaux

**Objectif** : Des vulnérabilités sont découvertes en continu. Des tests réguliers identifient et vérifient que les contrôles sont en place.

**Sous-exigences clés** :

**11.1 Processus et mécanismes pour tester régulièrement la sécurité des systèmes et réseaux**

- Politiques et procédures de tests définies

**11.2 Points d'accès sans fil identifiés et surveillés**

- **11.2.1** : Points d'accès sans fil autorisés et non autorisés détectés
- **11.2.2** : IDS/IPS sans fil ou équivalent déployé

**11.3 Vulnérabilités externes et internes régulièrement identifiées, priorisées et traitées**

- **11.3.1** : Analyses de vulnérabilités internes réalisées au moins une fois tous les 3 mois
- **11.3.2** : Analyses de vulnérabilités externes réalisées au moins une fois tous les 3 mois (par un Fournisseur d'Analyses Approuvé - ASV)
- **11.3.3** : Tests d'intrusion externes et internes réalisés

**Tests d'intrusion (11.4)** :

- **11.4.1** : Méthodologie de tests d'intrusion définie et mise en œuvre
- **11.4.2** : Tests d'intrusion internes réalisés au moins une fois tous les 12 mois
- **11.4.3** : Tests d'intrusion externes réalisés au moins une fois tous les 12 mois
- **11.4.4** : Vulnérabilités exploitables trouvées lors des tests d'intrusion corrigées
- **11.4.5** : Contrôles de segmentation testés (si segmentation réseau utilisée pour le périmètre)
- **11.4.6** : Exigence supplémentaire pour les prestataires de services — tests d'intrusion après mise à niveau significative de l'infrastructure/application
- **11.4.7** : Prestataires de services multi-locataires soutenant les tests d'intrusion clients ou fournissant des preuves de tests — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**

**11.5 Contrôles de sécurité réseau en place et efficaces**

- **11.5.1** : Mécanismes de détection des changements déployés
- **11.5.2** : Mécanismes de détection des changements configurés pour alerter le personnel

**11.6 Modifications non autorisées sur les pages de paiement détectées et traitées**

- **11.6.1** : Mécanisme de détection des changements et de falsification déployé sur les pages de paiement — **[Mis à jour v4.0.1]**

**Correspondance ISO 27001:2022** :

- A.8.8 : Gestion des vulnérabilités techniques
- A.5.7 : Renseignements sur les menaces
- A.8.34 : Protection des systèmes d'information lors des tests d'audit

---

## Exigence 12 : Soutenir la sécurité de l'information par des politiques et programmes organisationnels

**Objectif** : Les politiques et procédures de sécurité établissent les attentes et guident le personnel dans ses activités quotidiennes.

**Sous-exigences clés** :

**12.1 Une politique globale de sécurité de l'information est établie et publiée**

- **12.1.1** : Politique de sécurité établie, documentée, communiquée
- **12.1.2** : Politique de sécurité révisée au moins annuellement et mise à jour au besoin
- **12.1.3** : Rôles et responsabilités pour la sécurité attribués
- **12.1.4** : La direction générale est responsable en dernier ressort de la protection des DTC

**12.2 Les politiques d'utilisation acceptable pour les technologies des utilisateurs finaux définies et mises en œuvre**

- **12.2.1** : Politique d'utilisation acceptable pour les technologies des utilisateurs finaux définie

**12.3 Les risques pour l'EDTC formellement identifiés, évalués et gérés**

- **12.3.1** : Analyse de risque ciblée réalisée au moins une fois tous les 12 mois
- **12.3.2** : Analyse de risque ciblée réalisée lors de changements significatifs
- **12.3.3** : Résultats de l'évaluation des risques révisés et documentés
- **12.3.4** : Programme de conformité PCI DSS confirmé opérationnel au moins trimestriellement

**12.4 Conformité PCI DSS gérée**

- **12.4.1** : Responsabilités pour la gestion de la conformité PCI DSS attribuées
- **12.4.2** : La direction générale maintient la sensibilisation et la surveillance

**12.5 Périmètre PCI DSS documenté et validé**

- **12.5.1** : Inventaire de tous les composants des systèmes dans le périmètre PCI DSS
- **12.5.2** : Détermination du périmètre au moins une fois tous les 12 mois
- **12.5.2.1** : Impact des changements sur le périmètre PCI DSS déterminé — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**
- **12.5.3** : Impact sur la sécurité des modifications des composants des systèmes déterminé

**12.6 Formation de sensibilisation à la sécurité est une activité continue**

- **12.6.1** : Programme de sensibilisation à la sécurité mis en œuvre
- **12.6.2** : Personnel complétant la formation de sensibilisation à l'embauche et au moins une fois tous les 12 mois
- **12.6.3** : Matériaux de formation du personnel référençant les politiques et procédures de sécurité correctes
- **12.6.3.1** : Personnel recevant une formation sur le hameçonnage et l'ingénierie sociale — **[Nouveau v4.0.1, Bonne pratique jusqu'au 31 mars 2025]**

**12.7 Personnel sélectionné pour réduire les risques liés aux menaces internes**

- **12.7.1** : Candidats potentiels sélectionnés avant embauche (vérifications des antécédents selon la loi locale)

**12.8 Risque pour les actifs informationnels associé aux relations avec les prestataires de services tiers (PST) géré**

- **12.8.1** : Liste des PST maintenue (incluant les services fournis)
- **12.8.2** : Accords écrits avec les PST incluant la reconnaissance de responsabilité
- **12.8.3** : Processus en place pour engager les PST (diligence raisonnable avant engagement)
- **12.8.4** : Programme pour surveiller le statut de conformité PCI DSS des PST
- **12.8.5** : Informations maintenues sur les exigences PCI DSS gérées par chaque PST

**12.9 Les prestataires de services tiers (PST) soutiennent la conformité PCI DSS de leurs clients**

- **12.9.1** : Les PST reconnaissent la responsabilité de la sécurité des DTC
- **12.9.2** : Les PST fournissent des informations aux clients sur demande

**12.10 Les incidents de sécurité suspectés et confirmés sont traités immédiatement**

- **12.10.1** : Plan de réponse aux incidents créé et maintenu
- **12.10.2** : Plan de réponse aux incidents testé au moins annuellement
- **12.10.3** : Personnel désigné et formé pour la réponse aux incidents
- **12.10.4** : Systèmes d'alertes et de surveillance en place
- **12.10.5** : Systèmes de détection/prévention des intrusions surveillant tout le trafic dans l'EDTC
- **12.10.6** : Mécanismes de détection des changements surveillant les journaux d'audit
- **12.10.7** : Procédures de réponse aux incidents incluant : (i) rôles/responsabilités, (ii) stratégie de communication, (iii) procédures spécifiques, (iv) procédures de reprise d'activité, (v) processus de sauvegarde des données, (vi) exigences légales, (vii) investigation numérique

**Correspondance ISO 27001:2022** :

- A.5.1 : Politiques de sécurité de l'information
- A.5.36 : Conformité aux politiques, règles et normes pour la sécurité de l'information
- A.6.3 : Sensibilisation, éducation et formation à la sécurité de l'information
- A.5.24–5.28 : Gestion des incidents
- A.5.19–5.23 : Relations avec les fournisseurs
- Clause 6.1.2–6.1.3 : Évaluation et traitement des risques

---

# Nouvelles exigences et exigences mises à jour de PCI DSS v4.0.1

## Calendrier de mise en œuvre progressive

**PCI DSS v4.0** a introduit de nouvelles exigences progressivement :

| Catégorie d'exigence | Date d'application | Statut |
|---------------------|--------------------|--------|
| **Toutes les exigences v3.2.1 existantes** | 31 mars 2024 | Obligatoire |
| **Nouvelles exigences — Dates futures** | 31 mars 2024 – 31 mars 2025 | Bonne pratique |
| **Toutes les exigences v4.0.1** | 31 mars 2025 | Obligatoire |

## Nouvelles exigences clés (effectives au 31 mars 2025)

**Extension de l'authentification multi-facteurs** :

- 8.3.5 : L'AMF doit utiliser des facteurs de deux catégories différentes (ce que vous savez, avez, êtes)
- 8.3.6 : AMF résistante au hameçonnage pour l'accès administratif
- 8.3.7 : AMF pour les comptes d'applications/systèmes à privilèges
- 8.3.8 : AMF pour l'accès distant des prestataires de services

**Authentification renforcée** :

- 8.5.1 : Mots de passe minimum 12 caractères (précédemment 7)

**Améliorations cryptographiques** :

- 3.5.1.1 : Hachages avec clé (HMAC) requis pour le hachage du PAN
- 3.5.1.2 : Chiffrement disque/partition avec séparation de la gestion des clés
- 3.7.9 : Inventaire matériel/logiciel des appareils cryptographiques
- 4.2.1.1 : Inventaire des clés et certificats de confiance

**Sécurité des applications Web** :

- 1.4.5 : CSR entre Internet et les applications Web (WAF ou équivalent)
- 6.4.2 : Techniques d'intégrité des scripts de pages de paiement (CSP, SRI, etc.)
- 11.6.1 : Détection de falsification pour les pages de paiement renforcée

**Anti-hameçonnage** :

- 5.3.2 : Mécanismes anti-hameçonnage maintenus et évalués
- 5.3.3 : Contrôles techniques anti-hameçonnage mis en œuvre
- 12.6.3.1 : Formation du personnel sur le hameçonnage et l'ingénierie sociale

**Journalisation et surveillance** :

- 10.4.1.1 : Alertes automatisées pour les anomalies/activités suspectes
- 10.7.1–10.7.3 : Détection et réponse aux défaillances des contrôles de sécurité critiques (prestataires de services)

**Périmètre et gestion des risques** :

- 12.3.4 : Confirmation trimestrielle du programme de conformité PCI DSS opérationnel
- 12.5.2.1 : Détermination de l'impact des changements sur le périmètre PCI DSS

**Exigences pour les prestataires de services** :

- 11.4.7 : Prestataires multi-locataires soutenant les tests d'intrusion clients

---

# Validation et conformité

## Méthodes de validation

**Rapport de Conformité (ROC)** :

- Requis pour : Commerçants Niveau 1, prestataires de services
- Réalisé par : Évaluateur de Sécurité Qualifié (QSA)
- Fréquence : Annuelle
- Livrable : Rapport de conformité détaillé (300+ pages)

**Questionnaire d'Auto-Évaluation (SAQ)** :

- Requis pour : Commerçants Niveaux 2–4 (selon les canaux de paiement)
- Réalisé par : Évaluation interne (ou QSA optionnel)
- Fréquence : Annuelle
- Livrable : SAQ complété + Attestation de Conformité (ADC)

**Types de SAQ** :

| Type SAQ | Applicabilité | Exigences |
|----------|---------------|-----------|
| **SAQ A** | Sans présence de la carte, entièrement externalisé (pas de stockage, traitement, transmission électronique) | 22 exigences |
| **SAQ A-EP** | E-commerce, partiellement externalisé | 169 exigences |
| **SAQ B** | Machines à empreinte uniquement OU terminaux autonomes à ligne commutée | 41 exigences |
| **SAQ B-IP** | Terminaux IP autonomes connectés, pas de stockage électronique | 79 exigences |
| **SAQ C** | Systèmes d'application de paiement connectés à Internet, pas de stockage électronique | 158 exigences |
| **SAQ C-VT** | Terminal virtuel Web, pas de stockage électronique | 80 exigences |
| **SAQ P2PE** | Terminaux de paiement matériels utilisant une solution P2PE validée | 32 exigences |
| **SAQ D — Commerçant** | Tous les autres commerçants ne correspondant pas aux catégories ci-dessus | 337 exigences |
| **SAQ D — Prestataire de services** | Prestataires de services éligibles au SAQ | 337 exigences |

**Analyses réseau trimestrielles** :

- Requises pour : Toutes les entités avec des systèmes accessibles depuis Internet dans l'EDTC
- Réalisées par : Fournisseur d'Analyses Approuvé (ASV)
- Fréquence : Trimestrielle au minimum (également après des changements réseau significatifs)
- Critères de réussite : Aucune vulnérabilité notée 4,0 ou plus (CVSS)

## Attestation de Conformité (ADC)

Documentation requise soumise à la banque acquéreuse/marques de paiement :

- ROC ou SAQ complété
- Attestation de Conformité (ADC) — document signé
- Résultats des analyses ASV (4 analyses trimestrielles réussies)
- Tests de segmentation (si segmentation réseau utilisée pour le périmètre)

---

# Mise en correspondance ISO 27001:2022 — PCI DSS

## Matrice de correspondance des contrôles

| Exigence PCI DSS | Contrôle ISO 27001:2022 | Analyse des écarts |
|------------------|-------------------------|--------------------|
| 1. Contrôles de sécurité réseau | A.8.20–8.23 | PCI DSS : Règles pare-feu plus prescriptives |
| 2. Configurations sécurisées | A.8.9, A.8.19, A.8.1 | Aligné |
| 3. Protéger les DTC stockées | A.8.24, A.8.10, A.8.11 | **Spécifique PCI DSS** : Stockage DAS interdit, exigences de chiffrement strictes |
| 4. Protéger les DTC en transmission | A.8.24, A.5.14 | PCI DSS : TLS 1.2+ obligatoire, messagerie utilisateur finale interdite |
| 5. Protéger contre les logiciels malveillants | A.8.7, A.5.7 | PCI DSS : Ajoute les exigences anti-hameçonnage (v4.0) |
| 6. Développement sécurisé | A.8.8, A.8.25–8.33 | PCI DSS : Délais de correctifs prescriptifs (30 jours critique) |
| 7. Restreindre l'accès selon le besoin | A.5.15, A.5.18, A.8.2–8.3 | Aligné |
| 8. Identifier et authentifier | A.5.16–5.17, A.8.5 | **Spécifique PCI DSS** : AMF obligatoire, mots de passe 12 caractères |
| 9. Restreindre l'accès physique | A.7.1–7.4, A.7.7–7.8, A.7.10, A.7.14 | PCI DSS : Ajoute la protection des appareils PDI |
| 10. Journaliser et surveiller | A.8.15–8.16 | PCI DSS : Conservation 12 mois prescriptive, révision quotidienne |
| 11. Tester la sécurité | A.8.8, A.5.7, A.8.34 | **Spécifique PCI DSS** : Analyses ASV trimestrielles, tests d'intrusion annuels |
| 12. Politique de sécurité et programme | A.5.1, A.5.36, A.6.3, A.5.24–5.28, A.5.19–5.23 | PCI DSS : Ajoute analyse de risque ciblée, responsabilité de la direction |

## Écarts clés entre ISO 27001:2022 et PCI DSS

**Écart 1 : Exigences spécifiques aux données du titulaire de carte**

- ISO 27001 : Protection générale des données
- PCI DSS : Traitement explicite des DTC, interdiction de stockage des DAS, masquage du PAN

**Écart 2 : Contrôles techniques prescriptifs**

- ISO 27001 : Sélection de contrôles basée sur les risques
- PCI DSS : Contrôles obligatoires (pare-feux, chiffrement, AMF, anti-malware)

**Écart 3 : Fréquence des tests et de la validation**

- ISO 27001 : Aucune fréquence de tests imposée
- PCI DSS : Analyses ASV trimestrielles, tests d'intrusion annuels, validation annuelle de la conformité

**Écart 4 : Exigences spécifiques aux commerçants/prestataires de services**

- ISO 27001 : Pas d'orientations spécifiques aux commerçants
- PCI DSS : Niveaux de commerçants explicites, types de SAQ, obligations des prestataires de services

**Écart 5 : Responsabilité de la direction**

- ISO 27001 : Engagement de la direction
- PCI DSS : La direction générale est responsable en dernier ressort (12.1.4)

## Conformité PCI DSS avec une base ISO 27001

**Point clé** :
La certification ISO 27001:2022 fournit des contrôles de sécurité fondamentaux. Cependant, PCI DSS requiert :
1. **Périmètre EDTC** et documentation des flux de données du titulaire de carte
2. **Contrôles techniques prescriptifs** (AMF, standards de chiffrement, délais de correctifs)
3. **Validation régulière** (analyses ASV, tests d'intrusion, attestation annuelle de conformité)
4. **Exigences spécifiques de journalisation/surveillance** (conservation 12 mois, révision quotidienne)
5. **Exigences spécifiques aux commerçants** selon le volume de transactions

Les organisations dotées d'ISO 27001 nécessitent généralement **30 à 50 % d'effort supplémentaire** pour atteindre la conformité PCI DSS, principalement dans le périmètre EDTC, les contrôles prescriptifs et les processus de validation.

---

# Considérations de mise en œuvre

## Feuille de route de conformité PCI DSS

**Si [Organisation] traite des cartes de paiement** :

**Phase 1 : Périmètre (Mois 1–2)**

- Documenter les flux de données du titulaire de carte
- Définir l'Environnement des Données du Titulaire de Carte (EDTC)
- Identifier les systèmes dans le périmètre et les systèmes connectés
- Segmentation réseau le cas échéant
- Déterminer le niveau de commerçant et les exigences de validation

**Phase 2 : Évaluation des écarts (Mois 2–3)**

- Évaluer les contrôles actuels par rapport aux exigences PCI DSS
- Identifier les écarts et les priorités de remédiation
- Documenter les contrôles compensatoires si nécessaire
- Estimer le calendrier et le budget de remédiation

**Phase 3 : Remédiation (Mois 3–9)**

- **Écarts critiques en premier** : Exigence 3 (protéger les DTC stockées), Exigence 4 (protéger la transmission des DTC), Exigence 8 (AMF)
- **Haute priorité** : Exigences 1–2 (sécurité réseau, configurations), Exigence 6 (correctifs), Exigence 10 (journalisation)
- **Priorité moyenne** : Exigence 5 (anti-malware), Exigence 7 (contrôles d'accès), Exigence 9 (sécurité physique)
- **Administratif** : Exigence 11 (tests), Exigence 12 (politiques et procédures)

**Phase 4 : Préparation à la validation (Mois 9–11)**

- Évaluation interne de l'état de préparation
- Analyses ASV trimestrielles (4 analyses réussies requises)
- Tests d'intrusion internes
- Compilation de la documentation
- Engagement d'un QSA (si ROC requis)

**Phase 5 : Validation de la conformité (Mois 12)**

- Audit QSA (si Niveau 1) ou complétion du SAQ
- Analyse ASV finale
- Complétion de l'Attestation de Conformité (ADC)
- Soumission à la banque acquéreuse/marques de paiement

**Continu (Après conformité)** :

- Analyses ASV trimestrielles
- Revalidation annuelle de la conformité
- Révision continue de la surveillance et de la journalisation
- Gestion des changements avec évaluation de l'impact PCI
- Tests d'intrusion annuels et gestion des vulnérabilités

## Ressources nécessaires

**Personnel** :

- Responsable/Coordinateur de Conformité PCI
- QSA (externe, pour les commerçants Niveau 1)
- ASV (externe, pour les analyses trimestrielles)
- Équipe de sécurité interne (pare-feux, chiffrement, journalisation, correctifs)
- Équipe de développement d'applications (codage sécurisé, protection des pages de paiement)
- Équipe de sécurité physique (le cas échéant)

**Technologie** :

- Contrôles de sécurité réseau (pare-feux, IDS/IPS)
- Solutions de chiffrement (TLS pour la transmission, chiffrement disque/base de données)
- Plateforme d'authentification multi-facteurs
- SIEM ou journalisation centralisée
- Outils d'analyse des vulnérabilités
- Solutions anti-malware
- Surveillance de l'intégrité des fichiers (FIM)
- Synchronisation temporelle (NTP)
- Tokenisation des paiements ou P2PE (optionnel, pour la réduction du périmètre)

**Services externes** :

- QSA pour l'audit annuel (Niveau 1)
- ASV pour les analyses trimestrielles des vulnérabilités
- Services de tests d'intrusion (annuels)
- Fournisseur de destruction/élimination sécurisée (médias)
- Service d'investigation numérique (réponse aux incidents)

## Implications financières

Les coûts de conformité PCI DSS varient significativement selon le niveau de commerçant et la complexité de l'environnement :

**Commerçant Niveau 1 (> 6 M transactions/an)** :

- Audit QSA : 30 000 $ – 100 000 $ (annuel)
- Analyses ASV : 3 000 $ – 10 000 $ (annuel)
- Tests d'intrusion : 15 000 $ – 50 000 $ (annuel)
- Investissements technologiques : 100 000 $ – 500 000 $ (initial)
- Personnel : 1 à 3 ETP dédiés à la conformité PCI
- **Coût annuel total** : 200 000 $ – 1 000 000 $+

**Commerçants Niveaux 2–4 (< 6 M transactions/an)** :

- SAQ + ADC : 0 $ – 20 000 $ (si assistance QSA)
- Analyses ASV : 2 000 $ – 5 000 $ (annuel)
- Tests d'intrusion : 10 000 $ – 30 000 $ (annuel)
- Investissements technologiques : 50 000 $ – 200 000 $ (initial)
- Personnel : 0,5 à 1 ETP dédié à la conformité PCI
- **Coût annuel total** : 50 000 $ – 250 000 $

**Pénalités de non-conformité** :

- Amendes des marques de carte : 5 000 $ – 100 000 $ par mois (progressives)
- Amendes et frais de la banque acquéreuse
- Perte potentielle de la capacité d'accepter des cartes
- Coûts de violation : 200 $+ par enregistrement compromis
- Dommages réputationnels

---

# Défis courants et retours d'expérience

## Défis courants en matière de conformité PCI DSS

**Défi 1 : Expansion du périmètre**

- EDTC non correctement segmenté du reste du réseau
- Les réseaux « plats » font entrer l'environnement entier dans le périmètre
- Absence de diagrammes réseau et de documentation des flux de données

**Défi 2 : Stockage des Données d'Authentification Sensibles (DAS)**

- Stockage accidentel de CVV/CVV2, données de piste complètes, NIP/PIN
- Même le stockage chiffré des DAS est interdit après autorisation
- Les applications anciennes peuvent avoir un stockage de DAS caché

**Défi 3 : Mise en œuvre de l'authentification multi-facteurs**

- Sous-estimation de la complexité du déploiement de l'AMF (extension v4.0)
- Systèmes anciens ne supportant pas l'AMF
- Exceptions pour les « comptes de services » non correctement gérées

**Défi 4 : Lacunes de journalisation et de surveillance**

- Journaux non conservés pendant 12 mois
- Révision quotidienne des journaux non réalisée de manière cohérente
- SIEM non correctement configuré pour l'EDTC
- Problèmes de synchronisation temporelle (horloges désynchronisées)

**Défi 5 : Échecs des analyses ASV trimestrielles**

- Vulnérabilités non corrigées découvertes lors des analyses
- Gestion des faux positifs
- Fenêtres d'analyse non alignées sur les délais de soumission de conformité

**Défi 6 : Gestion des changements**

- Modifications de l'EDTC non évaluées pour l'impact PCI
- Segmentation réseau rompue suite aux changements
- Règles pare-feu ajoutées sans documentation/justification

**Défi 7 : Gestion des fournisseurs**

- Prestataires de services tiers non validés pour la conformité PCI
- Applications de paiement non validées PA-DSS ou PCI SSC
- Hébergeurs non conformes à PCI DSS

## Bonnes pratiques

**Pratique 1** : Réduire le périmètre via la tokenisation, P2PE ou l'externalisation
**Pratique 2** : Mettre en œuvre une segmentation réseau robuste (réduire le périmètre EDTC)
**Pratique 3** : Utiliser un QSA pour une analyse des écarts pré-évaluation (avant l'audit formel)
**Pratique 4** : Automatiser la surveillance de la conformité (conformité continue)
**Pratique 5** : Intégrer PCI DSS dans le SDLC pour les applications de paiement
**Pratique 6** : Réaliser des revues internes trimestrielles de l'état de préparation PCI
**Pratique 7** : Former tout le personnel aux bases de PCI DSS (pas seulement l'informatique)
**Pratique 8** : Utiliser la documentation des contrôles compensatoires lorsque les contrôles techniques ne sont pas réalisables
**Pratique 9** : Maintenir une documentation complète (diagrammes, politiques, preuves)
**Pratique 10** : Planifier les analyses ASV tôt (laisser du temps pour la remédiation avant les délais)

---

# Références et ressources

## Ressources officielles PCI DSS

**PCI Security Standards Council (PCI SSC)** :

- Site web : https://www.pcisecuritystandards.org/
- PCI DSS v4.0.1 : https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf
- Guide de référence rapide PCI DSS
- Questionnaires d'Auto-Évaluation (SAQ)
- Approche priorisée pour PCI DSS v4.0

**Ressources des marques de paiement** :

- **Visa** : https://usa.visa.com/support/small-business/security-compliance.html
- **Mastercard** : https://www.mastercard.us/en-us/business/overview/safety-and-security/security-recommendations.html
- **American Express** : https://www.americanexpress.com/us/merchant/data-security-operating-policy.html
- **Discover** : https://www.discoverglobalnetwork.com/en-us/resources/compliance

## Prestataires de services qualifiés

**Trouver un QSA (Évaluateur de Sécurité Qualifié)** :

- Répertoire QSA du PCI SSC : https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors

**Trouver un ASV (Fournisseur d'Analyses Approuvé)** :

- Répertoire ASV du PCI SSC : https://www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors

**Applications de paiement validées** :

- Applications validées PCI SSC : https://www.pcisecuritystandards.org/assessors_and_solutions/payment_applications

## Normes et cadres connexes

**Normes ISO** :

- ISO/IEC 27001:2022 : Systèmes de Management de la Sécurité de l'Information
- ISO/IEC 27002:2022 : Contrôles de sécurité de l'information

**Publications NIST** (référence informative) :

- NIST SP 800-53 : Contrôles de sécurité et de confidentialité
- NIST Cybersecurity Framework

**Orientations sectorielles** :

- OWASP Application Security : https://owasp.org/
- CIS Controls : https://www.cisecurity.org/controls

## Formation et certification

**Formation PCI SSC** :

- PCI Professional (PCIP) : Certification de niveau initial
- Internal Security Assessor (ISA) : Certification d'audit interne
- Qualified Security Assessor (QSA) : Certification d'auditeur externe

**Ressources en ligne** :

- PCI Guru : https://pciguru.wordpress.com/ (blog non officiel)
- PCI Compliance Guide : https://www.pcicomplianceguide.org/

---

# Annexe A : Liste de contrôle d'auto-évaluation de la conformité PCI DSS

Cette liste de contrôle fournit une couverture de haut niveau. Les organisations devraient utiliser les SAQ officiels pour une évaluation complète.

## Construire et maintenir un réseau sécurisé (Exigences 1–2)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Règles pare-feu documentées et justifiées | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Règles pare-feu révisées tous les 6 mois | ⬜ Oui ⬜ Non | | |
| Segmentation réseau entre l'EDTC et les autres réseaux | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Mots de passe par défaut des fournisseurs modifiés | ⬜ Oui ⬜ Non | | |
| Services inutiles désactivés | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Réseaux sans fil sécurisés (WPA2/WPA3) | ⬜ Oui ⬜ Non ⬜ N/A | | |

## Protéger les données du titulaire de carte (Exigences 3–4)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Stockage des DTC minimisé (uniquement si nécessaire) | ⬜ Oui ⬜ Non | | |
| Données d'Authentification Sensibles (DAS) NON stockées après autorisation | ⬜ Oui ⬜ Non | | |
| PAN masqué à l'affichage (6 premiers, 4 derniers chiffres max) | ⬜ Oui ⬜ Non | | |
| PAN chiffré ou tokenisé lors du stockage | ⬜ Oui ⬜ Non | | |
| Clés de chiffrement sécurisées et gérées | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| TLS 1.2+ utilisé pour la transmission des DTC sur des réseaux ouverts | ⬜ Oui ⬜ Non | | |
| PAN non envoyé via messagerie des utilisateurs finaux (e-mail, chat, SMS) | ⬜ Oui ⬜ Non | | |

## Maintenir un programme de gestion des vulnérabilités (Exigences 5–6)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Anti-malware déployé sur tous les systèmes (couramment affectés) | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Anti-malware à jour, en fonctionnement et journalisant | ⬜ Oui ⬜ Non | | |
| Mécanismes anti-hameçonnage déployés | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Correctifs de sécurité appliqués dans les 30 jours (vulnérabilités critiques) | ⬜ Oui ⬜ Non | | |
| Processus de gestion des vulnérabilités en place | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Pratiques de codage sécurisé pour les logiciels personnalisés | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Applications Web accessibles depuis Internet protégées (WAF ou équivalent) | ⬜ Oui ⬜ Non ⬜ N/A | | |

## Mettre en œuvre des mesures robustes de contrôle des accès (Exigences 7–9)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Accès accordé selon le besoin de savoir | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Droits d'accès révisés au moins tous les 6 mois | ⬜ Oui ⬜ Non | | |
| Identifiants utilisateurs uniques attribués à chaque personne | ⬜ Oui ⬜ Non | | |
| Comptes partagés interdits (sauf approbation) | ⬜ Oui ⬜ Non | | |
| AMF pour tous les accès à l'EDTC | ⬜ Oui ⬜ Non | | |
| AMF pour l'accès distant au réseau de l'entité | ⬜ Oui ⬜ Non | | |
| Mots de passe minimum 12 caractères | ⬜ Oui ⬜ Non | | |
| Verrouillage de compte après 10 tentatives de connexion infructueuses | ⬜ Oui ⬜ Non | | |
| Contrôles d'accès physique pour les systèmes EDTC | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Accès visiteurs contrôlé et journalisé | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Médias contenant des DTC détruits de manière sécurisée quand plus nécessaires | ⬜ Oui ⬜ Non | | |

## Surveiller et tester les réseaux (Exigences 10–11)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Journaux d'audit activés pour tous les composants | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Journaux d'audit révisés au moins une fois par jour | ⬜ Oui ⬜ Non | | |
| Journaux d'audit conservés pendant au moins 12 mois | ⬜ Oui ⬜ Non | | |
| Synchronisation temporelle mise en œuvre (NTP) | ⬜ Oui ⬜ Non | | |
| Points d'accès sans fil détectés (autorisés/non autorisés) | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Analyses de vulnérabilités internes tous les 3 mois | ⬜ Oui ⬜ Non | | |
| Analyses de vulnérabilités externes (ASV) tous les 3 mois — 4 analyses réussies | ⬜ Oui ⬜ Non | | |
| Tests d'intrusion internes au moins annuellement | ⬜ Oui ⬜ Non | | |
| Tests d'intrusion externes au moins annuellement | ⬜ Oui ⬜ Non | | |
| Mécanismes de détection des changements déployés (FIM) | ⬜ Oui ⬜ Non | | |

## Politique de sécurité de l'information (Exigence 12)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Politique de sécurité de l'information établie et publiée | ⬜ Oui ⬜ Non | | |
| Politique de sécurité révisée au moins annuellement | ⬜ Oui ⬜ Non | | |
| Politique d'utilisation acceptable pour les technologies des utilisateurs finaux | ⬜ Oui ⬜ Non | | |
| Analyse de risque ciblée réalisée au moins annuellement | ⬜ Oui ⬜ Non | | |
| Périmètre PCI DSS documenté et validé annuellement | ⬜ Oui ⬜ Non | | |
| Formation de sensibilisation à la sécurité complétée par tout le personnel (annuel) | ⬜ Oui ⬜ Non | | |
| Formation sur le hameçonnage et l'ingénierie sociale fournie | ⬜ Oui ⬜ Non | | |
| Vérifications des antécédents avant embauche | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Prestataires de services tiers validés pour la conformité PCI | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Plan de réponse aux incidents créé et testé annuellement | ⬜ Oui ⬜ Non | | |

---

# Annexe B : Modèle de diagramme de flux des données du titulaire de carte

Les organisations doivent créer un diagramme de flux de données détaillé montrant comment les DTC entrent, circulent et sortent de l'environnement.

**Éléments du modèle** :

```
[Client]
    ↓
[Canal de paiement : PDV / Web / Mobile / Téléphone]
    ↓
[Point d'entrée : Terminal de paiement / Formulaire Web / Passerelle de paiement]
    ↓
[Traitement : Application de paiement / Serveur]
    ↓
[Stockage : Base de données / Système de fichiers] ← (si stocké)
    ↓
[Transmission : Processeur / Acquéreur / Marque de paiement]
    ↓
[Sortie : Réponse d'autorisation / Règlement]
```

**Documentation requise** :

- Tous les systèmes qui stockent, traitent ou transmettent des DTC
- Zones réseau et segmentation
- Points de chiffrement des données (en transit et au repos)
- Politiques de conservation des données et procédures de suppression
- Connexions de tiers à l'EDTC

---

**FIN DE LA RÉFÉRENCE TECHNIQUE**

---

*Cette référence technique soutient les exigences potentielles de conformité PCI DSS telles que déterminées dans ISMS-POL-00. Toutes les déterminations d'applicabilité réglementaire et les exigences contraignantes sont définies dans ISMS-POL-00 et les documents de politique SMSI approuvés.*

*Pour les organisations NE TRAITANT PAS de cartes de paiement, ce document est fourni à titre de sensibilisation informative uniquement et ne crée PAS d'obligations de conformité.*

<!-- QA_VERIFIED: 2026-03-30 -->
