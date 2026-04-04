<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.24-FR:operational:OP-POL:a.8.24 -->
**ISMS-OP-POL-A.8.24 — Utilisation de la cryptographie**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Utilisation de la cryptographie |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.24 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
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

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.24 — Utilisation de la cryptographie

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la cryptographie |
|----------|-------------------------------|
| A.5.12–13 Classification et étiquetage de l'information | Détermine les exigences de chiffrement selon le niveau de classification |
| A.5.14 Transfert de l'information | Exigences de chiffrement pour les données en transit |
| A.5.23 Sécurité de l'information pour les services cloud | Chiffrement au repos et en transit pour les données hébergées dans le cloud |
| A.5.31 Exigences légales, réglementaires et statutaires | Contrôles à l'exportation, obligations de chiffrement nLPD/RGPD |
| A.8.1 Appareils des utilisateurs finaux | Chiffrement intégral du disque, contrôles cryptographiques au niveau des appareils |
| A.8.5 Authentification sécurisée | Protection cryptographique des identifiants d'authentification |
| A.8.10 Suppression des informations | L'effacement cryptographique comme méthode de suppression sécurisée |
| A.8.13 Sauvegarde des informations | Exigences de chiffrement des sauvegardes |
| A.8.20 Sécurité des réseaux | TLS/IPsec pour le chiffrement du transport réseau |
| A.8.28 Codage sécurisé | Utilisation de bibliothèques cryptographiques approuvées dans le développement |

**Politiques internes associées** :

- Politique de classification et de traitement de l'information
- Politique de transfert de l'information
- Politique de contrôle d'accès
- Politique de sauvegarde
- Politique de développement sécurisé

---

# Politique d'utilisation de la cryptographie

## Finalité

La présente politique a pour objet de garantir l'utilisation correcte et efficace de la cryptographie pour protéger la confidentialité, l'intégrité et l'authenticité des informations.

La présente politique soutient la nLPD (revLPD) suisse et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger les données personnelles (y compris les données personnelles sensibles). Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également. Le chiffrement est une mesure technique clé pour démontrer la conformité aux obligations de protection des données dans les deux cadres réglementaires.

## Champ d'application

Les informations confidentielles et personnelles traitées, stockées ou transmises dans les systèmes et applications possédés, gérés et contrôlés par l'organisation considérés dans le périmètre par la déclaration de périmètre ISO 27001.

Tous les employés et utilisateurs tiers.

## Principe

Les informations sont protégées par des mesures cryptographiques basées sur leur classification telle que définie dans la Politique de classification et de traitement de l'information et sur l'évaluation des risques.

Seules les technologies et processus de chiffrement approuvés par l'organisation doivent être utilisés.

L'exportation de technologies de chiffrement ou de données chiffrées peut être soumise à des restrictions réglementaires, y compris les dispositions suisses sur le contrôle des exportations et l'Arrangement de Wassenaar. Le personnel doit consulter le service juridique si l'exportation de technologies cryptographiques ou de données chiffrées est requise.

La gestion des clés cryptographiques est fondée sur des normes reconnues par le secteur, notamment le NIST SP 800-57 et les lignes directrices de gestion des clés OWASP. Les clés cryptographiques sont classifiées Confidentiel.

---

## Mesures cryptographiques

### Algorithmes approuvés et longueurs de clés

L'organisation doit utiliser les normes cryptographiques minimales suivantes :

| Cas d'usage | Algorithme | Exigence minimale |
|------------|-----------|------------------|
| Chiffrement symétrique | AES | 256 bits |
| Chiffrement asymétrique | RSA | 2 048 bits minimum ; 4 096 bits recommandé |
| Chiffrement asymétrique | ECDSA/ECDH | P-256 minimum ; P-384 recommandé |
| Fonctions de hachage | Famille SHA-2 | SHA-256 minimum ; SHA-384/SHA-512 pour les usages à haute assurance |
| Signatures numériques | RSA | 2 048 bits minimum ; 4 096 bits recommandé |
| Signatures numériques | ECDSA | P-256 minimum |
| Dérivation de clés | PBKDF2, scrypt, Argon2 | Conformément aux directives NIST actuelles |

