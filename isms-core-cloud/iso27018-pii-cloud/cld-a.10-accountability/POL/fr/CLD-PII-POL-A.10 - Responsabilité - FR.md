<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.10-FR:cloud:POL:a.10 -->
**CLD-PII-POL-A.10 — Responsabilité**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Responsabilité |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-PII-POL-A.10 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) / RSSI |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Cloud** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DPD / RSSI | Politique initiale pour la mise en œuvre d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors d'un changement réglementaire ou de modèle de service significatif)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : Délégué à la Protection des Données (DPD)
- Secondaire : RSSI / Responsable Sécurité Cloud
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.24-28 (Cycle de vie de la gestion des incidents — politique d'incident parente)
- ISMS-POL-A.5.34 (Protection des données et protection des DCP)
- ISMS-POL-A.5.33 (Protection des enregistrements)
- CLD-PII-POL-A.1 (Généralités)
- CLD-PII-POL-A.6 (Limitation de l'utilisation, de la conservation et de la divulgation)
- CLD-PII-POL-A.11 (Sécurité de l'information)
- ISO/IEC 27018:2025 Annex A, Section A.10 et Contrôles A.10.1–A.10.3
- ISO/IEC 27701:2025 Contrôles A.3.11–A.3.12 ; Clause 7.5 ; A.2.4.3
- RGPD Article 33 (72 heures) ; Article 34 ; Article 28(3)(f) ; Article 28(3)(g)
- LPD suisse Article 24 (notification au PFPDT)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en tant que sous-traitant de DCP en cloud public en matière de responsabilité — spécifiquement la notification des violations au responsable du traitement des DCP, la conservation des documents de sécurité administratifs, et les procédures de retour, transfert et élimination des DCP à la résiliation du contrat — conformément à ISO/IEC 27018:2025 Annex A, Section A.10 et Contrôles A.10.1, A.10.2 et A.10.3.

**Périmètre** : Tous les traitements de DCP effectués par [Organisation] pour le compte de responsables du traitement des DCP, y compris les obligations en fin de contrat.

**Justification des contrôles combinés** : A.10.1–A.10.3 établissent les trois piliers de la responsabilité du sous-traitant : (1) informer rapidement le responsable du traitement lorsque des problèmes surviennent (A.10.1), (2) conserver les preuves des engagements de sécurité aussi longtemps que nécessaire (A.10.2), et (3) veiller à ce que les DCP ne restent pas dans les systèmes de [Organisation] après qu'elles ne sont plus nécessaires (A.10.3).

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27018:2025

**Section A.10 — Responsabilité (principe)**

La Section A.10 établit le principe qu'un sous-traitant de DCP en cloud public doit maintenir sa responsabilité envers les responsables du traitement des DCP par une notification rapide des violations, la conservation de la documentation de conformité et le retour ou l'élimination sécurisée des DCP à la fin d'un engagement de service.

**Contrôle A.10.1 — Notification d'une violation de données impliquant des DCP**

Le Contrôle A.10.1 exige que le sous-traitant notifie le responsable du traitement des DCP de tout incident de sécurité DCP confirmé ou raisonnablement suspecté, sans retard injustifié et dans un délai permettant au responsable du traitement de respecter ses propres obligations réglementaires de notification.

**Contrôle A.10.2 — Période de conservation des politiques et directives de sécurité administratives**

Le Contrôle A.10.2 exige que le sous-traitant conserve les politiques de sécurité administratives et la documentation connexe pendant une période suffisante pour démontrer la conformité et soutenir les audits et investigations rétrospectifs.

**Contrôle A.10.3 — Retour, transfert et élimination des DCP**

Le Contrôle A.10.3 exige que le sous-traitant retourne ou élimine de manière sécurisée toutes les DCP à la résiliation du contrat, selon les instructions du responsable du traitement, et confirme la complétion par écrit.

## Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per PRIV-POL-00) :

- **RGPD UE** : Article 28(3)(f) (le sous-traitant assiste le responsable du traitement pour les notifications de violations et les obligations de sécurité) ; Article 33 (le responsable du traitement doit notifier l'autorité de contrôle dans les 72 heures — le sous-traitant doit notifier le responsable du traitement à temps) ; Article 34 ; Article 28(3)(g)
- **LPD suisse** : Article 24 (notification de violation au PFPDT — le plus rapidement possible) ; Article 9 (obligations de responsabilité du sous-traitant)
- **ISO/IEC 27018:2025** : Contrôles A.10.1, A.10.2, A.10.3

---

# Dispositions de la politique : Notification des violations (A.10.1)

## Obligation de notification

[Organisation] DOIT notifier le responsable du traitement des DCP concerné de tout incident de sécurité DCP confirmé ou raisonnablement suspecté **sans retard injustifié**, et en tout état de cause dans les **24 heures** suivant la détection. Un soupçon raisonnable surgit lorsque les preuves initiales indiquent un accès non autorisé à un système contenant des DCP, même si l'étendue complète de l'impact n'a pas encore été déterminée. Ce délai garantit que le responsable du traitement dispose de suffisamment de temps pour respecter sa propre obligation de notification à l'autorité de contrôle dans les 72 heures en vertu du RGPD.

## Contenu de la notification

Les notifications de violation aux responsables du traitement des DCP DOIVENT inclure les informations suivantes, dans la mesure disponible au moment de la notification :

| Élément | Description |
|---------|-------------|
| **Nature de la violation** | Type d'incident (accès non autorisé, divulgation accidentelle, rançongiciel, perte de données, etc.) |
| **Catégories de DCP** | Types de données à caractère personnel affectées (identité, contact, financières, santé, etc.) |
| **Nombre approximatif de personnes concernées** | Nombre estimé de personnes dont les DCP peuvent être affectées |
| **Conséquences probables** | Impact probable sur les personnes concernées |
| **Mesures prises** | Étapes de confinement et de remédiation mises en œuvre ou proposées |
| **Référence de l'incident** | Numéro de référence interne de l'incident de [Organisation] |
| **Point de contact** | DPD ou contact de sécurité pour les questions de suivi du responsable du traitement |

Lorsque les informations ne sont pas pleinement disponibles au moment de la notification initiale, [Organisation] DOIT fournir les informations au fur et à mesure qu'elles deviennent disponibles dans des mises à jour par phases, sans retard injustifié supplémentaire et en tout état de cause à des intervalles de 24 heures au maximum jusqu'à ce que l'incident soit entièrement caractérisé.

## Escalade et coordination

Le processus de réponse aux violations DCP de [Organisation] :

1. **Détection** — les Opérations de sécurité ou l'Ingénierie Cloud détectent un incident DCP potentiel
2. **Triage** (dans les 2 heures) — le RSSI détermine si les DCP sont impliquées ; active la réponse aux violations DCP si confirmée ou suspectée
3. **Notification initiale** (dans les 24 heures suivant la détection) — le DPD notifie le(s) responsable(s) du traitement des DCP affecté(s) avec les informations disponibles
4. **Investigation** — confinement parallèle et enquête forensique ; mises à jour par phases du responsable du traitement au fur et à mesure que les faits émergent
5. **Clôture** — analyse des causes profondes et remédiation confirmées ; rapport final d'incident fourni au responsable du traitement

---

# Dispositions de la politique : Conservation des documents (A.10.2)

## Calendrier de conservation

[Organisation] DOIT conserver la documentation administrative suivante pour les périodes minimales définies :

| Type de document | Conservation minimale |
|----------------|----------------------|
| Politiques de sécurité cloud CLD-PII-POL-A.X (toutes versions) | 5 ans à compter de la supersession de version |
| Accords et registres de sous-traitants ultérieurs | Durée de l'engagement + 5 ans |
| Enregistrements de traitement des DCP (registre des activités de traitement) | Durée du traitement + 5 ans |
| Enregistrements de notification des violations et rapports d'incidents | 5 ans à compter de la clôture de l'incident |
| Enregistrements de divulgation de DCP (registre CLD-PII-POL-A.6.2) | 5 ans à compter de la divulgation |
| Confirmations de retour/élimination des DCP (A.10.3) | 5 ans à compter de la complétion |
| Rapports d'évaluation de sécurité et d'audit | 5 ans |
| Accords de service avec les responsables du traitement | Durée de l'accord + 5 ans |

## Historique des versions

Tous les documents de politique CLD-PII-POL-A.X DOIVENT maintenir un historique des versions capturant la version du document, la date, l'auteur et le résumé des modifications. Les versions précédentes DOIVENT être conservées conformément au calendrier de conservation ci-dessus.

---

# Dispositions de la politique : Retour, transfert et élimination des DCP (A.10.3)

## Obligation en fin de contrat

À la résiliation ou l'expiration d'un accord de service cloud dans le cadre duquel [Organisation] traite des DCP, [Organisation] DOIT, selon les instructions du responsable du traitement des DCP :

**Option A — Retour** : Retourner toutes les DCP au responsable du traitement des DCP dans un format structuré et lisible par machine (JSON, CSV ou export standard de base de données tel que convenu), dans le délai spécifié dans l'accord de service ou, à défaut d'une telle spécification, dans les **30 jours calendaires** suivant la résiliation.

**Option B — Élimination** : Détruire de manière sécurisée toutes les DCP (y compris les entrepôts principaux, les sauvegardes, les copies répliquées et toute copie de sous-traitant ultérieur) en utilisant des méthodes empêchant la récupération, dans les **30 jours calendaires** suivant la résiliation. [Organisation] DOIT fournir au responsable du traitement des DCP un **certificat de destruction écrit** (voir la section Certificat de destruction ci-dessous) confirmant la complétion.

Lorsque le volume ou la complexité des DCP détenues rend la complétion dans les 30 jours calendaires impraticable, [Organisation] PEUT convenir d'un calendrier étendu avec le responsable du traitement des DCP **par écrit avant l'expiration de la période de 30 jours**. Toute extension convenue doit spécifier une date de complétion révisée et des confirmations de jalons intermédiaires.

## Copies de sauvegarde et répliquées

Lorsque des DCP existent dans des copies de sauvegarde ou répliquées au moment de la résiliation du contrat, [Organisation] DOIT :

- Inclure les copies de sauvegarde dans le processus de retour ou d'élimination dans la même fenêtre de 30 jours (ou période étendue convenue)
- Définir dans l'accord de service le délai maximum pour l'élimination des sauvegardes (tenant compte des cycles de rotation des sauvegardes)
- Confirmer par écrit lorsque l'élimination des sauvegardes est complète

## Élimination par les sous-traitants ultérieurs

Lorsque [Organisation] engage des sous-traitants ultérieurs qui détiennent des DCP, [Organisation] DOIT :

- Instruire les sous-traitants ultérieurs de retourner ou détruire les DCP dans la même fenêtre de 30 jours (ou période étendue convenue)
- Obtenir un certificat de destruction écrit de chaque sous-traitant ultérieur et le transmettre au responsable du traitement des DCP dans le cadre du propre enregistrement de confirmation de [Organisation]
- [Organisation] demeure responsable envers le responsable du traitement des DCP pour l'élimination par les sous-traitants ultérieurs — les certificats des sous-traitants ultérieurs sont des preuves étayantes, non une décharge de l'obligation de [Organisation]

## Certificat de destruction

Lorsque l'élimination des DCP est choisie (Option B), le certificat de destruction écrit fourni au responsable du traitement des DCP DOIT inclure au minimum :

| Champ | Description |
|-------|-------------|
| **Date de complétion** | Date à laquelle l'élimination a été complétée |
| **Périmètre** | Catégories de DCP détruites et volume approximatif (nombre d'enregistrements ou de personnes concernées) |
| **Systèmes couverts** | Entrepôts principaux, supports de sauvegarde, entrepôts de données répliqués et tout autre système confirmé comme purgé |
| **Méthode d'élimination** | Méthode technique utilisée (ex. effacement cryptographique, écrasement sécurisé selon la norme NIST SP 800-88, destruction physique) |
| **Confirmation du sous-traitant ultérieur** | Confirmation que les copies des sous-traitants ultérieurs ont également été détruites (avec les certificats des sous-traitants ultérieurs annexés ou référencés) |
| **Responsable certifiant** | Nom et rôle du responsable de [Organisation] certifiant la complétion |

## Enregistrement de confirmation

[Organisation] DOIT fournir au responsable du traitement des DCP une confirmation écrite du retour ou de l'élimination complétés, incluant :

- Date de livraison du retour ou de complétion de l'élimination
- Périmètre des DCP retournées ou éliminées (catégories, volume approximatif)
- Méthode d'élimination (lorsque l'élimination a été choisie)
- Confirmation que les DCP des sous-traitants ultérieurs ont également été retournées ou éliminées

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Délégué à la Protection des Données (DPD)** | Propriétaire du processus de notification des violations ; veille à ce que les notifications aux responsables du traitement soient émises dans les 24 heures ; gère le calendrier de conservation des documents ; supervise le processus de retour/élimination des DCP en fin de contrat |
| **RSSI / Responsable Sécurité Cloud** | Dirige la réponse technique aux violations (confinement, investigation) ; confirme le périmètre DCP des incidents ; met en œuvre l'élimination sécurisée pour les obligations en fin de contrat |
| **Responsable Juridique/Conformité** | Conseille sur les obligations de notification en vertu du RGPD et de la LPD ; examine les clauses de retour/élimination dans les accords de service ; maintient la conformité au calendrier de conservation |
| **Ingénierie Cloud** | Met en œuvre des mécanismes d'élimination sécurisée ; génère des exports de données pour les retours ; confirme la complétion de la purge des sauvegardes |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Enregistrements de notification des violations | Toutes les notifications envoyées aux responsables du traitement des DCP avec horodatages et contenu | 5 ans à compter de la clôture de l'incident |
| Rapports d'incidents | Rapports post-incident finaux pour tous les événements de sécurité DCP | 5 ans à compter de la clôture de l'incident |
| Archive des versions des documents | Toutes les versions précédentes des politiques CLD-PII-POL-A.X | 5 ans à compter de la supersession de version |
| Confirmations en fin de contrat | Confirmations écrites de retour ou d'élimination des DCP par contrat | 5 ans à compter de la complétion |
| Certificats de destruction | Certificats confirmant l'élimination sécurisée avec méthode et périmètre | 5 ans à compter de la complétion |
| Confirmations d'élimination des sauvegardes | Confirmation écrite que les copies de sauvegarde des DCP ont été purgées | 5 ans à compter de la complétion |

Les périodes de conservation de 5 ans reflètent le délai standard de prescription contractuelle applicable dans les juridictions de l'UE et suisses pour les litiges relatifs aux accords de sous-traitance, et soutiennent les exigences d'audit réglementaire rétrospectif.

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-PII-POL-A.10 doivent s'attendre à trouver :

- Une procédure de notification des violations documentée avec l'exigence de notification du responsable du traitement dans les 24 heures
- Des enregistrements de tous les incidents de sécurité DCP incluant les délais de notification — les notifications doivent précéder l'expiration du délai de 72 heures RGPD de tout responsable du traitement
- Un historique des versions pour tous les documents de politique CLD-PII-POL-A.X avec une conservation conforme au calendrier
- Des confirmations de retour ou d'élimination en fin de contrat et des certificats de destruction pour tous les accords résiliés au cours de la période d'audit

---

<!-- QA_VERIFIED: 2026-04-04 -->
