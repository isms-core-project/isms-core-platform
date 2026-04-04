<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.31-FR:operational:OP-POL:a.8.31 -->
**ISMS-OP-POL-A.8.31 — Séparation des environnements de développement, de test et de production**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Séparation des environnements de développement, de test et de production |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.31 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Usage interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôle A.8.31 — Séparation des environnements de développement, de test et de production
- ISO/IEC 27002:2022 Section 8.31 — Recommandations de mise en œuvre pour la séparation des environnements
- NIST SP 800-53 Rév. 5 — CM-4 (Analyses d'impact), CM-7 (Fonctionnalité minimale), SA-11 (Tests par les développeurs), SC-32 (Partitionnement des systèmes)
- CIS Controls v8 — Mesure 16.1–16.14 (Sécurité des logiciels applicatifs)

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la séparation des environnements |
|----------|------------------------------------------------|
| A.5.15–16–18 Gestion des identités et des accès | Cadre IAM fondamental ; accès basé sur les rôles par niveau d'environnement |
| A.5.34 Vie privée et DCP | Les données de test contenant des données personnelles nécessitent une anonymisation ou un substitut synthétique |
| A.8.2–3–5 Authentification et accès privilégié | AMF pour l'accès à la production ; gestion des accès privilégiés pour les accès d'urgence |
| A.8.4 Accès au code source | Les contrôles d'accès aux dépôts et la protection des branches s'intègrent aux workflows de promotion |
| A.8.9 Gestion de la configuration | Référentiels de configuration propres à chaque environnement et détection de la dérive |
| A.8.11 Masquage des données | Techniques de protection des données utilisées dans les environnements hors production |
| A.8.15 Journalisation | Journaux d'audit pour les accès aux environnements, les promotions et les accès d'urgence |
| A.8.25–26–29 Cycle de développement sécurisé | Intégration au SDLC ; portes de sécurité entre les environnements |
| A.8.32 Gestion des changements | Approbation du Comité consultatif des changements pour les déploiements en production |
| A.8.33 Informations de test | Protection et gestion des données de test dans tous les environnements |

**Politiques internes connexes** :

- Politique de gestion des identités et des accès
- Politique de cycle de développement sécurisé
- Politique de gestion des changements
- Politique de journalisation
- Politique de classification et de traitement des données
- Politique de protection de la vie privée et des données personnelles
- Politique de réponse aux incidents

---

# Politique de séparation des environnements de développement, de test et de production

## Objectif

La présente politique a pour objectif de garantir que les environnements de développement, de test et de production sont séparés et sécurisés afin de réduire le risque d'accès non autorisé ou de modifications non autorisées dans l'environnement de production. La séparation des environnements protège les opérations métier contre les activités de développement et de test susceptibles d'introduire des erreurs, des vulnérabilités ou des modifications non autorisées dans les systèmes et données en production.

Cette politique soutient l'application de la loi fédérale suisse sur la protection des données (nLPD/revLPD) en son art. 8, en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles traitées dans les environnements de production, et en interdisant l'utilisation de données personnelles de production dans les environnements de développement et de test sans contrôles de protection équivalents. Lorsque l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences de l'art. 32 du RGPD s'appliquent également. La séparation des environnements constitue une mesure technique clé pour démontrer que les systèmes traitant des données personnelles sont soumis à des restrictions d'accès et des contrôles de traitement des données appropriés.

## Champ d'application

Tous les systèmes d'information, applications et infrastructures exploités, gérés ou contrôlés par l'organisation et relevant du périmètre défini dans la déclaration de champ d'application ISO 27001. Cela inclut :

- Tous les niveaux d'environnement : développement, test/AQ, staging/pré-production et production.
- Tous les modèles d'hébergement : sur site, cloud ([Fournisseur cloud] — ex. : AWS, Azure, GCP ou équivalent), hybride et infrastructure basée sur des conteneurs ([Plateforme de conteneurs] — ex. : Kubernetes, Docker Swarm ou équivalent).
- Tous les pipelines CI/CD ([Plateforme CI/CD] — ex. : GitHub Actions, GitLab CI, Jenkins, Azure DevOps ou équivalent) qui font progresser les changements entre les environnements.
- Les systèmes gérés par des tiers traitant des données organisationnelles pour lesquels l'organisation conserve la responsabilité de la gestion des environnements.

Tous les employés, sous-traitants et utilisateurs tiers ayant accès à tout environnement.

**Hors champ d'application** : Environnements de recherche isolés, mono-utilisateur, non connectés aux réseaux de l'organisation ; systèmes temporaires de preuve de concept ne contenant aucune donnée organisationnelle ou personnelle ; systèmes de démonstration fournisseurs entièrement gérés par les fournisseurs. Dès lors que des environnements de recherche ou de preuve de concept transitionnent vers un usage organisationnel, ils doivent se conformer à la présente politique.

## Principe

Les environnements de développement, de test et de production doivent être séparés afin de protéger l'intégrité, la disponibilité et la confidentialité des systèmes et données de production. Les changements doivent suivre des chemins de promotion définis avec révision et approbation appropriées à chaque étape. Aucun individu ne doit avoir la capacité d'apporter des modifications à la fois au développement et à la production sans révision et approbation préalables. Le niveau de séparation doit être proportionné au risque pour les opérations métier et à la sensibilité des données traitées.

L'organisation doit administrer de manière centralisée les accès aux environnements en s'appuyant sur des contrôles d'accès basés sur les rôles. L'accès par défaut aux environnements de production est « aucun accès » — toute attribution d'accès doit être explicite. Les développeurs ne doivent pas disposer d'un accès permanent à l'infrastructure de production.

---

## Définitions des environnements

L'organisation doit maintenir au minimum les niveaux d'environnement suivants. Chaque niveau doit avoir un objectif défini, des ressources d'infrastructure dédiées, des restrictions documentées sur le traitement des données, et des contrôles d'accès appliqués.

**Niveaux d'environnement** :

| Environnement | Objectif | Données autorisées | Accès |
|---------------|----------|-------------------|-------|
| **Développement** | Développement actif de code, expérimentation, intégration | Données synthétiques uniquement ; pas de données de production | Développeurs (complet) ; AQ (lecture) ; Opérations (selon besoin) |
| **Test / AQ** | Assurance qualité, tests d'intégration, tests d'acceptation utilisateur | Données synthétiques ou anonymisées (approuvées par le DPD) | Équipe AQ (complet) ; Développeurs (limité) ; Opérations (selon besoin) |
| **Staging / Pré-production** | Validation finale avant mise en production ; reflète la configuration de production | Données synthétiques ou anonymisées ; configuration de production (pas de données) | Opérations (complet) ; AQ (lecture) ; Développeurs (lecture seule pour le monitoring) |
| **Production** | Opérations métier en ligne, au service d'utilisateurs réels avec des données réelles | Données de production (données métier et personnelles réelles) | Opérations (complet) ; Développeurs (pas d'accès permanent ; accès d'urgence uniquement) |
| **Sandbox** (optionnel) | Expérimentation isolée, évaluation de technologies, preuve de concept | Données synthétiques uniquement ; pas de connectivité réseau vers d'autres environnements | Développeurs (complet) ; pas de connectivité vers les réseaux de production |

Les noms et étiquettes visuels des environnements doivent identifier clairement le type d'environnement (ex. : bannières à code couleur, préfixes de noms d'hôtes, étiquettes de console) afin de prévenir toute opération accidentelle dans le mauvais environnement.

