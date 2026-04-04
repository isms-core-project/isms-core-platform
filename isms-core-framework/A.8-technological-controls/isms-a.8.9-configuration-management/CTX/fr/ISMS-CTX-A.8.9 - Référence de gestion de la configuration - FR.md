<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-FR-configuration-management-reference:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 – Référence de gestion de la configuration**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence de gestion de la configuration |
| **Type de document** | Référence technique (NON SMSI) |
| **Identifiant du document** | ISMS-CTX-A.8.9 |
| **Créateur du document** | Responsable de la configuration |
| **Propriétaire du document** | Architecte de sécurité |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date] |
| **Classification** | Interne |
| **Statut** | Référence |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | Responsable de la configuration / Architecte de sécurité | Référence technique initiale extraite de la politique consolidée |

**Cycle de révision** : Semestriel ou lors de changements de normes/technologies
**Prochaine date de révision** : [Date + 6 mois]

**Autorité de révision** :

- Révision technique : Responsable de la configuration
- Révision sécurité : Architecte de sécurité
- AUCUNE approbation exécutive requise (NON SMSI)

---

## ⚠️ IMPORTANT : Statut du document

**CE DOCUMENT NE FAIT PAS PARTIE DU SMSI.**

**CE DOCUMENT NE DÉFINIT PAS D'EXIGENCES OBLIGATOIRES.**

**CE DOCUMENT N'ÉTABLIT PAS D'OBLIGATIONS CONTRAIGNANTES.**

**TOUTES LES EXIGENCES CONTRAIGNANTES SONT DÉFINIES DANS ISMS-POL-A.8.9.**

Il s'agit d'une référence technique et d'orientations opérationnelles à titre de sensibilisation et de soutien à la mise en œuvre uniquement.

**Objet** : Fournir une référence des normes techniques, des procédures de mise en œuvre et des orientations opérationnelles pour soutenir la mise en œuvre de la politique de gestion de la configuration. Ce document complète ISMS-POL-A.8.9 mais NE remplace PAS les exigences de politique.

**Public visé** : Responsables de configuration, administrateurs systèmes, ingénieurs DevOps, ingénieurs sécurité, personnel des opérations.

**Utilisation** : Référence pour les définitions de référentiels, les procédures de changement, la réponse aux dérives et les orientations opérationnelles rapides. Les organisations personnalisent ce contenu en fonction de leur pile technologique, de leurs outils et de leurs processus opérationnels spécifiques.

**Mises à jour** : Ce document peut être mis à jour plus fréquemment que les politiques SMSI pour refléter l'évolution des technologies, des nouveaux outils et des normes actualisées. Les mises à jour ne nécessitent pas d'approbation exécutive mais doivent être communiquées au personnel concerné.

---

## Partie 1 : Référence des normes de configuration

### Paysage des normes de durcissement

Le durcissement de la configuration applique des configurations axées sur la sécurité basées sur des normes sectorielles reconnues. [Organisation] sélectionne les normes applicables selon le type d'actif, les exigences réglementaires et l'évaluation des risques.

**1.1.1 CIS Benchmarks** (Center for Internet Security)

**Couverture** : Plus de 100 benchmarks couvrant plus de 25 familles de technologies

- Systèmes d'exploitation : Windows, Linux (RHEL, Ubuntu, SUSE), macOS, variantes Unix
- Plateformes cloud : AWS, Azure, GCP, Oracle Cloud
- Équipements réseau : Cisco, Palo Alto, Fortinet
- Bases de données : Oracle, SQL Server, PostgreSQL, MongoDB, MySQL
- Applications : Serveurs web, plateformes de conteneurs, Kubernetes

**Niveaux** :

- **Niveau 1** : Durcissement de référence pratique (impact opérationnel minimal)
- **Niveau 2** : Défense en profondeur (peut impacter la fonctionnalité)

**Obtention** : Téléchargement gratuit sur cisecurity.org (inscription requise)

