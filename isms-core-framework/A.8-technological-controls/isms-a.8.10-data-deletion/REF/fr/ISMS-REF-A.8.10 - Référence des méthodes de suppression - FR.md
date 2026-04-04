<!-- ISMS-CORE:REF:ISMS-REF-A.8.10-FR-deletion-methods-reference:framework:REF:a.8.10 -->
**ISMS-REF-A.8.10 — Référence des méthodes de suppression**
**Normes d'assainissement des supports et sélection des outils (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des méthodes de suppression |
| **Type de document** | Interne — Référence technique (Non SMSI) |
| **Identifiant du document** | ISMS-REF-A.8.10 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | RSSI (Référence technique — Aucune approbation exécutive requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Opérations IT | Référence technique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Selon les besoins (évolution des technologies et des outils)
**Prochaine date de révision** : [Date + 12 mois]
**Approbateurs** : Responsable des opérations IT / Architecture de sécurité (référence technique, aucune approbation SMSI requise)

**Distribution** : Opérations IT, Ingénierie de sécurité, Propriétaires de systèmes (pour sensibilisation à la mise en œuvre technique)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à titre d'information et de sensibilisation uniquement.

- Ce document NE fait PAS partie du Système de Management de la Sécurité de l'Information (SMSI).
- Ce document ne définit PAS de contrôles ou d'exigences de suppression obligatoires.
- Ce document N'établit PAS d'exigences contraignantes, de délais, d'ICP ou de SLA.
- Ce document NE mandate PAS l'utilisation, l'interdiction ou la configuration d'outils, de fournisseurs ou de plateformes de suppression spécifiques.
- Ce document NE remplace ni n'étend aucune politique SMSI.

Toutes les exigences contraignantes de suppression, les obligations et les décisions de gouvernance sont définies exclusivement dans **ISMS-POL-A.8.10 (Politique de suppression de l'information)** et dans les autres documents SMSI approuvés.

Ce document sert uniquement de référence technique pour :

- Décrire les méthodes de suppression et les techniques d'assainissement des supports couramment utilisées
- Suivre l'évolution des normes sectorielles et la disponibilité des outils
- Soutenir la sensibilisation à la sélection des méthodes de suppression
- Informer les discussions techniques et la planification de mise en œuvre future
- **Ce document ne doit pas être utilisé comme preuve d'audit de la mise en œuvre**

L'utilisation de ce document n'implique pas la mise en œuvre, la conformité ou la maturité opérationnelle.

**Déclaration de positionnement critique** : Ce document fournit intentionnellement des détails techniques au-delà de ce qui est requis pour la documentation des politiques ISO/IEC 27001. Son objet est la sensibilisation technique uniquement. Aucune conclusion d'audit ne doit être tirée de la présence, de l'absence ou de la classification d'une méthode de suppression, d'un outil ou d'un fournisseur mentionné ici.

---

## Objet et périmètre du document

**Objet**

Ce document fournit une vue d'ensemble technique des méthodes de suppression et des techniques d'assainissement des supports couramment utilisées pour la suppression de l'information. Il est destiné à soutenir :

- La sensibilisation technique aux options de suppression disponibles
- La compréhension de l'efficacité des méthodes selon le type de support
- Le contexte pour la sélection des méthodes de suppression lors de la mise en œuvre
- Les discussions de planification de mise en œuvre future
- Les critères d'évaluation des outils

## Ce que ce document n'est PAS

Ce document NE :

- Définit PAS les méthodes de suppression approuvées ou interdites de [Organisation]
- N'établit PAS d'exigences de mise en œuvre obligatoires
- Ne crée PAS d'obligations de conformité ou de critères d'audit
- Ne remplace PAS les exigences de la politique ISMS-POL-A.8.10
- N'impose PAS la sélection d'outils spécifiques ou de relations fournisseurs
- N'établit PAS de procédures de suppression ou de processus de vérification

## Relation avec le SMSI

**Relation avec ISMS-POL-A.8.10 Annexe A** : L'Annexe A de ISMS-POL-A.8.10 (Matrice des méthodes de suppression approuvées) fournit la **norme organisationnelle contraignante** pour la sélection des méthodes de suppression. Cette référence technique (ISMS-REF-A.8.10) fournit des détails techniques et un contexte supplémentaires soutenant l'annexe de politique, mais ne remplace ni n'étend les exigences de politique.

Ce document est une **référence technique non contraignante**. Toutes les exigences de contrôle de suppression sont définies exclusivement dans ISMS-POL-A.8.10.

---

# Cadre d'assainissement NIST SP 800-88

## Vue d'ensemble

La Publication spéciale NIST 800-88 Révision 1 (« Lignes directrices pour l'assainissement des supports ») fournit des orientations faisant autorité sur les méthodes d'assainissement des supports. Bien qu'il s'agisse d'une référence informative (non obligatoire sauf si contractuellement requise), elle représente les meilleures pratiques sectorielles.

**Trois catégories d'assainissement** :

1. **Effacement (Clear)** : Appliquer des techniques logiques pour assainir les données dans tous les emplacements de stockage adressables par l'utilisateur, offrant une protection contre les techniques simples et non invasives de récupération de données
2. **Purge (Purge)** : Appliquer des techniques physiques ou logiques pour rendre la récupération des données cibles infaisable en utilisant des techniques de laboratoire à la pointe de l'état de l'art
3. **Destruction (Destroy)** : Rendre le support inutilisable et la récupération des données cibles infaisable en utilisant des techniques de laboratoire à la pointe de l'état de l'art

## Facteurs de décision pour la sélection des méthodes

**Destination du support** :

- Reste sous le contrôle de l'organisation → L'effacement peut être suffisant (selon la classification)
- Quitte le contrôle de l'organisation → Purge minimum
- Mise au rebut / fin de vie → Destruction recommandée pour les données sensibles

**Classification des données** :

- Données Publiques → Effacement suffisant
- Données Internes → Effacement ou Purge
- Données Confidentielles → Purge minimum
- Données Restreintes → Destruction ou Purge avec vérification

**Intention de réutilisation du support** :

- Réutilisation au sein de l'organisation → Effacement ou Purge
- Vente/don externe → Purge ou Destruction
- Mise au rebut → Destruction

---

# Suppression des supports magnétiques (HDD, bandes)

## Disques durs (HDD)

**Caractéristiques du support** :

- Données stockées magnétiquement sur des plateaux rotatifs
- La suppression standard de fichiers ne supprime que les pointeurs du système de fichiers, pas les données réelles
- Les données restent récupérables jusqu'à leur écrasement
- Méthodes d'assainissement bien établies

### Méthodes d'effacement (Clear)

**Écrasement en un seul passage** :

- Écriture d'un motif sur tous les emplacements adressables
- NIST SP 800-88 : Un seul passage suffisant pour les disques modernes
- Les méthodes multi-passages hérités (DoD 5220.22-M, 7 passages) ne sont plus nécessaires selon le NIST
- Outils : `shred` (Linux), `sdelete` (Windows), `dd` (Unix/Linux)
- Efficacité : Adéquate pour les données non sensibles, la réutilisation interne
- Limitations : Ne traite pas les secteurs défectueux ni les zones réservées par le micrologiciel

### Méthodes de purge (Purge)

**ATA Secure Erase** :

- Commande intégrée au disque qui écrase tous les emplacements adressables, y compris les secteurs remappés
- Mis en œuvre par le fabricant, exploite la connaissance par le contrôleur du disque de toutes les zones de stockage
- Commande unique, exécution rapide (généralement 1 à 4 heures pour les disques modernes)
- Outils : `hdparm` (Linux), Parted Magic, utilitaires du fabricant
- Efficacité : Très efficace pour les HDD, méthode recommandée
- Vérification : Vérifier les données SMART ou le statut de complétion de la commande ATA

**Dégazage (Degaussing)** :

- Exposer le disque à un puissant champ magnétique pour perturber les domaines magnétiques
- Rend le disque définitivement inopérable (ne peut pas être réutilisé)
- Nécessite un dégazeur de la Liste des produits évalués de la NSA (EPL) pour les données classifiées
- Efficacité : Très élevée pour les supports magnétiques
- Limitations : Disque inutilisable après le dégazage, équipement coûteux requis
- Cas d'utilisation : Environnements haute sécurité, mise au rebut de données classifiées

### Méthodes de destruction (Destroy)

**Désintégration physique** :

- Déchiqueter le disque en petites particules (≤ 2 mm recommandé selon DIN 66399)
- Incinération à haute température
- Pulvérisation
- Fusion
- Services de prestataires : Prestataires de destruction certifiés NAID AAA
- Efficacité : Niveau le plus élevé, récupération des données infaisable
- Cas d'utilisation : Données de très haute sensibilité, mise au rebut en fin de vie

### Effacement cryptographique pour HDD

**Disques à chiffrement automatique (SED)** :

- Chiffrement intégral du disque basé sur le matériel
- L'effacement cryptographique détruit la clé de chiffrement, rendant les données inaccessibles
- Extrêmement rapide (opération de quelques secondes)
- Nécessite un SED compatible TCG Opal ou ATA Security
- Efficacité : Élevée si le chiffrement était actif avant le stockage des données
- Outils : Utilitaires de gestion TCG Opal, commandes ATA Security (CRYPTO SCRAMBLE)

---

# Suppression des supports à état solide (SSD, mémoire flash)

## Caractéristiques du support SSD

- Les données sont stockées dans des cellules de mémoire flash
- Les méthodes d'écrasement traditionnelles sont moins efficaces en raison de la répartition de l'usure (wear leveling)
- Les SSD peuvent conserver des données dans des zones inaccessibles au système d'exploitation
- Requièrent des méthodes de suppression spécifiques

## Méthodes d'effacement pour SSD

**Commande ATA Secure Erase (SANITIZE BLOCK ERASE)** :

- Efface toutes les cellules flash, y compris les zones de réserve
- Pris en charge par la plupart des SSD modernes
- Recommandé par NIST SP 800-88 pour les SSD
- Outils : `hdparm`, `blkdiscard`, utilitaires fabricant (Samsung Magician, Crucial Storage Executive)
- Vérification : Confirmer l'exécution réussie de la commande SANITIZE

**Effacement cryptographique** :

- Méthode préférée pour les SSD : détruire la clé de chiffrement
- Requiert un SED ou un chiffrement logiciel préalablement activé
- Instantané et efficace même pour les données dans les zones de réserve
- Outils : Utilitaires de gestion TCG Opal, BitLocker (destruction des clés), FileVault (macOS)

## Méthodes de destruction pour SSD

**Destruction physique** :

- Déchiquetage en particules fines (≤ 2 mm pour les données Restreintes)
- Les puces mémoire flash peuvent survivre à l'écrasement du boîtier — les puces elles-mêmes doivent être détruites
- Prestataires certifiés recommandés

---

# Suppression sur support optique (CD, DVD, Blu-ray)

## Caractéristiques du support optique

- Les données gravées physiquement ou par colorant sur le support
- La suppression logique n'est pas possible pour les supports inscriptibles une seule fois (CD-R, DVD-R)
- Les supports réinscriptibles (CD-RW, DVD-RW) peuvent être effacés mais avec limitations

## Méthodes de suppression pour supports optiques

**Destruction physique** (recommandée pour toutes les classifications ≥ Interne) :

- Déchiquetage par un destructeur certifié pour supports optiques
- Désintégration en particules de 6 mm maximum
- Prestataires certifiés NAID recommandés
- Conserver l'attestation de destruction

**Effacement pour supports réinscriptibles** (Données Publiques uniquement) :

- Utilitaires de formatage du système d'exploitation (Windows, macOS)
- Limitations : peut ne pas effacer intégralement — la destruction physique est préférable

---

# Suppression des documents papier

## Méthodes de destruction selon la norme DIN 66399

La norme DIN 66399 définit 7 niveaux de sécurité pour la destruction de documents :

| Niveau | Taille maximale des particules | Cas d'utilisation recommandé |
|--------|-------------------------------|------------------------------|
| P-1 | 2 000 mm² | Données non sensibles (journaux, documents publics) |
| P-2 | 800 mm² | Données Internes générales |
| P-3 | 320 mm² | Données personnelles, documents confidentiels |
| P-4 | 160 mm² | Données confidentielles, informations financières |
| P-5 | 30 mm² | Données Restreintes, données haute sécurité |
| P-6 | 10 mm² | Données top secrètes, utilisation gouvernementale/défense |
| P-7 | 5 mm² | Données extrêmement sensibles, utilisation spéciale |

**Recommandations de [Organisation]** (selon la classification) :

- Documents Publics : P-1 ou P-2 (ou corbeille ordinaire)
- Documents Internes : P-3 minimum
- Documents Confidentiels : P-4 minimum
- Documents Restreints : P-5 minimum

**Déchiqueteurs de bureau** :

- Coupe droite : P-1 uniquement, non recommandé pour documents sensibles
- Coupe croisée : P-3 à P-4, adéquat pour la plupart des usages d'entreprise
- Microcoupe : P-5 à P-6, pour documents hautement sensibles
- Déchiquetage de bureau en vrac : Vérifier la certification DIN 66399

**Prestataires de destruction documentaire** :

- NAID AAA (National Association for Information Destruction) — certification internationale
- Destruction sur site ou hors site
- Attestation de destruction systématiquement fournie

---

# Suppression dans le cloud

## Défis spécifiques au cloud

- Les données peuvent être répliquées dans plusieurs régions géographiques
- Les fournisseurs cloud gèrent leur propre infrastructure de stockage
- Les données peuvent persister dans les sauvegardes, caches, journaux et métadonnées
- La vérification directe de la suppression peut ne pas être possible
- Les délais de rémanence des données varient selon les fournisseurs

## Approche d'effacement cryptographique dans le cloud

**Principe** : Chiffrer toutes les données avec des clés gérées par le client (CMEK — Customer-Managed Encryption Keys) avant le stockage. La suppression des données = destruction des clés de chiffrement.

**Avantages** :

- Efficace même si des copies de données persistent dans les systèmes cloud
- Immédiat (révocation des clés instantanée)
- Auditable (journalisation de la révocation des clés)
- Fonctionne pour toutes les régions et copies répliquées

**Exigences** :

- CMEK activé AVANT le stockage des données
- Clés de chiffrement sous le contrôle de [Organisation]
- Système de gestion des clés externe (AWS KMS, Azure Key Vault, GCP Cloud KMS, ou solution on-premise)
- Processus documenté de révocation et de vérification des clés

## Capacités de suppression par fournisseur cloud

### Amazon Web Services (AWS)

**Objets S3** :

- `s3:DeleteObject` / `s3:DeleteBucket` — suppression des objets et des buckets
- Versionnement S3 : Suppression définitive uniquement via la suppression des marqueurs de version
- Réplication S3 : La suppression se propage aux buckets répliqués
- Délai de rémanence : AWS déclare que les données supprimées ne sont pas accessibles immédiatement mais peuvent persister brièvement
- Recommandation : CMEK + S3 Object Lock (WORM) pour les données à haute conservation

**Volumes EBS** :

- `ec2:DeleteVolume` après `ec2:DetachVolume`
- Les snapshots doivent être supprimés séparément
- Outil de vérification : AWS Config pour confirmer l'absence de volumes EBS orphelins

**RDS (Bases de données)** :

- `rds:DeleteDBInstance` — suppression de l'instance
- Les snapshots automatiques sont supprimés automatiquement selon la politique de conservation
- Les snapshots manuels doivent être supprimés explicitement

### Microsoft Azure

**Stockage Blob** :

- `DeleteBlob` API — suppression des objets individuels
- Soft delete (suppression réversible) : Désactiver ou attendre la période de conservation avant suppression définitive
- Réplication géographique (GRS/GZRS) : La suppression se propage aux régions secondaires dans les minutes suivantes
- Recommandation : Azure Customer-Managed Keys + Azure Purge Protection pour les coffres de clés

**Azure SQL / Managed Instance** :

- Suppression via le portail Azure ou Azure CLI
- Suppression de la base de données + suppression des sauvegardes associées
- Azure Backup : Supprimer les points de récupération séparément

### Google Cloud Platform (GCP)

**Cloud Storage (GCS)** :

- `gcs:DeleteObject` — suppression des objets
- Versionnement d'objet : Supprimer toutes les versions
- Classe de stockage Nearline/Coldline : Peut avoir des frais de suppression anticipée
- CMEK recommandé avec Cloud KMS

**BigQuery** :

- `bq:tables.delete` — suppression des tables
- Les tables supprimées dans un dataset sont récupérables pendant la fenêtre de voyage dans le temps (paramétrable)
- Recommandation : Définir une période de voyage dans le temps = 0 pour les données hautement sensibles avant suppression

---

# Suppression des appareils mobiles

## iOS (iPhone, iPad)

**Effacement à distance** :

- MDM (Mobile Device Management) : Commande d'effacement à distance
- Portail iCloud : Effacement à distance via Localiser mon iPhone
- Apple Business Manager : Effacement géré via MDM
- **Remarque** : L'effacement iOS utilise l'effacement cryptographique — destruction de la clé UID

**Réinitialisation d'usine** :

- Paramètres → Général → Réinitialiser → Effacer contenu et réglages
- Sur les appareils récents avec Secure Enclave : Équivalent à l'effacement cryptographique

**Vérification** :

- L'appareil doit afficher l'écran de configuration initial après l'effacement
- Vérifier que l'appareil est sorti de l'activation MDM
- Documenter : Numéro de série, méthode, date, exécutant

## Android

**Effacement à distance** :

- MDM (Intune, Jamf, etc.) : Effacement complet de l'appareil ou effacement sélectif du profil professionnel
- Google Find My Device : Effacement à distance pour les appareils enregistrés

**Réinitialisation d'usine** :

- Paramètres → Gestion générale → Réinitialiser → Réinitialisation d'usine
- **Avertissement** : La réinitialisation d'usine seule peut ne pas être suffisante sur les appareils anciens sans chiffrement activé
- Recommandation : Activer le chiffrement du stockage avant la réinitialisation d'usine pour les données Confidentielles/Restreintes

---

# Référentiel des outils courants de suppression

## Outils d'effacement sécurisé (Windows)

| Outil | Éditeur | Type | Cas d'utilisation |
|-------|---------|------|-------------------|
| **Eraser** | Open source | Logiciel | Effacement de fichiers et de disques |
| **SDelete** | Microsoft Sysinternals | Utilitaire CLI | Effacement de fichiers Windows |
| **DBAN (Darik's Boot and Nuke)** | Open source | Bootable | Effacement complet du disque |
| **Active@ KillDisk** | LSoft Technologies | Commercial | Effacement professionnel HDD/SSD |
| **BitRaser** | Stellar | Commercial | Effacement certifié avec rapports |
| **Blancco Drive Eraser** | Blancco | Commercial | Effacement certifié entreprise |

## Outils d'effacement sécurisé (Linux/Unix)

| Commande/Outil | Description |
|----------------|-------------|
| `shred` | Effacement de fichiers avec écrasement multiple |
| `dd` + `/dev/zero` ou `/dev/urandom` | Effacement de disques entiers |
| `hdparm -I /dev/sdX` | Vérification du support ATA Secure Erase |
| `hdparm --security-erase` | Exécution d'ATA Secure Erase |
| `blkdiscard` | Suppression des blocs SSD (TRIM/SANITIZE) |
| `wipe` | Effacement sécurisé de fichiers |
| `scrub` | Effacement de données d'appareils |

## Outils d'effacement sécurisé (macOS)

| Outil | Description |
|-------|-------------|
| `diskutil secureErase` | Effacement sécurisé depuis le terminal |
| FileVault (désactivation + suppression clé) | Effacement cryptographique |
| Disk Utility | Interface graphique pour l'effacement de disques |

## Scanners de vérification de suppression

| Outil | Objet |
|-------|-------|
| **Recuva** (Piriform) | Vérification des données récupérables après suppression |
| **PhotoRec** | Récupération pour tester l'efficacité de la suppression |
| **TestDisk** | Analyse des partitions et données résiduelles |
| **Autopsy / Sleuth Kit** | Analyse forensique pour vérification |

---

# Processus de sélection des méthodes de suppression

## Arbre de décision

```
DÉPART : Méthode de suppression requise pour ce support/données

├─ Classification des données = Restreint ?
│  ├─ OUI + Support quitte l'organisation → DESTRUCTION PHYSIQUE
│  ├─ OUI + Support reste dans l'organisation → PURGE + vérification
│  └─ NON → Continuer

├─ Type de support = SSD/Flash ?
│  ├─ OUI → EFFACEMENT CRYPTOGRAPHIQUE (préféré) ou PURGE spécifique SSD
│  └─ NON → Continuer

├─ Type de support = Cloud ?
│  ├─ OUI → EFFACEMENT CRYPTOGRAPHIQUE (CMEK requis)
│  └─ NON → Continuer

├─ Type de support = Papier ?
│  ├─ OUI + Confidentiel/Restreint → DÉCHIQUETAGE P-4/P-5 minimum
│  ├─ OUI + Interne → DÉCHIQUETAGE P-3 minimum
│  └─ OUI + Public → DÉCHIQUETAGE P-1/P-2 ou corbeille

├─ Type de support = HDD magnétique ?
│  ├─ Données Confidentielles/Restreintes → ATA SECURE ERASE ou PURGE
│  ├─ Données Internes → EFFACEMENT (single-pass overwrite) minimum
│  └─ Données Publiques → SUPPRESSION LOGIQUE acceptable

└─ TOUJOURS : Documenter la méthode utilisée et conserver les preuves
```

---

# Standards et référentiels de certification

## Certifications de prestataires de destruction

| Certification | Organisme | Applicabilité |
|--------------|-----------|---------------|
| **NAID AAA** | National Association for Information Destruction | Destruction de supports physiques, documents |
| **e-Stewards** | Basel Action Network | Recyclage et destruction d'équipements électroniques |
| **R2 (Responsible Recycling)** | SERI | Traitement éthique des équipements électroniques |
| **DIN 66399** | Deutsches Institut für Normung | Niveau de sécurité de destruction (particulièrement Europe) |

## Normes d'assainissement

| Norme | Organisme | Statut |
|-------|----------|--------|
| **NIST SP 800-88 Rév. 1** | NIST (USA) | Standard de référence actuel |
| **ISO/IEC 27040:2015** | ISO | Sécurité du stockage |
| **ISO/IEC 27555:2024** | ISO | Suppression des DCP |
| **DoD 5220.22-M** | DoD (USA) | Héritage — remplacé par NIST SP 800-88 |
| **HMG IS5** | UK Government | Suppression des données gouvernementales UK |

---

## Notes de maintenance du document

Cette référence technique peut être mise à jour lors de :

- Publications ou révisions de nouvelles normes (NIST, ISO, DIN)
- Disponibilité de nouveaux outils ou capacités de fournisseurs cloud
- Identification de méthodes ou outils de suppression obsolètes
- Enseignements tirés d'incidents ou d'audits impliquant la suppression

Les mises à jour sont gérées par les Opérations IT / l'Architecture de sécurité et ne nécessitent pas d'approbation SMSI.

---

**FIN DU DOCUMENT DE RÉFÉRENCE TECHNIQUE**

*Pour les exigences de politique contraignantes, consulter ISMS-POL-A.8.10 Politique de suppression de l'information.*

<!-- QA_VERIFIED: 2026-04-02 -->
