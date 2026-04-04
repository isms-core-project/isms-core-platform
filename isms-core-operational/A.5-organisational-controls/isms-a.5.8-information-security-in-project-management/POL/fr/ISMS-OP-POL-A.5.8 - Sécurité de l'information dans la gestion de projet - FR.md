<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.8-FR:operational:OP-POL:a.5.8 -->
**ISMS-OP-POL-A.5.8 — Sécurité de l'information dans la gestion de projet**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité de l'information dans la gestion de projet |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.8 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
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

- ISO/IEC 27001:2022 Contrôle A.5.8 — Sécurité de l'information dans la gestion de projet
- ISO/IEC 27002:2022 Section 5.8 — Conseils d'implémentation
- ISO 21500:2021 — Gestion de projets, programmes et portefeuilles
- nFADP suisse (LPD révisée) Art. 22 — Analyse d'impact relative à la protection des données
- NIST SP 800-53 Rév. 5 SA-3 — Cycle de développement des systèmes
- NIST SP 800-53 Rév. 5 PL-2 — Plans de sécurité et de protection de la vie privée des systèmes

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la sécurité de l'information dans la gestion de projet |
|----------|----------------------------------------------------------------------|
| A.5.1 Politiques de sécurité de l'information | Cadre de politique général fournissant la base des exigences de sécurité pour les projets |
| A.5.7 Renseignement sur les menaces | Le renseignement sur les menaces informe l'évaluation des risques et la modélisation des menaces spécifiques au projet |
| A.5.9 Inventaire des informations et des actifs associés | Les projets créent de nouveaux actifs qui doivent être enregistrés lors du transfert |
| A.5.12 Classification de l'information | La classification des données détermine la classification de sécurité du projet et la sélection des contrôles |
| A.5.19 Sécurité de l'information dans les relations avec les fournisseurs | Les exigences de sécurité des fournisseurs s'appliquent aux projets impliquant des prestataires externes |
| A.5.34 Protection de la vie privée et des DCP | Exigences d'AIPD pour les projets traitant des données personnelles |
| A.8.25 Cycle de développement sécurisé | Exigences de développement sécurisé pour les projets logiciels |
| A.8.26 Exigences de sécurité des applications | Identification des exigences de sécurité pour les projets d'application |
| A.8.27 Architecture et principes d'ingénierie des systèmes sécurisés | Sécurité de l'architecture pour les projets d'infrastructure et de systèmes |
| A.8.29 Tests de sécurité dans le développement et l'acceptation | Exigences de tests de sécurité intégrées dans les jalons de phase du projet |
| A.8.32 Gestion du changement | Processus de contrôle du changement pour les modifications de la production initiées par les projets |

**Politiques internes connexes** :

- Politique de classification et de traitement de l'information
- Politique de sécurité des relations avec les fournisseurs
- Politique de cycle de développement sécurisé
- Politique de gestion du changement
- Politique de protection de la vie privée et des DCP
- Politique de gestion des risques

---

# Politique de sécurité de l'information dans la gestion de projet

## Objet

L'objet de cette politique est de veiller à ce que les risques de sécurité de l'information liés aux projets et aux livrables des projets soient systématiquement identifiés, évalués et traités tout au long du cycle de vie du projet. La sécurité de l'information doit être intégrée dans la gestion de projet afin qu'elle fasse partie de chaque projet — et non comme une mesure corrective appliquée en fin de parcours.

Les projets introduisent du changement. Le changement introduit des risques. Qu'il s'agisse d'une nouvelle application logicielle, d'une mise à niveau de l'infrastructure, d'un achat auprès d'un fournisseur ou d'une refonte d'un processus métier, chaque projet crée des opportunités pour que les contrôles de sécurité soient affaiblis, contournés ou omis si la sécurité n'est pas explicitement traitée à chaque phase.

Cette politique soutient la nFADP suisse (LPD révisée) en mettant en œuvre des mesures organisationnelles appropriées au risque pour protéger les données personnelles lors des activités de projet, y compris l'exigence d'analyses d'impact relatives à la protection des données (AIPD) en vertu de l'art. 22, lorsque le traitement est susceptible d'entraîner un risque élevé pour la personnalité ou les droits fondamentaux des individus. Là où l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences de l'art. 25 du RGPD (protection des données dès la conception et par défaut) et de l'art. 35 (AIPD) s'appliquent également.

## Périmètre

Tous les projets entrepris par l'organisation, quel que soit leur type, leur méthodologie, leur taille ou leur durée. Cela comprend :

- Les projets de développement logiciel (internes et externalisés).
- Les projets de mise en œuvre et d'intégration de systèmes.
- Les projets de déploiement et de migration d'infrastructure (sur site et dans le nuage).
- Les projets d'approvisionnement informatique (matériel, logiciels, services SaaS).
- Les projets de refonte de processus métier ayant des implications pour la sécurité de l'information.
- Les projets de mise en conformité réglementaire.
- Les projets de fusion, d'acquisition ou de cession impliquant des actifs informatiques ou des données.

**Hors périmètre** : Les activités opérationnelles de routine ne constituant pas un projet (maintenance et support courants) ; les activités de réponse aux incidents d'urgence (couvertes par la Politique de gestion des incidents) ; les modifications mineures gérées via le processus standard de contrôle du changement (couvertes par la Politique de gestion du changement). En cas d'incertitude sur la qualification d'une activité en tant que projet, le RSSI ou le Responsable de la sécurité de l'information devrait conseiller.

