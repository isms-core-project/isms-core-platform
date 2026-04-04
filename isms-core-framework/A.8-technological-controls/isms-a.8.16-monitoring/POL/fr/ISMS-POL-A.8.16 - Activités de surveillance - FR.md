<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.16-FR:framework:POL:a.8.16 -->
**ISMS-POL-A.8.16 – Activités de surveillance**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Activités de surveillance |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.16 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur des Systèmes d'Information (DSI)
- Revue opérationnelle : Responsable du SOC
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.8.15 (Journalisation)
- ISMS-POL-A.5.24-5.28 (Gestion des incidents)
- ISMS-IMP-A.8.16.1-UG/TG (Évaluation de l'infrastructure de surveillance)
- ISMS-IMP-A.8.16.2-UG/TG (Évaluation du référentiel et de la détection)
- ISMS-IMP-A.8.16.3-UG/TG (Évaluation de la couverture)
- ISMS-IMP-A.8.16.4-UG/TG (Évaluation de la gestion des alertes et de la réponse)
- ISO/IEC 27001:2022 Contrôle A.8.16

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière d'activités de surveillance pour détecter les comportements anormaux et les incidents potentiels de sécurité de l'information, conformément au Contrôle A.8.16 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les réseaux, systèmes et applications où la surveillance est techniquement faisable ; tous les utilisateurs (employés, contractants, comptes de service) ; et toutes les technologies de surveillance quel que soit le fournisseur ou le modèle de déploiement.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de surveillance. Cette politique établit QUELLE surveillance est requise, OÙ elle doit être mise en œuvre et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.16 (variantes UG/TG).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

**Philosophie** : Une surveillance efficace nécessite des référentiels documentés, des seuils mesurables, des procédures de réponse démontrées et des métriques d'efficacité quantifiables — pas seulement des tableaux de bord que personne ne lit ou des alertes que tout le monde ignore.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.16 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.16 — Activités de surveillance**

> *Les réseaux, les systèmes et les applications devraient être surveillés pour détecter les comportements anormaux et des mesures appropriées devraient être prises pour évaluer les incidents potentiels de sécurité de l'information.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les activités de surveillance visant à détecter les comportements anormaux et les incidents potentiels de sécurité par une observation systématique, l'établissement de référentiels, la détection des anomalies et l'intégration avec les processus de gestion des incidents.

---

# Exigences de surveillance

## Périmètre de surveillance

[Organisation] DOIT mettre en œuvre une surveillance de sécurité sur :

**Infrastructure réseau** :

- Pare-feu et zones de sécurité réseau
- Passerelles VPN et concentrateurs d'accès distant
- Équipements de segmentation réseau (commutateurs de cœur, routeurs)
- Périmètre Internet et zones démilitarisées (DMZ)
- Frontières du réseau interne (latéral)

**Systèmes et serveurs** :

- Contrôleurs de domaine et systèmes d'identité
- Serveurs de production critiques (Niveau 1)
- Serveurs d'application exposés à Internet
- Infrastructure de base de données contenant des données Confidentielles/Restreintes
- Systèmes de sauvegarde et de reprise après sinistre

**Terminaux** :

- Postes de travail d'entreprise (via agents EDR)
- Appareils mobiles gérés (via telémétrie MDM)
- Postes de travail à accès privilégié (PAW)

**Environnements cloud** :

- Console d'administration cloud (AWS, Azure, GCP)
- Services IaaS et PaaS critiques
- Applications SaaS avec données Confidentielles/Restreintes
- Activité IAM cloud (création/modification/suppression de comptes)

**Applications** :

- Applications web exposées à Internet
- API exposées à l'externe
- Applications traitant des données Restreintes

## Référentiels de comportement normal

[Organisation] DOIT établir des référentiels documentés pour définir le comportement normal avant de déployer la surveillance des anomalies.

**Référentiels obligatoires** :

- **Authentification** : Horaires de connexion typiques, sources géographiques normales, volumes de tentatives normaux par système
- **Réseau** : Volumes de trafic de référence par segment, protocoles attendus, destinations normales
- **Accès aux ressources** : Volumes d'accès normaux par rôle/utilisateur, schémas d'accès aux données
- **Privilèges** : Fréquence normale d'élévation de privilèges, durée des sessions administratives

**Processus d'établissement des référentiels** :

1. Collecte des données pendant une période d'observation (minimum 30 jours)
2. Calcul des métriques statistiques de référence (moyenne, écart-type, percentiles)
3. Documentation des valeurs de référence avec dates et contexte
4. Définition des seuils d'alerte (par ex. ≥ 3σ au-dessus de la moyenne)
5. Révision et mise à jour des référentiels trimestriellement ou lors de changements significatifs

**Vérification des référentiels** : Les référentiels NE DOIVENT PAS être des suppositions — ils DOIVENT être basés sur des données mesurées et documentées. La date d'établissement et la période d'observation DOIVENT être documentées pour chaque référentiel.

## Capacités de détection des anomalies

[Organisation] DOIT mettre en œuvre des capacités de détection couvrant :

**Détection basée sur les signatures** :

- Indicateurs de compromission (IoC) connus : hachages de logiciels malveillants, adresses IP malveillantes, domaines
- Patterns d'attaques connus (TTPs MITRE ATT&CK)
- Règles de détection basées sur les journaux (corrélation SIEM)
- Mises à jour quotidiennes des renseignements sur les menaces

**Détection basée sur les anomalies** :

- Écarts statistiques par rapport aux référentiels établis
- Comportements inhabituels pour l'utilisateur ou le système (UEBA si disponible)
- Analyses de la volumétrie des données (transferts anormalement importants)
- Détection des accès à des heures inhabituelles ou depuis des emplacements inhabituels

**Catégories de détection prioritaires** :

| Catégorie | Exemples d'indicateurs |
|-----------|------------------------|
| **Compromission des identifiants** | Multiples échecs de connexion puis succès, connexion depuis une nouvelle géolocalisation |
| **Escalade de privilèges** | Accès admin en dehors des heures normales, élévation de privilèges sur plusieurs systèmes |
| **Mouvement latéral** | Connexions réseau inhabituelles entre systèmes internes, utilisation de protocoles d'administration (PSExec, WMI) |
| **Exfiltration de données** | Gros transferts vers des destinations externes, utilisation de canaux inhabituels |
| **Logiciel malveillant** | Processus inconnus, comportements de rançongiciel, beaconing vers des domaines C2 |
| **Abus de comptes de service** | Compte de service accédant à des ressources inhabituelles, connexions interactives |
| **Persistance** | Nouvelles tâches planifiées, nouvelles clés de registre, nouveaux services |

## Exigences d'infrastructure de surveillance

**Plateforme SIEM** :

[Organisation] DOIT maintenir une plateforme SIEM (Security Information and Event Management) centralisée :

- Collecte et corrélation de journaux de toutes les sources dans le périmètre
- Capacité de recherche historique (au minimum sur la durée de conservation des journaux)
- Tableau de bord en temps réel pour le SOC
- Système de gestion des alertes et des cas d'investigation
- Intégration avec la gestion des incidents (ISMS-POL-A.5.24)

**Disponibilité de l'infrastructure de surveillance** :

- Disponibilité cible de la plateforme SIEM : ≥ 99,5 %
- La perte de visibilité sur des systèmes critiques (Niveau 1) DOIT déclencher une alerte dans les 5 minutes
- Des procédures de surveillance de secours DOIVENT être documentées pour les pannes de la plateforme principale

## Gestion des alertes

**Classification des alertes** :

| Niveau | Délai de triage | Délai d'escalade | Exemples |
|--------|----------------|------------------|---------|
| **Critique** | 15 minutes | 30 minutes si non résolu | Rançongiciel actif, compromission de compte admin, exfiltration confirmée |
| **Élevé** | 1 heure | 2 heures si non résolu | Multiples échecs de connexion avec succès, anomalie significative de données |
| **Moyen** | 4 heures | 8 heures si non résolu | Comportement suspect, dérive de configuration, scan de ports |
| **Faible** | 24 heures | Ticket de suivi | Informationnel, activité à faible risque |

**Gestion de la qualité des alertes** :

- Le taux de faux positifs DOIT être mesuré et suivi mensuellement
- Les règles générant > 20 % de faux positifs DOIVENT être révisées et ajustées dans les 30 jours
- Une réduction continue des faux positifs DOIT être démontrée trimestre après trimestre
- Les alertes inopéantes (jamais triées) DOIVENT être désactivées ou améliorées

## Couverture et lacunes de surveillance

[Organisation] DOIT documenter et gérer les lacunes de couverture de surveillance.

**Évaluation de la couverture** :

- L'évaluation de couverture DOIT être effectuée trimestriellement
- La couverture DOIT être mesurée en pourcentage de systèmes dans le périmètre ayant une surveillance active
- **Cibles** : Niveau 1 (critique) 100 %, Niveau 2 (élevé) ≥ 95 %, Niveau 3 (standard) ≥ 85 %

**Gestion des lacunes** :

- Les lacunes de couverture DOIVENT être documentées avec leur justification et un calendrier de remédiation
- Les systèmes sans couverture de surveillance DOIVENT avoir des contrôles compensatoires (révisions manuelles, accès restreint)
- L'approbation du RSSI est requise pour les lacunes persistantes de plus de 90 jours

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **RSSI** | Propriétaire de la politique ; définition de la stratégie de surveillance ; approbation des référentiels |
| **Responsable SOC** | Opérations quotidiennes de surveillance ; gestion des règles de détection ; reporting |
| **Analystes SOC** | Triage des alertes ; investigation des incidents ; escalade |
| **DSI / Opérations IT** | Mise en œuvre de l'infrastructure de surveillance ; intégration des sources |
| **Propriétaires de systèmes** | Coopération à l'intégration des sources de journaux ; validation des référentiels |

---

# Gouvernance et conformité

## Métriques de performance de la surveillance

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Couverture de surveillance (systèmes critiques) | 100 % | Mensuelle |
| Délai moyen de triage des alertes critiques (MTTA) | ≤ 15 minutes | Mensuelle |
| Taux de faux positifs | < 15 % | Mensuelle |
| Délai moyen de détection (MTTD) des incidents | Tendance décroissante | Trimestrielle |
| Disponibilité SIEM | ≥ 99,5 % | Mensuelle |
| Référentiels documentés et à jour | 100 % | Trimestrielle |

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigences |
|----------------|-----------|
| **nLPD suisse** | Art. 8 — Mesures techniques ; surveillance des accès aux données personnelles |
| **RGPD de l'UE** | Art. 32 — Sécurité du traitement ; surveillance pour détecter les violations |
| **ISO/IEC 27001:2022** | Contrôle A.8.16 — Surveillance des réseaux, systèmes et applications |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Exigences |
|---------------|-----------|
| **FINMA** | Surveillance des systèmes TIC critiques ; détection des incidents |
| **DORA** | Art. 10 — Surveillance des systèmes TIC en temps réel |
| **NIS2** | Art. 21 — Surveillance continue pour la gestion des incidents |

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.16 v1.0)
- ✅ Signatures d'approbation du RSSI, DSI, Direction générale
- ✅ Périmètre de surveillance défini
- ✅ Exigences de référentiels de comportement normal documentées
- ✅ Catégories de détection et seuils spécifiés
- ✅ Délais de triage des alertes définis
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

- Rapports de couverture de surveillance (% de systèmes surveillés)
- Référentiels de comportement normal documentés avec données de mesure
- Tableaux de bord des métriques de surveillance (MTTA, MTTD, taux de faux positifs)
- Journaux de triage des alertes avec horodatages
- Règles de détection SIEM avec historique de révision
- Rapports d'évaluation trimestrielle de la couverture

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable du SOC** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences relatives aux activités de surveillance. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.16 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