---

## Séparation des réseaux

Les environnements doivent être isolés par segmentation réseau afin de prévenir les flux de données et les accès non intentionnels entre environnements.

**Exigences de séparation réseau** :

| Exigence | Standard |
|----------|----------|
| Isolation réseau | Chaque environnement sur un segment réseau, VLAN, VPC ou équivalent distinct |
| Règle de trafic par défaut | Tout refusé entre environnements ; seuls les chemins de promotion contrôlés sont autorisés |
| Connectivité production vers développement | Interdite — aucun chemin réseau direct entre production et développement |
| Règles de pare-feu | Documentées, révisées trimestriellement et limitées aux flux strictement nécessaires |
| Séparation DNS | Zones DNS ou espaces de noms distincts par environnement pour éviter la résolution inter-environnements |

**Séparation des environnements cloud** :

Lorsque l'organisation utilise une infrastructure cloud, la séparation des environnements doit être mise en œuvre en utilisant le modèle de limite de compte ou d'abonnement du fournisseur cloud :

| Fournisseur cloud | Mécanisme de séparation |
|-------------------|------------------------|
| AWS | Comptes AWS distincts par environnement au sein d'une Organisation AWS |
| Azure | Abonnements distincts par environnement au sein d'un Groupe de gestion |
| GCP | Projets distincts par environnement au sein d'une Organisation |
| Multi-cloud | Modèle de séparation cohérent documenté par fournisseur |

**Séparation des conteneurs et Kubernetes** :

Lorsque l'organisation utilise des plateformes d'orchestration de conteneurs, les environnements doivent être séparés en utilisant :

