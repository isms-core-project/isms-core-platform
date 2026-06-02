<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.12-FR:cloud:POL:a.12 -->
**CLD-PII-POL-A.12 — Conformité en matière de protection des données**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Conformité en matière de protection des données |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-PII-POL-A.12 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) / RSSI |
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
| 1.0 | [Date] | DPD / RSSI | Politique initiale pour l'implémentation d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors de changements significatifs de réglementation, d'empreinte de service ou de résidence des données)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : Délégué à la Protection des Données (DPD)
- Secondaire : RSSI / Responsable Sécurité Cloud
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection de la vie privée et des DCP)
- ISMS-POL-A.5.19-23 (Relations avec les fournisseurs et les tiers)
- CLD-PII-POL-A.1 (Généralités)
- CLD-PII-POL-A.8 (Ouverture, transparence — divulgation des sous-traitants ultérieurs)
- CLD-PII-POL-A.11 (§11.12 — Traitement des DCP sous-traité)
- ISO/IEC 27018:2025 Annexe A, Section A.12 et Contrôles A.12.1–A.12.2
- ISO/IEC 27701:2025 Contrôles A.2.5.2 (base du transfert de DCP entre juridictions) et A.2.5.3 (pays et organisations internationales vers lesquels les DCP peuvent être transférées)
- RGPD Articles 28(3)(a) (le sous-traitant traite uniquement sur instructions documentées) ; Articles 44–49 (transferts vers des pays tiers) ; Article 46 (garanties appropriées pour les transferts internationaux)
- LPD suisse Articles 16–17 (transferts internationaux de données personnelles) ; Article 9(3) (obligations du sous-traitant sur les sous-traitants ultérieurs et les emplacements)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en tant que sous-traitant de DCP en cloud public en matière de conformité à la protection des données — spécifiquement l'obligation de divulguer les emplacements géographiques où les DCP sont stockées, traitées ou transitent, de respecter les exigences de résidence des données imposées par les responsables du traitement des DCP, et de documenter et communiquer toutes les destinations prévues des DCP, y compris les transferts internationaux et leur base juridique — conformément à la Section A.12 et aux Contrôles A.12.1 et A.12.2 de l'Annexe A d'ISO/IEC 27018:2025.

**Périmètre** : Toutes les DCP traitées par [Organisation] pour le compte des responsables du traitement des DCP, dans toutes les régions d'infrastructure, zones de disponibilité et emplacements de sous-traitants ultérieurs.

**Justification des contrôles combinés** : A.12.1 et A.12.2 traitent de la dimension géographique de la transparence du traitement des DCP. A.12.1 établit l'obligation de divulguer où résident les DCP ; A.12.2 établit l'obligation d'identifier toutes les destinations vers lesquelles les DCP peuvent transiter et de documenter la base juridique de tout transfert en dehors de la juridiction du responsable du traitement. Ensemble, ces contrôles permettent aux responsables du traitement des DCP de remplir leurs propres obligations de responsabilité en matière de transfert conformément à l'Article 44+ du RGPD et aux législations nationales équivalentes.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27018:2025

**Section A.12 — Conformité en matière de protection des données (principe)**

La Section A.12 établit le principe qu'un sous-traitant de DCP en cloud public doit maintenir et divulguer aux responsables du traitement les emplacements géographiques où les DCP sont stockées, traitées ou transmises, mettre en œuvre des mécanismes pour appliquer les exigences de résidence des données, et documenter la base juridique de tout transfert transfrontalier.

**Contrôle A.12.1 — Emplacement géographique des DCP**

Le Contrôle A.12.1 exige que le sous-traitant divulgue tous les pays et régions impliqués dans le traitement des DCP — y compris les emplacements des sous-traitants ultérieurs — fournisse un préavis avant de modifier ces emplacements, et applique techniquement toute restriction de résidence convenue avec le responsable du traitement.

**Contrôle A.12.2 — Destination prévue des DCP**

