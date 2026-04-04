<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.24-FR:framework:POL:a.8.24 -->
**ISMS-POL-A.8.24 – Utilisation de la cryptographie**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Utilisation de la cryptographie |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.24 |
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
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.24.1-UG/TG (Évaluation de la transmission des données)
- ISMS-IMP-A.8.24.2-UG/TG (Évaluation du stockage des données)
- ISMS-IMP-A.8.24.3-UG/TG (Évaluation de l'authentification)
- ISMS-IMP-A.8.24.4-UG/TG (Évaluation de la gestion des clés)
- ISMS-CTX-A.8.24 (Référence du paysage cryptographique — Non SMSI)
- ISO/IEC 27001:2022 Contrôle A.8.24

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles cryptographiques pour protéger la confidentialité, l'intégrité et l'authenticité des informations, conformément au Contrôle A.8.24 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les actifs informationnels, systèmes et personnel manipulant des informations classifiées (Internes, Confidentielles ou Restreintes).

**Objet** : Définir les exigences organisationnelles pour la sélection, la mise en œuvre et la gouvernance des contrôles cryptographiques. Cette politique établit QUELLE protection cryptographique est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.24 (variantes UG/TG).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.24 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.24 — Utilisation de la cryptographie**

> *Une politique sur l'utilisation de contrôles cryptographiques pour la protection de l'information devrait être développée et mise en œuvre.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les contrôles cryptographiques protégeant les informations tout au long de leur cycle de vie.

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de contrôles cryptographiques alignées sur la classification des données
- **Établit** le cadre de gouvernance pour la prise de décision cryptographique
- **Précise** la responsabilisation pour la mise en œuvre des contrôles cryptographiques
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les détails de mise en œuvre techniques** (voir ISMS-IMP-A.8.24)
- **Définit pas les algorithmes approuvés ou les longueurs de clés** (voir ISMS-CTX-A.8.24 et ISMS-IMP-A.8.24)
- **Fournit pas de procédures de configuration spécifiques aux systèmes** (voir ISMS-IMP-A.8.24)
- **Remplace pas l'évaluation des risques** (contrôles cryptographiques sélectionnés selon le traitement des risques)

**Justification** : La séparation entre les exigences de politique et les orientations de mise en œuvre permet la stabilité de la politique malgré l'évolution des normes cryptographiques, et l'agilité technique pour les mises à jour d'algorithmes sans révision de politique.

## Périmètre

**Cette politique s'applique à** :

- Tous les actifs informationnels classifiés Internes, Confidentiels ou Restreints
- Tous les systèmes, applications, réseaux et services traitant des informations organisationnelles
- Toutes les mises en œuvre cryptographiques (chiffrement, hachage, signatures numériques, gestion des clés)
- Tout le personnel (employés, contractants, tiers) ayant accès aux informations organisationnelles
- Tous les services tiers traitant des données organisationnelles

**Hors périmètre** :

- Informations publiques (aucune protection cryptographique requise)
- Contrôles de sécurité non cryptographiques (couverts par d'autres politiques SMSI)

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés |
|----------------|---------------|----------------|
| **nLPD suisse** | Toutes les opérations suisses | Art. 8 — Mesures techniques appropriées incluant le chiffrement |
| **RGPD de l'UE** | Lors du traitement de données personnelles UE | Art. 32 — Chiffrement des données personnelles comme mesure de sécurité |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôle A.8.24 — Politique documentée et mise en œuvre |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Condition de déclenchement | Exigences cryptographiques |
|---------------|---------------------------|---------------------------|
| **PCI DSS v4.0.1** | Traitement de données de cartes de paiement | Cryptographie robuste pour les données de titulaires ; contrôles de gestion des clés |
| **FINMA** | Institution financière réglementée en Suisse | Chiffrement conformément à la Circulaire FINMA 2023/1 |
| **DORA** | Entité de services financiers UE | Chiffrement des systèmes TIC ; agilité cryptographique |
| **NIS2** | Entité essentielle/importante (UE) | Chiffrement comme mesure de gestion des risques en cybersécurité |

**Niveau 3 : Référence informative**

- NIST SP 800-57 (Gestion des clés)
- BSI TR-02102 (Mécanismes cryptographiques)
- ENISA (Algorithmes et tailles de clés)
- OWASP (Stockage cryptographique)

---

# Exigences de contrôles cryptographiques

## Chiffrement des données au repos

[Organisation] DOIT chiffrer les données au repos selon leur classification.

**Exigences par classification** :

| Classification | Exigence de chiffrement au repos |
|----------------|----------------------------------|
| **Restreint** | Chiffrement obligatoire — AES-256 ou équivalent ; gestion des clés via HSM ou KMS |
| **Confidentiel** | Chiffrement obligatoire — AES-256 ou équivalent |
| **Interne** | Chiffrement recommandé pour les données sur appareils mobiles et supports amovibles |
| **Public** | Chiffrement non requis |

**Cas d'usage obligatoires** :

- Données personnelles (DCP) : chiffrement au repos obligatoire
- Données financières sensibles : chiffrement au repos obligatoire
- Données sur appareils mobiles et ordinateurs portables : chiffrement intégral du disque obligatoire (conformément à A.8.1)
- Sauvegardes contenant des données Confidentielles/Restreintes : chiffrement obligatoire

## Chiffrement des données en transit

[Organisation] DOIT chiffrer les données en transit selon leur classification et le canal de communication.

**Exigences générales** :

- Toutes les données Confidentielles et Restreintes DOIVENT être chiffrées en transit
- Les communications Internet contenant des données organisationnelles DOIVENT utiliser TLS 1.2 minimum (TLS 1.3 recommandé)
- Les protocoles non chiffrés (HTTP, FTP non sécurisé, Telnet) DOIVENT être interdits pour les données classifiées
- La confidentialité persistante (Perfect Forward Secrecy — PFS) DOIT être activée pour les services web exposés

**Exigences par protocole** :

| Protocole | Exigence | Standard minimum |
|-----------|----------|-----------------|
| HTTPS (web) | Obligatoire pour toutes les applications web | TLS 1.2+ ; TLS 1.3 recommandé |
| API REST | Obligatoire | TLS 1.2+ |
| SMTP (e-mail) | TLS obligatoire pour relais internes | STARTTLS ou TLS natif |
| Accès distant | VPN ou Zero Trust obligatoire | TLS 1.2+ ou IPsec AES-256 |
| Base de données | Chiffrement en transit recommandé | TLS 1.2+ |

## Gestion des clés cryptographiques

[Organisation] DOIT mettre en œuvre une gestion des clés cryptographiques appropriée.

**Principes de gestion des clés** :

- Les clés DOIVENT être générées de manière sécurisée (générateurs de nombres aléatoires cryptographiques)
- Les clés DOIVENT être stockées séparément des données chiffrées
- Les clés Restreintes DOIVENT être stockées dans un HSM (Hardware Security Module) ou un KMS approuvé
- Les clés DOIVENT avoir une durée de vie définie et être rotées selon un calendrier documenté
- Les clés en fin de vie DOIVENT être détruites de manière sécurisée (pas seulement supprimées)
- Des procédures de récupération des clés DOIVENT exister pour éviter la perte de données

**Cycle de vie des clés** :

| Phase | Exigence |
|-------|---------|
| Génération | Utiliser des sources d'entropie cryptographiquement sûres |
| Distribution | Canaux sécurisés uniquement ; jamais en clair |
| Stockage | HSM ou KMS pour les clés Restreintes ; coffre-fort de mots de passe pour les autres |
| Utilisation | Journalisation de l'utilisation des clés critiques |
| Rotation | Calendrier défini selon la classification des données |
| Révocation | Procédure immédiate en cas de compromission suspectée |
| Destruction | Écrasement sécurisé ou destruction physique (HSM) |

## Signatures numériques et authenticité

[Organisation] DOIT utiliser des signatures numériques pour :

- Authentifier l'origine des logiciels et des mises à jour (vérification des signatures logicielles)
- Signer les documents importants nécessitant une authentification (contrats, approbations)
- Authentifier les e-mails officiels (DKIM, S/MIME)
- Garantir l'intégrité des artefacts logiciels dans les pipelines CI/CD

## Agilité cryptographique

[Organisation] DOIT développer et maintenir une capacité d'agilité cryptographique :

- Les systèmes DOIVENT être conçus pour permettre le changement d'algorithmes cryptographiques sans refontes majeures
- Un inventaire des algorithmes et protocoles cryptographiques utilisés DOIT être maintenu
- Un plan de migration cryptographique (notamment vers la cryptographie post-quantique) DOIT être élaboré
- Les dépendances sur les algorithmes déprécié ou obsolètes DOIVENT être identifiées et planifiées pour migration

---

# Gouvernance des contrôles cryptographiques

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation des exceptions ; supervision de la conformité |
| **Architecte de sécurité** | Sélection et validation des contrôles cryptographiques ; révision de l'agilité crypto |
| **Opérations IT** | Mise en œuvre et maintenance ; gestion des clés opérationnelles ; gestion des certificats |
| **Équipes de développement** | Utilisation d'algorithmes et bibliothèques approuvés dans les applications |
| **Propriétaires de systèmes** | S'assurer que leurs systèmes respectent les exigences cryptographiques |

## Gestion des exceptions

Les exceptions aux exigences cryptographiques DOIVENT être :

- Justifiées par des contraintes techniques documentées
- Assorties de contrôles compensatoires
- Approuvées par le RSSI
- Limitées dans le temps (maximum 12 mois)
- Révisées lors de la révision annuelle de la politique

## Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Systèmes de production utilisant TLS 1.2+ | 100 % | Mensuelle |
| Données Restreintes chiffrées au repos | 100 % | Trimestrielle |
| Sauvegardes chiffrées | 100 % | Mensuelle |
| Certificats expirés | 0 | Continue |
| Clés avec rotation dans les délais | ≥ 95 % | Trimestrielle |

---

# Définitions

**Contrôle cryptographique** : Mécanisme matériel ou logiciel utilisant des algorithmes cryptographiques pour protéger la confidentialité, l'intégrité ou l'authenticité des informations.

**Algorithme approuvé** : Algorithme cryptographique satisfaisant aux normes de sécurité de [Organisation] telles que définies dans ISMS-CTX-A.8.24.

**Gestion des clés** : Processus couvrant l'intégralité du cycle de vie des clés cryptographiques : génération, stockage, distribution, rotation, sauvegarde et destruction.

**Module de sécurité matérielle (HSM)** : Dispositif matériel inviolable pour le stockage sécurisé des clés et les opérations cryptographiques.

**Service de gestion des clés (KMS)** : Service logiciel ou cloud pour la gestion centralisée des clés cryptographiques.

**Agilité cryptographique** : Capacité organisationnelle à changer rapidement d'algorithmes cryptographiques sans refonte majeure des systèmes.

**Confidentialité persistante (PFS)** : Propriété cryptographique garantissant que la compromission des clés à long terme ne compromet pas les clés de session passées.

**Documentation du paysage cryptographique** : ISMS-CTX-A.8.24 (document de référence technique, non contraignant).

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences d'utilisation de la cryptographie. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.24 (UG/TG). La référence du paysage cryptographique est documentée dans ISMS-CTX-A.8.24 (NON SMSI).*

<!-- QA_VERIFIED: 2026-04-02 -->
