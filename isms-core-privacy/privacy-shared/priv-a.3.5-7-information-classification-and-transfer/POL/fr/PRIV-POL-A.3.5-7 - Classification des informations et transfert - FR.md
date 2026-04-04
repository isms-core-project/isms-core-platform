<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.5-7-FR:privacy:POL:a.3.5-7 -->
**PRIV-POL-A.3.5-7 — Classification des informations et transfert**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Classification des informations et transfert |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.3.5-7 |
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
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.5-7-UG / TG
- ISMS-POL-A.5.12-13 (Classification et étiquetage — parallèle SGSI)
- ISMS-POL-A.5.14 (Transfert d'informations — parallèle SGSI)
- ISO/IEC 27701:2025 Contrôles A.3.5, A.3.6, A.3.7
- RGPD Article 32 (sécurité) ; Articles 44–49 (transferts internationaux)
- LPD suisse Article 7 (sécurité des données) ; Articles 16–17 (communication transfrontalière)

**Applicabilité du rôle** : Cette politique s'applique à l'organisation agissant à la fois comme **Responsable du traitement et comme Sous-traitant des DCP**. Les contrôles A.3.5, A.3.6 et A.3.7 sont des contrôles partagés (Tableau A.3).

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la classification, l'étiquetage et le transfert des informations en lien avec le traitement des DCP — conformément aux contrôles A.3.5, A.3.6 et A.3.7 d'ISO/IEC 27701:2025.

**Périmètre** : Toutes les informations contenant ou liées aux DCP ; toutes les procédures de classification et d'étiquetage appliquées aux DCP ; tout transfert de DCP au sein de [Organisation] et entre [Organisation] et d'autres parties.

**Justification des contrôles combinés** : A.3.5 (classification), A.3.6 (étiquetage) et A.3.7 (transfert) forment une triade cohésive de protection des flux de données DCP. La classification informe l'étiquetage appliqué ; l'étiquetage détermine la méthode de transfert requise. Ils sont mis en œuvre ensemble comme couche de protection intégrée des DCP.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**Contrôle A.3.5 — Classification des informations**
Le contrôle A.3.5 exige que [Organisation] classe les informations selon leurs besoins de sécurité, en tenant compte du contenu en DCP en plus de la confidentialité, l'intégrité, la disponibilité et les exigences des parties intéressées.

**Contrôle A.3.6 — Étiquetage des informations**
Le contrôle A.3.6 exige que [Organisation] développe et mette en œuvre des procédures d'étiquetage reconnaissant les DCP, cohérentes avec le schéma de classification.

**Contrôle A.3.7 — Transfert d'informations**
Le contrôle A.3.7 exige que [Organisation] dispose de règles, procédures et accords régissant le transfert des DCP par tous types de moyens, au sein de l'organisation et vers l'extérieur.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 32 (sécurité appropriée du traitement, y compris lors du transfert) ; Articles 44–49 (garanties pour les transferts internationaux) ; Article 5(1)(f) (principe d'intégrité et de confidentialité)
- **LPD suisse** : Article 7 (mesures techniques et organisationnelles proportionnées à la sensibilité) ; Articles 16–17 (communication transfrontalière — équivalence, clauses standard)
- **ISO/IEC 27701:2025** : Contrôles A.3.5, A.3.6, A.3.7 (normatifs)

---

# Classification des informations portant sur les DCP (A.3.5)

## Extension du schéma de classification pour les DCP

Le schéma de classification des informations de [Organisation] (défini dans ISMS-POL-A.5.12-13) DOIT être appliqué à toutes les informations. Pour les informations contenant ou liées aux DCP, cette politique établit des critères spécifiques aux DCP qui étendent et complètent le schéma de classification SGSI.

### Niveaux de classification minimaux pour les DCP

Les niveaux de classification minimaux suivants DOIVENT s'appliquer aux informations contenant des DCP, indépendamment des autres critères de classification :

| Catégorie de DCP | Classification minimale |
|-----------------|------------------------|
| **Données à caractère personnel ordinaires** (nom, adresse, coordonnées, dossier d'emploi) | CONFIDENTIEL |
| **Données à caractère personnel financières** (comptes bancaires, registres de paiement, salaire, crédit) | CONFIDENTIEL |
| **DCP de catégorie spéciale** (santé/médical, biométrique, génétique, origine raciale/ethnique, conviction religieuse, opinion politique, vie/orientation sexuelle, appartenance syndicale) | RESTREINT |
| **Données à caractère personnel sensibles** (données d'enfants, casiers judiciaires, numéros d'identification nationaux) | RESTREINT |
| **Identifiants d'authentification** (mots de passe, jetons, clés cryptographiques associés à des identités individuelles) | RESTREINT — inclus pour commodité opérationnelle car ils coexistent fréquemment avec des DCP dans les registres d'identité ; classifiés RESTREINT pour des raisons de sécurité per ISMS-POL-A.5.12-13 |
| **DCP de personnes à haut risque** (personnes vulnérables, lanceurs d'alerte, personnes concernées sous mesures de protection) | RESTREINT |

### Règle d'agrégation des DCP

Lorsque des informations individuellement classifiées en dessous de CONFIDENTIEL sont combinées de telle sorte que des DCP peuvent être dérivés, identifiés ou inférés, le jeu de données agrégé DOIT être classifié au minimum CONFIDENTIEL. Lorsque le jeu de données agrégé contient ou permet la dérivation de DCP de catégorie spéciale, il DOIT être classifié RESTREINT.

Le Propriétaire des données (ou le DPD lorsqu'aucun Propriétaire des données n'est attribué) DOIT effectuer la détermination de classification par agrégation et la documenter dans le Registre de classification. Le DPD est propriétaire du Registre de classification.

### Autorité de classification pour les DCP

| Niveau de classification | Qui peut classifier les DCP | Qui peut déclassifier |
|-------------------------|---------------------------|----------------------|
| CONFIDENTIEL (DCP ordinaires) | Propriétaire des données, DPD | Propriétaire des données avec notification DPD |
| RESTREINT (DCP catégorie spéciale) | Propriétaire des données avec approbation DPD | Propriétaire des données avec approbation DPD et Direction générale |
| RESTREINT (DCP à haut risque) | DPD avec approbation Direction générale | DPD avec approbation Direction générale |

### Révision de la classification des DCP

En plus des déclencheurs de révision définis dans ISMS-POL-A.5.12-13, la classification des DCP DOIT être revue : lorsque la finalité du traitement change, impliquant différentes catégories de DCP ; lorsque la base légale du traitement change, affectant le niveau de sensibilité ; suite à une AIPD identifiant une exigence de reclassification ; lors de notification d'une APD ou autorité de contrôle ; lorsque de nouvelles orientations ou jurisprudences modifient matériellement l'interprétation d'une catégorie de DCP.

---

# Étiquetage des informations portant sur les DCP (A.3.6)

## Exigences d'étiquetage des DCP

[Organisation] DOIT développer et mettre en œuvre des procédures d'étiquetage identifiant les informations contenant des DCP comme telles. Les procédures d'étiquetage des DCP DOIVENT être cohérentes avec et étendre le schéma d'étiquetage SGSI (ISMS-POL-A.5.12-13).

### Étiquetage obligatoire des DCP

Toutes les informations classifiées CONFIDENTIEL ou RESTREINT en raison de leur contenu en DCP DOIVENT porter :

1. L'étiquette de classification applicable (CONFIDENTIEL ou RESTREINT) per les normes d'étiquetage SGSI
2. Un indicateur DCP désignant que l'information contient des données à caractère personnel

**Formats de l'indicateur DCP** (définis en détail dans PRIV-IMP-A.3.5-7-TG) :

| Format | Indicateur DCP |
|--------|---------------|
| Documents électroniques | Notation « Contient des données à caractère personnel » dans l'en-tête/pied de page ou les propriétés du document |
| Documents physiques | Tampon « DONNÉES PERSONNELLES » ou indicateur imprimé sur la couverture et la première page |
| Bases de données et entrepôts de données | Champ de métadonnées de classification : `pii_present = true` ; champ de catégorie DCP renseigné |
| E-mail | Ajout de préfixe de sujet où le contenu contient des DCP : `[DP]` ou `[DPS]` pour catégorie spéciale |
| Nommage des fichiers/dossiers | Suffixe `_DCP` ou `_DCS` lorsque pratique et cohérent avec les capacités du système |

### Étiquetage des DCP de catégorie spéciale

Les informations contenant des DCP de catégorie spéciale DOIVENT porter en plus un indicateur de catégorie spéciale pour permettre une manipulation renforcée. Le format spécifique de cet indicateur est défini dans PRIV-IMP-A.3.5-7-TG.

### Étiquetage des systèmes et référentiels

Les référentiels, bases de données, systèmes et environnements de traitement qui stockent ou traitent des DCP DOIVENT être étiquetés au niveau système avec : la présence de DCP (oui/non) ; les catégories de DCP traitées (ordinaires, financières, catégorie spéciale, ou liste des catégories applicables) ; le périmètre juridictionnel applicable (ex. personnes concernées UE/EEE, personnes concernées suisses).

L'étiquetage au niveau système est maintenu dans le Registre des actifs de données (voir PRIV-IMP-A.3.5-7-TG pour la structure du registre).

### Obligation de cohérence de l'étiquetage

Lorsque l'étiquette de classification SGSI et l'exigence d'étiquetage DCP sont en conflit (ex. un actif est classifié INTERNE selon les critères SGSI mais contient des DCP ordinaires nécessitant une classification CONFIDENTIEL), la classification la plus élevée DOIT prévaloir et le plancher minimum DCP DOIT s'appliquer.

---

# Règles et accords de transfert des DCP (A.3.7)

## Exigences de transfert des DCP

[Organisation] DOIT établir et maintenir des règles, procédures et accords couvrant tout transfert de DCP par tous types de moyens, qu'ils soient internes ou externes, électroniques ou physiques.

### Transfert interne des DCP

**Au sein de [Organisation]** : Les DCP NE DOIVENT être transférés qu'aux rôles et personnels organisationnels disposant d'une finalité de traitement légitime et d'une autorisation d'accès appropriée ; le transfert interne de DCP RESTREINTS (catégorie spéciale) DOIT être journalisé et traçable ; les transferts DCP de système à système DOIVENT utiliser des canaux chiffrés ; le transfert interne de DCP vers des environnements de traitement dans d'autres juridictions DOIT être traité comme un transfert transfrontalier.

### Transfert externe des DCP

**Vers les Sous-traitants de DCP** : Les transferts externes de DCP vers des sous-traitants NÉCESSITENT un accord de sous-traitance actuel et valide (Article 28 RGPD ; Article 9 LPD suisse) en place avant le début du transfert. Aucun transfert de DCP vers un sous-traitant externe ne DOIT avoir lieu sans accord de sous-traitance signé. Le DPD tient le Registre des accords de sous-traitance.

**Vers les Co-responsables** : Les transferts externes de DCP vers des co-responsables NÉCESSITENT un arrangement de co-responsabilité (Article 26 RGPD) documentant les responsabilités respectives. Le DPD DOIT approuver les arrangements de co-responsabilité avant le transfert de DCP.

**Vers les Destinataires et Tiers** : Les transferts externes de DCP vers des destinataires autres que des sous-traitants ou co-responsables nécessitent : une base légale documentée per RGPD Article 6 ; la revue du DPD lorsque la divulgation n'est pas routinière ; un enregistrement du transfert dans le RADT.

### Transfert international et transfrontalier des DCP

Les transferts de DCP vers des pays ou organisations internationales hors EEE (pour le RGPD) ou hors de Suisse (pour la LPD suisse) sont soumis aux exigences suivantes :

**Base légale du transfert** :

| Mécanisme | Applicabilité |
|-----------|--------------|
| Décision d'adéquation (Commission UE / PFPDT suisse) | Transferts vers des pays à protection adéquate — aucune mesure supplémentaire requise |
| Clauses Contractuelles Types (CCT) | Transferts vers des pays sans adéquation — CCT UE (2021) ou CCT suisses selon le cas |
| Règles d'entreprise contraignantes (BCR) | Transferts intragroupe avec BCR approuvées par l'APD compétente — applicable uniquement aux groupes ayant obtenu l'approbation APD ; ce mécanisme est inclus pour exhaustivité ; sa disponibilité dépend de la structure de l'entreprise |
| Dérogations Article 49 | Circonstances exceptionnelles uniquement (consentement de la personne concernée, intérêts vitaux, intérêt public important, réclamations juridiques) — pas pour les transferts systématiques |

**Évaluation d'Impact du Transfert (EIT)** : Lorsque des CCT ou d'autres mécanismes contractuels sont utilisés, [Organisation] DOIT conduire une EIT évaluant si le cadre juridique du pays de destination fournit une protection essentiellement équivalente. L'EIT, la décision sur les mesures supplémentaires et l'approbation du DPD DOIVENT être documentées dans le Registre des transferts internationaux.

### Méthodes de transfert pour les DCP

| Type de transfert | DCP CONFIDENTIEL | DCP RESTREINT / Catégorie spéciale |
|------------------|------------------|------------------------------------|
| **Électronique — interne** | Canal chiffré (TLS minimum) | Canal chiffré + entrée dans le journal d'accès |
| **Électronique — externe** | E-mail chiffré ou plateforme de transfert sécurisé | Plateforme chiffrée de bout en bout ; vérification de l'identité du destinataire requise |
| **Physique — documents** | Enveloppe scellée, livraison suivie, signature du destinataire | Double scellage, coursier agréé, documentation de la chaîne de custody |
| **Physique — supports** | Support chiffré, livraison suivie | Support chiffré, coursier sécurisé, confirmation de livraison |
| **Cloud — traitement** | Chiffré au repos et en transit ; résidence des données vérifiée | Chiffré au repos et en transit ; résidence confirmée ; sous-traitant approuvé par l'APD |

### Accords de transfert

Tous les transferts externes de DCP dans le cadre de relations continues DOIVENT être régis par un accord écrit couvrant au minimum : les finalités pour lesquelles le destinataire peut utiliser les DCP ; les limites de conservation et les obligations de suppression/retour ; les mesures de sécurité que le destinataire doit maintenir ; les restrictions sur l'engagement de sous-traitants ultérieurs ; les obligations et délais de notification des violations ; les droits d'audit (le cas échéant) ; la loi applicable et la juridiction. Le DPD tient le Registre des accords de transfert. Aucun transfert externe continu de DCP ne DOIT être établi sans accord actuel dans le registre.

---

# Rôles et responsabilités

| Rôle | Responsabilités pour A.3.5–A.3.7 |
|------|----------------------------------|
| **DPD** | Autorité principale pour les niveaux de classification minimaux DCP et les règles de transfert ; approuve les mécanismes de transfert transfrontalier ; tient le Registre des transferts internationaux et le Registre des accords de transfert ; examine les déterminations de classification par agrégation |
| **Propriétaire des données** | Classe les jeux de données DCP dans son domaine ; applique les étiquettes DCP ; autorise les transferts internes ; escalade les transferts transfrontaliers au DPD |
| **RSSI** | Assure l'extension cohérente du schéma de classification SGSI aux DCP per cette politique ; assure la mise en œuvre des contrôles de transfert (chiffrement, journalisation) |
| **Équipe Sécurité IT / Propriétaires de systèmes** | Mettent en œuvre l'étiquetage DCP au niveau système ; configurent les canaux de transfert chiffré ; maintiennent les métadonnées de classification des systèmes |
| **Champions de la protection des données** | Soutien de première ligne pour les questions de classification DCP ; escalade des déclencheurs de reclassification |
| **Juridique/Conformité** | Conseille sur les mécanismes de transfert transfrontalier ; examine les CCT et décisions d'adéquation des APD |
| **Tout le personnel** | Applique la classification et l'étiquetage aux DCP gérés dans son rôle ; utilise uniquement les méthodes de transfert approuvées ; signale toute mauvaise classification suspectée |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Registre de classification | Enregistrements des classifications de jeux de données DCP, y compris les déterminations par agrégation | 3 ans à compter du remplacement de la classification ou de l'élimination du jeu de données |
| Registre des actifs de données | Enregistrements d'étiquetage DCP au niveau système | En cours + 3 ans |
| Registre des transferts internationaux | Enregistrements EIT, CCT, références de décisions d'adéquation, approbations DPD | Durée de l'activité de transfert + 3 ans |
| Registre des accords de transfert | Accords de sous-traitance signés, arrangements de co-responsabilité, accords avec les destinataires | Durée de l'accord + 3 ans |
| Journaux de transfert interne | Journaux des transferts internes de DCP RESTREINTS, y compris la finalité et l'autorisation | 3 ans à compter de la date du transfert |
| Enregistrements de révision de classification | Preuves de révision périodique et déclenchée | 3 ans à compter de la date de la révision |

---

# Considérations d'audit

**Pour A.3.5 (Classification)** : Documentation du schéma de classification montrant les niveaux minimaux DCP ; preuves que les jeux de données DCP sont classifiés au niveau minimum requis ; déterminations de classification par agrégation ; enregistrements de révision de classification.

**Pour A.3.6 (Étiquetage)** : Procédures d'étiquetage couvrant les informations contenant des DCP dans tous les formats ; exemples de documents étiquetés et métadonnées système montrant les champs d'indicateur DCP ; Registre des actifs de données avec champs DCP renseignés.

**Pour A.3.7 (Transfert)** : Règles et procédures de transfert couvrant les transferts internes et externes ; accords de sous-traitance signés pour toutes les relations actives ; Registre des transferts internationaux avec documentation EIT ; journaux de transfert pour les DCP RESTREINTS.

---

<!-- QA_VERIFIED: 2026-04-03 -->