Le Contrôle A.12.2 exige que le sous-traitant documente et communique toutes les destinations prévues pour les transferts de DCP, y compris le mécanisme de transfert applicable et les garanties pour chaque flux transfrontalier ou transjuridictionnel.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 28(3)(a) (le sous-traitant traite uniquement conformément aux instructions du responsable du traitement, y compris sur l'emplacement) ; Articles 44–49 (interdiction des transferts vers des pays tiers sans protection adéquate sauf garanties appropriées) ; Article 46 (clauses contractuelles types, règles d'entreprise contraignantes, codes de conduite comme mécanismes de transfert) ; Article 30 (registre des activités de traitement incluant les destinataires et les pays tiers)
- **LPD suisse** : Articles 16–17 (interdiction de transfert de données personnelles vers des pays sans protection adéquate ; garanties reconnues) ; Article 9(3) (obligations du sous-traitant en matière de sous-traitance et d'emplacement)
- **ISO/IEC 27018:2025** : Contrôles A.12.1, A.12.2

---

# Énoncés de politique : Emplacement géographique des DCP (A.12.1)

## Divulgation de l'emplacement

[Organisation] DOIT maintenir un **Registre des emplacements de traitement des DCP** documentant tous les pays et régions dans lesquels les DCP sont stockées, traitées ou transitent dans le cadre de la prestation de services cloud. Le registre DOIT couvrir :

- **Emplacements de stockage primaires** : Centres de données et régions cloud où les DCP au repos résident
- **Emplacements de traitement** : Régions de calcul où les DCP sont activement traitées
- **Routes de transit** : Régions par lesquelles les DCP peuvent passer lors d'opérations de réplication, de sauvegarde ou de livraison
- **Emplacements des sous-traitants ultérieurs** : Tous les emplacements géographiques des sous-traitants ultérieurs engagés conformément à CLD-PII-POL-A.11 (§11.12)

Le Registre des emplacements de traitement des DCP DOIT être mis à la disposition des responsables du traitement des DCP sur demande. Une version résumée — couvrant les emplacements de stockage et de traitement primaires ainsi que les pays des sous-traitants ultérieurs, mais omettant les informations détaillées sur les routes de transit — DOIT être publiée sur le portail de confiance de [Organisation] pour les responsables du traitement opérant sous autorisation générale. Les responsables du traitement authentifiés peuvent demander le registre complet via le portail de confiance ou directement auprès du DPD. Les informations détaillées sur les routes de transit sont fournies uniquement aux responsables du traitement authentifiés, compte tenu des implications de sécurité d'une divulgation publique complète.

## Application de la résidence des données

Lorsqu'un responsable du traitement des DCP spécifie des exigences de résidence des données dans l'accord de service (ex. « stockage UE uniquement », « Suisse uniquement »), [Organisation] DOIT :

- **Appliquer techniquement** la contrainte de résidence via la configuration de l'infrastructure (restrictions régionales, géo-cloisonnement, règles de politique de stockage)
- **Documenter** le mécanisme technique utilisé pour appliquer la contrainte et rendre cette documentation disponible au responsable du traitement sur demande
- **Auditer** la conformité à la résidence au moins annuellement et lors de changements significatifs d'infrastructure, confirmant qu'aucune DCP n'a été stockée ou traitée en dehors des régions convenues

## Notification de changement

Avant de modifier l'emplacement géographique du traitement des DCP — y compris l'ouverture d'une nouvelle région de service, l'ajout d'un sous-traitant ultérieur dans une nouvelle juridiction ou la relocalisation du stockage de sauvegarde — [Organisation] DOIT :

1. Notifier le responsable du traitement des DCP concerné à l'avance, avec un préavis minimum de **30 jours** (sauf si l'accord de service spécifie une période plus longue)
2. Identifier le nouvel emplacement et expliquer la raison opérationnelle du changement
3. Obtenir le consentement préalable des responsables du traitement dont les accords de service exigent un consentement spécifique (et non uniquement une autorisation générale) pour les changements d'emplacement
4. Mettre à jour le Registre des emplacements de traitement des DCP dans les 5 jours ouvrables suivant l'entrée en vigueur du changement

Les changements d'emplacement d'urgence (ex. en raison d'une défaillance du centre de données ou d'un cas de force majeure) DOIVENT être notifiés aux responsables du traitement concernés sans retard injustifié. [Organisation] DOIT en outre fournir aux responsables du traitement concernés un accusé de réception écrit provisoire de l'écart — incluant le nouvel emplacement temporaire, la durée prévue de l'écart et tout écart temporaire de résidence — afin que les responsables du traitement puissent prendre des décisions éclairées concernant leurs propres obligations de notification pendant la période d'écart. La documentation formelle et rétroactive du changement et de sa justification DOIT être complétée dans les 5 jours ouvrables.

---

# Énoncés de politique : Destination prévue des DCP (A.12.2)

## Documentation des transferts

[Organisation] DOIT maintenir des enregistrements documentés de toutes les **destinations prévues** vers lesquelles les DCP peuvent être transférées dans le cadre de la prestation de services cloud, y compris les flux transfrontaliers ou transjuridictionnels vers :

