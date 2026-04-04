<!-- ISMS-CORE:POLICY:ISMS-POL-A.6.7-8-FR:framework:POL:a.6.7-8 -->
**ISMS-POL-A.6.7-8 – Télétravail et déclaration des événements de sécurité**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Télétravail et déclaration des événements de sécurité |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.6.7-8 |
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
- Secondaire : Directeur des Ressources Humaines (DRH)
- Technique : Directeur informatique / DSI
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.6.7-8.-UG/TGS1 à .S5 (Suite de guides de mise en œuvre et d'évaluation)
- ISO/IEC 27001:2022 Contrôles A.6.7, A.6.8
- ISO/IEC 27002:2022 Sections 6.7, 6.8 (Orientations de mise en œuvre)
- ISMS-POL-A.5.1-2-6.1-2 (Sécurité de l'emploi et des rôles)
- ISMS-POL-A.6.3 (Sensibilisation et formation)
- ISMS-POL-A.5.24-28 (Cycle de vie de la gestion des incidents)
- ISMS-POL-A.8.1-7-18-19 (Sécurité des postes de travail)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de sécurité du télétravail et de déclaration des événements de sécurité de l'information, conformément aux Contrôles A.6.7 et A.6.8 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à l'ensemble du personnel travaillant à distance ou hors des locaux de [Organisation], à tous les appareils utilisés pour le télétravail (entreprise et personnels), à toutes les informations consultées ou traitées à distance, et à l'ensemble du personnel responsable de la déclaration des événements de sécurité quel que soit le lieu de travail.

**Objet** : Définir les exigences organisationnelles pour le télétravail sécurisé et la déclaration rapide des événements de sécurité. Cette politique établit QUELLES mesures de sécurité sont requises pour le télétravail, QUI peut travailler à distance et dans quelles conditions, CE QUI constitue un événement de sécurité à déclarer, et QUI est responsable de la déclaration et de la réponse. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.6.7-8 (variantes UG/TG).S1 à .S5.

**Cadre de contrôles combinés** : Ces deux contrôles sont mis en œuvre comme un cadre unifié parce que :

1. **Les télétravailleurs sont en première ligne de la détection des événements** — Le personnel travaillant à distance est souvent le premier à observer des anomalies de sécurité affectant ses appareils, connexions ou accès aux données
2. **Les menaces spécifiques au télétravail nécessitent un signalement spécialisé** — Les télétravailleurs font face à des menaces absentes en environnement de bureau (réseaux non sécurisés, accès physique par des tiers, risques dans les espaces publics)
3. **La norme ISO 27002:2022 les lie explicitement** — Les orientations sur le télétravail exigent que les procédures de déclaration des incidents soient accessibles depuis les emplacements distants
4. **Même population de personnel** — Les deux contrôles s'adressent aux mêmes personnes et à leurs responsabilités de sécurité ; une formation combinée est plus efficace

**Indépendance de la Déclaration d'applicabilité** : Bien que mis en œuvre comme un cadre unifié, A.6.7 et A.6.8 sont évalués indépendamment dans la Déclaration d'applicabilité. Chaque contrôle conserve des exigences distinctes, une collecte de preuves et une notation de conformité à des fins d'audit.

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment la nLPD suisse (protection des données), le RGPD de l'UE (si applicable), la norme ISO/IEC 27001:2022 et les exigences sectorielles spécifiques le cas échéant.

**Pourquoi c'est important** : Le télétravail est devenu une pratique standard, élargissant la surface d'attaque organisationnelle au-delà des défenses périmètriques traditionnelles. Les recherches sectorielles indiquent que les télétravailleurs font face à une exposition au hameçonnage 3 fois plus élevée, et que le délai moyen de détection d'une violation augmente significativement lorsque le personnel travaille en dehors des réseaux surveillés. Ce cadre traite ces risques par des exigences de sécurité systématiques et des mécanismes robustes de déclaration des événements.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.6.7 de la norme ISO/IEC 27001:2022 – Télétravail

**Norme ISO/IEC 27001:2022 Annexe A.6.7 – Télétravail**

> *Des mesures de sécurité devraient être mises en œuvre lorsque le personnel travaille à distance afin de protéger les informations consultées, traitées ou stockées en dehors des locaux de l'organisation.*

**Objectif du contrôle** : S'assurer que le personnel distant dispose des contrôles de sécurité nécessaires pour protéger la confidentialité, l'intégrité et la disponibilité des informations, procédures et systèmes organisationnels contre tout accès ou divulgation non autorisés lors du travail en dehors des locaux de [Organisation].

**Type de contrôle** : Préventif
**Catégorie de contrôle** : Contrôle lié au personnel
**Propriétés de sécurité** : Confidentialité, Intégrité, Disponibilité

## Contrôle A.6.8 de la norme ISO/IEC 27001:2022 – Déclaration des événements de sécurité de l'information

**Norme ISO/IEC 27001:2022 Annexe A.6.8 – Déclaration des événements de sécurité de l'information**

> *L'organisation devrait mettre à la disposition du personnel un mécanisme permettant de déclarer les événements de sécurité de l'information observés ou suspectés via des canaux appropriés et en temps opportun.*

**Objectif du contrôle** : Favoriser une déclaration rapide, cohérente et efficace des événements de sécurité de l'information identifiables par le personnel, garantissant que les événements sont documentés avec précision pour soutenir les activités de réponse aux incidents et autres responsabilités de management de la sécurité.

**Type de contrôle** : Détectif
**Catégorie de contrôle** : Contrôle lié au personnel
**Propriétés de sécurité** : Confidentialité, Intégrité, Disponibilité

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences pour les arrangements de télétravail sécurisé
- **Établit** les exigences d'autorisation pour le télétravail
- **Précise** les exigences de sécurité physique pour les environnements de télétravail
- **Impose** les contrôles techniques de sécurité pour l'accès distant
- **Définit** les exigences de traitement des données lors du télétravail
- **Établit** les mécanismes et canaux de déclaration des événements de sécurité
- **Précise** ce qui constitue un événement de sécurité à déclarer
- **Impose** un signalement rapide et une culture sans reproche
- **Attribue** les responsabilités pour la gouvernance du télétravail et la réponse aux événements
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00
- **Intègre** avec les contrôles connexes (sécurité des postes de travail, gestion des incidents, contrôle d'accès)

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les procédures techniques de configuration VPN** (voir ISMS-IMP-A.6.7-8.S2)
- **Fournit pas d'instructions détaillées de configuration de l'AMF** (spécifique aux éditeurs, voir procédures IT)
- **Fournit pas de formulaires d'approbation de télétravail** (voir modèles en annexe)
- **Détaille pas les procédures de réponse aux incidents** (voir ISMS-POL-A.5.24-28)
- **Précise pas les procédures de durcissement des postes de travail** (voir ISMS-POL-A.8.1-7-18-19)
- **Définit pas les politiques RH de télétravail** (éligibilité, planification – domaine RH)
- **Remplace pas les obligations du droit du travail local** (complète le cadre RH existant)
- **Précise pas les procédures de triage des événements** (voir ISMS-IMP-A.6.7-8.S4)

## Périmètre

**Cette politique s'applique à** :

**Personnel** :

- Tous les employés travaillant à distance (temps plein, temps partiel, occasionnel)
- Tous les contractants et consultants travaillant hors des locaux de [Organisation]
- Tout le personnel tiers ayant un accès distant aux systèmes de [Organisation]
- Tout le personnel en déplacement professionnel qui accède aux ressources organisationnelles
- Tout le personnel susceptible d'observer ou de déclarer des événements de sécurité

**Arrangements de télétravail** :

- Travail à domicile (régulier ou occasionnel)
- Travail depuis des espaces de coworking ou bureaux partagés
- Travail depuis les locaux de clients ou partenaires
- Travail en déplacement (hôtels, aéroports, espaces publics)
- Tout travail effectué en dehors des locaux contrôlés de [Organisation]

**Appareils et équipements** :

- Ordinateurs portables, tablettes et appareils mobiles fournis par l'entreprise
- Appareils personnels utilisés pour le travail (BYOD) lorsque autorisé
- Supports de stockage portables contenant des données organisationnelles
- Appareils de communication utilisés à des fins organisationnelles

**Informations et systèmes** :

- Toutes les données organisationnelles consultées à distance
- Tous les systèmes organisationnels accessibles via des connexions distantes
- Toutes les communications contenant des informations organisationnelles
- Tous les documents et matériaux traités en dehors des locaux de [Organisation]

**Hors périmètre** :

- Travail sur site effectué dans les locaux contrôlés de [Organisation]
- Activités personnelles sur appareils personnels sans données organisationnelles
- Aspects RH du télétravail (éligibilité, équilibre vie professionnelle/personnelle, planification)
- Politiques de compensation et de remboursement des frais (domaine RH distinct)

## Applicabilité réglementaire

Les exigences réglementaires sont catégorisées conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**.

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés |
|----------------|---------------|----------------|
| **nLPD suisse** | Toutes les opérations suisses | Art. 8 – Mesures techniques et organisationnelles appropriées pour la protection des données en environnement distant |
| **RGPD de l'UE** | Lors du traitement de données personnelles de l'UE | Art. 32 – La sécurité du traitement doit s'étendre au télétravail ; Art. 33 – La notification de violation dans les 72 heures nécessite une détection rapide des événements |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôles A.6.7 (Télétravail), A.6.8 (Déclaration des événements) |

**Niveau 2 : Applicabilité conditionnelle**

S'applique uniquement lorsque des conditions métier spécifiques déclenchent l'applicabilité :

| Réglementation | Condition de déclenchement | Exigences télétravail/déclaration |
|---------------|---------------------------|----------------------------------|
| **Directive NIS2** | Entité essentielle/importante (UE) | Art. 21 – Pratiques de cybersécurité incluant la sécurité de l'accès distant ; Art. 23 – Notification d'incident dans les 24 heures |
| **DORA** | Services financiers UE | Art. 9 – Les exigences de sécurité TIC s'étendent à l'accès distant ; Art. 19 – Déclaration d'incident aux autorités compétentes |
| **Circulaire FINMA 2008/21** | Établissement financier réglementé en Suisse | Contrôles d'accès distant, déclaration d'incident à la FINMA |
| **PCI DSS v4.0.1** | Traitement de données de cartes de paiement | Exig. 12.3.1 – Sécurité de l'accès distant ; Exig. 12.10 – Réponse aux incidents |

**Niveau 3 : Référence informative**

Ces référentiels informent la mise en œuvre mais ne constituent pas une conformité obligatoire sauf si contractuellement requis :

- NIST SP 800-46 Rév. 2 – Guide to Enterprise Telework, Remote Access, and BYOD Security
- NIST SP 800-61 Rév. 2 – Computer Security Incident Handling Guide
- CIS Controls v8.1 – Contrôle 4 (Configuration sécurisée), Contrôle 17 (Réponse aux incidents)
- ENISA – Lignes directrices sur la sécurité du télétravail

---

# Exigences pour le télétravail (Contrôle A.6.7)

## Autorisation du télétravail

[Organisation] DOIT établir un processus d'autorisation formel pour les arrangements de télétravail.

**2.1.1 Exigences d'autorisation**

| Exigence | Description |
|----------|-------------|
| **Approbation formelle** | Tous les arrangements de télétravail réguliers DOIVENT être formellement approuvés avant le début |
| **Autorité d'autorisation** | Les responsables hiérarchiques autorisent le télétravail ; la Sécurité IT approuve l'accès technique |
| **Évaluation des risques** | Une évaluation des risques DOIT être réalisée pour les rôles traitant des données sensibles à distance |
| **Critères d'évaluation des risques** | L'évaluation DOIT évaluer au minimum : (a) Le niveau de classification des données consultées à distance (conformément à A.5.12) ; (b) La capacité de sécurité physique de l'emplacement distant ; (c) La posture de sécurité réseau ; (d) La conformité de la référence de sécurité des appareils ; (e) Les restrictions réglementaires ou contractuelles |
| **Vérification de l'évaluation des risques** | L'adéquation de l'évaluation est vérifiée par des critères documentés alignés sur la méthodologie de risque organisationnelle (conformément à A.5.7). Les procédures d'évaluation détaillées sont dans ISMS-IMP-A.6.7-8.S1 |
| **Accord documenté** | Les télétravailleurs DOIVENT reconnaître les exigences de sécurité du télétravail |
| **Révision périodique** | Les autorisations de télétravail DOIVENT être révisées au moins annuellement |

**2.1.2 Critères d'autorisation**

L'autorisation de télétravail DOIT prendre en compte :

- L'adéquation du rôle au télétravail
- La classification des données des informations à consulter
- La capacité technique à établir des connexions distantes sécurisées
- L'adéquation de l'environnement physique (confidentialité, sécurité)
- Les restrictions réglementaires ou contractuelles
- Les exigences de continuité des activités

**2.1.3 Révocation**

L'autorisation de télétravail DOIT être révoquée lorsque :

- L'emploi ou le contrat prend fin
- Le rôle évolue vers un rôle inadapté au télétravail
- Les exigences de sécurité ne sont pas respectées
- Des violations de politique surviennent
- Les besoins métier exigent une présence sur site

## Exigences de sécurité physique

[Organisation] DOIT définir les exigences de sécurité physique pour les environnements de télétravail.

**2.2.1 Exigences relatives à l'espace de travail**

Les télétravailleurs DOIVENT :

- Positionner leurs écrans pour empêcher tout regard non autorisé par d'autres personnes
- Utiliser des filtres de confidentialité lorsqu'ils travaillent dans des espaces partagés ou publics
- Sécuriser les équipements de travail lorsque l'espace de travail est sans surveillance
- Empêcher l'accès aux appareils de travail par les membres de la famille, les visiteurs ou autres personnes non autorisées
- Stocker les documents sensibles de manière sécurisée lorsqu'ils ne sont pas en cours d'utilisation
- Éliminer les documents sensibles en utilisant des méthodes approuvées (déchiquetage)

**Vérification** : La conformité à la sécurité physique est vérifiée par l'achèvement annuel d'une liste de contrôle d'auto-évaluation, une réévaluation déclenchée par des événements de sécurité ou des changements significatifs de l'espace de travail, ou une attestation lors du renouvellement de l'autorisation.

**2.2.2 Sécurité des équipements**

Les télétravailleurs DOIVENT :

- Sécuriser physiquement les équipements portables (câbles antivol, stockage sécurisé)
- Ne jamais laisser les appareils sans surveillance dans les espaces publics
- Verrouiller les appareils lors des absences momentanées, même brèves
- Signaler immédiatement les appareils perdus ou volés (voir Section 3)
- Transporter les appareils de manière sécurisée entre les emplacements

**2.2.3 Exigences de bureau propre**

La politique de bureau propre (conformément à A.7.7) DOIT s'étendre aux environnements de télétravail :

- Les documents sensibles NE DOIVENT PAS être visibles lorsqu'ils ne sont pas en cours d'utilisation
- Les supports de travail DOIVENT être sécurisés à la fin de chaque session de travail
- Les documents imprimés DOIVENT être stockés de manière sécurisée ou éliminés de façon appropriée

## Exigences de sécurité technique

[Organisation] DOIT imposer des contrôles techniques de sécurité pour tous les accès distants.

**2.3.1 Exigences de connexion sécurisée**

| Exigence | Obligatoire pour |
|----------|-----------------|
| **VPN ou accès Zero Trust** | Toutes les connexions aux ressources internes |
| **Authentification multifacteur (AMF)** | Tout accès distant aux systèmes organisationnels |
| **Communications chiffrées** | Toute transmission de données (TLS 1.2+ minimum) |
| **DNS d'entreprise** | Résolution via le DNS organisationnel lors de la connexion |

**2.3.2 Exigences d'authentification**

L'authentification pour l'accès distant DOIT exiger :

- L'authentification multifacteur (AMF) pour tout accès aux systèmes
- Des mots de passe robustes conformément à la politique organisationnelle de mots de passe (A.5.17)
- L'absence de partage ou de stockage des identifiants dans des emplacements non sécurisés
- Un changement immédiat du mot de passe en cas de compromission suspectée
- Un délai d'expiration de session après une période d'inactivité

**2.3.3 Exigences de sécurité réseau**

Les télétravailleurs DOIVENT :

- Utiliser uniquement des réseaux sans fil sécurisés et chiffrés (WPA2/WPA3 minimum)
- Éviter le Wi-Fi public non sécurisé pour le travail organisationnel sans protection VPN
- Ne pas désactiver ni contourner les contrôles de sécurité
- Signaler les préoccupations ou anomalies de sécurité réseau

**Vérification** : La conformité à la sécurité réseau peut être surveillée via la télémétrie de gestion des postes de travail (SSID réseau, type de chiffrement, statut de connexion VPN, validité des certificats), l'application de la connexion VPN, ou l'attestation des utilisateurs lors des révisions périodiques. Lorsque la télémétrie n'est pas techniquement réalisable, l'attestation des utilisateurs lors du renouvellement de l'autorisation fournit une assurance raisonnable.

## Exigences de traitement des données

[Organisation] DOIT définir les exigences de traitement des données dans le contexte du télétravail.

**2.4.1 Conformité à la classification des données**

Les télétravailleurs DOIVENT :

- Traiter les données conformément à leur niveau de classification (conformément à A.5.12-13)
- Ne pas traiter les données Restreintes à distance sauf autorisation spécifique
- Appliquer une protection appropriée aux données Confidentielles
- Suivre les procédures de transfert sécurisé des informations (conformément à A.5.14)

**2.4.2 Exigences de stockage des données**

| Classification des données | Stockage distant autorisé | Conditions |
|---------------------------|--------------------------|------------|
| **Public** | Oui | Sécurité standard des appareils |
| **Interne** | Oui | Appareil chiffré, emplacement sécurisé |
| **Confidentiel** | Conditionnel | Appareils approuvés et chiffrés uniquement, justification métier |
| **Restreint** | Non (par défaut) | Nécessite l'approbation explicite du RSSI, contrôles renforcés |

**Processus d'autorisation conditionnelle** : Le stockage distant de données Confidentielles nécessite : (a) Justification écrite du Responsable hiérarchique ; (b) Vérification des contrôles techniques (chiffrement de l'appareil, emplacement de stockage sécurisé) ; (c) Approbation du Responsable de la Sécurité IT. Les données Restreintes nécessitent une approbation écrite du RSSI avec des contrôles compensatoires documentés. Toutes les approbations DOIVENT être consignées dans le registre des exceptions (Section 5.4).

**2.4.3 Sauvegarde des données**

Les télétravailleurs DOIVENT :

- Stocker les fichiers de travail dans des emplacements cloud ou réseau approuvés
- Ne pas s'appuyer uniquement sur le stockage local des appareils pour les données critiques
- Suivre les politiques de sauvegarde organisationnelles

## Sécurité des appareils et équipements

[Organisation] DOIT définir les exigences de sécurité pour les appareils utilisés en télétravail.

**2.5.1 Exigences pour les appareils d'entreprise**

Les appareils fournis par l'entreprise utilisés pour le télétravail DOIVENT :

- Être configurés selon la référence de sécurité organisationnelle (conformément à A.8.9)
- Avoir le chiffrement intégral du disque activé
- Disposer d'un logiciel de protection des postes de travail à jour (conformément à A.8.7)
- Être mis à jour et corrigés selon le calendrier organisationnel (conformément à A.8.8)
- Avoir la capacité d'effacement à distance activée
- Être enregistrés dans l'inventaire des appareils (conformément à A.5.9)

**2.5.2 Exigences pour les appareils personnels (BYOD)**

Lorsque les appareils personnels sont autorisés pour le travail organisationnel, ils DOIVENT :

- Répondre aux exigences de sécurité minimales définies par la Sécurité IT
- Avoir la solution MDM/EMM organisationnelle installée (si requise)
- Maintenir une séparation entre les données personnelles et professionnelles (conteneurisation)
- Être soumis à l'effacement à distance des données organisationnelles à la résiliation
- Ne pas stocker de données organisationnelles après la révocation de l'accès

**2.5.3 Appareils prohibés**

Les appareils suivants NE DOIVENT PAS être utilisés pour le travail organisationnel :

- Appareils débridés (jailbreakés ou rootés)
- Appareils avec fonctionnalités de sécurité désactivées
- Appareils partagés non sous le contrôle de l'utilisateur
- Appareils ne pouvant pas satisfaire aux exigences de sécurité
- Appareils fonctionnant sous des systèmes d'exploitation en fin de vie sans mises à jour de sécurité
- Appareils appartenant ou contrôlés par des tiers non soumis aux politiques de sécurité organisationnelles

## Résiliation du télétravail

[Organisation] DOIT définir les exigences pour la fin des arrangements de télétravail.

**2.6.1 Révocation des accès**

Lors de la résiliation de l'autorisation de télétravail :

- Les identifiants d'accès distant DOIVENT être révoqués immédiatement
- Les jetons d'accès VPN et distant DOIVENT être désactivés
- L'accès aux systèmes accessibles à distance DOIT être révisé et supprimé

**2.6.2 Restitution des équipements**

Lors de la résiliation de l'emploi ou du contrat :

- Tous les équipements organisationnels DOIVENT être restitués conformément à A.5.11
- Toutes les données organisationnelles DOIVENT être supprimées des appareils personnels
- La restitution DOIT être vérifiée et documentée

---

# Exigences de déclaration des événements de sécurité (Contrôle A.6.8)

## Mécanismes de déclaration

[Organisation] DOIT fournir des mécanismes accessibles pour déclarer les événements de sécurité.

**3.1.1 Exigences relatives aux canaux de déclaration**

| Exigence | Description |
|----------|-------------|
| **Canaux multiples** | Au moins deux canaux de déclaration distincts DOIVENT être disponibles |
| **Disponibilité 24h/24 7j/7** | Au moins un canal DOIT être disponible en dehors des heures de bureau |
| **Accessibilité depuis les emplacements distants** | Tous les canaux DOIVENT être accessibles depuis les emplacements distants |
| **Coordonnées clairement publiées** | Les contacts de déclaration DOIVENT être publiés de manière bien visible |
| **Accusé de réception** | Tous les rapports DOIVENT être pris en compte dans les délais définis |

**Vérification** : La disponibilité des canaux est vérifiée par des tests trimestriels des canaux de déclaration (e-mail, téléphone, billetterie), des exercices annuels de réponse aux incidents vérifiant l'accessibilité des canaux, ou une surveillance automatisée continue lorsque techniquement réalisable.

**3.1.2 Canaux de déclaration standard**

[Organisation] DOIT maintenir les canaux de déclaration suivants :

- **E-mail sécurité** : Adresse e-mail dédiée aux rapports d'événements de sécurité
- **Téléphone/Hotline** : Numéro de contact pour les urgences de sécurité
- **Système de billetterie** : Soumission formelle de tickets pour les événements non urgents
- **Option anonyme** : Mécanisme pour le signalement anonyme le cas échéant

**Déclaration anonyme** : Le signalement anonyme DOIT être supporté par : (a) Un alias e-mail dédié ne nécessitant pas d'authentification ; (b) Un formulaire web accessible sans connexion ; ou (c) Une hotline tierce si implémentée. **Limitations** : Le signalement anonyme peut empêcher les questions de suivi et les retours détaillés. Les déclareurs sont encouragés à fournir des coordonnées lorsqu'ils le souhaitent, avec assurance de confidentialité conformément à la Section 3.4.1.

**3.1.3 Accessibilité des canaux**

Les canaux de déclaration DOIVENT être :

- Publiés sur l'intranet et inclus dans les supports de sensibilisation à la sécurité
- Inclus dans les supports d'intégration des employés
- Affichés dans les espaces communs et sur les écrans de connexion
- Accessibles sans nécessiter d'accès au système (pour signaler les problèmes d'accès)

## Événements à déclarer

[Organisation] DOIT définir ce qui constitue un événement de sécurité à déclarer.

**3.2.1 Distinction Événement / Incident**

| Terme | Définition |
|-------|------------|
| **Événement de sécurité** | Occurrence identifiée indiquant une *possible* violation de politique ou défaillance de contrôle |
| **Incident de sécurité** | Événement qui a été évalué comme ayant une *probabilité significative* de compromettre les opérations ou de menacer la sécurité |

**Le personnel déclare les ÉVÉNEMENTS. L'Équipe sécurité évalue si les événements constituent des INCIDENTS.**

**3.2.2 Catégories d'événements à déclarer**

Le personnel DOIT déclarer les catégories d'événements suivantes :

**Hameçonnage et ingénierie sociale** :

- E-mails suspects demandant des identifiants ou des informations sensibles
- Appels téléphoniques ou SMS suspects
- Tentatives de manipulation pour contourner les contrôles de sécurité

**Logiciels malveillants et compromission de systèmes** :

- Comportement système inattendu ou problèmes de performance
- Fenêtres contextuelles, messages ou notifications suspects
- Infection suspectée par un logiciel malveillant (NOUVEAU dans ISO 27002:2022)
- Indicateurs de rançongiciel

**Accès non autorisé** :

- Tentatives de connexion inconnues ou inattendues à vos comptes
- Appareils inconnus connectés à vos comptes
- Verrouillages de comptes ou changements de mots de passe inattendus
- Modifications suspectes de privilèges

**Violation et fuite de données** :

- E-mails mal envoyés contenant des informations sensibles
- Accès non autorisé ou exposition de données
- Documents contenant des données organisationnelles perdus ou volés
- Exfiltration de données suspectée

**Sécurité physique** :

- Appareils perdus ou volés (ordinateurs portables, téléphones, clés USB)
- Talonnage ou accès physique non autorisé
- Équipements manquants
- Personnes suspectes dans des zones sécurisées

**Violations de politique** :

- Contournement observé des contrôles de sécurité
- Violations connues des politiques de sécurité par des tiers
- Modifications de système non traitées via la gestion des changements (NOUVEAU dans ISO 27002:2022)

**Spécifiques au télétravail** :

- Compromission suspectée du réseau domestique
- Accès non autorisé à l'appareil de travail par des tiers
- Problèmes VPN ou d'accès distant suggérant une attaque
- Activité suspecte lors du travail depuis des emplacements publics
- Tentatives d'accès aux systèmes organisationnels depuis des appareils non approuvés
- Demandes suspectes de support IT pour les identifiants d'accès distant
- Modifications de la configuration du routeur domestique non initiées par l'utilisateur
- Observation physique des supports de travail par des personnes non autorisées

## Procédures de déclaration

[Organisation] DOIT définir des procédures de déclaration claires.

**3.3.1 Quoi déclarer**

Les rapports DOIVENT inclure (lorsque disponible) :

- Date et heure de l'observation
- Description de l'événement
- Systèmes ou actifs potentiellement affectés
- Actions déjà prises (le cas échéant)
- Coordonnées pour le suivi (sauf signalement anonyme)
- Toute preuve à l'appui (captures d'écran, en-têtes d'e-mail)

**3.3.2 Délais de déclaration**

| Gravité de l'événement | Délai de déclaration |
|------------------------|---------------------|
| **Critique** (attaque active, violation de données, rançongiciel) | Immédiatement |
| **Élevé** (appareil perdu, compromission des identifiants) | Dans l'heure |
| **Moyen** (tentative de hameçonnage, activité suspecte) | Dans les 4 heures |
| **Faible** (préoccupation de politique, observation générale) | Dans les 24 heures |

**Détermination de la gravité** : Les déclareurs DOIVENT faire leur rapport en fonction de leur meilleure appréciation de la gravité. En cas d'incertitude entre les niveaux de gravité, déclarer au niveau le plus élevé pour garantir une réponse rapide. L'Équipe de Sécurité IT réévaluera la gravité lors du triage initial. Les déclareurs NE DOIVENT PAS retarder le signalement pour déterminer la classification précise.

**3.3.3 Responsabilités du déclareur**

Le personnel déclarant des événements DOIT :

- Déclarer rapidement conformément aux délais ci-dessus
- Fournir des informations exactes au mieux de ses connaissances
- Préserver les preuves potentielles : pour les e-mails de hameçonnage, transférer en pièce jointe pour préserver les en-têtes (ne pas transférer dans le corps ni cliquer sur les liens) ; pour les anomalies système, faire des captures d'écran des messages d'erreur et noter l'heure exacte et les systèmes affectés ; pour les événements de sécurité physique, photographier si la sécurité le permet. Ne jamais compromettre sa sécurité personnelle pour collecter des preuves
- NE PAS tenter d'investiguer ou de vérifier l'événement par lui-même
- NE PAS tenter de tester ou d'exploiter des vulnérabilités suspectées
- Coopérer à toute investigation de suivi

## Culture sans reproche

[Organisation] DOIT favoriser un environnement non punitif pour la déclaration des événements de sécurité.

**3.4.1 Principes sans reproche**

| Principe | Engagement |
|----------|-----------|
| **Protection de bonne foi** | Le personnel qui déclare des événements de bonne foi NE DOIT PAS faire face à des conséquences négatives pour l'acte de déclaration |
| **Traitement des erreurs honnêtes** | Les erreurs honnêtes déclarées rapidement DOIVENT être traitées de manière constructive, en se concentrant sur l'apprentissage et l'amélioration |
| **Aucune représaille** | Les représailles contre les déclareurs de bonne foi sont interdites et passibles de mesures disciplinaires |
| **Confidentialité** | L'identité du déclareur DOIT être protégée dans la mesure du possible |

**3.4.2 Encouragement du signalement**

[Organisation] DOIT :

- Reconnaître le personnel qui adopte un comportement de signalement exemplaire
- Utiliser les événements déclarés comme opportunités d'apprentissage, pas de sanction
- Communiquer la valeur du signalement par les programmes de sensibilisation
- Fournir des retours sur les événements déclarés pour démontrer que des mesures sont prises

**Vérification** : L'efficacité de la culture sans reproche peut être évaluée par les tendances des volumes de signalement (des volumes en baisse peuvent indiquer une crainte des conséquences et déclencher une révision de la culture), des enquêtes anonymes du personnel sur le confort du signalement, ou l'analyse des délais de signalement. Le benchmarking avec des organisations pairs ou des moyennes sectorielles peut informer l'évaluation de l'adéquation.

**3.4.3 Exceptions**

Les principes sans reproche NE protègent PAS :

- Les violations délibérées de politique déclarées uniquement après découverte
- L'activité malveillante déguisée en accidentelle
- La négligence répétée après formation et avertissements
- Les faux rapports de mauvaise foi

## Réponse et retours

[Organisation] DOIT répondre aux rapports d'événements de sécurité.

**3.5.1 Délais de réponse**

| Type de réponse | Délai |
|----------------|-------|
| **Accusé de réception** | Dans les 4 heures ouvrables |
| **Évaluation initiale** | Dans les 24 heures |
| **Mise à jour de statut au déclareur** | Dans les 72 heures |
| **Notification de clôture** | À la résolution |

**Vérification** : La conformité aux délais de réponse est mesurée par les indicateurs du système de billetterie, les tableaux de bord de reporting, ou les audits de conformité périodiques.

**3.5.2 Retours aux déclareurs**

[Organisation] DOIT :

- Accuser réception de tous les rapports
- Fournir des mises à jour de statut sur les événements déclarés
- Communiquer les résultats le cas échéant et lorsque permis
- Utiliser les enseignements tirés pour améliorer le processus de déclaration
- Remercier les déclareurs pour leur contribution à la sécurité organisationnelle

**3.5.3 Escalade**

Les événements DOIVENT être escaladés conformément à ISMS-POL-A.5.24-28 (Cycle de vie de la gestion des incidents) lorsque :

- L'événement est évalué comme un incident de sécurité confirmé
- L'événement nécessite des ressources au-delà de l'équipe de réponse initiale
- L'événement a des implications de notification réglementaire
- L'événement affecte plusieurs systèmes ou unités métier

---

# Rôles et responsabilités

## Matrice de responsabilités

| Rôle | Télétravail (A.6.7) | Déclaration des événements (A.6.8) |
|------|--------------------|------------------------------------|
| **Direction générale** | Approuver la politique de télétravail ; Fournir les ressources | Promouvoir la culture sans reproche ; Recevoir les briefings sur les incidents critiques |
| **RSSI** | Définir les exigences de sécurité ; Autoriser les exceptions ; Réviser la conformité | Définir les mécanismes de déclaration ; Superviser la réponse ; Rendre compte au management |
| **Équipe Sécurité IT** | Mettre en œuvre les contrôles techniques ; Surveiller la conformité ; Évaluer les risques | Recevoir les rapports ; Évaluer les événements ; Coordonner la réponse ; Fournir des retours |
| **Opérations IT** | Déployer l'accès distant ; Maintenir le VPN/AMF ; Soutenir les appareils | Soutenir les canaux de déclaration ; Mettre en œuvre des mesures de confinement |
| **RH** | Gérer les accords de télétravail ; Coordonner les résiliations | Inclure le signalement dans l'intégration ; Traiter les incidents liés au personnel |
| **Responsables hiérarchiques** | Autoriser le télétravail ; Assurer la conformité de l'équipe | Encourager le signalement ; Escalader les préoccupations de l'équipe |
| **Tout le personnel** | Se conformer aux exigences de télétravail ; Sécuriser les appareils et les données | Déclarer les événements rapidement ; Préserver les preuves ; Coopérer aux investigations |

---

# Gouvernance et conformité

## Révision de la politique

| Aspect | Exigence |
|--------|----------|
| **Fréquence de révision** | Annuelle, ou lors de changements significatifs |
| **Autorité de révision** | RSSI avec approbation de la Direction générale |
| **Révisions déclenchées** | Incident de sécurité majeur, changement réglementaire, changement technologique, restructuration organisationnelle |
| **Périmètre de révision** | Efficacité de la politique, indicateurs de conformité, tendances des incidents, alignement réglementaire |

## Surveillance de la conformité

[Organisation] DOIT surveiller la conformité à cette politique par :

**Conformité au télétravail** :

- Révision périodique des autorisations de télétravail
- Contrôles de conformité technique (utilisation du VPN, statut de l'AMF, chiffrement des appareils)
- Évaluations de la référence de sécurité pour les appareils distants
- Audit des journaux d'accès distant

**Conformité à la déclaration des événements** :

- Suivi de la disponibilité des canaux de déclaration
- Analyse des indicateurs de déclaration des événements
- Révision des délais de réponse
- Évaluation des retours des déclareurs

## Non-conformité

**5.3.1 Conséquences de la non-conformité**

Les violations de cette politique peuvent entraîner :

- Révocation des privilèges de télétravail
- Formation à la sécurité supplémentaire obligatoire
- Mesure disciplinaire conformément aux politiques RH
- Résiliation de l'emploi ou du contrat pour les violations graves
- Action en justice en cas d'activité criminelle

**5.3.2 Signalement de la non-conformité**

La non-conformité observée DOIT être signalée à :

- Le Responsable hiérarchique (pour les problèmes des membres de l'équipe)
- La Sécurité IT (pour les violations techniques)
- Les RH (pour les questions liées au personnel)
- Le RSSI (pour les violations significatives ou répétées)

## Gestion des exceptions

**5.4.1 Processus d'exception**

Les exceptions à cette politique nécessitent :

- Justification métier documentée
- Évaluation des risques de l'exception
- Contrôles compensatoires le cas échéant
- Approbation du RSSI (ou délégué)
- Durée limitée dans le temps avec date de révision
- Documentation dans le registre des exceptions

**5.4.2 Autorité des exceptions**

| Type d'exception | Autorité d'approbation |
|-----------------|----------------------|
| Exceptions standard (déviations mineures) | Responsable de la Sécurité IT |
| Exceptions à haut risque (données sensibles, durée prolongée) | RSSI |
| Dérogations à la politique (exigences fondamentales) | Direction générale |

---

# Intégration avec d'autres contrôles

## Contrôles connexes

| Contrôle | Relation |
|----------|----------|
| **A.5.1-2-6.1-2** (Emploi sécurisé et rôles) | Responsabilités du personnel, vérification, conditions d'emploi |
| **A.5.10** (Utilisation acceptable) | Définit l'utilisation acceptable des actifs incluant les scénarios de télétravail |
| **A.5.11** (Restitution des actifs) | Restitution des équipements à la résiliation du télétravail |
| **A.5.17** (Informations d'authentification) | Exigences de mots de passe et d'authentification |
| **A.5.24-28** (Gestion des incidents) | Voie d'escalade pour les événements de sécurité devenant des incidents |
| **A.6.3** (Sensibilisation et formation) | Formation sur la sécurité du télétravail et la déclaration des événements |
| **A.7.7** (Bureau propre) | Les exigences de bureau propre s'étendent aux environnements distants |
| **A.8.1-7-18-19** (Sécurité des postes de travail) | Sécurité des appareils, protection contre les logiciels malveillants pour les appareils distants |
| **A.8.5** (Authentification sécurisée) | AMF et exigences d'authentification |
| **A.8.20-22** (Sécurité réseau) | VPN et sécurité réseau pour les connexions distantes |

## Ressources de mise en œuvre

**Orientations de mise en œuvre** (Suite ISMS-IMP-A.6.7-8) :

- ISMS-IMP-A.6.7-8.S1 : Évaluation de l'autorisation de télétravail et des politiques
- ISMS-IMP-A.6.7-8.S2 : Évaluation des contrôles techniques (VPN, AMF, Chiffrement)
- ISMS-IMP-A.6.7-8.S3 : Évaluation de la sécurité des postes de travail et physique
- ISMS-IMP-A.6.7-8.S4 : Évaluation des mécanismes de déclaration des événements

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

Preuves requises pour démontrer que cette politique est adéquatement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-A.6.7-8 v1.0)
- ✅ Signatures d'approbation du RSSI, DRH, Direction générale
- ✅ Procédure d'autorisation de télétravail documentée
- ✅ Documentation des canaux de déclaration publiée
- ✅ Supports de formation sur le télétravail et la déclaration des événements
- ✅ Registre des exceptions avec approbations documentées
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

Preuves requises pour démontrer que cette politique est opérationnellement efficace :

- Échantillons d'autorisation de télétravail (arrangements approuvés)
- Dossiers d'accusés de réception des politiques par le personnel
- Dossiers de formation complétée pour la formation télétravail/déclaration
- Rapports de conformité technique (utilisation du VPN, inscription AMF, statut du chiffrement des appareils)
- Rapports d'événements de sécurité échantillonnés démontrant l'utilisation du mécanisme
- Dossiers de réponse montrant une réponse rapide aux événements déclarés
- Tableau de bord des indicateurs de conformité montrant les niveaux de conformité à la politique

**Conservation des preuves :**

- Versions de la politique : Durée du SMSI + 3 ans
- Dossiers d'autorisation : Durée de l'arrangement + 2 ans
- Dossiers de formation : Durée de l'emploi + 2 ans
- Rapports d'événements : 3 ans minimum (ou selon les exigences réglementaires)
- Évaluations de conformité : 3 ans minimum

---

# Annexe A : Exigences de documentation de soutien

Cette politique nécessite la documentation de soutien suivante à développer et maintenir par [Organisation]. Il s'agit de documents opérationnels appartenant aux propriétaires de processus respectifs, et non d'une partie intégrante du cadre central de politiques du SMSI.

## A.1 Documentation du télétravail

| Type de document | Objet | Propriétaire |
|-----------------|-------|-------------|
| **Formulaire d'autorisation de télétravail** | Demande formelle et approbation des arrangements de télétravail | RH |
| **Reconnaissance des exigences de sécurité du télétravail** | Reconnaissance par le personnel des exigences de sécurité | RH/Sécurité IT |
| **Accord de télétravail** | Conditions et modalités des arrangements de télétravail | RH/Juridique |
| **Auto-évaluation de la sécurité du bureau à domicile** | Liste de contrôle pour que le personnel évalue la sécurité de son espace de travail | Sécurité IT |

## A.2 Documentation de la déclaration des événements

| Type de document | Objet | Propriétaire |
|-----------------|-------|-------------|
| **Formulaire de déclaration d'événement de sécurité** | Formulaire standardisé pour déclarer les événements de sécurité | Sécurité IT |
| **Guide de classification des événements** | Orientations sur les catégories d'événements et les niveaux de gravité | Sécurité IT |
| **Référence rapide des canaux de déclaration** | Coordonnées et procédures de déclaration | Sécurité IT |
| **Modèle d'accusé de réception des rapports** | Modèle pour accuser réception des rapports reçus | Sécurité IT |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Directeur des Ressources Humaines (DRH)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences relatives au télétravail et à la déclaration des événements de sécurité de l'information. Les procédures de mise en œuvre, les modèles d'évaluation et les orientations détaillées sont documentés dans ISMS-IMP-A.6.7-8 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-01 -->
