<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.17-FR:framework:POL:a.8.17 -->
**ISMS-POL-A.8.17 – Synchronisation des horloges**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Synchronisation des horloges |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.17 |
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
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.17.1-UG/TG (Configuration des sources de temps)
- ISMS-IMP-A.8.17.2-UG/TG (Processus de vérification de la synchronisation)
- ISMS-IMP-A.8.17.3-UG/TG (Gestion des exceptions)
- ISO/IEC 27001:2022 Contrôle A.8.17
- ISMS-POL-A.8.15 (Journalisation)
- ISMS-POL-A.8.16 (Activités de surveillance)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de synchronisation des horloges sur l'ensemble des systèmes de traitement de l'information afin de permettre la corrélation des journaux, les analyses forensiques et la fiabilité des pistes d'audit, conformément au Contrôle A.8.17 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les systèmes de traitement de l'information générant des journaux ou participant à des opérations liées à la sécurité, notamment les serveurs, les équipements réseau, les systèmes de sécurité et les instances cloud.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance de la synchronisation des horloges. Cette politique établit QUELLE synchronisation des horloges est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.17 (variantes UG/TG).

**Pourquoi c'est important** : Des horodatages incohérents entre les systèmes compromettent directement :
- La **corrélation des journaux** dans le SIEM : des événements liés sur des systèmes différents peuvent sembler se produire dans un ordre différent
- Les **investigations forensiques** : l'établissement de la chronologie des incidents devient impossible
- La **valeur probante des pistes d'audit** : les horodatages inexacts affaiblissent l'admissibilité des preuves
- L'**intégrité des certificats numériques** : la validation des certificats dépend des horloges système

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.17 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.17 — Synchronisation des horloges**

> *Les horloges des systèmes de traitement de l'information utilisés par l'organisation doivent être synchronisées avec des sources de temps approuvées.*

**Objectif du contrôle** : Établir la politique organisationnelle pour la synchronisation des horloges assurant des horodatages précis et cohérents sur tous les systèmes d'information afin de permettre la corrélation des journaux, soutenir les investigations forensiques, valider les signatures numériques et maintenir l'intégrité des pistes d'audit.

---

# Exigences de synchronisation des horloges

## Sources de temps autorisées

[Organisation] DOIT utiliser des sources de temps autorisées et fiables.

**Hiérarchie NTP (Network Time Protocol)** :

| Niveau | Description | Exemples |
|--------|-------------|---------|
| **Stratum 0** | Références de temps atomiques (non accessibles directement via réseau) | Horloges GPS, horloges atomiques |
| **Stratum 1** | Serveurs NTP directement connectés à une source Stratum 0 | Serveurs de temps nationaux (METAS/Metrology et al.) |
| **Stratum 2** | Serveurs NTP synchronisés sur Stratum 1 | Pools NTP publics (pool.ntp.org) |
| **Stratum interne** | Serveurs NTP internes de [Organisation] | Serveurs NTP internes synchronisés sur des serveurs Stratum 1/2 |

**Sources de temps approuvées pour [Organisation]** :

- Serveurs NTP internes de [Organisation] (Stratum interne, synchronisés sur des sources Stratum 1/2)
- Pools NTP publics de confiance : `0.ch.pool.ntp.org`, `1.ch.pool.ntp.org` (pour le contexte suisse)
- Services de temps des fournisseurs cloud : AWS (169.254.169.123), Azure (time.windows.com), GCP (metadata.google.internal)

**Sources de temps prohibées** :

- Horloges non synchronisées (systèmes utilisant leur propre heure locale non synchronisée)
- Sources de temps non vérifiées ou non fiables
- Sources de temps n'utilisant pas NTP ou un protocole équivalent sécurisé

## Infrastructure NTP interne

[Organisation] DOIT maintenir une infrastructure NTP interne :

- Au moins deux serveurs NTP internes (redondance)
- Serveurs NTP internes synchronisés sur au moins deux sources externes distinctes (pour résilience)
- Tous les systèmes internes configurés pour utiliser les serveurs NTP internes
- Serveurs NTP internes exclusivement dans l'accès entrant depuis les sources Stratum 1/2 approuvées (restrictions réseau)

## Exigences de synchronisation par type de système

**Serveurs de production critiques (Niveau 1)** :

- Synchronisation NTP requise, vérifiée toutes les 5 minutes
- Dérive d'horloge maximale tolérée : **± 500 millisecondes**
- Alertes automatiques si la dérive dépasse 1 seconde
- Alertes automatiques si la synchronisation NTP échoue depuis plus de 15 minutes

**Serveurs et systèmes standard (Niveau 2-3)** :

