<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.12-FR:framework:POL:a.8.12 -->
**ISMS-POL-A.8.12 – Prévention des fuites de données**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Prévention des fuites de données |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.12 |
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
| 1.0 | [Date] | RSSI | Cadre de politique modulaire initial (14 documents) |

**Statut de mise en œuvre** :

- **Statut de déploiement** : [Totalement opérationnel / Déploiement partiel / Planifié]
- **Opérationnel depuis** : [Date de mise en service de l'infrastructure DLP]
- **Couverture actuelle** : [Pourcentage]% des canaux de sortie organisationnels protégés
- **Dernière évaluation** : [Date de la dernière évaluation IMP-A.8.12-3]
- **Prochaine évaluation** : [Date selon le calendrier de révision trimestriel]

*Note : Le statut de mise en œuvre est suivi dans les tableaux de bord récapitulatifs et rapporté à la Direction générale trimestriellement.*

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur des Systèmes d'Information (DSI)
- Conformité : Délégué à la Protection des Données (DPD) / Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.12.1-UG/TG (Évaluation de l'infrastructure DLP)
- ISMS-IMP-A.8.12.2-UG/TG (Évaluation de la classification des données)
- ISMS-IMP-A.8.12.3-UG/TG (Évaluation de la couverture des canaux)
- ISMS-IMP-A.8.12.4-UG/TG (Évaluation de la surveillance et de la réponse)
- ISO/IEC 27001:2022 Contrôle A.8.12

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de prévention des fuites de données (DLP) pour protéger les informations sensibles contre la divulgation, le transfert ou l'exfiltration non autorisés, conformément au Contrôle A.8.12 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les actifs informationnels classifiés comme Internes, Confidentiels ou Restreints ; tous les canaux de sortie des données (e-mail, web, postes de travail, réseau, cloud et mobile) ; l'ensemble du personnel organisationnel ; et toutes les technologies DLP quel que soit leur modèle de déploiement.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles DLP. Cette politique établit QUELLE protection contre les fuites de données est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.12 (variantes UG/TG). Les contrôles DLP traitent à la fois l'exfiltration malveillante (menaces internes, systèmes compromis) et la divulgation accidentelle (erreur utilisateur, mauvaise configuration).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse (surveillance des employés Art. 328b CO), le RGPD de l'UE (traitement licite Art. 5, sécurité Art. 32) et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.12 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.12 — Prévention des fuites de données**

> *Des mesures de prévention des fuites de données devraient être appliquées aux systèmes, réseaux et autres dispositifs traitant, stockant ou transmettant des informations sensibles.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les contrôles DLP empêchant l'exfiltration non autorisée des données dans l'ensemble de l'environnement de traitement de l'information de [Organisation].

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de contrôle DLP alignées sur la classification des données et l'appétit au risque organisationnel
- **Établit** le cadre de gouvernance pour la prise de décision et la responsabilisation en matière de DLP
- **Précise** les protections obligatoires pour les informations sensibles sur tous les canaux de sortie
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00
- **Identifie** les rôles et responsabilités organisationnels pour la mise en œuvre du DLP
- **Traite** les exigences légales de surveillance des employés (nLPD suisse Art. 328b CO, RGPD Art. 88)

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les détails de mise en œuvre techniques** (voir ISMS-IMP-A.8.12)
- **Définit pas les règles, patterns ou logiques de détection DLP spécifiques** (voir ISMS-IMP-A.8.12-2)
- **Sélectionne pas les technologies ou fournisseurs DLP** (sélection basée sur l'évaluation des risques)
- **Définit pas les procédures de réponse aux incidents** (voir ISMS-IMP-A.8.12-4)

---

# Exigences de prévention des fuites de données

## Classification des données et portée DLP

[Organisation] DOIT maintenir une classification des données à jour pour définir la portée de la protection DLP.

**Données nécessitant une protection DLP** (classification minimale : Interne) :

- Données à caractère personnel (DCP) soumises au RGPD/nLPD
- Données financières (données de cartes de paiement, informations bancaires, dossiers financiers)
- Propriété intellectuelle (code source, documents stratégiques, données R&D)
- Informations d'authentification (mots de passe, jetons, clés API, certificats privés)
- Informations contractuelles et tarifaires
- Données clients et partenaires
- Toute donnée classifiée Confidentielle ou Restreinte

## Protection des canaux de sortie

[Organisation] DOIT mettre en œuvre des contrôles DLP sur tous les canaux de sortie pertinents.

**E-mail** :

- Analyse automatisée des pièces jointes et du corps des messages pour détecter les données sensibles
- Application des politiques DLP sur les e-mails sortants
- Chiffrement obligatoire pour l'envoi de données Confidentielles/Restreintes hors de l'organisation
- Blocage ou mise en quarantaine des e-mails contenant des données Restreintes non chiffrées

**Web et applications cloud** :

- Inspection HTTPS (TLS inspection) des données quittant l'organisation via le web
- Blocage des téléchargements non autorisés de données sensibles vers des services cloud non approuvés
- Contrôle du partage de fichiers via les services de stockage cloud (shadow IT)
- Politique pour les services cloud approuvés vs. non approuvés

**Postes de travail (Endpoint DLP)** :

- Contrôle des périphériques amovibles (clés USB, disques externes) — politique de blocage ou de journalisation
- Contrôle des impressions de données sensibles (impression, PDF virtuel)
- Surveillance des opérations de copier-coller vers des applications non approuvées
- Contrôle des captures d'écran de données sensibles

**Réseau** :

- Inspection du trafic réseau sortant pour détecter les données sensibles
- Contrôle des protocoles de transfert de fichiers (FTP, SFTP non autorisé)
- Surveillance des transferts de données volumineuses anormaux

**Mobile** :

- Contrôles DLP appliqués via MDM pour les appareils d'entreprise
- Restriction du partage de données d'entreprise vers des applications personnelles (conteneurisation)
- Effacement à distance des données d'entreprise en cas de perte ou vol

## Actions DLP et flux de réponse

**Actions configurables selon la classification et le canal** :

| Action DLP | Description | Application typique |
|-----------|-------------|---------------------|
| **Surveiller** | Journaliser l'événement sans bloquer | Données Internes, détection initiale |
| **Alerter** | Notifier le SOC/RSSI et journaliser | Données Confidentielles, anomalies |
| **Bloquer et journaliser** | Empêcher la transmission et notifier | Données Restreintes, canaux non autorisés |
| **Chiffrer** | Forcer le chiffrement avant transmission | E-mail sortant avec données sensibles |
| **Mettre en quarantaine** | Retenir pour révision humaine | Données ambiguës, faux positifs potentiels |
| **Avertir l'utilisateur** | Afficher un avertissement et demander confirmation | Formation et sensibilisation en temps réel |

**Workflow de réponse aux incidents DLP** :

1. **Détection** : Le moteur DLP détecte une politique violée
2. **Action automatique** : Appliquer l'action configurée (bloquer, alerter, mettre en quarantaine)
3. **Notification** : Alerter le SOC et/ou le RSSI selon la gravité
4. **Triage** : Investiguer si l'incident est un vrai positif ou un faux positif
5. **Réponse** : Actions correctives si vrai positif (incident de sécurité, action disciplinaire)
6. **Documentation** : Journaliser l'incident et les actions prises
7. **Amélioration** : Affiner les règles DLP si faux positif

## Exigences légales pour la surveillance des employés

**Cadre juridique suisse** :

Conformément à l'Article 328b du Code des obligations suisse et à la nLPD :

- La surveillance des employés via DLP DOIT avoir un objectif légitime documenté
- Les employés DOIVENT être informés des mesures de surveillance DLP déployées (transparence)
- La surveillance DOIT être proportionnée à l'objectif de protection poursuivi
- Les données de surveillance NE DOIVENT PAS être utilisées à d'autres fins que la sécurité de l'information
- La conservation des journaux DLP DOIT respecter les durées de conservation légales
- Une consultation avec les représentants du personnel (si applicable) DOIT être réalisée avant déploiement

**Documentation requise** :

- Politique de surveillance des employés documentée et communiquée
- Notice de confidentialité informant les employés des traitements DLP
- Mesures techniques limitant l'accès aux données de surveillance au personnel autorisé
- Registre des activités de traitement (conformément à l'Art. 31 RGPD et à la nLPD) incluant les traitements DLP

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **RSSI** | Propriétaire de la politique ; supervision du programme DLP ; réponse aux incidents critiques |
| **DPD** | Conformité RGPD/nLPD pour la surveillance des employés ; validation de la proportionnalité |
| **Responsable juridique** | Conformité au droit du travail suisse ; révision des politiques de surveillance |
| **DSI / Opérations IT** | Mise en œuvre technique ; maintenance des systèmes DLP |
| **SOC** | Surveillance des alertes DLP ; triage et réponse aux incidents |
| **RH** | Communication aux employés ; gestion des incidents liés au personnel |
| **Responsables hiérarchiques** | Application des politiques DLP par leurs équipes |

---

# Gouvernance et conformité

## Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Couverture des canaux de sortie | ≥ 90 % | Trimestrielle |
| Taux de faux positifs DLP | < 5 % | Mensuelle |
| Délai de réponse aux incidents DLP critiques | < 1 heure | Continue |
| Incidents de fuites de données confirmés | 0 | Continue |
| Complétion de la formation DLP | ≥ 95 % | Annuelle |

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigences clés |
|----------------|----------------|
| **nLPD suisse + CO (Art. 328b)** | Surveillance proportionnée des employés, transparence, limitation de la finalité |
| **RGPD de l'UE** | Art. 5 — Traitement licite ; Art. 32 — Sécurité du traitement ; Art. 88 — Traitement dans le cadre des relations de travail |
| **ISO/IEC 27001:2022** | Contrôle A.8.12 |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Condition | Exigences |
|---------------|-----------|-----------|
| **PCI DSS v4.0.1** | Données de cartes de paiement | Contrôles anti-fuite pour les données de titulaires |
| **FINMA** | Institution financière suisse | Protection des données clients et des informations réglementées |
| **DORA** | Entité de services financiers UE | Contrôles de sécurité TIC incluant la prévention de l'exfiltration |

## Gestion des exceptions

Les exceptions aux exigences DLP DOIVENT être :

- Justifiées par un besoin métier documenté
- Évaluées pour le risque et assorties de contrôles compensatoires
- Approuvées par le RSSI (et DPD pour les exceptions impliquant des DCP)
- Limitées dans le temps (maximum 90 jours pour les exceptions de production)
- Documentées dans le registre des exceptions

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.12 v1.0)
- ✅ Signatures d'approbation du RSSI, DPD, Responsable juridique, Direction générale
- ✅ Classification des données et portée DLP définis
- ✅ Exigences de protection des canaux documentées
- ✅ Cadre légal pour la surveillance des employés documenté
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

- Rapports de couverture des canaux DLP
- Journaux d'incidents DLP avec statut (vrai/faux positif)
- Communication aux employés sur les mesures de surveillance
- Rapports de complétion de la formation DLP
- Tableaux de bord des métriques DLP (mensuels)

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

*Cette politique établit les exigences de prévention des fuites de données. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.12 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