**1.1.2 DISA STIGs** (Defense Information Systems Agency)

**Couverture** : Exigences de sécurité du département de la défense américain

- Systèmes d'exploitation : Windows, Linux, Unix
- Applications : Bases de données, serveurs web, serveurs d'applications
- Équipements réseau : Routeurs, commutateurs, pare-feu

**Classification** : CAT I (Critique), CAT II (Élevé), CAT III (Moyen)

**Obtention** : Téléchargement gratuit sur public.cyber.mil/stigs

**Utilisation** : Contractants gouvernementaux/de défense, environnements haute sécurité

**1.1.3 Guides de sécurité fournisseurs**

**Microsoft** :

- Windows Server Security Baseline
- Microsoft 365 Security Baseline
- Azure Security Baseline
- Security Compliance Toolkit

**Fournisseurs cloud** :

- AWS Security Best Practices
- Azure Security Benchmarks
- Google Cloud Security Foundations
- Oracle Cloud Security Posture Management

**Fournisseurs réseau** : Guides de sécurité Cisco, Palo Alto, Fortinet, Check Point

**1.1.4 Publications NIST**

- **NIST SP 800-53 Rév. 5** : Contrôles de sécurité et de confidentialité (famille CM)
- **NIST SP 800-128** : Gestion de la configuration axée sur la sécurité
- **NIST SP 800-70** : Programme national des listes de contrôle
- **NIST Cybersecurity Framework** : Gestion de la configuration dans la fonction PROTECT

**1.1.5 Normes supplémentaires**

- **BSI Grundschutz** : Office fédéral allemand pour la sécurité de l'information
- **Essential Eight** : Centre australien de cybersécurité
- **CMMC** : Modèle de maturité en cybersécurité (contractants de défense)
- **SWIFT CSC** : Contrôles de sécurité pour la messagerie financière

### Normes de configuration par type d'actif

**1.2.1 Systèmes d'exploitation**

**Windows Server** :

- **Norme principale** : CIS Windows Server Benchmark (spécifique à la version)
- **Complémentaire** : Microsoft Security Baselines, DISA STIG (haute sécurité)
- **Contrôles clés** :
  - Contrôle de compte utilisateur (UAC) activé
  - Pare-feu Windows activé avec règles restrictives
  - Journalisation d'audit pour l'authentification, l'utilisation des privilèges, l'accès aux objets
  - Politique de mots de passe : Minimum 14 caractères, complexité, verrouillage après 5 tentatives
  - Services désactivés : Spouleur d'impression (si non nécessaire), Bureau à distance (si non nécessaire)
  - Correctifs de sécurité : Installation mensuelle dans les 30 jours

**Linux/Unix** :

- **Norme principale** : CIS Benchmark spécifique à la distribution (RHEL, Ubuntu, SUSE, etc.)
- **Complémentaire** : DISA STIG (haute sécurité)
- **Contrôles clés** :
  - Connexion root désactivée (utiliser sudo)
  - Durcissement SSH (auth par clé, désactiver connexion root, désactiver protocole 1)
  - iptables/firewalld configuré avec refus par défaut
  - SELinux/AppArmor activé (mode enforcing)
  - Démon d'audit (auditd) activé et configuré
  - Permissions fichiers : /etc/passwd 644, /etc/shadow 000, /boot 700

**1.2.2 Équipements réseau**

**Pare-feu** (Palo Alto, Fortinet, Cisco ASA) :

- **Norme principale** : Guide de sécurité spécifique au fournisseur + CIS Benchmark
- **Contrôles clés** :
  - Politiques de refus par défaut
  - Ensembles de règles selon le moindre privilège
  - Journalisation activée pour toutes les décisions d'autorisation/refus
  - Accès admin restreint au VLAN de gestion
  - Authentification multifacteur (AMF) pour l'accès admin
  - Révision et nettoyage réguliers de la politique

**Routeurs/Commutateurs** (Cisco, Juniper, Arista) :