- Des clusters distincts par environnement (préféré pour l'isolation de la production).
- Une séparation au niveau des espaces de noms avec des politiques réseau appliquées pour les environnements hors production.
- Les charges de travail de production ne doivent pas partager un cluster avec les charges de travail de développement ou de test.
- Les registres d'images de conteneurs doivent être séparés ou contrôlés par accès par environnement.

**Sécurité des conteneurs en production :**

- Les conteneurs de production ne doivent pas monter les systèmes de fichiers de l'hôte, sauf pour les cas d'usage explicitement approuvés.
- Les conteneurs de production doivent s'exécuter avec des utilisateurs non-root.
- Les images de conteneurs de production doivent être signées et vérifiées avant déploiement.
- Les registres de conteneurs doivent être séparés par environnement (ex. : `prod.registry.example.com` vs `dev.registry.example.com`).

**Durcissement Kubernetes en production :**

- Les clusters de production doivent utiliser des plans de contrôle et des pools de nœuds distincts.
- Les normes de sécurité des pods (PSS — Pod Security Standards) doivent être appliquées au niveau « Restricted » pour la production.
- Les politiques réseau doivent tout refuser par défaut avec des règles d'autorisation explicites.
- Les comptes de service doivent être limités aux permissions minimales requises.

---

## Contrôle d'accès par environnement

L'accès à chaque environnement doit respecter le principe du moindre privilège. Les droits d'accès doivent être définis par rôle et par niveau d'environnement.

**Matrice d'accès** :

| Rôle | Développement | Test / AQ | Staging | Production |
|------|---------------|-----------|---------|------------|
| **Développeur** | Accès complet | Lecture + déploiement vers test | Lecture seule | Pas d'accès permanent |
| **Ingénieur AQ** | Lecture | Accès complet | Lecture + exécution des tests | Pas d'accès |
| **Opérations / SRE** | Selon besoin | Selon besoin | Accès complet | Accès complet |
| **Administrateur de bases de données** | Selon besoin | Selon besoin | Selon besoin | Accès complet (avec PAM) |
| **Équipe sécurité** | Lecture (audit) | Lecture (audit) | Lecture (audit) | Lecture (audit + monitoring) |
| **Sous-traitant externe** | Limité au projet | Limité au projet | Pas d'accès | Pas d'accès |

**Restrictions d'accès à la production** :

- Les développeurs ne doivent pas disposer d'accès permanent à l'infrastructure, aux bases de données ou aux consoles applicatives de production.
- Tout accès à la production doit nécessiter une authentification multifacteur (AMF).
- Les sessions d'accès à la production doivent être journalisées, enregistrées et surveillées.
- Les accès privilégiés à la production doivent être gérés via un système de gestion des accès privilégiés (PAM — Privileged Access Management) ([Outil PAM] — ex. : CyberArk, HashiCorp Boundary, AWS SSM Session Manager ou équivalent).

**Accès d'urgence (break-glass)** :

L'accès d'urgence des développeurs à la production n'est autorisé que lors d'incidents déclarés nécessitant l'expertise des développeurs pour la résolution. L'accès break-glass doit :

- Requérir l'approbation du Responsable des incidents et du RSSI (ou son délégué).
- Être limité dans le temps à un maximum de 8 heures, renouvelable avec une nouvelle approbation.
- Être limité à la portée de l'incident déclaré.
- Être journalisé avec : l'identifiant de l'incident, le développeur demandeur, l'autorité approbatrice, la durée d'accès, les systèmes accédés et les actions effectuées.
- Déclencher une revue post-incident obligatoire dans les 7 jours suivant la clôture de l'incident.

Les activations break-glass doivent être examinées mensuellement par le Responsable de la sécurité de l'information et rapportées dans le tableau de bord trimestriel du RSSI avec une analyse des tendances.

**Revues d'accès** :

| Environnement | Fréquence de révision |
|---------------|----------------------|
| Production | Trimestrielle |
| Staging | Semestrielle |
| Développement / Test | Annuelle |

Les accès des employés dont le contrat est terminé doivent être révoqués dans la même journée ouvrable dans tous les environnements. La déprovisionnement automatisé via le système de gestion des identités est préférable.

---

## Règles de gestion des données

Les données de production ne doivent pas être utilisées dans les environnements de développement ou de test. Cette exigence protège les données métier critiques contre toute exposition dans des environnements moins contrôlés et soutient la conformité nLPD pour les données personnelles.

**Interdiction des données de production** :

- Les données de production ne doivent pas être copiées, exportées, restaurées ou répliquées vers des environnements de développement, de test ou de staging.
- Les sauvegardes de bases de données de production ne doivent pas être restaurées dans des environnements hors production.
- Les identifiants de production, clés API, chaînes de connexion et secrets ne doivent pas être utilisés dans les environnements hors production.
- Les fichiers journaux contenant des données personnelles de production ne doivent pas être transférés vers des environnements hors production sans anonymisation.

**Sources de données approuvées pour la hors-production** :

| Source de données | Approbation requise | Restrictions |
|-------------------|---------------------|-------------|
| **Données synthétiques** (générées, non dérivées de la production) | Aucune approbation supplémentaire | Méthode préférée ; représentative structurellement mais entièrement artificielle |
| **Données anonymisées** (dé-identifiées de manière irréversible à partir de la production) | Approbation du Délégué à la protection des données (DPD) | L'anonymisation doit être irréversible ; validée contre le risque de ré-identification ; supprimée dans les 30 jours suivant l'achèvement du projet |
| **Données pseudonymisées** (dé-identifiées de manière réversible) | Approbation du RSSI et du DPD ; traitées comme données personnelles au sens de la nLPD | Acceptable uniquement lorsque l'anonymisation ou les données synthétiques sont techniquement infaisables ; contrôles de sécurité équivalents requis |
| **Sous-ensemble de la structure de production** (schéma uniquement, sans données) | Approbation du Responsable du développement | Schémas de bases de données, contrats d'API, modèles de configuration sans valeurs de données |

En vertu de la nLPD suisse (revLPD), les données pseudonymisées demeurent des données personnelles pour toute partie qui détient ou peut accéder à la clé de pseudonymisation. Les données pleinement anonymisées — lorsqu'il n'est pas possible de ré-identifier les personnes par aucun moyen raisonnable — sortent du champ d'application de la LPD.

**Application de la classification des données** :

- Les classifications de données Confidentielles et Restreintes doivent être interdites dans les environnements de développement et de test.
- Une analyse automatisée doit être mise en œuvre pour détecter les schémas de données de production interdits (ex. : noms réels, identifiants nationaux, numéros de comptes financiers) dans les environnements hors production. L'analyse doit couvrir les bases de données, systèmes de fichiers, fichiers journaux et images de conteneurs.
- Les violations doivent être corrigées dans les 7 jours suivant leur détection et signalées au Responsable de la sécurité de l'information.

---

## Gestion des données de test

Les données de test doivent être gérées comme un actif contrôlé tout au long du cycle de développement logiciel.

**Principes relatifs aux données de test** :

- Les données synthétiques constituent l'approche par défaut et préférée pour toutes les activités de test.
- Les données de test doivent être représentatives de la structure des données de production (même schéma, types de données, relations et caractéristiques de volume) sans contenir de données personnelles ou métier réelles.
- La génération des données de test doit être automatisée dans la mesure du possible via [Outil de données de test] (ex. : Faker, Mockaroo, Tonic.ai, Delphix ou équivalent).
- Les données de test doivent être versionnées et reproductibles afin de soutenir les tests de régression.
- Les données de test doivent être purgées des environnements hors production dans les 30 jours suivant l'achèvement du projet ou la conclusion du cycle de test.

**Validation de l'anonymisation** :

Lorsque des données de production anonymisées sont approuvées pour un usage hors production, le processus d'anonymisation doit être validé avant chaque utilisation :

1. Le Délégué à la protection des données doit vérifier que les identifiants directs ont été supprimés ou remplacés.
2. Les combinaisons de quasi-identifiants doivent être évaluées pour le risque de ré-identification.
3. Les résultats de la validation doivent être documentés et conservés à des fins d'audit.
4. Un échec de validation entraîne le rejet et la correction avant que les données puissent être utilisées.

**Données de titulaires de cartes** : Les données de titulaires de cartes (PAN, CVV, données de piste) ne doivent jamais être utilisées dans les environnements de développement ou de test, quelle que soit leur statut d'anonymisation. Des numéros de cartes synthétiques conformes aux plages de test doivent être utilisés à la place.

---

## Processus de promotion du code

Les changements doivent suivre un chemin de promotion défini du développement vers la production. Le déploiement direct en production doit être interdit, sauf pour les correctifs d'urgence approuvés.

**Chemin de promotion standard** :

```
Développement → Test / AQ → Staging → Production
```

Chaque étape de promotion doit inclure des portes de qualité et de sécurité définies.

**Exigences des portes de promotion** :

| Porte | De → Vers | Exigences |
|-------|-----------|-----------|
| **Porte 1** | Développement → Test | Révision du code effectuée (minimum 1 réviseur, pas l'auteur) ; tests unitaires automatisés réussis ; analyse statique réussie ; aucune vulnérabilité critique ou élevée |
| **Porte 2** | Test → Staging | Tests d'intégration réussis ; validation AQ ; tests de sécurité complets (SAST, DAST si applicable) ; tests de performance réussis pour les systèmes critiques |
| **Porte 3** | Staging → Production | Approbation du Comité consultatif des changements (CAB) (selon A.8.32) ; plan de retour arrière documenté et testé ; sauvegarde de production vérifiée ; procédure de déploiement révisée ; approbation du propriétaire du système |

**Séparation des tâches dans la promotion** :

- Le développeur qui rédige le code ne doit pas être la même personne qui approuve sa promotion en production.
- La personne qui promeut le code vers le staging ne doit pas être la même personne qui le promeut en production, dans la mesure où la taille de l'équipe le permet.
- Les identifiants du pipeline CI/CD pour le déploiement en production doivent être réservés à l'équipe des opérations.

**Sécurité du pipeline CI/CD** :

- Les définitions de pipeline doivent être versionnées et soumises à révision de code.
- Les identifiants et secrets du pipeline doivent être stockés dans le magasin de secrets de la plateforme de pipeline — et non codés en dur dans les définitions du pipeline.
- Chaque environnement doit disposer d'identifiants de pipeline dédiés avec les permissions minimales requises.
- Les journaux d'exécution du pipeline doivent être conservés à des fins d'audit (minimum 1 an).
- Les artefacts doivent être construits une seule fois et promus à travers les environnements (artefacts immuables) — et non reconstruits par environnement.

**Déploiements d'urgence** :

Les correctifs d'urgence peuvent contourner le chemin de promotion standard dans les conditions suivantes :

- Incident déclaré ou vulnérabilité de sécurité critique nécessitant une remédiation immédiate.
- Approbation du Responsable des incidents (ou du responsable d'astreinte) et du RSSI (ou son délégué).
- Revue post-implémentation dans les 48 heures, incluant des tests rétrospectifs dans tous les environnements contournés.
- Documentation de l'urgence dans le système de gestion des changements avec justification du contournement des portes.

**Capacité de retour arrière** :

- Les versions précédentes doivent être conservées pour permettre le retour arrière.
- Les procédures de retour arrière doivent être documentées et testées au moins trimestriellement.
- L'équipe des opérations doit être habilitée à exécuter des retours arrière sans approbation supplémentaire lors d'incidents.
- Les environnements de production doivent être sauvegardés avant chaque déploiement pour faciliter le retour arrière.
- Les données de test et les artefacts de développement doivent être supprimés avant la promotion vers la production.

---

## Séparation des configurations

Les configurations des environnements doivent être gérées pour prévenir les fuites d'identifiants, la contamination inter-environnements et la dérive de configuration.

**Exigences de séparation des configurations** :

| Exigence | Standard |
|----------|----------|
| Identifiants et secrets | Uniques par environnement ; stockés dans un gestionnaire de secrets ([Gestionnaire de secrets] — ex. : HashiCorp Vault, AWS Secrets Manager, Azure Key Vault ou équivalent) |
| Chaînes de connexion aux bases de données | Propres à chaque environnement ; jamais partagées entre niveaux |
| Points de terminaison API | URLs propres à chaque environnement ; pas de points de terminaison de production codés en dur dans le code hors production |
| Indicateurs de fonctionnalités | Configuration propre à chaque environnement ; indicateurs de production gérés séparément du développement |
| Infrastructure as Code | Configurations des environnements stockées dans le contrôle de version ; les changements suivent le même chemin de promotion que le code applicatif |

**Parité de configuration** :

- Les environnements de staging doivent refléter aussi fidèlement que possible la configuration de production (mêmes versions logicielles, même dimensionnement d'infrastructure dans les contraintes budgétaires, mêmes contrôles de sécurité).
- La dérive de configuration entre staging et production doit être détectée et rapportée. La détection de dérive doit être effectuée au moins hebdomadairement.
- Les différences entre staging et production doivent être documentées, justifiées et approuvées par le Responsable des opérations informatiques.

**Différences staging-production documentées :**

Le tableau suivant doit être maintenu par le Responsable des opérations informatiques et révisé trimestriellement. Les différences non approuvées détectées lors de la vérification de dérive doivent être investiguées et résolues.

| Élément de configuration | Staging | Production | Justification |
|--------------------------|---------|------------|---------------|
| Dimensionnement des instances | Réduit (optimisation des coûts) | Spécifications de production complètes | Optimisation des coûts ; le staging valide les fonctionnalités, pas la charge |
| Nombre de répliques | Minimum (1–2) | Selon les exigences de disponibilité (3+) | Optimisation des coûts ; le staging ne nécessite pas de haute disponibilité |
| Rétention des sauvegardes | 7 jours | Selon la politique de conservation des données (90+ jours) | Exigence de conformité pour les données de production uniquement |
| Granularité du monitoring | Intervalles de 5 minutes | Intervalles de 1 minute | La production nécessite des alertes à granularité plus fine |

**Identification des environnements** :

- Chaque environnement doit afficher une identification visuelle claire pour prévenir les opérations accidentelles dans le mauvais environnement.
- Des préfixes de noms d'hôtes, des bannières de console, des étiquettes d'onglets de navigateur et des éléments d'interface à code couleur doivent distinguer les niveaux d'environnement.
- Les environnements de production doivent afficher une identification bien visible (ex. : bannières rouges, étiquettes « [PRODUCTION] »).

---

## Séparation des environnements cloud

Lorsque l'organisation opère dans un environnement cloud ou multi-cloud, les contrôles supplémentaires suivants s'appliquent.

**Isolation des comptes et abonnements** :

- Les charges de travail de production doivent résider dans des comptes, abonnements ou projets cloud dédiés — distincts de toutes les charges de travail hors production.
- Les politiques IAM doivent empêcher les accès inter-comptes sauf via des rôles explicitement définis et audités.
- Les politiques de contrôle des services (SCP), les politiques Azure ou les politiques d'organisation doivent appliquer les limites des environnements au niveau organisationnel.
- La facturation doit être séparée par environnement pour permettre l'attribution des coûts et la détection des anomalies.

**Étiquetage des ressources cloud** :

Toutes les ressources cloud doivent être étiquetées avec l'identification de l'environnement (ex. : `env:production`, `env:staging`, `env:development`) pour soutenir :

- L'application automatisée des politiques (ex. : empêcher les rôles de développement d'accéder aux services de données de production).
- L'allocation et le reporting des coûts par environnement.
- L'analyse de conformité et le reporting d'audit.

**Gouvernance de l'Infrastructure as Code** :

- Les définitions d'infrastructure doivent être stockées dans des dépôts versionnés.
- Les modifications d'infrastructure doivent suivre le même workflow de promotion que le code applicatif (développement, révision, test, déploiement).
- Les modifications manuelles de l'infrastructure de production (« ClickOps ») doivent être interdites ; toutes les modifications doivent être appliquées via le pipeline CI/CD.

---

## Séparation des environnements et réponse aux incidents

La séparation des environnements soutient les objectifs de réponse aux incidents :

| Type d'incident | Bénéfice de la séparation des environnements | Procédure de réponse |
|-----------------|---------------------------------------------|---------------------|
| **Compromission de la production** | L'attaquant ne peut pas pivoter vers le code de développement/staging | Isoler l'environnement de production affecté ; le développement continue sans interruption |
| **Compromission du développement** | L'attaquant ne peut pas accéder aux données ou systèmes de production | Reconstruire l'environnement de développement ; pas d'impact sur la production |
| **Attaque sur la chaîne d'approvisionnement** | Code malveillant détecté lors des tests avant d'atteindre la production | Bloquer la promotion ; enquêter sur la portée ; remédier en développement |
| **Compromission du pipeline CI/CD** | Les identifiants du pipeline délimités par environnement limitent le rayon d'impact | Renouveler les identifiants affectés ; auditer la configuration du pipeline ; reconstruire les artefacts affectés |

Lors d'incidents impliquant des violations des limites d'environnement (accès non autorisé entre environnements, données de production découvertes hors production), le Responsable de la sécurité de l'information doit :

- Notifier immédiatement le RSSI et le DPD.
- Évaluer l'exposition des données et les exigences de notification réglementaire au titre de la nLPD.
- Mettre en œuvre des mesures de confinement pour prévenir tout accès inter-environnements supplémentaire.
- Conduire une revue post-incident pour identifier la cause racine et prévenir la récurrence.
- Documenter la violation dans le registre des exceptions avec les actions correctives.

---

## Expérience des développeurs et productivité

La présente politique est conçue pour protéger les systèmes de production tout en permettant une livraison logicielle efficace. Pour soutenir la productivité des développeurs :

- Les **environnements de développement locaux** sont sans restriction (sur les postes de travail des développeurs).
- L'**accès en lecture seule à la production** est disponible pour le monitoring, les journaux et les métriques.
- L'**environnement de staging** reflète fidèlement la production pour des tests réalistes.
- L'**accès d'urgence** est disponible lors d'incidents (avec approbation).
- Les **données de test synthétiques** sont facilement disponibles et représentatives des schémas de production.

Les développeurs sont encouragés à proposer des améliorations aux environnements de développement et de test qui maintiennent la sécurité tout en améliorant la productivité.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Anonymisation** | Processus irréversible de suppression des données personnelles tel que les individus ne peuvent être ré-identifiés par aucun moyen raisonnable ; les données anonymisées ne constituent pas des données personnelles au sens de la nLPD |
| **Accès d'urgence (break-glass)** | Procédure d'urgence permettant un accès à la production limité dans le temps et approuvé pour les personnes ne disposant pas d'accès permanent à la production |
| **Comité consultatif des changements (CAB)** | Groupe interfonctionnel qui révise et approuve les changements dans les environnements de production |
| **Pipeline CI/CD** | Workflow automatisé qui construit, teste et déploie les modifications logicielles à travers les niveaux d'environnement |
| **Dérive de configuration** | Divergence non intentionnelle entre la configuration prévue (telle que définie dans le code ou la documentation) et la configuration d'exécution réelle d'un environnement |
| **Artefact immuable** | Artefact de construction logicielle créé une seule fois et promu sans modification à travers tous les environnements, garantissant la cohérence |
| **AMF** | Authentification multifacteur — requérant deux facteurs de vérification ou plus pour obtenir l'accès |
| **PAM** | Gestion des accès privilégiés (Privileged Access Management) — système de gestion, de surveillance et de sécurisation des accès aux comptes et identifiants privilégiés |
| **Normes de sécurité des pods (PSS)** | Cadre natif Kubernetes pour définir des politiques de sécurité au niveau des pods ; définit trois niveaux (Privileged, Baseline, Restricted) |
| **Environnement de production** | Environnement opérationnel en ligne au service d'utilisateurs réels avec des données métier réelles |
| **Promotion** | Processus de déplacement des changements d'un niveau d'environnement à un autre via un workflow défini et contrôlé |
| **Pseudonymisation** | Processus réversible de remplacement des données identifiantes par des pseudonymes ; les données pseudonymisées demeurent des données personnelles au sens de la nLPD pour toute partie pouvant accéder à la clé de ré-identification |
| **Environnement de staging** | Environnement de pré-production reflétant la configuration de production pour la validation finale avant mise en ligne |
| **Données synthétiques** | Données générées artificiellement qui maintiennent les propriétés statistiques et structurelles des données de production sans contenir aucune information personnelle ou métier réelle |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; approbation des exceptions de séparation des environnements ; autorité d'approbation break-glass ; revue trimestrielle de conformité ; révision annuelle de la politique ; reporting à la Direction générale |
| **DT / Responsable du développement** | Gestion des environnements de développement et de test ; mise en œuvre du pipeline CI/CD ; application du workflow de promotion ; formation des développeurs à la séparation des environnements ; allocation des ressources pour l'infrastructure des environnements |
| **Responsable des opérations informatiques** | Sécurité de l'environnement de production ; approbation des accès en production ; gestion du PAM ; exécution des déploiements ; procédures de retour arrière ; surveillance de l'infrastructure ; détection de la dérive de configuration ; documentation de la parité staging-production |
| **Responsable de la sécurité de l'information** | Maintenance de la politique ; évaluations de conformité ; revue break-glass ; revue des exceptions ; surveillance de la sécurité ; investigation des incidents ; reporting trimestriel de conformité au RSSI ; réponse aux violations des limites d'environnement |
| **Délégué à la protection des données (DPD)** | Approbation de l'anonymisation pour l'utilisation de données hors production ; évaluation du risque de ré-identification ; conformité des données de test avec la nLPD ; audit du traitement des données |
| **Responsable de l'équipe AQ** | Gestion de l'environnement de test ; gestion du cycle de vie des données de test ; intégrité de l'environnement de test ; validation AQ pour les portes de promotion |
| **Propriétaires de systèmes** | Documentation de l'architecture des environnements ; preuves de conformité pour les systèmes dont ils sont responsables ; signalement des exceptions ; approbation de la promotion pour leurs systèmes |
| **Développeurs** | Utiliser uniquement les environnements assignés ; respecter les exigences de gestion des données ; utiliser les workflows de promotion définis ; signaler les violations d'environnement ; compléter la formation sur la séparation des environnements ; proposer des améliorations de productivité dans les limites de la politique |
| **Équipe sécurité** | Surveillance des journaux d'accès aux environnements ; analyse des données de production dans les environnements hors production ; investigation des violations ; évaluation de sécurité des contrôles de séparation des environnements ; réponse aux incidents de violation des limites d'environnement |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Inventaire des environnements** avec classification par niveau, modèle d'hébergement, détails de segmentation réseau et propriétaire responsable | Responsable des opérations informatiques | Maintenu en continu ; révisé annuellement | Durée de vie de l'environnement + 3 ans |
| 2 | **Documentation de segmentation réseau** (règles de pare-feu, configurations VPC, assignations VLAN) avec enregistrements de révision trimestrielle | Responsable des opérations informatiques / Équipe réseau | Trimestrielle | 3 ans |
| 3 | **Matrices de contrôle d'accès** par niveau d'environnement avec mappages rôle-permission | Responsable des opérations informatiques / Responsable du développement | Maintenu en continu ; révisé selon le calendrier de révision des accès | 3 ans |
| 4 | **Enregistrements de révision des accès** (production trimestrielle, staging semestrielle, développement/test annuelle) | Propriétaires de systèmes / Responsable des opérations informatiques | Selon calendrier | 3 ans |
| 5 | **Journaux d'activation break-glass** avec identifiant d'incident, approbateur, durée, actions et revue post-incident | Responsable de la sécurité de l'information | Par événement ; révision mensuelle | 3 ans |
| 6 | **Configuration du pipeline CI/CD** montrant les portes de promotion, exigences d'approbation et séparation des tâches | Responsable du développement / DevOps | Maintenu en continu ; révisé trimestriellement | 2 ans |
| 7 | **Enregistrements de déploiement en production** avec approbation CAB, plan de retour arrière et résultat du déploiement | Responsable des opérations informatiques | Par déploiement | 3 ans |
| 8 | **Enregistrements de gestion des données de test** (journaux de génération de données synthétiques, approbations d'anonymisation, confirmations de purge) | Responsable AQ / DPD | Par cycle de test | 3 ans |
| 9 | **Résultats des analyses des environnements hors production** montrant l'absence de données de production détectées (ou enregistrements de remédiation pour les violations) | Équipe sécurité | Analyse hebdomadaire ; reporting mensuel | 2 ans |
| 10 | **Rapports de dérive de configuration** entre staging et production avec enregistrements de résolution | Responsable des opérations informatiques | Détection hebdomadaire ; révision trimestrielle | 2 ans |
| 11 | **Documentation de séparation des comptes/abonnements cloud** avec exports de politiques IAM et politiques de contrôle des services | Responsable des opérations informatiques / Équipe cloud | Trimestrielle | 3 ans |
| 12 | **Registre des exceptions** (demandes, approbations, contrôles compensatoires, dates d'expiration, révisions trimestrielles) | Responsable de la sécurité de l'information | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |
| 13 | **Enregistrements de formation à la séparation des environnements** pour les développeurs, équipes AQ et opérations | RSSI / RH | Annuelle | Durée d'emploi + 3 ans |
| 14 | **Enregistrements de déploiements d'urgence** avec justification du contournement du chemin de promotion standard et revue post-implémentation | Responsable des opérations informatiques / Responsable du développement | Par événement | 3 ans |
| 15 | **Documentation de parité de configuration staging-production** avec différences approuvées et enregistrements de révision trimestrielle | Responsable des opérations informatiques | Trimestrielle | 2 ans |
| 16 | **Enregistrements d'incidents de violation des limites d'environnement** avec actions de confinement, analyse de la cause racine et actions correctives | Responsable de la sécurité de l'information | Par événement | 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, incluant notamment les rapports d'accès aux environnements, les audits de segmentation réseau, les revues de configuration des pipelines CI/CD, les rapports d'analyse des données, les enregistrements d'approbation des déploiements, les enregistrements de réalisation des révisions d'accès, les audits internes et externes, et le retour d'information au propriétaire de la politique.

**Métriques de conformité** :

| Métrique | Cible | Fréquence de mesure |
|----------|--------|---------------------|
| Environnements avec séparation réseau conforme (refus par défaut, aucun chemin développement-production) | 100 % | Trimestrielle |
| Accès à la production limité au personnel des opérations autorisé (pas d'accès permanent aux développeurs) | 100 % | Trimestrielle |
| Déploiements en production avec approbation CAB et plan de retour arrière documenté | >= 95 % | Mensuelle |
| Environnements hors production sans données de production détectées (analyse nette) | >= 95 % | Mensuelle |
| Activations break-glass avec documentation complète et revue post-incident | 100 % | Par événement |
| Révisions d'accès complétées selon le calendrier par niveau d'environnement | >= 90 % | Trimestrielle |
| Pipelines CI/CD appliquant les portes de promotion et la séparation des tâches | >= 95 % | Trimestrielle |
| Données de test purgées dans les 30 jours suivant l'achèvement du projet | >= 90 % | Trimestrielle |
| Images de conteneurs en production signées et vérifiées | 100 % | Mensuelle |

**Notation de la conformité** :

| Composant | Pondération | Calcul |
|-----------|-------------|--------|
| Conformité de la séparation réseau | 25 % | (Environnements avec séparation réseau conforme) / Total des environnements × 100 |
| Conformité du contrôle d'accès | 25 % | (Environnements avec accès basé sur les rôles correct + révisions effectuées) / Total × 100 |
| Conformité du processus de promotion | 25 % | (Déploiements en production conformes avec approbation + plan de retour arrière) / Total des déploiements × 100 |
| Conformité de la gestion des données | 25 % | (Environnements hors production sans données de production + données de test purgées selon calendrier) / Total × 100 |

**Tableau de bord de conformité (cible) :**

Le Responsable de la sécurité de l'information doit générer ce tableau de bord trimestriellement et le présenter lors de la revue de direction :

| Domaine | Score | Statut |
|---------|-------|--------|
| **Conformité globale** | [calculé] | VERT (>= 90 %) / ORANGE (>= 70 %) / ROUGE (< 70 %) |
| Séparation réseau | [calculé] | |
| Contrôle d'accès | [calculé] | |
| Processus de promotion | [calculé] | |
| Gestion des données | [calculé] | |

Les éléments nécessitant attention et les améliorations récentes doivent être mis en évidence dans le rapport du tableau de bord.

**Gestion de la non-conformité** : Un score inférieur à 70 % nécessite une escalade immédiate au RSSI et un plan de remédiation. Entre 70 et 89 %, une supervision du Responsable de la sécurité de l'information avec des revues mensuelles est requise. À partir de 90 %, le suivi trimestriel standard s'applique.

**Responsabilité de remédiation par composant de score** :

| Composant | En dessous de la cible | Responsable de la remédiation | Escalade |
|-----------|------------------------|-------------------------------|----------|
| Conformité de la séparation réseau | < 100 % | Responsable des opérations informatiques | RSSI sous 15 jours de retard |
| Conformité du contrôle d'accès | < 100 % (production) | Responsable des opérations informatiques / Responsable du développement | RSSI sous 15 jours de retard |
| Conformité du processus de promotion | < 95 % | Responsable du développement / DevOps | RSSI sous 30 jours de retard |
| Conformité de la gestion des données | < 95 % | Responsable AQ / DPD | RSSI immédiatement si données personnelles de production trouvées hors production |

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation documentée du risque, contrôles compensatoires et date de révision définie (maximum 12 mois). Les exceptions doivent être rapportées à l'Équipe de revue de direction.

Les exceptions ne peuvent être approuvées que pour : les systèmes legacy dont le déclassement est programmé dans les 12 mois ; les limitations techniques rendant une séparation complète infaisable (avec justification documentée et contrôles compensatoires) ; les exceptions temporaires lors de projets de migration ou de transformation (avec date de fin définie).

Lorsque des exceptions sont approuvées, les contrôles compensatoires doivent inclure un ou plusieurs des éléments suivants : journalisation et surveillance renforcées des accès, révision obligatoire du code pour tous les changements, restrictions d'accès en lecture seule, exigences de masquage des données, rigueur accrue dans la gestion des changements, et évaluations de sécurité plus fréquentes.

## Non-conformité

Tout employé reconnu coupable d'avoir violé la présente politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement. Les violations de la politique doivent être documentées, investiguées par le Responsable de la sécurité de l'information et rapportées au RSSI.

Les violations impliquant l'exposition de données de production dans des environnements hors production doivent être traitées comme des incidents de données et signalées au Délégué à la protection des données pour évaluation au titre des exigences de notification de violation de la nLPD.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions des capacités des plateformes cloud et de conteneurs, les menaces émergentes pesant sur la séparation des environnements (attaques sur la chaîne d'approvisionnement, compromission des pipelines CI/CD, vulnérabilités d'évasion de conteneurs), les changements réglementaires (nLPD, RGPD), les constatations d'audit, et les enseignements tirés des activations break-glass et des incidents d'environnement.

---

# Zones de la norme ISO 27001 couvertes

Politique de séparation des environnements de développement, de test et de production — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et standards |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.9 Gestion de la configuration |
| | 8.11 Masquage des données |
| | 8.25 Cycle de développement sécurisé |
| | **8.31 Séparation des environnements de développement, de test et de production** |
| | 8.32 Gestion des changements |
| | 8.33 Informations de test |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données ; séparation des environnements comme mesure technique ; interdiction des données personnelles de production dans les environnements hors production sans contrôles équivalents |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données ; contrôles d'accès aux environnements comme mesure de sécurité |
| RGPD de l'UE (le cas échéant) | Art. 25 — Protection des données dès la conception et par défaut (séparation des environnements) ; Art. 32 — Sécurité du traitement (contrôle d'accès par environnement) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.31 — Séparation des environnements de développement, de test et de production |
| ISO/IEC 27002:2022 | Section 8.31 — Recommandations de mise en œuvre pour la séparation des environnements |
| NIST SP 800-53 Rév. 5 | CM-4 (Analyses d'impact), CM-7 (Fonctionnalité minimale), SA-11 (Tests et évaluation par les développeurs), SC-32 (Partitionnement des systèmes) |
| CIS Controls v8 | 4.1 (Configuration sécurisée des actifs d'entreprise), 16.1–16.4 (Sécurité des logiciels applicatifs) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
