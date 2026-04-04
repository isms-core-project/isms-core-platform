<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.8-10-FR:privacy:POL:a.3.8-10 -->
**PRIV-POL-A.3.8-10 — Contrôles d'identité, d'accès et des fournisseurs**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Contrôles d'identité, d'accès et des fournisseurs |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.3.8-10 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Privacy** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DPD | Politique initiale pour la première certification ISO/IEC 27701:2025 |

**Cycle de révision** : Annuel | **Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** : Principale: DPD; Secondaire: RSSI; Juridique: Responsable Juridique/Conformité; Autorité finale: Direction générale.

**Documents connexes** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.8-10-UG / TG
- ISMS-POL-A.5.15-16-18 (Gestion des identités et des accès — parallèle SGSI)
- ISMS-POL-A.5.19-23 (Services cloud et relations fournisseurs — parallèle SGSI)
- ISO/IEC 27701:2025 Contrôles A.3.8, A.3.9, A.3.10
- RGPD Article 25 (Protection des données dès la conception) ; Article 28 (Contrats sous-traitants) ; Article 32 (Sécurité)
- LPD suisse Article 7 (Sécurité des données) ; Article 9 (Accords sous-traitants)

**Applicabilité du rôle** : Cette politique s'applique à l'organisation agissant à la fois comme **Responsable du traitement et comme Sous-traitant des DCP**. Les contrôles A.3.8, A.3.9 et A.3.10 sont des contrôles partagés (Tableau A.3).

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la gestion du cycle de vie des identités, la gouvernance des droits d'accès et les obligations de sécurité de l'information dans les accords fournisseurs en lien avec le traitement des DCP — conformément aux contrôles A.3.8, A.3.9 et A.3.10 d'ISO/IEC 27701:2025.

**Périmètre** : Toutes les identités utilisées pour accéder aux DCP ou aux systèmes de traitement des DCP ; tous les droits d'accès aux DCP et actifs associés ; toutes les relations fournisseurs où les exigences de sécurité de l'information pour le traitement des DCP s'appliquent.

