<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.2-3-5-FR:framework:POL:a.8.2-3-5 -->
**ISMS-POL-A.8.2-3-5 – Authentification et accès privilégié**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique d'authentification et de sécurité des accès privilégiés |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.2-3-5 |
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
- Opérations de sécurité : Responsable des opérations de sécurité
- Opérations IT : Responsable des opérations IT
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.15-16-18 (Fondation IAM)
- ISMS-IMP-A.8.2-3-5.S1-UG/TG (Inventaire de l'authentification)
- ISMS-IMP-A.8.2-3-5.S2-UG/TG (Couverture AMF)
- ISMS-IMP-A.8.2-3-5.S3-UG/TG (Comptes privilégiés)
- ISMS-IMP-A.8.2-3-5.S4-UG/TG (Surveillance des accès privilégiés)
- ISMS-IMP-A.8.2-3-5.S5-UG/TG (Restrictions d'accès)
- ISO/IEC 27001:2022 Contrôles A.8.2, A.8.3, A.8.5

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de sécurité de l'authentification, de gestion des accès privilégiés et d'application technique des contrôles d'accès, conformément à la norme ISO/IEC 27001:2022.

**Contrôles traités** :

- **A.8.5 — Authentification sécurisée** : Mécanismes d'authentification fondés sur les restrictions d'accès
- **A.8.2 — Droits d'accès privilégiés** : Restriction et gestion des accès privilégiés
- **A.8.3 — Restriction d'accès à l'information** : Application technique des contrôles d'accès

**Périmètre** : Tous les mécanismes d'authentification, les comptes privilégiés et les contrôles d'accès techniques sur l'ensemble des systèmes, plateformes et environnements détenus ou exploités par [Organisation].

**Objet** : Définir QUELS contrôles d'authentification et d'accès sont requis et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées dans ISMS-IMP-A.8.2-3-5.

**Justification du contrôle empilé** : Ces contrôles forment des couches indissociables du dispositif de sécurité de l'authentification et des accès. Une mise en œuvre séparée créerait des lacunes entre l'authentification, la gestion des privilèges et l'application des accès.

**Alignement réglementaire** : Conformément à ISMS-POL-00 :

- **Obligatoire** : nLPD suisse (Art. 8), RGPD de l'UE (Art. 32), ISO 27001:2022
- **Conditionnel** : FINMA, DORA, NIS2 (Art. 21(2)(e) — obligation d'AMF), PCI DSS v4.0.1

---

# Alignement sur les contrôles et périmètre

## Exigences des contrôles ISO/IEC 27001:2022

**Contrôle A.8.5 — Authentification sécurisée** :
> *Des technologies et procédures d'authentification sécurisées doivent être mises en œuvre selon les restrictions d'accès à l'information et la politique thématique sur le contrôle d'accès.*

**Contrôle A.8.2 — Droits d'accès privilégiés** :
> *L'attribution et l'utilisation des droits d'accès privilégiés doivent être restreintes et gérées.*

**Contrôle A.8.3 — Restriction d'accès à l'information** :
> *L'accès à l'information et aux autres actifs associés doit être restreint conformément à la politique thématique établie sur le contrôle d'accès.*

## Définition du périmètre

**Dans le périmètre** :

- Toute authentification utilisateur (mots de passe, AMF, SSO, certificats, biométrie)
- Tous les comptes privilégiés (administrateur, root, comptes de service, brise-glace)
- Tous les contrôles d'accès techniques (OS, base de données, application, API, cloud, réseau)
- Tous les modèles de déploiement (sur site, cloud, hybride, SaaS)
- Tous les types d'utilisateurs (employés, contractants, fournisseurs, clients le cas échéant)

**Hors périmètre** :

- Contrôles d'accès physique (traités dans A.7.x — Sécurité physique)
- Détails de la segmentation réseau (traités dans A.8.20-22 — Sécurité des réseaux)
- Gestion des clés cryptographiques (traitée dans A.8.24 — Cryptographie)

## Indépendance dans la Déclaration d'applicabilité

Chaque contrôle conserve une applicabilité indépendante :

- A.8.5 peut être applicable sans A.8.2 (authentification des utilisateurs standard uniquement)
- A.8.2 nécessite A.8.5 (les accès privilégiés nécessitent une authentification)
- A.8.3 nécessite A.8.5 et A.8.2 (l'application nécessite la définition de l'authentification et des privilèges)

---

# Exigences d'authentification (Contrôle A.8.5)

## Normes des mécanismes d'authentification

[Organisation] DOIT mettre en œuvre des mécanismes d'authentification appropriés à la sensibilité des informations et des systèmes auxquels l'accès est demandé.

**Exigences minimales d'authentification** :

| Classification du système | Exigence minimale | Exigence AMF |
|--------------------------|-------------------|--------------|
| **Critique/Haut risque** | AMF obligatoire | Jeton matériel ou application d'authentification |
| **Métier standard** | Mot de passe + AMF recommandée | Application d'authentification acceptable |
| **Faible risque/Public** | Mot de passe acceptable | Optionnel |
| **Accès privilégié** | AMF obligatoire | Jeton matériel de préférence (FIDO2) |
| **Accès distant** | AMF obligatoire | Requise pour toutes les connexions distantes |

**Exigences relatives aux mots de passe** (conformément à NIST SP 800-63B) :

- Longueur minimale : 12 caractères (14 pour les comptes privilégiés)
- Complexité : mélange de types de caractères OU phrase de passe de 16+ caractères
- Pas d'expiration du mot de passe sauf en cas de compromission suspectée ou avérée
- Détection des violations : mots de passe vérifiés par rapport aux bases de données de violations connues (par ex. API Have I Been Pwned) ; les mots de passe compromis nécessitent une réinitialisation immédiate
- Historique des mots de passe : minimum 24 mots de passe antérieurs

**Vérification** : Application de la politique de mots de passe validée par des exports de configuration du fournisseur d'identité ; alertes de détection des violations révisées hebdomadairement.

## Authentification multifacteur (AMF)

**L'AMF DOIT être obligatoire pour** :

- Tous les accès privilégiés (administrateurs Niveaux 0, 1 et 2)
- Tous les accès distants (VPN, bureau à distance, console cloud)
- Tous les accès aux données sensibles (données personnelles, financières, propriété intellectuelle)
- Toutes les applications exposées à l'externe avec authentification
- Toutes les consoles d'administration de plateformes cloud

**Méthodes AMF acceptables** (par ordre de préférence, avec niveau de résistance à l'hameçonnage) :

| Méthode | Résistance à l'hameçonnage | Cas d'utilisation |
|---------|---------------------------|-------------------|
| Clés de sécurité matérielles (FIDO2/WebAuthn) | Élevée (résistante à l'hameçonnage) | Requise pour le Niveau 0, recommandée pour tous les accès privilégiés |
| Applications d'authentification (TOTP) | Moyenne | Acceptable pour les Niveaux 1/2 et utilisateurs standard |
| Notifications push (avec correspondance de numéro) | Moyenne | Acceptable avec correspondance de numéro activée |
| Code à usage unique par SMS/voix | Faible | Uniquement si d'autres méthodes ne sont pas faisables (systèmes hérités) |

**Cibles de couverture AMF** :

- Utilisateurs privilégiés : 100 % d'enrôlement AMF
- Tous les utilisateurs : ≥ 95 % d'enrôlement dans les 12 mois suivant l'adoption de la politique
- Accès distant : 100 % d'application de l'AMF

**Évaluation de la référence** : Avant l'application des cibles, [Organisation] DOIT établir la couverture AMF actuelle via les rapports d'enrôlement du fournisseur d'identité. Si la référence est < 80 %, un plan de comblement des lacunes est requis.

**Feuille de route de déploiement** : Si la couverture AMF actuelle est inférieure à la cible, des jalons de déploiement DOIVENT être documentés (par ex. 80 % au mois 3, 90 % au mois 6, 95 % au mois 12). Progression suivie trimestriellement.

**Vérification** : Statut d'enrôlement AMF vérifié via les exports du tableau de bord du fournisseur d'identité (Microsoft Entra ID, Okta ou équivalent) ; rapports hebdomadaires pour les utilisateurs privilégiés, mensuels pour tous les utilisateurs.

## Authentification unique (SSO)

[Organisation] DOIT mettre en œuvre un SSO centralisé avec une cible de ≥ 90 % d'intégration des applications SaaS :

- Nouvelles applications SaaS : intégration SSO requise avant approbation des achats
- Applications existantes : intégration SSO priorisée selon le risque et le volume d'utilisateurs
- Réduit la fatigue des mots de passe et améliore la posture de sécurité
- Permet la révocation centralisée des accès à la résiliation

**Exceptions** : Les applications sans capacité SSO nécessitent une exception documentée avec des contrôles compensatoires (par ex. AMF individuelle, surveillance renforcée).

**Vérification** : Inventaire des applications SSO maintenu dans le Classeur 1 ; pourcentage d'intégration suivi trimestriellement.

## Journalisation de l'authentification

Tous les événements d'authentification DOIVENT être journalisés :

- Tentatives d'authentification réussies et échouées
- Enrôlement AMF et changements de méthode
- Changements et réinitialisations de mots de passe
- Verrouillages et déverrouillages de comptes
- Création et fin de sessions

**Vérification** : Journaux d'authentification révisés via intégration SIEM ; anomalies investiguées dans les 24 heures.

---

# Exigences d'accès privilégié (Contrôle A.8.2)

## Principes de l'accès privilégié

[Organisation] DOIT restreindre l'accès privilégié selon les principes suivants :

- **Moindre privilège** : accès minimum requis pour exercer les fonctions du poste
- **Besoin d'en savoir** : accès uniquement aux informations nécessaires aux tâches spécifiques
- **Séparation des fonctions** : fonctions critiques réparties entre plusieurs personnes
- **Accès limité dans le temps** : provisionnement en juste-à-temps (JIT) autant que possible

## Classification des comptes privilégiés

**Modèle de niveaux d'administration** — [Organisation] DOIT mettre en œuvre une administration par niveaux :

| Niveau | Périmètre | Exemples | Exigences |
|--------|-----------|----------|-----------|
| **Niveau 0** | Domaine/Entreprise | Administrateurs de domaine, Administrateur global Azure, PKI, SIEM | AMF matérielle, PAW requis, enregistrement de session obligatoire |
| **Niveau 1** | Serveur/Application | Administrateurs serveur, DBA, administrateurs d'abonnement cloud | AMF requise, poste d'administration dédié recommandé |
| **Niveau 2** | Poste de travail/Terminal | Support desktop, service desk avec admin local | AMF requise, poste de travail standard acceptable |

**Exigences d'isolation des niveaux** :

- Les comptes de Niveau 0 NE DOIVENT JAMAIS s'authentifier sur les systèmes de Niveau 1 ou 2
- Les comptes de Niveau 1 NE DOIVENT JAMAIS s'authentifier sur les systèmes de Niveau 2
- Des identifiants distincts requis par niveau (par ex. jean.dupont.n0, jean.dupont.n1)

**Application de l'isolation des niveaux** :

- Contrôles techniques : politiques d'accès conditionnel, restrictions GPO ou règles de pare-feu empêchant l'authentification inter-niveaux
- Surveillance : alertes SIEM configurées pour les tentatives de violation de niveau
- Déploiement des PAW : postes de travail à accès privilégié (PAW) de Niveau 0 physiquement ou logiquement séparés du réseau standard

**Documentation du statut de mise en œuvre** : La phase de déploiement du modèle de niveaux (planification, pilote, application partielle, application complète) DOIT être documentée dans le Classeur 3. En cas de déploiement progressif, les contrôles compensatoires pour les niveaux non encore appliqués DOIVENT être documentés.

**Vérification** : L'isolation des niveaux est vérifiée par l'analyse des journaux d'authentification (aucune connexion de Niveau 0 sur les systèmes de Niveau 1/2) ; audit trimestriel des politiques d'accès conditionnel ; configuration des PAW validée par rapport à la référence.

## Gestion des accès privilégiés (PAM)

[Organisation] DOIT mettre en œuvre les contrôles d'accès privilégié suivants :

**Contrôles requis** :

- Inventaire des comptes privilégiés : tous les comptes privilégiés documentés et classifiés
- Coffre-fort de mots de passe : mots de passe privilégiés stockés dans la solution PAM approuvée
- Enregistrement des sessions : sessions de Niveau 0 enregistrées ; enregistrement de Niveau 1 recommandé
- Accès en juste-à-temps : élévation temporaire des privilèges avec révocation automatique
- Rotation des identifiants : mots de passe des comptes de service tournés selon le calendrier défini

**Exigences de rotation des identifiants** :

| Type de compte | Rotation par défaut | Ajustement basé sur les risques |
|----------------|--------------------|---------------------------------|
| Comptes de service (Niveau 0) | 90 jours maximum | Extension jusqu'à 180 jours avec approbation du Responsable de la sécurité IT et acceptation de risque documentée |
| Comptes de service (Niveau 1/2) | 180 jours maximum | Extension jusqu'à 365 jours avec approbation du Responsable de la sécurité IT et contrôles compensatoires |
| Comptes brise-glace | Après chaque utilisation + 365 jours maximum | Pas d'ajustement — rotation systématique après chaque utilisation |
| Comptes administratifs partagés | 90 jours (déconseillés) | Migration vers des comptes individuels ; comptes partagés nécessitent une exception du RSSI |

**Approbation des ajustements basés sur les risques** : Toutes les extensions de rotation nécessitent une justification documentée, la signature de l'approbateur, des contrôles compensatoires (par ex. surveillance renforcée, accès restreint) et un renouvellement annuel. Les ajustements approuvés sont suivis dans le Classeur 3.

**Exigences de la solution PAM** :

- Coffre-fort de mots de passe : tous les identifiants privilégiés de Niveau 0/1 stockés dans la solution PAM approuvée
- Enregistrement des sessions : sessions de Niveau 0 enregistrées via PAM ou équivalent ; enregistrements conservés selon la Section 8.3
- Juste-à-temps (JIT) : demandes d'élévation de privilèges journalisées ; révocation automatique après la période définie

**Documentation du statut de déploiement** : La phase de déploiement PAM (évaluation, pilote, intégration Niveau 0, intégration Niveau 1, pleine exploitation) DOIT être documentée dans le Classeur 3. Si la PAM n'est pas totalement opérationnelle, des contrôles compensatoires DOIVENT être documentés avec une date cible de déploiement.

**Vérification** : Statut de déploiement PAM documenté dans le Classeur 3 ; pourcentage de comptes en coffre-fort suivi ; échantillons d'enregistrements de sessions révisés trimestriellement par le Responsable de la sécurité IT.

## Révisions des accès privilégiés

**Fréquence de révision** :

- Trimestrielle : tous les droits d'accès privilégiés révisés et recertifiés
- Immédiate : en cas de changement de rôle, résiliation ou incident de sécurité
- Annuelle : audit complet des accès privilégiés avec validation externe

**Processus de révision** :

- Campagnes de révision des accès initiées via l'outil de gouvernance des identités ou processus manuel
- Réviseurs : responsables hiérarchiques directs pour les accès privilégiés standard ; RSSI/Responsable de la sécurité pour le Niveau 0
- Période de révision : 10 jours ouvrables pour compléter la révision
- Absence de réponse : rappel automatique au jour 5 ; escalade vers le responsable du réviseur au jour 8 ; suspension de l'accès au jour 15 sans réponse
- Attestation : le réviseur confirme que chaque accès est toujours nécessaire ; demandes de suppression traitées dans les 48 heures

**Vérification** : Révisions trimestrielles documentées dans le Classeur 4 avec signatures d'attestation ; taux de complétion des révisions suivi comme ICP (cible : 100 %) ; attestations échantillonnées conservées pour l'audit.

## Brise-glace / Accès d'urgence

[Organisation] DOIT maintenir des procédures d'accès d'urgence :

- Comptes brise-glace sécurisés avec identifiants sous scellés (coffre physique ou enveloppe scellée PAM)
- Autorisation multi-personnes requise pour l'utilisation brise-glace (contrôle dual)
- Toute utilisation brise-glace journalisée, alertée et révisée dans les 24 heures
- Identifiants tournés immédiatement après chaque utilisation

**Tests périodiques** : Comptes brise-glace testés semestriellement (T1 et T3, par ex. janvier et juillet) pour vérifier que les identifiants fonctionnent et que les procédures sont à jour. Tests documentés avec date, testeur, confirmation d'authentification réussie et rotation post-test des identifiants.

**Vérification** : Journal d'utilisation brise-glace révisé mensuellement (utilisation attendue : minimale) ; dossiers de test conservés dans le Classeur 4 ; rotation post-utilisation confirmée via PAM ou vérification manuelle.

---

# Exigences de restriction d'accès (Contrôle A.8.3)

## Principes d'application des accès

[Organisation] DOIT appliquer les restrictions d'accès par des contrôles techniques :

- **Refus par défaut** : accès refusé par défaut ; autorisation explicite requise
- **Contrôle d'accès basé sur les rôles (RBAC)** : accès basé sur les rôles professionnels
- **Contrôle d'accès basé sur les attributs (ABAC)** : accès contextuel là où supporté
- **Alignement sur la classification des données** : restrictions d'accès correspondant à la sensibilité des données

## Contrôles d'accès techniques

**Accès au système d'exploitation** :

- Permissions du système de fichiers appliquées selon la classification des données
- Commandes privilégiées réservées aux administrateurs autorisés
- Droits d'administrateur local supprimés pour les utilisateurs standard

**Accès aux bases de données** :

- Accès direct aux bases de données restreint aux DBA
- Accès applicatif via des comptes de service avec privilèges minimum
- Colonnes sensibles chiffrées ou masquées pour les accès non privilégiés

**Accès aux applications** :

- Accès basé sur les rôles dans les applications
- Fonctions sensibles nécessitant une authentification supplémentaire (AMF renforcée)
- Délais d'expiration de session appliqués :

| Classification | Délai d'inactivité | Délai absolu |
|---------------|---------------------|--------------|
| Sensible/Critique | 15 minutes | 8 heures |
| Métier standard | 30 minutes | 12 heures |
| Consoles d'administration privilégiées | 10 minutes | 4 heures |
| Non classifié (par défaut) | 30 minutes | 12 heures |

*Le délai absolu nécessite une ré-authentification quelle que soit l'activité.*

**Accès aux API** :

- Authentification API requise (OAuth 2.0, clés API avec rotation)
- Limitation du débit appliquée
- API sensibles nécessitant une autorisation supplémentaire

**Accès aux ressources cloud** :

- Politiques IAM cloud suivant le moindre privilège
- Accès inter-comptes restreint et journalisé
- Permissions au niveau des ressources appliquées

## Restrictions d'accès basées sur le réseau

- La segmentation réseau sépare les zones de confiance
- Les règles de pare-feu imposent les frontières d'accès
- Le Contrôle d'accès réseau (NAC) vérifie la conformité des terminaux avant l'accès

## Tests des contrôles d'accès

[Organisation] DOIT vérifier les contrôles d'accès :

- Tests d'intrusion annuels incluant des tentatives de contournement des contrôles d'accès
- Audits trimestriels des permissions pour les systèmes critiques
- Analyse automatisée de la conformité pour détecter les dérives de configuration

**Vérification** : Rapports de tests d'intrusion documentant l'efficacité des contrôles d'accès ; constats remédiés selon la classification des risques.

---

# Rôles et responsabilités

## Direction générale

- Approuver la politique de sécurité de l'authentification et des accès privilégiés
- Allouer le budget pour les solutions PAM, le déploiement AMF, les outils de sécurité
- Réviser les métriques de sécurité des accès privilégiés trimestriellement
- Point d'escalade pour les incidents majeurs d'accès privilégié

## Responsable de la Sécurité des Systèmes d'Information (RSSI)

- Responsabilité globale de la sécurité de l'authentification et des accès
- Approuver la sélection des solutions PAM et la stratégie AMF
- Approuver la mise en œuvre du modèle de niveaux d'administration
- Approuver les exceptions d'accès privilégié (risque moyen/élevé)
- Réviser les rapports trimestriels sur les accès privilégiés

**Délégation** : Le RSSI peut déléguer l'autorité d'approbation au RSSI adjoint ou au Responsable de la sécurité IT pour les décisions opérationnelles. Les approbations déléguées nécessitent une révision a posteriori par le RSSI dans les 5 jours ouvrables.

## Responsable de la sécurité IT

- Gestion quotidienne de l'infrastructure d'authentification
- Surveiller les alertes d'authentification et d'accès privilégié
- Conduire les révisions trimestrielles des accès privilégiés
- Approuver les exceptions à faible risque
- Coordonner la réponse aux incidents en cas de compromission des identifiants

## Équipe de Gestion des Identités et des Accès (IAM)

- Gérer le fournisseur d'identité et l'infrastructure SSO
- Traiter les demandes d'accès privilégié
- Maintenir l'enrôlement AMF et le support
- Exécuter le provisionnement et le déprovisionnement des accès
- Générer les rapports de certification des accès

## Administrateurs systèmes

- Mettre en œuvre les contrôles d'accès sur les systèmes gérés
- Se conformer aux exigences du modèle de niveaux d'administration
- Utiliser des comptes dédiés pour les accès privilégiés (pas les comptes personnels)
- Signaler les anomalies des contrôles d'accès
- Participer aux révisions d'accès pour les systèmes gérés

## Tout le personnel

- Protéger les identifiants d'authentification
- Signaler immédiatement toute compromission suspectée des identifiants
- Compléter l'enrôlement AMF dans le délai requis
- Ne pas partager les comptes ou les identifiants
- Ne pas tenter de contourner les contrôles d'accès

---

# Gouvernance et conformité

## Surveillance de la conformité à la politique

**Surveillance continue** :

- Statut d'enrôlement AMF suivi quotidiennement
- Activité des accès privilégiés surveillée en temps réel
- Échecs d'authentification corrélés dans le SIEM

**Évaluation périodique** :

- Trimestrielle : complétion des révisions des accès privilégiés, métriques de couverture AMF
- Annuelle : évaluation complète des contrôles d'authentification et d'accès

## Gestion des exceptions

**Processus d'exception** :

- Toutes les exceptions nécessitent une justification métier documentée
- Évaluation des risques requise pour les exceptions à risque moyen/élevé
- Contrôles compensatoires obligatoires pour toutes les exceptions
- Durée maximale de l'exception : 12 mois (renouvelable avec ré-approbation)

**Autorité d'approbation des exceptions** :

| Niveau de risque | Approbateur | Fréquence de révision |
|-----------------|------------|----------------------|
| Faible | Responsable de la sécurité IT | Annuelle |
| Moyen | RSSI | Trimestrielle |
| Élevé | RSSI + Comité des risques | Mensuelle |

## Gestion de la non-conformité

**Réponse progressive** (sur une période glissante de 12 mois) :

| Occurrence | Réponse | Délai | Responsable |
|------------|---------|-------|-------------|
| Première | Rappel de sensibilisation et formation | Dans les 5 jours ouvrables | Sécurité IT |
| Deuxième (dans les 90 jours) | Notification du responsable + avertissement documenté | Dans les 3 jours ouvrables | Sécurité IT + RH |
| Troisième (dans les 12 mois) | Restriction d'accès en attente de remédiation | Immédiate | Sécurité IT + Responsable |
| Violation délibérée/Critique | Mesure disciplinaire conformément aux politiques RH | Escalade immédiate | RH + RSSI |

**Violations critiques** (escalade immédiate quel que soit l'historique) :

- Partage d'identifiants privilégiés
- Contournement des contrôles de sécurité
- Violations de l'isolation des niveaux

**Échecs aux simulations d'hameçonnage** (sur une période glissante de 12 mois) :

- 1 échec : formation de sensibilisation ciblée (dans les 7 jours)
- 2 échecs : notification du responsable + formation complémentaire (dans les 5 jours)
- 3 échecs ou plus : accès privilégié suspendu ; accès standard restreint jusqu'à démonstration d'amélioration

**Vérification** : Incidents de non-conformité suivis dans le registre des incidents de sécurité ; délais de réponse auditables.

## Métriques et reporting

**Indicateurs clés de performance (ICP)** :

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Enrôlement AMF (tous utilisateurs) | ≥ 95 % | Mensuelle |
| Enrôlement AMF (utilisateurs privilégiés) | 100 % | Hebdomadaire |
| Complétion des révisions des accès privilégiés | 100 % | Trimestrielle |
| Conformité à la politique de mots de passe | ≥ 98 % | Mensuelle |
| Intégration SSO des applications | ≥ 90 % | Trimestrielle |
| Enregistrement des sessions privilégiées (Niveau 0) | 100 % | Mensuelle |

**Reporting** : ICP suivis dans les tableaux de bord récapitulatifs avec visualisation des tendances. Rapports mensuels au Responsable de la sécurité IT ; résumé exécutif trimestriel au RSSI et à la Direction générale avec posture de conformité et priorités de remédiation.

---

# Intégration avec les autres contrôles

## Contrôles SMSI connexes

| Contrôle | Relation |
|----------|----------|
| **A.5.15-16-18 (Fondation IAM)** | Cette politique s'appuie sur la fondation IAM ; le cycle de vie des identités alimente l'authentification |
| **A.5.17 (Informations d'authentification)** | Les procédures de gestion des identifiants soutiennent cette politique |
| **A.5.18 (Droits d'accès)** | Le provisionnement des accès met en œuvre les exigences de cette politique |
| **A.6.1-2 (Sécurité de l'emploi)** | La vérification des antécédents et les conditions d'emploi soutiennent la confiance requise pour les accès privilégiés |
| **A.8.1 (Terminaux utilisateurs)** | La sécurité des postes de travail soutient la sécurité de l'authentification |
| **A.8.15-16 (Journalisation et surveillance)** | Les journaux d'authentification et d'accès alimentent la surveillance de sécurité |
| **A.8.20-22 (Sécurité des réseaux)** | La segmentation réseau soutient la restriction des accès |
| **A.5.24-27 (Gestion des incidents)** | La compromission des identifiants déclenche la réponse aux incidents |

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.2-3-5 v1.0)
- ✅ Signatures d'approbation du RSSI, DSI, Direction générale
- ✅ Exigences d'authentification définies (Section 2 — A.8.5)
- ✅ Modèle de niveaux d'administration documenté (Section 3 — A.8.2)
- ✅ Exigences de restriction d'accès spécifiées (Section 4 — A.8.3)
- ✅ Rôles et responsabilités attribués
- ✅ Références aux classeurs d'évaluation documentées (ISMS-IMP-A.8.2-3-5)

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

**A.8.5 (Authentification)** :
- Inventaire des mécanismes d'authentification
- Rapports d'enrôlement AMF et métriques de couverture
- Configurations de politique de mots de passe
- Statut d'intégration SSO des applications
- Échantillons de journaux d'authentification

**A.8.2 (Accès privilégié)** :
- Inventaire des comptes privilégiés avec classification par niveau
- Documentation du déploiement de la solution PAM
- Échantillons d'enregistrements de sessions (Niveau 0)
- Attestations de révision trimestrielle des accès
- Journaux de rotation des identifiants

**A.8.3 (Restriction d'accès)** :
- Configurations des contrôles d'accès (OS, base de données, application)
- Rapports d'audit des permissions
- Constats des tests d'intrusion (section contrôles d'accès)
- Documentation de la segmentation réseau

**Conservation des preuves** :
- Journaux d'authentification : minimum 12 mois
- Attestations de révision des accès : 3 ans
- Enregistrements des sessions privilégiées : 12 mois minimum
- Classeurs d'évaluation : version actuelle + 2 versions antérieures

---

# Annexe A : Référence rapide du modèle de niveaux d'administration

## Résumé de la classification par niveau

| Niveau | Périmètre | Exigence AMF | Poste de travail | Enregistrement de session |
|--------|-----------|--------------|-----------------|--------------------------|
| **Niveau 0** | Domaine/Entreprise | Matériel (FIDO2) | PAW requis | Obligatoire |
| **Niveau 1** | Serveur/Application | Application d'authentification | Dédié recommandé | Recommandé |
| **Niveau 2** | Poste de travail/Terminal | Application d'authentification | Standard | Optionnel |

## Règles d'isolation des niveaux

**JAMAIS** :

- Comptes de Niveau 0 sur les systèmes de Niveau 1 ou 2
- Comptes de Niveau 1 sur les systèmes de Niveau 2
- Travail quotidien (messagerie, navigation) sur les PAW

**TOUJOURS** :

- Identifiants distincts par niveau
- Mots de passe différents par compte de niveau
- PAW dédiés pour l'administration de Niveau 0

## Réponse aux violations de niveau

Toutes les violations de niveau génèrent des alertes CRITIQUES. Les violations répétées entraînent :

1. Première occurrence : formation et avertissement documenté
2. Deuxième occurrence : escalade vers le responsable
3. Troisième occurrence : suspension des accès privilégiés en attente de révision

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable des opérations IT** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de sécurité de l'authentification, de gestion des accès privilégiés et d'application technique des contrôles d'accès. Les procédures de mise en œuvre, les méthodologies d'évaluation et les spécifications des classeurs sont documentées dans ISMS-IMP-A.8.2-3-5 (S1-S5).*

<!-- QA_VERIFIED: 2026-04-02 -->
