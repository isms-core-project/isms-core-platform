<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.11-12-FR:privacy:POL:a.3.11-12 -->
**PRIV-POL-A.3.11-12 — Gestion des incidents relatifs à la protection des données**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion des incidents relatifs à la protection des données |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.3.11-12 |
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
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.11-12-UG / TG
- ISMS-POL-A.5.24-28 (Cycle de vie de la gestion des incidents — parallèle SGSI)
- ISMS-POL-A.6.8 (Signalement des événements de sécurité)
- ISO/IEC 27701:2025 Contrôles A.3.11, A.3.12
- RGPD Article 33 (Notification à l'autorité de contrôle) ; Article 34 (Communication aux personnes concernées)
- LPD suisse Article 24 (Notification des violations de sécurité)

**Applicabilité du rôle** : Cette politique s'applique à l'organisation agissant à la fois comme **Responsable du traitement et comme Sous-traitant des DCP**. Les contrôles A.3.11 et A.3.12 sont des contrôles partagés (Tableau A.3). Les obligations de notification diffèrent matériellement entre les rôles de responsable et de sous-traitant et sont traitées séparément dans cette politique.

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la planification, la préparation et la réponse aux incidents de sécurité de l'information liés au traitement des DCP — conformément aux contrôles A.3.11 et A.3.12 d'ISO/IEC 27701:2025.

**Périmètre** : Tous les incidents de sécurité de l'information impliquant, affectant ou pouvant affecter la confidentialité, l'intégrité ou la disponibilité des DCP traités par [Organisation] ; tout le personnel ayant des rôles dans la détection, l'escalade, la gestion ou la notification des incidents de protection des données.

**Justification des contrôles combinés** : A.3.11 (planification et préparation) et A.3.12 (réponse) sont les deux phases de la même capacité. Une réponse efficace est impossible sans planification préalable ; une planification sans procédures de réponse testées est théorique. Ils sont mis en œuvre ensemble comme programme intégré de gestion des incidents de protection des données.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**Contrôle A.3.11 — Planification et préparation de la gestion des incidents de sécurité de l'information**
Le contrôle A.3.11 exige que [Organisation] planifie et se prépare aux incidents de sécurité de l'information liés au traitement des DCP en définissant, établissant et communiquant les processus, rôles et responsabilités de gestion des incidents qui régiront la réponse spécifique à la protection des données.

**Contrôle A.3.12 — Réponse aux incidents de sécurité de l'information**
Le contrôle A.3.12 exige que [Organisation] réponde aux incidents de sécurité de l'information liés au traitement des DCP conformément à ses procédures documentées de réponse aux incidents.

## Périmètre des incidents DCP

Les incidents suivants constituent des incidents liés aux DCP nécessitant une gestion selon cette politique : accès non autorisé aux DCP (confirmé ou suspecté) ; divulgation accidentelle de DCP à un destinataire non autorisé ; perte ou vol d'un appareil, support ou document contenant des DCP ; rançongiciel, malware ou compromission de système affectant des systèmes de traitement des DCP ; suppression ou corruption accidentelle de DCP ; traitement illicite des DCP ; notification par un fournisseur/sous-traitant d'un incident affectant les DCP de [Organisation].

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 33 (notification à l'autorité de contrôle dans les 72 heures) ; Article 34 (communication aux personnes concernées en cas de risque élevé) ; Article 5(1)(f) (principe d'intégrité et de confidentialité)
- **LPD suisse** : Article 24 (notification au PFPDT des violations susceptibles d'entraîner un risque élevé, sans délai injustifié)
- **ISO/IEC 27701:2025** : Contrôles A.3.11, A.3.12 (normatifs)

---

# Planification et préparation de la gestion des incidents de protection des données (A.3.11)

## Programme de gestion des incidents de protection des données

[Organisation] DOIT planifier et se préparer à gérer les incidents de sécurité de l'information liés au traitement des DCP comme programme défini, établi et communiqué. Ce programme étend le cadre SGSI de gestion des incidents (ISMS-POL-A.5.24-28) avec des processus, rôles et obligations spécifiques aux DCP.

### Plan de Réponse aux Incidents de Protection des Données (PRIPD)

[Organisation] DOIT maintenir un Plan de Réponse aux Incidents de Protection des Données (PRIPD) qui définit : les critères de classification des incidents DCP et les niveaux de sévérité ; les rôles et responsabilités pour la gestion des incidents de protection des données ; les chaînes d'escalade et de communication pour chaque niveau de sévérité ; la logique décisionnelle pour les notifications réglementaires ; les critères et processus de notification aux personnes concernées ; les obligations de notification aux sous-traitants (lorsque [Organisation] agit en tant que sous-traitant) ; les exigences de préservation des preuves pour les incidents DCP ; le processus de revue post-incident et de retours d'expérience.

Le PRIPD est un document contrôlé maintenu par le DPD. La structure et les exigences de contenu sont définies dans PRIV-IMP-A.3.11-12-UG.

### Classification de sévérité des incidents DCP

Les incidents DCP DOIVENT être classifiés par sévérité pour déterminer l'escalade et l'urgence de la réponse :

| Sévérité | Critères | Urgence de réponse |
|----------|----------|-------------------|
| **Critique** | Violation à grande échelle ; DCP de catégorie spéciale affectées ; forte probabilité de préjudice significatif pour les personnes concernées ; compromission systémique des systèmes de traitement des DCP | Immédiate — équipe de réponse aux incidents activée dans les 2 heures |
| **Élevée** | Violation de données personnelles confirmée ; notification réglementaire probable ; risque de préjudice significatif pour les personnes concernées ; volume significatif de DCP affectées | Même jour — DPD engagé dans les 4 heures |
| **Moyenne** | Violation suspectée en cours d'investigation ; DCP limitées affectées ; risque de préjudice faible mais non négligeable ; confinement atteint | 24 heures — DPD engagé dans les 24 heures |
| **Faible** | Quasi-incident ou événement potentiel ; aucun accès DCP confirmé ; violation procédurale sans violation réelle | Standard — évalué dans les 5 jours ouvrables |

### Exigences de préparation

[Organisation] DOIT maintenir sa préparation aux incidents de protection des données à travers : **Rôles attribués et communiqués** : tous les rôles d'incidents de protection des données définis, documentés et communiqués ; **Formation** : le personnel avec des rôles d'incidents de protection des données reçoit une formation spécifique au rôle ; **Tests** : le PRIPD DOIT être testé au minimum annuellement par des exercices de simulation ; **Maintenance des contacts** : les coordonnées des autorités de contrôle (CNIL/AEPD/CEPD/ICO pour le RGPD ; PFPDT pour la LPD suisse) et l'accès aux portails de notification DOIVENT être maintenus et actuels ; **Modèles de notification** : des projets de modèles de notification pour les autorités de contrôle et les personnes concernées DOIVENT être préparés, examinés par le Juridique/DPD, et maintenus prêts pour un déploiement rapide.

---

# Réponse aux incidents de protection des données (A.3.12)

## Exigences de réponse

Les réponses aux incidents de sécurité de l'information liés au traitement des DCP DOIVENT être menées selon les procédures documentées dans le PRIPD et PRIV-IMP-A.3.11-12-UG.

### Évaluation de la violation de données personnelles

Lorsqu'un incident lié aux DCP est détecté, [Organisation] DOIT rapidement évaluer si l'incident constitue une **violation de données personnelles** — définie comme une violation de sécurité entraînant la destruction, la perte, l'altération accidentelle ou non autorisée, ou la divulgation ou l'accès non autorisé à des données à caractère personnel.

L'évaluation DOIT considérer : si des DCP ont pu être accessibles, divulguées, perdues ou détruites sans autorisation ; les catégories et le volume approximatif de DCP impliqués ; les conséquences probables pour les personnes concernées ; si la violation est susceptible d'entraîner un risque (ou un risque élevé) pour les droits et libertés des personnes physiques.

L'évaluation et son résultat DOIVENT être documentés indépendamment de la conclusion.

### Notification réglementaire : en tant que Responsable du traitement des DCP

Lorsque [Organisation] agit en tant que Responsable du traitement des DCP et qu'une violation de données personnelles est confirmée ou raisonnablement suspectée :

**RGPD — Notification à l'autorité de contrôle (Article 33)** :

Le délai de 72 heures commence lorsque [Organisation] a une certitude raisonnable qu'une violation de données personnelles s'est produite — pas au moment de la première suspicion. Lorsque l'enquête initiale est non concluante, le délai commence lorsque des faits suffisants sont établis pour confirmer qu'une violation s'est produite. Une enquête prolongée sans détermination préliminaire n'est pas acceptable ; lorsqu'une violation ne peut être exclue dans les 24 heures, le DPD DOIT effectuer une notification provisoire à l'autorité de contrôle et la compléter au fur et à mesure.

- LORSQUE la violation est susceptible d'entraîner un risque pour les droits et libertés des personnes physiques : notifier l'autorité de contrôle compétente **sans délai injustifié et, lorsque c'est possible, au plus tard 72 heures** après en avoir pris connaissance
- LORSQUE la notification est faite après 72 heures : inclure une justification motivée du retard
- LORSQUE la violation n'est pas susceptible d'entraîner un risque : notification non requise, mais la violation DOIT être documentée dans le registre des violations
- Contenu de la notification : nature de la violation ; catégories et nombre approximatif de personnes concernées ; catégories et nombre approximatif d'enregistrements ; nom/contact du DPD ; conséquences probables ; mesures prises ou proposées

**LPD suisse — Notification au PFPDT (Article 24)** : LORSQUE la violation est susceptible d'entraîner un risque élevé pour la personnalité ou les droits fondamentaux des personnes concernées : notifier le PFPDT **dès que possible** selon le format spécifié par le PFPDT.

**RGPD — Communication aux personnes concernées (Article 34)** : LORSQUE la violation est susceptible d'entraîner un **risque élevé** pour les droits et libertés des personnes concernées : communiquer aux personnes concernées affectées **sans délai injustifié** ; la communication peut être retardée pour des raisons d'application de la loi (coordination avec le Juridique requise).

### Notification réglementaire : en tant que Sous-traitant des DCP

Lorsque [Organisation] agit en tant que Sous-traitant des DCP et qu'une violation (ou violation potentielle) affectant les DCP d'un client est détectée : notifier le Responsable du traitement (client) **sans délai injustifié** dès qu'une violation est confirmée ou raisonnablement suspectée — la notification n'est pas conditionnée à l'achèvement de l'enquête interne. La notification du sous-traitant permet au Responsable du traitement de commencer sa propre échéance de 72 heures ; [Organisation] ne DOIT PAS retarder la notification en attente d'une confirmation complète. Délai maximal de notification : 24 heures à compter du moment où [Organisation] prend connaissance qu'une violation s'est produite ou est raisonnablement suspectée. La notification DOIT être faite au contact de sécurité ou de protection des données désigné par le client dans l'accord de sous-traitance. [Organisation] NE DOIT PAS notifier directement l'autorité de contrôle ou les personnes concernées sauf autorisation explicite du Responsable du traitement ou obligation légale indépendante.

### Actions de réponse aux incidents

La réponse aux incidents de protection des données DOIT inclure, par ordre de priorité :

1. **Contenir** : Arrêter la violation en cours ou empêcher toute exposition supplémentaire des DCP
2. **Évaluer** : Déterminer le périmètre, les catégories de DCP affectées, le volume et les personnes concernées
3. **Préserver** : Sécuriser les preuves (journaux, enregistrements, systèmes affectés) — coordonner avec le RSSI per ISMS-POL-A.5.24-28
4. **Notifier** : Exécuter les notifications réglementaires et aux personnes concernées selon les seuils applicables
5. **Récupérer** : Rétablir le traitement des DCP à un fonctionnement normal avec des garanties appropriées
6. **Examiner** : Conduire une revue post-incident ; mettre à jour le PRIPD et les contrôles selon les besoins

### Registre des violations de la protection des données

[Organisation] DOIT maintenir un Registre des violations de la protection des données enregistrant toutes les violations de données personnelles, qu'une notification réglementaire ait été requise ou non. Le registre DOIT inclure : référence de l'incident et date de découverte ; nature de la violation et catégories de DCP affectées ; nombre approximatif de personnes concernées et d'enregistrements ; résultat de l'évaluation des risques ; décisions de notification et dates ; actions de remédiation prises ; référence de la revue post-incident.

Le DPD tient le Registre des violations. Conservation : minimum 5 ans.

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **DPD** | Responsable des incidents de protection des données — active le PRIPD ; prend les décisions de notification réglementaire ; communique avec les autorités de contrôle ; approuve les communications aux personnes concernées ; tient le Registre des violations ; dirige la revue post-incident |
| **RSSI** | Responsable technique des incidents — coordonne le confinement et la récupération ; préserve les preuves légales ; gère l'enquête technique |
| **Juridique/Conformité** | Conseils juridiques sur les obligations de notification ; examine les notifications à l'autorité de contrôle ; conseille sur les obligations du sous-traitant |
| **Champions de la protection des données** | Premier point d'escalade pour le personnel signalant des incidents DCP dans leur unité ; triage initial et escalade au DPD |
| **Équipe Sécurité IT** | Investigation et confinement technique ; isolation et récupération du système ; préservation des preuves per ISMS-POL-A.5.24-28 |
| **Direction générale** | Informée de tous les incidents Élevés et Critiques ; approuve les communications de crise ; soutient l'engagement réglementaire au niveau senior |
| **Communications** | Rédaction des notifications aux personnes concernées (avec approbation DPD) ; gestion des relations publiques |
| **Tout le personnel** | Signale immédiatement les incidents DCP suspectés à leur Champion de la protection des données ou directement au DPD ; préserve les preuves ; coopère à l'enquête |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Plan de Réponse aux Incidents de Protection des Données (PRIPD) | Version approuvée actuelle avec rôles, processus, logique décisionnelle de notification | En cours + 3 ans |
| Registre des violations de la protection des données | Enregistrement de toutes les violations de données personnelles avec évaluation des risques et décisions de notification | 5 ans |
| Notifications aux autorités de contrôle | Copies de toutes les notifications Article 33 / LPD Article 24 soumises | 5 ans |
| Communications aux personnes concernées | Copies des communications Article 34 aux personnes concernées | 5 ans |
| Enregistrements de test du PRIPD | Preuves des exercices de simulation annuels avec conclusions et améliorations | 3 ans |
| Enregistrements de chronologie de réponse aux incidents | Preuves de conformité à la fenêtre de notification de 72 heures (ou justification du retard) | 5 ans |
| Rapports de revue post-incident | Retours d'expérience et actions d'amélioration du PRIPD/contrôles | 3 ans |

---

# Considérations d'audit

**Pour A.3.11 (Planification et préparation)** : PRIPD documenté avec processus et rôles spécifiques aux DCP ; preuves que les rôles sont attribués et le personnel est conscient de ses responsabilités ; enregistrements de test annuel du PRIPD ; coordonnées des autorités de contrôle maintenues à jour ; modèles de notification préparés et examinés.

**Pour A.3.12 (Réponse)** : Registre des violations avec tous les incidents enregistrés, y compris les déterminations de non-notification ; pour les violations notifiées : notifications dans la fenêtre de 72 heures (ou justification du retard documentée) ; documentation d'évaluation des violations pour les incidents Élevés/Critiques ; rapports de revue post-incident avec actions suivies jusqu'à la réalisation ; preuves que les obligations de notification du sous-traitant ont été remplies (notification rapide au client lorsqu'agissant en tant que sous-traitant).

---

<!-- QA_VERIFIED: 2026-04-03 -->
