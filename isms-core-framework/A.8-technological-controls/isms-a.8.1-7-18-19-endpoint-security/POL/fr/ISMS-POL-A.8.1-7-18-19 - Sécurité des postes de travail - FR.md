<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.1-7-18-19-FR:framework:POL:a.8.1-7-18-19 -->
**ISMS-POL-A.8.1-7-18-19 – Sécurité des postes de travail**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité des postes de travail |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.1-7-18-19 |
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
| 1.0 | [Date] | RSSI / Responsable sécurité des postes de travail | Cadre initial – Contrôles combinés A.8.1, A.8.7, A.8.18, A.8.19 |

**Cycle de révision** : Annuel (ou lors de changements organisationnels, réglementaires ou technologiques significatifs)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur des Systèmes d'Information (DSI) ou Directeur informatique
- Revue technique : Responsable des opérations IT / Responsable de la gestion des postes de travail
- Conformité : Responsable juridique/conformité (alignement réglementaire)
- Autorité finale : Direction générale (PDG)

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.1-7-18-19-S1-UG/TG (Processus de découverte des terminaux)
- ISMS-IMP-A.8.1-7-18-19-S2-UG/TG (Déploiement de la protection contre les logiciels malveillants)
- ISMS-IMP-A.8.1-7-18-19-S3-UG/TG (Processus de contrôle des logiciels)
- ISMS-IMP-A.8.1-7-18-19-S4-UG/TG (Gestion des utilitaires privilégiés)
- ISMS-POL-A.5.9 (Inventaire des actifs)
- ISMS-POL-A.8.2 (Droits d'accès privilégiés)
- ISMS-POL-A.8.8 (Gestion des vulnérabilités)
- ISMS-POL-A.8.15 (Journalisation)
- ISMS-POL-A.8.16 (Activités de surveillance)
- ISMS-POL-A.8.20-22 (Sécurité des réseaux)
- ISO/IEC 27001:2022 Contrôles A.8.1, A.8.7, A.8.18, A.8.19

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de sécurité des postes de travail, mettant en œuvre les Contrôles ISO/IEC 27001:2022 A.8.1 (Appareils utilisateurs), A.8.7 (Protection contre les logiciels malveillants), A.8.18 (Utilisation des programmes utilitaires privilégiés) et A.8.19 (Installation de logiciels sur les systèmes opérationnels) sous forme de cadre de sécurité unifié.

**Périmètre** : Cette politique s'applique à tous les terminaux utilisateurs, quel que soit leur type (ordinateurs portables, ordinateurs de bureau, appareils mobiles, tablettes, objets connectés), leur système d'exploitation (Windows, macOS, Linux, iOS, Android, ChromeOS) ou leur modèle de propriété (équipement d'entreprise, BYOD, contractant, invité).

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de sécurité des postes de travail. Cette politique établit QUELS contrôles de sécurité sont requis, QUAND ils doivent être mis en œuvre et QUI en est responsable. Les procédures de mise en œuvre (COMMENT les contrôles sont mis en place) sont documentées séparément dans ISMS-IMP-A.8.1-7-18-19 (variantes UG/TG).

**Justification du cadre de contrôles combinés** : Les contrôles A.8.1 (terminaux), A.8.7 (protection contre les logiciels malveillants), A.8.18 (utilitaires privilégiés) et A.8.19 (installation de logiciels) sont mis en œuvre sous la forme d'un cadre unifié car ils opèrent sur la même infrastructure de postes de travail, les activités de découverte servent les quatre contrôles, les preuves d'évaluation se recoupent significativement, et la sécurité des postes de travail nécessite une mise en œuvre holistique.

**Indépendance dans la Déclaration d'applicabilité** : Malgré une mise en œuvre et une documentation unifiées, les Contrôles A.8.1, A.8.7, A.8.18 et A.8.19 sont évalués indépendamment dans la Déclaration d'applicabilité (DdA). Chaque contrôle conserve des exigences distinctes, une collecte de preuves et une notation de conformité à des fins d'audit.

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Alignement sur les contrôles ISO/IEC 27001:2022

Cette politique fournit la gouvernance organisationnelle pour quatre contrôles couvrant l'ensemble de l'écosystème de sécurité des postes de travail :

### A.8.1 — Appareils utilisateurs

> *Les informations stockées, traitées ou accessibles par les appareils utilisateurs doivent être protégées.*

**Objectif du contrôle** : S'assurer que les informations sur les terminaux utilisateurs sont protégées contre les risques liés à leur utilisation, notamment la perte, le vol, l'accès non autorisé, l'infection par des logiciels malveillants et les configurations insuffisantes.

**Cette politique traite** (A.8.1) :

- L'inventaire des terminaux et la gestion des actifs
- La classification et la criticité des terminaux
- Les exigences de référence de sécurité par type de terminal et modèle de propriété
- Les exigences de chiffrement des données au repos
- Les exigences de gestion et d'enrôlement des terminaux (MDM, agents)
- La réponse aux terminaux perdus ou volés
- Les exigences de mise au rebut sécurisée
- Les exigences de sécurité et de protection de la vie privée du programme BYOD

### A.8.7 — Protection contre les logiciels malveillants

> *Une protection contre les logiciels malveillants doit être mise en œuvre et soutenue par une sensibilisation appropriée des utilisateurs.*

**Objectif du contrôle** : Assurer la détection, la prévention et la récupération après des attaques de logiciels malveillants grâce à des contrôles techniques et à la sensibilisation des utilisateurs.

**Cette politique traite** (A.8.7) :

- Les exigences de solution anti-logiciels malveillants / EDR et les capacités de détection
- Les exigences de couverture sur l'ensemble des terminaux
- La protection en temps réel et les exigences d'analyse
- Les exigences de mise à jour des signatures/définitions
- La mise en quarantaine et les exigences de remédiation
- La réponse aux incidents de logiciels malveillants
- Les exigences de sensibilisation des utilisateurs

### A.8.18 — Utilisation des programmes utilitaires privilégiés

> *L'utilisation de programmes utilitaires susceptibles de passer outre les contrôles du système et des applications doit être restreinte et étroitement contrôlée.*

**Objectif du contrôle** : S'assurer que les utilitaires privilégiés susceptibles de contourner les contrôles de sécurité sont identifiés, réservés aux utilisateurs autorisés, utilisés de manière appropriée, et que leur utilisation est surveillée et journalisée.

**Cette politique traite** (A.8.18) :

- L'identification et l'inventaire des utilitaires privilégiés
- Les exigences de contrôle d'accès aux utilitaires privilégiés
- Les exigences de flux d'approbation pour l'accès privilégié
- Les exigences de surveillance et de journalisation de l'utilisation
- La gestion des outils susceptibles de contourner les contrôles de sécurité

### A.8.19 — Installation de logiciels sur les systèmes opérationnels

> *Des procédures et des mesures doivent être mises en œuvre pour gérer de manière sécurisée l'installation de logiciels sur les systèmes opérationnels.*

**Objectif du contrôle** : S'assurer que les installations de logiciels sur les systèmes opérationnels sont contrôlées, autorisées et n'introduisent pas de vulnérabilités de sécurité ni de logiciels malveillants.

**Cette politique traite** (A.8.19) :

- Les exigences relatives à la liste des logiciels autorisés
- Les exigences relatives au processus d'approbation des logiciels
- Les exigences d'intégration dans la gestion des changements
- La détection et la suppression des logiciels non autorisés
- Les exigences relatives aux technologies de contrôle des applications
- Les exigences de gestion des vulnérabilités logicielles
- Les exigences de contrôle des logiciels BYOD

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de contrôle de sécurité des postes de travail alignées sur la classification des données, l'appétit au risque organisationnel et les obligations réglementaires
- **Établit** le cadre de gouvernance pour la prise de décision et la responsabilisation en matière de sécurité des postes de travail
- **Précise** les exigences de mise en œuvre des contrôles obligatoires (CE QUI doit être mis en œuvre)
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00
- **Identifie** les rôles et responsabilités organisationnels pour la gouvernance de la sécurité des postes de travail
- **Fournit** un cadre pour la gestion des exceptions et des incidents

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les procédures de mise en œuvre techniques** (voir ISMS-IMP-A.8.1-7-18-19)
- **Définit pas les méthodes spécifiques de découverte des terminaux** (voir ISMS-IMP-A.8.1-7-18-19-S1)
- **Répertorie pas les configurations de référence de sécurité** (voir ISMS-IMP-A.8.1-7-18-19-S1)
- **Fournit pas les procédures de déploiement anti-logiciels malveillants** (voir ISMS-IMP-A.8.1-7-18-19-S2)
- **Détaille pas les flux d'approbation des logiciels** (voir ISMS-IMP-A.8.1-7-18-19-S3)
- **Précise pas les contrôles d'accès aux utilitaires privilégiés** (voir ISMS-IMP-A.8.1-7-18-19-S4)
- **Sélectionne pas les technologies ou fournisseurs spécifiques** (sélection basée sur l'évaluation des risques de [Organisation])
- **Remplace pas l'évaluation des risques** (contrôles sélectionnés selon les décisions de traitement des risques de [Organisation])

## Périmètre

**Cette politique s'applique à** :

**Types de terminaux** :

- Ordinateurs portables et ordinateurs de bureau (équipements d'entreprise et BYOD, tous systèmes d'exploitation)
- Appareils mobiles (smartphones et tablettes — iOS, Android, autres systèmes mobiles)
- Terminaux spécialisés (clients légers, Chromebooks, bornes, terminaux de point de vente)
- Objets connectés stockant, traitant ou accédant aux informations organisationnelles
- Infrastructure de bureau virtuel (composants de sécurité côté client VDI/DaaS)

**Systèmes d'exploitation** :

- Windows (Windows 10, Windows 11, Windows Server pour les cas d'utilisation en postes de travail)
- macOS (macOS 12 Monterey et versions ultérieures)
- Linux (Ubuntu, Red Hat, CentOS, Debian et autres distributions)
- iOS (iOS 15 et versions ultérieures)
- Android (Android 11 et versions ultérieures)
- ChromeOS et autres systèmes d'exploitation utilisés sur les terminaux utilisateurs

**Modèles de propriété** :

- Équipements d'entreprise : appareils achetés et gérés par [Organisation]
- BYOD : appareils personnels utilisés à des fins professionnelles
- Appareils de contractants : appareils appartenant à des contractants, consultants, personnel temporaire
- Appareils invités : appareils de visiteurs temporaires avec accès limité
- Appareils de laboratoire/test : terminaux de développement, test et assurance qualité

**Personnel** :

- Employés (temps plein, temps partiel, temporaires)
- Contractants et consultants
- Fournisseurs tiers ayant accès aux terminaux
- Invités et visiteurs (scénarios d'accès limité)

**Emplacements réseau** :

- Sur site (bureaux, centres de données, salles de conférence)
- Distants/domicile (postes de travail en télétravail)
- Mobiles (employés en déplacement, personnel terrain)
- Sites secondaires et antennes
- Sites clients et emplacements tiers

## Hors périmètre

Cette politique ne couvre **pas** les domaines suivants (couverts par des politiques SMSI distinctes) :

- **Infrastructure serveur** : couverte par les politiques de sécurité et de durcissement des serveurs
- **Infrastructure réseau** : couverte par ISMS-POL-A.8.20-22 (Sécurité des réseaux)
- **Infrastructure cloud** : couverte par ISMS-POL-A.5.23 (Sécurité des services cloud)
- **Sécurité physique** : couverte par ISMS-POL-A.7.x (Sécurité physique et environnementale)
- **Gestion des identités et des accès** : couverte par ISMS-POL-A.5.15-16-18 (IAM)
- **Classification et traitement des données** : couverte par ISMS-POL-A.5.12-13

## Neutralité technologique

Cette politique est **entièrement neutre vis-à-vis des technologies** :

- Compatible avec toute plateforme de gestion des terminaux (Intune, Jamf, SCCM, Google Workspace MDM, VMware Workspace ONE, etc.)
- Supportée par tout fournisseur anti-logiciels malveillants/EDR (CrowdStrike, Microsoft Defender, SentinelOne, Carbon Black, etc.)
- Adaptable à toute technologie de contrôle des applications (AppLocker, Gatekeeper, solutions de liste d'autorisation)
- Compatible avec toute solution de PAM (Gestion des Accès Privilégiés)
- Les décisions de sélection des fournisseurs sont distinctes du cadre politique
- Les principes et exigences demeurent constants quelle que soit la technologie

## Applicabilité réglementaire

Les exigences réglementaires sont catégorisées conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**.

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés |
|----------------|---------------|----------------|
| **nLPD suisse** | Toutes les opérations suisses | Art. 8 – Mesures techniques et organisationnelles appropriées pour la protection des données |
| **RGPD de l'UE** | Lors du traitement de données personnelles de l'UE | Art. 32 – Mesures de sécurité incluant chiffrement, contrôles d'accès, protection contre les logiciels malveillants |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôles A.8.1, A.8.7, A.8.18, A.8.19 |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Condition de déclenchement | Exigences de sécurité des terminaux |
|---------------|---------------------------|-------------------------------------|
| **PCI DSS v4.0.1** | Traitement de données de cartes de paiement | Sécurité des terminaux accédant aux données de titulaires de cartes (Exig. 2, 5, 6, 10, 11) |
| **FINMA** | Établissement financier réglementé en Suisse | Mesures techniques et organisationnelles selon évaluation des risques |
| **DORA** | Entité de services financiers UE | Gestion des risques TIC incluant les contrôles de sécurité des terminaux |
| **NIS2** | Entité essentielle/importante (UE) | Mesures de sécurité pour les systèmes d'information incluant les terminaux |

**Niveau 3 : Référence informative**

- NIST Cybersecurity Framework 2.0
- NIST SP 800-53 Rév. 5
- CIS Controls v8.1 (Contrôles 1, 2, 4, 5, 7, 10, 16)
- Framework MITRE ATT&CK

---

# Cadre des exigences de sécurité des postes de travail

## Sécurité des terminaux (A.8.1)

**Objectif** : Protéger les informations stockées sur, traitées par ou accessibles via les terminaux utilisateurs.

### Inventaire des terminaux (Obligatoire)

[Organisation] DOIT maintenir un inventaire complet et à jour de tous les terminaux utilisateurs stockant, traitant ou accédant aux informations organisationnelles.

**Couverture minimale de l'inventaire** : ≥ 95 % des terminaux connectés au réseau (cible : 100 %)

**Fréquence de mise à jour de l'inventaire** : Découverte automatisée hebdomadaire minimum (quotidienne de préférence), rapprochement mensuel

**Note de mise en œuvre** : Les procédures de découverte des terminaux, les attributs de l'inventaire et les méthodes de rapprochement sont définis dans ISMS-IMP-A.8.1-7-18-19-S1 (Processus de découverte des terminaux).

### Classification des terminaux (Obligatoire)

[Organisation] DOIT classifier les terminaux par type d'appareil, modèle de propriété et criticité pour appliquer les contrôles de sécurité appropriés.

**Dimensions de classification** :

- Type d'appareil (ordinateur portable, de bureau, mobile, tablette, objet connecté, client VDI)
- Modèle de propriété (équipement d'entreprise, BYOD, contractant, invité, laboratoire/test)
- Criticité (critique, élevée, moyenne, faible — selon les données consultées et l'impact métier)

**Note de mise en œuvre** : Les critères de classification, les procédures et la correspondance avec les contrôles de sécurité sont définis dans ISMS-IMP-A.8.1-7-18-19-S1.

### Référentiels de sécurité (Obligatoire)

[Organisation] DOIT mettre en œuvre des référentiels de sécurité appropriés au type de terminal et au modèle de propriété.

**Exigences du référentiel universel** (tous les terminaux) :

- Durcissement du système d'exploitation (dernières mises à jour de sécurité, pare-feu activé, services inutiles désactivés)
- Contrôles d'authentification (mots de passe robustes, verrouillage d'écran, AMF le cas échéant)
- Sécurité réseau (Wi-Fi sécurisé, restrictions Bluetooth)
- Journalisation et surveillance (journalisation des événements de sécurité, intégration SIEM le cas échéant)

**Référentiels spécifiques aux plateformes** : Les référentiels Windows, macOS, Linux, iOS/Android DOIVENT être définis sur la base des guides de sécurité des éditeurs (Microsoft Security Baselines, Apple Platform Security Guide) et des normes sectorielles (CIS Benchmarks).

**Surveillance de la conformité aux référentiels** : Analyses de conformité automatisées hebdomadaires minimum (quotidiennes de préférence), rapports de conformité mensuels, cible de ≥ 90 % de conformité sur l'ensemble des terminaux.

**Note de mise en œuvre** : Les spécifications détaillées des référentiels, les mécanismes d'application et les procédures de surveillance de la conformité sont définis dans ISMS-IMP-A.8.1-7-18-19-S1.

### Chiffrement (Obligatoire)

[Organisation] DOIT mettre en œuvre le chiffrement pour protéger les données au repos sur les terminaux.

**Exigences de chiffrement intégral du disque** :

- Tous les ordinateurs portables et de bureau d'entreprise : chiffrement intégral du disque (FDE) requis (cible ≥ 98 %)
- Algorithme de chiffrement : AES-256 minimum
- Authentification pré-démarrage : requise
- Séquestre des clés de chiffrement : requis pour les appareils d'entreprise (clés de récupération stockées de manière centralisée)

**Exigences de chiffrement pour les appareils mobiles** :

- Tous les appareils mobiles d'entreprise : chiffrement activé (cible ≥ 95 %)
- Appareils mobiles BYOD : chiffrement du conteneur requis (applications/données d'entreprise uniquement)

**Calendrier de déploiement du chiffrement** :

- Nouveaux appareils : chiffrement activé avant le déploiement (100 % de conformité)
- Appareils existants : terminaux critiques dans les 30 jours, priorité élevée dans les 90 jours, priorité moyenne dans les 180 jours

**Exceptions** : Les ordinateurs de bureau situés dans des installations sécurisées PEUVENT être exemptés avec l'approbation du RSSI et des contrôles compensatoires. Les installations sécurisées sont définies comme des zones à accès contrôlé (badge/biométrie), une surveillance 24h/24 7j/7 ou un accueil en journée, sans accès public, documentées dans le registre de sécurité physique conformément à A.7.1-4.

**Note de mise en œuvre** : Les procédures de déploiement du chiffrement, la gestion des clés et les méthodes de vérification sont définies dans ISMS-IMP-A.8.1-7-18-19-S1.

### Gestion des terminaux (Obligatoire)

[Organisation] DOIT enrôler tous les terminaux d'entreprise dans un système de gestion des terminaux (MDM pour les appareils mobiles, agent pour les ordinateurs portables/de bureau).

**Capacités de gestion requises** :

- Gestion de la configuration (déploiement et application des référentiels de sécurité)
- Déploiement de logiciels (distribution centralisée des logiciels et mises à jour)
- Surveillance de la conformité (conformité aux référentiels, statut de chiffrement, inventaire des logiciels)
- Capacité d'effacement à distance (pour les appareils perdus ou volés)
- Synchronisation de l'inventaire (mise à jour automatique de l'inventaire des terminaux)

**Exigences d'enrôlement** :

- Calendrier : enrôlement requis avant la remise de l'appareil à l'utilisateur (pré-déploiement)
- Couverture : cible 100 % pour les ordinateurs portables, de bureau et appareils mobiles d'entreprise
- BYOD : gestion conteneurisée (MAM) via MDM — périmètre limité (applications/données d'entreprise uniquement)

**Gestion de la dérive de configuration** : Analyses de conformité de configuration hebdomadaires, remédiation automatique si possible, dérive corrigée dans les 7 jours.

### Réponse aux terminaux perdus ou volés (Obligatoire)

[Organisation] DOIT mettre en œuvre des procédures de réponse aux terminaux perdus ou volés.

**Exigences de signalement** : Les utilisateurs DOIVENT signaler immédiatement les appareils perdus ou volés (cible : dans l'heure suivant la découverte).

**Exigences d'effacement à distance** : La capacité d'effacement à distance DOIT être disponible pour tous les terminaux d'entreprise, initiée dans les 4 heures suivant le signalement (1 heure pour les terminaux critiques).

### Mise au rebut sécurisée (Obligatoire)

[Organisation] DOIT mettre au rebut les terminaux de manière sécurisée lors de leur décommissionnement.

**Méthodes de mise au rebut** :

- Effacement sécurisé : conformément à NIST SP 800-88 Rév. 2 (Effacement/Purge)
- Démagnétisation : pour les disques durs magnétiques
- Destruction physique : déchiquetage, écrasement ou incinération (prestataire certifié)

**Exigences** : Attestation de destruction requise pour tous les terminaux mis au rebut ; mise à jour de l'inventaire avec l'attestation en pièce jointe.

### Programme BYOD (Conditionnel)

[Organisation] PEUT mettre en œuvre un programme BYOD permettant l'utilisation d'appareils personnels à des fins professionnelles.

**Exigences de sécurité BYOD** :

- Accord d'utilisation BYOD requis (l'utilisateur reconnaît les exigences de sécurité et l'effacement à distance du conteneur)
- Sécurité minimale de l'appareil : code d'accès, chiffrement ou chiffrement du conteneur, verrouillage automatique, OS supporté
- Gestion conteneurisée (MAM) : applications d'entreprise dans un conteneur géré, séparées des données personnelles
- Périmètre de l'effacement à distance : effacement du conteneur uniquement (pas de l'intégralité de l'appareil)

**Protections de la vie privée BYOD** : Aucun accès aux données personnelles, aucun inventaire des applications personnelles, aucun contrôle total de l'appareil, gestion limitée au conteneur, notification de confidentialité transparente.

## Protection contre les logiciels malveillants (A.8.7)

**Objectif** : Protéger les terminaux contre les logiciels malveillants par des contrôles de détection, de prévention et de récupération, soutenus par la sensibilisation des utilisateurs.

### Solution anti-logiciels malveillants / EDR (Obligatoire)

[Organisation] DOIT déployer des solutions anti-logiciels malveillants ou EDR (Détection et Réponse sur les Postes de Travail) avec des capacités de détection multicouches.

**Mécanismes de détection requis** :

- Détection basée sur les signatures : signatures antivirus traditionnelles pour les logiciels malveillants connus
- Détection comportementale (heuristiques) : surveillance du comportement des programmes
- Détection par apprentissage automatique : modèles IA/ML pour les menaces inconnues (fortement recommandé)
- Prévention des exploits : bloque les techniques d'exploitation
- Protection spécifique aux rançongiciels : analyse comportementale, accès contrôlé aux dossiers, capacité de restauration

**Protection fournie dans le cloud** : Les solutions anti-logiciels malveillants/EDR DEVRAIENT exploiter la protection fournie dans le cloud pour des renseignements sur les menaces en temps réel.

**Protection contre la falsification** : Les agents anti-logiciels malveillants/EDR DOIVENT avoir la protection contre la falsification activée.

### Couverture de la protection (Obligatoire)

[Organisation] DOIT atteindre une couverture de protection contre les logiciels malveillants sur l'ensemble des terminaux.

**Exigences de couverture** :

- Terminaux d'entreprise : ≥ 98 % de couverture (cible : 100 %)
- Terminaux BYOD : ≥ 80 % de couverture (inférieur en raison du caractère volontaire et de la gestion limitée)

**Surveillance de la couverture** : Rapports quotidiens depuis la console de gestion anti-logiciels malveillants, alerte immédiate si la couverture tombe en dessous de 95 %.

**Remédiation des lacunes** : Terminal non protégé identifié → protection déployée dans les 24 heures.

### Protection en temps réel et analyses (Obligatoire)

[Organisation] DOIT mettre en œuvre une protection en temps réel et des analyses périodiques.

**Protection en temps réel** : L'analyse à l'accès DOIT être activée sur tous les terminaux protégés (fichiers analysés lors de leur ouverture, exécution ou copie).

**Analyses complètes du système** : Des analyses complètes DOIVENT être effectuées hebdomadairement sur tous les terminaux protégés.

**Analyses rapides** : Des analyses rapides DEVRAIENT être effectuées quotidiennement sur tous les terminaux protégés.

### Mises à jour des signatures (Obligatoire)

[Organisation] DOIT maintenir les signatures/définitions anti-logiciels malveillants à jour.

**Fréquence de mise à jour** : Quotidienne minimum (mises à jour en temps réel fortement préférées pour la protection fournie dans le cloud).

**Vérification des mises à jour** : Signatures obsolètes signalées (Jaune : > 24 heures, Rouge : > 48 heures), remédiation dans les 24 heures.

**Actualité de l'agent** : Le logiciel agent anti-logiciels malveillants/EDR DOIT être maintenu à jour (dernière version ou N-1), ≥ 90 % des terminaux sur la dernière version ou N-1.

### Mise en quarantaine et remédiation (Obligatoire)

[Organisation] DOIT mettre en œuvre une mise en quarantaine automatique des logiciels malveillants et des procédures de remédiation.

**Mise en quarantaine automatique** : Les logiciels malveillants détectés DOIVENT être automatiquement mis en quarantaine sans intervention de l'utilisateur.

**Exigences de remédiation** : La remédiation DOIT inclure le nettoyage, la vérification et la récupération (restauration des fichiers depuis la sauvegarde, réinitialisation des identifiants compromis, réimage si nécessaire pour les infections graves).

### Réponse aux incidents de logiciels malveillants (Obligatoire)

[Organisation] DOIT mettre en œuvre des procédures de réponse aux incidents pour les infections par logiciels malveillants.

**Délais de réponse** : Triage dans l'heure, confinement immédiat pour les critiques (rançongiciel actif, exfiltration de données), dans les 4 heures pour les incidents de haute gravité.

**Journalisation des incidents** : Toutes les détections de logiciels malveillants journalisées de manière centralisée (SIEM conformément à ISMS-POL-A.8.15), tickets d'incident créés, conservation minimale de 12 mois.

### Sensibilisation des utilisateurs (Obligatoire)

[Organisation] DOIT fournir une formation de sensibilisation à la sécurité sur les menaces de logiciels malveillants.

**Exigences de formation** :

- Sujets : reconnaissance de l'hameçonnage, pratiques sécurisées de messagerie/navigation, risques des supports amovibles, signalement des activités suspectes
- Fréquence : formation initiale lors de l'intégration, remise à niveau annuelle minimum (trimestrielle recommandée)
- Simulations d'hameçonnage : campagnes trimestrielles
- Mesure de l'efficacité : ≥ 95 % de taux d'achèvement annuel, cible de ≤ 10 % de taux de clics aux simulations d'hameçonnage
- Remédiation en cas d'échecs répétés : le personnel échouant à deux simulations consécutives DOIT recevoir une formation de remédiation ciblée dans les 14 jours ; trois échecs consécutifs ou plus déclenchent une notification au responsable et une surveillance renforcée conformément à la politique RH

## Gestion des utilitaires privilégiés (A.8.18)

**Objectif** : Restreindre et contrôler étroitement les programmes utilitaires privilégiés susceptibles de contourner les contrôles du système et des applications.

### Inventaire des utilitaires privilégiés (Obligatoire)

[Organisation] DOIT maintenir un inventaire des programmes utilitaires privilégiés susceptibles de contourner les contrôles du système et des applications.

**Les utilitaires privilégiés comprennent** :

- Outils d'administration système (Gestionnaire des tâches, Éditeur de registre, Gestionnaire de services, MMC)
- Outils d'accès distant (Bureau à distance, VNC, TeamViewer, clients SSH)
- Outils de débogage et de développement (débogueurs, décompilateurs, éditeurs hexadécimaux)
- Utilitaires de disque et de fichiers (formateurs de disque, gestionnaires de partitions, outils de suppression sécurisée)
- Outils de mots de passe et de sécurité (outils de récupération de mots de passe, outils de contournement du chiffrement)
- Utilitaires réseau (analyseurs de paquets, scanners de ports, analyseurs réseau)
- Outils de virtualisation (hyperviseurs, outils de gestion de machines virtuelles)
- Tout outil pouvant contourner les contrôles de sécurité (désactiver l'antivirus, modifier les journaux d'audit)

**Maintenance de l'inventaire** : Révision trimestrielle, nouveaux utilitaires évalués avant déploiement.

### Contrôle d'accès (Obligatoire)

[Organisation] DOIT restreindre l'accès aux utilitaires privilégiés au seul personnel autorisé.

**Contrôle d'accès basé sur les rôles (RBAC)** : L'accès aux utilitaires privilégiés DOIT être restreint selon le rôle professionnel et le besoin métier.

**Mécanismes de contrôle d'accès** :

- Liste d'autorisation des applications : utilitaires privilégiés bloqués pour les utilisateurs standard
- Gestion des accès privilégiés (PAM) : accès en juste-à-temps, enregistrement des sessions pour les utilitaires hautement privilégiés
- Stratégie de groupe (Windows) : désactivation du Gestionnaire des tâches, de l'Éditeur de registre pour les utilisateurs standard
- Restrictions MDM (macOS/mobile) : restriction de l'accès aux outils de développement, aux paramètres système
- Restrictions sudo (Linux) : limitation de l'accès sudo aux utilisateurs autorisés uniquement

**Authentification multifacteur** : L'accès aux utilitaires privilégiés critiques DOIT nécessiter une authentification multifacteur (AMF).

### Flux d'approbation (Obligatoire)

[Organisation] DOIT mettre en œuvre des flux d'approbation pour les demandes d'accès aux utilitaires privilégiés.

**Types de demandes d'accès** :

- Accès permanent (attribution permanente) : approbation du responsable + approbation du RSSI (utilitaires critiques), recertification annuelle
- Accès temporaire (limité dans le temps) : approbation du responsable, révocation automatique après la durée, maximum 1 à 90 jours
- Accès d'urgence (brise-glace) : approbation post-factum (accès accordé immédiatement, responsable notifié), révisé dans les 24 heures

**Documentation des approbations** : Ticket de demande, justification métier, autorité d'approbation, date d'approbation, durée d'accès (si temporaire).

### Surveillance et journalisation de l'utilisation (Obligatoire)

[Organisation] DOIT journaliser et surveiller l'utilisation des utilitaires privilégiés.

**Exigences de journalisation** : Identité de l'utilisateur, nom de l'utilitaire, horodatage, durée, identifiant du terminal, actions effectuées (si disponible — enregistrement de session).

**Conservation des journaux** : 12 mois minimum.

**Exigences de surveillance** : Alerte en temps réel pour les tentatives d'utilisation non autorisée d'utilitaires privilégiés, révision quotidienne des journaux (détection automatisée des anomalies), audit trimestriel de l'utilisation.

**Intégration SIEM** : Journaux d'utilisation des utilitaires privilégiés transmis au SIEM centralisé (conformément à ISMS-POL-A.8.15).

### Gestion des outils de contournement de la sécurité (Obligatoire)

[Organisation] DOIT identifier et restreindre étroitement les outils susceptibles de contourner les contrôles de sécurité.

**Les outils de contournement comprennent** : désactivateurs d'anti-logiciels malveillants, outils de modification des journaux d'audit, outils de contournement du chiffrement (casseurs de mots de passe), outils rootkit, outils désactivant Windows Defender ou la protection contre la falsification, outils modifiant la protection de l'intégrité du système (macOS SIP).

**Approche de contrôle** :

- Interdits : outils de contournement prohibés sur les terminaux de production (sauf autorisation pour les tests de sécurité)
- Détection : le contrôle des applications détecte les outils non autorisés
- Remédiation automatique : outils détectés automatiquement mis en quarantaine/supprimés
- Utilisation autorisée : équipe sécurité uniquement, environnement de laboratoire de sécurité isolé, approbation requise

## Contrôles d'installation des logiciels (A.8.19)

**Objectif** : Gérer de manière sécurisée l'installation de logiciels sur les systèmes opérationnels par des contrôles, des autorisations et une gestion des vulnérabilités.

### Liste des logiciels autorisés (Obligatoire)

[Organisation] DOIT maintenir une liste des logiciels autorisés.

**Contenu de la liste des logiciels autorisés** : Nom du logiciel et éditeur, version(s) autorisée(s), objet/justification métier, statut de la révision sécurité, méthode d'installation, autorité d'approbation, statut de conformité des licences.

**Catégories de logiciels** :

- Logiciels d'entreprise obligatoires : requis pour tous les utilisateurs (OS, anti-logiciels malveillants, suite bureautique)
- Logiciels spécifiques aux rôles : requis pour des rôles spécifiques (outils de développement pour les développeurs)
- Logiciels autorisés optionnels : disponibles pour l'installation par l'utilisateur (navigateurs approuvés, utilitaires)
- Logiciels interdits : explicitement prohibés (risques de sécurité, problèmes de licence)

**Maintenance de la liste** : Révision annuelle, ajouts/suppressions trimestriels, révision sécurité requise avant approbation.

### Processus d'approbation des logiciels (Obligatoire)

[Organisation] DOIT mettre en œuvre un processus d'approbation des logiciels avant déploiement.

**Composantes du processus d'approbation** :

- Demande de logiciel avec justification métier
- Révision sécurité (évaluation des vulnérabilités, réputation de l'éditeur, révision de confidentialité, conformité des licences)
- Décision d'approbation (approuvé, approuvé avec conditions, refusé)
- Déploiement (déploiement centralisé préféré, auto-installation si approuvé)

**SLA d'approbation** : Demande standard 5 jours ouvrables, demande urgente 2 jours ouvrables (approbation du responsable), demande d'urgence 1 jour ouvrable (approbation du RSSI). En cas d'absence du RSSI, l'autorité d'approbation d'urgence est déléguée à : (1) RSSI adjoint, (2) Directeur informatique, (3) Responsable de la sécurité désigné, avec révision a posteriori par le RSSI dans les 5 jours ouvrables.

### Intégration dans la gestion des changements (Obligatoire)

[Organisation] DOIT soumettre les installations de logiciels sur les systèmes de production aux procédures de gestion des changements.

**Exigences de gestion des changements** : Déploiement de logiciels classifié comme changement, demande de changement soumise, évaluation d'impact requise, approbation requise (Comité consultatif des changements pour les changements significatifs), tests requis (déploiement pilote), plan de retour arrière documenté.

**Exceptions** : Correctifs de sécurité d'urgence (changement accéléré), changements standard pré-approuvés (mises à jour OS, mises à jour anti-logiciels malveillants), logiciels autorisés installés par l'utilisateur (déjà approuvés, faible impact).

### Détection des logiciels non autorisés (Obligatoire)

[Organisation] DOIT détecter et supprimer les logiciels non autorisés.

**Méthodes de détection** : Analyses d'inventaire des logiciels (quotidiennes via la plateforme de gestion des terminaux), alertes de contrôle des applications (tentatives d'exécution non autorisées), analyse du trafic réseau, signalements des utilisateurs.

**Les logiciels non autorisés comprennent** : logiciels hors de la liste autorisée, logiciels interdits (explicitement prohibés), logiciels malveillants, versions non approuvées de logiciels approuvés, shadow IT (services cloud non approuvés).

**Calendrier de remédiation** : Logiciels prohibés/malveillants supprimés dans les 24 heures, logiciels non approuvés supprimés dans les 7 jours (ou approuvés si besoin métier légitime).

### Technologies de contrôle des applications (Obligatoire)

[Organisation] DOIT mettre en œuvre des technologies de contrôle des applications pour restreindre l'exécution de logiciels.

**Approches de contrôle des applications** :

- Liste d'autorisation (préférée) : seuls les logiciels approuvés peuvent s'exécuter, refus par défaut pour tous les autres exécutables
- Liste de blocage (complémentaire) : logiciels malveillants/prohibés connus bloqués, autorisation par défaut pour tout le reste

**Périmètre du contrôle des applications** : Exécutables (.exe, .com, .bat, .ps1), scripts (PowerShell, VBScript, JavaScript), bibliothèques (DLL, dylibs, fichiers .so), paquets d'installation (MSI, PKG, DEB, RPM), extensions et modules complémentaires de navigateur.

**Application** :

- Ordinateurs portables/de bureau d'entreprise : liste d'autorisation appliquée (obligatoire)
- Appareils BYOD : applications conteneurisées uniquement (liste d'autorisation du conteneur d'entreprise)
- Serveurs : liste d'autorisation stricte (gestion des changements requise pour tout nouveau logiciel)

### Gestion des vulnérabilités logicielles (Obligatoire)

[Organisation] DOIT maintenir les logiciels installés à jour avec les correctifs et mises à jour de sécurité.

**Exigences de correction** :

- Correctifs de sécurité critiques : installés dans les 7 jours suivant leur publication
- Correctifs de haute gravité : installés dans les 30 jours
- Correctifs de gravité moyenne/faible : installés dans les 90 jours
- Vulnérabilités zero-day activement exploitées : correction d'urgence (dans les 24 à 48 heures)

**Gestion du cycle de vie des logiciels** : Logiciels en fin de vie identifiés et remplacés avant la fin du support éditeur, logiciels non supportés signalés comme risque élevé avec contrôles compensatoires requis.

**Intégration** : La gestion des vulnérabilités logicielles s'intègre avec ISMS-POL-A.8.8 (Gestion des vulnérabilités).

---

# Rôles et responsabilités

## Matrice RACI

| Rôle | A.8.1 Terminaux | A.8.7 Logiciels malv. | A.8.18 Utilitaires | A.8.19 Logiciels | Cadre global |
|------|----------------|----------------------|-------------------|-----------------|--------------|
| **RSSI** | Responsable | Responsable | Responsable | Responsable | Responsable |
| **Responsable sécurité IT** | En charge | En charge | En charge | En charge | En charge |
| **Admins postes de travail** | En charge | En charge | Consulté | Consulté | En charge |
| **SOC** | Consulté | En charge | En charge | Consulté | Consulté |
| **Service desk IT** | Informé | Informé | Informé | Informé | Informé |
| **Utilisateurs finaux** | En charge (conformité) | Informé | Informé | Informé | En charge (conformité) |
| **Gestion des actifs** | Consulté | Informé | Informé | Informé | Consulté |
| **Gestion des changements** | Consulté | Informé | Consulté | En charge (approbations) | Consulté |

**Légende RACI** : En charge (exécute), Responsable (autorité décisionnelle), Consulté (avis sollicité), Informé (tenu informé)

## Rôles clés

**Responsable de la Sécurité des Systèmes d'Information (RSSI)** :

- Responsabilité globale du cadre de sécurité des postes de travail
- Approuver la politique et les exceptions majeures
- Allouer les ressources pour la mise en œuvre
- Reporting exécutif sur la posture de sécurité des postes de travail
- Acceptation des risques pour les lacunes de sécurité

**Responsable de la sécurité IT** :

- Gestion quotidienne des contrôles de sécurité des postes de travail
- Mettre en œuvre et maintenir le cadre de sécurité
- Coordonner les évaluations de sécurité
- Gérer les incidents de sécurité des postes de travail
- Rendre compte du statut de conformité au RSSI

**Administrateurs des postes de travail** :

- Déployer et configurer les plateformes de gestion des terminaux
- Appliquer les référentiels et configurations de sécurité
- Gérer le déploiement du chiffrement
- Effectuer la gestion de l'inventaire des terminaux
- Mettre en œuvre les correctifs et mises à jour de sécurité

**Centre des Opérations de Sécurité (SOC)** :

- Surveiller les alertes anti-logiciels malveillants/EDR
- Trier et répondre aux incidents de logiciels malveillants
- Enquêter sur les événements de sécurité sur les terminaux
- Coordonner la réponse aux incidents
- Surveiller l'utilisation des utilitaires privilégiés pour détecter les anomalies
- Escalader les événements critiques de sécurité

**Utilisateurs finaux** :

- Se conformer aux exigences de sécurité des postes de travail
- Signaler immédiatement les appareils perdus ou volés
- Signaler les logiciels malveillants ou incidents de sécurité suspectés
- Suivre la formation de sensibilisation à la sécurité
- Maintenir la sécurité physique des terminaux assignés
- Ne pas tenter de contourner les contrôles de sécurité

---

# Intégration et mise en œuvre

## Intégration avec les autres contrôles du SMSI

**Points d'intégration critiques** :

| Contrôle connexe | Point d'intégration | Dépendance |
|-----------------|---------------------|------------|
| **A.5.9 – Inventaire des actifs** | L'inventaire des terminaux alimente l'inventaire des actifs | Terminaux = actifs informationnels |
| **A.8.2 – Droits d'accès privilégiés** | L'accès aux utilitaires privilégiés est un sous-ensemble de la gestion des accès privilégiés | Les utilisateurs d'utilitaires privilégiés nécessitent une gouvernance |
| **A.8.5 – Authentification sécurisée** | L'authentification des terminaux met en œuvre l'authentification sécurisée | AMF pour les terminaux et les utilitaires privilégiés |
| **A.8.8 – Gestion des vulnérabilités** | La correction des logiciels remédie aux vulnérabilités des terminaux | L'analyse des vulnérabilités identifie les logiciels non corrigés |
| **A.8.9 – Gestion de la configuration** | Les référentiels des terminaux sont des configurations gérées | La dérive des référentiels = écart de configuration |
| **A.8.15 – Journalisation** | Les événements de sécurité des terminaux journalisés de manière centralisée | Les journaux d'utilisation des utilitaires privilégiés alimentent le SIEM |
| **A.8.16 – Surveillance** | La surveillance des terminaux met en œuvre les activités de surveillance | Le SOC surveille les événements de sécurité des terminaux |
| **A.8.20-22 – Sécurité des réseaux** | La sécurité réseau des terminaux complète la sécurité de l'infrastructure réseau | Le NAC vérifie la conformité des terminaux |
| **A.6.7 – Télétravail** | Les terminaux distants ont des exigences de sécurité supplémentaires | Application du VPN, chiffrement renforcé |

## Ressources de mise en œuvre

**Guides de mise en œuvre** (Suite ISMS-IMP-A.8.1-7-18-19) :

- **ISMS-IMP-A.8.1-7-18-19-S1** : Processus de découverte des terminaux
- **ISMS-IMP-A.8.1-7-18-19-S2** : Déploiement de la protection contre les logiciels malveillants
- **ISMS-IMP-A.8.1-7-18-19-S3** : Processus de contrôle des logiciels
- **ISMS-IMP-A.8.1-7-18-19-S4** : Gestion des utilitaires privilégiés

## Évaluation et vérification

**Fréquence d'évaluation** :

- Continue : surveillance automatisée de la conformité via MDM (quotidienne)
- Hebdomadaire : analyses de conformité aux référentiels, mises à jour de l'inventaire, vérification des signatures
- Mensuelle : rapport de conformité complet (toutes les métriques)
- Trimestrielle : tableau de bord exécutif et analyse des tendances
- Annuelle : évaluation complète, révision auditeur, révision de la politique

**Seuils de conformité** :

- ✅ Conforme (Vert) : ≥ 90 %
- ⚠️ Conformité partielle (Jaune) : 70 – 89 %
- ❌ Non conforme (Rouge) : < 70 %

## Gestion des exceptions

**Autorité d'approbation des exceptions** :

- Risque faible : Responsable de la sécurité IT
- Risque moyen : RSSI (évaluation des risques requise)
- Risque élevé : RSSI + Comité des risques (contrôles compensatoires obligatoires, notification exécutive)
- Exceptions permanentes : RSSI + Comité des risques (recertification annuelle requise)

**Suivi des exceptions** : Toutes les exceptions approuvées documentées dans le registre des exceptions centralisé, exceptions temporaires révisées mensuellement, exceptions permanentes révisées annuellement, exceptions à haut risque révisées trimestriellement.

---

# Définitions

**Terminal utilisateur** : Tout appareil orienté utilisateur stockant, traitant ou accédant aux informations organisationnelles (ordinateurs portables, de bureau, appareils mobiles, tablettes, objets connectés).

**EDR (Endpoint Detection and Response — Détection et Réponse sur les Postes de Travail)** : Solution de sécurité avancée fournissant une surveillance en temps réel, la détection des menaces, l'investigation et des capacités de réponse automatisée.

**MAM (Mobile Application Management — Gestion des Applications Mobiles)** : Gestion des applications d'entreprise sur les appareils mobiles, notamment les scénarios BYOD, permettant le contrôle des applications/données d'entreprise tout en préservant la confidentialité des utilisateurs.

**MDM (Mobile Device Management — Gestion des Appareils Mobiles)** : Gestion centralisée des appareils mobiles, application des politiques de sécurité, déploiement des configurations et capacité d'effacement à distance.

**Programme utilitaire privilégié** : Outil logiciel capable de contourner ou d'ignorer les contrôles de sécurité du système et des applications (par ex. éditeurs de registre, débogueurs, outils administratifs).

**BYOD (Bring Your Own Device — Apportez votre propre appareil)** : Programme permettant aux employés d'utiliser des appareils personnels à des fins professionnelles, sous réserve de contrôles de sécurité et de confidentialité.

**Référentiel de sécurité** : Exigences minimales de configuration de sécurité pour les terminaux, généralement alignées sur les guides de sécurité des éditeurs (Microsoft, Apple) et les benchmarks CIS.

**Contrôle des applications (liste d'autorisation)** : Contrôle de sécurité n'autorisant l'exécution que des logiciels explicitement approuvés, bloquant par défaut tous les autres exécutables.

**Chiffrement intégral du disque (FDE)** : Chiffrement de l'intégralité du ou des volumes de disque, protégeant les données au repos contre tout accès physique non autorisé.

**Protection contre la falsification** : Fonctionnalité anti-logiciels malveillants empêchant les logiciels malveillants ou les utilisateurs non autorisés de désactiver, modifier ou désinstaller le logiciel de sécurité.

**Menace zero-day** : Logiciel malveillant ou exploit précédemment inconnu, non encore détecté par l'antivirus basé sur les signatures, nécessitant une détection comportementale ou par apprentissage automatique.

**Dérive de configuration** : Écart par rapport à la configuration de référence de sécurité approuvée.

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable des opérations IT** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale (PDG)** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de sécurité des postes de travail. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.1-7-18-19 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
