<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.24-28-FR:operational:OP-POL:a.5.24-28 -->
**ISMS-OP-POL-A.5.24-28 — Gestion des incidents**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion des incidents |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.24-28 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôles A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 — Planification, évaluation, réponse, enseignements et collecte de preuves en matière d'incidents

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la gestion des incidents |
|----------|---------------------------------------|
| A.5.5–6 Contact avec les autorités et les groupes d'intérêt spécial | Obligations de signalement externe (PFPDT, forces de l'ordre, CERT) |
| A.5.7 Renseignement sur les menaces | Le renseignement sur les menaces éclaire la détection et la réponse aux incidents |
| A.5.29 Sécurité de l'information lors d'une perturbation | Activation du plan de continuité d'activité lors d'incidents majeurs |
| A.5.34 Vie privée et protection des DCP | Exigences de notification des violations de données personnelles |
| A.6.8 Signalement des événements de sécurité de l'information | Le signalement par les utilisateurs des événements de sécurité alimente le triage des incidents |
| A.8.15 Journalisation | Les données de journaux soutiennent la détection des incidents et l'analyse légale |
| A.8.16 Surveillance des activités | La surveillance détecte les événements de sécurité pour le triage des incidents |

**Politiques internes connexes** :

- Politique de contrôle d'accès
- Politique de journalisation
- Politique de surveillance des activités (A.8.16)
- Politique de continuité d'activité
- Politique de vie privée et de protection des DCP
- Politique de classification et de traitement de l'information

---

# Politique de gestion des incidents

## Objet

La présente politique fournit des orientations sur la gestion des incidents de sécurité de l'information de manière structurée, notamment l'identification, l'évaluation, la réponse et la résolution des événements et incidents de sécurité, ainsi que l'identification, la collecte, l'acquisition et la préservation d'informations pouvant servir de preuves.

Cette politique soutient la nLPD suisse (revDSG) et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre des procédures de notification des violations et des mesures techniques et organisationnelles proportionnées aux risques. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les systèmes d'information, applications et services considérés dans le périmètre de la déclaration de périmètre ISO 27001.

## Principe

Tous les événements de sécurité de l'information doivent être signalés et évalués. Les incidents confirmés doivent être gérés par un processus de réponse structuré avec des rôles définis, des voies d'escalade et des procédures de communication. L'organisation doit tirer des enseignements des incidents pour améliorer sa posture de sécurité. Lorsque des incidents peuvent conduire à des investigations externes ou à des poursuites judiciaires, des ressources externes spécialisées doivent être engagées.

---

## Définitions

| Terme | Définition |
|-------|-----------|
| **Événement de sécurité** | Occurrence identifiée indiquant une possible violation de la politique de sécurité ou une défaillance des contrôles. Tous les événements ne constituent pas des incidents. |
| **Incident de sécurité** | Événement de sécurité qui a été évalué et confirmé comme ayant un effet négatif réel ou potentiel sur la confidentialité, l'intégrité ou la disponibilité des informations. |
| **Violation de données personnelles** | Incident de sécurité impliquant la destruction, la perte, l'altération, la divulgation non autorisée ou l'accès non autorisé accidentel ou illicite à des données personnelles. |
| **Incident significatif** | Incident constituant une violation légale ou réglementaire, pouvant conduire à une investigation externe ou à des poursuites judiciaires, ou créant un risque élevé pour les personnes concernées. |

---

## Signalement des incidents

Tous les employés et utilisateurs tiers doivent signaler immédiatement les événements de sécurité dès leur découverte à l'équipe de management de la sécurité de l'information via les canaux de signalement désignés :

- **Principal** : Service d'assistance IT (e-mail, téléphone ou système de gestion des tickets).
- **Alternatif** : Contact direct avec l'équipe de management de la sécurité de l'information (liste de distribution par e-mail ou téléphone).
- **En dehors des heures de bureau** : Contact de sécurité d'astreinte (téléphone ou messagerie).
- **Anonyme** : Lorsque les employés souhaitent signaler des préoccupations de manière anonyme, les signalements peuvent être soumis via le mécanisme de signalement éthique ou de lanceur d'alerte de l'organisation.