**Justification des contrôles combinés** : A.3.8 (cycle de vie des identités), A.3.9 (droits d'accès) et A.3.10 (sécurité fournisseurs) forment la triade de gouvernance des accès pour la protection des DCP. Les identités créent les acteurs ; les droits d'accès déterminent ce qu'ils peuvent atteindre ; les accords fournisseurs étendent ces contrôles à la chaîne d'approvisionnement.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**Contrôle A.3.8 — Gestion des identités**
Le contrôle A.3.8 exige que [Organisation] gère l'ensemble du cycle de vie de toutes les identités ayant une relation avec le traitement des DCP — couvrant le provisionnement, la modification, la suspension et la désactivation des identités humaines et non humaines.

**Contrôle A.3.9 — Droits d'accès**
Le contrôle A.3.9 exige que [Organisation] provisionne, examine, modifie et supprime les droits d'accès aux DCP et autres actifs associés conformément à sa politique de contrôle d'accès.

**Contrôle A.3.10 — Prise en compte de la sécurité de l'information dans les accords fournisseurs**
Le contrôle A.3.10 exige que [Organisation] établisse et convienne d'exigences pertinentes de sécurité de l'information pour le traitement des DCP avec chaque fournisseur, calibrées selon le type de relation fournisseur.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 25 (contrôle d'accès comme mesure de protection des données dès la conception) ; Article 28 (les contrats de sous-traitance doivent inclure des obligations de sécurité adéquates) ; Article 32 (mesures techniques appropriées incluant les contrôles d'accès) ; Article 5(1)(f) (principe d'intégrité et de confidentialité)
- **LPD suisse** : Article 7 (mesures techniques et organisationnelles de sécurité) ; Article 9 (les accords de sous-traitance doivent assurer une protection équivalente)
- **ISO/IEC 27701:2025** : Contrôles A.3.8, A.3.9, A.3.10 (normatifs)

---

# Gestion du cycle de vie des identités pour le traitement des DCP (A.3.8)

## Exigences du cycle de vie des identités

[Organisation] DOIT gérer l'ensemble du cycle de vie de toutes les identités ayant accès aux DCP ou aux systèmes de traitement des DCP. La gestion du cycle de vie des identités pour les DCP DOIT être cohérente avec et étendre les exigences SGSI de gestion des identités (ISMS-POL-A.5.15-16-18).

### Provisionnement des identités pour l'accès aux DCP

Les identités auxquelles est accordé l'accès aux DCP ou aux systèmes de traitement des DCP DOIVENT être provisionnées selon les bases suivantes :

- **Finalité commerciale documentée** : Une justification commerciale documentée et approuvée pour l'accès aux DCP doit exister avant le provisionnement
- **Alignement avec le rôle** : L'accès DOIT être aligné sur les responsabilités documentées de traitement des DCP du rôle ; l'accès aux DCP non requis pour le rôle NE DOIT PAS être provisionné
- **Privilège minimum** : Les identités DOIVENT être provisionnées avec le niveau d'accès minimum nécessaire pour la finalité documentée (principe du minimum nécessaire, cohérent avec RGPD Article 5(1)(c) minimisation des données)
- **Autorité d'approbation** : Le provisionnement de l'accès aux DCP DOIT nécessiter l'approbation du Propriétaire des données pour le jeu de données DCP concerné, ou du DPD lorsqu'aucun Propriétaire des données n'est attribué

### Modification et suspension des identités

Lorsqu'un rôle change, qu'un individu est transféré vers une autre fonction, ou que les circonstances changent de telle sorte qu'une finalité d'accès aux DCP précédemment justifiée ne s'applique plus : les droits d'accès aux DCP DOIVENT être modifiés ou suspendus dans le délai spécifié dans PRIV-IMP-A.3.8-10-TG ; la notification des changements de rôle DOIT être fournie par la direction hiérarchique à l'Équipe Sécurité IT et documentée ; la suspension (pas la suppression immédiate) DOIT s'appliquer lorsqu'un blocage légal ou une enquête exige la préservation des enregistrements d'identité.

### Désactivation des identités

Lorsque l'emploi ou l'engagement d'un individu prend fin, ou que la finalité d'un compte de service est terminée : les droits d'accès aux DCP DOIVENT être supprimés le jour du dernier accès ou avant (départ des employés, fin de contrat) ; les enregistrements de désactivation des identités DOIVENT être conservés pendant 3 ans à compter de la date de désactivation ; lorsque la désactivation est retardée pour des raisons techniques, l'accès DOIT être suspendu immédiatement et la désactivation complétée dans les 5 jours ouvrables ; pour garantir une désactivation rapide lorsque la notification RH n'est pas reçue, la Sécurité IT DOIT effectuer une réconciliation mensuelle des identités actives avec accès aux DCP avec les dossiers RH actuels ; toute identité sans dossier d'emploi ou d'engagement actif courant DOIT être suspendue en attente de confirmation du DPD.

### Gestion des identités non humaines

Les comptes de service, de traitement applicatif et d'automatisation utilisés dans les pipelines de traitement des DCP DOIVENT être : individuellement identifiés et enregistrés dans le Registre des identités ; associés à un propriétaire humain responsable (responsable de la gestion du cycle de vie du compte de service) ; soumis à une révision périodique (au minimum annuellement) pour confirmer la nécessité continue ; désactivés lorsque la finalité de traitement qu'ils soutiennent est abandonnée.

---

# Droits d'accès aux DCP et actifs associés (A.3.9)

## Exigences des droits d'accès

[Organisation] DOIT veiller à ce que les droits d'accès aux DCP et actifs associés soient provisionnés, examinés, modifiés et supprimés conformément à la politique de contrôle d'accès SGSI (ISMS-POL-A.5.15-16-18) et aux extensions spécifiques aux DCP définies dans cette politique.

### Principes des droits d'accès aux DCP

Les droits d'accès aux DCP DOIVENT être régis par :

1. **Accès minimum nécessaire** : L'accès accordé DOIT être limité aux DCP et actifs associés minimum requis pour remplir la finalité de traitement documentée
2. **Besoin de traitement** : L'accès n'est accordé que lorsqu'il existe un besoin documenté et actuel de traiter les DCP spécifiques
3. **Séparation des fonctions** : Lorsque le traitement des DCP implique des opérations à haut risque (suppression, export, accès en masse), des contrôles de séparation des fonctions DOIVENT être mis en œuvre pour empêcher les abus par un acteur unique. Le standard minimum est qu'aucune identité unique ne peut à la fois initier et approuver une opération DCP à haut risque
4. **Accès limité dans le temps** : Lorsque l'accès est accordé pour un projet, une tâche ou une finalité temporaire spécifiques, les droits d'accès DOIVENT être limités dans le temps et automatiquement réexaminés à l'expiration

### Révision des droits d'accès aux DCP

Les droits d'accès aux DCP et aux systèmes de traitement des DCP DOIVENT être revus : **au minimum annuellement** pour tous les droits d'accès (certification formelle) ; **lors d'un changement de rôle** pour l'individu concerné ; **lors d'un changement organisationnel** (restructuration, changements d'unités commerciales) affectant les finalités de traitement ; **suite à un incident de protection des données** impliquant un accès non autorisé ou inapproprié aux DCP ; **à la demande du Propriétaire des données** pour le jeu de données DCP concerné.

Les révisions des droits d'accès DOIVENT être documentées. Les droits confirmés comme n'étant plus nécessaires DOIVENT être supprimés dans les 5 jours ouvrables pour l'accès standard et immédiatement pour l'accès privilégié. Les enregistrements de révision DOIVENT être conservés comme preuves.

### Accès privilégié aux DCP

L'accès privilégié aux systèmes de traitement des DCP (accès administratif, accès en masse aux données, droits d'administrateur de bases de données, accès de sauvegarde et de récupération) nécessite : la notification explicite au DPD et l'approbation du Propriétaire des données avant l'octroi ; une identité privilégiée distincte (pas combinée avec l'identité d'utilisateur standard) ; une journalisation d'audit renforcée des activités de session privilégiée impliquant des DCP ; une révision périodique plus fréquente (au minimum tous les 6 mois) ; une révocation immédiate à tout signe d'abus.

