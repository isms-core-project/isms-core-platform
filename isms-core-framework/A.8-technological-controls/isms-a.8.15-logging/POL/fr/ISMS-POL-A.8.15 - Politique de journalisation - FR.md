<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.15-FR:framework:POL:a.8.15 -->
**ISMS-POL-A.8.15 – Politique de journalisation**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de journalisation |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.15 |
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
| 1.0 | [Date] | RSSI | Cadre de politique initial |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Revue technique : Responsable de la sécurité de l'information
- Revue opérationnelle : Responsable du SOC / Responsable des opérations IT
- Revue de confidentialité : Délégué à la Protection des Données (DPD)
- Revue de conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.15.1-UG/TG (Inventaire des sources de journaux)
- ISMS-IMP-A.8.15.2-UG/TG (Collecte et centralisation des journaux)
- ISMS-IMP-A.8.15.3-UG/TG (Protection et conservation des journaux)
- ISMS-IMP-A.8.15.4-UG/TG (Analyse et révision des journaux)
- ISMS-REF-A.8.15 (Référence des normes de journalisation)
- ISMS-POL-A.8.16 (Activités de surveillance)
- ISMS-POL-A.8.17 (Synchronisation des horloges)
- ISMS-POL-A.5.24 (Gestion des incidents de sécurité de l'information)

---

# Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de journalisation des événements afin de soutenir la détection des incidents, les investigations forensiques, les obligations de conformité et la responsabilisation, conformément au Contrôle A.8.15 de la norme ISO/IEC 27001:2022.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de journalisation des événements. Cette politique établit :

- QUELS événements doivent être journalisés
- COMBIEN DE TEMPS les journaux doivent être conservés
- QUI est responsable de la gestion des journaux
- QUAND les journaux doivent être révisés

Les procédures de mise en œuvre (COMMENT les journaux sont techniquement configurés) sont documentées séparément dans ISMS-IMP-A.8.15 (variantes UG/TG).

**Contrôle A.8.15 de la norme ISO/IEC 27001:2022 — Journalisation** :

> *Des journaux d'événements enregistrant les activités des utilisateurs, les exceptions, les défaillances et les événements de sécurité de l'information doivent être produits, conservés et régulièrement révisés.*

---

# Périmètre

## Systèmes et activités dans le périmètre

**Cette politique s'applique à** :

- Tous les systèmes d'information, applications et composants d'infrastructure
- Équipements réseau (routeurs, commutateurs, pare-feu, passerelles VPN, équilibreurs de charge)
- Outils de sécurité (SIEM, IDS/IPS, anti-logiciels malveillants, protection des postes de travail, DLP)
- Systèmes de bases de données et plateformes de stockage de données
- Services cloud et applications SaaS
- Systèmes d'authentification et de gestion des identités
- Infrastructure d'accès administratif (serveurs de rebond, hôtes bastion, PAM)

**Modèles de déploiement couverts** :

- Infrastructure sur site
- Environnements cloud (public, privé, hybride)
- Services hébergés par des tiers

## Hors périmètre

- Pistes d'audit d'applications métier non liées à la sécurité
- Journaux de transactions financières à des fins comptables (couverts par les politiques de contrôle financier)
- Surveillance en temps réel et alertes (couvertes par ISMS-POL-A.8.16)

---

# Énoncés de politique

## Exigences de journalisation des événements

[Organisation] DOIT journaliser les événements liés à la sécurité sur l'ensemble des systèmes dans le périmètre.

**Catégories d'événements obligatoires** :

- **Événements d'authentification** : Tentatives de connexion (réussites et échecs), déconnexions, verrouillages de comptes, changements de mots de passe, événements AMF
- **Événements d'autorisation** : Accès aux données sensibles, élévation de privilèges, modifications des contrôles d'accès
- **Actions administratives** : Modifications de configuration, gestion des comptes utilisateurs, octroi de privilèges, modifications des politiques de sécurité
- **Événements de sécurité** : Détections de logiciels malveillants, alertes d'intrusion, blocages de pare-feu, alertes DLP
- **Événements système** : Démarrages/arrêts, changements d'état des services, erreurs, épuisement des ressources
- **Événements réseau** : Correspondances de règles de pare-feu, connexions VPN, traversées des frontières de segmentation
- **Événements applicatifs** : Erreurs, exceptions, authentification API, exécution de fonctions privilégiées

**Exigences relatives au contenu des journaux** : Chaque entrée de journal DOIT inclure un horodatage, l'identité de l'utilisateur, le système source, le type d'événement, le résultat et le contexte pertinent. Les spécifications détaillées des champs sont documentées dans ISMS-REF-A.8.15.

## Exigences de centralisation des journaux

[Organisation] DOIT centraliser les journaux dans une infrastructure SIEM ou équivalente :

- Tous les systèmes dans le périmètre DOIVENT transmettre leurs journaux à la plateforme de journalisation centralisée
- La transmission des journaux DOIT être effectuée en temps quasi réel (délai de transmission cible : < 5 minutes)
- La plateforme de journalisation centralisée DOIT être dédiée à la sécurité et distincte des systèmes de production journalisés
- Les journaux DOIVENT être transmis via des protocoles sécurisés (TLS/TLS mutualisé)
- La couverture de centralisation DOIT atteindre ≥ 95 % des systèmes de production dans le périmètre

## Exigences de protection des journaux

[Organisation] DOIT protéger les journaux contre la modification, la suppression et l'accès non autorisé.

**Contrôles d'intégrité** :

- Les journaux DOIVENT être stockés de façon inviolable (write-once-read-many ou équivalent)
- La modification des journaux par les administrateurs système des systèmes sources DOIT être techniquement impossible
- L'intégrité des journaux DOIT être vérifiée régulièrement (mensuelle minimum)

**Contrôles d'accès** :

- L'accès aux journaux DOIT être restreint au personnel autorisé (équipe SOC, auditeurs)
- L'accès aux journaux DOIT lui-même être journalisé
- Les administrateurs des systèmes sources NE DOIVENT PAS avoir d'accès en écriture à leurs propres journaux dans la plateforme de journalisation centralisée

**Disponibilité** :

- La plateforme de journalisation DOIT maintenir une disponibilité de ≥ 99,5 % (hors maintenance planifiée)
- Des alertes DOIVENT être générées en cas d'interruption de la transmission des journaux depuis des systèmes critiques

## Exigences de conservation des journaux

[Organisation] DOIT conserver les journaux selon des périodes minimales basées sur la classification et les exigences réglementaires.

**Durées minimales de conservation** :

| Catégorie de journal | Conservation minimale | Justification |
|---------------------|-----------------------|---------------|
| Journaux d'authentification et d'accès privilégié | 12 mois | ISO 27001, forensique, conformité |
| Journaux des événements de sécurité | 12 mois | Détection des incidents, forensique |
| Journaux d'audit des changements de configuration | 24 mois | Traçabilité, audit |
| Journaux système et d'infrastructure | 6 mois | Diagnostic, forensique |
| Journaux d'accès aux données Restreintes | 24 mois | Conformité réglementaire (RGPD, nLPD) |
| Journaux des incidents de sécurité confirmés | 36 mois | Conformité légale, référence |

**Durées conditionnelles** : Des durées plus longues peuvent s'appliquer selon les réglementations sectorielles (PCI DSS : 12 mois accessibles + 12 mois archivés ; FINMA : selon les exigences spécifiques).

**Exigences d'archivage** :

- Les journaux archivés (au-delà de la période de stockage chaud) DOIVENT être récupérables dans les 48 heures pour les besoins d'audit
- Les journaux archivés DOIVENT maintenir leur intégrité et leur lisibilité

## Exigences de révision et d'analyse des journaux

[Organisation] DOIT réviser et analyser régulièrement les journaux pour détecter les événements de sécurité.

**Révision automatisée** :

- La plateforme de journalisation centralisée (SIEM) DOIT analyser les journaux en temps réel pour les indicateurs d'attaque connus
- Les alertes automatiques DOIVENT être générées pour les catégories d'événements à haut risque
- Les règles de détection DOIVENT être maintenues et mises à jour régulièrement

**Révision manuelle** :

- Les alertes SIEM DOIVENT être triées par le SOC dans les délais définis dans la politique de gestion des incidents (ISMS-POL-A.5.24)
- Des révisions hebdomadaires des journaux DOIVENT être effectuées pour les systèmes critiques (Niveau 1) en l'absence d'alertes automatiques
- Des révisions mensuelles DOIVENT être documentées avec les résultats

**Indicateurs de révision efficace** :

- Taux de traitement des alertes : ≥ 95 % des alertes triées dans les SLA définis
- Taux de faux positifs : suivi et réduction continue (cible < 15 %)
- Délai moyen de détection (MTTD) : suivi trimestriellement

---

# Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigences de journalisation |
|----------------|----------------------------|
| **nLPD suisse** | Art. 8 — Mesures techniques de protection ; journalisation des accès aux données personnelles |
| **RGPD de l'UE** | Art. 32 — Sécurité du traitement incluant la journalisation ; Art. 33 — Détection des violations (nécessite des journaux) |
| **ISO/IEC 27001:2022** | Contrôle A.8.15 — Production, conservation et révision des journaux |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Exigences spécifiques |
|---------------|----------------------|
| **PCI DSS v4.0.1** | Exig. 10 — Journalisation et surveillance de tous les accès aux composants système ; conservation 12 mois |
| **FINMA** | Journalisation des accès aux systèmes critiques et aux données clients |
| **DORA** | Art. 10 — Journalisation des systèmes TIC pour la détection des incidents |
| **NIS2** | Art. 21 — Journalisation pour la gestion des incidents de cybersécurité |

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **RSSI** | Propriétaire de la politique ; définition des exigences de journalisation ; supervision de la conformité |
| **Responsable de la sécurité de l'information** | Mise en œuvre quotidienne ; maintenance de la plateforme SIEM ; révision des journaux |
| **SOC** | Surveillance en temps réel ; triage des alertes ; réponse aux incidents basés sur les journaux |
| **Opérations IT** | Configuration de la transmission des journaux sur les systèmes source ; maintenance de l'infrastructure |
| **DPD** | Conformité RGPD/nLPD pour la journalisation des DCP ; durées de conservation |
| **Propriétaires de systèmes** | S'assurer que leurs systèmes transmettent les journaux requis |

---

# Gouvernance et conformité

## Calendrier d'évaluation

| Domaine | Fréquence | Procédure | Résultat |
|---------|-----------|-----------|---------|
| Inventaire des sources de journaux | Annuelle (mises à jour trimestrielles) | ISMS-IMP-A.8.15.1 | Classeur d'inventaire avec % de couverture |
| Collecte et centralisation | Annuelle (métriques trimestrielles) | ISMS-IMP-A.8.15.2 | Rapport de conformité à la transmission |
| Protection et conservation | Semestrielle | ISMS-IMP-A.8.15.3 | Classeur de conformité à la conservation |
| Analyse et révision | Trimestrielle | ISMS-IMP-A.8.15.4 | Dossiers de complétion des révisions |

## Gestion des lacunes et des constats

**Identification et enregistrement des lacunes** :

- Les constats des évaluations de journalisation DOIVENT être enregistrés dans le Registre des lacunes organisationnel
- Chaque constat DOIT inclure : ID du contrôle (A.8.15), description du constat, gravité, systèmes/périmètre concernés, cause profonde, responsable de remédiation, date cible, statut

**Exigences de clôture des lacunes** :

- La clôture des lacunes nécessite une vérification des preuves par le Responsable de la sécurité de l'information
- Les lacunes de gravité Élevée/Critique nécessitent l'approbation du RSSI pour la clôture
- Les lacunes clôturées restent dans le registre pendant 3 ans minimum

**Escalade et reporting** :

- Les lacunes ouvertes DOIVENT être rapportées mensuellement au RSSI
- Les lacunes de gravité élevée ouvertes depuis > 30 jours DOIVENT être escaladées vers la Direction générale
- Les lacunes critiques ouvertes depuis > 14 jours nécessitent une décision exécutive : accepter le risque OU allouer des ressources d'urgence

## Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Couverture de centralisation des journaux (systèmes de production) | ≥ 95 % | Mensuelle |
| Conformité à la conservation des journaux | 100 % | Mensuelle |
| Taux de complétion de la révision des journaux | 100 % | Trimestrielle |
| Disponibilité de la plateforme SIEM | ≥ 99,5 % | Mensuelle |
| Intégrité des journaux (vérifications réussies) | 100 % | Mensuelle |

---

# Intégration dans le SMSI

## Contrôles connexes

| Contrôle | Intégration |
|----------|-------------|
| **A.8.16 (Surveillance)** | La surveillance en temps réel consomme les journaux pour les alertes |
| **A.8.17 (Synchronisation des horloges)** | Les horodatages précis permettent la corrélation des journaux |
| **A.5.24 (Gestion des incidents)** | Les journaux fournissent les preuves de détection et d'investigation |
| **A.5.17-18 (Authentification/Accès)** | Les événements d'authentification et d'autorisation sont journalisés |
| **A.8.9 (Gestion de la configuration)** | Les modifications de configuration sont journalisées |

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.15 v1.0)
- ✅ Signatures d'approbation du RSSI, DPD, Responsable juridique/conformité, Direction générale
- ✅ Catégories d'événements obligatoires définies
- ✅ Exigences de centralisation des journaux documentées
- ✅ Exigences de protection et d'intégrité spécifiées
- ✅ Durées minimales de conservation définies
- ✅ Exigences de révision et d'analyse spécifiées
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

- Rapports de couverture de la plateforme SIEM (% de systèmes transmettant des journaux)
- Configuration SIEM et règles de détection
- Dossiers de révision des journaux (complétés selon le calendrier)
- Rapports de vérification de l'intégrité des journaux
- Métriques de conservation des journaux (conformité aux délais)
- Dossiers de triage des alertes SOC

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Responsable de la sécurité de l'information** | [Nom] | [Date] |
| **Responsable du SOC** | [Nom] | [Date] |
| **Responsable des opérations IT** | [Nom] | [Date] |
| **Délégué à la Protection des Données (DPD)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de journalisation des événements. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.15 (UG/TG). Les normes techniques sont documentées dans ISMS-REF-A.8.15.*

<!-- QA_VERIFIED: 2026-04-02 -->
