<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.23-FR:framework:POL:a.8.23 -->
**ISMS-POL-A.8.23 – Filtrage web**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Filtrage web |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.23 |
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
- ISMS-IMP-A.8.23.1-UG/TG (Évaluation de l'infrastructure de filtrage)
- ISMS-IMP-A.8.23.2-UG/TG (Évaluation de la couverture réseau)
- ISMS-IMP-A.8.23.3-UG/TG (Évaluation de la configuration des politiques)
- ISO/IEC 27001:2022 Contrôle A.8.23

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de filtrage web pour protéger les utilisateurs et les informations organisationnelles contre les menaces basées sur le web, conformément au Contrôle A.8.23 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les segments réseau où les utilisateurs accèdent aux ressources Internet, à l'ensemble du personnel organisationnel et à toutes les technologies de filtrage web quel que soit le modèle de déploiement.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de filtrage web. Cette politique établit QUELLE protection de filtrage web est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.23 (variantes UG/TG).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.23 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.23 — Filtrage web**

> *L'accès aux sites web externes doit être géré pour réduire l'exposition aux contenus malveillants.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les contrôles de filtrage web protégeant les utilisateurs et les informations contre les menaces basées sur le web dans l'ensemble de l'infrastructure réseau de [Organisation].

---

# Exigences de filtrage web

## Catégories de sites web bloqués

[Organisation] DOIT bloquer l'accès aux catégories de sites web suivantes sur tous les réseaux organisationnels :

**Blocage obligatoire (sécurité)** :

- Sites web hébergeant des logiciels malveillants connus ou des téléchargements malveillants
- Sites web de phishing et d'hameçonnage connus
- Domaines de commande et contrôle (C2) associés à des logiciels malveillants
- Sites web d'hébergement de rançongiciels
- Sites web distribuant des logiciels espions ou des logiciels publicitaires
- Flux de renseignements sur les menaces — domaines et IP malveillants

**Blocage obligatoire (conformité légale / risque juridique)** :

- Contenu illégal en vertu du droit suisse (contenu pédopornographique, contenu promouvant la violence)
- Sites web de jeux d'argent non autorisés (selon la réglementation suisse)
- Sites web violant manifestement le droit d'auteur
- Sites web en rapport avec des activités terroristes ou extrémistes

**Blocage recommandé (risque de sécurité élevé)** :

- Réseaux d'anonymisation (proxies web, Tor relays)
- Services de partage de fichiers pair-à-pair non approuvés
- Services de partage de fichiers cloud non gérés par l'organisation (shadow IT)
- Sites web de contournement de pare-feu et de proxies

## Catégories de sites web soumises à surveillance renforcée

Les catégories suivantes DOIVENT être surveillées mais ne sont pas nécessairement bloquées — la décision de blocage DOIT être basée sur l'évaluation des risques de [Organisation] :

- Réseaux sociaux (productivité et risques de fuite de données)
- Services de messagerie personnels (risque de phishing)
- Sites de téléchargement de logiciels (risque de logiciels malveillants)
- Services de stockage cloud personnels (risque d'exfiltration de données)

## Couverture du filtrage web

**Périmètre de couverture obligatoire** :

- Tous les accès Internet depuis les réseaux d'entreprise DOIVENT passer par le filtrage web
- Le filtrage web DOIT couvrir le trafic HTTP et HTTPS (inspection TLS requise pour le trafic HTTPS)
- Les terminaux d'entreprise en télétravail DOIVENT maintenir la protection de filtrage web (via agent ou tunnel VPN)
- La cible de couverture est de ≥ 95 % des accès Internet organisationnels

**Inspection TLS (déchiffrement HTTPS)** :

- L'inspection TLS DOIT être activée pour les catégories de menaces à haut risque
- Les exceptions à l'inspection TLS (par ex. sites bancaires, portails RH) DOIVENT être documentées
- Les utilisateurs DOIVENT être informés de l'inspection TLS dans la politique d'utilisation acceptable
- Les données personnelles décryptées lors de l'inspection TLS DOIVENT être protégées conformément au RGPD/nLPD

## Processus d'exception et de déblocage

**Demandes de déblocage** :

- Les utilisateurs ayant besoin d'accéder à des sites bloqués pour des raisons professionnelles légitimes PEUVENT soumettre une demande de déblocage
- Les demandes DOIVENT inclure : URL/domaine, justification métier, durée (permanente ou temporaire)
- Les demandes DOIVENT être approuvées par le responsable hiérarchique + validation sécurité
- Les accès temporaires DOIVENT être limités dans le temps (maximum 90 jours) et journalisés

**Urgences** :

- En cas d'urgence, les exceptions temporaires PEUVENT être accordées par le Responsable des opérations IT avec notification du RSSI
- Les exceptions d'urgence DOIVENT être révisées dans les 24 heures ouvrables

## Journalisation et surveillance du filtrage web

**Journalisation** :

- Toutes les tentatives d'accès à des sites bloqués DOIVENT être journalisées
- Les journaux DOIVENT inclure : horodatage, identifiant utilisateur (anonymisé si requis), URL tentée, catégorie, action (bloqué/autorisé)
- Les journaux DOIVENT être transmis à la plateforme de journalisation centralisée (conformément à A.8.15)
- Conservation des journaux de filtrage web : 6 mois minimum

**Surveillance** :

- Les tentatives répétées d'accès à des sites web malveillants DOIVENT déclencher des alertes SOC
- Les volumes anormaux de sites bloqués par un utilisateur ou un système DOIVENT être investigués
- Les rapports mensuels de filtrage web DOIVENT être produits et révisés par le RSSI

## Exigences légales pour la surveillance des employés

Conformément au droit suisse (Art. 328b CO) et à la nLPD :

- Le filtrage web et la journalisation associée DOIVENT être mentionnés dans la politique d'utilisation acceptable communiquée aux employés
- Les journaux de navigation web NE DOIVENT PAS être utilisés pour surveiller la productivité individuelle des employés (usage disproportionné)
- L'accès aux journaux nominatifs des employés DOIT être restreint au personnel autorisé (SOC, RSSI) et limité aux investigations de sécurité
- Une conservation disproportionnément longue des données de navigation NE DOIT PAS être maintenue

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; définition des catégories bloquées ; approbation des exceptions |
| **Opérations IT** | Maintenance de l'infrastructure de filtrage ; gestion des exceptions |
| **SOC** | Surveillance des alertes de filtrage ; investigation des tentatives d'accès suspectes |
| **DPD** | Conformité RGPD/nLPD pour la journalisation des accès web ; consultation sur l'inspection TLS |
| **Responsables hiérarchiques** | Approbation des demandes de déblocage de leurs équipes |

---

# Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigences |
|----------------|-----------|
| **nLPD suisse + CO (Art. 328b)** | Proportionnalité de la surveillance ; transparence envers les employés |
| **RGPD de l'UE** | Art. 5 — Traitement licite ; proportionnalité ; Art. 32 — Protection contre les menaces web |
| **ISO/IEC 27001:2022** | Contrôle A.8.23 — Gestion de l'accès aux sites web externes |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Exigences |
|---------------|-----------|
| **PCI DSS v4.0.1** | Contrôle de l'accès web depuis les systèmes traitant des données de cartes |
| **FINMA** | Protection contre les menaces web pour les systèmes financiers |
| **DORA** | Filtrage web dans le cadre de la gestion des risques TIC |

---

# Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Couverture de filtrage web des accès Internet | ≥ 95 % | Mensuelle |
| Blocage des domaines malveillants connus | 100 % | Continue |
| Délai de mise à jour des renseignements sur les menaces | < 1 heure pour les IoC critiques | Continue |
| Taux de faux positifs (déblocages légitimes) | < 2 % | Mensuelle |
| Demandes de déblocage traitées dans les délais | 100 % | Mensuelle |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Délégué à la Protection des Données (DPD)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de filtrage web. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.23 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