### Registre des droits d'accès

[Organisation] DOIT tenir un Registre des droits d'accès aux DCP qui documente : les identités avec accès aux DCP, par jeu de données et système ; le niveau et le périmètre d'accès accordés ; la base d'approbation et l'identité de l'approbateur ; la date d'octroi et la date de dernière révision ; la date d'expiration (pour les accès limités dans le temps). Le Registre est maintenu par l'Équipe Sécurité IT sous la supervision du DPD.

---

# Sécurité de l'information dans les accords fournisseurs (A.3.10)

## Exigences de sécurité fournisseurs pour les DCP

[Organisation] DOIT établir et convenir d'exigences pertinentes de sécurité de l'information liées au traitement des DCP avec chaque fournisseur, proportionnellement au type de relation.

### Catégorisation des fournisseurs pour les exigences DCP

| Catégorie de fournisseur | Description | Exigences minimales |
|-------------------------|-------------|---------------------|
| **Sous-traitant de DCP** | Traite directement les DCP pour le compte de [Organisation] sous instruction | Accord de sous-traitance complet per RGPD Article 28 / LPD suisse Article 9 + programme de sécurité DCP |
| **Fournisseur adjacent aux DCP** | A accès aux systèmes ou environnements contenant des DCP dans le cadre de sa prestation (ex. services IT gérés, infrastructure cloud, maintenance) | Obligation de confidentialité + restrictions de traitement des données + obligation de notification des incidents |
| **Aucun accès aux DCP** | Fournit des services sans accès aux DCP ou aux systèmes de traitement des DCP | Conditions standard de sécurité fournisseurs (ISMS-POL-A.5.19-23) — pas d'avenant spécifique aux DCP requis |

### Exigences obligatoires de sécurité DCP dans les accords fournisseurs

Pour les catégories Sous-traitant de DCP et Fournisseur adjacent aux DCP, les exigences de sécurité de l'information suivantes liées au traitement des DCP DOIVENT être établies et convenues dans l'accord fournisseur :

**Obligations de sécurité** : Engagement à mettre en œuvre et maintenir des mesures techniques et organisationnelles de sécurité appropriées pour les DCP, au moins aussi protectrices que les propres exigences de [Organisation] ; obligation de traiter les DCP uniquement selon les instructions de [Organisation] (pour les sous-traitants) ; interdiction d'utiliser les DCP à des fins propres du fournisseur.

**Confidentialité** : Le personnel du fournisseur ayant accès aux DCP est lié par des obligations de confidentialité ; les obligations de confidentialité survivent à la résiliation de l'accord.

**Notification des incidents** : Obligation de notifier [Organisation] de tout incident de sécurité DCP réel ou suspecté dans le délai spécifié dans l'accord (aligné sur les fenêtres de notification réglementaires — maximum 24 heures en cas de risque de violation de données personnelles) ; coopération à l'investigation et à la remédiation.

**Contrôle des sous-traitants ultérieurs / sous-contractants** : Consentement écrit préalable requis avant d'engager des sous-traitants ultérieurs ayant accès aux DCP de [Organisation] ; transmission des obligations de sécurité équivalentes à tout sous-traitant ultérieur.

**Droits d'audit** : Droit de [Organisation] d'auditer ou d'évaluer les mesures de sécurité DCP du fournisseur, ou de recevoir des rapports d'audit tiers (ex. certification ISO 27001, SOC 2 Type II).

**Retour et suppression** : À la résiliation ou sur demande, le fournisseur DOIT retourner ou supprimer de manière sécurisée tous les DCP, et confirmer la suppression par écrit.

