<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.31-FR:framework:POL:a.8.31 -->
**ISMS-POL-A.8.31 — Séparation des environnements de développement, de test et de production**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Séparation des environnements de développement, de test et de production |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.31 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Opérations IT | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.8.25-26-29 (Cadre de développement sécurisé)
- ISMS-POL-A.8.32 (Gestion des changements)
- ISMS-POL-A.5.15-16-18 (Gestion des identités et des accès)
- ISMS-POL-A.8.2-3-5 (Authentification et gestion des accès privilégiés)
- ISMS-IMP-A.8.31-S1-UG/TG (Mise en œuvre de l'architecture des environnements)
- ISMS-IMP-A.8.31-S2-UG/TG (Mise en œuvre du contrôle d'accès aux environnements)
- ISMS-IMP-A.8.31-S3-UG/TG (Évaluation et tableau de bord de la séparation des environnements)
- ISMS-REF-A.8.31-Environment-Architecture-Patterns (Modèles d'architecture d'environnement)
- ISMS-REF-A.8.31-CICD-Pipeline-Integration (Intégration du pipeline CI/CD)
- ISO/IEC 27001:2022 Contrôle A.8.31

---

# Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la séparation des environnements de développement, de test et de production afin de réduire les risques associés aux modifications non autorisées et à l'exposition des données, conformément au Contrôle A.8.31 de la norme ISO/IEC 27001:2022.

**Objet** : Définir les exigences organisationnelles pour la séparation des environnements, établissant QUELLE séparation est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.31 (variantes UG/TG).

**Principes fondateurs** :

- Les environnements de production DOIVENT être protégés des activités de développement et de test
- Les données de production NE DOIVENT PAS être utilisées dans les environnements de développement ou de test
- Les changements DOIVENT suivre des chemins de promotion définis avant d'atteindre la production
- L'accès des développeurs à la production DOIT être restreint aux situations d'urgence uniquement

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la norme ISO/IEC 27001:2022, la nLPD suisse et le RGPD de l'UE.

---

# Périmètre

## Dans le périmètre

**Types d'environnements** :

- Environnements de développement (développement de code actif, expérimentation)
- Environnements de test/assurance qualité (assurance qualité, tests d'intégration, UAT)
- Environnements de préproduction/pré-production (validation finale avant la production)
- Environnements de production (opérations métier en direct)

**Périmètre technologique** :

- Tous les systèmes d'information et applications exploités par [Organisation]
- Infrastructure sur site, cloud, hybride et basée sur des conteneurs
- Systèmes internes et à destination des clients
- Systèmes gérés par des tiers traitant les données organisationnelles

**Personnel** : Tous les employés, contractants et tiers ayant accès aux systèmes organisationnels.

## Hors périmètre

- Environnements de recherche isolés non connectés aux réseaux organisationnels
- Systèmes de preuve de concept temporaires sans données organisationnelles
- Systèmes de démonstration de fournisseurs gérés entièrement par des fournisseurs

Une fois que les systèmes de recherche ou de preuve de concept passent à un usage organisationnel, ils DOIVENT se conformer à cette politique.

---

# Énoncés de politique

## Exigences d'architecture des environnements

[Organisation] DOIT maintenir des environnements séparés avec les caractéristiques suivantes :

**Niveaux d'environnements minimum**

- Les organisations DOIVENT maintenir au minimum trois niveaux d'environnements : Développement, Test/Assurance qualité et Production
- Chaque niveau d'environnement DOIT avoir un objet défini, des ressources d'infrastructure, des restrictions de traitement des données et des contrôles d'accès
- La dénomination des environnements DOIT distinguer clairement le type d'environnement pour éviter toute confusion

**Séparation réseau**

- Les environnements DOIVENT être isolés par segmentation réseau
- Le trafic inter-environnements DOIT être bloqué par défaut (refus de tout)
- Les chemins de promotion contrôlés DOIVENT être les seules connexions inter-environnements autorisées
- Les environnements de production NE DOIVENT PAS avoir de connectivité réseau directe avec les environnements de développement

**Séparation de l'infrastructure**

- Les ressources de calcul, de stockage et de base de données DOIVENT être séparées par environnement
- Les charges de travail de production et hors production NE DOIVENT PAS partager des ressources d'infrastructure
- Les identifiants et secrets DOIVENT être uniques par environnement

**Gestion de la configuration**

- Les configurations des environnements DOIVENT être gérées sous forme de code et versionnées
- Les environnements de préproduction DOIVENT refléter la configuration de production
- Les changements de configuration DOIVENT suivre le même chemin de promotion que le code applicatif

**Validation de la configuration**

- Les configurations des environnements DOIVENT être stockées dans un référentiel sous contrôle de version avec contrôle d'accès
- Les changements de configuration DOIVENT suivre le même flux de promotion que le code applicatif
- La configuration de préproduction DOIT être validée par rapport à la configuration de production avant chaque déploiement en production
- La détection de dérive de configuration DOIT être effectuée hebdomadairement avec signalement des violations au Responsable des opérations IT

## Exigences de contrôle d'accès aux environnements

**Accès basé sur les rôles**

- L'accès à chaque environnement DOIT respecter les principes du moindre privilège
- Les droits d'accès DOIVENT être définis par rôle et niveau d'environnement
- Les développeurs DOIVENT avoir un accès complet uniquement aux environnements de développement
- L'équipe des opérations DOIT avoir l'accès principal aux environnements de production

**Restrictions d'accès à la production**

- Les développeurs NE DOIVENT PAS avoir d'accès permanent à l'infrastructure de production
- L'accès à la production DOIT nécessiter des contrôles de gestion des accès privilégiés (PAM)
- L'authentification multifacteur (AMF) DOIT être requise pour tout accès à la production
- Les sessions d'accès à la production DOIVENT être journalisées et surveillées

**Accès d'urgence (Brise-glace)**

- L'accès des développeurs en urgence à la production N'EST AUTORISÉ que lors d'incidents déclarés
- L'accès brise-glace DOIT nécessiter l'approbation du Commandant d'incident et du RSSI
- L'accès brise-glace DOIT être limité dans le temps (maximum 8 heures, renouvelable avec ré-approbation) et dans son objet
- Une revue post-incident DOIT être obligatoire pour toutes les activations brise-glace

**Exigences de documentation des activations brise-glace**

Les activations brise-glace DOIVENT être journalisées avec :

- Identifiant de l'incident (du système de gestion des incidents) et niveau de gravité déclaré
- Nom, rôle et responsable du développeur demandeur
- Noms du Commandant d'incident et du RSSI approbateurs avec horodatages d'approbation
- Durée de l'accès (accordé, utilisé, expiré) et systèmes/applications consultés
- Actions effectuées pendant la session brise-glace (depuis l'enregistrement de session ou le journal d'activité)
- Résultat de la revue post-incident (complétée dans les 7 jours suivant la clôture de l'incident)
- Enseignements tirés et améliorations de processus identifiées

Les journaux brise-glace DOIVENT être :

- Maintenus dans le système PAM avec conservation automatisée
- Révisés mensuellement par le Responsable de la sécurité de l'information pour les patterns et la conformité à la politique
- Inclus dans le tableau de bord trimestriel du RSSI avec analyse des tendances (fréquence, durée, catégories de justification)

**Révisions des accès**

- L'accès aux environnements de production DOIT être révisé trimestriellement
- L'accès aux environnements de préproduction DOIT être révisé semestriellement
- L'accès aux environnements de développement/test DOIT être révisé annuellement
- L'accès des employés résiliés DOIT être révoqué dans les 24 heures

## Exigences de traitement des données

**Interdiction des données de production**

- Les données de production NE DOIVENT PAS être copiées dans les environnements de développement ou de test
- Les sauvegardes de bases de données de production NE DOIVENT PAS être restaurées dans des environnements hors production
- Les identifiants de production NE DOIVENT PAS être utilisés dans des environnements hors production

**Données approuvées pour les environnements hors production**

- Les données synthétiques (générées, non dérivées de la production) DOIVENT être privilégiées
- Les données anonymisées PEUVENT être utilisées avec l'approbation du DPD
- L'anonymisation DOIT être irréversible (pas la pseudonymisation ou le chiffrement)
- Les données anonymisées DOIVENT être supprimées dans les 30 jours suivant la complétion du projet

**Processus de validation de l'anonymisation**

Avant que le DPD approuve des données anonymisées pour une utilisation hors production :

- Le DPD DOIT tester l'efficacité de l'anonymisation par des tentatives de réidentification
- La validation DOIT évaluer le risque de réidentification par :
  - Vérification de la suppression des identifiants directs
  - Analyse des combinaisons de quasi-identifiants (évaluation k-anonymat avec k ≥ 5)
  - Simulation d'attaques de liaison avec des jeux de données accessibles au public
- Les résultats DOIVENT être documentés dans le Registre de traitement des données (ISMS-IMP-A.8.31-S2)
- Les procédures d'anonymisation DOIVENT être révisées et approuvées par le RSSI et le DPD avant leur première utilisation

**Application de la classification des données**

- Les classifications de données Confidentielles et Restreintes DOIVENT être interdites dans les environnements de développement et de test
- Une analyse automatisée DOIT détecter les données interdites dans les environnements hors production
- Les violations DOIVENT être remédiées dans les 7 jours suivant leur détection

**Analyse automatisée des données**

- Les environnements hors production DOIVENT être analysés hebdomadairement pour détecter des patterns de données de production
- L'analyse DOIT couvrir les bases de données, les systèmes de fichiers, les journaux et les images de conteneurs
- Les violations DOIVENT déclencher des alertes au Responsable de la sécurité de l'information dans les 24 heures
- La couverture et l'efficacité de l'analyse DOIVENT être vérifiées lors des auto-évaluations trimestrielles

## Exigences de promotion des environnements

**Chemin de promotion obligatoire**

- Les changements DOIVENT suivre le chemin de promotion standard : Développement → Test → Préproduction → Production
- Le déploiement direct en production DOIT être interdit sauf pour les correctifs d'urgence approuvés
- Le saut de niveaux d'environnements DOIT nécessiter une exception documentée et l'approbation du RSSI

**Exigences d'approbation**

- Les déploiements en production DOIVENT nécessiter l'approbation du Comité d'Approbation des Changements (CAC) conformément à ISMS-POL-A.8.32 (Gestion des changements)
- La composition du CAC et l'autorité d'approbation sont définies dans ISMS-POL-A.8.32
- Les déploiements en production DOIVENT avoir lieu uniquement pendant les fenêtres de changements approuvées
- Les plans de retour arrière DOIVENT être documentés et disponibles avant le déploiement en production
- Les changements d'urgence PEUVENT contourner l'approbation du CAC avec revue post-mise en œuvre dans les 48 heures

**Capacité de retour arrière**

- Les versions précédentes DOIVENT être conservées à des fins de retour arrière
- Les procédures de retour arrière DOIVENT être documentées et testées périodiquement
- L'équipe des opérations DOIT être autorisée à exécuter des retours arrière sans approbation supplémentaire pendant les incidents

## Exigences de support de la production

**Accès à la surveillance**

- Un accès en lecture seule à la surveillance DOIT être fourni pour permettre le dépannage sans accès à la production
- Les données sensibles DOIVENT être expurgées des journaux accessibles au personnel non opérationnel
- Les identifiants NE DOIVENT PAS être inclus dans les journaux

**Dépannage à distance**

- Les procédures de dépannage DOIVENT permettre la résolution des problèmes sans accès des développeurs à la production
- Des guides de procédures DOIVENT être maintenus pour les scénarios opérationnels courants
- Le partage d'écran PEUT être utilisé avec l'équipe des opérations contrôlant les systèmes de production

---

# Rôles et responsabilités

## Rôles de gouvernance

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation des exceptions ; révision de la conformité trimestrielle |
| **Responsable des opérations IT** | Sécurité de l'environnement de production ; approbation d'accès à la production ; gestion PAM |
| **Responsable du développement** | Gestion des environnements de développement/test ; mise en œuvre du flux de promotion |
| **Responsable de la sécurité de l'information** | Évaluations de conformité ; investigation des violations ; maintenance de la politique |
| **DPD** | Approbation de l'anonymisation ; conformité au traitement des données ; tests de réidentification |

## Rôles opérationnels

| Rôle | Responsabilités |
|------|----------------|
| **Propriétaires de systèmes** | Définition de l'architecture des environnements ; documentation de la conformité ; signalement des exceptions |
| **Développeurs** | Utiliser uniquement les environnements assignés ; respecter les exigences de traitement des données ; utiliser les flux de promotion |
| **Équipe d'assurance qualité** | Tests dans les environnements appropriés ; gestion des données de test ; signalement des violations |
| **Équipe des opérations** | Gestion des accès à la production ; déploiements en production ; réponse aux incidents |
| **Équipe sécurité** | Surveillance des journaux d'accès ; investigation des violations ; évaluations de sécurité |

---

# Conformité et application

## Exigences d'évaluation

| Type d'évaluation | Fréquence | Partie responsable |
|------------------|-----------|-------------------|
| Auto-évaluation | Trimestrielle | Propriétaires de systèmes, Opérations IT |
| Évaluation de sécurité | Semestrielle | Équipe de sécurité de l'information |
| Audit interne | Annuel | Audit interne |
| Audit externe | Annuel | Auditeur externe (ISO 27001) |
| Surveillance continue | En continu | Opérations de sécurité |

**Méthodologie d'évaluation**

Les évaluations DOIVENT vérifier la conformité à la séparation des environnements par :

**Validation des contrôles techniques** :

- Segmentation réseau : tester que le trafic inter-environnements est bloqué (trimestriel)
- Application des accès : vérifier que l'accès des développeurs à la production est interdit (trimestriel)
- Analyse des données : réviser les résultats d'analyse automatisée des données de production en hors production (trimestriel)
- Cohérence de la configuration : valider que la préproduction reflète la production (trimestriel)

**Validation des contrôles de processus** :

- Flux de promotion : auditer les 30 derniers jours de déploiements en production pour la conformité aux approbations (trimestriel)
- Utilisation brise-glace : réviser la documentation post-incident pour toutes les activations (trimestriel)
- Revues d'accès : vérifier la complétion et la résolution des constats (trimestriel pour la production, semestriel pour la préproduction)

## Exigences de preuves

[Organisation] DOIT maintenir des preuves de conformité, notamment :

- Documentation de l'architecture des environnements
- Matrices de contrôle d'accès par environnement
- Documentation du flux de promotion
- Dossiers de révision des accès
- Journaux d'activation brise-glace et revues post-incident
- Documentation des procédures de traitement des données
- Rapports d'évaluation de la conformité

## Non-conformité

Les violations de cette politique peuvent entraîner :

- Révocation immédiate de l'accès
- Mesure disciplinaire conformément aux politiques RH
- Signalement aux autorités réglementaires si requis
- Suivi des actions correctives dans le registre des risques

---

# Gestion des exceptions

## Critères d'exception

Des exceptions PEUVENT être approuvées uniquement pour :

- Systèmes hérités prévus pour décommissionnement dans les 12 mois
- Limitations techniques où la séparation n'est pas faisable (avec justification documentée)
- Exceptions temporaires pendant les projets de migration ou de transformation

## Processus d'exception

1. **Demande** : Le Propriétaire du système documente la justification, l'évaluation des risques, les contrôles compensatoires et le plan de remédiation
2. **Revue** : Le Responsable de la sécurité de l'information valide la justification et les contrôles compensatoires
3. **Approbation** : Le RSSI approuve ou refuse avec contrôles additionnels optionnels
4. **Suivi** : Exception suivie dans le registre des risques avec date d'expiration
5. **Ré-approbation** : Les exceptions expirent et nécessitent une ré-approbation

## Contrôles compensatoires

Lorsque des exceptions sont approuvées, les contrôles compensatoires DOIVENT inclure un ou plusieurs des éléments suivants :

- Journalisation et surveillance renforcées des accès
- Revue de code obligatoire pour toutes les modifications
- Restrictions d'accès en lecture seule
- Exigences de masquage des données
- Rigueur accrue de la gestion des changements
- Évaluations de sécurité plus fréquentes

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Anonymisation** | Processus irréversible de suppression des données personnelles rendant la réidentification des individus impossible |
| **Accès brise-glace** | Procédure d'urgence permettant aux développeurs un accès temporaire à la production lors d'incidents déclarés |
| **Environnement** | Ensemble distinct de ressources d'infrastructure servant un objet spécifique dans le cycle de vie du développement logiciel |
| **PAM (Gestion des Accès Privilégiés)** | Système de gestion et de sécurisation des identifiants privilégiés |
| **Environnement de production** | Environnement opérationnel en direct servant de vrais utilisateurs avec de vraies données métier |
| **Promotion** | Processus de déplacement des changements d'un environnement à un autre via un flux défini |
| **Pseudonymisation** | Processus réversible remplaçant les identifiants par des pseudonymes (toujours considéré comme DCP) |
| **Environnement de préproduction** | Environnement pré-production reflétant la production pour la validation finale |
| **Données synthétiques** | Données artificiellement générées ne contenant aucune vraie information personnelle |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date à définir] |
| **Responsable des opérations IT** | [Nom] | [Date à définir] |
| **Responsable du développement** | [Nom] | [Date à définir] |
| **Délégué à la Protection des Données (DPD)** | [Nom] | [Date à définir] |
| **Responsable juridique/conformité** | [Nom] | [Date à définir] |
| **Direction générale (PDG)** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de séparation des environnements de développement, de test et de production. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.31-S1, S2 et S3.*

<!-- QA_VERIFIED: 2026-04-02 -->
