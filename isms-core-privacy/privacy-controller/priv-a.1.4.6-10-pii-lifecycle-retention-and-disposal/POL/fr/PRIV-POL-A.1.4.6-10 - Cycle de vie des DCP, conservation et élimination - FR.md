<!-- ISMS-CORE:POLICY:PRIV-POL-A.1.4.6-10-FR:privacy:POL:a.1.4.6-10 -->
**PRIV-POL-A.1.4.6-10 — Cycle de vie des DCP, conservation et élimination**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cycle de vie des DCP, conservation et élimination |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.1.4.6-10 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Privacy** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DPD | Politique initiale pour la première certification ISO/IEC 27701:2025 |

**Cycle de révision** : Annuel (ou en cas de changement réglementaire ou organisationnel significatif)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** : Principale: DPD; Secondaire: Responsable Juridique/Conformité; Autorité finale: Direction générale.

**Documents connexes** :

- PRIV-POL-00 (Cadre d'applicabilité réglementaire)
- PRIV-POL-01 (Cadre de gouvernance et de prise de décisions)
- PRIV-IMP-A.1.4.6-10-UG (Cycle de vie des DCP — Guide utilisateur)
- PRIV-IMP-A.1.4.6-10-TG (Cycle de vie des DCP — Guide technique)
- PRIV-POL-A.1.4.2-5 (Minimisation des données — politique sœur)
- PRIV-POL-A.3.20-22 (Supports physiques et sécurité des endpoints — exécution de l'élimination)
- ISO/IEC 27701:2025 Contrôles A.1.4.6, A.1.4.7, A.1.4.8, A.1.4.9, A.1.4.10
- RGPD Article 5(1)(e) (limitation de la conservation) ; Article 17 (effacement) ; Article 32(1)(a) (sécurité)
- LPD suisse Article 6(4) (limitation de la conservation) ; Article 7 (sécurité des transmissions)

**Applicabilité du rôle** : Cette politique s'applique à [Organisation] agissant en tant que **Responsable du traitement uniquement**. Les contrôles A.1.4.6–A.1.4.10 sont spécifiques au responsable du traitement (Tableau A.1).

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la désidentification et la suppression des DCP en fin de traitement, la gestion des fichiers temporaires, les limites de conservation des DCP, les procédures d'élimination et les contrôles de transmission — conformément aux contrôles A.1.4.6 à A.1.4.10 d'ISO/IEC 27701:2025.

**Périmètre** : Tous les DCP détenus par [Organisation] en tant que responsable du traitement depuis le moment où la finalité du traitement est atteinte jusqu'à l'élimination confirmée ; tous les fichiers temporaires générés pendant le traitement des DCP ; toute transmission de DCP sur des réseaux de données.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**Contrôle A.1.4.6 — Désidentification et suppression des DCP en fin de traitement**
Le contrôle A.1.4.6 exige que [Organisation] supprime les DCP ou les rende non identifiables dès qu'ils ne sont plus nécessaires pour la finalité pour laquelle ils ont été traités.

**Contrôle A.1.4.7 — Fichiers temporaires**
Le contrôle A.1.4.7 exige que [Organisation] élimine les fichiers temporaires créés pendant le traitement des DCP dans un délai défini et documenté, selon des procédures documentées.

**Contrôle A.1.4.8 — Conservation**
Le contrôle A.1.4.8 exige que [Organisation] ne conserve pas les DCP plus longtemps que nécessaire pour les finalités pour lesquelles ils sont traités.

**Contrôle A.1.4.9 — Élimination**
Le contrôle A.1.4.9 exige que [Organisation] dispose de politiques, procédures et mécanismes documentés pour l'élimination des DCP.

**Contrôle A.1.4.10 — Contrôles de transmission des DCP**
Le contrôle A.1.4.10 exige que [Organisation] applique des contrôles appropriés aux DCP transmis sur des réseaux de données, conçus pour garantir que les données atteignent leur destination prévue.

## Cadre réglementaire

Cette politique s'inscrit dans le cadre réglementaire établi dans PRIV-POL-00. Les obligations suivantes sont pertinentes :

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :

- **RGPD UE** : Article 5(1)(e) (limitation de la conservation — pas de conservation plus longue que nécessaire ; conservation plus longue pour l'archivage/recherche avec garanties appropriées) ; Article 17 (effacement — en fin de finalité, retrait du consentement, ou demande d'effacement réussie) ; Article 32(1)(a) (pseudonymisation et chiffrement comme mesures de sécurité, y compris en transit)
- **LPD suisse** : Article 6(4) (conservation — uniquement le temps nécessaire) ; Article 7 (sécurité des transmissions)
- **ISO/IEC 27701:2025** : Contrôles A.1.4.6–A.1.4.10 (normatifs)

---

# A.1.4.6 — Désidentification et suppression en fin de traitement

Lorsque les DCP ne sont plus nécessaires pour les finalités de traitement identifiées, [Organisation] DOIT soit :

- **Supprimer** les DCP (destruction irréversible), OU
- **Désidentifier** les DCP vers une forme ne permettant pas l'identification ou la réidentification des personnes concernées (anonymisation — confirmée par le DPD per PRIV-POL-A.1.4.2-5)

Cette obligation s'applique **dès que** la finalité n'est plus servie. Elle s'applique à toutes les copies de DCP : bases de données principales, sauvegardes, archives, journaux de traitement et copies temporaires.

### Conservation pour obligation légale contraire

Lorsqu'une obligation légale exige une conservation au-delà de la finalité du traitement (ex. registres fiscaux, registres d'emploi, blocage légal), la conservation DOIT être :

- Limitée à la période légalement requise
- Restreinte au périmètre minimum nécessaire (lorsque possible, les autres champs non requis par l'obligation légale doivent être supprimés)
- Clairement enregistrée dans le Calendrier de conservation avec la référence à la disposition légale

---

# A.1.4.7 — Fichiers temporaires

[Organisation] DOIT veiller à ce que les fichiers temporaires créés lors du traitement des DCP soient éliminés dans un délai documenté et précis.

### Types de fichiers temporaires et délais d'élimination

| Type de fichier temporaire | Conservation maximale | Méthode d'élimination |
|---------------------------|----------------------|----------------------|
| Fichiers de cache de traitement (données de session, résultats intermédiaires) | 24 heures après la fin de session ou la fin du traitement | Purge automatique |
| Fichiers d'export générés pour les demandes d'accès des personnes concernées | 72 heures après transmission à la personne concernée | Suppression sécurisée |
| Fichiers de staging de traitement par lots | 48 heures après la fin du lot | Suppression sécurisée |
| Fichiers de débogage / journaux d'erreurs contenant des DCP | 30 jours | Rotation automatisée avec suppression sécurisée |
| Copies de développement temporaires avec DCP réels | Immédiatement après utilisation (per exigences PRIV-POL-A.3.23-31 sur les données de test) | Suppression sécurisée approuvée par le DPD avec confirmation |

Les délais d'élimination spécifiques pour d'autres types de fichiers temporaires sont documentés dans PRIV-IMP-A.1.4.6-10-TG. Les mécanismes de purge automatisés sont préférés à la suppression manuelle.

---

# A.1.4.8 — Conservation

[Organisation] NE DOIT PAS conserver les DCP plus longtemps que nécessaire pour les finalités pour lesquelles ils sont traités.

### Calendrier de conservation

Le DPD tient un **Calendrier de conservation des DCP** qui précise :

- Catégorie de DCP ou activité de traitement
- Période de conservation (à partir d'une date de déclenchement définie : ex. fin de contrat, dernière utilisation active, date de collecte)
- Base légale ou réglementaire de la période de conservation (le cas échéant)
- Méthode d'élimination à l'expiration

Le Calendrier de conservation est publié en interne et fait partie du RADT. Il est revu au minimum annuellement et lors de changements réglementaires ou d'activités de traitement.

### Blocages légaux

Lorsque le Juridique/Conformité identifie une exigence de blocage légal, les DCP soumis au blocage DOIVENT être conservés indépendamment de leur date d'élimination prévue. Les blocages légaux DOIVENT être :

- Autorisés par écrit par le Juridique/Conformité ou la Direction générale
- Documentés dans le Calendrier de conservation avec la base du blocage et la date de fin prévue
- Revus au minimum trimestriellement ; levés rapidement une fois la base du blocage inapplicable
- Appliqués de manière étroite au périmètre minimum de DCP nécessaire

Les blocages légaux qui ne sont pas formellement revus et levés deviennent une source de conservation illicite. Le DPD surveille tous les blocages légaux actifs.

### Principes de conservation

- Les périodes de conservation DOIVENT être basées sur un besoin documenté (légal, contractuel ou opérationnel) — pas sur le principe de « conserver au cas où »
- Lorsque plusieurs obligations réglementaires créent des exigences de conservation différentes pour les mêmes données, la période obligatoire la plus longue s'applique pour le périmètre légalement requis ; les données excédentaires sont supprimées à la première période applicable
- Les sauvegardes contenant des DCP DOIVENT être soumises aux mêmes limites de conservation que les données principales — les calendriers de conservation des sauvegardes DOIVENT s'aligner sur les périodes de conservation des DCP ou disposer d'une exception documentée avec des contrôles compensatoires

---

# A.1.4.9 — Élimination

[Organisation] DOIT disposer de politiques, procédures et mécanismes documentés pour l'élimination des DCP.

### Exigences d'élimination

L'élimination des DCP DOIT être :

- **Irréversible** : Les DCP éliminés ne peuvent pas être récupérés par des moyens techniques ordinaires
- **Documentée** : Chaque action d'élimination est enregistrée (ce qui a été éliminé, quand, par qui, méthode)
- **Vérifiée** : Lorsque techniquement faisable, l'élimination est confirmée par vérification automatisée ou manuelle
- **Conforme au traitement de la classification** : L'élimination des DCP RESTREINTS utilise la méthode la plus stricte per PRIV-POL-A.3.20-22

### Méthodes d'élimination

| Emplacement des données | Méthode d'élimination |
|------------------------|----------------------|
| Enregistrements de base de données | SQL DELETE ou équivalent ; ou anonymisation en place lorsque la suppression crée des problèmes d'intégrité des données (avec approbation DPD) |
| Système de fichiers (électronique) | Effacement cryptographique (si chiffré) ou standard d'écrasement approuvé |
| Supports de sauvegarde | Écrasement par cycle de sauvegarde aligné sur le calendrier de conservation ; ou destruction physique pour les supports de sauvegarde expirés |
| Documents physiques | Déchiquetage croisé (CONFIDENTIEL), déchiquetage croisé + témoin (RESTREINT) |
| Stockage cloud | Suppression via API/console approuvée ; confirmation de suppression du fournisseur le cas échéant |

Les procédures d'élimination sont détaillées dans PRIV-IMP-A.1.4.6-10-TG.

### Déclencheurs d'élimination

L'élimination des DCP DOIT être déclenchée par :

- L'expiration de la période de conservation per le Calendrier de conservation
- La cessation de la finalité du traitement (lorsqu'aucune obligation légale contraire ne s'applique)
- La demande d'effacement d'une personne concernée (per PRIV-POL-A.1.3.5-10) — dans le délai de réponse requis
- Le retrait du consentement (pour le traitement basé sur le consentement sans autre base)
- La fin du contrat ou de l'emploi (pour les catégories de DCP applicables)

---

# A.1.4.10 — Contrôles de transmission des DCP

[Organisation] DOIT soumettre les DCP transmis sur des réseaux de données à des contrôles appropriés pour garantir que les données atteignent leur destination prévue.

### Exigences de contrôle des transmissions

- Tous les DCP transmis sur des réseaux DOIVENT être chiffrés en transit avec les standards TLS actuels (minimum TLS 1.2 ; TLS 1.3 préféré)
- Les DCP transmis à des tiers DOIVENT utiliser des méthodes de transfert sécurisé approuvées per PRIV-POL-A.3.5-7 (règles de transfert)
- La transmission non chiffrée de DCP CONFIDENTIELS ou RESTREINTS sur des réseaux publics est interdite
- Une confirmation de livraison ou un accusé de réception DOIT être obtenu pour les transferts de DCP RESTREINTS (catégorie spéciale)
- Les journaux de transmission DOIVENT être tenus pour les transferts de DCP CONFIDENTIELS et RESTREINTS per PRIV-POL-A.3.25 (journalisation)

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Délégué à la Protection des Données (DPD)** | Propriétaire du Calendrier de conservation ; approuve les exceptions d'élimination ; confirme l'anonymisation ; surveille la conformité à l'élimination ; répond aux demandes d'effacement impliquant des conflits de conservation |
| **Propriétaire des données** | Déclenche l'élimination à l'expiration de la période de conservation dans son domaine ; escalade les conflits d'élimination au DPD |
| **Équipe Sécurité IT** | Met en œuvre les mécanismes d'élimination automatisés ; exécute l'alignement de la conservation des sauvegardes ; tient les journaux d'élimination ; configure le chiffrement des transmissions |
| **Juridique/Conformité** | Conseille sur les exigences de blocage légal ; identifie les périodes de conservation légalement obligatoires |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Calendrier de conservation des DCP | Périodes de conservation documentées par catégorie de DCP, avec base légale | En cours + 3 ans |
| Journaux d'élimination | Enregistrements des actions d'élimination des DCP avec date, méthode et périmètre | 5 ans |
| Confirmation de purge des fichiers temporaires | Confirmation automatisée ou manuelle de l'élimination des fichiers temporaires | 3 ans à compter de la date de purge |
| Configuration du chiffrement des transmissions | Enregistrements de configuration TLS pour les systèmes transportant des DCP | En cours + 3 ans |
| Enregistrements de révision du Calendrier de conservation | Preuves de révision annuelle | 3 ans à compter de la date de la révision |

---

# Considérations d'audit

- Calendrier de conservation avec périodes documentées et base légale pour toutes les catégories de DCP
- Preuves des actions d'élimination dans les délais prévus
- Aucun DCP conservé au-delà de la période de conservation documentée sans base légale documentée
- Mécanismes de purge des fichiers temporaires configurés et vérifiés
- Application de TLS pour les DCP en transit (preuves de configuration)
- Journaux d'élimination montrant la méthode et le calendrier

---

<!-- QA_VERIFIED: 2026-04-03 -->