- **Norme principale** : CIS Network Device Benchmark
- **Contrôles clés** :
  - Contrôle d'accès console et VTY (SSH uniquement, pas de Telnet)
  - SNMP v3 ou désactivé
  - Authentification AAA
  - Journalisation vers un syslog centralisé
  - Synchronisation NTP
  - Ports inutilisés désactivés

**Équilibreurs de charge** :

- **Norme principale** : Guide de sécurité du fournisseur
- **Contrôles clés** :
  - TLS 1.2+ uniquement
  - Suites de chiffrement robustes
  - Validation des certificats
  - Configuration du délai d'expiration de session
  - Interface admin sur réseau de gestion

**1.2.3 Plateformes cloud**

**AWS** :

- **Norme principale** : CIS AWS Foundations Benchmark
- **Contrôles clés** :
  - IAM : AMF pour tous les utilisateurs, principe du moindre privilège, rotation régulière des clés d'accès
  - Journalisation : CloudTrail activé dans toutes les régions, journalisation des buckets S3, VPC Flow Logs
  - Surveillance : Alarmes CloudWatch pour les appels API non autorisés
  - Réseau : Groupes de sécurité VPC en refus par défaut, pas de buckets S3 publics (sauf si explicitement requis)
  - Chiffrement : Chiffrement EBS, chiffrement S3 au repos

**Azure** :

- **Norme principale** : CIS Microsoft Azure Foundations Benchmark
- **Contrôles clés** :
  - Identité : AMF activée, politiques d'accès conditionnel, PIM pour les rôles privilégiés
  - Journalisation : Conservation du journal d'activité ≥ 365 jours, Paramètres de diagnostic activés
  - Réseau : NSG en refus par défaut, pas de RDP/SSH depuis Internet
  - Chiffrement : Azure Disk Encryption, chiffrement du service de stockage

**Google Cloud Platform (GCP)** :

- **Norme principale** : CIS Google Cloud Platform Foundation Benchmark
- **Contrôles clés** :
  - IAM : Rotation des clés de compte de service, principe du moindre privilège
  - Journalisation : Cloud Audit Logs activés, sinks de journaux configurés
  - Réseau : Règles de pare-feu VPC restrictives, accès privé Google
  - Chiffrement : CMEK si requis, disques persistants chiffrés

**1.2.4 Bases de données**

**SQL Server** :

- **Norme principale** : CIS Microsoft SQL Server Benchmark, DISA STIG
- **Contrôles clés** :
  - Mode d'authentification Windows (pas le mode mixte)
  - Compte sa désactivé/renommé
  - Fonctionnalités inutiles désactivées (xp_cmdshell, OLE Automation, etc.)
  - SQL Server Audit activé
  - Chiffrement : TDE (Transparent Data Encryption), Always Encrypted pour les colonnes sensibles

**Oracle Database** :

- **Norme principale** : CIS Oracle Database Benchmark, DISA STIG
- **Contrôles clés** :
  - Politique de mots de passe robuste
  - Comptes par défaut verrouillés
  - Audit activé
  - Chiffrement : TDE, chiffrement réseau (Native Network Encryption)

**PostgreSQL/MySQL/MongoDB** :