Les canaux de signalement doivent être communiqués lors de l'intégration et de la formation annuelle de sensibilisation, et publiés sur l'intranet de l'organisation.

Les signalements doivent inclure, dans la mesure du possible :

- Ce qui a été observé (description de l'événement).
- Quand cela s'est produit ou a été découvert.
- Quels systèmes, données ou personnes sont concernés.
- Toute action déjà prise.

Les événements de sécurité peuvent également être détectés par surveillance automatisée, analyse des journaux ou notification par des tiers.

Les employés ne doivent pas tenter d'enquêter ou de résoudre eux-mêmes les incidents suspectés. La préservation des preuves est prioritaire sur la curiosité.

---

## Évaluation et triage des événements

L'équipe de management de la sécurité de l'information doit évaluer tous les événements de sécurité signalés pour déterminer s'ils constituent un incident de sécurité.

L'évaluation doit prendre en compte :

- La nature et la portée de l'événement.
- La classification des informations affectées.
- Le nombre de personnes concernées ou de systèmes affectés.
- Si des données personnelles sont impliquées (violation potentielle de données).
- L'impact commercial, juridique ou réglementaire potentiel.

Les événements ne satisfaisant pas au seuil d'un incident doivent être journalisés et les tendances doivent être surveillées.

### Registre des incidents

Tous les événements de sécurité signalés et les incidents confirmés doivent être enregistrés dans le registre des incidents avec les champs minimaux suivants :

| Champ | Description |
|-------|-------------|
| Identifiant de l'incident | Identifiant unique (p. ex. INC-2026-001) |
| Date/heure de signalement | Quand l'événement a été signalé |
| Date/heure de détection | Quand l'événement s'est produit ou a été détecté pour la première fois |
| Déclarant | Qui a signalé l'événement |
| Description | Résumé de ce qui s'est passé |
| Systèmes/données affectés | Quels systèmes, applications ou types de données sont impliqués |
| Niveau de classification | Classification des informations affectées |
| Données personnelles impliquées | Oui/Non ; si oui, catégories et nombre estimé de personnes concernées |
| Gravité | Critique / Élevée / Moyenne / Faible |
| Statut | Ouvert / En cours d'investigation / Contenu / Résolu / Clôturé |
| Assigné à | Responsable de l'incident ou équipe |
| Cause profonde | Déterminée après investigation |
| Actions prises | Actions de confinement, d'éradication, de reprise avec horodatages |
| Enseignements tirés | Référence à la révision post-incident (si effectuée) |
| Date de clôture | Quand l'incident a été officiellement clôturé |

---

## Classification des incidents

Les incidents confirmés doivent être classifiés par gravité pour déterminer la priorité de réponse, l'escalade et les exigences de communication :

| Gravité | Description | Exemples | Réponse initiale |
|---------|-------------|----------|-----------------|
| **Critique** | Violation de données avérée, interruption totale du service, compromission active de systèmes critiques | Rançongiciel, exfiltration de données, compromission des systèmes d'authentification | Immédiate (dans l'heure) |
| **Élevée** | Impact significatif sur les fonctions principales, exposition potentielle de données, attaque ciblée | Logiciel malveillant sur plusieurs points de terminaison, accès non autorisé à des données sensibles, campagne de phishing ciblant les dirigeants | Dans les 4 heures |
| **Moyenne** | Impact limité, contenu à un seul système ou utilisateur, aucune perte de données confirmée | Détection de logiciel malveillant unique, violation de politique, tentative d'intrusion échouée | Dans 1 jour ouvrable |
| **Faible** | Impact minimal, aucune donnée impliquée, informatif | Augmentation du spam, écart mineur de politique, schéma de connexion échouée unique | Dans 3 jours ouvrables |

La gravité peut être escaladée à tout moment pendant le cycle de vie de l'incident à mesure que de nouvelles informations émergent.

---

## Réponse aux incidents

### Cycle de vie de la réponse

Les incidents doivent être gérés à travers les phases suivantes, conformément à NIST SP 800-61 :

