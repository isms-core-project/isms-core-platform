<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.4-FR:framework:POL:a.8.4 -->
**ISMS-POL-A.8.4 – Accès au code source**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Accès au code source |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.4 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur de la Technologie (DT) ou Directeur de l'ingénierie
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.4.1-UG/TG (Mise en œuvre du contrôle d'accès aux référentiels)
- ISMS-IMP-A.8.4.2-UG/TG (Configuration de la protection des branches)
- ISMS-IMP-A.8.4.3-UG/TG (Évaluation de l'accès au code source)
- ISO/IEC 27001:2022 Contrôle A.8.4
- ISMS-POL-A.8.25-26-29 (Cycle de vie du développement sécurisé)
- ISMS-POL-A.5.15-16-18 (Contrôle d'accès / Gestion des identités et des accès)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôle d'accès au code source afin de protéger la propriété intellectuelle et de maintenir des pratiques de développement logiciel sécurisées, conformément au Contrôle A.8.4 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les référentiels de code source (production, outils internes, infrastructure-as-code, contributions open source, archivés) ; tous les artefacts de développement (bibliothèques, scripts de build, code de test) ; toutes les plateformes de référentiels (GitHub, GitLab, Bitbucket, Azure DevOps, auto-hébergés) ; et l'ensemble du personnel, contractants et tiers ayant accès au code source.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles d'accès au code source. Cette politique établit QUELS contrôles d'accès sont requis et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans la suite ISMS-IMP-A.8.4.

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.4 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.4 — Accès au code source**

> *L'accès au code source, aux outils de développement et aux bibliothèques logicielles doit être géré de manière appropriée.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les contrôles d'accès au code source, protégeant la propriété intellectuelle et assurant un développement logiciel sécurisé par une gestion appropriée des accès aux référentiels de code source et aux artefacts de développement connexes.

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de contrôle d'accès au code source alignées sur la classification des données et les obligations réglementaires
- **Établit** le cadre de gouvernance pour la prise de décision et la responsabilisation en matière d'accès aux référentiels
- **Précise** les contrôles d'accès obligatoires pour les référentiels et les artefacts de développement
- **Identifie** les rôles et responsabilités organisationnels pour les contrôles d'accès au code source

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les détails techniques de mise en œuvre** (voir ISMS-IMP-A.8.4)
- **Définit pas les procédures de configuration spécifiques aux plateformes** (voir ISMS-IMP-A.8.4.1 et ISMS-IMP-A.8.4.2)
- **Fournit pas les méthodologies d'évaluation ou de collecte de preuves** (voir ISMS-IMP-A.8.4.3)
- **Sélectionne pas les plateformes de référentiels ou technologies** (sélection basée sur l'évaluation des risques)
- **Remplace pas l'évaluation des risques**
- **Établit pas les normes de codage sécurisé** (traitées par ISMS-POL-A.8.25-26-29)

**Structure documentaire** :

- **ISMS-POL-A.8.4** (CE DOCUMENT) : Exigences de politique (QUOI et QUI)
- **ISMS-IMP-A.8.4.1** : Procédures de mise en œuvre du contrôle d'accès aux référentiels (COMMENT)
- **ISMS-IMP-A.8.4.2** : Guide de configuration de la protection des branches (COMMENT)
- **ISMS-IMP-A.8.4.3** : Procédures d'évaluation de l'accès au code source (COMMENT)

## Périmètre

**Cette politique s'applique à** :

- Tous les référentiels de code source contenant du code d'application de production, des outils internes, de l'infrastructure-as-code, de la gestion de la configuration ou des artefacts de développement
- Toutes les plateformes de référentiels (plateformes Git hébergées dans le cloud, plateformes Git auto-hébergées, systèmes de contrôle de version alternatifs)
- Tous les artefacts de développement (code source, bibliothèques, scripts de build, code de test, documentation, définitions de conteneurs, pipelines CI/CD)
- Tout le personnel organisationnel ayant des besoins d'accès au code source
- Tous les partenaires de développement tiers, équipes de développement externalisées et auditeurs de sécurité
- Tous les modèles de déploiement

**Hors périmètre** :

- Binaires compilés et exécutables (couverts par A.8.1)
- Configurations d'exécution de production (couvertes par A.8.9)
- Normes et pratiques de codage sécurisé (couvertes par ISMS-POL-A.8.25-26-29)
- Gestion des changements pour les déploiements en production (couverte par A.8.32)
- Logiciels commerciaux tiers sans accès au code source
- Logiciels open source utilisés mais non modifiés par [Organisation]

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés |
|----------------|---------------|----------------|
| **ISO/IEC 27001:2022** | Toutes les opérations | A.8.4 — L'accès au code source doit être géré de manière appropriée |
| **nLPD suisse** | Toutes les opérations suisses | Art. 8 — Les mesures techniques et organisationnelles incluent le contrôle d'accès au code source |
| **RGPD de l'UE** | Traitement de données UE | Art. 32 — Les mesures techniques appropriées incluent le contrôle d'accès aux systèmes traitant des données personnelles |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Condition de déclenchement | Exigences clés |
|---------------|---------------------------|----------------|
| **FINMA** | Établissement financier réglementé en Suisse | Protection du code source incluse dans les exigences de sécurité de l'information |
| **DORA** | Entité de services financiers UE | Art. 9 — La gestion des actifs TIC inclut le code source |
| **NIS2** | Entité essentielle/importante (UE) | Art. 21(2) — La gestion des actifs inclut le code source |

## Intégration des contrôles connexes

| Contrôle | Relation |
|----------|----------|
| **A.5.15-16-18 (IAM)** | Fournit le cadre IAM fondateur ; l'AMF et les révisions d'accès s'appliquent aux référentiels |
| **A.8.2-3-5 (Authentification et accès privilégié)** | L'accès administrateur aux référentiels est traité comme un accès privilégié |
| **A.8.25-26-29 (Cycle de vie du développement sécurisé)** | A.8.4 permet les contrôles de développement sécurisé en assurant que seul le personnel autorisé peut modifier le code |
| **A.8.32 (Gestion des changements)** | A.8.4 se concentre sur le contrôle de l'accès au code source avant le déploiement |
| **A.5.24-27 (Gestion des incidents)** | A.8.4 aide à détecter les incidents d'accès au code source par la surveillance |

---

# Exigences de contrôle d'accès

## Gestion de l'accès aux référentiels

[Organisation] met en œuvre le contrôle d'accès basé sur les rôles pour tous les référentiels de code source avec le principe du moindre privilège.

**Principes de contrôle d'accès** :

Tous les référentiels DOIVENT mettre en œuvre un RBAC. Les permissions par défaut DOIVENT être « aucun accès » — attribution explicite requise pour tout niveau d'accès. L'accès aux référentiels DOIT être accordé uniquement sur la base d'un besoin métier documenté et approuvé par le propriétaire du référentiel. L'accès DOIT être révisé trimestriellement pour vérifier la justification continue. L'accès DOIT être automatiquement révoqué à la résiliation de l'emploi, au changement de rôle ou à l'expiration du contrat.

**Processus de révision trimestrielle de l'accès** :

- Révisions conduites avec un formulaire de révision standardisé (modèle dans ISMS-IMP-A.8.4.3)
- Le propriétaire du référentiel confirme pour chaque utilisateur : accès toujours requis (oui/non), niveau d'accès approprié (oui/non), action (maintenir/modifier/révoquer)
- Complétion documentée avec signature et date du propriétaire du référentiel
- Non-réponse escaladée vers le Responsable du développement après 10 jours ouvrables ; vers le RSSI après 15 jours ouvrables

**Demande et approbation d'accès** :

Toutes les demandes d'accès DOIVENT inclure : nom et rôle du demandeur, nom et classification du référentiel, niveau d'accès demandé (lecture/écriture/admin), justification métier, et durée attendue si limitée dans le temps. Les demandes DOIVENT être approuvées par le propriétaire du référentiel (obligatoire), le responsable d'équipe de développement pour l'accès en écriture ou supérieur, et le RSSI ou délégué pour l'accès admin aux référentiels de production. L'accès DOIT être provisionné dans les 24 heures suivant l'approbation pendant les heures ouvrables. Toutes les demandes et approbations DOIVENT être documentées et conservées à des fins d'audit (minimum 3 ans).

**Provisionnement et déprovisionnement des accès** :

L'accès DOIT être provisionné via les systèmes de gestion des identités centralisés autant que techniquement faisable. L'accès DOIT être accordé à des référentiels spécifiques, pas un accès global à tous les référentiels sauf justification explicite. Le système RH DOIT déclencher un flux de déprovisionnement automatisé dans l'heure suivant le traitement de la résiliation. Le déprovisionnement DOIT être vérifié dans les 24 heures via des rapports automatisés.

**Processus de vérification du déprovisionnement** :

- Rapport quotidien automatisé des résiliations traitées dans les 48 dernières heures avec statut de révocation d'accès aux référentiels
- La sécurité IT révise le rapport et confirme : accès révoqué (horodatage), référentiels concernés, vérification complète (case à cocher)
- Échecs de vérification immédiatement escaladés vers les Opérations IT pour remédiation manuelle
- Rapport mensuel de conformité au déprovisionnement adressé au RSSI (cible : 100 % vérifié dans les 24 heures)

## Classification des référentiels et contrôles

[Organisation] classe tous les référentiels de code source pour déterminer les niveaux de protection appropriés.

**Catégories de classification** :

- **Référentiels de code de production** : code directement déployé sur des systèmes de production à destination des clients ou critiques pour l'entreprise (protection maximale) — par ex. application web client, service de traitement des paiements, passerelle API
- **Référentiels d'outils internes** : code pour l'automatisation interne, les utilitaires et les outils opérationnels (protection élevée) — par ex. scripts de pipeline CI/CD, tableaux de bord de surveillance, outils d'administration internes
- **Référentiels de contribution open source** : code de projets publics ou open source auxquels [Organisation] contribue (protection moyenne — accès public contrôlé)
- **Référentiels archivés/dépréciés** : code historique n'étant plus en développement actif (lecture seule)

La classification DOIT être attribuée par le propriétaire du référentiel lors de la création et révisée annuellement.

**Contrôles basés sur la classification** :

Les référentiels de code de production DOIVENT exiger : révision d'au minimum deux personnes pour toutes les fusions de code, protection des branches sur les branches principale et de publication, commits signés si techniquement faisable, analyse des secrets quotidienne, et révisions d'accès trimestrielles. Les référentiels d'outils internes DOIVENT exiger : révision d'au minimum une personne pour les fusions vers la branche principale, protection de la branche principale, analyse des secrets hebdomadaire, et révisions d'accès trimestrielles. Les référentiels open source DOIVENT avoir un contrôle d'accès (non modifiables publiquement), un processus de révision des contributions, une analyse des secrets avant tout push public, et aucun secret ou identifiant interne dans les référentiels publics. Les référentiels archivés/dépréciés DOIVENT être en mode lecture seule, avec suppression des accès en écriture pour tous les utilisateurs, conservation des journaux d'accès, et documentation de l'archivage avec date de dépréciation.

## Contrôle d'accès basé sur les rôles

**Rôles d'accès aux référentiels** :

Les **développeurs** ont l'accès en écriture pour cloner/récupérer les référentiels, créer des branches/commits, pousser vers les branches non protégées, soumettre des pull requests, et assigner des réviseurs. Les développeurs ne peuvent pas pousser vers les branches protégées, approuver leurs propres pull requests, ni modifier les paramètres du référentiel.

L'**équipe sécurité** a l'accès en lecture à tous les référentiels pour les révisions et audits de sécurité, peut cloner/récupérer, lire le code source et l'historique des commits. L'équipe sécurité ne peut pas effectuer de commits ni modifier les paramètres du référentiel sauf attribution spécifique.

Les **auditeurs** ont un accès en lecture seule limité dans le temps pendant la période d'audit, avec accès aux journaux d'audit et rapports de permissions. L'accès expire automatiquement à la fin de l'audit.

Les **contractants externes** ont un accès en écriture limité dans le temps et spécifique au référentiel, limité aux travaux contractuels. L'accès expire à la date de fin de contrat, ne permet pas d'accéder aux référentiels hors du périmètre du projet, et tous les commits sont soumis à une révision renforcée.

Les **administrateurs de référentiels** gèrent les paramètres du référentiel, configurent la protection des branches, gèrent l'accès des collaborateurs. L'accès admin n'accorde pas automatiquement l'accès en écriture au code (séparation des fonctions), et les actions admin sont journalisées.

Les **propriétaires de référentiels** ont la responsabilité ultime du référentiel, approuvent les demandes d'accès, conduisent les révisions d'accès, et définissent la classification du référentiel.

Les **comptes de service** (CI/CD, automatisation de déploiement, scanners de sécurité) DOIVENT être créés avec des noms descriptifs indiquant leur objet, avoir un accès limité aux référentiels spécifiques requis pour l'automatisation, utiliser une authentification par jeton avec expiration, être révisés trimestriellement pour la pertinence continue, et documentés avec propriétaire et objet.

**Critères de révision trimestrielle des comptes de service** :

- L'automatisation/pipeline est-elle toujours active ? (Vérifier la date de dernière activité ; signalée pour suppression si inactive depuis > 90 jours)
- Le propriétaire documenté est-il toujours responsable ?
- Le niveau d'accès est-il toujours approprié ?
- L'expiration du jeton est-elle configurée de manière appropriée ? (Maximum 1 an ; 90 jours recommandés pour les comptes à hauts privilèges)
- Action : Maintenir (avec confirmation), Modifier (réduire l'accès), ou Révoquer (plus nécessaire)

**Application du moindre privilège** :

L'accès admin NE DOIT PAS être accordé aux contractants externes sauf dans des cas exceptionnels documentés avec approbation du RSSI.

## Protection des branches et révision du code

**Protection de la branche principale** :

La branche principale (master/main/trunk) des référentiels de production et d'outils internes DOIT être protégée avec : commits directs bloqués, pull request requis avant fusion, réviseurs minimum (2 pour la production, 1 pour les outils internes), rejet des approbations de pull request obsolètes lors de nouveaux commits, vérifications de statut obligatoires avant fusion (tests CI/CD, linters, analyses de sécurité), commits signés si techniquement faisable, et historique linéaire si techniquement faisable.

Seuls les administrateurs de référentiel PEUVENT modifier les règles de protection des branches. La suppression temporaire des règles de protection nécessite une justification documentée, l'approbation du RSSI, et une réactivation automatique après la période spécifiée.

**Exigences des pull requests** :

Toutes les modifications de code vers les branches protégées DOIVENT être soumises via des pull requests. Les pull requests NE DOIVENT PAS être approuvées par l'auteur du code (séparation des fonctions). Les pull requests DOIVENT inclure une description claire des modifications et de leur objet, un lien vers le ticket/issue connexe le cas échéant, des preuves de tests, et une évaluation de l'impact sécurité pour les modifications liées à la sécurité.

Les pull requests DOIVENT rester ouvertes pendant une période minimale de révision : 4 heures pour les modifications de code de production, 1 heure pour les outils internes, à l'exception des correctifs d'urgence avec révision a posteriori.

**Révision accélérée** (période de révision réduite) : Les modifications à faible risque (mises à jour de documentation, corrections de fautes de frappe, modifications de configuration uniquement sans logique de code) peuvent utiliser une période de révision d'1 heure pour les référentiels de production si : étiquetées « faible risque » ou « docs uniquement », limitées aux fichiers de documentation/configuration, sans modifications de code exécutable, et approuvées par le propriétaire du code.

## Gestion des secrets

**Interdiction des secrets dans le code source** :

Les référentiels DOIVENT être exempts de : mots de passe/phrases secrètes/identifiants, clés API/jetons/clés d'accès, clés cryptographiques privées/certificats, chaînes de connexion aux bases de données avec identifiants intégrés, clés privées SSH/secrets OAuth, clés de chiffrement/vecteurs d'initialisation, ou tout autre matériau d'authentification sensible.

Les fichiers de configuration nécessitant des secrets DOIVENT utiliser des variables d'environnement, des systèmes de gestion des secrets, une configuration chiffrée avec gestion de clés externe, ou des modèles de configuration avec valeurs fictives.

**Analyse des secrets** :

Tous les référentiels DOIVENT avoir l'analyse automatisée des secrets activée avec : analyse pré-commit (empêche les secrets d'entrer dans le référentiel), analyse côté serveur (détecte les secrets déjà présents), fréquence d'analyse en temps réel pour les nouveaux commits et quotidienne pour l'analyse complète du référentiel.

Les résultats d'analyse DOIVENT déclencher : notification immédiate au propriétaire du référentiel et à l'équipe sécurité, création automatique d'un ticket de remédiation, et blocage du commit si l'analyse pré-commit est activée.

**Remédiation des secrets** :

Les secrets découverts DOIVENT être remédiés dans : 1 heure pour les secrets de référentiels de production et 24 heures pour les référentiels d'outils internes, avec rotation immédiate si le secret est confirmé exposé ou utilisé.

**Gestion des exceptions de délai de remédiation** :

- Découverte hors heures ouvrables : ingénieur de garde contacté via PagerDuty/équivalent ; le délai commence à l'accusé de réception ; si pas d'accusé de réception dans les 30 minutes, escalade vers l'ingénieur de garde secondaire
- Si la remédiation en 1 heure n'est pas réalisable : contrôle compensatoire immédiat requis (désactiver le secret chez le fournisseur, révoquer la clé API, bloquer le service concerné) ; remédiation complète dans les 4 heures ; exception documentée avec justification
- Toutes les exceptions de délai journalisées et révisées hebdomadairement par l'Équipe sécurité

## Authentification et AMF

**Méthodes d'authentification** :

L'accès aux référentiels DOIT être authentifié par : nom d'utilisateur/mot de passe (avec AMF requise), authentification par clé publique SSH, jetons d'accès personnels (avec expiration), authentification par certificat, ou SSO via le fournisseur d'identité organisationnel.

**AMF obligatoire pour** :

Tous les comptes utilisateur humain avec accès en écriture ou admin aux référentiels de production, tous les comptes utilisateur humain avec accès admin à tout référentiel, et l'accès aux référentiels via interface web pour tous les utilisateurs.

Méthodes AMF acceptées : applications d'authentification, clés de sécurité matérielles (YubiKey), notification push vers appareil mobile enregistré, et codes SMS (moins préférés, uniquement si d'autres méthodes ne sont pas disponibles).

**Exception AMF pour les comptes de service** : Les comptes de service ne peuvent pas effectuer d'AMF interactive ; contrôles compensatoires appliqués : jetons émis avec périmètre minimum requis (moindre privilège), expiration des jetons appliquée (maximum 1 an ; 90 jours recommandés), activité des comptes de service journalisée et surveillée, révision trimestrielle, comptes de service à hauts privilèges nécessitant l'approbation du RSSI et une surveillance renforcée.

## Journalisation et surveillance des audits

**Exigences de journalisation** :

Les plateformes de référentiels DOIVENT journaliser : événements d'accès (tentatives de connexion, déconnexions, durée de session), accès aux référentiels (clone, récupération, navigation), modifications de code (commits avec auteur/horodatage/message/fichiers, pushs, pushs forcés), opérations sur les branches (création, suppression, modifications de protection), activités de pull request (création, révision, approbation, fusion, rejet), modifications de permissions (accès accordé, révoqué, changements de rôle), actions administratives, et événements de sécurité (alertes d'analyse des secrets, échecs d'authentification, schémas d'accès suspects).

Les journaux DOIVENT inclure au minimum : horodatage (UTC), identité de l'utilisateur, adresse IP source, action effectuée, référentiel concerné, et statut de réussite ou d'échec. Les journaux DOIVENT être inviolables et protégés contre toute modification ou suppression non autorisée.

**Conservation des journaux** :

Les journaux d'accès aux référentiels DOIVENT être conservés pendant des périodes minimales : événements d'accès 1 an, événements de modification du code 3 ans, modifications de permissions 3 ans, événements de sécurité 3 ans, actions administratives 3 ans.

**Surveillance et alertes** :

Les journaux DOIVENT être surveillés pour : tentatives d'authentification multiples échouées (force brute), accès depuis des emplacements géographiques inhabituels, accès en dehors des heures normales d'activité, opérations de téléchargement en masse, tentatives d'élévation de permissions, pushs forcés vers les branches protégées, alertes d'analyse des secrets, et changements importants dans les schémas d'accès.

Les alertes de sécurité DOIVENT être générées et envoyées à l'équipe des opérations de sécurité dans les 15 minutes suivant la détection.

## Sauvegarde et récupération

**Exigences de sauvegarde** :

Tous les référentiels DOIVENT être sauvegardés avec : fréquence de sauvegardes incrémentielles quotidiennes et complètes hebdomadaires, conservation d'au minimum 90 jours pour les référentiels actifs et 7 ans pour les référentiels de production, et redondance géographique avec stockage dans un emplacement géographique différent du référentiel principal.

Les sauvegardes DOIVENT inclure : code source (toutes les branches, tous les commits, historique complet), métadonnées du référentiel (permissions, paramètres, configurations), historique des pull requests, données de suivi des issues si intégrées, et wikis et documentation.

**Tests de récupération** :

Les procédures de récupération des référentiels DOIVENT être testées : trimestriellement pour les référentiels de production, annuellement pour les référentiels d'outils internes, et après les mises à niveau majeures de la plateforme ou les changements de configuration.

**Méthodologie des tests de récupération** :

- Tests effectués dans un environnement de test isolé (pas en production) pour éviter les perturbations opérationnelles
- Tests par échantillons représentatifs acceptables : minimum 3 référentiels de production par trimestre
- La récupération simulée (restauration dans l'environnement de test, vérification de l'intégrité, mesure du RTO) est acceptable
- Test complet annuel incluant au moins une restauration complète de référentiel de production avec validation des permissions

## Gestion des accès tiers

**Exigences d'accès tiers** :

Les développeurs tiers, contractants et équipes de développement externalisées DOIVENT signer des accords de non-divulgation (NDA) avant l'octroi d'accès aux référentiels, avoir un accès limité aux référentiels spécifiques requis pour les travaux contractuels, avoir un accès limité dans le temps lié à la durée du contrat, voir leur accès automatiquement révoqué à l'expiration du contrat, et être soumis à des exigences renforcées de révision du code.

Les demandes d'accès tiers DOIVENT inclure : nom de la société contractante et coordonnées, noms des développeurs individuels nécessitant un accès, référentiels nécessitant un accès avec justification, dates de début et de fin du contrat, et responsabilité du chef de projet.

**Surveillance des tiers** :

L'accès tiers aux référentiels DOIT être surveillé pour détecter des schémas ou comportements inhabituels, révisé mensuellement pour la pertinence continue, et documenté dans le registre des accès tiers. Toutes les contributions de code des tiers DOIVENT nécessiter une révision par un développeur interne, une révision sécurité pour les modifications liées à la sécurité, et une révision de la documentation.

## Gestion des exceptions

**Processus de demande d'exception** :

Les exceptions DOIVENT être demandées par écrit avec : exigence(s) nécessitant une exception, justification métier, contrôles compensatoires le cas échéant, durée demandée, et évaluation et acceptation des risques.

Les exceptions DOIVENT être approuvées par : le propriétaire du référentiel (obligatoire), le Responsable de la sécurité de l'information (obligatoire), et le RSSI (pour les exceptions de référentiels de production).

Les exceptions DOIVENT être accordées pour des périodes limitées (maximum 12 mois) et nécessitent un renouvellement. Toutes les exceptions actives DOIVENT être révisées trimestriellement.

---

# Rôles, gouvernance et conformité

## Rôles et responsabilités

**RSSI** : Responsabilité globale de la politique ; approbation des exceptions ; supervision des incidents de sécurité liés au code source ; révision annuelle de la politique ; reporting à la Direction générale.

**Directeur de la Technologie (DT) / Directeur de l'ingénierie** : Responsabilité de la sélection et de la configuration de la plateforme de développement ; approbation des classifications des référentiels ; point d'escalade pour les litiges d'accès.

**Responsable de la sécurité de l'information** : Maintenance de la politique ; approbation des exceptions (référentiels hors production) ; surveillance de sécurité et investigation des incidents ; coordination des audits ; reporting trimestriel de conformité au RSSI.

**Propriétaires de référentiels** : Attribution de la classification du référentiel ; approbation des demandes d'accès ; révisions trimestrielles des accès ; maintenance de la configuration de sécurité du référentiel ; déclaration des incidents.

**Responsables d'équipes de développement** : Révision des demandes d'accès pour les membres de l'équipe ; application du processus de révision du code ; formation des développeurs aux pratiques de référentiel sécurisé.

**Équipe sécurité** : Surveillance et configuration des alertes de sécurité ; gestion des outils d'analyse des secrets ; audits et évaluations de sécurité ; réponse aux incidents de sécurité liés au code source.

**Opérations IT** : Maintenance et disponibilité de la plateforme de référentiels ; mise en œuvre de la sauvegarde et de la récupération ; automatisation du provisionnement/déprovisionnement des accès.

**Développeurs individuels et contractants** : Conformité aux exigences de contrôle d'accès et d'authentification ; protection des identifiants ; aucun stockage de secrets dans les référentiels ; participation aux révisions de code ; déclaration des incidents.

## Révision et mises à jour de la politique

Cette politique DOIT être révisée annuellement. Les mises à jour de la politique DOIVENT être déclenchées par la révision annuelle planifiée, des incidents de sécurité significatifs liés à l'accès au code source, des changements aux exigences réglementaires, des changements majeurs de la plateforme de référentiels, ou des conclusions d'audit.

Les mises à jour DOIVENT être approuvées par le RSSI (obligatoire), le DT ou Directeur de l'ingénierie (obligatoire), le Responsable juridique/conformité (obligatoire), et la Direction générale (autorité finale). La date d'entrée en vigueur DOIT être fixée à 30 jours après approbation pour permettre la préparation de la mise en œuvre.

## Surveillance de la conformité et reporting

Le Responsable de la sécurité de l'information DOIT surveiller la conformité par des évaluations trimestrielles des contrôles d'accès, une surveillance continue de l'analyse des secrets, une analyse des journaux et détection des anomalies, et un audit des configurations de protection des branches.

Le statut de conformité DOIT être rapporté : mensuellement au RSSI (tableau de bord récapitulatif), trimestriellement à la Direction générale (rapport détaillé), et annuellement au Conseil d'administration (vue d'ensemble stratégique).

**Méthode de calcul du score de conformité global** :

| Composante | Pondération | Source des données |
|-----------|-------------|-------------------|
| Conformité au contrôle d'accès aux référentiels | 35 % | Rapports de la plateforme, dossiers de révision des accès |
| Conformité à la protection des branches | 35 % | Exports de configuration de la protection des branches |
| Gestion des secrets | 20 % | Rapports de l'outil d'analyse des secrets |
| Accès tiers | 10 % | Registre des accès tiers |

**Cibles de conformité** : SMSI mature ≥ 90 % de conformité globale, nouveau SMSI ≥ 70 % de conformité dans les 180 jours.

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.4 v1.0)
- ✅ Signatures d'approbation du RSSI, DT, Direction générale
- ✅ Exigences de contrôle d'accès aux référentiels définies
- ✅ Exigences de protection des branches documentées
- ✅ Exigences de gestion des secrets spécifiées
- ✅ Exigences d'authentification documentées
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