**Algorithmes interdits :** MD5, SHA-1, DES, 3DES, RC4, RSA inférieur à 2 048 bits. Ces algorithmes ne doivent être utilisés à aucune fin.

L'organisation doit surveiller les normes de cryptographie post-quantique NIST (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA) et planifier la migration à mesure que les calendriers d'adoption sont établis. Une évaluation d'agilité cryptographique doit être conduite pour identifier les systèmes et dépôts de données nécessitant une planification de migration vers la cryptographie post-quantique, en priorisant les clés à longue durée de vie et les données avec des périodes de conservation dépassant 10 ans.

### Sécurité de la couche de transport

Toutes les communications réseau transportant des données confidentielles ou personnelles doivent utiliser un transport chiffré :

- TLS 1.2 est la version minimale acceptable.
- TLS 1.3 est préféré et doit être utilisé lorsqu'il est pris en charge.
- TLS 1.0 et TLS 1.1 doivent être désactivés sur tous les systèmes.
- SSL (toutes versions) doit être désactivé sur tous les systèmes.
- Seules les suites de chiffrement utilisant AEAD (p. ex. AES-GCM) doivent être activées dans la mesure du possible.

### Chiffrement des appareils mobiles, portables et des supports amovibles

Les appareils mobiles, ordinateurs portables et supports amovibles doivent avoir le chiffrement intégral du disque activé au niveau matériel ou du système d'exploitation.

- Le chiffrement des appareils ne doit pas être désactivé.
- L'accès au stockage chiffré doit être protégé par un mot de passe, une phrase de passe, un code PIN ou une authentification biométrique.
- Seuls les supports amovibles possédés et gérés par l'organisation peuvent être utilisés pour stocker des données confidentielles.

### Chiffrement des courriels

Les courriels ne doivent pas être utilisés pour transférer des données confidentielles ou personnelles en format non chiffré, conformément à la Politique de transfert de l'information.

Lorsque des données confidentielles doivent être envoyées par courriel, une pièce jointe chiffrée doit être utilisée avec une longueur de clé satisfaisant aux exigences minimales d'algorithme approuvé ci-dessus.

L'organisation doit évaluer et approuver une solution de chiffrement des courriels adaptée à ses besoins. En attendant le déploiement d'une solution, des pièces jointes chiffrées avec échange de clé hors bande doivent être utilisées à titre de mesure provisoire.

### Chiffrement des services web et cloud

Les services web et cloud qui traitent, stockent ou transmettent des données confidentielles ou personnelles doivent mettre en œuvre TLS 1.2 au minimum pour protéger les données en transit.

Tous les serveurs doivent avoir un certificat valide émis par une Autorité de certification reconnue. Les propriétaires de systèmes sont responsables du renouvellement des certificats et de la mise à jour des systèmes avant expiration.

### Chiffrement sans fil

- WEP ne doit pas être utilisé.
- WPA3 est préféré pour tous les réseaux sans fil.
- Le mode WPA2 Entreprise avec authentification 802.1X et chiffrement AES est la norme minimale acceptable.
- Le mode WPA2 Personnel peut être utilisé pour les réseaux non-production avec une phrase de passe aléatoire d'au moins 16 caractères et le chiffrement AES.

### Chiffrement des sauvegardes

Les sauvegardes contenant des données confidentielles ou personnelles doivent être chiffrées à l'aide de la technologie de chiffrement approuvée par l'organisation satisfaisant aux exigences minimales d'algorithme ci-dessus.

Le chiffrement des sauvegardes ne doit pas reposer uniquement sur des mécanismes propriétaires des fournisseurs sans garantie documentée de la norme de chiffrement utilisée.

### Chiffrement des bases de données

Les bases de données contenant des informations confidentielles ou des données personnelles doivent être chiffrées au repos au niveau de la couche applicative de la base de données ou au niveau du disque/volume.

