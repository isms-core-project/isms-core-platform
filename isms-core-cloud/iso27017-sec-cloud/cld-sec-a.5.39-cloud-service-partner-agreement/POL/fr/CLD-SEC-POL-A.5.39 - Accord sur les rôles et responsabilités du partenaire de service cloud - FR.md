<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.39-FR:sec:POL:a.5.39 -->
**CLD-SEC-POL-A.5.39 — Accord sur les rôles et responsabilités du partenaire de service cloud**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Accord sur les rôles et responsabilités du partenaire de service cloud |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-SEC-POL-A.5.39 |
| **Auteur du document** | RSSI / Responsable Sécurité Cloud |
| **Propriétaire du document** | RSSI |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date à définir] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Cloud** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date à définir] | RSSI | Politique initiale pour la mise en œuvre d'ISO/IEC 27017:2026 Éd. 2 |

**Cycle de révision** : Annuel (ou lors de l'intégration/du changement d'un partenaire de service cloud, ou à la suite de toute escalade liée à un conflit de périmètre)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : RSSI
- Secondaire : Responsable Sécurité Cloud
- Conformité : Responsable Juridique/Conformité
- Autorité finale : Direction générale

**Documents connexes** :

- CLD-SEC-POL-A.5.38 (Rôles et responsabilités partagés au sein d'un environnement d'informatique en nuage — l'allocation CSC/CSP à laquelle cette politique doit rester cohérente)
- ISMS-POL-A.5.19-23-S1 (Fondamentaux des relations fournisseurs)
- ISMS-POL-A.5.19-23-S2 (Exigences des accords fournisseurs)
- ISMS-POL-A.5.19-23-S5 (Sécurité des services cloud)
- CLD-SEC-IMP-A.5.39-TG (Accord sur les rôles et responsabilités du partenaire de service cloud — Guide technique, contient le schéma complet du registre des rôles CSN et du contrôle de cohérence)
- CLD-SEC-REF-A.5-A.8 (Addendum de guidance sur la sécurité cloud)
- ISO/IEC 27017:2026, Clause 5.39 (CLD — Accord sur les rôles et responsabilités du partenaire de service cloud)
- ISO/IEC 22123-3 (Informatique en nuage — Architecture de référence)

---

## Résumé exécutif

Cette politique établit la manière dont [Organisation] classe, définit et convient des rôles et responsabilités en matière de sécurité de l'information de tout **partenaire de service cloud (CSN)** qu'elle engage ou par lequel elle est engagée, conformément à ISO/IEC 27017:2026, Clause 5.39.

**Périmètre** : Tous les partenaires de service cloud — tiers dont les activités soutiennent ou sont auxiliaires au rôle de client de service cloud (CSC) de [Organisation], au rôle de fournisseur de service cloud (CSP) de [Organisation], ou aux deux. Selon ISO/IEC 22123-3, les activités d'un CSN relèvent généralement d'un ou plusieurs des trois sous-rôles suivants : développeur de service cloud, auditeur cloud et courtier de service cloud.

**Note sur les contrôles étendus** : ISO/IEC 27017:2026, Clause 5.39 est l'un des quatre contrôles étendus spécifiques au cloud « CLD » introduits par la deuxième édition de la norme (aux côtés des clauses 5.38, 8.35 et 8.36). Il est entièrement nouveau — il n'a pas d'équivalent dans la première édition de 2015 d'ISO/IEC 27017 ni d'équivalent direct dans ISO/IEC 27002:2022. [Organisation] le met en œuvre comme une extension informative de son SGSI fondé sur ISO/IEC 27001:2022.

**Relation avec CLD-SEC-POL-A.5.38** : Le CSC et le CSP disposent déjà de rôles et responsabilités partagés entre eux au titre de CLD-SEC-POL-A.5.38. Tout accord conclu par [Organisation] avec un partenaire de service cloud DOIT être cohérent avec cette allocation partagée préexistante — un accord CSN ne peut pas réattribuer une responsabilité en dehors du CSC ou du CSP sans le consentement des deux. Un engagement CSN qui créerait une telle réattribution est traité comme un risque de sécurité de l'information nécessitant une escalade avant signature, et non comme une question à résoudre après coup.

---

# Périmètre et applicabilité

## ISO/IEC 27017:2026 — Clause 5.39

**Énoncé du contrôle (ISO/IEC 27017:2026, 5.39) :**
> « Les rôles et responsabilités en matière de sécurité de l'information du CSN devraient être définis et convenus avec le CSC ou le CSP qui utilise le service du CSN. »

**Finalité (ISO/IEC 27017:2026, 5.39) :**
> « Délimiter les rôles et responsabilités du CSC et du CSP lors du recours à un CSN. »

*(Traduction de travail établie à partir du texte anglais original de la norme, à des fins de lisibilité ; en cas de divergence, le texte anglais officiel d'ISO/IEC 27017:2026 fait foi.)*

## Sous-rôles du partenaire de service cloud (selon ISO/IEC 22123-3)

| Sous-rôle | Description | Exemples typiques pour [Organisation] |
|-----------|-------------|-----------------------------------------|
| **Développeur de service cloud** | Conçoit, développe, teste ou maintient des composants utilisés pour fournir un service cloud | Cabinet d'ingénierie contractant construisant un module utilisé dans un service fourni ; fournisseur de pipeline CI/CD géré |
| **Auditeur cloud** | Réalise une évaluation indépendante du fonctionnement, des contrôles ou de la conformité d'un service cloud | Auditeur externe ISO/IEC 27001 ou SOC 2 ; cabinet indépendant de tests d'intrusion |
| **Courtier de service cloud** | Gère l'utilisation, la performance ou la fourniture de services cloud, et négocie les relations entre CSC et CSP | Revendeur cloud ; fournisseur de services managés agrégeant plusieurs CSP pour le compte de [Organisation] |

Un CSN peut détenir un seul sous-rôle, plusieurs sous-rôles, ou — dans certains engagements — agir comme CSN autonome dans une relation tout en agissant comme CSP dans une autre. [Organisation] DOIT déterminer et documenter le(s) sous-rôle(s) applicable(s) pour chaque partenaire de service cloud qu'elle engage, en utilisant la procédure de classification décrite dans CLD-SEC-IMP-A.5.39-UG, Partie 1.

## Applicabilité

Cette politique s'applique à :

- Tous les tiers que [Organisation] engage, en sa qualité de CSC ou de CSP, dont les activités répondent à la définition ISO/IEC 22123-3 d'un partenaire de service cloud (sous-rôle développeur, auditeur ou courtier)
- Toutes les équipes internes responsables de la sélection, de la contractualisation ou de la supervision de ces partenaires

---

# Dispositions de la politique : Accord sur les rôles du partenaire de service cloud (5.39)

## Classification et accord sur les rôles du CSN

[Organisation] DOIT, avant qu'un partenaire de service cloud n'entame une quelconque activité affectant un service cloud que [Organisation] consomme (en tant que CSC) ou fournit (en tant que CSP) :

- Classer le tiers au regard des trois sous-rôles ISO/IEC 22123-3, et confirmer si l'engagement fait également du tiers un CSP à part entière (auquel cas CLD-SEC-POL-A.5.38 s'applique en complément à cette partie de la relation)
- Définir clairement les rôles et responsabilités que le CSN est censé assumer, en lien avec son (ses) sous-rôle(s) classifié(s), avant la conclusion de la négociation contractuelle
- Récupérer et vérifier les responsabilités proposées du CSN au regard de la matrice de responsabilité partagée (CLD-SEC-IMP-A.5.38-TG, Section 1) pour la relation de service cloud que le CSN soutiendra
- Conclure un accord écrit avec le CSN sur ces rôles et responsabilités avant que le CSN ne commence à travailler — un accord informel ou verbal ne satisfait pas cette exigence
- Lorsque le contrôle de cohérence identifie un conflit avec l'allocation CSC/CSP existante, obtenir le consentement écrit de la contrepartie (CSC ou CSP) avant de poursuivre, ou décliner l'engagement

## Exigences contractuelles

Tout engagement de partenaire de service cloud relevant du périmètre de cette politique DOIT être régi par un accord écrit, négocié conformément à ISMS-POL-A.5.19-23-S2 (Exigences des accords fournisseurs), qui au minimum :

- Identifie le(s) sous-rôle(s) du CSN (développeur, auditeur, courtier, ou combinaison)
- Énonce les responsabilités spécifiques en matière de sécurité de l'information assignées au CSN, en tant que texte contractuel — et non comme une entente informelle annexe
- Confirme que les obligations du CSN ne sont pas en conflit avec les engagements de responsabilité partagée CSC/CSP existants de [Organisation], en faisant référence au contrôle de cohérence effectué

## Communication des rôles convenus

[Organisation] DOIT communiquer les rôles et responsabilités convenus du CSN aux équipes internes travaillant avec le CSN (prestation de services cloud, ingénierie, personnel de projet concerné) via le registre des rôles CSN et le programme de sensibilisation à la sécurité de l'information de l'organisation (voir ISMS-POL-A.6.3), ainsi qu'au personnel opérationnel propre du CSN via l'accord signé, complété par une discussion conjointe sur les responsabilités pour les engagements dont le périmètre est pertinent en matière de sécurité de l'information.

## Registre des rôles CSN — Contenu minimal

Le registre des rôles CSN (schéma complet dans CLD-SEC-IMP-A.5.39-TG, Section 1) DOIT consigner, par partenaire de service cloud, au minimum : le nom du CSN ; son (ses) sous-rôle(s) classifié(s) et s'il agit également de manière indépendante en tant que CSP ; les responsabilités qui lui sont assignées ; la relation de service cloud concernée et la référence à la matrice de responsabilité partagée ; la référence et la date de l'accord ; le résultat du contrôle de cohérence ; et la date de la dernière révision. Le registre DOIT être tenu par le Responsable Sécurité Cloud et révisé au moins une fois par an.

## Supervision continue et changements de périmètre

[Organisation] DOIT :

- Réviser le registre des rôles CSN au moins une fois par an, en confirmant que la classification, les responsabilités convenues et la cohérence continue avec la matrice de responsabilité partagée applicable de chaque CSN demeurent exactes
- Réévaluer la classification et la cohérence, et modifier l'accord en conséquence, chaque fois que l'activité réelle d'un CSN change substantiellement par rapport à son périmètre initialement convenu
- Faire remonter au Responsable Sécurité Cloud, et en cas de non-résolution au RSSI, tout cas où l'activité d'un CSN s'avère excéder son périmètre convenu, en traitant cela comme un risque de sécurité de l'information nécessitant une évaluation, et non comme une simple formalité contractuelle

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Est propriétaire de CLD-SEC-POL-A.5.39 ; approuve les engagements CSN dont le périmètre est pertinent en matière de sécurité de l'information ; résout les conflits entre les accords CSN et les allocations CSC/CSP existantes ; examine les escalades de risques liées aux CSN |
| **Responsable Sécurité Cloud** | Classe chaque CSN potentiel par sous-rôle ; effectue et consigne le contrôle de cohérence au regard de la matrice de responsabilité partagée applicable avant la signature de l'accord CSN ; tient à jour le registre des rôles CSN ; rapporte au RSSI les indicateurs de couverture CSN |
| **Responsable Juridique/Conformité** | Négocie et conclut les accords CSN conformément à ISMS-POL-A.5.19-23-S2 ; s'assure que les rôles et responsabilités convenus sont retranscrits dans le texte contractuel |
| **Prestation de services cloud / Ingénierie** | Opère dans les limites des rôles convenus du CSN ; fait remonter toute activité du CSN excédant son périmètre convenu |

---

# Exigences en matière de preuves

| Preuve | Description | Propriétaire | Conservation |
|-------|-------------|-------------|-------------|
| Registre des rôles CSN | Liste de tous les partenaires de service cloud actifs avec sous-rôle(s) assigné(s), périmètre et référence de l'accord | Responsable Sécurité Cloud | En cours + 3 ans à compter de la fin de l'engagement |
| Extraits des accords CSN | Extrait de l'accord écrit de chaque CSN énonçant les rôles et responsabilités convenus | Responsable Juridique/Conformité | Durée de l'accord + 3 ans |
| Registres du contrôle de cohérence | Registres confirmant que chaque accord CSN a été vérifié au regard de la matrice de responsabilité partagée applicable avant signature, y compris le résultat et tout consentement de contrepartie obtenu | Responsable Sécurité Cloud | En cours + 3 ans |
| Registres des avenants pour changement de périmètre | Registres de la reclassification du périmètre CSN et des avenants à l'accord en cas de changement substantiel de l'activité d'un CSN | Responsable Sécurité Cloud | En cours + 3 ans |
| Registres d'escalade de risques liés aux CSN | Registres de tout conflit lié à un CSN ou de tout dépassement de périmètre escaladé dans le processus d'appréciation et de traitement des risques, avec sa résolution | RSSI | En cours + 3 ans |

---

# Suivi et indicateurs

Le Responsable Sécurité Cloud rapporte au RSSI, au moins trimestriellement :

- La proportion des partenaires de service cloud actifs disposant d'une entrée à jour et classifiée dans le registre des rôles CSN et d'un contrôle de cohérence achevé
- Le nombre d'engagements CSN pour lesquels un conflit avec l'allocation CSC/CSP existante a été identifié, et la manière dont il a été résolu
- Le nombre d'escalades pour dépassement de périmètre et leur statut de résolution

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-SEC-POL-A.5.39 doivent s'attendre à trouver :

- Un registre des rôles CSN couvrant chaque tiers répondant à la définition ISO/IEC 22123-3 d'un partenaire de service cloud
- Des accords écrits énonçant explicitement le(s) sous-rôle(s) assigné(s) et les responsabilités en matière de sécurité de l'information du CSN
- Des preuves documentées que chaque accord CSN a été vérifié au regard de la matrice de responsabilité partagée applicable au titre de CLD-SEC-POL-A.5.38 avant sa conclusion, y compris la manière dont tout conflit a été résolu
- Des preuves que les changements de périmètre ont déclenché une reclassification et un avenant à l'accord, et non une dérive silencieuse
- Des indicateurs de suivi trimestriels démontrant une surveillance active, et non un exercice ponctuel réalisé lors de l'intégration

---

<!-- QA_VERIFIED: 2026-08-01 -->