**Référentiel des preuves** : Toutes les preuves d'audit stockées dans la Bibliothèque de preuves SMSI centralisée (SharePoint, Confluence ou équivalent) avec structure de dossiers par contrôle et période d'évaluation.

**Preuves de contrôle d'accès** : Matrice utilisateur-référentiel, dossiers d'approbation des demandes d'accès, dossiers de complétion des révisions trimestrielles, dossiers de signature de NDA, journaux de déprovisionnement et vérification.

**Preuves de protection des branches** : Exports de configuration de la protection des branches, journaux d'application des pull requests, dossiers de complétion des révisions de code, dossiers d'exceptions temporaires avec approbations.

**Preuves de gestion des secrets** : Configuration et journaux de l'outil d'analyse des secrets, dossiers de remédiation des secrets, dossiers de complétion de formation des développeurs.

**Preuves d'authentification** : Rapports d'enrôlement AMF, configuration d'authentification, inventaire et dossiers de rotation des clés SSH/jetons.

**Preuves de sauvegarde et récupération** : Journaux d'exécution des sauvegardes, résultats des tests de récupération, mesures de conformité au RTO.

---

# Date d'entrée en vigueur et transition

## Priorités de mise en œuvre

Les référentiels DOIVENT être mis en conformité dans l'ordre de priorité suivant :

1. Référentiels de code de production (applications à destination des clients)
2. Référentiels d'infrastructure-as-code de production
3. Référentiels d'outils internes
4. Référentiels de contribution open source
5. Référentiels archivés/dépréciés

## Exceptions et période transitoire

Aucune exception permanente NE DOIT être accordée uniquement sur la base de « l'état existant » ou du « référentiel hérité ». Des exceptions temporaires PEUVENT être accordées pendant la période transitoire pour des limitations techniques, des dépendances tierces ou des contraintes de ressources. Toutes les exceptions temporaires DOIVENT être documentées avec justification et plan de remédiation, approuvées par le RSSI, expirer au plus tard 12 mois après la date d'entrée en vigueur de la politique, et suivies dans le système de gestion des exceptions.

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur de la Technologie (DT)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale (PDG)** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de contrôle d'accès au code source. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.4.1 (Contrôle d'accès aux référentiels), ISMS-IMP-A.8.4.2 (Protection des branches) et ISMS-IMP-A.8.4.3 (Évaluation de l'accès au code source).*

<!-- QA_VERIFIED: 2026-04-02 -->