Lorsque le chiffrement intégral du disque ou du volume est utilisé, l'effacement cryptographique (destruction de la clé de chiffrement) peut être utilisé comme méthode valide de suppression sécurisée, à condition que le risque soit évalué et que l'approche soit documentée et approuvée.

### Chiffrement des données en mouvement

Le transfert d'informations confidentielles et personnelles doit utiliser des canaux chiffrés. Le chiffrement est requis pour :

- Le transport de fichiers sensibles (SFTP, SCP ou transfert chiffré équivalent).
- Tout le trafic réseau pour l'accès à distance (VPN ou équivalent).
- Les requêtes de bases de données ou appels de services web transmettant des données sensibles.
- L'accès à privilèges aux équipements réseau ou aux serveurs (SSH ; Telnet est interdit).

### Bluetooth

Bluetooth ne doit pas être utilisé comme méthode de communication pour des données confidentielles, personnelles ou autrement sensibles non chiffrées. Voir la Politique de transfert de l'information.

---

## Gestion des clés cryptographiques

### Génération des clés

Les clés cryptographiques doivent être générées au sein de modules cryptographiques conformes au minimum FIPS 140-2 ou FIPS 140-3, ou d'une assurance validée équivalente.

Toute valeur aléatoire requise pour la génération des clés doit être générée au sein du module cryptographique à l'aide d'un générateur de bits aléatoires validé.

Les modules cryptographiques matériels (HSM) sont préférés aux modules logiciels pour la protection des clés à valeur élevée.

### Distribution des clés

Les clés doivent être transportées via des canaux sécurisés. Le matériel de clé ne doit pas être transmis en clair sur un réseau.

### Stockage des clés

- Les clés ne doivent jamais être stockées en format en clair.
- Les clés doivent être stockées dans un coffre cryptographique, un HSM ou un service de gestion de clés (KMS) cloud.
- Les clés ne doivent pas être codées en dur dans le code source, stockées en clair dans des fichiers de configuration, ou partagées via courriel ou messagerie. Cela s'applique également aux clés API, aux jetons, aux identifiants de service et autres secrets — ceux-ci doivent être gérés via une solution de gestion des secrets dédiée (p. ex. AWS KMS, Azure Key Vault, HashiCorp Vault, ou équivalent). Les secrets ne nécessitent pas les mêmes normes de chiffrement au repos que les clés de chiffrement des données mais ne doivent jamais être stockés en clair et doivent être renouvelés selon les périodes de rotation des clés ci-dessus.
- Les clés de chiffrement des clés (KEK) utilisées pour envelopper les clés stockées doivent être au moins aussi robustes que les clés qu'elles protègent.
- Des protections d'intégrité doivent être appliquées aux clés pendant leur stockage.

### Contrôle d'accès aux clés

L'accès aux clés cryptographiques doit suivre le principe du moindre privilège.

- Les accès administratif et opérationnel aux clés doivent être séparés dans la mesure du possible.
- L'authentification multifacteur doit être requise pour les détenteurs de clés.
- Un registre des personnes ayant accès au matériel de clé doit être maintenu.

### Rotation des clés

Les périodes de rotation des clés doivent être définies en fonction du type de clé, du risque et des exigences réglementaires.

Les clés doivent être renouvelées immédiatement en cas de compromission suspectée ou confirmée, quelle que soit la rotation planifiée.

**Périodes minimales de rotation des clés** :

| Type de clé | Durée de vie maximale |
|------------|----------------------|
| Certificats TLS/SSL | 398 jours (conformément au référentiel CA/Browser Forum) |
| Clés de chiffrement des données symétriques (AES) | 2 ans (ou selon les limites de période cryptographique NIST SP 800-57) |
| Paires de clés asymétriques (RSA/ECDSA) | 3 ans |
| Clés API et jetons de service | 90 jours (extensible à 1 an avec acceptation documentée du risque) |
| Clés de chiffrement des bases de données | 1 an |

Des périodes de rotation plus courtes peuvent être requises sur la base d'une évaluation des risques ou d'exigences réglementaires.

### Séquestre et sauvegarde des clés

Le matériel de clé doit être sauvegardé pour permettre la récupération des données chiffrées.