- **Norme principale** : CIS Benchmark pour chacun
- **Contrôles clés** :
  - Authentification requise (pas d'accès anonyme)
  - Connexions SSL/TLS imposées
  - Permissions utilisateur selon le moindre privilège
  - Journalisation d'audit activée

**1.2.5 Conteneurs et orchestration**

**Docker** :

- **Norme principale** : CIS Docker Benchmark
- **Contrôles clés** :
  - Exécuter les conteneurs en tant qu'utilisateur non-root
  - Système de fichiers racine en lecture seule si possible
  - Limites de ressources (CPU, mémoire)
  - Profils AppArmor/SELinux
  - Analyse régulière des images pour les vulnérabilités

**Kubernetes** :

- **Norme principale** : CIS Kubernetes Benchmark
- **Contrôles clés** :
  - RBAC activé et configuré
  - Pod Security Standards appliqués
  - Politiques réseau définies
  - Gestion des secrets (magasin de secrets externe)
  - Authentification et autorisation du serveur API
  - Chiffrement etcd au repos

**1.2.6 Applications**

**Serveurs web** (Apache, Nginx, IIS) :

- **Norme principale** : CIS Benchmark pour chacun
- **Contrôles clés** :
  - Exécuter en tant qu'utilisateur non privilégié
  - Modules inutiles désactivés
  - Journalisation des accès activée
  - TLS 1.2+ uniquement, suites de chiffrement robustes
  - En-têtes de sécurité (HSTS, X-Frame-Options, CSP)

**Serveurs d'applications** (JBoss, WebLogic, Tomcat) :

- **Norme principale** : Guide de sécurité fournisseur + CIS Benchmark
- **Contrôles clés** :
  - Comptes par défaut supprimés
  - Interface de gestion sur réseau séparé
  - Journalisation d'audit activée
  - Services inutiles désactivés

### Arbre de décision pour la sélection des normes

```
DÉPART : Quelle norme de durcissement utiliser ?

├─ L'actif traite-t-il des données réglementées (PCI, HIPAA, etc.) ?
│  ├─ OUI → Utiliser en priorité la norme imposée par la réglementation
│  └─ NON → Continuer

├─ Existe-t-il un CIS Benchmark pour ce type d'actif ?
│  ├─ OUI → Utiliser le CIS Benchmark (Niveau 1 de référence, Niveau 2 haute sécurité)
│  └─ NON → Continuer

├─ Existe-t-il un guide de sécurité fournisseur ?
│  ├─ OUI → Utiliser le guide fournisseur
│  └─ NON → Continuer

├─ Le type d'actif est-il couvert par les lignes directrices NIST ?
│  ├─ OUI → Utiliser les contrôles NIST comme référence
│  └─ NON → Développer un référentiel personnalisé avec approbation de l'Architecte de sécurité

TOUJOURS : Documenter la sélection de norme dans la documentation du référentiel
```

### Méthodes de vérification

**Analyse automatisée** :

- **OpenSCAP** : Analyse de conformité CIS et STIG (Linux/Windows)
- **Nessus/Tenable** : Analyse de vulnérabilités et de conformité
- **Qualys** : Analyse de conformité basée dans le cloud
- **AWS Security Hub** : Conformité spécifique AWS (CIS AWS Benchmark)
- **Azure Security Center** : Conformité spécifique Azure
- **GCP Security Command Center** : Conformité spécifique GCP

**Vérification manuelle** :

- Réviser les fichiers de configuration par rapport au référentiel
- Exécuter des scripts de vérification de conformité
- Valider les contrôles de sécurité par des tests
- Documenter les constats et exceptions

**Conformité continue** :

- Intégrer les analyses dans les pipelines CI/CD
- Reporting automatisé dans les tableaux de bord récapitulatifs
- Alerte sur la dérive de conformité
- Réévaluation régulière (trimestrielle minimum)

---

## Partie 2 : Guide de mise en œuvre de la gestion des changements

### Modèle de formulaire de demande de changement

**Champs du formulaire de demande de changement** :

**Section 1 : Identification du changement**

- ID de la demande de changement : [Généré automatiquement ou CR-AAAA-####]
- Date de soumission : [JJ.MM.AAAA]
- Soumis par : [Nom, Département, Contact]
- Titre du changement : [Titre descriptif court, max 100 caractères]
- Classification du changement : [Standard / Normal / Urgence]
- Si Urgence, justification : [Pourquoi ne peut pas attendre le processus normal]

**Section 2 : Description du changement**

- Justification métier : [Pourquoi nécessaire ? Quel problème résolu ?]
- Description technique : [Qu'est-ce qui sera modifié précisément ?]
- Systèmes/Services concernés : [Lister tous les actifs impactés]
- Éléments de configuration (CI) : [Numéros CI CMDB si applicable]

**Section 3 : Évaluation de l'impact**

- Impact utilisateurs : [Aucun / Minimal / Modéré / Significatif / Grave]
- Indisponibilité de service requise : [Aucune / < 1h / 1-4h / 4-8h / > 8h]
- Niveau de risque : [Faible / Moyen / Élevé / Critique]
- Dépendances : [Autres systèmes, services, équipes impactés]

**Section 4 : Plan de mise en œuvre**

- Étapes de mise en œuvre : [Procédure détaillée étape par étape]
- Date/Heure de mise en œuvre : [JJ.MM.AAAA HH:MM]
- Durée de mise en œuvre : [Durée estimée]
- Équipe de mise en œuvre : [Noms et rôles]
- Ressources requises : [Outils, accès, soutien fournisseur nécessaires]

**Section 5 : Tests et validation**

- Environnement de test : [Dev / Test / Préproduction / UAT]
- Date des tests : [JJ.MM.AAAA]
- Résultats des tests : [Réussi / Échoué / Partiel]
- Preuves des tests : [Lien vers la documentation de test]
- Critères de succès : [Comment déterminer si le changement est réussi]

**Section 6 : Plan de retour arrière**

- Critères de déclenchement du retour arrière : [Quand exécuter le retour arrière]
- Procédure de retour arrière : [Instructions étape par étape]
- Durée du retour arrière : [Durée estimée]
- Sauvegarde vérifiée : [Oui / Non / N/A]
- Retour arrière testé : [Oui / Non / N/A — date si testé]

**Section 7 : Communication**

- Utilisateurs à notifier : [Liste de distribution]
- Méthode de communication : [E-mail / Portail / Annonce]
- Calendrier de notification : [Avant / Pendant / Après le changement]

**Section 8 : Approbations**

- Révision technique : [Nom, Rôle, Décision, Date, Commentaires]
- Révision sécurité : [Nom, Rôle, Décision, Date, Commentaires]
- Décision du CAC : [Approuvé / Approuvé sous conditions / Refusé / Reporté]
- Date du CAC : [JJ.MM.AAAA]
- Conditions : [Toute condition d'approbation]

**Section 9 : Revue post-mise en œuvre**

- Date/Heure réelle de mise en œuvre : [JJ.MM.AAAA HH:MM]
- Statut de mise en œuvre : [Réussi / Réussi avec problèmes / Échoué / Retour arrière effectué]
- Problèmes rencontrés : [Description]
- Résolution : [Comment les problèmes ont été résolus]
- Enseignements tirés : [Ce qui pourrait être amélioré]

### Procédures de réunion du CAC

**Avant la réunion (responsabilités du Président du CAC)** :

- Distribuer les demandes de changement 48 heures avant la réunion
- S'assurer que toutes les approbations requises ont été obtenues
- Pré-sélectionner les dossiers pour vérifier leur complétude (rejeter les dossiers incomplets)
- Publier l'ordre du jour de la réunion

**Pendant la réunion** :

- Réviser chaque demande de changement normal
- Évaluer le risque et l'impact
- Vérifier les plans de tests et de retour arrière
- Prioriser en cas de conflits de ressources
- Prendre la décision d'approbation (Approuvé / Approuvé sous conditions / Refusé / Reporté)
- Documenter la décision et la justification

**Après la réunion** :

- Publier le procès-verbal dans les 24 heures
- Notifier les demandeurs de changement des décisions
- Mettre à jour le système de gestion des changements
- Planifier la prochaine réunion

**Fréquence des réunions du CAC** : Hebdomadaire ou bimensuelle selon le volume de changements.

### Catalogue des changements standard

Les changements standard sont pré-approuvés par le CAC et exécutables sans révision individuelle. Exemples :

**Réinitialisations de mots de passe** :

- Procédure : Suivre la procédure de vérification d'identité, réinitialiser dans AD/IAM
- Risque : Faible
- Tests : N/A
- Retour arrière : L'utilisateur peut réinitialiser à nouveau si nécessaire

**Renouvellements de certificats** :

- Procédure : Générer une CSR, soumettre à l'AC, installer le nouveau certificat
- Risque : Faible (si mêmes paramètres que le certificat expirant)
- Tests : Vérifier la chaîne de certificats et la date d'expiration
- Retour arrière : Revenir au certificat précédent (si encore valide)

**Correctifs logiciels standard** :

- Procédure : Installer depuis la liste des correctifs approuvés en test, puis en production
- Risque : Faible (correctifs de la liste des fournisseurs approuvés)
- Tests : Requis en environnement de test
- Retour arrière : Désinstaller le correctif ou restaurer depuis une sauvegarde

**Création/suppression de comptes utilisateurs** :

- Procédure : Suivre le processus d'entrée/sortie
- Risque : Faible
- Tests : Vérifier les accès et les permissions
- Retour arrière : Désactiver le compte (suppression), supprimer le compte (création)

Les organisations maintiennent leur propre Catalogue des changements standard selon leurs besoins opérationnels et leur appétit au risque.

### Procédures de changement d'urgence

**Quand utiliser le processus de changement d'urgence** :

- Exploit de sécurité actif (vulnérabilité en cours d'exploitation active)
- Interruption de service critique affectant les opérations métier
- Confinement d'une violation de données
- Violation critique de conformité nécessitant une remédiation immédiate

**Quand NE PAS utiliser** :

- Mauvaise planification (« oublié de soumettre la demande de changement »)
- Commodité (« ne veux pas attendre le CAC »)
- Pression du fournisseur (« le fournisseur dit que cela doit être fait maintenant »)

**Flux du changement d'urgence** :

1. **Approbation verbale immédiate** : Contacter le DSI, le RSSI ou le Président du CAC par téléphone
2. **Documenter la justification** : Dans l'heure, envoyer un e-mail documentant la justification d'urgence
3. **Mettre en œuvre le changement** : Exécuter le changement sous supervision (règle des deux personnes si possible)
4. **Documenter la mise en œuvre** : Dans les 24 heures, compléter le formulaire de demande de changement avec les étapes réelles effectuées
5. **Révision rétrospective du CAC** : Dans les 5 jours ouvrables, présenter au CAC pour révision

**Résultats de la révision rétrospective du CAC** :

- **Approuvé** : Urgence justifiée, changement approprié
- **Approuvé avec remédiation** : Urgence justifiée, mais améliorations de processus nécessaires
- **Refusé** : Urgence non justifiée, retour arrière requis ou mesure disciplinaire

---

## Partie 3 : Procédures de réponse aux dérives de configuration

### Détection et triage des dérives

**Étape 1 : Réception de l'alerte**

- L'outil de surveillance de la configuration génère une alerte de dérive
- Alerte acheminée vers le Responsable de la configuration et le Propriétaire du système
- L'alerte contient : ID de l'actif, changement détecté, valeur attendue du référentiel, valeur réelle, horodatage de détection

**Étape 2 : Triage initial** (dans 1 à 4 heures selon la gravité)

- Le Responsable de la configuration révise les détails de l'alerte
- Vérifie le système de gestion des changements pour les changements autorisés
- Classe la dérive : Autorisée, Non autorisée ou Faux positif

**Étape 3 : Décision de classification**

**Dérive autorisée** : Le changement a été approuvé mais le référentiel n'a pas encore été mis à jour

- Action : Mettre à jour la documentation du référentiel, mettre à jour la CMDB avec la nouvelle configuration, clôturer le ticket d'incident

**Dérive non autorisée** : Changement non approuvé ou inconnu

- Action : Procéder à l'investigation (Étape 4)

**Faux positif** : Mauvaise configuration de l'outil de surveillance ou erreur dans le référentiel

- Action : Ajuster la règle de surveillance, mettre à jour le référentiel si incorrect, clôturer le ticket d'incident

**Étape 4 : Investigation d'une dérive non autorisée**

- Réviser les journaux système pour déterminer qui/quoi a effectué le changement
- Déterminer l'horodatage du changement
- Évaluer si le changement est malveillant ou une erreur opérationnelle
- Classifier la gravité (Critique / Élevée / Moyenne / Faible)

**Étape 5 : Réponse aux incidents** (si malveillant)

- Escalader vers le SOC (Centre des Opérations de Sécurité)
- Suivre les procédures de réponse aux incidents (ISMS-POL-A.5.24)
- Préserver les preuves
- Contenir la menace

**Étape 6 : Remédiation** (si erreur opérationnelle)

- Revenir à la configuration de référence
- Documenter les actions de remédiation
- Effectuer une analyse des causes profondes
- Mettre en œuvre des mesures préventives
- Clôturer le ticket d'incident

### Processus de demande d'exception

**Quand demander une exception** :

- Le contrôle de durcissement du référentiel n'est pas techniquement faisable
- L'exigence métier est en conflit avec le référentiel de sécurité
- La limitation du produit fournisseur empêche une conformité totale
- Une exception temporaire est nécessaire pendant une migration/un projet

**Procédure de demande d'exception** :

**Étape 1 : Compléter le formulaire de demande d'exception**

- Système/Actif nécessitant l'exception
- Contrôle(s) du référentiel nécessitant une exception
- Justification métier (pourquoi l'exception est nécessaire)
- Évaluation des risques (quel risque l'exception introduit)
- Contrôles compensatoires (comment le risque est atténué)
- Durée demandée (maximum 12 mois)
- Plan pour atteindre la pleine conformité (si temporaire)

**Étape 2 : Révision sécurité**

- L'Architecte de sécurité révise la demande
- Valide l'évaluation des risques
- Vérifie l'adéquation des contrôles compensatoires
- Recommande l'approbation/le refus

**Étape 3 : Décision d'approbation**

- Autorité d'exception selon le niveau de risque (conformément à ISMS-POL-A.8.9 Section 2.5.4)
- Critique : RSSI uniquement
- Élevé : Responsable de la configuration + Architecte de sécurité
- Moyen/Faible : Responsable de la configuration

**Étape 4 : Suivi des exceptions**

- Ajouter au registre des exceptions
- Définir la date d'expiration
- Planifier la révision avant expiration
- Surveiller les contrôles compensatoires

**Étape 5 : Révision des exceptions**

- 30 jours avant expiration, notification du Propriétaire du système
- Options : Renouveler l'exception, atteindre la pleine conformité, accepter le risque et documenter
- Le renouvellement nécessite le même processus d'approbation

---

## Partie 4 : Référence rapide

### Dois-je soumettre une demande de changement ?

**OUI — Demande de changement requise** :

- Modification des règles de pare-feu
- Changement des configurations système (OS, application, réseau)
- Installation de nouveaux logiciels
- Mise à niveau de versions de logiciels
- Modification des paramètres de sécurité
- Ajout/suppression de services
- Changements réseau (routage, VLANs, ACL)
- Mises à jour des référentiels

**NON — Demande de changement NON requise** :

- Réinitialisations de mots de passe (changement standard)
- Renouvellements de certificats (changement standard — si mêmes paramètres)
- Correctifs de routine depuis la liste approuvée (changement standard)
- Alertes/notifications de surveillance
- Lecture des fichiers de configuration

**En cas de doute** : Contacter le Responsable de la configuration.

### Arbre de décision pour la classification des changements

```
DÉPART : De quel type de changement s'agit-il ?

├─ Est-ce une procédure répétable, pré-approuvée et à faible risque ?
│  └─ OUI → CHANGEMENT STANDARD (pré-approuvé, suivre la procédure)

├─ Est-ce un incident de sécurité urgent ou une panne critique ?
│  └─ OUI → CHANGEMENT D'URGENCE (approbation accélérée)

├─ Tout le reste
   └─ CHANGEMENT NORMAL (approbation du CAC requise)

Si CHANGEMENT NORMAL, quel est le niveau de risque ?

├─ Périmètre limité, système unique, retour arrière facile
│  └─ FAIBLE RISQUE → Approbation à un niveau

├─ Systèmes multiples, impact modéré, procédure standard
│  └─ RISQUE MOYEN → Approbation à deux niveaux

├─ Organisation entière, systèmes critiques, complexe/non testé
   └─ RISQUE ÉLEVÉ → Approbation à trois niveaux (CAC)
```

### Qui approuve quoi ?

| Risque du changement | Approbateur(s) | Délai |
|---------------------|---------------|-------|
| **Standard** | Pré-approuvé (suivre la procédure) | Immédiat |
| **Normal — Faible** | Responsable technique / Propriétaire du système | 1-2 jours |
| **Normal — Moyen** | Responsable technique + Propriétaire du service | 3-5 jours |
| **Normal — Élevé** | CAC (3 niveaux) | 5-10 jours |
| **Urgence** | DSI ou RSSI (verbal) | < 4 heures |

### Coordonnées

**Responsable de la configuration** : [Nom], [E-mail], [Téléphone]
**Président du CAC** : [Nom], [E-mail], [Téléphone]
**Architecte de sécurité** : [Nom], [E-mail], [Téléphone]
**SOC (Centre des Opérations de Sécurité)** : [E-mail], [Téléphone], [Permanence]

**Calendrier des réunions du CAC** : [Jour/Heure], [Lien réunion/Lieu]
**Contact d'urgence** : [Permanence 24h/24 7j/7]

### FAQ

**Q : Ma demande de changement a été refusée. Que faire ?**
R : Réviser le motif du refus, répondre aux préoccupations du CAC, soumettre à nouveau avec les mises à jour.

**Q : Puis-je contourner le contrôle des changements pour des besoins métier urgents ?**
R : Non. Utiliser le processus de changement d'urgence avec la justification appropriée et la révision rétrospective.

**Q : Comment trouver le bon référentiel pour mon système ?**
R : Rechercher dans le Référentiel de configuration par système d'exploitation et rôle. Si non trouvé, contacter le Responsable de la configuration.

**Q : J'ai reçu une alerte de dérive pour un changement autorisé. Que faire ?**
R : Vérifier que le changement était autorisé, mettre à jour la documentation du référentiel, clôturer l'incident.

**Q : Mon système ne peut pas satisfaire au référentiel en raison de limitations fournisseur. Quelles sont mes options ?**
R : Demander une exception formelle avec contrôles compensatoires, ou contacter le fournisseur pour une solution de contournement/mise à niveau.

**Q : À quelle fréquence dois-je vérifier mes systèmes par rapport aux référentiels ?**
R : La surveillance automatisée vérifie en continu. Révisions manuelles : Niveau 1 (mensuelle), Niveau 2 (trimestrielle), Niveau 3 (semestrielle), Niveau 4 (annuelle).

---

## Annexe : Mises à jour du document

Cette référence technique peut être mise à jour plus fréquemment que les politiques SMSI pour refléter :

- Nouvelles normes de durcissement (mises à jour des CIS Benchmarks, nouveaux DISA STIGs)
- Changements technologiques (nouveaux services cloud, plateformes de conteneurs)
- Évolution du paysage des outils (nouveaux outils de surveillance/analyse)
- Améliorations procédurales (enseignements tirés de l'expérience opérationnelle)

Les mises à jour sont communiquées via les canaux de communication de [Organisation] et ne nécessitent pas d'approbation exécutive.

**Dernière mise à jour** : [Date]
**Prochaine révision prévue** : [Date + 6 mois]

---

**FIN DU DOCUMENT DE RÉFÉRENCE TECHNIQUE**

*Pour les exigences de politique contraignantes, consulter ISMS-POL-A.8.9 Politique de gestion de la configuration.*

<!-- QA_VERIFIED: 2026-04-02 -->