- Les sous-traitants ultérieurs (qu'ils soient dans l'EEE ou en dehors)
- Les sites de sauvegarde et de reprise d'activité dans des pays tiers
- L'infrastructure des fournisseurs cloud dans des juridictions en dehors du pays d'origine du responsable du traitement
- Le personnel de support ou d'exploitation accédant aux DCP à distance depuis l'extérieur de la région de traitement (géré via une architecture de serveur de rebond maintenant les données dans la région, ou via des CCT intégrées dans les accords d'emploi ou de prestataire — le mécanisme spécifique de [Organisation] DOIT être documenté dans les enregistrements de destination des transferts)

Pour chaque destination identifiée, [Organisation] DOIT documenter :

| Élément | Description |
|---------|-------------|
| **Pays/région de destination** | Juridiction du destinataire prévu ou de l'emplacement de traitement |
| **Finalité du transfert** | Raison opérationnelle du transfert (sauvegarde, accès support, réplication, etc.) |
| **Mécanisme de transfert** | Base juridique du transfert (décision d'adéquation, CCT, BCR, dérogation — voir ci-dessous) |
| **Garanties en place** | Protections techniques et contractuelles appliquées (chiffrement en transit, APD/avenant, accord de sous-traitance) |
| **Statut de notification du responsable du traitement** | Si le responsable du traitement a été informé de cette destination |

## Mécanismes de transfert

Pour les transferts de DCP vers des pays en dehors de l'EEE ou de la Suisse ne disposant pas d'une décision d'adéquation, [Organisation] DOIT mettre en œuvre l'un des mécanismes de transfert approuvés suivants :

- **Clauses Contractuelles Types (CCT)** : CCT approuvées par la CE (ensemble 2021) intégrées dans les accords de sous-traitance et de traitement des données
- **Accord de Transfert de Données International du Royaume-Uni (IDTA)** : Pour les transferts vers/depuis le Royaume-Uni — le Responsable Juridique/Conformité doit vérifier les orientations actuelles de l'ICO sur les versions IDTA avant l'exécution
- **Clauses standard de protection des données du PFPDT suisse** : Pour les transferts soumis à la LPD suisse — le Responsable Juridique/Conformité doit confirmer le titre exact de l'instrument et la date de publication sur le site web du PFPDT avant l'exécution
- **Décision d'adéquation** : Lorsque le pays de destination dispose d'une décision d'adéquation UE ou suisse en vigueur au moment du transfert
- **Règles d'entreprise contraignantes (BCR)** : Le cas échéant pour les transferts intragroupe

[Organisation] NE DOIT PAS transférer de DCP vers un pays tiers sans que l'un des mécanismes ci-dessus soit en place et documenté. Lorsque le statut d'adéquation d'un pays de destination change, [Organisation] DOIT :

1. **Cesser les nouveaux transferts** vers le pays concerné dans les **5 jours ouvrables** suivant l'expiration ou l'invalidation de la décision d'adéquation
2. **Mettre en œuvre des mécanismes de transfert alternatifs** (ex. CCT) dans les **60 jours**, sous supervision du DPD et avec notification des responsables du traitement tout au long du processus
3. **Notifier les responsables du traitement des DCP concernés** dès qu'ils prennent connaissance du changement d'adéquation, confirmant la date de cessation et le mécanisme alternatif prévu

La distinction entre l'obligation de cessation et la mise en œuvre du mécanisme alternatif reflète la réalité pratique de la renégociation des instruments avec plusieurs sous-traitants ultérieurs simultanément, tout en protégeant les personnes concernées contre des transferts non sécurisés continus.

## Évaluations d'Impact du Transfert (EIT)

Une Évaluation d'Impact du Transfert (EIT) est requise avant de transférer des DCP vers tout pays pour lequel il y a des raisons de croire que le cadre juridique local ne fournit pas des protections substantiellement équivalentes au RGPD. Les indicateurs déclenchant une EIT comprennent : des pays avec des programmes de surveillance de masse documentés, aucune autorité indépendante de protection des données ou aucune protection par l'état de droit pour les données des ressortissants étrangers. Le DPD DOIT maintenir une liste des juridictions désignées comme nécessitant une EIT. La méthodologie de l'EIT suit les Recommandations 01/2020 du CEPD sur les mesures supplémentaires. Les EIT complétées sont conservées conformément au calendrier des preuves et mises à disposition des responsables du traitement sur demande.

## Changements d'emplacement des sous-traitants ultérieurs

Les sous-traitants ultérieurs sont contractuellement tenus de notifier [Organisation] de tout changement de l'emplacement géographique de leurs opérations de traitement des DCP dans les 10 jours ouvrables suivant le changement (conformément aux exigences des accords de sous-traitants ultérieurs de CLD-PII-POL-A.11 §11.12). [Organisation] DOIT examiner les données d'emplacement des sous-traitants ultérieurs au minimum annuellement dans le cadre de l'audit annuel des sous-traitants ultérieurs en vertu de CLD-PII-POL-A.11 §11.12, et mettre à jour le Registre des emplacements de traitement des DCP en conséquence.

## Information des responsables du traitement

[Organisation] DOIT mettre la documentation des transferts à la disposition des responsables du traitement des DCP sur demande. Lorsqu'un responsable du traitement le demande pour soutenir son propre registre des activités de traitement conformément à l'Article 30 du RGPD ou ses évaluations d'impact des transferts, [Organisation] DOIT fournir :

- La liste complète des destinations de transfert pour les DCP du responsable du traitement
- Le mécanisme de transfert et la référence pertinente à l'instrument juridique (ex. référence de clause CCT, citation de décision d'adéquation) pour chaque destination
- Un résumé des garanties techniques supplémentaires appliquées pour les transferts vers des juridictions à haut risque

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Délégué à la Protection des Données (DPD)** | Est propriétaire du Registre des emplacements de traitement des DCP et de la documentation des transferts ; conseille sur les évaluations d'adéquation et la sélection des mécanismes de transfert ; gère la notification des responsables du traitement pour les changements d'emplacement ; examine les mécanismes de transfert annuellement |
| **RSSI / Responsable Sécurité Cloud** | Met en œuvre et audite les contrôles techniques d'application de la résidence des données ; supervise la surveillance des emplacements des sous-traitants ultérieurs ; gère les notifications de changements d'emplacement d'urgence |
| **Responsable Juridique/Conformité** | Maintient les modèles de CCT, IDTA et clauses standard suisses ; conseille sur le statut d'adéquation des pays tiers ; examine la documentation des transferts pour la conformité réglementaire |
| **Cloud Engineering** | Met en œuvre les contraintes géographiques de données et les mécanismes d'application de la résidence ; configure l'isolation régionale pour les charges de travail clients ; audite la conformité à la résidence |
| **Achats** | S'assure que les emplacements des sous-traitants ultérieurs sont capturés avant la signature du contrat ; déclenche l'examen du DPD pour les nouveaux emplacements ou les emplacements modifiés des sous-traitants ultérieurs |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Registre des emplacements de traitement des DCP | Registre complet de tous les emplacements de stockage, de traitement et de transit des DCP, y compris les sous-traitants ultérieurs | En cours + versions précédentes pendant 5 ans |
| Enregistrements de configuration de résidence des données | Documentation technique des mécanismes d'application de la résidence par responsable du traitement | Durée de l'accord + 5 ans |
| Résultats des audits de résidence | Résultats des audits annuels confirmant l'absence de traitement des DCP hors périmètre | 5 ans |
| Notifications de changement d'emplacement | Enregistrements des préavis envoyés aux responsables du traitement pour les changements d'emplacement | 5 ans |
| Enregistrements de destination des transferts | Documentation complète des destinations de transfert par responsable du traitement | Durée de l'accord + 5 ans |
| Instruments de mécanisme de transfert | Copies des CCT, IDTA, BCR et citations de décisions d'adéquation invoquées | Durée de l'engagement + 5 ans |
| Enregistrements d'Évaluation d'Impact du Transfert | EIT documentées ou évaluations équivalentes pour les transferts vers des juridictions à haut risque | 5 ans |

---

# Considérations d'audit

Les auditeurs vérifiant la conformité avec CLD-PII-POL-A.12 devraient s'attendre à trouver :

- Un Registre des emplacements de traitement des DCP actuel couvrant tous les emplacements de stockage, de traitement et de transit, y compris les sous-traitants ultérieurs — cohérent avec la liste publiée des sous-traitants ultérieurs (CLD-PII-POL-A.8.1)
- Des preuves techniques que les contrôles de résidence des données sont mis en œuvre et appliqués pour tous les responsables du traitement ayant des exigences de résidence
- Des enregistrements de notification préalable aux responsables du traitement pour tout changement d'emplacement survenu au cours de la période d'audit
- Des enregistrements de destination des transferts avec des mécanismes de transfert documentés pour tous les emplacements de traitement hors EEE/hors Suisse — y compris les CCT ou instruments équivalents pour chaque destination dans un pays tiers
- Aucun transfert de DCP non documenté vers des pays tiers sans mécanisme de transfert approuvé

---

<!-- QA_VERIFIED: 2026-04-04 -->