**Conformité réglementaire** : Le fournisseur reconnaît le cadre réglementaire applicable (RGPD, LPD suisse) et s'engage à la conformité dans ses activités de traitement.

### Révision des accords fournisseurs

Les accords fournisseurs liés aux DCP DOIVENT être revus : au minimum annuellement, ou lors du renouvellement du contrat ; lors d'un changement matériel dans la nature des DCP traités par le fournisseur ; suite à un incident de sécurité impliquant le fournisseur ; lors d'un changement significatif des exigences réglementaires applicables ; lors de la notification d'un changement des arrangements de sous-traitants ultérieurs du fournisseur.

---

# Rôles et responsabilités

| Rôle | Responsabilités pour A.3.8–A.3.10 |
|------|----------------------------------|
| **DPD** | Approuve l'accès privilégié aux DCP ; tient la supervision du Registre des droits d'accès ; approuve les accords fournisseurs pertinents pour les DCP ; examine les décisions de catégorisation des fournisseurs ; tient le Registre des accords de sous-traitance |
| **Propriétaire des données** | Approuve le provisionnement des accès DCP pour son jeu de données ; conduit ou supervise les révisions périodiques des droits d'accès ; escalade les accès non autorisés au DPD et RSSI |
| **RSSI** | Définit les exigences techniques du cycle de vie des identités et du contrôle d'accès ; assure l'extension de la gestion des identités SGSI aux DCP per cette politique ; examine les programmes de sécurité fournisseurs |
| **Équipe Sécurité IT** | Tient le Registre des identités et le Registre des droits d'accès ; exécute le provisionnement et la désactivation des accès ; conduit les révisions des droits d'accès ; met en œuvre les contrôles d'accès privilégié |
| **Juridique/Conformité** | Examine les clauses de sécurité DCP dans les accords fournisseurs ; conseille sur les exigences contractuelles Article 28 |
| **Achats / Gestion des fournisseurs** | Assure la catégorisation DCP avant la signature de l'accord ; engage le Juridique/DPD pour les accords pertinents aux DCP ; tient l'inventaire des accords fournisseurs |
| **Direction hiérarchique** | Notifie l'Équipe Sécurité IT des changements de rôle et des départs ; approuve les demandes d'accès aux DCP pour les membres de son équipe |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Registre des identités | Toutes les identités (humaines et non humaines) avec accès aux DCP, y compris le statut du cycle de vie | En cours + 3 ans |
| Registre des droits d'accès | Droits d'accès aux DCP par identité, jeu de données et système ; enregistrements d'approbation et de révision | En cours + 3 ans |
| Enregistrements de révision des droits d'accès | Preuves documentées de la certification périodique des droits d'accès, y compris les droits supprimés | 3 ans à compter de la date de la révision |
| Inventaire des accords fournisseurs | Liste de tous les accords fournisseurs avec catégorisation DCP et référence aux clauses de sécurité DCP | En cours + 3 ans |
| Copies des accords fournisseurs | Accords signés contenant les obligations de sécurité DCP | Durée de l'accord + 3 ans |
| Enregistrements d'approbation d'accès privilégié | Notifications DPD et approbations du Propriétaire des données pour l'accès privilégié aux DCP | 3 ans à compter de la révocation de l'accès |
| Enregistrements de désactivation des identités | Preuves de suppression rapide des accès lors du départ ou du changement de rôle | 3 ans à compter de la date de désactivation |

---

# Considérations d'audit

**Pour A.3.8 (Gestion des identités)** : Registre des identités couvrant toutes les identités humaines et non humaines avec accès aux DCP ; preuves d'approbation documentée pour le provisionnement des accès DCP ; enregistrements de désactivation des identités lors du départ ou du changement de rôle ; enregistrements de révision périodique des identités non humaines.

**Pour A.3.9 (Droits d'accès)** : Registre des droits d'accès aux DCP avec droits actuels documentés ; preuves de révisions périodiques des droits d'accès (au minimum annuelles) ; enregistrements de modification ou suppression des accès suite aux changements de rôle ; enregistrements d'approbation et de révision des accès privilégiés ; preuves de séparation des fonctions pour les opérations DCP à haut risque.

**Pour A.3.10 (Accords fournisseurs)** : Enregistrements de catégorisation des fournisseurs ; accords fournisseurs signés contenant les exigences de sécurité de l'information DCP ; preuves de révision annuelle ou déclenchée des accords fournisseurs DCP ; enregistrements d'approbation des sous-traitants ultérieurs et confirmation de la transmission des obligations.

---

<!-- QA_VERIFIED: 2026-04-03 -->
