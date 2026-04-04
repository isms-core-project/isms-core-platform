<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.10-FR:operational:OP-POL:a.8.10 -->
**ISMS-OP-POL-A.8.10 — Suppression des informations**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Suppression des informations |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.10 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Usage interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.10 — Suppression des informations

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la suppression des informations |
|----------|-----------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | L'inventaire des actifs définit le périmètre de suppression et la propriété des données |
| A.5.10 Utilisation acceptable des informations et autres actifs | Le cycle de vie de l'utilisation acceptable inclut la suppression en fin de vie |
| A.5.12–13 Classification et étiquetage des informations | La classification détermine la méthode de suppression et le niveau de vérification |
| A.5.14 Transfert d'informations | Obligations de suppression après achèvement du transfert |
| A.5.33 Protection des enregistrements | Les calendriers de conservation déclenchent la suppression à l'expiration |
| A.5.34 Vie privée et protection des DCP | Droits d'effacement des personnes concernées ; obligations de suppression des DCP |
| A.7.10 Supports de stockage | Assainissement et élimination des supports physiques |
| A.7.14 Élimination ou réutilisation sécurisée des équipements | La mise hors service des équipements nécessite la suppression des données |
| A.8.13 Sauvegarde des informations | Les copies de sauvegarde sont incluses dans le périmètre de suppression |
| A.8.24 Utilisation de la cryptographie | L'effacement cryptographique comme méthode de suppression |

**Politiques internes associées** :

- Politique de classification et de traitement de l'information
- Politique de vie privée et de protection des DCP
- Politique de protection de l'information et de gestion des enregistrements
- Politique de sauvegarde
- Politique de gestion des actifs
- Politique d'utilisation de la cryptographie

---

# Politique de suppression des informations

## Objet

La présente politique a pour objet de s'assurer que les informations stockées dans les systèmes d'information, les appareils ou tout autre support de stockage sont supprimées lorsqu'elles ne sont plus nécessaires, en utilisant des méthodes appropriées à la sensibilité des données et au type de support, afin de prévenir toute exposition inutile et de se conformer aux exigences légales, réglementaires et contractuelles.

Cette politique soutient la nLPD suisse (revDSG) art. 6(4) (proportionnalité et minimisation des données — les données personnelles doivent être détruites ou anonymisées dès qu'elles ne sont plus nécessaires à la finalité du traitement) et art. 8 (mesures techniques et organisationnelles pour la sécurité des données). Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, le RGPD art. 5(1)(e) (limitation de la conservation) et art. 17 (droit à l'effacement) s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Toutes les informations traitées, stockées ou transmises sur ou dans les systèmes, appareils et supports détenus, gérés et contrôlés par l'organisation et inclus dans le périmètre de la déclaration de champ d'application ISO 27001.

Cela comprend :

- Toutes les catégories de données (données personnelles, informations métier confidentielles, données financières, données techniques, communications, journaux)
- Tous les emplacements de stockage (sur site, cloud, tiers, sauvegarde, reprise après sinistre)
- Tous les types de supports (magnétiques, à semi-conducteurs, optiques, papier, supports amovibles, appareils mobiles)
- Toutes les phases du cycle de vie (utilisation active, archivage, sauvegarde, développement/test, fin de vie)

## Principe

Les informations ne sont pas conservées plus longtemps que nécessaire pour leur finalité métier, légale ou réglementaire définie. Lorsque les délais de conservation expirent ou qu'un déclencheur de suppression valide se produit, les informations sont supprimées en utilisant une méthode appropriée à la sensibilité des données et au type de support, avec des preuves vérifiables que la suppression a été effectuée.

Seules les méthodes de suppression approuvées par l'organisation sont utilisées. La suppression standard du système d'exploitation (par exemple « supprimer » ou « vider la corbeille ») est insuffisante pour les données confidentielles ou personnelles, car ces méthodes sont généralement récupérables.

---

## Calendriers de conservation et déclencheurs de suppression

### Calendrier de conservation

L'organisation maintient un calendrier de conservation définissant les délais de conservation pour toutes les catégories de données. Les délais de conservation sont basés sur l'exigence la plus longue applicable parmi :

- Obligations légales et réglementaires (CO suisse, nLPD, droit fiscal)
- Exigences réglementaires (réglementations sectorielles)
- Obligations contractuelles (accords clients, fournisseurs, partenaires)
- Besoin métier documenté (avec approbation du propriétaire)

Lorsque plusieurs exigences s'appliquent aux mêmes données, le délai de conservation le plus long prévaut, sauf si le Conseiller juridique en décide autrement.

**Délais de conservation de référence pour les PME suisses** :

