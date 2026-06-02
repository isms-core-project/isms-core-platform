<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.11-FR:cloud:POL:a.11 -->
**CLD-PII-POL-A.11 — Sécurité de l'information**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Sécurité de l'information |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-PII-POL-A.11 |
| **Auteur du document** | RSSI / Responsable Sécurité Cloud |
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
| 1.0 | [Date] | RSSI / Responsable Sécurité Cloud | Politique initiale pour l'implémentation d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors de changements significatifs d'infrastructure, de technologie ou de réglementation)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : RSSI / Responsable Sécurité Cloud
- Secondaire : Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection de la vie privée et des DCP)
- ISMS-POL-A.5.15-16-18 (Gestion des identités et des accès)
- ISMS-POL-A.5.19-23 (Relations avec les fournisseurs et les tiers)
- ISMS-POL-A.8.10 (Suppression des informations)
- ISMS-POL-A.8.24 (Utilisation de la cryptographie)
- CLD-PII-POL-A.1 (Généralités)
- CLD-PII-POL-A.5 (Minimisation des données — effacement des fichiers temporaires)
- CLD-PII-POL-A.8 (Ouverture, transparence — divulgation des sous-traitants ultérieurs)
- CLD-PII-POL-A.10 (Responsabilité — notification des violations)
- ISO/IEC 27018:2025 Annexe A, Section A.11 et Contrôles A.11.1–A.11.13
- ISO/IEC 27701:2025 Annexe A.3 (Contrôles de sécurité de l'information — A.3.3 à A.3.31, applicables aux responsables et sous-traitants du traitement, mis en œuvre par cette politique)
- ISO/IEC 27002:2022 Contrôles 6.2 (conditions générales), 8.11 (masquage des données), 8.12 (prévention des fuites de données), 8.24 (cryptographie)
- RGPD Article 28(3)(c) (le sous-traitant met en œuvre les mesures techniques et organisationnelles appropriées conformément à l'Article 32) ; Article 32 (sécurité du traitement)
- LPD suisse Article 9 (conditions d'engagement du sous-traitant et obligations de sécurité des données associées)

---

## Résumé exécutif

Cette politique établit les exigences de sécurité de l'information de [Organisation] pour la protection des DCP dans les environnements cloud publics — la section la plus complète du jeu de contrôles de l'Annexe A d'ISO/IEC 27018:2025, couvrant 13 contrôles en matière de confidentialité, de sécurité des supports physiques, de gestion des accès, de chiffrement, de journalisation des audits, de gestion des sous-traitants ultérieurs et de rémanence des données.

**Périmètre** : Tous les systèmes, personnels, processus et sous-traitants ultérieurs impliqués dans le traitement des DCP pour le compte des responsables du traitement des DCP dans les services cloud publics de [Organisation].

**Couverture des contrôles** : Cette politique couvre les contrôles A.11.1 à A.11.13 d'ISO/IEC 27018:2025.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27018:2025

**A.11.1 — Accords de confidentialité ou de non-divulgation** : Le personnel ayant accès aux DCP est lié par des obligations NDA documentées survivant à la résiliation.

**A.11.2 — Restriction de la création de documents papier** : Impression des DCP limitée à des finalités légitimes documentées ; DCP imprimées gérées de manière sécurisée.

**A.11.3 — Contrôle et journalisation de la restauration des données** : La restauration des DCP à partir des sauvegardes est une opération contrôlée et journalisée ; journaux protégés et examinés.

**A.11.4 — Protection des données sur les supports de stockage quittant les locaux** : Supports physiques contenant des DCP chiffrés ou détruits avant de quitter l'environnement contrôlé.

**A.11.5 — Utilisation de supports de stockage portables non chiffrés** : Appareils portables non chiffrés interdits pour les DCP ; perte/vol traité comme incident DCP.

**A.11.6 — Chiffrement des DCP transmises sur les réseaux de transmission de données publics** : DCP en transit chiffrées avec TLS 1.2 minimum, 1.3 préféré ; HTTPS appliqué.

**A.11.7 — Élimination sécurisée des documents papier** : Documents papier contenant des DCP éliminés par déchiquetage croisé ou équivalent ; élimination documentée.

**A.11.8 — Utilisation unique d'identifiants d'utilisateur** : Chaque personne ayant accès aux DCP se voit attribuer un identifiant unique ; pas de comptes partagés.

**A.11.9 — Gestion des identifiants d'utilisateur** : Cycle de vie des identifiants d'utilisateur géré ; désactivés promptement lors de la résiliation ou du changement de rôle ; comptes inactifs examinés.

**A.11.10 — Registres des utilisateurs autorisés** : Registres à jour de tous les utilisateurs autorisés des systèmes DCP ; examinés au moins trimestriellement ; disponibles pour le responsable du traitement.

**A.11.11 — Mesures contractuelles** : Les accords entre sous-traitant et responsable du traitement couvrent le périmètre, la sécurité, la notification des violations, l'assistance aux droits, l'audit, l'approbation des sous-traitants ultérieurs, le retour/la suppression, la juridiction.

**A.11.12 — Traitement des DCP sous-traité** : Les sous-traitants ultérieurs liés par des obligations équivalentes via des contrats contraignants ; audités périodiquement ; le sous-traitant reste responsable.

**A.11.13 — Accès aux données sur l'espace de stockage de données précédemment utilisé** : Stockage réalloué à un nouveau client effacé de manière cryptographique ; procédures de mise hors service documentées et testées.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 28(3)(c) (le sous-traitant met en œuvre les mesures techniques et organisationnelles appropriées conformément à l'Article 32) ; Article 32 (sécurité du traitement — pseudonymisation, chiffrement, résilience, restauration, tests)
- **LPD suisse** : Article 9 (conditions d'engagement du sous-traitant et obligations de sécurité des données associées)
- **ISO/IEC 27018:2025** : Contrôles A.11.1–A.11.13

---

# Énoncés de politique : Obligations de confidentialité (A.11.1)

Tous les employés et contractants de [Organisation] ayant accès aux systèmes contenant des DCP DOIVENT être liés par des obligations de confidentialité et de non-divulgation écrites. Les NDA DOIVENT explicitement :

- Interdire l'utilisation secondaire, la conservation personnelle ou la divulgation non autorisée des DCP
- Survivre à la résiliation de l'emploi ou de l'engagement
- Être signés avant l'accès à tout système DCP

Les NDA sont gérés conformément à ISMS-POL-A.6.3 (Accords de confidentialité). La couverture NDA DOIT être vérifiée lors des processus d'intégration et de départ.

---

# Énoncés de politique : Restriction des documents papier (A.11.2)

La création de documents papier (imprimés) contenant des DCP est **restreinte**. L'impression de DCP nécessite :

- Une justification commerciale documentée (ex. exigence réglementaire, piste d'audit sur papier)
- Une autorisation du responsable d'équipe concerné et une notation DPD pour les impressions en grand volume
- La collecte immédiate depuis l'imprimante ; les DCP imprimées ne doivent pas être laissées sans surveillance dans des zones partagées

Les DCP imprimées DOIVENT être gérées selon les procédures de bureau propre et éliminées conformément au §11.7 (élimination sécurisée des documents papier). Dans la mesure du possible techniquement, des logiciels de gestion d'impression ou des contrôles DLP DOIVENT être configurés pour signaler ou restreindre les tâches d'impression contenant des DCP ; lorsque l'application technique n'est pas mise en œuvre, le recours aux contrôles procéduraux DOIT être documenté par le RSSI avec une surveillance compensatoire identifiée.

---

# Énoncés de politique : Contrôle et journalisation de la restauration des données (A.11.3)

La restauration de DCP à partir de sauvegardes ou d'archives est une **opération contrôlée** nécessitant :

- Une autorisation de restauration documentée du responsable d'équipe ou du commandant d'incident
- La journalisation de : l'identité de l'opérateur, l'horodatage, la source de sauvegarde, la portée des données restaurées et la référence d'autorisation
- Les journaux de restauration protégés contre la falsification (écriture unique ou signature cryptographique)
- L'examen trimestriel des journaux de restauration par le RSSI

Des alertes automatisées DOIVENT être configurées pour notifier le RSSI en temps réel des événements de restauration, permettant la détection des restaurations hors schéma sans attendre l'examen trimestriel des journaux. Les tentatives de restauration non planifiées ou non autorisées DOIVENT être traitées comme des événements de sécurité et faire l'objet d'une enquête conformément à ISMS-POL-A.5.24-28.

---

# Énoncés de politique : Supports de stockage quittant les locaux (A.11.4)

Les supports de stockage physiques (disques, bandes, supports amovibles) contenant des DCP qui quittent les installations cloud de [Organisation] DOIVENT être :

- **Chiffrés** à l'aide d'un chiffrement intégral du disque ou de volume approuvé avec gestion des clés conformément à ISMS-POL-A.8.24, ou
- **Physiquement détruits** selon une norme empêchant la récupération des données (ex. destruction conforme à NIST SP 800-88) avant de quitter les locaux

Les mouvements de supports DOIVENT être :
- Autorisés par le RSSI ou le Responsable Sécurité Cloud
- Enregistrés dans un registre des mouvements de supports avec documentation de la chaîne de custody
- Suivis jusqu'à la destination finale (installation de retour ou de destruction)

---

# Énoncés de politique : Appareils de stockage portables non chiffrés (A.11.5)

L'utilisation de supports et appareils de stockage portables non chiffrés pour le stockage ou le transfert de DCP est **interdite**. Cette interdiction couvre les clés USB, les disques durs externes, les ordinateurs portables, les tablettes et les téléphones mobiles.

Lorsque des appareils portables sont autorisés pour les DCP :
- Le chiffrement intégral du disque répondant aux normes approuvées (AES-256 minimum) est **obligatoire**
- L'état de chiffrement de l'appareil DOIT être vérifié par l'IT avant que l'accès aux DCP soit autorisé
- La capacité d'effacement à distance DOIT être activée pour les appareils mobiles

**La perte ou le vol** de tout appareil portable susceptible de contenir des DCP DOIT être signalé immédiatement au RSSI et au DPD et traité comme un incident de sécurité DCP conformément à CLD-PII-POL-A.10.1 et ISMS-POL-A.5.24-28.

---

# Énoncés de politique : Chiffrement des DCP en transit (A.11.6)

Les DCP transmises sur les réseaux publics DOIVENT être chiffrées. Exigences :

- **TLS 1.3 requis** pour toutes les nouvelles implémentations ; **TLS 1.2 autorisé uniquement pour les intégrations existantes** où TLS 1.3 n'est pas encore techniquement faisable, sous réserve d'un plan de remédiation documenté et d'une approbation du RSSI
- **HTTPS appliqué** sur toutes les interfaces web et les points de terminaison API gérant des DCP ; redirection HTTP vers HTTPS obligatoire
- Les certificats TLS DOIVENT être émis par des autorités de certification de confiance et renouvelés avant expiration (renouvellement automatique préféré)
- La **transmission non chiffrée** (HTTP simple, FTP, SMTP sans STARTTLS) de DCP est interdite

Les configurations de suite de chiffrement DOIVENT être examinées annuellement par rapport aux meilleures pratiques actuelles (ex. BSI TR-02102, NIST SP 800-52). Les chiffrements faibles (RC4, DES, 3DES, SSL 3.0, TLS 1.0, TLS 1.1) DOIVENT être désactivés.

---

# Énoncés de politique : Élimination sécurisée des documents papier (A.11.7)

Les documents papier contenant des DCP DOIVENT être éliminés de manière sécurisée :

- **Élimination individuelle** : Déchiquetage croisé au niveau DIN 66399 P-5 (taille de particule max 30 mm²) pour les documents contenant des DCP ou des catégories spéciales ; P-4 est acceptable pour les documents internes généraux ne contenant pas de DCP
- **Élimination en volume** : Services de destruction certifiés avec certificat de destruction fourni au demandeur
- **Bacs d'élimination** : Bacs verrouillés et à accès contrôlé pour les DCP dans tous les espaces de travail contenant des DCP

L'élimination DOIT être documentée. Les certificats de destruction DOIVENT être conservés pendant 3 ans.

---

# Énoncés de politique : Identifiants d'utilisateur uniques (A.11.8)

Chaque personne ayant accès aux systèmes DCP DOIT se voir attribuer un **identifiant d'utilisateur unique**. Les comptes partagés, génériques ou basés sur des rôles NE DOIVENT PAS être utilisés pour accéder aux systèmes où des DCP sont traités ou stockés.

Les identifiants uniques garantissent que toutes les actions sur les DCP peuvent être attribuées à un individu spécifique à des fins d'audit et de responsabilité. Les exceptions (ex. comptes de service) nécessitent l'approbation du RSSI et des contrôles compensatoires renforcés (gestion des accès privilégiés, enregistrement des sessions).

---

# Énoncés de politique : Gestion des identifiants d'utilisateur (A.11.9)

Les identifiants d'utilisateur pour les systèmes DCP DOIVENT être gérés à travers un cycle de vie documenté :

| Phase du cycle de vie | Exigence |
|-----------------|-------------|
| **Provisionnement** | Nécessite une autorisation documentée du responsable de l'utilisateur et du propriétaire du système |
| **Examen des accès** | Tous les comptes des systèmes DCP examinés au moins trimestriellement |
| **Changement de rôle** | Accès mis à jour dans un délai d'1 jour ouvrable après confirmation du changement de rôle |
| **Résiliation** | Compte désactivé dans les 4 heures suivant le départ confirmé par les RH |
| **Comptes inactifs** | Comptes inactifs depuis 30 jours sur les systèmes DCP critiques (45 jours sur les systèmes DCP moins sensibles) examinés ; suspendus en attente d'examen ; supprimés en l'absence de justification commerciale |

La gestion du cycle de vie des identifiants d'utilisateur s'intègre à ISMS-POL-A.5.15-16-18 (IAM).

---

# Énoncés de politique : Registres des utilisateurs autorisés (A.11.10)

[Organisation] DOIT maintenir un **Registre des utilisateurs autorisés** pour chaque système DCP, enregistrant :

- L'identité et le rôle de chaque individu
- La portée de l'accès accordé (lecture, écriture, admin)
- La date d'autorisation et le responsable autorisant
- La date du dernier examen

Le Registre des utilisateurs autorisés DOIT être :
- Examiné et certifié par les propriétaires de systèmes au moins **trimestriellement**
- Mis à la disposition de tout responsable du traitement des DCP sur demande — [Organisation] DOIT fournir à chaque responsable du traitement un **extrait limité** montrant uniquement le personnel ayant accès aux données DCP de ce responsable du traitement, et non l'intégralité du registre sur tous les clients
- Mis à jour dans un délai d'1 jour ouvrable après tout changement d'accès

---

# Énoncés de politique : Mesures contractuelles (A.11.11)

Les accords de service entre [Organisation] et les responsables du traitement des DCP DOIVENT inclure des dispositions couvrant :

- La portée et la finalité documentée du traitement des DCP
- Les obligations de sécurité alignées sur l'Article 32 du RGPD et cette politique
- Les exigences de notification des violations (notification du responsable du traitement dans les 24 heures per CLD-PII-POL-A.10.1)
- Les obligations d'assistance aux droits des personnes concernées (per CLD-PII-POL-A.2.1 et CLD-PII-POL-A.9)
- Les droits d'audit : le responsable du traitement (ou son auditeur désigné) peut auditer la conformité de [Organisation], exercisable avec un préavis d'au moins 30 jours, pas plus d'une fois par année civile sauf incident de sécurité confirmé justifiant un audit supplémentaire, et aux frais du responsable du traitement sauf si une non-conformité est démontrée
- Les exigences d'approbation des sous-traitants ultérieurs (per CLD-PII-POL-A.8.1)
- Le retour ou la suppression des DCP à la résiliation (per CLD-PII-POL-A.10.3)
- La loi applicable et la juridiction

Les conditions contractuelles DOIVENT être examinées lorsque les exigences réglementaires changent de manière significative. Le Responsable Juridique/Conformité maintient le modèle standard d'accord de traitement.

---

# Énoncés de politique : Traitement des DCP sous-traité (A.11.12)

[Organisation] DOIT imposer à tous les sous-traitants ultérieurs, via des contrats contraignants, des **obligations équivalentes** à celles de cette politique et de l'intégralité de la suite CLD-PII-POL-A.X. Les contrats de sous-traitants ultérieurs DOIVENT :

- Refléter les obligations de protection des données de l'accord responsable du traitement-sous-traitant
- Exiger le consentement préalable écrit de [Organisation] (et par extension, du responsable du traitement des DCP) avant tout sous-traitement ultérieur
- Inclure des droits d'audit pour [Organisation] sur la conformité du sous-traitant ultérieur
- Exiger la notification des violations à [Organisation] dans les 12 heures suivant la détection (permettant à [Organisation] d'honorer son obligation de notification au responsable du traitement dans les 24 heures per CLD-PII-POL-A.10.1) — cette exigence de 12 heures est une **clause obligatoire** dans tous les accords de sous-traitants ultérieurs ; le Responsable Juridique/Conformité maintient le modèle standard d'accord de sous-traitants ultérieurs
- Exiger le retour ou la suppression des DCP à la résiliation de l'engagement du sous-traitant ultérieur

[Organisation] DOIT auditer les sous-traitants ultérieurs au moins annuellement (via questionnaire, examen de documents ou audit sur site) et reste **entièrement responsable** envers les responsables du traitement des DCP des manquements de conformité des sous-traitants ultérieurs. Les résultats des audits des sous-traitants ultérieurs DOIVENT être documentés et disponibles pour les responsables du traitement sur demande.

---

# Énoncés de politique : Espace de stockage de données précédemment utilisé (A.11.13)

[Organisation] DOIT s'assurer que les DCP ne peuvent pas être accédées depuis un stockage précédemment alloué à un autre client (**prévention de la rémanence des données**).

Avant qu'un stockage soit réalloué à une nouvelle charge de travail client :
- Toutes les données précédentes DOIVENT être **effacées de manière cryptographique** (suppression des clés de chiffrement pour les volumes chiffrés — la méthode principale pour le stockage cloud) ou écrasées selon une norme empêchant la récupération
- L'effacement DOIT être documenté et le relevé de mise hors service conservé

Les procédures de mise hors service DOIVENT :
- Couvrir tous les types de stockage : stockage en blocs (EBS, volumes), stockage d'objets (contenu des buckets), stockage d'instance éphémère et stockage de bases de données
- Être testées au moins **annuellement** en échantillonnant aléatoirement des stockages réalloués et en confirmant l'absence de données résiduelles
- S'appliquer également à la mise hors service physique des supports de stockage (voir A.11.4)

Ce contrôle est le fondement de l'isolation des DCP multi-locataires. Tout manquement DOIT être traité comme un incident de sécurité DCP potentiel.

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI / Responsable Sécurité Cloud** | Est propriétaire de cette politique ; garantit que les 13 contrôles sont mis en œuvre et maintenus ; effectue l'examen annuel de la sécurité ; gère le programme de mouvements de supports et d'audit des sous-traitants ultérieurs |
| **Délégué à la Protection des Données (DPD)** | Examine la politique annuellement pour l'alignement réglementaire ; conseille sur les conditions contractuelles (A.11.11) ; supervise les évaluations d'adéquation des sous-traitants ultérieurs |
| **Cloud Engineering** | Met en œuvre les contrôles techniques (chiffrement, configuration TLS, effacement, journalisation) ; teste les procédures de mise hors service |
| **IT / Gestion des identités** | Gère le cycle de vie des identifiants d'utilisateur per A.11.8–A.11.10 ; maintient le Registre des utilisateurs autorisés ; applique les politiques d'accès |
| **Responsable Juridique/Conformité** | Maintient le modèle standard d'accord de traitement ; examine les accords de sous-traitants ultérieurs ; conseille sur les clauses de juridiction et de droits d'audit |
| **Ressources Humaines** | Déclenche la désactivation des comptes d'utilisateur lors du départ ; gère le processus de signature des NDA lors de l'intégration |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Enregistrements NDA | NDA signés pour tout le personnel ayant accès aux DCP | Durée de l'engagement + 5 ans |
| Journaux d'autorisation d'impression | Enregistrements des opérations d'impression DCP autorisées | 3 ans |
| Journaux de restauration des sauvegardes | Événements de restauration journalisés avec enregistrements d'autorisation | 3 ans |
| Registre des mouvements de supports | Journal de mouvements des supports physiques avec chaîne de custody | 3 ans |
| Enregistrements de configuration TLS / Chiffrement | Documentation actuelle de la suite de chiffrement et de la configuration TLS | Actuel + versions précédentes 5 ans |
| Certificats de destruction | Certificats d'élimination de documents papier et de supports | 3 ans |
| Registre des utilisateurs autorisés | Enregistrements d'accès certifiés trimestriellement par système DCP | 5 ans |
| Enregistrements d'audit des sous-traitants ultérieurs | Résultats d'audit annuels pour chaque sous-traitant ultérieur | 5 ans |
| Enregistrements de mise hors service du stockage | Enregistrements d'effacement cryptographique par événement de mise hors service du stockage | 3 ans |
| Résultats des tests de mise hors service | Résultats des tests annuels confirmant l'absence de données résiduelles dans le stockage réalloué | 3 ans |

---

# Considérations d'audit

Les auditeurs vérifiant la conformité avec CLD-PII-POL-A.11 devraient s'attendre à trouver :

- Une couverture NDA pour tout le personnel ayant accès aux DCP — sans exception
- TLS 1.2+ appliqué sur toutes les interfaces réseau gérant des DCP ; TLS 1.0/1.1 désactivé
- Des certifications trimestrielles du Registre des utilisateurs autorisés avec suppression rapide des partants et des personnes changeant de rôle
- Des rapports d'audit des sous-traitants ultérieurs pour la période d'audit confirmant l'application d'obligations équivalentes
- Des résultats de tests de mise hors service du stockage confirmant l'absence de rémanence de données entre locataires
- Des journaux de restauration des sauvegardes avec enregistrements d'autorisation pour tous les événements de restauration

---

<!-- QA_VERIFIED: 2026-04-04 -->