## Principe

La sécurité de l'information devrait être intégrée dans la gestion de projet. Les exigences de sécurité doivent être identifiées tôt — lors de l'initiation du projet — et traitées de manière proportionnée tout au long du cycle de vie du projet en fonction de la classification du risque de sécurité du projet. Aucun projet ne doit passer au déploiement en production sans validation de sécurité appropriée pour son niveau de classification.

Toutes les décisions de sécurité du projet doivent être basées sur les risques, en tenant compte de la sensibilité et de la classification des données impliquées, de la criticité des systèmes affectés, de l'environnement réglementaire et du potentiel d'impact sur l'activité si la sécurité est insuffisante.

---

## Classification des projets

Tous les projets doivent être classifiés selon le risque de sécurité de l'information afin de déterminer les exigences de sécurité proportionnées. La classification doit avoir lieu lors de l'initiation du projet et être documentée dans la charte de projet ou le document d'initiation équivalent.

### Facteurs de classification

Les projets doivent être classifiés en fonction du **facteur le plus élevé applicable** selon les dimensions suivantes :

| Facteur | Risque élevé | Risque moyen | Risque faible |
|---------|-------------|-------------|--------------|
| **Sensibilité des données** | Données confidentielles ou restreintes (DCP, dossiers financiers, propriété intellectuelle, secrets commerciaux) | Données internes (informations commerciales non publiques, dossiers des employés) | Données publiques (contenu marketing, documentation publiée) |
| **Criticité du système** | Système critique pour l'activité (OTR < 4 heures) ; générateur de revenus ou orienté clients | Système important pour l'activité (OTR 4-24 heures) ; opérationnel interne | Système de support (OTR > 24 heures) ; outils non critiques |
| **Périmètre réglementaire** | Traitement à risque élevé selon la nFADP, AIPD requise selon l'art. 35 RGPD, PCI DSS applicable | Traitement standard nFADP applicable | Aucun traitement de données réglementées |
| **Exposition externe** | Accessible depuis Internet ou par des parties externes (clients, partenaires, public) | Accès externe contrôlé (VPN, connexion dédiée) | Accès interne uniquement |
| **Implication de tiers** | Fonction critique externalisée (hébergement, authentification, traitement des paiements) | Composants gérés par un fournisseur (intégration SaaS, services gérés) | Livraison entièrement interne |

**Règle de classification** : Si **un seul facteur** satisfait aux critères de risque élevé, le projet doit être classifié comme **risque élevé**. Si un facteur satisfait au risque moyen (et qu'aucun facteur n'est à risque élevé), classifier comme **risque moyen**. Ce n'est que si **tous les facteurs** sont à faible risque que le projet doit être classifié comme **risque faible**.

### Exemples de classification

Pour soutenir des décisions de classification cohérentes, les exemples suivants illustrent des scénarios de projet typiques par niveau de classification :

| Facteur | Exemple risque élevé | Exemple risque moyen | Exemple risque faible |
|---------|---------------------|---------------------|----------------------|
| **Sensibilité des données** | Données de carte de crédit des clients, dossiers de santé des employés | Adresses e-mail des employés, rapports financiers internes | Brochures marketing, documentation publique |
| **Criticité du système** | Système de traitement des paiements (OTR < 1 heure) | CRM interne (OTR 8 heures) | Environnement de test, système de preuve de concept |
| **Périmètre réglementaire** | AIPD requise selon l'art. 35 RGPD (profilage), commerçant PCI DSS niveau 1 | nFADP suisse applicable (données personnelles standard) | Aucune donnée réglementée |
| **Exposition externe** | Site web public, API orientée clients | Extranet partenaires, accès VPN uniquement | LAN interne uniquement |
| **Implication de tiers** | Processeur de paiement hébergé dans le nuage, SaaS d'authentification | Hébergé sur AWS avec gestion organisationnelle, Office 365 | Entièrement interne, sur site |

### Approbation de la classification

| Classification | Autorité d'approbation |
|----------------|------------------------|
| **Risque élevé** | Approbation du RSSI requise |
| **Risque moyen** | Approbation du Responsable de la sécurité de l'information |
| **Risque faible** | Auto-classification par le Chef de projet ; confirmation par le Responsable de la sécurité de l'information |

La classification doit être révisée à chaque jalon de phase. Si le périmètre du projet, la sensibilité des données ou l'exposition externe change de manière significative, la classification doit être mise à jour et de nouveau approuvée.

### Guide budgétaire pour la sécurité

Les chefs de projet doivent estimer les coûts de sécurité en fonction de la classification du projet lors de la préparation des budgets :

| Classification | Coût de sécurité typique | Activités incluses |
|----------------|--------------------------|--------------------|
| **Risque élevé** | 8-12 % du coût total du projet | Modélisation des menaces, révision de l'architecture de sécurité, tests d'intrusion, revue du code de sécurité, temps du Responsable de la sécurité de l'information |
| **Risque moyen** | 4-6 % du coût total du projet | Analyse des exigences de sécurité, analyse des vulnérabilités, tests de sécurité fonctionnels, temps du Responsable de la sécurité de l'information |
| **Risque faible** | 1-2 % du coût total du projet | Revue de la liste de contrôle de sécurité, analyse de vulnérabilité de base |