1. **Confinement** — Limiter l'impact et prévenir tout dommage supplémentaire. Des actions de confinement à court terme (p. ex. isoler les systèmes affectés, désactiver les comptes compromis) doivent être prises immédiatement. Des stratégies de confinement à long terme doivent être planifiées lorsque l'éradication ne peut pas être immédiate.

2. **Éradication** — Éliminer la cause profonde de l'incident. Cela peut inclure la suppression de logiciels malveillants, la résolution de vulnérabilités, la réinitialisation des identifiants compromis ou la reconstruction des systèmes affectés.

3. **Reprise** — Restaurer les systèmes et services en opération normale. La reprise doit être vérifiée par des tests avant de remettre les systèmes en production. La surveillance doit être renforcée pendant la période de reprise pour détecter toute récurrence.

4. **Révision post-incident** — Effectuer une révision structurée après la résolution (voir section Enseignements tirés ci-dessous).

Toutes les actions de réponse aux incidents doivent être documentées avec des horodatages, les actions prises et le personnel impliqué.

### Équipe de réponse aux incidents

Les rôles suivants doivent être assignés au sein des capacités de réponse aux incidents :

| Rôle | Responsabilité | Assigné à |
|------|----------------|-----------|
| **Chef de l'équipe de réponse aux incidents** | Coordination globale de la réponse aux incidents ; décisions d'escalade ; communication avec la direction générale | RSSI ou Responsable de la sécurité IT |
| **Responsable technique** | Investigation technique, confinement et éradication ; préservation des preuves | Analyste senior en sécurité IT ou Responsable des opérations IT |
| **Responsable des communications** | Communications internes et externes ; liaison avec les médias (si nécessaire) | RSSI ou porte-parole désigné |
| **Conseiller juridique** | Conseils juridiques sur les obligations de notification, la gestion des preuves, les exigences réglementaires | Conseiller juridique (interne ou externe) |
| **Liaison métier** | Évaluation de l'impact sur l'activité ; coordination avec les unités métier affectées | Chef de département ou coordinateur de la continuité d'activité |

Les assignations de rôles doivent être documentées, communiquées à tous les membres de l'équipe et révisées annuellement. Des suppléants doivent être désignés pour chaque rôle afin de garantir la disponibilité.

### Escalade

Le chef de l'équipe de réponse aux incidents doit escalader les incidents à la direction générale lorsque :

- L'incident est classifié Critique ou Élevé.
- L'incident implique des données personnelles (notification potentielle d'une violation de données).
- L'incident peut nécessiter une notification externe (réglementaire, forces de l'ordre, clients).
- L'incident dépasse les capacités ou l'autorité de l'équipe de réponse.
- L'incident n'a pas été contenu dans le délai prévu.

### Communication

Les informations relatives aux incidents doivent être partagées sur la base d'un strict besoin d'en connaître. La communication pendant un incident actif doit être coordonnée par le chef de l'équipe de réponse aux incidents.

Des mises à jour de statut internes doivent être fournies à intervalles réguliers pour les incidents Critiques et Élevés.

La communication externe (médias, clients, partenaires) doit être approuvée par la direction générale et examinée par le conseiller juridique avant sa diffusion.

---

## Incidents significatifs

Les incidents significatifs sont définis comme des incidents constituant une violation légale ou réglementaire, pouvant conduire à une investigation externe ou à des poursuites judiciaires.

### Orientations générales

Dans tous les cas où une situation peut conduire à une investigation externe ou à des poursuites judiciaires, des ressources externes spécialisées doivent être engagées.

Dès que possible, tout travail sur, accès à, modification de ou altération des systèmes, documents, emplacements, fichiers, bases de données, applications ou autres entités dans le périmètre affectés doit cesser. Les seules exceptions sont la préservation de la vie, de la santé et de la sécurité, ou les actions minimales nécessaires pour le triage et la mise en sécurité.

### Processus