- Le stockage de sauvegarde des clés doit être chiffré avec au moins le même niveau d'assurance que les clés opérationnelles.
- Les clés de signature ne doivent pas être mises sous séquestre.
- Les clés de chiffrement peuvent être mises sous séquestre lorsque les exigences métier le justifient.

### Compromission et récupération des clés

Un plan de récupération en cas de compromission de clés doit être documenté, testé annuellement et maintenu en tant que procédure de référence. Le plan doit inclure :

- Coordonnées du personnel à notifier et de ceux responsables des actions de récupération.
- La méthode et les procédures de renouvellement des clés.
- Un inventaire de toutes les clés cryptographiques et de leur utilisation.
- L'identification de toutes les données ou autres clés protégées par la clé compromise.
- La surveillance des opérations de renouvellement pour confirmer leur achèvement.

### Magasins de confiance

Les magasins de confiance doivent être protégés contre l'injection de certificats racines non autorisés. Les contrôles d'accès doivent être gérés et appliqués par entité et par application.

Un processus sécurisé de mise à jour du magasin de confiance doit être mis en œuvre.

### Bibliothèques cryptographiques

Seules des bibliothèques cryptographiques réputées doivent être utilisées, activement maintenues, régulièrement mises à jour et validées par des organisations tierces (p. ex. NIST/FIPS, Critères communs).

Des implémentations cryptographiques personnalisées ne doivent pas être développées sauf si elles sont spécifiquement approuvées par le RSSI avec une justification documentée.

---

## Optionnel : Contrôles pour les données de carte de paiement (PCI DSS)

*Applicable uniquement si des données de carte de paiement sont traitées et si un périmètre PCI existe.*

Si un périmètre PCI existe, les exigences supplémentaires suivantes s'appliquent :

- Les clés secrètes et privées utilisées pour chiffrer/déchiffrer les données de titulaire de carte doivent être stockées chiffrées avec une clé de chiffrement de clé au moins aussi robuste que la clé de chiffrement des données, stockées séparément de la clé de chiffrement des données, ou au sein d'un appareil approuvé PTS ou d'un HSM.
- Le chiffrement de l'environnement des données de titulaire de carte doit satisfaire aux exigences PCI DSS en plus de la présente politique.

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

- **Inventaire cryptographique** (algorithmes, longueurs de clés, protocoles utilisés sur les systèmes) — *maintenu trimestriellement par la Sécurité IT*
- **Résultats d'analyse de configuration TLS** (p. ex. SSL Labs, testssl.sh) — *analyses automatisées mensuelles*
- **Inventaire des certificats et relevés de surveillance des expirations** — *surveillance automatisée, révisée mensuellement*
- **Journaux d'accès KMS et pistes d'audit d'utilisation des clés** — *conservés 12 mois, révisés trimestriellement*
- **Relevés de rotation des clés** — *journalisés dans KMS, audités semestriellement*
- **Documentation de configuration du chiffrement** pour les bases de données, sauvegardes, terminaux — *révisée annuellement*
- **Plan de récupération en cas de compromission de clé** (documenté et testé annuellement)

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, notamment les audits de configuration technique, les analyses TLS/certificats, les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée par le Responsable de la sécurité de l'information à l'avance, avec acceptation documentée du risque, mesures compensatoires et date de révision définie. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

## Non-conformité

Un employé reconnu avoir violé la présente politique peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les modifications des normes cryptographiques, les menaces émergentes (y compris les développements de la cryptographie post-quantique), les changements réglementaires et les enseignements tirés des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique d'utilisation de la cryptographie — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.1 Appareils des utilisateurs finaux |
| | **8.24 Utilisation de la cryptographie** |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales pour la sécurité des données |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement (chiffrement comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.24 — Utilisation de la cryptographie |
| ISO/IEC 27002:2022 | Section 8.24 — Lignes directrices de mise en œuvre pour les mesures cryptographiques |
| NIST SP 800-57 | Recommandations pour la gestion des clés |

<!-- QA_VERIFIED: 2026-03-29 -->
