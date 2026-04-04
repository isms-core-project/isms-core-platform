<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.9-FR:operational:OP-POL:a.8.9 -->
**ISMS-OP-POL-A.8.9 — Gestion de la configuration**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion de la configuration |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.9 |
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

- ISO/IEC 27001:2022 Contrôle A.8.9 — Gestion de la configuration
- ISO/IEC 27002:2022 Section 8.9 — Recommandations de mise en œuvre pour la gestion de la configuration
- NIST SP 800-128 — Guide pour la gestion de la configuration axée sur la sécurité des systèmes d'information
- NIST SP 800-53 Rév. 5 — CM-2 (Configuration de référence), CM-3 (Contrôle des changements de configuration), CM-6 (Paramètres de configuration), CM-7 (Fonctionnalité minimale)
- CIS Controls v8 — Contrôle 4 (Configuration sécurisée des actifs et logiciels d'entreprise)
- CIS Benchmarks — Guides de durcissement spécifiques aux plateformes

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la gestion de la configuration |
|----------|--------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | L'inventaire des actifs définit le périmètre de la gestion de la configuration ; chaque élément de configuration est rattaché à un actif inventorié |
| A.5.23 Sécurité de l'information pour les services cloud | Les configurations des services cloud sont gérées dans le cadre de cette politique ; le modèle de responsabilité partagée définit les limites de configuration |
| A.5.24–28 Gestion des incidents | La dérive de configuration ou les changements non autorisés peuvent déclencher la réponse aux incidents ; les changements échoués sont escaladés comme incidents |
| A.8.1–7–18–19 Sécurité des points de terminaison | Les configurations de référence et les normes de durcissement des points de terminaison sont définies et appliquées dans le cadre de cette politique |
| A.8.8 Gestion des vulnérabilités techniques | La remédiation des vulnérabilités peut nécessiter des changements de configuration ; le durcissement réduit la surface de vulnérabilité |
| A.8.15 Journalisation | Les événements de changement de configuration sont journalisés pour la piste d'audit et la détection de dérive |
| A.8.16 Activités de supervision | Les outils de supervision détectent la dérive de configuration et les changements non autorisés |
| A.8.20–22 Sécurité des réseaux | Les configurations des équipements réseau (pare-feux, commutateurs, routeurs) sont gérées comme éléments de configuration |
| A.8.32 Gestion des changements | Les changements de configuration suivent le processus d'approbation de la gestion des changements ; disciplines complémentaires |

**Politiques internes associées** :

- Politique de gestion des actifs
- Politique de gestion des changements
- Politique de sécurité des points de terminaison
- Politique de sécurité des réseaux
- Politique de journalisation
- Politique des activités de supervision (A.8.16)
- Politique de gestion des vulnérabilités
- Politique de gestion des incidents

---

# Politique de gestion de la configuration

## Objet

La présente politique a pour objet de s'assurer que les configurations, y compris les configurations de sécurité, des équipements, logiciels, services et réseaux sont établies, documentées, mises en œuvre, supervisées et révisées de manière à réduire le risque d'incidents de sécurité causés par des erreurs de configuration, des changements non autorisés ou une dérive de configuration.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles traitées par les systèmes soumis à la gestion de la configuration. La configuration sécurisée des systèmes traitant des données personnelles est une mesure technique fondamentale démontrant la conformité aux obligations de protection des données. Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, les exigences du RGPD art. 32 s'appliquent également.

## Champ d'application

Tous les employés, prestataires et utilisateurs tiers ayant des responsabilités dans la configuration, la maintenance ou l'administration des systèmes d'information.

Tous les systèmes d'information, infrastructures et services nécessitant une gestion de la configuration, notamment :

- **Calcul et infrastructure** : Serveurs (physiques et virtuels), conteneurs, postes de travail, appareils mobiles.
- **Équipements réseau** : Pare-feux, routeurs, commutateurs, équilibreurs de charge, points d'accès sans fil, passerelles VPN.
- **Services cloud** : Configurations IaaS, PaaS et SaaS dans le périmètre de contrôle de l'organisation.
- **Systèmes d'exploitation** : Configurations des systèmes d'exploitation des serveurs et des points de terminaison.
- **Applications et intergiciels** : Serveurs d'applications, bases de données, serveurs web, files de messages.
- **Systèmes de sécurité** : SIEM, protection des points de terminaison, détection/prévention des intrusions, fournisseurs d'identité.
- **Systèmes IoT et OT** : Appareils connectés et technologies opérationnelles gérés par l'organisation.

Dans tous les environnements : production, hors production (développement, test, assurance qualité, pré-production), reprise après sinistre et bac à sable.

**Hors périmètre** : Appareils AVEC non gérés par l'organisation ; plateformes SaaS où l'organisation n'a aucun contrôle de configuration (gérées uniquement par le fournisseur) ; systèmes temporaires dont le cycle de vie est inférieur à 24 heures (sauf traitement de données personnelles ou sensibles) ; systèmes explicitement exclus par évaluation des risques documentée avec approbation du RSSI.

## Principe

Tous les systèmes d'information doivent être configurés selon des configurations de référence de sécurité documentées et approuvées avant leur déploiement en production. Les configurations par défaut du fabricant (« prêt à l'emploi ») ne sont pas acceptables pour un usage en production.

Les configurations doivent être :

- **Établies** : Configurations de référence sécurisées définies pour chaque type d'actif selon des normes de durcissement reconnues.
- **Documentées** : Paramètres de référence enregistrés, soumis au contrôle de version et accessibles au personnel autorisé.
- **Mises en œuvre** : Systèmes déployés à partir de configurations de référence ou d'images standardisées approuvées.
- **Supervisées** : Configurations réelles comparées aux configurations de référence approuvées pour détecter les dérives.
- **Révisées** : Configurations de référence révisées et mises à jour à des intervalles définis et à la suite de changements significatifs.

L'organisation applique le principe de fonctionnalité minimale : les systèmes sont configurés pour ne fournir que les fonctionnalités requises pour leur objet, avec les services, ports, protocoles et comptes inutiles désactivés ou supprimés.

**Mise en œuvre de la fonctionnalité minimale** (exigences spécifiques) :