- Synchronisation NTP requise, vérifiée toutes les 60 minutes
- Dérive d'horloge maximale tolérée : **± 1 seconde**
- Alertes si la synchronisation échoue depuis plus de 1 heure

**Équipements réseau (pare-feu, commutateurs, routeurs)** :

- Synchronisation NTP requise
- Utilisation du même serveur NTP interne que les systèmes de production
- Dérive maximale tolérée : ± 1 seconde

**Appareils mobiles et postes de travail** :

- Synchronisation automatique via le fournisseur d'identité ou MDM
- Les systèmes d'exploitation modernes (Windows, macOS, iOS, Android) maintiennent une synchronisation automatique via NTP ou protocoles équivalents

**Environnements cloud** :

- Les instances cloud DOIVENT utiliser les services de temps du fournisseur cloud
- Vérifier que les services de temps cloud sont configurés et actifs lors du déploiement

## Fuseau horaire

**Standard organisationnel pour les journaux** :

- Tous les horodatages dans les journaux de sécurité DOIVENT être en **UTC** (Temps Universel Coordonné)
- Format obligatoire : ISO 8601 — `YYYY-MM-DDTHH:MM:SS.mmmZ`
- L'affichage des interfaces utilisateur peut utiliser le fuseau horaire local, mais les journaux doivent être stockés en UTC

**Pourquoi UTC** :

- Élimine la confusion liée aux changements d'heure (heure d'été/heure d'hiver)
- Facilite la corrélation entre les systèmes dans différentes zones géographiques
- Standard international pour les pistes d'audit forensiques

## Vérification de la conformité

**Surveillance continue** :

- La dérive d'horloge DOIT être surveillée en continu sur tous les systèmes de production
- L'état de synchronisation NTP DOIT être collecté et agrégé dans la plateforme de surveillance
- Les alertes DOIVENT être configurées pour les systèmes dépassant les seuils de dérive

**Vérification périodique** :

- Révision mensuelle de la conformité à la synchronisation des horloges sur tous les systèmes dans le périmètre
- Documentation des systèmes non conformes et plan de remédiation
- Rapport trimestriel sur la santé globale de l'infrastructure NTP

---

# Gestion des exceptions

**Exceptions autorisées** :

- Systèmes air-gapped (isolés) sans accès réseau : utiliser une référence de temps interne avec vérification manuelle documentée
- Équipements hérités ne supportant pas NTP : contrôles compensatoires (ajustement manuel documenté et fréquent)

**Processus d'exception** :

- Justification métier et contrainte technique documentées
- Contrôles compensatoires (par ex. ajustement manuel quotidien, surveillance renforcée)
- Approbation du RSSI
- Durée maximale : 12 mois (renouvellement avec réévaluation)

---

# Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Pertinence |
|----------------|-----------|
| **nLPD suisse** | Art. 8 — Piste d'audit fiable pour les accès aux données personnelles |
| **RGPD de l'UE** | Art. 33 — Délais précis pour la notification des violations (72 heures) nécessitent des horodatages fiables |
| **ISO/IEC 27001:2022** | Contrôle A.8.17 — Synchronisation avec des sources de temps approuvées |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Exigence |
|---------------|---------|
| **PCI DSS v4.0.1** | Exig. 10.6 — Synchronisation de l'heure sur les systèmes traitant des données de cartes |
| **FINMA** | Journalisation fiable des systèmes TIC |
| **DORA** | Précision des journaux d'événements pour la gestion des incidents |

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation des exceptions ; supervision de la conformité |
| **Opérations IT** | Maintenance de l'infrastructure NTP ; configuration des clients NTP ; remédiation des non-conformités |
| **Responsable SOC** | Surveillance de la dérive d'horloge ; gestion des alertes de synchronisation |
| **Propriétaires de systèmes** | S'assurer que les systèmes gérés sont configurés pour utiliser le NTP approuvé |

---

# Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Systèmes de production dans les seuils de dérive | 100 % | Mensuelle |
| Systèmes configurés avec NTP approuvé | ≥ 99 % | Mensuelle |
| Incidents de dérive d'horloge significative (> 1 sec) | 0 | Mensuelle |
| Disponibilité de l'infrastructure NTP interne | ≥ 99,9 % | Mensuelle |

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.17 v1.0)
- ✅ Signatures d'approbation du RSSI, DSI, Direction générale
- ✅ Sources de temps autorisées définies
- ✅ Seuils de dérive par type de système spécifiés
- ✅ Exigences de fuseau horaire documentées
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

- Configuration NTP des serveurs (exports de configuration)
- Rapports de dérive d'horloge (métriques de surveillance)
- Journaux de statut de synchronisation NTP
- Alertes de non-synchronisation avec actions de remédiation

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de synchronisation des horloges. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.17 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