Les estimations du budget de sécurité doivent être incluses dans la documentation d'initiation du projet et approuvées dans le cadre du budget du projet. Lorsque les coûts de sécurité réels sont susceptibles de dépasser la plage estimée, le Chef de projet doit en informer le Responsable de la sécurité de l'information et ajuster le budget du projet en conséquence.

---

## Identification des exigences de sécurité

Les exigences de sécurité pour les livrables du projet doivent être identifiées de manière systématique lors de la phase de planification, en fonction de la classification du projet et des catégories d'actifs et de données impliqués.

### Catégories d'exigences

Le Chef de projet, avec le soutien du Responsable de la sécurité de l'information, doit évaluer chacune des catégories d'exigences suivantes par rapport au périmètre du projet :

| Catégorie d'exigence | Applicable quand | Source |
|---------------------|-----------------|--------|
| **Contrôle d'accès** | Tous les projets (niveau de référence minimal) | Politique de gestion des identités et des accès |
| **Protection des données et chiffrement** | Le projet implique des données confidentielles ou restreintes | Politique d'utilisation de la cryptographie, art. 8 nFADP |
| **Sécurité des applications** | Le projet comprend du développement logiciel ou du code personnalisé | Politique de cycle de développement sécurisé |
| **Sécurité de l'infrastructure** | Le projet déploie ou modifie l'infrastructure réseau | Politique de sécurité des réseaux |
| **Sécurité des fournisseurs** | Le projet implique des prestataires externes ou des services cloud | Politique de sécurité des relations avec les fournisseurs |
| **Protection de la vie privée et des DCP** | Le projet traite des données personnelles | Politique de protection de la vie privée et des DCP, art. 22 nFADP |
| **Continuité des activités** | Le projet affecte des systèmes critiques pour l'activité | Politique de continuité des activités et de reprise après sinistre |
| **Journalisation et surveillance** | Le projet déploie des systèmes nécessitant une surveillance de sécurité | Politique de journalisation |

### Cartographie des sources d'exigences

Le tableau de référence suivant indique les domaines de politique qui s'appliquent généralement aux types de projets courants, afin d'aider les chefs de projet à identifier les exigences applicables :

| Type de projet | Toujours applicable | Souvent applicable | Conditionnellement applicable |
|---------------|--------------------|--------------------|-------------------------------|
| **Développement logiciel** | Cycle de développement sécurisé, contrôle d'accès, journalisation | Sécurité des applications, protection des données, gestion du changement | Protection de la vie privée et des DCP (si données personnelles), sécurité des fournisseurs (si externalisé) |
| **Déploiement d'infrastructure** | Contrôle d'accès, sécurité des réseaux, journalisation | Gestion de la configuration, continuité des activités | Sécurité des fournisseurs (si géré par un fournisseur) |
| **Approvisionnement SaaS** | Sécurité des fournisseurs, contrôle d'accès | Protection des données, protection de la vie privée et des DCP | Sécurité des applications (si intégration personnalisée) |

### Documentation

- **Projets à risque élevé et moyen** : Les exigences de sécurité doivent être documentées dans un Registre des exigences de sécurité (ou section équivalente dans [Outil de gestion de projet]) et suivies jusqu'à leur mise en œuvre et leurs tests.
- **Projets à risque faible** : Les exigences de sécurité doivent être documentées comme éléments d'atténuation des risques dans le registre des risques du projet avec confirmation de la conformité à la politique applicable.

### Approbation

- **Risque élevé** : Le RSSI approuve les exigences de sécurité avant la phase d'exécution.
- **Risque moyen** : Le Responsable de la sécurité de l'information approuve avant la phase d'exécution.
- **Risque faible** : Le Responsable de la sécurité de l'information confirme l'exhaustivité des exigences.

---

## Révisions de sécurité aux jalons de phase

Les révisions de sécurité doivent être intégrées dans la gouvernance du projet aux jalons de phase suivants. Les projets ne doivent pas passer à la phase suivante tant que les critères de sécurité du jalon actuel ne sont pas satisfaits ou formellement acceptés par l'autorité appropriée.

### Exigences des jalons de phase

| Jalon de phase | Activités de sécurité requises |
|----------------|--------------------------------|
| **Initiation / Approbation du projet** | Classification du risque de sécurité déterminée et approuvée ; risques de sécurité initiaux identifiés dans le registre des risques du projet ; budget et ressources de sécurité estimés ; dépistage AIPD effectué (voir section Intégration AIPD) |
| **Planification / Approbation de la conception** | Exigences de sécurité documentées, révisées et approuvées ; modèle de menaces complété pour les projets à risque élevé (recommandé pour le risque moyen) ; architecture de sécurité révisée pour les projets à risque élevé ; AIPD complétée lorsque le dépistage a indiqué un risque élevé |
| **Exécution / Point de contrôle de construction** | Tests de sécurité effectués conformément aux exigences de classification ; résultats des tests de sécurité suivis et remédiés selon les cibles de gravité ; exigences de sécurité tracées jusqu'aux preuves de mise en œuvre |
| **Déploiement / Approbation de la mise en production** | Toutes les constatations critiques remédiées ; constatations importantes remédiées selon les cibles de classification (voir section Tests de sécurité) ; documentation de transfert de sécurité complète et acceptée par les opérations ; risques résiduels formellement documentés et acceptés par l'autorité appropriée |
| **Clôture** | Enseignements tirés documentés (obligatoire pour les risques élevés/moyens) ; nouveaux actifs enregistrés dans l'inventaire des actifs ; risques résiduels transférés au registre des risques opérationnels ; documentation de sécurité du projet archivée conformément aux exigences de gestion des enregistrements |