| Catégorie de données | Conservation minimale | Base légale | Remarques |
|----------------------|-----------------------|-------------|-----------|
| **Enregistrements comptables** (rapports annuels, rapports d'audit, états financiers) | 10 ans à compter de la fin de l'exercice | CO suisse art. 958f | Doit être conservé sous forme écrite et signée (rapports annuels/d'audit) ou électroniquement avec garantie d'intégrité |
| **Pièces justificatives comptables** (factures, reçus, relevés bancaires, documents TVA) | 10 ans à compter de la fin de l'exercice | CO suisse art. 958f | Peut être conservé électroniquement selon les exigences Olico |
| **Contrats de travail et dossiers RH** | 10 ans à compter de la fin de l'emploi | CO suisse art. 127–128 (délais de prescription) ; exigences cantonales | Créances salariales : prescription de 5 ans (CO art. 128) ; certificats de travail : prescription de 10 ans (CO art. 127) |
| **Fiches de salaire et documents d'assurance sociale** | 10 ans à compter de la fin de l'exercice | CO suisse art. 958f ; exigences AVS/AI | Inclut les fiches de salaire, les cotisations de sécurité sociale |
| **Données fiscales** | 10 ans à compter de la fin de l'exercice | CO suisse art. 958f ; droit fiscal cantonal | Inclut les données fiscales des entreprises et TVA |
| **Contrats clients** | Durée + 10 ans | CO suisse art. 127 (prescription générale) | Délai de prescription de 10 ans pour les créances contractuelles |
| **Contrats fournisseurs** | Durée + 10 ans | CO suisse art. 127 | Conserver pendant le délai de prescription après la fin du contrat |
| **Données personnelles (général)** | Uniquement le temps nécessaire à la finalité du traitement | nLPD art. 6(4) | Doivent être supprimées ou anonymisées lorsque la finalité est atteinte |
| **Enregistrements de consentement des personnes concernées** | Durée du traitement + 3 ans | nLPD art. 6 ; bonne pratique | Preuve de la base légale du traitement |
| **Journaux de sécurité et pistes d'audit** | 12 mois (en ligne), jusqu'à 3 ans (archive) | Politique organisationnelle ; OPDo art. 4 | Conservation plus longue pour les journaux de traitement de données sensibles |
| **Preuves d'audit SMSI** | 3 ans minimum | Cycle de certification ISO 27001 | Conserver sur l'ensemble du cycle de certification |
| **Enregistrements d'enquête sur les incidents** | 3 ans à compter de la clôture | Politique organisationnelle | Plus longtemps si un litige est anticipé |

Ce tableau fournit des délais de référence minimaux. Le Responsable des enregistrements maintient le calendrier de conservation faisant autorité, qui est révisé annuellement par le Conseiller juridique et approuvé par la Direction générale.

### Déclencheurs de suppression

La suppression est déclenchée lorsque l'un des événements suivants se produit :

| # | Événement déclencheur | Responsable | Délai |
|---|----------------------|-------------|-------|
| 1 | **Expiration du délai de conservation** | Responsable des enregistrements / Propriétaire du système | Dans les 90 jours suivant l'expiration (automatisé si réalisable) |
| 2 | **Demande d'effacement d'une personne concernée** (nLPD / RGPD art. 17) | DPD / Conseiller en confidentialité | Dans les 30 jours suivant la demande validée |
| 3 | **Résiliation du contrat ou de l'accord de service** | Propriétaire du système | Selon les termes contractuels (défaut : 90 jours) |
| 4 | **Achèvement de la finalité du traitement** | Propriétaire des données | Dans les 90 jours suivant l'accomplissement de la finalité |
| 5 | **Levée du blocage légal** | Conseiller juridique | Dans les 90 jours suivant la levée du blocage |
| 6 | **Décommissionnement d'actif** | Opérations informatiques | Avant que l'actif quitte le contrôle organisationnel |
| 7 | **Retrait du consentement** | DPD / Conseiller en confidentialité | Dans les 30 jours (sauf si une autre base légale s'applique) |

Lorsque la suppression automatisée est techniquement réalisable, elle devrait être mise en œuvre avec des dispositifs de sécurité contre la suppression prématurée (vérifications de blocage légal, notification du propriétaire métier). Lorsque l'automatisation n'est pas réalisable, des procédures de suppression manuelle sont documentées avec des points de vérification définis.

---

## Méthodes de suppression

### Normes d'assainissement

Les méthodes de suppression sont alignées sur NIST SP 800-88 Rév. 2 (Lignes directrices pour l'assainissement des supports, septembre 2025), qui définit trois niveaux d'assainissement, et IEEE 2883 pour les techniques d'assainissement spécifiques aux supports.

| Niveau d'assainissement | Description | Quand l'utiliser | Exemples de méthodes |
|--------------------------|-------------|------------------|----------------------|
| **Effacement** | Techniques logiques rendant les données inaccessibles via les interfaces standard ; la récupération est possible avec des outils spécialisés | Supports restant sous contrôle organisationnel ; données de sensibilité inférieure (Publique, Usage interne) | Écrasement standard, réinitialisation du fabricant, effacement sécurisé du système d'exploitation |
| **Purge** | Techniques physiques ou logiques rendant les données inaccessibles même avec des outils de laboratoire | Supports quittant le contrôle organisationnel ; données sensibles (Confidentielle) ; réutilisation de supports par des tiers | Effacement cryptographique, effacement de blocs (flash/SSD), démagnétisation (supports magnétiques) |
| **Destruction** | Destruction physique rendant le support inutilisable et la récupération des données irréalisable | Supports en fin de vie ; données de plus haute sensibilité ; supports sans valeur future | Désintégration, pulvérisation, incinération, fusion, déchiquetage |

### Méthode de suppression par classification et type de support

| Classification des données | Support restant en interne | Support quittant l'organisation | Support en fin de vie |
|---------------------------|----------------------------|---------------------------------|-----------------------|
| **Publique** | Effacement | Effacement | Destruction (ou recyclage si effacement vérifié) |
| **Usage interne** | Effacement | Purge | Destruction |
| **Confidentielle** | Purge | Purge | Destruction |
| **Strictement confidentielle** | Purge | Destruction | Destruction |

### Documents papier

| Classification des données | Méthode d'élimination |
|---------------------------|------------------------|
| **Publique** | Déchets ordinaires ou recyclage |
| **Usage interne** | Déchiquetage croisé (DIN 66399 P-3 minimum) |
| **Confidentielle** | Déchiquetage croisé (DIN 66399 P-4 minimum) ou incinération avec témoins |
| **Strictement confidentielle** | DIN 66399 P-5 minimum ou destruction certifiée par un tiers avec certificat |

### Effacement cryptographique

L'effacement cryptographique peut être utilisé comme méthode valide de niveau Purge lorsque les données ont été chiffrées au repos et que le chiffrement satisfait aux normes organisationnelles (conformément à la Politique d'utilisation de la cryptographie). Pour que l'effacement cryptographique constitue une suppression au sens de la présente politique :

- Toutes les données cibles doivent avoir été chiffrées avant le stockage (le chiffrement appliqué rétroactivement n'est pas éligible).
- L'algorithme de chiffrement doit satisfaire aux normes minimales approuvées (AES-256 ou équivalent).
- Un mappage données-clés documenté doit exister, permettant d'identifier quelles clés de chiffrement protègent quelles données.
- La destruction des clés doit être effectuée via un processus vérifié (mise à zéro des clés HSM, suppression de clés KMS avec journal d'audit, ou équivalent).
- Les preuves de destruction des clés doivent être conservées (journaux d'audit, certificats HSM) pendant au minimum 3 ans.
- Les copies de sauvegarde de la clé de chiffrement doivent également être détruites — si une sauvegarde de clé, un séquestre ou un stockage externe existe et ne peut être vérifié comme détruit, l'effacement cryptographique ne sera pas accepté comme seule méthode de suppression.

### Suppression des sauvegardes

La suppression dans les systèmes de production s'étend à toutes les copies de sauvegarde contenant les données supprimées, notamment :

- Sauvegardes complètes, incrémentielles et différentielles
- Instantanés et copies à un instant donné
- Répliques de reprise après sinistre
- Sauvegardes au niveau applicatif (exports de base de données, exports de VM)
- Services de sauvegarde natifs cloud avec politiques de conservation indépendantes

Lorsque la suppression immédiate des sauvegardes n'est pas techniquement réalisable (par exemple bandes de sauvegarde immuables, sauvegardes cloud verrouillées à la conservation), l'organisation :

1. Documente le calendrier de conservation des sauvegardes indiquant quand les données seront naturellement écrasées ou expirées.
2. Obtient l'approbation du RSSI et du Propriétaire des données pour la période de conservation prolongée.
3. Applique des contrôles d'accès pour empêcher la restauration des données à partir de la sauvegarde.
4. Suit la suppression en attente dans le registre de suppression jusqu'à confirmation de l'achèvement.

---

## Suppression par des tiers et dans le cloud

### Exigences contractuelles

Tous les contrats avec des tiers qui traitent des données organisationnelles comprennent des obligations de suppression précisant :

- Délai maximal de suppression après résiliation du contrat ou sur demande écrite (défaut : 30 jours)
- Norme d'assainissement appropriée à la sensibilité des données (en référence aux niveaux NIST SP 800-88)
- Périmètre de suppression couvrant toutes les copies, y compris les sauvegardes, caches, journaux et répliques de reprise après sinistre
- Obligation de fournir une vérification de la suppression (certificat de destruction ou attestation équivalente)
- Transmission des exigences de suppression aux sous-traitants ultérieurs
- Droit d'audit de la conformité à la suppression

### Évaluation des fournisseurs de services cloud

Avant de faire appel à un fournisseur de services cloud, l'organisation évalue les capacités de suppression, notamment :

- Prise en charge d'API pour la suppression des données et la vérification de la suppression
- Propagation de la suppression à toutes les régions, zones de disponibilité et répliques
- Garanties d'isolation multi-locataires (la suppression n'affecte pas les autres locataires ; les autres locataires ne peuvent accéder aux données résiduelles)
- Capacités et délais de suppression des sauvegardes et instantanés
- Contrôles de rémanence des données après suppression
- Certification ou attestation des pratiques de suppression (SOC 2 Type II, ISO 27001 avec A.8.10 dans le périmètre)

### Vérification de la suppression par des tiers

L'organisation obtient la vérification de la suppression auprès des tiers par une ou plusieurs des méthodes suivantes :

**Destruction de supports physiques** — Certificats de destruction comprenant :
- Numéros de série des supports ou identifiants d'actifs
- Méthode de destruction (en référence au niveau NIST SP 800-88 ou au niveau de sécurité DIN 66399)
- Date et lieu de destruction
- Nom et accréditation de l'émetteur du certificat (par exemple NAID AAA, ISO 21964)

**Suppression logique par le prestataire de services** — L'un des éléments suivants :
- Rapport SOC 2 Type II avec test des contrôles de suppression
- Rapport d'audit indépendant vérifiant les procédures de suppression
- Certification ISO 27001 avec A.8.10 dans le périmètre

**Suppression via API cloud/SaaS** — Preuves journalisées comprenant :
- Horodatage de l'appel API et utilisateur authentifié
- Identifiant(s) de ressource(s) supprimé(es)
- Réponse de succès HTTP (200/204)
- Confirmation de la suppression des sauvegardes/instantanés lorsque le fournisseur le prend en charge

Pour les données Confidentielles et Strictement Confidentielles : les certificats de fournisseurs de destruction accrédités ou les rapports d'audit indépendants sont requis. Les journaux API seuls sont insuffisants.

### Escalade en cas d'échec de suppression par des tiers

| Délai | Action | Responsable |
|-------|--------|-------------|
| J+0 | Enregistrer l'échec dans le registre des écarts ; initier un suivi avec le contact tiers | Opérations informatiques |
| J+15 | Escalader au responsable de compte tiers ; copier le RSSI et le DPD | Propriétaire du système |
| J+30 | Escalader au contact de direction tiers ; lancer la revue du contrat avec le Conseiller juridique | RSSI |
| J+45 | Examiner les recours contractuels (crédits de service, résiliation pour manquement grave) ; envisager la migration des données vers un fournisseur conforme | Direction générale |

Pour les données Confidentielles/Strictement Confidentielles, les délais d'escalade sont accélérés : J+7, J+15, J+21.

---

## Demandes d'effacement des personnes concernées

### Acceptation et traitement des demandes

L'organisation accepte et traite les demandes d'effacement des personnes concernées conformément à la nLPD suisse art. 6(4) et, le cas échéant, au RGPD art. 17 (droit à l'effacement / droit à l'oubli).

**Processus de traitement des demandes** :

| Étape | Action | Délai | Responsable |
|-------|--------|-------|-------------|
| 1 | Recevoir la demande (courriel, formulaire web, courrier, en personne) | — | DPD / Conseiller en confidentialité |
| 2 | Enregistrer la demande dans le registre des demandes des personnes concernées | Dans les 24 heures | DPD / Conseiller en confidentialité |
| 3 | Vérifier l'identité de la personne concernée | Dans les 5 jours ouvrés | DPD / Conseiller en confidentialité |
| 4 | Identifier tous les systèmes, bases de données et sauvegardes contenant les données personnelles de la personne concernée | Dans les 10 jours ouvrés | Opérations informatiques / Propriétaires de systèmes |
| 5 | Évaluer si l'obligation d'effacement s'applique ou si une exception légale existe | Dans les 15 jours ouvrés | DPD + Conseiller juridique |
| 6 | Exécuter la suppression ou émettre un refus motivé | Dans les 25 jours ouvrés | Opérations informatiques / DPD |
| 7 | Confirmer l'achèvement à la personne concernée par écrit | Dans les 30 jours suivant la demande | DPD / Conseiller en confidentialité |

### Exceptions légales à l'effacement

L'effacement peut être refusé lorsque le traitement est nécessaire pour :

- Respecter une obligation légale de conservation (par exemple CO suisse art. 958f pour les enregistrements comptables, obligations fiscales)
- Établir, exercer ou défendre des droits en justice
- Des finalités d'archivage dans l'intérêt public, de recherche scientifique ou historique
- Des raisons d'intérêt public dans le domaine de la santé publique
- L'exercice du droit à la liberté d'expression et d'information

Lorsque l'effacement est refusé sur la base d'une exception légale :

1. Documenter la base légale spécifique invoquée.
2. Fournir une explication écrite à la personne concernée incluant l'exception invoquée et les droits de réclamation (droit de déposer une plainte auprès du PFPDT ou de l'autorité de contrôle compétente).
3. Appliquer une restriction du traitement dans la mesure du possible (données conservées mais non activement traitées).
4. Définir une date de révision pour réexaminer si l'exception s'applique toujours.

### Notification aux tiers

Lorsque des données personnelles faisant l'objet d'une demande d'effacement ont été divulguées à des tiers, l'organisation notifie ces tiers de la demande d'effacement conformément au RGPD art. 19 et aux obligations nLPD, à moins que cela s'avère impossible ou implique un effort disproportionné.

---

## Gestion des blocages légaux

### Déclencheurs de blocage légal

La suppression est suspendue lorsque les données font l'objet d'un blocage légal pour l'une des raisons suivantes :

- Litige (intenté, menacé ou raisonnablement anticipé)
- Enquête gouvernementale ou examen réglementaire
- Enquête interne nécessitant une conservation à des fins légales (fraude, inconduite, violation de données)
- Audit externe nécessitant la conservation de données spécifiques

### Initiation et levée

Seul le Conseiller juridique (ou le Responsable juridique/conformité désigné) peut initier ou lever un blocage légal.

**Processus d'émission** :

1. Le Conseiller juridique émet une notification formelle de blocage documentant : nom/numéro de la procédure, périmètre (systèmes, plages de dates, dépositaires, catégories de données), date d'effet, obligations de conservation.
2. Les dépositaires concernés sont notifiés dans les 24 heures et accusent réception dans les 2 jours ouvrés.
3. Les opérations informatiques suspendent la suppression automatisée pour les systèmes concernés dans les 48 heures et confirment la suspension par écrit.
4. Le Conseiller juridique maintient un Registre des blocages légaux enregistrant : identifiant du blocage, nom de la procédure, date d'émission, périmètre, systèmes concernés, dépositaires, statut d'accusé de réception, dates de révision.

### Révision trimestrielle

Les blocages légaux sont révisés au moins trimestriellement par le Conseiller juridique. Chaque révision produit une évaluation documentée comprenant :

- Identifiant du blocage et date d'initiation
- Statut actuel du litige/de l'enquête
- Détermination de la nécessité continue avec base légale
- Ajustement du périmètre si applicable (restriction à des catégories de données spécifiques)
- Date de levée anticipée du blocage ou condition de déclenchement
- Nom du réviseur et date de révision

### Levée du blocage et suppression post-blocage

À la levée du blocage :

1. Le Conseiller juridique émet une notification formelle de levée du blocage.
2. Les dépositaires et les opérations informatiques sont notifiés dans les 24 heures.
3. Les opérations informatiques réactivent les calendriers de suppression normaux.
4. Les données conservées au-delà de la conservation normale uniquement en raison du blocage légal doivent être supprimées dans les 90 jours suivant la levée du blocage, sauf si une justification métier approuvée existe.

### Conflit avec les demandes d'effacement

Lorsqu'une demande d'effacement d'une personne concernée entre en conflit avec un blocage légal actif :

- Le blocage légal a la priorité.
- Une restriction du traitement est appliquée (données conservées mais non activement utilisées).
- La suppression s'exécute dans les 30 jours suivant la levée du blocage.
- La personne concernée est informée que la demande a été enregistrée mais ne peut actuellement être satisfaite, en citant l'exception légale applicable, sans divulguer des détails susceptibles de nuire aux procédures judiciaires.

---

## Vérification et preuves

### Piste d'audit de suppression

L'organisation maintient des pistes d'audit de suppression comprenant :

| Champ | Description |
|-------|-------------|
| **Horodatage de suppression** | Date et heure d'exécution de la suppression |
| **Catégorie de données** | Type et classification des données supprimées |
| **Méthode de suppression** | Méthode d'assainissement appliquée (Effacement / Purge / Destruction / Effacement cryptographique) |
| **Identifiant du support** | Nom du système, numéro de série de l'appareil ou emplacement de stockage |
| **Déclencheur de suppression** | Événement ayant initié la suppression (expiration de conservation, demande DSR, décommissionnement, etc.) |
| **Partie responsable** | Personne ou système ayant effectué la suppression |
| **Résultat de vérification** | Confirmation que la suppression a été effectuée avec succès |

### Conservation des journaux de suppression

Les journaux de suppression sont conservés pendant au minimum 3 ans ou la durée réglementaire applicable, selon la plus longue. Les journaux de suppression ne contiennent pas les données supprimées elles-mêmes — uniquement les métadonnées de l'événement de suppression.

### Méthodes de vérification

L'efficacité de la suppression est vérifiée par :

- **Vérification automatisée** : Confirmation générée par le système de la suppression réussie (réponse API, sortie de l'outil, entrée de journal)
- **Échantillonnage périodique** : Échantillonnage trimestriel des enregistrements de suppression pour vérifier l'exhaustivité et l'exactitude (échantillon minimum de 10 % des suppressions par trimestre)
- **Attestation tierce** : Certificats de destruction pour les supports physiques et les prestataires de services externes
- **Contrôles ponctuels** : Contrôle ponctuel annuel de systèmes sélectionnés aléatoirement pour confirmer qu'aucune donnée n'existe au-delà de son délai de conservation

---

## Gestion des exceptions

### Demandes d'exception

Les exceptions aux procédures de suppression standard requièrent une demande documentée comprenant :

- Catégorie et classification des données
- Justification métier de l'exception
- Évaluation des risques (quel est le risque de conserver les données au-delà de leur délai normal ?)
- Contrôles compensatoires pour atténuer le risque de conservation
- Date d'expiration proposée (les exceptions ne doivent pas être indéfinies)

### Autorité d'approbation

| Classification des données | Durée de l'exception | Approbateurs |
|---------------------------|----------------------|--------------|
| Usage interne | Jusqu'à 12 mois | Propriétaire du système + RSSI |
| Confidentielle | Jusqu'à 6 mois | RSSI + DPD |
| Strictement confidentielle | Toute durée | RSSI + DPD + Conseiller juridique + Direction générale |

### Exceptions interdites

Les exceptions suivantes ne sont pas accordées :

- Conservation indéfinie sans date de fin spécifique ni déclencheur de révision
- Exceptions pour contourner les demandes d'effacement légitimes des personnes concernées
- Exceptions pour contourner les limitations de conservation réglementaires
- Exceptions générales pour des catégories de données entières sans justification spécifique documentée

### Registre des exceptions

Toutes les exceptions approuvées sont enregistrées dans le registre des exceptions avec le propriétaire, la date d'approbation, la date d'expiration, les contrôles compensatoires et le calendrier de révision. Les exceptions sont révisées trimestriellement et expirent automatiquement à moins d'être renouvelées via le processus d'approbation.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Suppression des informations** | Processus de suppression des données des supports de stockage de sorte qu'elles ne puissent être récupérées par des moyens normaux ou, selon le niveau d'assainissement, spécialisés |
| **Assainissement des données** | Toutes les méthodes de rendre les données inaccessibles, incluant l'effacement, la purge et la destruction |
| **Effacement** | Assainissement logique protégeant contre la récupération des données à l'aide des outils standard du système d'exploitation ou de techniques simples non invasives |
| **Purge** | Assainissement physique ou logique protégeant contre la récupération des données à l'aide de techniques d'attaque de niveau laboratoire |
| **Destruction** | Destruction physique rendant le support inutilisable et la récupération des données irréalisable par toute technique connue |
| **Effacement cryptographique** | Méthode de suppression rendant les données chiffrées irrécupérables en détruisant de manière sécurisée les clés de chiffrement |
| **Délai de conservation** | Période définie pendant laquelle les données doivent être conservées avant que la suppression soit autorisée ou requise |
| **Déclencheur de suppression** | Événement ou condition qui initie le processus de suppression (par exemple expiration de conservation, demande d'effacement) |
| **Blocage légal** | Suspension de la suppression pour conserver les données dans le cadre d'un litige, d'une enquête, d'un examen réglementaire ou d'un audit |
| **Demande d'effacement d'une personne concernée** | Demande d'une personne concernée exerçant son droit à l'effacement en vertu de la nLPD ou du RGPD art. 17 |
| **Certificat de destruction** | Attestation d'un tiers que les supports physiques ont été détruits selon une norme spécifiée |
| **Rémanence des données** | Données résiduelles subsistant sur les supports de stockage après des tentatives de suppression ; le risque que les méthodes d'assainissement cherchent à éliminer |
| **Propriétaire des données** | Individu ou rôle responsable de la définition de la finalité métier, du délai de conservation et des exigences de suppression d'une catégorie de données |
| **Responsable des enregistrements** | Rôle responsable du maintien du calendrier de conservation organisationnel et de la supervision des processus d'élimination |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; approbation des méthodes de suppression ; approbation des exceptions ; supervision de la conformité et des métriques ; point d'escalade pour les échecs de suppression |
| **DPD / Conseiller en confidentialité** | Traitement des demandes d'effacement des personnes concernées ; conformité en matière de confidentialité ; révision du calendrier de conservation pour les données personnelles ; approbation des exceptions (Confidentiel+) |
| **Conseiller juridique** | Gestion des blocages légaux (initiation, révision, levée) ; termes des contrats tiers (clauses de suppression) ; interprétation réglementaire ; évaluation des exceptions d'effacement |
| **Responsable des enregistrements** | Maintenance et révision annuelle du calendrier de conservation ; supervision de l'élimination ; gestion du registre de suppression ; suivi de la conformité et rapports |
| **Opérations informatiques** | Exécution des suppressions ; gestion et maintenance des outils de suppression ; suppression des sauvegardes ; journalisation et vérification ; coordination de la suppression avec les tiers |
| **Propriétaires de systèmes** | Mise en œuvre de la suppression spécifique au système ; coordination avec les opérations informatiques ; demandes d'exception ; évaluation de la faisabilité de la suppression automatisée |
| **Propriétaires des données** | Définition des délais de conservation pour les catégories de données détenues ; approbation de la suppression des données critiques pour l'activité ; décisions de classification |
| **Ensemble du personnel** | Traiter les données conformément aux exigences de classification et de conservation ; ne pas conserver les données au-delà des délais autorisés ; signaler les échecs de suppression suspectés |

---

## Preuves

Les éléments de preuve suivants démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Calendrier de conservation** (version actuelle, approuvée par le Conseiller juridique et la Direction générale) | Responsable des enregistrements | *Révisé annuellement ; soumis au contrôle de version* | Actuel + versions précédentes (7 ans) |
| 2 | **Journaux d'exécution des suppressions** (horodatages, catégories de données, méthodes, résultats de vérification) | Opérations informatiques | *Continu ; révisé trimestriellement* | 3 ans |
| 3 | **Certificats de destruction tiers** (supports physiques, certificats de fournisseurs accrédités) | Opérations informatiques | *Par événement de destruction* | 3 ans à compter de la date de destruction |
| 4 | **Registre des demandes d'effacement des personnes concernées** (demandes reçues, évaluation, résultat, date d'achèvement) | DPD / Conseiller en confidentialité | *Par demande ; registre révisé trimestriellement* | 3 ans à compter de la clôture de la demande |
| 5 | **Registre des blocages légaux** (blocages actifs, périmètre, révisions trimestrielles, enregistrements de levée) | Conseiller juridique | *Blocages actifs révisés trimestriellement ; registre maintenu en continu* | 3 ans à compter de la levée du blocage |
| 6 | **Registre des exceptions** (exceptions approuvées avec justification, contrôles compensatoires, dates d'expiration) | RSSI | *Révisé trimestriellement ; présenté lors de la revue de direction* | Durée de l'exception + 3 ans |
| 7 | **Inventaire des données** avec délais de conservation et périmètre de suppression par catégorie de données | Responsable des enregistrements | *Révisé annuellement ; instantanés trimestriels* | Actuel + instantanés trimestriels (3 ans) |
| 8 | **Rapport de conformité trimestriel** (métriques de suppression : taux de suppression dans les délais, éléments en retard, exceptions, délais de réponse aux demandes DSR) | RSSI / Responsable des enregistrements | *Trimestriel ; présenté lors de la revue de direction* | 3 ans |
| 9 | **Journaux de suppression via API cloud/SaaS** (enregistrements d'appels API, identifiants de ressources, confirmations de succès) | Opérations informatiques | *Par événement de suppression* | 3 ans |
| 10 | **Enregistrements de revue des contrats tiers** (clauses de suppression, évaluations des capacités de suppression des fournisseurs) | Conseiller juridique / RSSI | *Par contrat ; révisé lors du renouvellement du contrat* | Durée du contrat + 3 ans |
| 11 | **Enregistrements de configuration de suppression automatisée** (politiques de conservation configurées dans les systèmes, statut d'intégration du blocage légal) | Opérations informatiques | *Révisé semestriellement* | Configuration actuelle + 3 ans |
| 12 | **Résultats de l'échantillonnage de vérification des suppressions** (enregistrements d'échantillonnage trimestriel, résultats des contrôles ponctuels) | Sécurité de l'information | *Échantillonnage trimestriel ; contrôle ponctuel annuel* | 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifie la conformité à la présente politique par diverses méthodes, notamment les audits des journaux de suppression, les revues de conformité au calendrier de conservation, le suivi des réponses aux demandes des personnes concernées, les revues de vérification des suppressions par des tiers, les revues du registre des exceptions, les audits internes et externes, et les retours au propriétaire de la politique.

**Métriques clés de conformité** :

| # | Métrique | Cible | Fréquence de mesure |
|---|----------|-------|---------------------|
| 1 | Taux de suppression dans les délais (suppressions exécutées dans les 90 jours suivant l'expiration de conservation) | ≥ 95 % | Trimestriel |
| 2 | Demandes d'effacement des personnes concernées complétées dans les 30 jours | 100 % | Par demande ; rapport trimestriel |
| 3 | Certificats de destruction tiers obtenus pour les données Confidentielles+ | 100 % | Par événement ; rapport trimestriel |
| 4 | Blocages légaux révisés dans le cycle trimestriel | 100 % | Trimestriel |
| 5 | Registre des exceptions révisé et à jour (aucune exception expirée non révisée) | 100 % | Trimestriel |
| 6 | Couverture du calendrier de conservation (pourcentage des catégories de données avec conservation définie) | 100 % | Annuel |
| 7 | Achèvement de la suppression des sauvegardes (données supprimées de toutes les copies de sauvegarde dans le délai documenté) | ≥ 90 % | Trimestriel |

Les métriques ne respectant pas les cibles sont escaladées au RSSI pour attention immédiate et communiquées lors de la prochaine revue de direction.

## Exceptions

Toute exception à la présente politique est approuvée et enregistrée par le Responsable de la sécurité de l'information au préalable, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie. Les exceptions sont communiquées à l'équipe de revue de direction. Les exceptions liées à la conservation requièrent l'approbation du Conseiller juridique.

## Non-conformité

Tout employé reconnu coupable d'avoir enfreint la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. L'omission de supprimer les données personnelles conformément aux exigences légales peut en outre exposer l'organisation à des sanctions réglementaires (nLPD art. 60–66 ; RGPD art. 83 le cas échéant).

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions prennent en compte les évolutions des réglementations en matière de protection des données (nLPD, RGPD, exigences cantonales), des normes d'assainissement des supports (NIST SP 800-88, IEEE 2883), des capacités de suppression des fournisseurs de services cloud, des technologies de stockage émergentes, des conclusions des audits et des enseignements tirés des échecs de suppression ou des plaintes des personnes concernées.

---

# Domaines de la norme ISO 27001 couverts

Politique de suppression des informations — Correspondance des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.9 Inventaire des informations et autres actifs associés |
| Clause 7.3 Sensibilisation | 5.12 Classification de l'information |
| Clause 7.5.3 Maîtrise de l'information documentée | 5.33 Protection des enregistrements |
| | 5.34 Vie privée et protection des DCP |
| | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 7.10 Supports de stockage |
| | 7.14 Élimination ou réutilisation sécurisée des équipements |
| | **8.10 Suppression des informations** |
| | 8.13 Sauvegarde des informations |
| | 8.24 Utilisation de la cryptographie |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 6 — Principes (proportionnalité, limitation de la finalité, limitation de la conservation) ; Art. 8 — Sécurité des données (mesures techniques et organisationnelles) ; Art. 25 — Droit d'accès (inclut les droits de suppression) ; Art. 24 — Notification de violation |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales de sécurité des données |
| CO suisse (Code des obligations) | Art. 957–958f — Obligations de tenue de la comptabilité et de conservation des enregistrements (10 ans) ; Art. 127–128 — Délais de prescription pour les créances |
| RGPD (le cas échéant) | Art. 5(1)(e) — Limitation de la conservation ; Art. 17 — Droit à l'effacement ; Art. 19 — Obligation de notification relative à l'effacement ; Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.10 — Suppression des informations |
| ISO/IEC 27002:2022 | Section 8.10 — Recommandations de mise en œuvre pour la suppression des informations |
| NIST SP 800-88 Rév. 2 | Lignes directrices pour l'assainissement des supports (Effacement, Purge, Destruction ; effacement cryptographique) |
| IEEE 2883 | Norme pour l'assainissement du stockage (techniques d'assainissement spécifiques aux supports) |
| NIST SP 800-53 Rév. 5 | MP-6 (Assainissement des supports), SI-12 (Gestion et conservation de l'information) |
| DIN 66399 | Classification des niveaux de sécurité de destruction du papier et des supports |

**Cadres conditionnels** (applicables lorsque les activités métier déclenchent l'applicabilité) :

| Cadre | Condition |
|-------|-----------|
| PCI DSS v4.0 | Applicable si des données de cartes de paiement sont traitées ; exige la suppression sécurisée des données du titulaire de la carte lorsqu'elles ne sont plus nécessaires |
| Circulaires FINMA | Applicable si l'organisation est un établissement financier suisse supervisé |
| Règle de sécurité HIPAA | Applicable si des informations de santé protégées américaines sont traitées |

---

<!-- QA_VERIFIED: 2026-03-29 -->
