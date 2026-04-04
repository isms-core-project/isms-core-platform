<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.20-22-FR:framework:POL:a.8.20-22 -->
**ISMS-POL-A.8.20-22 – Sécurité des réseaux**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité des réseaux |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.20-22 |
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
- Secondaire : Directeur des Systèmes d'Information (DSI)
- Technique : Responsable des opérations réseau
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.20-22.S1-UG/TG (Découverte du réseau)
- ISMS-IMP-A.8.20-22.S2-UG/TG (Documentation de l'architecture)
- ISMS-IMP-A.8.20-22.S3-UG/TG (Durcissement des équipements)
- ISMS-IMP-A.8.20-22.S4-UG/TG (Sécurité des services)
- ISMS-IMP-A.8.20-22.S5-UG/TG (Mise en œuvre de la segmentation)
- ISMS-IMP-A.8.20-22.S6-UG/TG (Tests de sécurité)
- ISO/IEC 27001:2022 Contrôles A.8.20, A.8.21, A.8.22
- ISMS-POL-A.8.15 (Journalisation)
- ISMS-POL-A.8.16 (Activités de surveillance)
- ISMS-POL-A.5.23 (Services cloud)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de sécurité des réseaux pour protéger les actifs informationnels par une infrastructure réseau sécurisée, des services et une segmentation appropriés, conformément aux Contrôles A.8.20, A.8.21 et A.8.22 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à l'ensemble de l'infrastructure réseau, des équipements réseau, des services réseau et des segments réseau quel que soit le modèle de déploiement (sur site, cloud, hybride) ou la technologie (réseau traditionnel, réseau défini par logiciel — SDN).

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de sécurité des réseaux. Cette politique établit QUELLE protection de sécurité réseau est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.20-22 (variantes UG/TG).

**Approche par contrôles combinés** : Ces trois contrôles sont mis en œuvre comme un cadre unifié car ils opèrent sur la même infrastructure réseau et partagent des processus communs de découverte, d'évaluation et de collecte de preuves. Malgré une mise en œuvre unifiée, chaque contrôle conserve des exigences distinctes pour les besoins de la Déclaration d'applicabilité (DdA).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôles ISO/IEC 27001:2022 A.8.20, A.8.21 et A.8.22

**Norme ISO/IEC 27001:2022 Annexe A.8.20 — Sécurité des réseaux**

> *Les réseaux et les équipements réseau doivent être sécurisés, gérés et contrôlés pour protéger les informations dans les systèmes et applications.*

**Objectif du contrôle** : S'assurer que l'infrastructure et les équipements réseau sont durcis, surveillés et configurés pour prévenir les accès non autorisés et protéger les informations en transit.

**Norme ISO/IEC 27001:2022 Annexe A.8.21 — Sécurité des services réseau**

> *Les mécanismes de sécurité, les niveaux de service et les exigences de service des services réseau doivent être identifiés, mis en œuvre et surveillés.*

**Objectif du contrôle** : S'assurer que les services réseau sont sécurisés, disponibles et surveillés pour soutenir les opérations métier tout en se protégeant contre les attaques basées sur les services.

**Norme ISO/IEC 27001:2022 Annexe A.8.22 — Séparation des réseaux**

> *Les groupes de services d'information, d'utilisateurs et de systèmes d'information doivent être séparés dans les réseaux de l'organisation.*

**Objectif du contrôle** : Mettre en œuvre la segmentation réseau pour limiter le rayon d'impact d'une compromission, appliquer le moindre privilège d'accès réseau et satisfaire aux exigences réglementaires d'isolation des données.

**Indépendance dans la DdA** : Malgré une mise en œuvre et une documentation unifiées, les Contrôles A.8.20, A.8.21 et A.8.22 sont évalués indépendamment dans la DdA. Chaque contrôle conserve des exigences distinctes, une collecte de preuves et une notation de conformité à des fins d'audit.

---

# Exigences de sécurité réseau

## Sécurité de l'infrastructure réseau (A.8.20)

[Organisation] DOIT sécuriser, gérer et contrôler les réseaux et les équipements réseau.

### Durcissement des équipements réseau

**Tous les équipements réseau DOIVENT** :

- Être configurés selon les référentiels de sécurité approuvés (CIS Benchmarks ou équivalents pour les fournisseurs concernés)
- Avoir les services, protocoles et interfaces inutilisés désactivés
- Utiliser des protocoles de gestion sécurisés (SSH v2, HTTPS — pas Telnet, HTTP)
- Être gérés uniquement depuis des réseaux de gestion dédiés
- Avoir l'authentification AMF activée pour l'accès administratif
- Être inclus dans les processus de gestion des correctifs (conformément à A.8.8)

**Gestion des mots de passe des équipements réseau** :

- Tous les identifiants par défaut DOIVENT être modifiés avant le déploiement en production
- Les mots de passe des équipements réseau DOIVENT être stockés dans un coffre-fort de mots de passe approuvé
- Les accès administratifs DOIVENT être nominatifs (pas de comptes partagés)

### Documentation de l'architecture réseau

[Organisation] DOIT maintenir une documentation de l'architecture réseau à jour :

- Topologie réseau (schémas physiques et logiques)
- Inventaire des équipements réseau (conformément à A.5.9)
- Flux de trafic entre les zones de sécurité
- Matrice de contrôle d'accès réseau (règles de pare-feu, ACL)
- Plages d'adresses IP et attribution VLAN

**Fréquence de mise à jour** : La documentation réseau DOIT être mise à jour dans les 5 jours ouvrables suivant tout changement significatif de l'infrastructure.

### Journalisation et surveillance réseau

- Tous les équipements réseau DOIVENT transmettre leurs journaux à la plateforme de journalisation centralisée (conformément à A.8.15)
- Les événements de sécurité réseau DOIVENT être intégrés dans la surveillance SIEM (conformément à A.8.16)
- Les tentatives de connexion réseau non autorisées DOIVENT déclencher des alertes

### Chiffrement des communications réseau

- Les communications contenant des données Confidentielles ou Restreintes DOIVENT être chiffrées en transit
- Protocoles de chiffrement minimaux : TLS 1.2 (TLS 1.3 recommandé)
- Les protocoles non chiffrés (HTTP, FTP non sécurisé, Telnet) DOIVENT être remplacés par leurs équivalents sécurisés
- Les accès distants DOIVENT utiliser des tunnels VPN ou des solutions Zero Trust équivalentes

## Sécurité des services réseau (A.8.21)

[Organisation] DOIT identifier, mettre en œuvre et surveiller les mécanismes de sécurité des services réseau.

### Inventaire des services réseau

[Organisation] DOIT maintenir un inventaire des services réseau incluant :

- Services DNS internes et externes
- Services DHCP
- Services proxy et filtrage web
- Services d'équilibrage de charge
- Services VPN et d'accès distant
- Services cloud natifs (passerelles cloud, CloudFront, etc.)

### Exigences de sécurité par service

**DNS** :

- DNSSEC activé pour les zones DNS critiques
- DNS-over-HTTPS (DoH) ou DNS-over-TLS (DoT) pour les requêtes sortantes
- Filtrage DNS pour les domaines malveillants connus
- Surveillance des requêtes DNS anormales (tunneling DNS, DGA)

**DHCP** :

- DHCP Snooping activé sur les commutateurs de réseau local
- Journal des attributions DHCP conservé pour la corrélation des journaux
- DHCP séparé par VLAN/segment

**Accès distant / VPN** :

- AMF obligatoire pour toutes les connexions VPN
- Vérification de la posture des terminaux avant l'octroi de l'accès VPN
- Split tunneling évalué selon les risques (le tunneling complet est préféré pour les utilisateurs accédant à des données sensibles)
- Journalisation de toutes les connexions VPN

### Surveillance des services réseau

- Disponibilité des services critiques surveillée en continu
- Métriques de performance des services (latence, débit, taux d'erreur) collectées
- Alertes de dégradation des services configurées

## Séparation des réseaux (A.8.22)

[Organisation] DOIT séparer les groupes de services d'information, d'utilisateurs et de systèmes d'information dans ses réseaux.

### Zones de sécurité réseau

[Organisation] DOIT définir et maintenir des zones de sécurité réseau distinctes :

| Zone | Description | Exemples de systèmes |
|------|-------------|---------------------|
| **Zone Internet** | Trafic non fiable en provenance d'Internet | Routeurs de périphérie, interfaces WAN |
| **Zone démilitarisée (DMZ)** | Services exposés à Internet | Serveurs web publics, passerelles API, relais e-mail |
| **Zone de production** | Systèmes métier internes | Serveurs d'applications, bases de données de production |
| **Zone de gestion** | Infrastructure de gestion IT | Consoles d'administration, SIEM, systèmes de sauvegarde |
| **Zone utilisateurs** | Postes de travail et appareils des utilisateurs | Postes de travail, appareils mobiles |
| **Zone de développement** | Systèmes de développement et de test | Serveurs de build, environnements de test |
| **Zone IoT** | Objets connectés (si applicable) | Caméras, contrôleurs d'accès physique |

### Contrôles de segmentation

**Entre les zones** :

- Les flux de trafic entre les zones DOIVENT passer par des contrôles de sécurité (pare-feu, IPS)
- La politique par défaut DOIT être le refus de tout trafic non explicitement autorisé
- Les règles d'autorisation inter-zones DOIVENT être documentées avec justification métier
- Les règles inter-zones DOIVENT être révisées trimestriellement pour supprimer les règles obsolètes

**Isolation des données** :

- Les systèmes traitant des données Restreintes DOIVENT être dans des segments réseau dédiés
- Les systèmes PCI DSS (si applicable) DOIVENT être dans un segment isolé réduisant la portée de l'audit
- Les systèmes de développement/test NE DOIVENT PAS avoir accès aux systèmes de production

**Zero Trust** :

[Organisation] DEVRAIT progresser vers un modèle Zero Trust Network Access (ZTNA) où :

- L'accès est accordé par identité et posture du terminal, pas par emplacement réseau
- La micro-segmentation est appliquée au niveau applicatif
- Toutes les communications sont chiffrées et authentifiées, même en réseau interne

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **RSSI** | Propriétaire de la politique ; définition de la stratégie de sécurité réseau ; approbation des exceptions |
| **Responsable des opérations réseau** | Mise en œuvre des contrôles ; maintenance de l'infrastructure ; gestion des changements réseau |
| **SOC** | Surveillance du réseau ; investigation des incidents réseau |
| **DSI** | Alignement de la stratégie réseau avec les objectifs IT |
| **Propriétaires d'applications** | Définition des exigences de connectivité réseau pour leurs applications |

---

# Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigences |
|----------------|-----------|
| **nLPD suisse** | Art. 8 — Mesures techniques incluant la sécurité réseau |
| **RGPD de l'UE** | Art. 32 — Sécurité du traitement incluant les contrôles réseau |
| **ISO/IEC 27001:2022** | Contrôles A.8.20, A.8.21, A.8.22 |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Exigences réseau spécifiques |
|---------------|------------------------------|
| **PCI DSS v4.0.1** | Exig. 1 — Pare-feu réseau ; isolation du périmètre PCI ; Exig. 4 — Chiffrement des transmissions |
| **FINMA** | Isolation des systèmes critiques ; surveillance réseau |
| **DORA** | Art. 9 — Sécurité réseau des systèmes TIC critiques |
| **NIS2** | Art. 21 — Sécurité des réseaux et systèmes d'information |

---

# Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Équipements réseau avec référentiel de sécurité appliqué | ≥ 95 % | Trimestrielle |
| Documentation de l'architecture réseau à jour | 100 % | Trimestrielle |
| Révision des règles de pare-feu interzone | 100 % | Trimestrielle |
| Incidents réseau liés à des failles de sécurité connues | 0 | Continue |
| Couverture de la segmentation réseau (zones définies) | 100 % | Trimestrielle |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable des opérations réseau** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de sécurité des réseaux. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.20-22 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