### Délais d'escalade

Les préoccupations de sécurité aux jalons de phase doivent être escaladées dans les délais suivants :

- **2 jours ouvrables** pour les projets à risque élevé.
- **5 jours ouvrables** pour les projets à risque moyen.

**Chemin d'escalade** : Chef de projet → Responsable de la sécurité de l'information → RSSI → Direction générale.

Les projets ne doivent pas passer à la phase suivante sans résoudre les préoccupations de sécurité critiques. Les préoccupations de sécurité importantes peuvent être traitées avec une acceptation formelle du risque de l'autorité appropriée. Les préoccupations moyennes et faibles peuvent être traitées avec un plan d'atténuation documenté.

---

## Tests de sécurité par classification

Tous les projets doivent inclure des tests de sécurité proportionnés à leur niveau de classification. Les tests doivent être complétés avant le déploiement et les résultats documentés.

### Exigences de tests

| Exigence | Risque élevé | Risque moyen | Risque faible |
|----------|-------------|-------------|--------------|
| **Test d'intrusion externe** | Obligatoire (tiers indépendant, méthodologie OWASP ou équivalent) | Requis si accessible depuis Internet ou traitant des données réglementées ; sinon recommandé | Non requis |
| **Analyse automatisée des vulnérabilités** | Obligatoire (hebdomadaire pendant le développement + finale avant déploiement) | Obligatoire (analyse finale avant déploiement) | Recommandé |
| **Revue du code de sécurité** | Obligatoire pour le code personnalisé (minimum : authentification, autorisation, protection des données, fonctions cryptographiques) | Recommandé pour le code personnalisé | Non requis |
| **Tests de sécurité fonctionnels** | Obligatoire (authentification, autorisation, validation des entrées, gestion des erreurs, gestion des sessions) | Obligatoire (authentification, autorisation, validation des données, gestion des erreurs) | Validation de la sécurité par rapport à la liste de contrôle des exigences |

### Cibles de remédiation avant déploiement

| Gravité de la constatation | Projets à risque élevé | Projets à risque moyen | Projets à risque faible |
|---------------------------|----------------------|----------------------|----------------------|
| **Critique** | 100 % remédiées | 100 % remédiées | 100 % remédiées |
| **Importante** | ≥ 80 % remédiées | ≥ 70 % remédiées | Au mieux ; risque accepté |
| **Moyenne** | Suivies ; plan de remédiation | Suivies ; plan de remédiation | Suivies |
| **Faible** | Documentées | Documentées | Documentées |

Si les cibles de remédiation ne peuvent pas être atteintes avant la date limite de déploiement, le risque résiduel doit être formellement accepté conformément à la section Gestion des exceptions de cette politique.

Les preuves de test (rapports d'analyse, rapports de test d'intrusion, résultats de revue de code) doivent être archivées conformément aux exigences de gestion des enregistrements.

---

## Transfert et acceptation de la sécurité

À la clôture du projet, la documentation de transfert de sécurité doit être fournie à l'équipe opérationnelle et validée comme complète avant la clôture formelle du projet. Un transfert de sécurité incomplet bloque la clôture du projet.

### Documentation de transfert

Le dossier de transfert de sécurité doit inclure :

1. **Documentation de l'architecture de sécurité** — conception de la sécurité du système, limites de confiance, modèle d'authentification et d'autorisation, mise en œuvre du chiffrement, diagrammes de flux de données avec classification, architecture réseau et segmentation.