**Services (processus/démons)** :
- Approche : Autoriser uniquement les services requis pour le rôle du système.
- Exemple — Configuration de référence du serveur d'applications Ubuntu : Services requis : sshd (gestion à distance), systemd-resolved (DNS), chrony (synchronisation de l'heure), service applicatif (par exemple nginx, processus d'application). Désactivés/supprimés : cups (impression), avahi-daemon (mDNS), bluetooth, X11 (services graphiques).
- Validation : `systemctl list-units --state=running` comparé à la liste blanche de référence ; services non autorisés signalés.

**Ports réseau** :
- Approche : Autoriser uniquement les ports en écoute requis.
- Exemple — Windows Server 2022 Contrôleur de domaine : Ports requis : 53 (DNS), 88 (Kerberos), 135 (RPC), 389/636 (LDAP/LDAPS), 445 (SMB), 3389 (RDP — restreint au sous-réseau d'administration). Bloqués : Tous les autres ports via le pare-feu hôte.
- Validation : `netstat -an` ou `ss -tuln` comparé à la référence ; auditeurs inattendus signalés.

**Protocoles** :
- Désactiver les protocoles anciens/non sécurisés : SMBv1 (désactivé), TLS inférieur à 1.2 (désactivé), SSHv1 (désactivé), Telnet (supprimé), FTP (remplacé par SFTP/FTPS).
- Activer uniquement les alternatives sécurisées : SSH (v2 minimum), TLS 1.2/1.3 uniquement, HTTPS obligatoire.

**Comptes par défaut** :
- Supprimer ou désactiver : Comptes invités, comptes par défaut des fournisseurs (Administrateur renommé, mots de passe par défaut modifiés), comptes de service inutilisés.
- Exigence de référence : Documenter tous les comptes dans la référence avec justification (pourquoi le compte existe, à quoi il sert).

**Fonctionnalités/rôles inutiles** :
- Windows : Supprimer les rôles de serveur inutilisés (par exemple supprimer Services d'impression si pas de serveur d'impression, supprimer IIS si pas de serveur web).
- Linux : Supprimer les paquets inutilisés (`apt autoremove`, `yum remove`).
- Cloud : Désactiver les services cloud inutilisés (par exemple désactiver la console série AWS EC2 si inutile, désactiver Azure Bastion si non utilisé).

Documentation : Chaque configuration de référence comprend un tableau « Services et ports requis » listant les éléments autorisés avec justification.

---

## Configurations de référence

### Définition des configurations de référence

L'organisation définit et maintient des configurations de référence sécurisées au niveau **type d'actif** (par exemple « Windows Server 2022 — Contrôleur de domaine », « Ubuntu 24.04 — Serveur d'applications », « Cisco IOS-XE — Commutateur principal »), et non au niveau des actifs individuels.

Les configurations de référence sont définies pour tous les types d'actifs en production active.

**Exigences de couverture des configurations de référence** :

La couverture est mesurée par :

- **Couverture des types d'actifs** : Pourcentage de types d'actifs distincts (combinaisons SE + rôle) avec des configurations de référence documentées.
- **Couverture des instances** : Pourcentage du total des instances d'actifs de production couvertes par des configurations de référence.

**Objectifs de couverture** :

| Niveau d'actif | Couverture des types d'actifs | Couverture des instances | Délai |
|----------------|-------------------------------|--------------------------|-------|
| **Niveau 1 (Critique)** | 100 % | 100 % | Immédiat (aucune exception) |
| **Niveau 2 (Élevé)** | 100 % | 95 % | Dans les 6 mois suivant le déploiement en production |
| **Niveau 3 (Moyen)** | 90 % | 90 % | Dans les 12 mois suivant le déploiement en production |
| **Niveau 4 (Faible)** | 80 % | 80 % | Meilleur effort |

**Gestion des lacunes** :

- **Actifs de niveaux 1/2 sans configurations de référence** : Le déploiement en production est bloqué jusqu'à la création d'une configuration de référence (appliqué via l'approbation des changements).
- **Lacunes de niveaux 3/4** : Documentées dans le registre des lacunes de configurations de référence avec un plan de remédiation (objectif : configuration de référence créée dans les 90 jours suivant le déploiement en production).
- **Exception** : Les systèmes hérités approchant de leur décommissionnement (moins de 12 mois restants) peuvent être dispensés de l'exigence de configuration de référence avec acceptation du risque par le RSSI et supervision renforcée.

Chaque configuration de référence documente :

- **Identifiant de la configuration de référence** (par exemple BASE-WIN2022-DC-v1.2) et version.
- **Type d'actif** et environnements applicables.
- **Paramètres du système d'exploitation** : Paramètres de sécurité, services activés/désactivés, paramètres du noyau, paramètres de registre.
- **Configurations applicatives** : Paramètres par défaut, paramètres de sécurité, points d'intégration.
- **Paramètres réseau** : Configuration IP, règles de pare-feu, listes de contrôle d'accès, routage.
- **Configurations de sécurité** : Paramètres d'authentification, paramètres de chiffrement, paramètres de journalisation et d'audit, politiques de mots de passe.
- **Norme de durcissement appliquée** : Niveau CIS Benchmark, guide du fournisseur ou norme personnalisée avec justification.
- **Exceptions et dérogations** : Tout écart par rapport à la norme de durcissement, avec justification documentée et acceptation du risque.
- **Critères de validation** : Comment vérifier qu'un système est conforme à la configuration de référence.

### Approbation des configurations de référence

Les nouvelles configurations de référence et les mises à jour suivent un processus d'approbation défini :

| Action | Autorité d'approbation | Délai |
|--------|------------------------|-------|
| **Nouvelle configuration de référence** | Responsable technique (valide l'exactitude) + RSSI ou délégué (valide la sécurité) | 14 jours ouvrés |
| **Mise à jour de configuration de référence** | Responsable technique + RSSI ou délégué | 7 jours ouvrés |
| **Changement d'urgence de configuration de référence** | RSSI (accéléré) | 24 heures ; revue rétrospective dans les 5 jours ouvrés |

### Révision des configurations de référence

Les configurations de référence sont révisées et mises à jour :

- **Annuellement** (minimum) pour toutes les configurations de référence.
- **Trimestriellement** pour les configurations de référence des systèmes de niveau 1 (critique).
- **Ponctuellement** lorsque déclenchées par : de nouvelles divulgations de vulnérabilités affectant les paramètres de référence, des mises à niveau technologiques ou des changements de version, des évolutions des exigences réglementaires ou de conformité, des enseignements tirés d'incidents de sécurité.

### Dépréciation des configurations de référence

Lorsqu'un type d'actif est décommissionné ou remplacé :

- La configuration de référence est marquée « DÉPRÉCIÉE » avec une date d'effet.
- La configuration de référence est conservée dans le référentiel pendant 3 ans à titre de référence historique.
- La configuration de référence est retirée de la supervision de conformité active.
- Une configuration de référence de remplacement (le cas échéant) est référencée dans le référentiel.

---

## Constructions standard et images standardisées

L'organisation devrait adopter des constructions standard et des images standardisées pour assurer un déploiement cohérent et reproductible de systèmes configurés de manière sécurisée.

### Exigences des images standardisées

Les images standardisées :

- Mettent en œuvre la configuration de référence approuvée pour le type d'actif concerné.
- Contiennent uniquement des logiciels approuvés et sous licence.
- Incluent les correctifs de sécurité courants au moment de la création de l'image.
- Sont testées dans un environnement hors production avant d'être approuvées pour un usage en production.
- Sont versionnées et suivies dans un référentiel de configuration.

**Politique d'actualisation des images standardisées** (basée sur les risques) :

**Actualisation programmée** (référence) :
- **Images de niveaux 1/2** : Actualisation mensuelle.
- **Images de niveaux 3/4** : Actualisation trimestrielle.

**Actualisation déclenchée** (immédiate, remplace le programme) :
- **Correctif de vulnérabilité critique** : Dans les 7 jours suivant la publication du correctif (pour les vulnérabilités affectant les logiciels de référence avec CVSS >= 9,0 ou exploitation active).
- **Mise à jour de la configuration de référence** : Dans les 14 jours suivant un changement de configuration de référence approuvé.
- **Incident de sécurité** : Immédiatement si l'image standardisée peut être compromise ou contient une configuration vulnérable.

**Procédure d'actualisation** :
1. Mettre à jour l'image de base avec les derniers correctifs.
2. Appliquer la configuration de référence actuelle.
3. Tester hors production : Déployer une instance de test, exécuter la suite de validation (tests fonctionnels, analyse de sécurité).
4. Validation par l'équipe sécurité : Analyser les erreurs de configuration, vérifier la conformité au durcissement.
5. Approbation : Signature du Responsable des opérations informatiques + Équipe sécurité.
6. Publication : Remplacer l'ancienne image dans le référentiel, marquer l'ancienne image « DÉPRÉCIÉE ».
7. Notification : Informer les administrateurs système de la nouvelle version de l'image.

**Conservation des anciennes images** :
- Version précédente : Conservée 90 jours (capacité de retour arrière si la nouvelle image présente des problèmes).
- Versions plus anciennes : Archivées pendant 1 an (référence historique).

**Application du déploiement** :
- Déploiements utilisant des images de plus de 60 jours : Signalés pour examen (pourquoi ne pas utiliser l'image actuelle ?).
- Déploiements utilisant des images de plus de 90 jours : Rejetés (doit utiliser l'image actuelle ou documenter une exception).

**Suivi de l'ancienneté des images** : [Système de gestion des actifs] enregistre la date de création de l'image par instance déployée ; rapport mensuel sur les « déploiements obsolètes » (instances issues d'images de plus de 30 jours).

La création des images standardisées est restreinte au personnel autorisé (administrateurs système ou ingénieurs DevOps). Les images standardisées nouvelles ou mises à jour sont validées par l'équipe sécurité avant approbation.

### Infrastructure en tant que code

Lorsque cela est réalisable, l'organisation devrait définir les configurations de référence sous forme de code (par exemple Terraform, Ansible, CloudFormation, manifestes Kubernetes, Puppet, Chef) et les gérer via le contrôle de version :

- **Contrôle de version** : Définitions IaC stockées dans Git ou équivalent avec historique complet des changements.
- **Revue de code** : Les changements de configuration soumis via demande de fusion et révisés avant intégration.
- **Tests automatisés** : IaC validée par des tests automatisés (analyse statique, analyse politique en tant que code, simulation) avant déploiement.
- **Intégration à la gestion des changements** : Les déploiements IaC soumis au processus de gestion des changements de l'organisation.
- **Analyse des erreurs de configuration** : Les modèles IaC analysés pour les erreurs de configuration de sécurité avant déploiement (par exemple Checkov, tfsec, ou équivalent).

**Exigences d'analyse de sécurité IaC** :

**Outils d'analyse** : [Checkov / tfsec / Terraform Sentinel / Open Policy Agent] configurés selon les normes de l'organisation.

**Règles d'analyse obligatoires** (tous les modèles IaC) :

| Catégorie | Exemples de règles | Niveau d'application |
|-----------|-------------------|----------------------|
| **Chiffrement** | Compartiments S3 chiffrés au repos, chiffrement RDS activé, volumes EBS chiffrés, TLS en transit | Bloquant (le déploiement échoue en cas de violation) |
| **Contrôle d'accès** | Pas de compartiments S3 publics (sauf approbation explicite), groupes de sécurité sans ingress 0.0.0.0/0 sur les ports sensibles (22, 3389), politiques IAM respectant le moindre privilège | Bloquant |
| **Journalisation** | CloudTrail activé, journaux de flux VPC activés, journalisation RDS/base de données activée | Bloquant |
| **Gestion des secrets** | Pas d'identifiants en dur dans l'IaC (doit utiliser des références au gestionnaire de secrets), pas de clés API en clair | Bloquant |
| **Sécurité réseau** | VPC par défaut non utilisé, sous-réseaux correctement segmentés (public/privé), NACL configurés | Avertissement (revue requise, peut être contourné avec justification) |
| **Fonctionnalité minimale** | Règles du groupe de sécurité par défaut supprimées, services inutiles désactivés dans les configurations de lancement | Avertissement |

**Règles personnalisées** (spécifiques à l'organisation) :
- Étiquettes obligatoires : Toutes les ressources étiquetées avec Propriétaire, Environnement, CentreDeCoûts, ClassificationDesDonnées.
- Types d'instances approuvés : Uniquement les familles d'instances approuvées par l'organisation (pas de types exotiques sans approbation).
- Régions approuvées : Déploiements uniquement dans les régions cloud approuvées (par exemple eu-central-1, westeurope).

**Exécution des analyses** :
- **Pré-contribution** : Les développeurs exécutent les analyses localement avant de valider les changements IaC (recommandé, non appliqué).
- **Pipeline CI/CD** : Analyse automatisée sur demande de fusion (requise) ; les violations bloquantes empêchent l'intégration.
- **Processus d'exception** : Si une violation bloquante ne peut être remédiée (besoin métier légitime), le développeur documente l'exception dans [Outil de suivi des exceptions], le RSSI approuve, l'exception est ajoutée à l'IaC comme commentaire + règle de suppression.

**Traitement des résultats d'analyse** :
- Violations bloquantes : Déploiement suspendu, remédier avant une nouvelle tentative.
- Violations avec avertissement : Journalisées, révisées par l'équipe sécurité hebdomadairement, escaladées si un schéma émerge.
- Exceptions : Révisées trimestriellement, révoquées si plus justifiées.

**Maintenance du jeu de règles** :
- L'équipe sécurité maintient le jeu de règles d'analyse IaC dans [Référentiel Git].
- Jeu de règles révisé trimestriellement, mis à jour pour les nouvelles menaces et bonnes pratiques.
- Soumis au contrôle de version avec journal des changements.

L'IaC ne remplace pas le besoin de configurations de référence documentées ; elle constitue la méthode privilégiée pour les mettre en œuvre et les faire respecter.

---

## Contrôle des changements de configuration

Tous les changements de configuration des systèmes suivent le processus de gestion des changements de l'organisation (voir **Politique de gestion des changements — A.8.32**). La présente section aborde les exigences spécifiques à la configuration qui complètent la gestion des changements.

### Classification des changements

Les changements de configuration sont classifiés selon le risque et l'impact :

| Type | Définition | Approbation | Exemples |
|------|------------|-------------|---------|
| **Standard** | Changement de configuration pré-approuvé, à faible risque et reproductible selon une procédure documentée | Pré-approuvé (catalogue) | Renouvellement de certificat, ajout d'enregistrement DNS, règle de pare-feu standard |
| **Normal** | Nécessite une évaluation, des tests et une approbation formelle | Propriétaire du service / CCH | Mise à jour de configuration de référence, nouvelle norme de durcissement, changement de topologie réseau |
| **Urgence** | Changement urgent pour résoudre un incident critique ou une vulnérabilité | RSSI ou Responsable des opérations informatiques (accéléré) | Désactivation d'un service compromis, règle de pare-feu d'urgence, correctif critique |

### Catégorisation des changements de configuration

**Nécessite une approbation formelle de changement** (Politique de gestion des changements A.8.32) :
- Changements de configuration liés à la sécurité : Paramètres d'authentification, paramètres de chiffrement, règles de pare-feu, contrôles d'accès, niveaux de journalisation (événements de sécurité), autorisations utilisateur/groupe.
- Changements de configuration de référence : Toute modification de la définition de la configuration de référence approuvée.
- Changements de systèmes de production : Tout changement de configuration des systèmes de production de niveaux 1/2 (quel que soit le rapport avec la sécurité).
- Changements de topologie réseau : Routage, VLAN, sous-réseaux, politiques de pare-feu.
- Changements multi-systèmes : Changements de configuration affectant plus de 5 systèmes simultanément.

**Pré-approuvés** (catalogue de changements standard, sans CCH) :
- Ajustement de paramètres dans les plages documentées : Durée de rotation des journaux (7–30 jours), tailles de cache (dans les limites définies), valeurs de délai d'expiration (dans des plages sûres).
- Renouvellements de certificats : Remplacement de certificat TLS/SSL avec les mêmes paramètres.
- Ajouts d'enregistrements DNS : Ajout d'enregistrements A/AAAA/CNAME (pas de changement des serveurs faisant autorité).
- Provisionement/déprovisionement d'utilisateurs : Suivant les procédures d'entrée/mutation/sortie documentées.

**Ne nécessite pas d'approbation de changement** (ajustement opérationnel) :
- Changements cosmétiques : Libellés d'interface, descriptions non fonctionnelles, champs de commentaires.
- Ajustement des seuils de supervision : Modification des seuils d'alerte sur la base des valeurs observées (documenté dans l'outil de supervision).
- Systèmes hors production : Changements de configuration des systèmes de développement/test de niveaux 3/4 (journalisés mais pas formellement approuvés, sauf si liés à la sécurité).

Recommandation : En cas de doute sur la nécessité d'une approbation, la réponse par défaut est **oui** (soumettre une demande de changement).

Documentation : Le catalogue de changements standard est maintenu dans [Système de gestion des changements] avec des procédures pré-approuvées et des évaluations des risques.

### Mise à jour de la documentation de configuration

À la suite de tout changement de configuration approuvé, les éléments suivants sont mis à jour dans les **5 jours ouvrés** :

- Documentation des configurations de référence (si la configuration de référence elle-même a changé).
- Base de données de gestion des configurations (BDGC) ou enregistrements d'actifs équivalents.
- Schémas réseau et documentation de topologie (si la configuration réseau a changé).
- Procédures opérationnelles et manuels d'exploitation (si les étapes opérationnelles ont changé).
- Procédures de reprise après sinistre (si le changement affecte les systèmes critiques ou le RTO/RPO).

### Changements de configuration non autorisés

Les changements de configuration effectués en dehors du processus de gestion des changements approuvé sont traités comme des événements de sécurité :

- Détectés par la supervision de la configuration et la détection de dérive.
- Faisant l'objet d'une enquête pour déterminer la cause profonde (malveillant, accidentel ou lacune de processus).
- Signalés au RSSI.
- Soumis à des mesures correctives pouvant inclure des mesures disciplinaires.
- Le système concerné est remédié à la configuration de référence approuvée ou une nouvelle configuration de référence est formellement approuvée via le processus standard.

---

## Détection et supervision de la dérive de configuration

### Exigences de supervision

L'organisation met en œuvre une supervision de la configuration pour détecter les écarts par rapport aux configurations de référence approuvées.

**Objectifs de couverture par criticité des actifs** :

| Niveau d'actif | Objectif de couverture | Fréquence de supervision | Écart acceptable |
|----------------|------------------------|--------------------------|------------------|
| **Niveau 1 (Critique)** | 100 % | Temps réel ou horaire | 0 % |
| **Niveau 2 (Élevé)** | 95 % ou plus | Quotidien | Moins de 5 % |
| **Niveau 3 (Moyen)** | 85 % ou plus | Hebdomadaire | Moins de 15 % |
| **Niveau 4 (Faible)** | 70 % ou plus | Mensuel | Moins de 30 % |

Les outils de supervision :

- Comparent la configuration réelle du système à la configuration de référence approuvée.
- Génèrent des alertes lorsque des déviations de configuration sont détectées.
- Conservent les résultats de supervision pendant un minimum de 90 jours.
- S'intègrent avec [SIEM] pour les alertes centralisées et la corrélation lorsque cela est réalisable.

**Sélection des outils** : L'organisation sélectionne des outils de supervision de la configuration adaptés à son environnement technique. Les outils prennent en charge la comparaison aux configurations de référence et la détection de dérive. Les exemples comprennent : outils de supervision de l'intégrité des fichiers (FIM), outils d'évaluation de la configuration cloud (par exemple AWS Config, Azure Policy, GCP Security Command Center), plateformes de gestion des points de terminaison et analyseurs de conformité de la configuration.

Les types d'actifs ne faisant pas encore l'objet d'une supervision automatisée sont documentés avec une date de déploiement prévue et des contrôles manuels intérimaires (par exemple audits manuels trimestriels). Les lacunes de couverture sont acceptées par le RSSI comme risques et enregistrées dans le registre des risques.

### Gestion des lacunes de couverture de la supervision

**Exigences de documentation des lacunes** :
- Type/instance d'actif non encore supervisé : Enregistré dans le Registre des lacunes de supervision.
- Champs du registre : Identifiant d'actif, Niveau, Raison de la lacune (limitation de l'outil, budget en attente, contrainte technique), Contrôle intérimaire (audit manuel, journalisation renforcée, accès restreint), Responsable (qui remédie), Date de déploiement prévue, Date de déploiement réelle, Statut (Ouvert/En cours/Clôturé).

**Délais de clôture des lacunes** (de l'identification au déploiement de la supervision) :

| Niveau d'actif | Durée maximale de la lacune | Exigence de contrôle intérimaire | Escalade si délai non respecté |
|----------------|------------------------------|----------------------------------|-------------------------------|
| **Niveau 1** | 30 jours | Audit manuel renforcé (revue hebdomadaire de configuration + audit mensuel complet) | RSSI (immédiat) ; peut nécessiter un gel de production jusqu'au déploiement de la supervision |
| **Niveau 2** | 90 jours | Audit manuel (revue mensuelle de configuration) | Responsable des opérations informatiques puis RSSI à 60 jours |
| **Niveau 3** | 180 jours | Audit manuel (trimestriel) | Responsable des opérations informatiques à 120 jours |
| **Niveau 4** | 365 jours | Audit manuel annuel acceptable | Responsable des opérations informatiques à 270 jours |

**Responsabilité de clôture des lacunes** :
- Responsable de la lacune : Chargé de mettre en œuvre la solution de supervision à la date de déploiement prévue.
- Revue mensuelle : Le Responsable des opérations informatiques examine le Registre des lacunes de supervision, suit les progrès, escalade les lacunes en retard.
- Rapport trimestriel : Résumé du registre des lacunes communiqué au RSSI (nombre de lacunes ouvertes par niveau, délai moyen de clôture, lacunes en retard).

**Contrôles intérimaires** (pendant que la lacune persiste) :
- Revue manuelle de la configuration : L'administrateur système exporte la configuration, la compare manuellement à la configuration de référence, documente les résultats.
- Journalisation renforcée des accès : L'accès des comptes à privilèges aux systèmes non supervisés est journalisé et révisé hebdomadairement.
- Gel des changements (niveau 1 uniquement) : Si la supervision ne peut être déployée dans les délais, envisager de geler les changements non urgents jusqu'à la disponibilité de la supervision.

**Acceptation du risque de lacune** :
- Si la lacune ne peut être comblée (par exemple système hérité incompatible avec les outils de supervision, contraintes budgétaires) : Le RSSI approuve l'acceptation du risque avec justification documentée, contrôles compensatoires et révision annuelle.
- L'acceptation du risque ne dispense pas des contrôles intérimaires — les audits manuels se poursuivent.

**Critère de succès** : Objectif de moins de 5 % des actifs de niveaux 1/2 dans le Registre des lacunes de supervision à tout moment.

### Classification et réponse à la dérive

Lorsqu'une dérive de configuration est détectée, elle est classifiée par gravité et traitée dans des délais définis :

| Gravité | Définition | Délai de réponse | Exemples |
|---------|------------|------------------|---------|
| **Critique** | Contrôle de sécurité désactivé ou compromis | Moins d'1 heure | Pare-feu désactivé, compte administrateur non autorisé créé, chiffrement désactivé, journalisation désactivée sur un système critique |
| **Élevée** | Configuration liée à la sécurité modifiée | Moins de 4 heures | Politique de mots de passe affaiblie, service inutile activé, liste de contrôle d'accès modifiée sans approbation |
| **Moyenne** | Dérive de configuration non liée à la sécurité | Moins de 24 heures | Port de service modifié, paramètre d'application non critique modifié, écart de documentation |
| **Faible** | Déviation informative | Moins de 5 jours ouvrés | Changements cosmétiques, paramètres non fonctionnels, différences mineures de paramètres |

**Acheminement des alertes** :

- **Critique et Élevée** : Équipe des opérations de sécurité + RSSI + Propriétaire du système.
- **Moyenne** : Responsable des opérations informatiques + Propriétaire du système.
- **Faible** : Opérations informatiques (rapport quotidien consolidé).

### Remédiation de la dérive

La remédiation de la dérive suit un processus structuré :

1. **Détection** : La supervision automatisée identifie la déviation de configuration.
2. **Tri** : Les opérations informatiques enquêtent sur la cause et déterminent si le changement était autorisé, non autorisé ou un faux positif.
3. **Action** :
   - **Changement autorisé** (approuvé mais documentation de référence pas encore mise à jour) : Mettre à jour la documentation de la configuration de référence ; clôturer l'alerte.
   - **Changement non autorisé** : Remédier le système à la configuration de référence approuvée ; enquêter sur la cause profonde ; signaler au RSSI ; clôturer après résolution.
   - **Faux positif** : Affiner les règles de supervision ; clôturer l'alerte.
4. **Documentation** : Tous les incidents de dérive journalisés, suivis jusqu'à clôture et conservés pour audit.

**Vérification de la remédiation de la dérive** (obligatoire) :

Procédure de remédiation :
1. **Identifier la dérive** : L'outil de supervision détecte la déviation (par exemple règle de pare-feu ajoutée, service activé, paramètre modifié).
2. **Enquêter** : Déterminer si autorisé (changement approuvé pas encore documenté) ou non autorisé.
3. **Remédier** : Si non autorisé, restaurer à la configuration de référence :
   - Manuel : L'administrateur système rétablit le paramètre de configuration à la valeur de référence.
   - Automatisé : L'outil de gestion de la configuration (Ansible, Puppet, Chef) réapplique la configuration de référence.
   - Réinstallation : En cas de dérive grave ou de compromission, reconstruire à partir de l'image standardisée.
4. **Vérifier la remédiation** (dans les 24 heures suivant la remédiation) :
   - Réanalyser le système avec le même outil de supervision qui a détecté la dérive.
   - Confirmer que l'alerte de dérive est effacée.
   - Documenter : Ticket de remédiation mis à jour avec horodatage de vérification, résultats d'analyse et signature.
5. **Analyse des causes profondes** (pour les dérives Critique/Élevée) :
   - Pourquoi la dérive s'est-elle produite ? (Lacune de processus, accès non autorisé, défaillance d'automatisation, erreur de configuration de référence.)
   - Action préventive : Mettre à jour la configuration de référence, améliorer l'automatisation, renforcer les contrôles d'accès, former le personnel.
6. **Clôturer le ticket** : Uniquement après que la vérification confirme la conformité à la configuration de référence.

**Vérification échouée** :
- Si la nouvelle analyse montre que la dérive persiste : Escalader au Responsable des opérations informatiques, réitérer la remédiation, envisager l'isolation du système en cas de dérive de contrôle de sécurité.
- Si la dérive récidive dans les 30 jours : Enquête obligatoire sur les causes profondes, RSSI notifié.

**Métriques de remédiation de la dérive** suivies :
- Pourcentage des remédiations de dérive avec vérification complète : Objectif 100 %.
- Délai entre remédiation et vérification : Objectif moins de 24 heures.
- Dérive récurrente (même système, même paramètre, plus de 2 occurrences) : Objectif 0.

Rapport mensuel au RSSI.

**Délais de remédiation** :

| Gravité | Délai de remédiation | Escalade si délai non respecté |
|---------|----------------------|-------------------------------|
| **Critique** | Moins de 4 heures | RSSI — peut isoler le système de la production |
| **Élevée** | Moins de 24 heures | RSSI |
| **Moyenne** | Moins de 5 jours ouvrés | Responsable des opérations informatiques |
| **Faible** | Moins de 30 jours | Meilleur effort |

Une dérive récurrente sur le même système ou type d'actif déclenche une analyse des causes profondes. Si la cause est une configuration de référence impraticable à maintenir, la configuration de référence est révisée et mise à jour via le processus d'approbation standard plutôt que d'accepter répétitivement des exceptions.

---

## Normes de durcissement de sécurité

### Sélection des normes de durcissement

L'organisation sélectionne et applique des normes de durcissement de sécurité reconnues pour tous les types d'actifs de production.

**Normes reconnues** (par ordre de préférence) :

| Norme | Fournisseur | Usage habituel |
|-------|-------------|----------------|
| **CIS Benchmarks** | Center for Internet Security | Référence principale pour les plateformes courantes (Windows, Linux, cloud, équipements réseau, bases de données) |
| **Guides de sécurité des fournisseurs** | Microsoft, AWS, Azure, GCP, Cisco, etc. | Plateformes cloud, produits spécifiques aux fournisseurs |
| **DISA STIGs** | Defense Information Systems Agency | Environnements haute sécurité, alignement gouvernemental |
| **Référentiels NIST** | NIST SP 800-53, SP 800-128 | Alignement sur les cadres, recommandations complémentaires |

Lorsque plusieurs normes existent pour un type d'actif, l'organisation sélectionne celle qui est la plus appropriée à son profil de risque et documente le raisonnement de sélection.

### Mise en œuvre du durcissement

Tous les systèmes de production sont durcis avant déploiement. Le durcissement comprend, au minimum :

- **Supprimer ou désactiver les services, ports et protocoles inutiles** (principe de fonctionnalité minimale — NIST CM-7).
- **Supprimer ou désactiver les comptes par défaut** ou modifier tous les mots de passe par défaut.
- **Désactiver les fonctionnalités inutiles** et les composants logiciels.
- **Configurer l'authentification** conformément à la politique d'authentification de l'organisation.
- **Activer la journalisation et les pistes d'audit** pour les événements liés à la sécurité.
- **Appliquer les correctifs de sécurité courants** avant la mise en production.
- **Configurer le chiffrement** pour les données au repos et en transit si applicable.
- **Restreindre l'accès administrateur** au personnel autorisé avec AMF.

### Objectifs de conformité au durcissement

| Niveau d'actif | Contrôles de sécurité critiques | Conformité globale au durcissement | Lacunes acceptables |
|----------------|----------------------------------|-------------------------------------|---------------------|
| **Niveau 1 (Critique)** | 100 % | 95 % ou plus | 0 lacune critique |
| **Niveau 2 (Élevé)** | 95 % ou plus | 90 % ou plus | Moins de 5 lacunes critiques |
| **Niveau 3 (Moyen)** | 90 % ou plus | 80 % ou plus | Moins de 10 lacunes critiques |
| **Niveau 4 (Faible)** | 80 % ou plus | 70 % ou plus | Meilleur effort |

**Contrôles de sécurité critiques** : Application de l'authentification, paramètres de chiffrement, configuration de la journalisation, application du contrôle d'accès et actualité des correctifs.

### Vérification du durcissement

La conformité au durcissement est vérifiée par des analyses périodiques :

| Niveau d'actif | Fréquence d'analyse automatisée | Vérification manuelle (si automatisation indisponible) |
|----------------|----------------------------------|-------------------------------------------------------|
| **Niveau 1 (Critique)** | Trimestriel | Semestriel |
| **Niveau 2 (Élevé)** | Semestriel | Annuel |
| **Niveaux 3/4 (Moyen/Faible)** | Annuel | Annuel |

Les outils de vérification peuvent comprendre : OpenSCAP, Nessus, Qualys, Tenable, outils de conformité natifs cloud (par exemple AWS Security Hub, Azure Defender for Cloud) ou plateformes équivalentes.

Les résultats d'analyse et les rapports de conformité sont conservés pendant un minimum de **3 ans** à des fins d'audit.

### Remédiation des lacunes

Les lacunes de durcissement identifiées par la vérification sont remédiées en fonction du risque :

| Risque de la lacune | Délai de remédiation | Approbation des exceptions |
|---------------------|----------------------|-----------------------------|
| **Critique** | Moins de 30 jours | RSSI uniquement |
| **Élevé** | Moins de 90 jours | RSSI ou Responsable des opérations informatiques |
| **Moyen** | Moins de 180 jours | Responsable des opérations informatiques |
| **Faible** | Meilleur effort | Responsable des opérations informatiques |

Les lacunes qui ne peuvent être remédiées en raison de contraintes techniques ou d'exigences métier sont documentées comme exceptions avec des contrôles compensatoires (voir Gestion des exceptions ci-dessous).

**Contrôles compensatoires pour les exceptions de durcissement** (exigences spécifiques) :

Scénario d'exception : Une recommandation de durcissement ne peut être mise en œuvre (par exemple impossible de désactiver un protocole hérité, de supprimer un compte par défaut, de corriger un composant vulnérable).

**Cadre de contrôles compensatoires** (défense en profondeur) :

Exemple 1 — Impossible de désactiver SMBv1 (dépendance d'application héritée) :
- Contrôles compensatoires :
  1. Isolation réseau : Système dans un VLAN isolé, règles de pare-feu bloquant SMB des réseaux non fiables.
  2. Restriction des accès : Seules des adresses IP de clients hérités spécifiques sont autorisées pour l'accès SMB (ACL).
  3. Supervision renforcée : Signatures IDS/IPS pour les tentatives d'exploitation SMBv1, alertes sur le trafic SMB inhabituel.
  4. Actualité des correctifs : S'assurer que tous les autres correctifs disponibles sont appliqués (même si SMBv1 ne peut être désactivé, appliquer MS17-010 et similaires).
  5. Plan de décommissionnement : Documenter le plan de migration depuis l'application héritée dans les 12 mois (l'exception n'est pas indéfinie).

Exemple 2 — Impossible de supprimer le compte administrateur par défaut (dépendance d'application codée en dur) :
- Contrôles compensatoires :
  1. Renommer le compte : Changer le nom de compte de « Administrateur » en un nom non évident.
  2. Mot de passe fort : Mot de passe aléatoire de 20+ caractères stocké dans [Coffre-fort de mots de passe].
  3. Application de l'AMF : Exiger l'AMF pour la connexion au compte.
  4. Supervision : Alerter sur toute utilisation du compte, journaliser toutes les actions.
  5. Rotation régulière du mot de passe : Tous les 90 jours.

Exemple 3 — Impossible de corriger un composant vulnérable (le fournisseur ne fournit plus de correctifs, décommissionnement planifié) :
- Contrôles compensatoires :
  1. Isolation réseau : Réseau isolé ou dédié.
  2. Désactiver l'accès à distance : Pas de RDP/SSH depuis l'extérieur du réseau isolé.
  3. Correctifs virtuels : Déployer une règle IPS pour bloquer les tentatives d'exploitation connues.
  4. Minimiser les données : Ne pas stocker de données CONFIDENTIELLES sur le système si possible.
  5. Calendrier de décommissionnement : Plan documenté pour remplacer le système dans les 6 mois.

**Évaluation de l'adéquation des contrôles compensatoires** :
- Les contrôles réduisent le risque à un niveau acceptable (appréciation du RSSI).
- Défense en profondeur : Minimum 3 contrôles compensatoires requis pour les lacunes Critiques/Élevées.
- Les contrôles doivent être vérifiables et auditables (pas simplement « nous ferons attention »).

**Documentation des exceptions** (dans le Registre des exceptions) :
- Recommandation de durcissement qui ne peut être satisfaite.
- Raison métier/technique (pourquoi la remédiation n'est pas possible).
- Évaluation des risques (quel est le risque de ne pas remédier).
- Contrôles compensatoires (spécifiques et mesurables).
- Approbation : Signature du RSSI.
- Fréquence de révision : Trimestrielle pour les lacunes Critiques, semestrielle pour les lacunes Élevées/Moyennes.
- Expiration : 12 mois maximum ; doit être rejustifiée si encore nécessaire.

**Métriques des exceptions** :
- Total des exceptions actives : Tendance à la baisse dans le temps.
- Exceptions de plus de 12 mois : Objectif 0 (nécessite une réapprobation ou une remédiation).
- Exceptions sans contrôles compensatoires adéquats : 0 (remédier ou renforcer les contrôles).

---

## Audit de la configuration

### Audits de configuration internes

L'organisation conduit des audits de configuration périodiques pour vérifier que :

- Les systèmes sont conformes aux configurations de référence approuvées.
- La documentation de la configuration est exacte et à jour.
- Les processus de contrôle des changements ont été respectés pour les changements de configuration.
- La couverture de la supervision satisfait aux objectifs définis.
- La conformité au durcissement satisfait aux seuils définis.

**Fréquence des audits** :

- **Annuel** : Audit complet de la configuration sur tous les niveaux d'actifs.
- **Trimestriel** : Audit ciblé des actifs de niveaux 1 et 2.
- **Ponctuel** : À la suite d'incidents significatifs, de changements technologiques majeurs ou de conclusions réglementaires.

### Preuves d'audit

Les audits de configuration produisent des preuves documentées comprenant :

- Résultats d'analyse de conformité aux configurations de référence.
- Enregistrements des changements de configuration pour la période d'audit.
- Rapports de détection de dérive et enregistrements de remédiation.
- Scores de conformité au durcissement par type d'actif.
- Revue du registre des exceptions.
- Évaluation de la couverture de la supervision.

Les résultats des audits sont communiqués au RSSI et intégrés dans le processus de revue de direction.

---

## Changements de configuration d'urgence

Les changements de configuration d'urgence sont principalement traités dans le cadre de la **Politique de gestion des changements (A.8.32)**. Les exigences spécifiques à la configuration pour les changements d'urgence comprennent :

- Le système est restauré dans un état de configuration documenté et reconnu valide aussi rapidement que possible.
- Si le changement d'urgence aboutit à un nouvel état de configuration (pas un retour à la configuration de référence), la configuration de référence est mise à jour via le processus d'approbation standard dans les **5 jours ouvrés**.
- Tous les changements de configuration d'urgence sont journalisés avec : les paramètres de configuration spécifiques modifiés, les valeurs précédentes, les nouvelles valeurs, la personne ayant effectué le changement et la justification métier.
- Une revue rétrospective par le RSSI ou son délégué intervient dans les **48 heures**.

Les changements de configuration d'urgence ne doivent pas dépasser **10 %** de l'ensemble des changements de configuration dans tout mois calendaire. Le dépassement de ce seuil déclenche une revue des processus.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Configuration de référence** | Ensemble documenté de paramètres de configuration de sécurité et opérationnels pour un type d'actif, servant de référence pour le déploiement, la vérification de la conformité et la détection de dérive |
| **Dérive de configuration** | Déviation de la configuration réelle d'un système par rapport à la configuration de référence approuvée, pouvant indiquer des changements non autorisés, des lacunes de processus ou des erreurs de documentation |
| **Élément de configuration (EC)** | Tout actif, service ou composant géré dans le cadre de la gestion de la configuration, suivi avec des attributs et relations définis |
| **BDGC** | Base de données de gestion des configurations — référentiel stockant les configurations de référence, les configurations d'actifs, l'historique des changements et les relations entre les éléments de configuration |
| **CIS Benchmark** | Guide de configuration de sécurité par consensus publié par le Center for Internet Security pour des plateformes et technologies spécifiques |
| **Image standardisée** | Image système préconfigurée mettant en œuvre la configuration de référence approuvée, utilisée pour un déploiement rapide et cohérent de nouveaux systèmes |
| **Durcissement** | Processus de sécurisation des configurations système en mettant en œuvre des normes de sécurité reconnues et en supprimant les services, comptes, ports et fonctionnalités inutiles |
| **Infrastructure en tant que code (IaC)** | Pratique de gestion des configurations de référence et du provisionnement de l'infrastructure via du code lisible par machine stocké dans le contrôle de version |
| **Fonctionnalité minimale** | Principe de configuration des systèmes pour ne fournir que les fonctionnalités requises pour leur objet |
| **Construction standard** | Configuration système approuvée, testée et documentée utilisée comme base pour déployer de nouvelles instances d'un type d'actif spécifique |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; autorité d'approbation des configurations de référence et des exceptions ; point d'escalade de la dérive ; supervision de la conformité au durcissement ; rapport à la Direction générale |
| **Responsable des opérations informatiques** | Opérations quotidiennes de gestion de la configuration ; maintenance du référentiel de configurations de référence ; coordination de la supervision ; rapport des métriques au RSSI |
| **Équipe sécurité** | Sélection et révision des normes de durcissement ; validation de la sécurité des configurations de référence ; enquête sur les alertes de dérive ; analyses de conformité ; support aux audits |
| **Propriétaires de systèmes** | Responsabilité de la conformité de configuration des systèmes détenus ; approbation des changements pour les systèmes détenus ; remédiation rapide de la dérive ; allocation des ressources pour le durcissement |
| **Administrateurs système / Ingénieurs DevOps** | Mise en œuvre des configurations de référence ; création et maintenance des images standardisées ; configuration de la supervision de la configuration ; exécution des changements approuvés ; tri et remédiation de la dérive |
| **Gestionnaire des changements / CCH** | Approbation des changements de configuration (normal et urgence) ; revue post-mise en œuvre ; suivi du succès des changements |
| **Auditeurs internes / externes** | Vérification indépendante de la conformité de la configuration ; revue des preuves ; rapport des conclusions |

---

## Preuves

Les éléments de preuve suivants démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Référentiel de configurations de référence** avec historique des versions, enregistrements d'approbation et dates de révision par type d'actif | Responsable des opérations informatiques | Maintenu en continu ; révisé annuellement (trimestriellement pour le niveau 1) | Durée de vie du type d'actif + 3 ans |
| 2 | **Inventaire des images standardisées** avec version, date de création, niveau de correctifs et enregistrements de validation | Administrateurs système / DevOps | Maintenu en continu ; actualisé mensuellement (niveaux 1/2) ou trimestriellement (niveaux 3/4) | Durée de vie de l'image + 1 an |
| 3 | **BDGC ou inventaire de configuration** indiquant les éléments de configuration, les configurations de référence appliquées et le statut de conformité actuel | Responsable des opérations informatiques | Maintenu en continu ; audité trimestriellement | Actif + 3 ans |
| 4 | **Enregistrements des changements de configuration** (demandes de changement, approbations, journaux de mise en œuvre, vérification post-changement) | Gestionnaire des changements | Par changement ; audité trimestriellement | 3 ans (7 ans pour les preuves d'audit) |
| 5 | **Rapports de détection de dérive** et journaux d'alertes avec résultats de tri, enregistrements de remédiation et résultats de vérification post-remédiation | Équipe sécurité / Opérations informatiques | Continu ; révisé mensuellement | 3 ans |
| 6 | **Résultats d'analyse de conformité au durcissement** par type d'actif indiquant le pourcentage de conformité et les lacunes identifiées | Équipe sécurité | Selon le programme d'analyse (trimestriel à annuel par niveau) | 3 ans |
| 7 | **Registre de remédiation des lacunes** avec description de la lacune, niveau de risque, responsable, date d'échéance, statut et preuve de clôture | Responsable des opérations informatiques | Maintenu en continu ; révisé mensuellement | Durée de la lacune + 3 ans |
| 8 | **Registre des exceptions** pour les dérogations de configuration (demande, justification, contrôles compensatoires, approbation, date d'expiration) | RSSI | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |
| 9 | **Rapports d'audit de configuration** (internes et externes) avec conclusions et mesures correctives | RSSI / Auditeurs | Annuel (complet) + trimestriel (ciblé) | 3 ans |
| 10 | **Enregistrements des changements de configuration d'urgence** avec justification, approbation, revue rétrospective et confirmation de mise à jour de la configuration de référence | RSSI | Par événement ; rétrospective dans les 48 heures | 3 ans |
| 11 | **Journaux d'accès et de changements du référentiel IaC** (historique des contributions, revues de demandes de fusion, enregistrements de déploiement) | DevOps / Opérations informatiques | Continu | 3 ans |
| 12 | **Rapport de couverture de supervision** indiquant le pourcentage d'actifs sous supervision automatisée de la configuration par niveau, incluant le statut du Registre des lacunes de supervision | Responsable des opérations informatiques | Mensuel | 1 an |
| 13 | **Preuves de conformité de configuration SOC 2** — Rapports trimestriels montrant que les systèmes de niveaux 1/2 satisfont aux configurations de référence de durcissement, avec exemples d'exports de configuration et résultats d'analyse | Équipe sécurité | Trimestriel avant l'audit SOC 2 | 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifie la conformité à la présente politique par diverses méthodes, notamment des évaluations de la couverture des configurations de référence, des rapports de supervision de la configuration, des analyses de conformité au durcissement, des enregistrements de détection et de remédiation de la dérive, des audits de documentation des changements, des audits internes et externes, et des retours au propriétaire de la politique.

**Métriques de conformité** :

| Métrique | Cible | Fréquence de mesure |
|----------|-------|---------------------|
| Types d'actifs de niveau 1 avec configurations de référence documentées et approuvées | 100 % | Trimestriel |
| Types d'actifs de niveau 2 avec configurations de référence documentées et approuvées | 100 % | Trimestriel |
| Types d'actifs de niveaux 3/4 avec configurations de référence documentées et approuvées | >= 80 % | Trimestriel |
| Actifs de niveaux 1 et 2 sous supervision automatisée de la configuration | >= 95 % | Mensuel |
| Alertes de dérive remédiées dans les délais | >= 90 % | Mensuel |
| Remédiations de dérive avec vérification post-remédiation complète | 100 % | Mensuel |
| Conformité au durcissement des contrôles de sécurité critiques (niveau 1) | >= 95 % | Trimestriel |
| Changements de configuration d'urgence en pourcentage de l'ensemble des changements | < 10 % | Mensuel |
| Conclusions d'audit de configuration clôturées dans les délais convenus | >= 90 % | Trimestriel |
| Images standardisées actualisées dans les délais (mensuel pour les niveaux 1/2, trimestriel pour les niveaux 3/4) | 100 % | Mensuel |
| Clôture des lacunes de supervision dans les délais par niveau | >= 90 % | Trimestriel |
| Exceptions de durcissement de plus de 12 mois | 0 | Trimestriel |

**Traitement des non-conformités** : Les métriques en dessous de 70 % nécessitent une escalade immédiate au RSSI et un plan de remédiation avec des délais définis. Les métriques entre 70 et 89 % nécessitent la supervision du Responsable des opérations informatiques avec des revues mensuelles des progrès. Les métriques à 90 % et au-dessus suivent la supervision trimestrielle standard.

## Exceptions

Toute exception à la présente politique est approuvée et enregistrée par le RSSI au préalable, avec acceptation des risques documentée, contrôles compensatoires et date d'expiration définie (maximum 12 mois). Les exceptions sont révisées trimestriellement et communiquées à l'équipe de revue de direction. Les exceptions expirées déclenchent une remédiation ou un renouvellement formel via le processus d'approbation standard.

## Non-conformité

Tout employé reconnu coupable d'avoir enfreint la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Effectuer des changements de configuration non autorisés dans des systèmes de production, désactiver des contrôles de sécurité, contourner la gestion des changements ou dissimuler une dérive de configuration constituent des violations graves.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions prennent en compte les évolutions des normes de durcissement industrielles (nouvelles versions de CIS Benchmarks, mises à jour des guides de sécurité des fournisseurs), les menaces et techniques d'attaque émergentes ciblant les erreurs de configuration, les évolutions technologiques (nouvelles plateformes, adoption de services cloud, conteneurisation), les évolutions réglementaires, les conclusions des audits et les enseignements tirés des incidents liés à la configuration.

---

# Domaines de la norme ISO 27001 couverts

Politique de gestion de la configuration — Correspondance des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 5.37 Procédures d'exploitation documentées |
| Clause 8.1 Planification et contrôle opérationnels | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | **8.9 Gestion de la configuration** |
| | 8.8 Gestion des vulnérabilités techniques |
| | 8.32 Gestion des changements |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles pour la sécurité des données ; la configuration sécurisée comme mesure technique fondamentale protégeant les systèmes traitant des données personnelles |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales de sécurité des données ; la gestion de la configuration soutient le contrôle d'accès, la journalisation et les exigences d'intégrité des systèmes |
| RGPD (le cas échéant) | Art. 32 — Sécurité du traitement ; la gestion sécurisée de la configuration comme mesure technique et organisationnelle appropriée |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.9 — Gestion de la configuration |
| ISO/IEC 27002:2022 | Section 8.9 — Recommandations de mise en œuvre pour la gestion de la configuration (nouveau contrôle dans l'édition 2022) |
| NIST SP 800-128 | Guide pour la gestion de la configuration axée sur la sécurité des systèmes d'information |
| NIST SP 800-53 Rév. 5 | CM-2 (Configuration de référence), CM-3 (Contrôle des changements de configuration), CM-6 (Paramètres de configuration), CM-7 (Fonctionnalité minimale), CM-8 (Inventaire des composants du système) |
| CIS Controls v8 | Contrôle 4 : Configuration sécurisée des actifs et logiciels d'entreprise (Mesures de sécurité 4.1–4.12) |
| CIS Benchmarks | Guides de durcissement spécifiques aux plateformes (Windows, Linux, macOS, plateformes cloud, équipements réseau, bases de données) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