1. Nommer un Chef d'équipe pour incidents significatifs issu de l'équipe de direction générale comme point de contact et de coordination unique.
2. Suivre les orientations ci-dessus pour arrêter et mettre en sécurité.
3. Contacter immédiatement le conseiller juridique.
4. Contacter immédiatement un fournisseur de criminalistique informatique et d'investigation d'une entreprise qualifiée et autorisée.
5. Le cas échéant, contacter les autorités compétentes, notamment les forces de l'ordre, le Préposé fédéral à la protection des données et à la transparence (PFPDT) et tout régulateur sectoriel applicable.
6. Si une couverture d'assurance cyber est détenue, informer immédiatement la compagnie d'assurance.
7. Suivre les orientations du conseiller juridique, des forces de l'ordre, des enquêteurs légaux et des assureurs, tout en suivant le processus de gestion des incidents pour l'enregistrement, le suivi et la gestion de l'incident.

---

## Notification des violations de données

Lorsqu'un incident implique des données personnelles (une violation de données personnelles), les exigences de notification suivantes s'appliquent :

### Notification nLPD suisse

| Notification | Déclencheur | Délai |
|--------------|-------------|-------|
| **PFPDT** (Préposé fédéral à la protection des données et à la transparence) | Violation de données susceptible d'entraîner un **risque élevé** pour la personnalité ou les droits fondamentaux des personnes concernées | **Dès que possible** après avoir eu connaissance de la violation |
| **Personnes concernées** | Lorsque la notification est nécessaire pour la protection des personnes concernées, ou lorsque le PFPDT le demande | **Dès que possible** (aucun délai fixe) |
| **Sous-traitant → Responsable du traitement** | Le sous-traitant découvre une violation impliquant les données personnelles du responsable du traitement | **Dès que possible** après la découverte |

### Notification RGPD de l'UE (le cas échéant)

| Notification | Déclencheur | Délai |
|--------------|-------------|-------|
| **Autorité de contrôle** | Toute violation de données personnelles sauf si elle est peu susceptible d'entraîner un risque pour les droits et libertés | **Dans les 72 heures** après en avoir eu connaissance |
| **Personnes concernées** | Violation susceptible d'entraîner un **risque élevé** pour les droits et libertés | **Dans les meilleurs délais** |

Lorsque la nLPD et le RGPD s'appliquent tous les deux, l'organisation doit respecter le délai le plus strict (72 heures).

### Contenu des notifications

Les notifications de violation aux autorités de contrôle doivent inclure, au minimum :

