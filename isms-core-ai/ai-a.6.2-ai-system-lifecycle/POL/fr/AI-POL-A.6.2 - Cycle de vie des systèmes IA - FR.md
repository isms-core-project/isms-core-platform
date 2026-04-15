<!-- ISMS-CORE:POLICY:AI-POL-A.6.2-FR:ai:POL:a.6.2 -->
**AI-POL-A.6.2 — Cycle de vie des systèmes IA**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cycle de vie des systèmes IA |
| **Type de document** | Politique |
| **ID du document** | AI-POL-A.6.2 |
| **Auteur du document** | Responsable de la Gouvernance IA (RGIA) / Directeur Technique (DT) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date à définir] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit AIMS** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|--------------|
| 1.0 | [Date à définir] | RGIA / DT | Politique initiale pour la première certification ISO/IEC 42001:2023 |

**Cycle de révision** : Annuel (ou en cas de changement significatif des pratiques de développement et d'exploitation IA)
**Date de prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la Gouvernance IA (RGIA)
- Secondaire : Directeur Technique (DT) / Responsable IA Engineering
- Conformité : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Autorité finale : Direction générale

**Documents connexes** :

- AI-POL-00 (Cadre d'applicabilité réglementaire IA)
- AI-POL-A.6.1 (Gouvernance du développement IA — objectifs et processus pré-cycle de vie)
- AI-POL-A.7.2-6 (Données pour les systèmes IA)
- AI-POL-A.5.2-5 (Évaluation d'impact des systèmes IA — l'ÉISIA doit précéder le déploiement)
- AI-IMP-A.6.2-UG (Cycle de vie des systèmes IA — Guide utilisateur)
- AI-IMP-A.6.2-TG (Cycle de vie des systèmes IA — Guide technique)
- ISO/IEC 42001:2023 Contrôles A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8
- ISO/IEC 42001:2023 Annexe B.6.2 (Orientations de mise en œuvre — Cycle de vie du système IA)

---

## Synthèse exécutive

La présente politique établit les exigences de l'[organisation] pour le cycle de vie des systèmes IA — couvrant la spécification, la documentation de conception et développement, la vérification et validation, le déploiement, l'exploitation et la surveillance, la documentation technique et la journalisation des événements — conformément aux Contrôles A.6.2.2 à A.6.2.8 d'ISO/IEC 42001:2023.

**Périmètre** : Tous les systèmes IA dans le périmètre AIMS à toutes les étapes du cycle de vie, de la spécification à la mise hors service. Les contrôles s'appliquent aux fournisseurs IA (en priorité) et aux déployeurs IA où ils exercent une influence significative sur la gestion du cycle de vie.

**Objectif** : Définir CE QUI doit être documenté et contrôlé à chaque étape du cycle de vie, QUI est responsable et QUAND les contrôles s'appliquent. Les détails de mise en œuvre sont dans AI-IMP-A.6.2-UG et AI-IMP-A.6.2-TG.

**Justification combinée des contrôles** : A.6.2.2 à A.6.2.8 correspondent directement aux étapes du cycle de vie du système IA. Chaque contrôle régit une étape distincte : spécification → documentation conception/développement → vérification/validation → déploiement → exploitation/surveillance → documentation technique → journalisation des événements. Ces sept contrôles sont interdépendants — chaque étape produit des livrables dont dépend la suivante.

---

## Périmètre et applicabilité

### Énoncés des contrôles ISO/IEC 42001:2023

**Contrôle A.6.2.2 — Exigences et spécification du système IA**
L'organisation doit spécifier et documenter les exigences pour les nouveaux systèmes IA ou les améliorations significatives des systèmes existants.

**Contrôle A.6.2.3 — Documentation de la conception et du développement du système IA**
L'organisation doit documenter la conception et le développement du système IA sur la base des objectifs organisationnels, des exigences documentées et des critères de spécification.

**Contrôle A.6.2.4 — Vérification et validation du système IA**
L'organisation doit définir et documenter les mesures de vérification et validation pour le système IA et spécifier les critères de leur utilisation.

**Contrôle A.6.2.5 — Déploiement du système IA**
L'organisation doit documenter un plan de déploiement et s'assurer que les exigences appropriées sont satisfaites avant le déploiement.

**Contrôle A.6.2.6 — Exploitation et surveillance du système IA**
L'organisation doit définir et documenter les éléments nécessaires au fonctionnement continu du système IA. Au minimum, cela doit inclure la surveillance du système et des performances, les réparations, les mises à jour et le support.

**Contrôle A.6.2.7 — Documentation technique du système IA**
L'organisation doit déterminer quelle documentation technique du système IA est nécessaire pour chaque catégorie pertinente de parties prenantes, telles que les utilisateurs, les partenaires, les autorités de supervision, et fournir la documentation technique sous la forme appropriée.

**Contrôle A.6.2.8 — Enregistrement des journaux d'événements du système IA**
L'organisation doit déterminer à quelles phases du cycle de vie du système IA la tenue des journaux d'événements doit être activée, mais au minimum lorsque le système IA est en cours d'utilisation.

### Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per AI-POL-00) :

- **Règlement IA de l'UE (Règlement 2024/1689)** : Article 11 (documentation technique), Article 12 (tenue de registres et journalisation), Article 13 (transparence et fourniture d'informations), Article 14 (supervision humaine), Article 15 (précision, robustesse, cybersécurité), Article 17 (SMQ — toutes les étapes du cycle de vie)

**Niveau 2 : Conditionnel** (per AI-POL-00) :

- **ISO/IEC 42001:2023** : Contrôles A.6.2.2–A.6.2.8 — applicable si la certification AIMS est dans le périmètre ou contractuellement requise

---

## Déclarations de politique : Exigences et spécification (A.6.2.2)

### Exigence de spécification du système IA

L'[organisation] DOIT spécifier et documenter les exigences pour chaque nouveau système IA et pour toute amélioration significative des systèmes existants, avant le début du développement ou de l'amélioration.

### Exigences relatives au document de spécification

La spécification du système IA doit documenter :

| Élément | Contenu requis |
|---------|---------------|
| **Finalité prévue** | Déclaration claire de ce que le système IA est conçu pour faire, pour qui et dans quel contexte |
| **Exigences fonctionnelles** | Ce que le système doit faire (entrées, sorties, types de décisions, attentes de performance) |
| **Exigences non fonctionnelles** | Fiabilité, disponibilité, temps de réponse, scalabilité, sécurité |
| **Exigences d'IA responsable** | Métriques et seuils d'équité ; niveau d'explicabilité ; mécanismes de supervision humaine ; dérivés de l'ÉISIA et des objectifs de AI-POL-A.6.1 |
| **Conditions opérationnelles** | Conditions dans lesquelles le système IA est censé fonctionner correctement (hypothèses de distribution des données, conditions environnementales) |
| **Usages hors périmètre** | Usages explicitement documentés pour lesquels le système N'est PAS conçu ou validé |
| **Parties prenantes** | Parties internes et externes qui interagiront avec le système ou seront affectées par lui |
| **Contraintes réglementaires** | Classification de risque Règlement IA UE ; déclencheurs RGPD Article 22 ; autres obligations applicables |
| **Exigences d'intégration** | Comment le système IA s'intègre aux systèmes et processus existants |

**Amélioration significative** est définie comme toute modification qui : modifie de manière significative les sorties du système IA ; introduit le système à une nouvelle population ; modifie le contexte opérationnel ou la finalité prévue ; ou modifie l'architecture du modèle, les données d'entraînement ou les hyperparamètres clés.

---

## Déclarations de politique : Documentation de conception et développement (A.6.2.3)

### Exigence de documentation de conception et développement

L'[organisation] DOIT documenter la conception et le développement du système IA, en s'assurant que la documentation est traçable à la spécification et aux objectifs d'IA responsable.

### Documentation requise

| Documentation | Contenu |
|--------------|---------|
| **Documentation de l'architecture** | Architecture système de haut niveau ; diagramme des composants ; flux de données ; points d'intégration |
| **Documentation du modèle** | Justification du choix de l'algorithme ; architecture du modèle ; approche d'entraînement ; choix d'hyperparamètres |
| **Documentation des données d'entraînement** | Jeux de données utilisés ; étapes de pré-traitement ; méthodologie de division des données ; lien vers les enregistrements de données A.7 |
| **Journal des décisions de conception** | Décisions de conception clés avec justification ; compromis effectués ; alternatives considérées |
| **Décisions de conception IA responsable** | Comment les exigences d'équité, de transparence et de sécurité ont été adressées dans la conception |
| **Historique des versions** | Toutes les versions du modèle avec modifications documentées ; informations de reproductibilité |

La documentation doit être versionnée et liée à la version du système IA qu'elle décrit.

---

## Déclarations de politique : Vérification et validation (A.6.2.4)

### Exigence de V&V

L'[organisation] DOIT définir et documenter les mesures de vérification et validation pour chaque système IA avant déploiement, et spécifier les critères devant être satisfaits pour l'autorisation de déploiement.

### Vérification

La vérification confirme que le système IA a été construit correctement selon les spécifications :

- Tests fonctionnels par rapport aux exigences de la spécification
- Tests de performance (précision, précision/rappel ou métriques spécifiques à la tâche) par rapport aux seuils définis
- Tests de sécurité — tests d'entrées adversariales, évaluation de la robustesse du modèle
- Tests d'intégration dans l'environnement de staging

### Validation

La validation confirme que le système IA résout le bon problème et est adapté à son usage prévu :

- Validation IA responsable — métriques d'équité évaluées par rapport aux seuils approuvés ; explicabilité validée pour le public cible
- Validation de l'usage prévu — tests avec des conditions réelles et des cas limites
- Tests hors distribution — comportement documenté lorsque les entrées sortent de la distribution d'entraînement
- Validation de la supervision humaine — les mécanismes de dérogation fonctionnent correctement ; seuils d'alerte calibrés

### Critères de déploiement

Chaque système IA doit avoir des critères documentés devant être satisfaits avant l'autorisation de déploiement. Le RGIA doit valider la complétion de la V&V par rapport aux critères. Un système ne satisfaisant pas aux critères de V&V ne doit pas être déployé.

---

## Déclarations de politique : Déploiement (A.6.2.5)

### Exigence de plan de déploiement

L'[organisation] DOIT documenter un plan de déploiement pour chaque système IA et s'assurer que toutes les exigences pré-déploiement sont satisfaites avant le déploiement opérationnel.

### Contenu du plan de déploiement

| Élément | Contenu requis |
|---------|---------------|
| **Périmètre du déploiement** | Quels environnements, populations d'utilisateurs et cas d'usage sont couverts dans ce déploiement |
| **Liste de contrôle pré-déploiement** | Toutes les exigences devant être confirmées avant déploiement (ÉISIA approuvée, V&V réussie, documentation technique prête, supervision humaine mise en œuvre, journalisation activée) |
| **Approche de déploiement** | Déploiement progressif / mode fantôme / déploiement complet — avec justification |
| **Procédure de retour en arrière** | Comment revenir à l'état précédent en cas de problèmes inattendus après déploiement |
| **Activation du monitoring** | Comment le monitoring opérationnel (A.6.2.6) est activé au déploiement |
| **Communication aux parties prenantes** | Qui doit être informé du déploiement et comment |
| **Autorisation de déploiement** | Autorisant nommé (le RGIA doit approuver) et date d'autorisation |

**Gate de déploiement** : Aucun système IA ne peut être déployé sans l'approbation documentée du RGIA confirmant que toutes les exigences pré-déploiement sont satisfaites, y compris une ÉISIA à jour.

---

## Déclarations de politique : Exploitation et surveillance (A.6.2.6)

### Exigence de surveillance opérationnelle

L'[organisation] DOIT définir et documenter les éléments nécessaires au fonctionnement continu et à la surveillance de chaque système IA dans le périmètre.

### Éléments de surveillance obligatoires

**Surveillance des performances** :

- Indicateurs clés de performance (KPI) définis à l'étape de spécification (A.6.2.2)
- Fréquence de surveillance adaptée au cas d'usage (continue / quotidienne / hebdomadaire)
- Seuils de dégradation des performances — lorsque les performances passent sous le seuil, une alerte est déclenchée
- Détection de dérive du modèle — surveillance statistique de la distribution des données d'entrée et de la distribution des sorties

**Surveillance IA responsable** :

- Surveillance de l'équité — métriques d'équité mesurées en production selon un calendrier défini
- Détection de biais — surveillance de l'émergence de biais en production absent lors de la V&V
- Efficacité de la supervision humaine — les mécanismes de dérogation sont-ils utilisés de manière appropriée ?
- Conformité au périmètre — le système IA est-il utilisé uniquement pour les finalités prévues documentées ?

**Surveillance opérationnelle** :

- Disponibilité et temps de fonctionnement du système
- Temps de réponse et débit
- Taux d'erreur et modes de défaillance
- Santé de l'infrastructure (liée à A.4.5)

**Alertes d'incidents** :

- Conditions d'alerte définies pour chaque dimension de surveillance
- Chemin d'escalade de l'alerte automatisée au Propriétaire du système IA puis au Responsable des risques IA
- Intégration au processus de réponse aux incidents IA (AI-POL-A.8.2-5)

### Documentation de la surveillance

Le plan de surveillance pour chaque système IA doit être documenté avant déploiement, couvrant tous les éléments de surveillance obligatoires avec :

- Ce qui est surveillé
- Comment c'est surveillé (outil, méthode)
- Fréquence
- Seuils d'alerte
- Chemin d'escalade en cas de dépassement de seuil

---

## Déclarations de politique : Documentation technique (A.6.2.7)

### Exigence de documentation technique

L'[organisation] DOIT déterminer quelle documentation technique est nécessaire pour chaque catégorie pertinente de parties prenantes et la fournir sous la forme appropriée.

### Catégories de parties prenantes et exigences de documentation

| Partie prenante | Documentation requise |
|----------------|----------------------|
| **Opérateurs / utilisateurs internes** | Guide utilisateur ; spécification de l'usage prévu ; limites ; procédures opérationnelles ; mécanismes de dérogation |
| **Propriétaire système IA / Gouvernance** | Spécification technique complète ; fiche modèle ; rapport de V&V ; synthèse ÉISIA ; plan de surveillance |
| **IT / Infrastructure** | Architecture système ; documentation d'intégration ; exigences d'infrastructure ; runbook de déploiement |
| **Autorités réglementaires** | Documentation technique Règlement IA UE (Article 11 pour l'IA à haut risque) ; synthèse ÉISIA ; documentation d'évaluation de conformité |
| **Clients / partenaires** | Description des capacités ; limites ; avis de transparence (A.8.2) ; mécanisme de signalement des incidents (A.8.3) |
| **Auditeurs (internes/externes)** | Ensemble complet de documentation ; preuves de V&V ; ÉISIA ; référence DDA |

La documentation technique doit être versionnée, liée à la version du système IA qu'elle décrit et révisée à chaque modification significative.

---

## Déclarations de politique : Journalisation des événements (A.6.2.8)

### Exigence de journalisation des événements

L'[organisation] DOIT déterminer à quelles phases du cycle de vie du système IA la journalisation des événements doit être activée. Au minimum, la journalisation doit être active lorsque le système IA est en cours d'utilisation opérationnelle.

### Phases de journalisation obligatoires

| Phase du cycle de vie | Exigence de journalisation |
|----------------------|--------------------------|
| **Utilisation opérationnelle** | OBLIGATOIRE — toutes les interactions, entrées, sorties et décisions du système IA doivent être journalisées |
| **Validation et tests** | Requis — entrées de test, sorties et résultats d'évaluation journalisés pour la traçabilité |
| **Déploiement** | Requis — événement de déploiement, version, autorisant, horodatage |
| **Alertes de surveillance** | Requis — tous les dépassements de seuil et événements d'alerte |
| **Incidents** | Requis — tous les événements d'incident IA pour la revue post-incident |
| **Développement** | Bonne pratique — exécutions d'entraînement du modèle, ensembles d'hyperparamètres, métriques d'évaluation |

### Exigences relatives au contenu des journaux

Pour les journaux opérationnels du système IA, chaque enregistrement d'événement doit inclure au minimum :

- Horodatage (UTC)
- Identifiant et version du système IA
- Résumé des entrées (ou hachage des entrées lorsque la journalisation des entrées complètes est interdite par les obligations de protection des données)
- Sortie ou décision produite
- Toute dérogation humaine appliquée
- Identifiant utilisateur ou de session (le cas échéant et dans les limites permises)

### Conservation des journaux

Les journaux d'événements des systèmes IA doivent être conservés pendant :

- La durée de la vie opérationnelle du système IA, PLUS
- 3 ans minimum après la mise hors service (à prolonger si le Règlement IA UE ou les réglementations sectorielles exigent des durées plus longues)

### Protection des journaux

Les journaux d'événements des systèmes IA constituent des preuves d'audit. Ils doivent être :

- Protégés contre la modification ou la suppression (immuables ou en ajout uniquement dans la mesure du possible)
- Soumis à contrôle d'accès (lecture seule pour les auditeurs ; accès en écriture restreint pour la gestion des journaux)
- Sauvegardés conformément aux exigences de sauvegarde ISMS

---

## Déclarations de politique : Mise hors service

### Exigence de mise hors service

L'[organisation] DOIT gérer la fin de vie planifiée des systèmes IA de manière contrôlée, préservant les preuves, protégeant les personnes concernées et garantissant qu'aucun préjudice résiduel ne découle des systèmes discontinués.

### Conditions déclenchant la mise hors service

Un processus de mise hors service du système IA doit être initié lorsque :

- Le système IA est retiré définitivement de l'utilisation opérationnelle
- Un système de remplacement est déployé et le système existant mis à la retraite
- L'ÉISIA du système IA identifie des risques qui ne peuvent être adéquatement atténués
- Le cas d'usage prévu est abandonné
- Une modification significative nécessiterait une réévaluation complète que le système ne peut satisfaire

### Processus de mise hors service

Le Propriétaire du système IA doit exécuter un plan de mise hors service documenté, approuvé par le RGIA, couvrant :

| Étape | Exigence |
|-------|---------|
| **Notification des utilisateurs** | Notifier tous les utilisateurs et parties concernées de la date de mise hors service prévue avec un préavis suffisant (minimum 30 jours pour les systèmes opérationnels ; selon les obligations contractuelles pour les systèmes côté client) |
| **Disposition des données** | Définir le sort de toutes les données d'entraînement, opérationnelles et de sortie : suppression, archivage ou transfert — documenté conformément aux exigences du cycle de vie des données RGPD |
| **Élimination du modèle** | Confirmer la suppression des poids du modèle et artefacts associés de tous les environnements (production, staging, sauvegardes), ou documenter la justification de conservation |
| **Révocation des accès** | Révoquer tous les accès utilisateurs et API au système avant ou à la mise hors service |
| **Conservation des journaux** | Conserver les journaux d'événements pendant au moins 3 ans après la mise hors service, ou selon la réglementation applicable |
| **Clôture de l'ÉISIA** | Clore l'ÉISIA avec un enregistrement de mise hors service, notant la méthode d'élimination et confirmant la résolution des risques en suspens |
| **Registre Règlement IA UE** | Lorsque le système était enregistré dans la base de données Règlement IA UE, mettre à jour le statut d'enregistrement à « mis hors service » |
| **Notification des tiers** | Notifier les tiers concernés (fournisseurs de composants IA, sous-traitants de données) de la mise hors service et obtenir la confirmation de la suppression des données si requis |

### Exigences de preuves pour la mise hors service

Le RGIA doit conserver un **Dossier de mise hors service** par système comprenant : identité du système, date de mise hors service, méthode d'élimination des données et artefacts du modèle, confirmation de notification des utilisateurs et clôture de l'ÉISIA.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RGIA** | Approuver le déploiement (toutes les étapes) ; posséder la politique du cycle de vie ; réviser les rapports de surveillance ; approuver la documentation technique pour les audiences réglementaires ; approuver les plans de mise hors service |
| **DT / Responsable IA Engineering** | Posséder la spécification A.6.2.2, la documentation A.6.2.3, les processus V&V A.6.2.4 ; s'assurer que les pratiques d'engineering satisfont à la politique |
| **Propriétaire du système IA** | Maintenir toute la documentation du cycle de vie pour les systèmes dont il est responsable ; posséder le plan de surveillance ; répondre aux alertes de surveillance |
| **RSSI** | Réviser les dimensions sécurité de la V&V (A.6.2.4), de la surveillance (A.6.2.6) et de la journalisation (A.6.2.8) |
| **Responsable des risques IA** | Accepter les risques résiduels identifiés lors de la V&V ; approuver l'acceptation des risques au déploiement |

---

## Exigences de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Spécification du système IA | Exigences documentées par version du système IA | Durée du système + 3 ans |
| Documentation de conception et développement | Architecture, modèle, entraînement, journal de décisions | Durée du système + 3 ans |
| Dossiers de V&V | Plans de test, résultats de test, passage/échec aux critères de déploiement | Durée du système + 3 ans |
| Plan et autorisation de déploiement | Plan de déploiement avec approbation du RGIA | Durée du système + 3 ans |
| Plan de surveillance | Plan de surveillance documenté avec seuils | Durée du système + 3 ans |
| Documentation technique | Documentation versionnée par catégorie de parties prenantes | Durée du système + 3 ans |
| Journaux d'événements | Journaux opérationnels du système IA | Durée du système + 3 ans après mise hors service |
| Dossiers de mise hors service | Méthode d'élimination, confirmation de suppression des données, clôture ÉISIA, notification des utilisateurs | 5 ans après mise hors service |

---

## Considérations pour l'audit

Les auditeurs vérifiant la conformité avec A.6.2.2–A.6.2.8 doivent s'attendre à trouver :

- Des documents de spécification pour tous les systèmes IA dans le périmètre, antérieurs au développement
- Une documentation de conception et développement traçable aux spécifications
- Des rapports de V&V avec critères de déploiement documentés et résultats de passage/échec
- Des dossiers d'autorisation de déploiement avec la validation du RGIA
- Des plans de surveillance actifs avec configurations d'alertes
- Une documentation technique disponible pour chaque catégorie de parties prenantes
- Une journalisation des événements active en utilisation opérationnelle, avec politique de conservation documentée
- Des dossiers de mise hors service pour les systèmes IA retirés, incluant la confirmation d'élimination des données/modèles et la clôture de l'ÉISIA

---

<!-- QA_VERIFIED: [2026-04-15] -->