2. **Procédures de sécurité opérationnelles** — exigences de surveillance (sources de journaux, seuils d'alerte, intégration [SIEM]), procédures de sauvegarde et de récupération, approche de gestion des correctifs de sécurité, chemins d'escalade de la réponse aux incidents.

3. **Risques résiduels acceptés** — enregistrements formels d'acceptation des risques avec signatures d'approbation, contrôles compensatoires le cas échéant, calendrier de réévaluation des risques pour les acceptations à durée limitée.

4. **Preuves de tests de sécurité** — rapport d'analyse de vulnérabilité final (daté dans les 7 jours suivant le déploiement), rapport de test d'intrusion (le cas échéant), enregistrements de remédiation pour les constatations critiques et importantes.

### Acceptation du transfert

Le propriétaire opérationnel doit confirmer l'exhaustivité du transfert via une Liste de contrôle de transfert de sécurité signée avant que le Chef de projet ne demande l'autorisation de clôture du projet. Pour les projets à risque élevé, le RSSI doit également approuver le transfert.

Après l'acceptation du transfert, le Chef de projet doit s'assurer que :
- Les nouveaux actifs sont enregistrés dans l'inventaire des actifs.
- Les risques résiduels sont transférés au registre des risques opérationnels.
- La documentation de sécurité est archivée conformément aux exigences de gestion des enregistrements.

---

## Rôles de sécurité du projet

### Matrice RACI

| Activité | Chef de projet | Resp. sécurité info. | RSSI | Propriétaire métier | Responsable technique |
|----------|:-:|:-:|:-:|:-:|:-:|
| Classification du risque de sécurité du projet | R | A | I | C | C |
| Identification des exigences de sécurité | R | A | I | C | C |
| Conception de l'architecture de sécurité | C | C | I | I | R/A |
| Exécution des tests de sécurité | R | C | I | I | R |
| Acceptation du risque résiduel | I | C | A (Élevé) | A (Moy/Faible) | I |
| Transfert de sécurité aux opérations | R | A | I | C | C |
| Enseignements tirés | R | C | I | C | C |

R = Responsable (effectue le travail), A = Approbateur (décision finale), C = Consulté (contribution requise), I = Informé (tenu au courant).

### Descriptions des rôles

| Rôle | Responsabilités clés |
|------|---------------------|
| **Direction générale** | Approuver cette politique ; accepter les risques résiduels pour les projets critiques ; assurer les ressources pour la sécurité des projets |
| **RSSI** | Approuver les classifications à risque élevé ; accepter les risques résiduels pour les projets à risque élevé ; stopper les projets présentant un risque de sécurité inacceptable ; surveiller les indicateurs de sécurité des projets |
| **Responsable de la sécurité de l'information** | Soutenir les équipes de projet dans l'évaluation des risques et les exigences ; approuver les classifications à risque moyen ; examiner l'adéquation des tests de sécurité ; maintenir les modèles d'exigences de sécurité |
| **Chef de projet** | Classifier le risque de sécurité du projet ; planifier et budgéter les activités de sécurité ; exécuter les activités de sécurité à chaque phase ; maintenir le registre des risques de sécurité du projet ; escalader les préoccupations de sécurité |
| **Propriétaire métier / Propriétaire produit** | Définir les exigences de sécurité métier ; participer à l'évaluation des risques ; accepter les risques résiduels pour les systèmes gérés (risque moyen/faible) |
| **Responsable technique / Architecte de solution** | Concevoir les contrôles de sécurité dans l'architecture de la solution ; mettre en œuvre les exigences de sécurité ; soutenir la modélisation des menaces ; traiter les résultats des tests de sécurité |
| **Prestataires tiers** | Respecter les exigences contractuelles de sécurité ; participer aux évaluations de sécurité ; signaler les incidents ou vulnérabilités de sécurité |

### Champions de la sécurité (optionnel)

Les organisations de 50 employés ou plus devraient envisager de désigner des Champions de la sécurité au sein des équipes de projet afin d'améliorer l'intégration de la sécurité et de réduire les goulets d'étranglement sur le Responsable de la sécurité de l'information :

| Aspect | Description |
|--------|-------------|
| **Sélection** | Membre de l'équipe formé (développeur, analyste métier ou chef de projet) faisant office de référent sécurité au sein de l'équipe de projet |
| **Formation** | Les Champions de la sécurité doivent suivre une formation en sécurité (minimum 8 heures par an) couvrant les pratiques de développement sécurisé, l'identification des menaces et les politiques de sécurité organisationnelles |
| **Responsabilités** | Aider à identifier les exigences de sécurité lors de la planification ; promouvoir la sécurité au sein de l'équipe de projet ; escalader les préoccupations de sécurité au Responsable de la sécurité de l'information ; soutenir la coordination des tests de sécurité |
| **Avantages** | Réduit le goulet d'étranglement sur le Responsable de la sécurité de l'information ; développe la sensibilisation à la sécurité dans toute l'organisation ; crée des défenseurs de la sécurité intégrés dans les équipes de projet |

Le Responsable de la sécurité de l'information doit coordonner le programme Champion de la sécurité, y compris les critères de sélection, le contenu de la formation et le soutien continu.

---

## Intégration de l'AIPD

Lorsqu'un projet implique le traitement de données personnelles, un dépistage d'Analyse d'impact relative à la protection des données (AIPD) doit être effectué lors de l'initiation du projet pour déterminer si une AIPD complète est requise.

### Dépistage AIPD

Un dépistage AIPD doit être effectué pour chaque projet traitant des données personnelles. Le dépistage doit évaluer si le traitement prévu est susceptible d'entraîner un risque élevé pour la personnalité ou les droits fondamentaux des individus, comme requis par l'art. 22 nFADP.

**Une AIPD est obligatoire lorsque le projet implique l'un des éléments suivants :**

- Traitement étendu de données personnelles sensibles (données de santé, données biométriques, opinions politiques, croyances religieuses, casiers judiciaires ou mesures d'aide sociale selon l'art. 5 nFADP).
- Surveillance systématique et étendue de personnes (y compris le profilage selon l'art. 5 lit. f nFADP).
- Déploiement de nouvelles technologies lorsque l'impact sur la vie privée est incertain.
- Prise de décision automatisée à grande échelle avec des effets significatifs sur les personnes.
- Combinaison ou croisement de jeux de données provenant de sources différentes de manière que les personnes n'auraient pas raisonnablement attendu.

### Calendrier de l'AIPD

- **Dépistage** : Effectué lors de l'initiation du projet (avant le jalon de la phase de planification).
- **AIPD complète** (si requise) : Effectuée lors de la phase de planification, avant le jalon de la phase d'exécution.
- **Mise à jour de l'AIPD** : Requise lorsque le périmètre du projet, le traitement des données ou la technologie change de manière significative lors de l'exécution.

### Approbation de l'AIPD

L'AIPD complétée doit être révisée par le Délégué à la protection des données (ou le RSSI si aucun DPD n'est désigné) et approuvée avant que le projet passe à l'exécution. Lorsque l'AIPD identifie des risques résiduels élevés ne pouvant être atténués, l'organisation doit consulter le Préposé fédéral à la protection des données et à la transparence (PFPDT) avant de procéder, comme requis par l'art. 23 nFADP.

---

## Intégration dans les projets agiles et itératifs

Pour les projets utilisant les méthodes agiles, Scrum ou d'autres méthodologies itératives, la sécurité doit être intégrée dans le processus itératif plutôt que différée à la fin.

### Sécurité dans le développement itératif

| Activité agile | Intégration de la sécurité |
|---------------|---------------------------|
| **Refinement du backlog** | Récits de sécurité et critères d'acceptation de sécurité ajoutés aux user stories impliquant des données sensibles, l'authentification, l'autorisation ou les interfaces externes |
| **Planification du sprint** | Tâches de sécurité estimées et incluses dans la capacité du sprint ; récits de sécurité priorisés aux côtés des fonctionnalités métier |
| **Exécution du sprint** | Tests de sécurité automatisés (SAST, analyse des dépendances) intégrés dans le pipeline CI/CD ; résultats de sécurité traités comme des défauts et suivis dans le backlog du sprint |
| **Revue de sprint** | Statut de sécurité rapporté aux côtés de l'avancement des fonctionnalités ; dette de sécurité suivie et priorisée |
| **Planification des versions** | Exigences de tests de sécurité (tests d'intrusion, analyse des vulnérabilités) planifiées avant la mise en production conformément aux exigences de classification |

### Points de contrôle de sécurité pour les projets itératifs

Plutôt que des jalons de phase uniques, les projets itératifs doivent mettre en œuvre des points de contrôle de sécurité aux moments suivants :

- **Initiation du projet** : Classification de sécurité, dépistage AIPD et modèle de menaces initial (identique aux projets traditionnels).
- **Sprint d'architecture / Sprint 0** : Revue de l'architecture de sécurité ; référence des exigences de sécurité établie.
- **Chaque candidat à la version** : Résultats des analyses de sécurité automatisées révisés ; tests de sécurité manuels pour les versions destinées à la production.
- **Version de production** : Tests de sécurité complets conformément aux exigences de classification ; documentation de transfert de sécurité mise à jour.
- **Clôture du projet** : Enseignements tirés finaux ; risques résiduels transférés aux opérations.

---

## Sécurité dans les projets d'approvisionnement

Les projets impliquant l'approvisionnement de systèmes informatiques, de logiciels ou de services doivent inclure des exigences de sécurité de l'information dans le processus d'approvisionnement.

### Exigences de sécurité pour l'approvisionnement

- **Évaluation de la sécurité des fournisseurs** : Les fournisseurs doivent être évalués par rapport aux exigences de sécurité des fournisseurs de l'organisation (selon la Politique de sécurité des relations avec les fournisseurs) avant l'attribution du contrat.
- **Exigences de sécurité dans les contrats** : Les contrats doivent inclure des exigences de sécurité de l'information, notamment les obligations de protection des données, les exigences de notification des incidents, les droits d'audit et les contrôles des sous-traitants.
- **Critères d'acceptation de la sécurité** : Les critères d'acceptation de l'approvisionnement doivent inclure la validation de la sécurité (p. ex., analyse de vulnérabilité du système livré, revue de la configuration de sécurité, vérification du contrôle d'accès).
- **Accords de traitement des données** : Lorsque le fournisseur traite des données personnelles pour le compte de l'organisation, un accord de traitement des données conforme à l'art. 9 nFADP (et à l'art. 28 RGPD le cas échéant) doit être conclu avant le début du traitement des données.

---

## Définitions

| Terme | Définition |
|-------|-----------|
| **Projet** | Une entreprise temporaire avec des dates de début et de fin définies, entreprise pour créer un produit, un service ou un résultat unique impliquant des actifs informationnels ou des systèmes d'information |
| **Jalon de phase** | Un point de révision formel entre les phases du projet où les critères de sécurité doivent être satisfaits avant que le projet ne progresse |
| **Classification de sécurité** | La catégorisation d'un projet comme risque élevé, moyen ou faible en fonction des facteurs d'impact sur la sécurité de l'information |
| **Registre des exigences de sécurité** | Une liste documentée des exigences de sécurité pour un projet, suivie jusqu'à la mise en œuvre et aux tests |
| **AIPD (Analyse d'impact relative à la protection des données)** | Une évaluation structurée de l'impact du traitement prévu des données sur la protection des données personnelles, requise par l'art. 22 nFADP lorsque le traitement est susceptible d'entraîner un risque élevé |
| **Modèle de menaces** | Une analyse structurée des menaces potentielles pesant sur un système ou une application, identifiant les vecteurs d'attaque, les acteurs de la menace et les contre-mesures requises |
| **Risque résiduel** | Le risque subsistant après la mise en œuvre des contrôles de sécurité, qui doit être formellement accepté par l'autorité appropriée |
| **Transfert de sécurité** | Le transfert formel de la documentation de sécurité, des responsabilités et des procédures opérationnelles de l'équipe du projet vers l'équipe opérationnelle à la clôture du projet |
| **Champion de la sécurité** | Un membre de l'équipe formé intégré dans une équipe de projet qui fait office de référent sécurité, aidant à identifier les exigences de sécurité et prônant les meilleures pratiques de sécurité |

---

## Rôles et responsabilités

| Rôle | Responsabilités en matière de sécurité de l'information dans la gestion de projet |
|------|-----------------------------------------------------------------------------------|
| **Direction générale** | Approuver cette politique ; assurer les ressources organisationnelles pour la sécurité des projets ; accepter les risques résiduels pour les projets critiques ; examiner l'état de sécurité des projets à risque élevé lors des révisions de direction |
| **RSSI** | Approuver les classifications à risque élevé et l'acceptation des risques résiduels ; stopper ou retarder les projets présentant un risque de sécurité inacceptable ; surveiller les indicateurs de sécurité des projets ; approuver les exceptions aux exigences de sécurité |
| **Responsable de la sécurité de l'information** | Soutenir les équipes de projet dans l'évaluation des risques de sécurité et l'identification des exigences ; approuver les classifications à risque moyen ; examiner l'adéquation des tests de sécurité ; maintenir les modèles et listes de contrôle de sécurité |
| **Chef de projet** | Classifier le risque de sécurité du projet (avec le soutien de la sécurité info.) ; planifier et budgéter les activités de sécurité ; exécuter les activités de sécurité à chaque jalon de phase ; maintenir le registre des risques de sécurité du projet ; préparer la documentation de transfert de sécurité |
| **Propriétaire métier** | Définir les exigences de sécurité métier ; participer à l'évaluation des risques de sécurité ; accepter les risques résiduels pour les projets à risque moyen/faible ; approuver les exigences de sécurité dans le périmètre du projet |
| **Responsable technique** | Concevoir les contrôles de sécurité dans les solutions ; mettre en œuvre les exigences de sécurité ; soutenir la modélisation des menaces ; traiter les résultats des tests de sécurité |
| **Délégué à la protection des données** | Réviser et approuver les AIPD ; conseiller sur les exigences de protection des données pour les projets ; assurer la liaison avec le PFPDT si requis par l'art. 23 nFADP |

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence |
|----|--------|-------------|-----------|
| 1 | **Enregistrements de classification des projets** montrant la détermination et l'approbation de la classification du risque de sécurité pour chaque projet | Chef de projet | *Par initiation de projet ; archivé à la clôture du projet* |
| 2 | **Registres des exigences de sécurité** (ou entrées du registre des risques pour les risques faibles) documentant les exigences de sécurité identifiées et le statut de mise en œuvre | Chef de projet | *Par projet ; mis à jour tout au long du cycle de vie* |
| 3 | **Enregistrements d'approbation des jalons de phase** avec vérification des critères de sécurité et signature | Chef de projet | *Par jalon de phase ; archivé à la clôture du projet* |
| 4 | **Rapports de tests de sécurité** (tests d'intrusion, analyses de vulnérabilités, revues de code) conformément aux exigences de classification | Resp. sécurité info. | *Par projet ; rapport final dans les 7 jours suivant le déploiement* |
| 5 | **Enregistrements de remédiation des résultats de sécurité** suivant les résultats jusqu'à leur clôture ou acceptation du risque | Chef de projet | *Par projet ; mis à jour jusqu'à la clôture* |
| 6 | **Dossiers de transfert de sécurité** acceptés par les équipes opérationnelles | Chef de projet | *Par clôture de projet* |
| 7 | **Enregistrements d'acceptation du risque résiduel** avec approbations appropriées selon la classification | RSSI / Propriétaire métier | *Par projet où des risques résiduels existent* |
| 8 | **Enregistrements de dépistage AIPD** (et AIPD complète le cas échéant) pour les projets traitant des données personnelles | DPD / RSSI | *Par projet impliquant des données personnelles* |
| 9 | **Documentation des enseignements tirés** pour les projets à risque moyen et élevé | Chef de projet | *Par clôture de projet* |
| 10 | **Registre des exceptions de sécurité** avec approbations, contrôles compensatoires et limites de temps | RSSI | *Par exception ; révisé trimestriellement* |
| 11 | **Tableau de bord des indicateurs de sécurité des projets** montrant la distribution des classifications, la completion des tests et les tendances des résultats | RSSI | *Mensuel ; rapporté trimestriellement à la Direction générale* |
| 12 | **Enregistrements de formation** pour les chefs de projet sur l'intégration des exigences de sécurité | RH / Resp. sécurité info. | *Annuel ; achèvement suivi* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les audits de classification des projets, les révisions de conformité aux jalons de phase, la vérification de la completion des tests de sécurité, les révisions de la documentation de transfert, les audits internes et externes, et les retours d'information au propriétaire de la politique.

Les indicateurs suivants doivent être suivis et rapportés au RSSI trimestriellement :

| Indicateur | Cible | Seuil d'alerte |
|------------|-------|----------------|
| Projets classifiés dans les 5 jours ouvrables suivant l'initiation | 100 % | < 80 % |
| Projets à risque élevé/moyen avec registre d'exigences de sécurité complété | 100 % | < 90 % |
| Tests de sécurité complétés avant le déploiement | 100 % | < 90 % |
| Constatations de sécurité critiques remédiées avant le déploiement | 100 % | < 100 % (toute constatation critique déployée = alerte) |
| Documentation de transfert de sécurité acceptée avant la clôture du projet | 100 % | < 80 % |
| Dépistage AIPD complété pour les projets traitant des données personnelles | 100 % | < 90 % |
| Enseignements tirés documentés pour les projets à risque élevé/moyen | 100 % | < 80 % |

### Tableau de bord des indicateurs

Le RSSI doit maintenir un tableau de bord des indicateurs de sécurité des projets fournissant une visibilité immédiate de la santé du programme. Le tableau de bord doit inclure :

- **Score global de conformité du programme** — agrégat des sept indicateurs ci-dessus, calculé comme la moyenne pondérée de l'atteinte des cibles.
- **Barres de conformité par indicateur** — chaque indicateur affiché avec le pourcentage actuel et l'indicateur d'état (vert ≥ cible, ambre ≥ seuil d'alerte, rouge < seuil d'alerte).
- **Projets actifs par classification** — nombre de projets actifs à risque élevé, moyen et faible.
- **Éléments à traiter** — projets avec des activités de sécurité en retard ou des indicateurs dépassant les seuils ambre/rouge.

Le tableau de bord doit être révisé lors de la revue mensuelle du RSSI et inclus dans le rapport trimestriel à la Direction générale pour fournir une visibilité claire de l'efficacité du programme de sécurité des projets.

**Exigences de rapportage** :
- **Tableau de bord mensuel du RSSI** : Projets par classification et statut de sécurité (en bonne voie / à risque / en retard) ; résultats de sécurité ouverts par gravité et ancienneté ; exceptions de sécurité accordées.
- **Rapport trimestriel à la Direction générale** : Nombre total de projets et de projets à risque élevé ; résultats de sécurité critiques et statut de remédiation ; taux de completion des AIPD ; incidents de sécurité significatifs affectant les projets.
- **Révision annuelle de la direction** : Efficacité complète du programme de sécurité des projets ; tendances des indicateurs ; résultats significatifs ; recommandations d'amélioration.

Les indicateurs dépassant les seuils d'alerte doivent être escaladés au RSSI pour une attention immédiate et rapportés lors de la prochaine Révision de direction.

## Exceptions

Toute exception à cette politique doit être approuvée et consignée par le RSSI à l'avance, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions aux exigences de tests de sécurité ou aux jalons de phase pour les projets à risque élevé nécessitent une approbation conjointe du RSSI et de la Direction générale. Les exceptions ne doivent pas dépasser 90 jours calendaires sans réévaluation et réapprobation.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement. Les projets déployés sans les tests de sécurité ou la classification requis peuvent être soumis à une suspension immédiate jusqu'à ce que les exigences de sécurité soient satisfaites. La non-conformité doit être signalée au RSSI et enregistrée dans le registre des non-conformités du SMSI.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements de méthodologie de gestion de projet, les résultats des audits, les changements réglementaires (y compris les amendements nFADP), les incidents de sécurité liés aux projets, les tendances des exceptions, les enseignements tirés des révisions de sécurité des projets et l'évolution du paysage des menaces. Les non-conformités relatives à cette politique doivent être enregistrées et gérées via le processus d'actions correctives SMSI (clause 10.2) avec analyse des causes profondes et remédiation suivie.

---

# Périmètre de la norme ISO 27001 couvert

Politique de sécurité de l'information dans la gestion de projet — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.3 Rôles, responsabilités et autorités | **5.8 Sécurité de l'information dans la gestion de projet** |
| Clause 6.1 Actions face aux risques et opportunités | 5.7 Renseignement sur les menaces |
| Clause 6.2 Objectifs de sécurité de l'information et planification | 5.9 Inventaire des informations et des actifs associés |
| Clause 7.4 Communication | 5.12 Classification de l'information |
| Clause 8.1 Planification et contrôle opérationnels | 5.19 Sécurité de l'information dans les relations avec les fournisseurs |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 5.34 Protection de la vie privée et des DCP |
| Clause 10.2 Non-conformité et actions correctives | 8.25 Cycle de développement sécurisé |
| | 8.26 Exigences de sécurité des applications |
| | 8.29 Tests de sécurité dans le développement et l'acceptation |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nFADP suisse (LPD révisée) | Art. 7 — Protection des données dès la conception et par défaut ; art. 8 — Mesures techniques et organisationnelles ; art. 22 — AIPD pour le traitement à risque élevé ; art. 23 — Consultation du PFPDT |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales pour la sécurité des données |
| RGPD UE (le cas échéant) | Art. 25 — Protection des données dès la conception et par défaut ; art. 32 — Sécurité du traitement ; art. 35 — Analyse d'impact relative à la protection des données |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.8 — Sécurité de l'information dans la gestion de projet |
| ISO/IEC 27002:2022 | Section 5.8 — Conseils d'implémentation pour la sécurité de l'information dans la gestion de projet |
| ISO 21500:2021 | Gestion de projets, programmes et portefeuilles — Contexte et concepts |
| NIST SP 800-53 Rév. 5 | SA-3 (Cycle de développement des systèmes) — Intégration de la sécurité tout au long du cycle de vie ; PL-2 (Plans de sécurité et de protection de la vie privée des systèmes) — Planification de la sécurité des systèmes |
| NIST CSF 2.0 | GV.RR — Rôles, responsabilités et autorités ; ID.RA — Évaluation des risques ; PR.IP — Processus et procédures de protection de l'information |
| CIS Controls v8 | Contrôle 16 (Sécurité des logiciels applicatifs) — Mesures de protection du cycle de développement sécurisé ; Fonction de gouvernance — Politiques et procédures de protection des actifs |

---

<!-- QA_VERIFIED: 2026-03-29 -->