| Élément | nLPD (art. 24) | RGPD (art. 33) |
|---------|----------------|----------------|
| Nature de la violation | Requis | Requis (y compris les catégories et le nombre approximatif de personnes concernées et d'enregistrements) |
| Conséquences et risques | Requis | Requis (conséquences probables) |
| Mesures prises ou prévues | Requis | Requis (mesures prises ou proposées pour remédier et atténuer) |
| Point de contact | Requis (auprès duquel le PFPDT ou les personnes concernées peuvent obtenir des informations supplémentaires) | Requis (nom et coordonnées du DPD ou autre point de contact) |

Lorsque toutes les informations ne sont pas disponibles au moment de la notification, elles doivent être fournies par phases dans les meilleurs délais.

### Évaluation de la violation

Tous les incidents de sécurité impliquant des données personnelles ne nécessitent pas de notification. L'équipe de réponse aux incidents doit évaluer :

- La nature et la sensibilité des données personnelles impliquées.
- Le nombre de personnes concernées affectées.
- La gravité et la probabilité des conséquences pour les personnes concernées.
- Si les données étaient chiffrées ou autrement rendues inintelligibles.
- Si la violation a été contenue et le risque atténué.

L'évaluation et la décision (y compris la justification de ne pas notifier, le cas échéant) doivent être documentées.

---

## Collecte et préservation des preuves

Lorsqu'un incident peut nécessiter une analyse légale, une action judiciaire ou une investigation réglementaire, les preuves doivent être collectées et préservées selon les principes suivants :

### Gestion des preuves

- Les preuves doivent être collectées dès que possible après l'identification de l'incident.
- Les preuves originales ne doivent pas être accédées, modifiées ou analysées directement. Des copies légales (images bit à bit) doivent être créées à l'aide d'outils de protection contre l'écriture.
- Toutes les preuves doivent être vérifiées à l'aide de fonctions de hachage cryptographiques (SHA-256 minimum) pour confirmer leur intégrité.

### Chaîne de possession

Un registre de chaîne de possession doit être maintenu pour toutes les preuves, documentant :

- Ce qui a été collecté (description, numéros de série, identifiants).
- Quand cela a été collecté (date, heure).
- Qui l'a collecté.
- Où cela est stocké.
- Qui y a eu accès et quand.
- Tout transfert entre dépositaires.

### Stockage des preuves

- Les preuves doivent être stockées dans un emplacement sécurisé avec accès restreint.
- Les preuves numériques doivent être stockées sur des supports chiffrés.
- Les preuves physiques doivent être stockées dans un conteneur verrouillé et inviolable.
- Les preuves doivent être conservées pendant un minimum de **12 mois** à compter de la clôture de l'incident, ou plus longtemps lorsque le conseil juridique, les exigences réglementaires ou les procédures en cours le requièrent.

### Support légal externe

Pour les incidents significatifs, des enquêteurs légaux externes qualifiés doivent être engagés. L'organisation doit identifier et pré-approuver au moins un prestataire légal externe et maintenir des coordonnées et des conditions d'engagement à jour (mandat ou conditions de référence pré-approuvées). Le personnel interne ne doit pas effectuer d'analyse légale à moins d'être formé et qualifié pour le faire.

---

## Enseignements tirés

Une révision post-incident doit être effectuée pour tous les incidents de gravité Critique et Élevée, et optionnellement pour les incidents de gravité Moyenne lorsque des enseignements utiles peuvent en être tirés.

### Processus de révision

La révision doit avoir lieu dans les 5 jours ouvrables suivant la résolution de l'incident, pendant que les détails sont encore frais. La révision doit inclure tout le personnel ayant contribué à la réponse.

La révision doit documenter :

- **Chronologie** : Une chronologie factuelle de l'incident depuis la détection jusqu'à la résolution.
- **Cause profonde** : La cause sous-jacente de l'incident (pas seulement le déclencheur).
- **Ce qui a bien fonctionné** : Actions de réponse efficaces, mesures de confinement réussies, bonne coordination d'équipe.
- **Ce qui pourrait être amélioré** : Lacunes dans la détection, retards de réponse, problèmes de communication, outils ou procédures manquants.
- **Plan d'action** : Améliorations spécifiques et mesurables avec un responsable assigné et un délai.

### Suivi

- Les plans d'action doivent être suivis jusqu'à leur réalisation.
- Les enseignements tirés doivent être communiqués au personnel concerné.
- Le plan de réponse aux incidents doit être mis à jour lorsque les résultats indiquent des lacunes.
- Les tendances entre les incidents doivent être examinées trimestriellement pour identifier les problèmes systémiques.

Les révisions doivent être effectuées de manière non punitive, en se concentrant sur l'amélioration des systèmes et des processus plutôt que sur les fautes individuelles.

---

## Test du plan de réponse aux incidents

Le plan de réponse aux incidents doit être testé au moins **annuellement** par des exercices de simulation ou des tests sur table pour vérifier que :

- Les rôles et responsabilités sont compris.
- Les canaux de communication fonctionnent correctement.
- Les voies d'escalade sont claires et efficaces.
- Les procédures de collecte des preuves sont pratiques.
- Les délais de notification des violations de données peuvent être respectés.

**Scénarios de test minimaux** (faire pivoter annuellement) :

| Scénario | Tests | Fréquence |
|----------|-------|-----------|
| Attaque par rançongiciel avec chiffrement des données | Confinement, reprise à partir de la sauvegarde, communication, décision de payer/ne pas payer | Au moins tous les 2 ans |
| Violation de données personnelles avec obligation de notification | Évaluation de la violation, processus de notification au PFPDT, notification aux personnes concernées | Au moins tous les 2 ans |
| Menace interne / compte à privilèges compromis | Détection, révocation des accès, préservation des preuves, coordination RH | Au moins tous les 2 ans |
| Compromission de messagerie professionnelle / ingénierie sociale | Détection, vérification des contrôles financiers, signalement de l'incident | Au moins tous les 2 ans |

Les résultats des tests et les améliorations doivent être documentés, y compris les participants, les détails du scénario, les lacunes observées et les mesures correctives avec responsables et délais.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

- **Registre des incidents** (tous les événements signalés et incidents confirmés avec gravité, statut, résolution) — *maintenu en continu ; révisé trimestriellement pour les tendances*
- **Enregistrements de réponse aux incidents** (actions de confinement, d'éradication, de reprise avec horodatages) — *conservés pendant un minimum de 3 ans*
- **Évaluations des violations de données et enregistrements de notification** (y compris les décisions de ne pas notifier, avec justification) — *conservés pendant 5 ans*
- **Registres de chaîne de possession** pour les preuves légales — *conservés pendant la durée de toute procédure judiciaire plus 2 ans*
- **Rapports de révision post-incident** avec plans d'action et suivi de réalisation — *complétés dans les 5 jours ouvrables suivant la résolution ; actions suivies jusqu'à la clôture*
- **Enregistrements de tests de réponse aux incidents** (exercices sur table, simulations) — *annuels ; conservés pendant 3 ans*
- **Liste de contacts pour la réponse aux incidents** (équipe interne, conseiller juridique, prestataire légal pré-approuvé, PFPDT, assureur cyber) — *révisée trimestriellement ; mise à jour lors de tout changement*
- **Modèles de communication** (notification interne, notification externe, notification des personnes concernées, déclaration aux médias) — *pré-approuvés par le conseiller juridique ; révisés annuellement*

### Indicateurs de gestion des incidents

Les indicateurs suivants doivent être rapportés trimestriellement au RSSI et à l'Équipe de révision de la direction :

| Indicateur | Description |
|-----------|-------------|
| Total des événements signalés | Volume d'événements de sécurité reçus |
| Événements convertis en incidents | Nombre et pourcentage d'événements classifiés comme incidents |
| Incidents par gravité | Répartition Critique / Élevée / Moyenne / Faible |
| Délai moyen de détection (MTTD) | Délai moyen entre l'occurrence de l'événement et la détection |
| Délai moyen de réponse (MTTR) | Délai moyen entre la détection et le confinement |
| Délai moyen de résolution | Délai moyen entre la détection et la clôture |
| Incidents en retard | Incidents dépassant les délais de réponse cibles |
| Violations de données signalées | Nombre nécessitant une notification au PFPDT ou à une autorité de contrôle |
| Révisions post-incident complétées | Pourcentage d'incidents Critiques/Élevés avec révisions complétées |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment, sans s'y limiter, les indicateurs de réponse aux incidents, la réalisation des révisions post-incident, les enregistrements de tests, les audits internes et externes, ainsi que les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec une acceptation du risque documentée, des mesures compensatoires et une date de révision définie. Les exceptions doivent être rapportées à l'Équipe de révision de la direction.

## Non-conformité

Un employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les modifications des normes de gestion des incidents, les exigences réglementaires de notification, les menaces émergentes et les enseignements tirés des incidents et des exercices.

---

# Domaines de la norme ISO 27001 couverts

Politique de gestion des incidents — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | **5.24 Planification et préparation de la gestion des incidents de sécurité de l'information** |
| Clause 8.1 Planification et contrôle opérationnels | **5.25 Évaluation et décision sur les événements de sécurité de l'information** |
| | **5.26 Réponse aux incidents de sécurité de l'information** |
| | **5.27 Enseignements tirés des incidents de sécurité de l'information** |
| | **5.28 Collecte de preuves** |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 6.8 Signalement des événements de sécurité de l'information |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 24 — Notification des violations de données au PFPDT (« dès que possible ») |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 33–34 — Notification des violations (72 heures à l'autorité, dans les meilleurs délais aux personnes concernées) |
| ISO/IEC 27001:2022 | Contrôles Annexe A 5.24, 5.25, 5.26, 5.27, 5.28 |
| ISO/IEC 27002:2022 | Sections 5.24–5.28 — Lignes directrices de mise en œuvre |
| ISO/IEC 27037:2012 | Lignes directrices pour l'identification, la collecte, l'acquisition et la préservation des preuves numériques |
| NIST SP 800-61 Rev 2 | Guide de gestion des incidents de sécurité informatique (cycle de vie en quatre phases) |
| CIS Controls v8 | Contrôle 17 (Gestion de la réponse aux incidents) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
