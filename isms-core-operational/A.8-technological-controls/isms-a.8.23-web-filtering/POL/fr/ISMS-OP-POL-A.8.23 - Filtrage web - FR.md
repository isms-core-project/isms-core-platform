<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.23-FR:operational:OP-POL:a.8.23 -->
**ISMS-OP-POL-A.8.23 — Filtrage web**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Filtrage web |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.23 |
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

- ISO/IEC 27001:2022 Contrôle A.8.23 — Filtrage web

**Contrôles Annexe A associés** :

| Contrôle | Relation avec le filtrage web |
|----------|-------------------------------|
| A.5.7 Renseignement sur les menaces | Les flux de renseignement sur les menaces informent les listes de blocage du filtrage web et la catégorisation des URL |
| A.5.10 Utilisation acceptable de l'information | La politique d'utilisation acceptable définit l'usage web autorisé et interdit |
| A.8.7 Protection contre les logiciels malveillants | Le filtrage web empêche la livraison de logiciels malveillants via les téléchargements automatiques et les sites malveillants |
| A.8.16 Activités de surveillance | Les journaux de filtrage web alimentent la surveillance sécuritaire et la détection d'anomalies |
| A.8.20 Sécurité des réseaux | Le filtrage web est un contrôle de sécurité au niveau réseau |
| A.8.21 Sécurité des services réseau | La passerelle web sécurisée (SWG) est un service de sécurité réseau géré |
| A.8.22 Cloisonnement des réseaux | Le filtrage web est appliqué aux frontières des segments réseau |
| A.8.24 Utilisation de la cryptographie | Considérations d'inspection TLS pour le trafic web chiffré |

**Politiques internes associées** :

- Politique d'utilisation acceptable
- Politique de sécurité des réseaux
- Politique de sécurité des terminaux
- Politique des activités de surveillance (A.8.16)
- Politique de protection contre les logiciels malveillants
- Politique de protection de la vie privée et des données à caractère personnel

---

# Politique de filtrage web

## Finalité

La présente politique a pour objet de gérer l'accès aux sites web externes afin de réduire l'exposition aux contenus malveillants, d'empêcher les fuites de données via les canaux web et de faire respecter les exigences d'utilisation acceptable. Le filtrage web protège les systèmes de l'organisation contre les logiciels malveillants livrés via les téléchargements automatiques, les sites de phishing et d'autres menaces véhiculées par le web.

Le filtrage web est un contrôle clé identifié dans le cadre de l'évaluation des risques de sécurité de l'information de l'organisation. Le périmètre de filtrage et les décisions de catégories définis dans la présente politique sont directement informés par le plan de traitement des risques, traitant des risques tels que : infection par des logiciels malveillants via des menaces web, vol d'identifiants via le phishing, fuites de données via des services web non autorisés, et atteinte à la réputation due à l'accès à des contenus inappropriés.

La présente politique soutient la nLPD (revLPD) suisse art. 8 en mettant en œuvre le filtrage web comme mesure technique pour protéger les données personnelles contre la compromission via des vecteurs d'attaque web. Le filtrage web qui surveille l'activité de navigation des employés doit être conforme au droit suisse du travail (CO art. 328/328b) et à l'interdiction de la surveillance des comportements (OLT 3 art. 26). Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD art. 32 s'appliquent également.

## Champ d'application

La présente politique s'applique à :

- Tout le trafic web (HTTP/HTTPS) provenant des appareils et réseaux gérés par l'organisation.
- Tous les employés, contractants et utilisateurs tiers accédant à Internet via l'infrastructure de l'organisation.
- Tous les environnements : réseau d'entreprise, travailleurs à distance (via VPN ou proxy cloud), et réseaux invités (périmètre limité).
- Toutes les méthodes d'accès web : navigateurs, applications effectuant des appels HTTP/HTTPS, et connexions API vers des services externes.

Hors champ d'application :
- Filtrage des courriels (couvert par les politiques de sécurité des terminaux et de protection contre les logiciels malveillants).
- Contrôles au niveau applicatif pour des plateformes SaaS spécifiques (couverts par la politique des services cloud, A.5.19-23).

## Principe

L'accès aux sites web externes doit être géré pour réduire l'exposition aux contenus malveillants. Le filtrage web doit opérer selon une approche fondée sur le risque : bloquer automatiquement les menaces connues, restreindre les catégories discrétionnaires par politique, et permettre un accès légitime aux activités métier sans friction inutile. Le filtrage doit s'appliquer de manière cohérente quelle que soit la localisation ou l'appareil de l'utilisateur.

---

## Architecture de filtrage web

### Approche de filtrage

L'organisation doit mettre en œuvre le filtrage web en utilisant une ou plusieurs des technologies suivantes :

| Couche | Technologie | Objectif |
|--------|-----------|---------|
| **Filtrage DNS** | Service de filtrage au niveau DNS (p. ex. Cisco Umbrella, Cloudflare Gateway, DNSFilter, ou équivalent) | Première ligne de défense ; bloque la résolution des domaines malveillants et interdits avant l'établissement de la connexion |
| **Filtrage URL** | Passerelle web sécurisée (SWG) ou proxy avec base de données de catégorisation des URL | Inspecte le chemin URL complet ; applique des politiques basées sur les catégories ; assure un contrôle granulaire |
| **Inspection TLS** | SWG ou proxy effectuant le déchiffrement et l'inspection SSL/TLS | Inspecte le trafic web chiffré pour les menaces cachées dans HTTPS (s'applique à des catégories sélectionnées — voir la section Inspection TLS) |
| **Isolation du navigateur** (optionnel) | Isolation du navigateur à distance (RBI) pour les sites à risque élevé ou non catégorisés | Affiche le contenu web dans un bac à sable cloud ; seule la sortie visuelle sécurisée est diffusée à l'utilisateur |

### Modèle de déploiement

| Environnement | Méthode de filtrage |
|---------------|---------------------|
| **Réseau d'entreprise** | SWG/proxy ou filtrage DNS appliqué au périmètre du réseau |
| **Travailleurs à distance** | Agent SWG cloud ou filtrage DNS sur les terminaux gérés ; politique cohérente quel que soit le réseau |
| **Appareils BYOD** | Filtrage DNS (léger, respectueux de la vie privée) ; l'inspection TLS ne doit **pas** être effectuée sur les appareils personnels |
| **Réseau invité** | Filtrage DNS pour les catégories logiciels malveillants/phishing uniquement ; filtrage des catégories discrétionnaires non appliqué |

Le filtrage DNS doit être appliqué sur tous les appareils gérés comme niveau de base. Les requêtes DNS directes vers des résolveurs externes (y compris DNS sur HTTPS (DoH) et DNS sur TLS (DoT) vers des résolveurs non approuvés) doivent être bloquées au niveau du pare-feu pour empêcher le contournement du filtrage.

### Disponibilité et performance (SOC 2 : A1.1)

La plateforme de filtrage web doit satisfaire aux objectifs de niveau de service suivants :

| OLS | Cible | Mesure |
|-----|-------|--------|
| **Disponibilité** | ≥ 99,9 % de disponibilité (mesurée mensuellement) | Tableau de bord de surveillance de la plateforme |
| **Latence** | ≤ 50 ms de latence supplémentaire par requête web (p95) | Tests de performance périodiques |
| **Basculement** | Basculement automatique vers le chemin de filtrage secondaire ou passage en mode ouvert dans les 5 minutes | Tests de basculement annuels |
| **Capacité** | Plateforme dimensionnée pour le trafic de pointe + 30 % de marge | Révision de capacité trimestrielle |

Si la plateforme de filtrage subit une dégradation soutenue dépassant les seuils OLS, les Opérations IT doivent mettre en œuvre la procédure de réponse aux incidents documentée. Le passage en mode ouvert (autorisant le trafic non filtré) n'est permis qu'à titre temporaire en cas de panne de la plateforme et doit être journalisé, signalé au RSSI et remédié dans les 4 heures.

### Gestion des changements pour les règles de filtrage (SOC 2 : CC8.1)

Les modifications de la configuration du filtrage web (politiques de catégories, listes de blocage/autorisation, paramètres d'inspection TLS, architecture de déploiement) doivent suivre le processus de gestion des changements de l'organisation :

1. **Demande** : Demande de changement soumise avec justification, périmètre et évaluation des risques.
2. **Révision** : La Sécurité IT examine le changement pour les implications sécuritaires ; le Conseiller à la protection des données examine l'impact sur la vie privée si la surveillance des employés est affectée.
3. **Test** : Changements testés dans un environnement staging ou déploiement limité si possible.
4. **Approbation** : Changements standard approuvés par le responsable de la Sécurité IT ; changements significatifs (nouveaux blocages de catégories, modifications du périmètre d'inspection TLS) approuvés par le RSSI.
5. **Mise en œuvre** : Changement déployé par les Opérations IT pendant la fenêtre de maintenance approuvée.
6. **Vérification** : Vérification post-implémentation que le changement fonctionne comme prévu.
7. **Documentation** : Changement enregistré dans le journal des changements avec les états de configuration avant/après.

Les changements d'urgence (p. ex. blocage d'une campagne de phishing active) peuvent contourner l'approbation standard mais doivent être documentés rétrospectivement dans les 24 heures.

### Gestion des fournisseurs (SOC 2 : CC9.2)

Lorsque le filtrage web est fourni par un service tiers (SWG cloud, fournisseur de filtrage DNS) :

- Le fournisseur doit être inclus dans le programme de gestion des risques fournisseurs de l'organisation.
- Le rapport SOC 2 Type II ou la certification ISO 27001 doivent être révisés annuellement.
- La conformité aux SLA (disponibilité, latence, taux de détection des menaces, délai de réponse du support) doit être surveillée par rapport aux seuils contractuels.
- Les accords de traitement des données doivent traiter : la gestion des données de navigation des employés, la résidence des données, les périodes de conservation et la notification des incidents.
- Le risque de verrouillage du fournisseur doit être évalué ; l'organisation doit conserver la capacité de migrer vers un fournisseur alternatif dans un délai raisonnable.

---

## Catégorisation des URL et règles de filtrage

### Blocage obligatoire — Catégories de menaces sécuritaires

Les catégories suivantes doivent être bloquées pour tous les utilisateurs sans exception :

| # | Catégorie | Justification |
|---|----------|--------------|
| 1 | **Distribution de logiciels malveillants** | Sites hébergeant ou distribuant activement des logiciels malveillants, des kits d'exploitation ou des téléchargements automatiques |
| 2 | **Phishing et fraude** | Sites conçus pour collecter des identifiants, des informations financières ou des données personnelles |
| 3 | **Commande et contrôle (C2)** | Infrastructure de botnet et de menaces persistantes avancées connue |
| 4 | **Rançongiciels** | Sites de distribution, de paiement et de communication de rançongiciels |
| 5 | **Logiciels espions et publicitaires** | Sites distribuant des logiciels indésirables ou des outils de traçage |
| 6 | **Cryptominage** | Sites exécutant des scripts de minage de cryptomonnaies non autorisés |
| 7 | **Kits d'exploitation** | Sites hébergeant des cadres d'exploitation de navigateurs et de plugins |
| 8 | **DNS dynamique (malveillant)** | Fréquemment utilisé pour l'infrastructure malveillante ; bloquer les fournisseurs de DNS dynamique connus comme malveillants |
| 9 | **Contenu illicite** | Contenu interdit par le droit suisse ou le droit applicable |
| 10 | **Matériel d'abus sexuel d'enfants** | Obligation légale obligatoire de blocage |

### Blocage obligatoire — Catégories de politique

Les catégories suivantes doivent être bloquées sauf si une exception approuvée existe :

| # | Catégorie | Justification |
|---|----------|--------------|
| 11 | **Contournement de proxy et anonymiseurs** | Proxys web, services VPN et nœuds Tor utilisés pour contourner les contrôles de filtrage |
| 12 | **Outils et ressources de piratage** | Bases de données d'exploits, tutoriels de piratage et distribution d'outils d'attaque (exception : équipe de sécurité avec justification documentée) |
| 13 | **Partage de fichiers pair à pair** | Risque de fuite de données et vecteur de logiciels malveillants |
| 14 | **Violation du droit d'auteur / piratage** | Risque de propriété intellectuelle et légal |

### Restriction discrétionnaire — Catégories surveillées

Les catégories suivantes peuvent être restreintes, surveillées ou autorisées selon la politique organisationnelle :

| # | Catégorie | Politique par défaut | Notes |
|---|----------|---------------------|-------|
| 15 | **Stockage cloud personnel** (Dropbox, Google Drive personnel, etc.) | Restreindre | Risque de fuite de données ; stockage cloud d'entreprise autorisé |
| 16 | **Webmail personnel** (Gmail, Outlook personnel, etc.) | Restreindre | Risque de fuite de données ; courriel d'entreprise autorisé |
| 17 | **Réseaux sociaux** | Autoriser avec surveillance | Des cas d'usage métier existent ; restreindre les envois si possible |
| 18 | **Médias en streaming / vidéo** | Autoriser avec limites de bande passante | Gestion de la bande passante ; restreindre aux heures de pointe si nécessaire |
| 19 | **Jeux** | Bloquer pendant les heures de travail | Productivité ; autoriser en dehors des heures si souhaité |
| 20 | **Contenu adulte** | Bloquer | Adaptation au lieu de travail |
| 21 | **Jeux d'argent** | Bloquer | Adaptation au lieu de travail et risque légal |

### Autorisé — Catégories critiques pour l'entreprise

Les catégories suivantes ne doivent pas être filtrées ou restreintes :

| Catégorie | Exemples |
|----------|---------|
| **Affaires et finance** | Banques, portails sectoriels, services professionnels |
| **Gouvernement et juridique** | Sites réglementaires, portails gouvernementaux, bases de données juridiques |
| **Technologie et IT** | Éditeurs de logiciels, documentation, ressources pour développeurs |
| **Éducation et formation** | Plateformes d'e-learning, développement professionnel, ressources académiques |
| **Actualités et médias** | Principaux organes de presse, publications sectorielles |
| **Moteurs de recherche** | Google, Bing, DuckDuckGo |
| **Applications SaaS d'entreprise** | Applications cloud approuvées selon le registre SaaS de l'organisation |

### Sites web non catégorisés

Les sites web non catégorisés par la solution de filtrage doivent être traités comme suit :

- **Par défaut** : Autoriser avec journalisation (pour les organisations avec une appétence pour le risque plus faible : restreindre avec option de dérogation utilisateur).
- Tout accès aux sites non catégorisés doit être journalisé pour révision sécuritaire.
- Si l'isolation du navigateur est déployée, les sites non catégorisés devraient être affichés via l'isolation par défaut.

---

## Inspection TLS

### Finalité

Environ 80 % du trafic web est chiffré (HTTPS). Sans inspection TLS, les menaces cachées dans le trafic chiffré ne peuvent pas être détectées par la solution de filtrage web. L'inspection TLS déchiffre, inspecte et rechiffre le trafic HTTPS au niveau de la SWG/proxy.

### Exigences

| Exigence | Spécification |
|----------|--------------|
| **Déploiement** | L'inspection TLS doit être activée sur la SWG/proxy pour le trafic provenant des appareils gérés par l'organisation |
| **Certificat** | Un certificat d'autorité de certification racine privé doit être déployé sur tous les terminaux gérés via MDM, Stratégie de groupe ou équivalent |
| **Firefox** | Firefox utilise son propre magasin de certificats ; le certificat d'autorité de certification racine privé doit être déployé séparément via la politique entreprise Firefox |
| **Performance** | La SWG/proxy doit être dimensionnée pour la charge de travail d'inspection TLS ; le protocole QUIC (UDP 443) doit être bloqué pour forcer l'inspection HTTPS basée sur TCP |

### Exclusions de la vie privée — Catégories à exclure de l'inspection TLS

Les catégories suivantes doivent être **exclues** de l'inspection TLS pour protéger la vie privée et éviter les problèmes techniques :

| # | Catégorie | Raison |
|---|----------|--------|
| 1 | **Finance / banque** | Sensibilité des identifiants ; considérations réglementaires |
| 2 | **Santé** | Confidentialité des données de santé (données personnelles sensibles selon la nLPD) |
| 3 | **Portails gouvernementaux** | Sensibilité réglementaire |
| 4 | **Applications avec épinglage de certificat** | Incompatibilité technique (p. ex. certaines API, applications financières) |
| 5 | **Appareils personnels (BYOD)** | Pas de fondement légal pour l'inspection TLS sur les appareils personnels |

### Exigences légales pour l'inspection TLS

- Les employés doivent être informés à l'avance que le trafic web chiffré peut être déchiffré et inspecté à des fins de sécurité.
- La politique d'utilisation acceptable doit documenter l'inspection TLS et son objectif.
- Les données d'inspection TLS doivent être traitées uniquement à des fins de sécurité (détection de logiciels malveillants, prévention des fuites de données, application des politiques) — et non pour la surveillance comportementale.
- Le trafic des appareils BYOD et du réseau invité ne doit **pas** être soumis à l'inspection TLS.

---

## Intégration du renseignement sur les menaces

### Mises à jour des listes de blocage

Les listes de blocage du filtrage web doivent être mises à jour à l'aide de renseignements sur les menaces provenant de plusieurs sources :

| Type de source | Exemples | Fréquence de mise à jour |
|----------------|---------|--------------------------|
| **Fournisseur** | Base de données de catégorisation des URL du fournisseur de la solution de filtrage | Temps réel ou quotidien (automatique) |
| **Flux de renseignement sur les menaces** | ISAC sectoriels, agences gouvernementales de cybersécurité (NCSC.ch, MELANI), flux commerciaux | Automatique si pris en charge ; révision manuelle hebdomadaire |
| **Renseignement interne** | IOC issus des investigations d'incidents, signalements de phishing des employés, recherches de l'équipe de sécurité | Ad hoc ; ajouté dans les 4 heures suivant l'identification |
| **Flux communautaires** | Renseignement sur les menaces open source (MISP, abuse.ch, PhishTank, URLhaus) | Automatique si pris en charge |

### Phishing et ingénierie sociale

- Les URL de phishing signalées par les employés doivent être évaluées et ajoutées à la liste de blocage dans les **4 heures** pendant les heures ouvrables.
- Les URL de simulation de phishing doivent être exclues du filtrage web pendant les campagnes de test (coordonnées entre la Sécurité de l'information et les Opérations IT).

### Intégration de la réponse aux incidents

Les événements de filtrage web doivent être intégrés au processus de gestion des incidents de l'organisation (A.5.24-28). Les seuils suivants déclenchent la création d'un incident :

| Déclencheur | Gravité | Action |
|-------------|---------|--------|
| Un utilisateur accède à un site de logiciels malveillants/C2 confirmé (filtrage contourné ou défaillant) | Critique | Incident immédiat ; isoler le terminal ; investigation légale |
| Plusieurs utilisateurs bloqués depuis la même URL de phishing en 1 heure | Élevé | Investiguer la campagne de phishing potentielle ; évaluer si des utilisateurs ont accédé à l'URL avant le blocage |
| Un utilisateur tente à plusieurs reprises d'accéder à des catégories bloquées (> 20 tentatives/jour) | Moyen | Investiguer pour violation de politique ou compte compromis |
| Contournement de la plateforme de filtrage détecté (évasion DoH/proxy réussie) | Élevé | Bloquer le vecteur d'évasion ; investiguer la portée ; évaluer les lacunes d'application de la politique |
| Pic soudain de requêtes bloquées (> 200 % de la référence) | Moyen | Évaluer pour campagne de logiciels malveillants, infrastructure compromise ou mauvaise configuration |

---

## Processus d'exception et de dérogation

### Demande d'accès aux sites bloqués

Lorsqu'un utilisateur rencontre un site web bloqué requis à des fins professionnelles légitimes :

1. **Page de blocage** : L'utilisateur voit une page de blocage indiquant la raison du blocage et un lien pour demander l'accès.
2. **Demande** : L'utilisateur soumet une demande d'exception via [système de tickets / portail libre-service] avec :
   - URL ou domaine demandé.
   - Justification métier.
   - Durée nécessaire (temporaire ou permanente).
   - Contexte de département et de projet.
3. **Révision** : La demande est examinée par :
   - **Responsable hiérarchique** : Confirme la justification métier (dans 1 jour ouvrable).
   - **Sécurité IT** : Évalue le risque sécuritaire (dans 1 jour ouvrable).
4. **Décision** :
   - **Approuver** : URL/domaine ajouté à la liste d'autorisation (durée limitée de préférence ; par défaut : 90 jours).
   - **Refuser** : Utilisateur notifié avec la raison ; alternative suggérée si possible.
   - **Escalader** : Les dérogations de catégories à risque élevé (contournement de proxy, outils de piratage) nécessitent l'approbation du RSSI.
5. **Mise en œuvre** : Les Opérations IT ajoutent l'exception approuvée à la solution de filtrage dans les 4 heures suivant l'approbation.
6. **Documentation** : Exception enregistrée dans le registre des exceptions avec le demandeur, la justification, l'approbateur, la date d'expiration et la date de révision.

### Registre des exceptions

| Champ | Description |
|-------|-------------|
| Identifiant de l'exception | Identifiant unique |
| URL/Domaine | Ce qui est autorisé |
| Demandeur | Nom, département |
| Justification métier | Pourquoi l'accès est requis |
| Évaluation des risques | Résultat de l'évaluation des risques sécuritaires |
| Approbateur | Nom et date |
| Date d'expiration | Par défaut : 90 jours (temporaire) ou révision annuelle (permanente) |
| Date de révision | Quand l'exception est prochainement révisée |
| Mesures compensatoires | Tout contrôle supplémentaire appliqué (p. ex. surveillance, journalisation) |

### Gouvernance des exceptions

- Toutes les exceptions doivent être révisées **trimestriellement** par la Sécurité IT.
- Les exceptions expirées doivent être automatiquement révoquées.
- Les exceptions inutilisées (aucun accès enregistré en 90 jours) doivent être supprimées.
- Le nombre total d'exceptions actives doit être rapporté au RSSI trimestriellement.
- Les exceptions doivent avoir le périmètre minimal nécessaire : URL spécifique préférée au domaine complet ; domaine préféré à la catégorie entière.

---

## Considérations pour les travailleurs à distance et les BYOD

### Travailleurs à distance (appareils gérés)

- L'agent SWG cloud ou de filtrage DNS doit être installé sur tous les terminaux gérés.
- Les politiques de filtrage web doivent s'appliquer de manière cohérente que l'utilisateur soit sur le réseau d'entreprise, le Wi-Fi domestique, le point d'accès mobile ou un réseau public.
- La tunnellisation fractionnée (VPN) ne doit pas contourner le filtrage web ; le trafic web doit être acheminé via la solution de filtrage quelle que soit la configuration VPN.

### BYOD (appareils personnels)

- Le filtrage DNS est le niveau de base minimum pour les appareils BYOD accédant aux ressources d'entreprise.
- L'inspection TLS ne doit **pas** être effectuée sur les appareils personnels (contraintes légales et de protection de la vie privée).
- Un navigateur géré ou un conteneur d'espace de travail sécurisé (p. ex. Microsoft Edge for Business, VMware Workspace ONE) devrait être envisagé pour l'accès BYOD aux applications web d'entreprise.
- Des politiques de filtrage moins intrusives et distinctes doivent s'appliquer aux appareils BYOD par rapport aux appareils gérés par l'entreprise.

---

## Vie privée des employés et filtrage web

### Exigences légales

Le filtrage web qui traite les données de navigation des employés doit être conforme au droit suisse du travail :

- **OLT 3 art. 26** : Les systèmes de filtrage web ne doivent pas être utilisés principalement pour surveiller le comportement des employés. Leur objectif est la sécurité (prévention des logiciels malveillants, prévention des fuites de données, application des politiques).
- **CO art. 328b** : Le traitement des données de navigation web des employés doit être proportionnel et limité aux objectifs de sécurité.
- **nLPD** : La licéité, la proportionnalité, la limitation de la finalité et la transparence s'appliquent à tout traitement des données de navigation web.

### Mesures de protection de la vie privée

- **Transparence** : Les employés doivent être informés que le filtrage web est en place, quelles catégories sont filtrées et que l'accès aux sites bloqués est journalisé. Ces informations doivent être incluses dans la politique d'utilisation acceptable et la documentation de l'emploi.
- **Surveillance non personnalisée par défaut** : Les journaux de filtrage web doivent être révisés de manière agrégée pour la surveillance sécuritaire (p. ex. total des requêtes bloquées par catégorie, principaux domaines bloqués). L'activité de navigation individuelle des utilisateurs ne doit pas être révisée sauf si :
  - (a) Une alerte de sécurité indique un incident potentiel ou une violation de politique, et
  - (b) L'investigation est documentée avec justification.
- **Limitation de la finalité** : Les données de filtrage web ne doivent pas être utilisées pour l'évaluation des performances RH, les mesures disciplinaires pour des raisons non sécuritaires, ou le profilage comportemental général.
- **Minimisation des données** : Les journaux de filtrage web doivent être conservés uniquement aussi longtemps que nécessaire à des fins de sécurité (selon le calendrier de conservation des journaux dans la Politique de journalisation, A.8.15).
- **AIPD** : Si le filtrage web inclut l'inspection TLS ou une journalisation détaillée au niveau utilisateur à grande échelle, une Analyse d'impact relative à la protection des données selon la nLPD art. 22 peut être requise.

---

## Formation et sensibilisation

- Tous les employés doivent être formés sur :
  - La politique de filtrage web de l'organisation et l'utilisation web acceptable.
  - Comment reconnaître les avertissements de sécurité du navigateur (erreurs de certificat, indicateurs de phishing).
  - Comment signaler les sites web suspects malveillants à la Sécurité de l'information.
  - Le processus de demande d'exception pour accéder aux sites bloqués.
- La formation doit être incluse dans le programme annuel de sensibilisation à la sécurité de l'information.
- Les administrateurs système responsables de la maintenance du filtrage web doivent recevoir une formation spécifique à la plateforme.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation des décisions de filtrage par catégorie ; approbation des exceptions à risque élevé ; supervision de l'efficacité du filtrage web |
| **Opérations IT / Équipe réseau** | Déploiement, configuration et maintenance de la plateforme de filtrage web ; mise en œuvre des exceptions ; gestion de la capacité ; gestion des certificats d'inspection TLS |
| **Sécurité de l'information** | Intégration du renseignement sur les menaces ; mises à jour des listes de blocage ; évaluation des risques des exceptions ; révision trimestrielle des exceptions ; analyse des journaux de filtrage web |
| **Responsables hiérarchiques** | Révision de la justification métier pour les demandes d'exception |
| **Tout le personnel** | Se conformer à la politique de filtrage web ; signaler les sites web suspects malveillants ; utiliser le processus de demande d'exception pour les besoins métier légitimes |
| **Conseiller à la protection des données** | Évaluation AIPD pour l'inspection TLS ; orientation sur les mesures de protection de la vie privée des employés |

### Révision de l'accès administratif (SOC 2 : CC6.1)

L'accès administratif à la plateforme de filtrage web doit être :

- Restreint au personnel des Opérations IT et de la Sécurité de l'information avec un besoin documenté.
- Révisé trimestriellement pour s'assurer que seul le personnel autorisé conserve l'accès.
- Protégé par AMF et des contrôles de gestion des accès à privilèges.
- Journalisé — toutes les actions administratives (changements de règles, modifications de configuration, ajouts d'exceptions) doivent être auditables.
- Révoqué dans les 24 heures lorsque le personnel change de rôle ou quitte l'organisation.

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Configuration de la plateforme de filtrage web** (catégories bloquées/autorisées, paramètres d'inspection TLS, configuration du filtrage DNS) | Opérations IT | *Documentée ; révisée semestriellement et après les modifications de politique* |
| 2 | **Relevés de mise à jour des listes de blocage** (sources de renseignement sur les menaces, fréquence de mise à jour, ajouts manuels issus des investigations d'incidents) | Sécurité de l'information | *Mises à jour automatiques continues ; ajouts manuels journalisés avec date et source* |
| 3 | **Registre des exceptions** (exceptions actives avec justification, approbateur, expiration et date de révision) | Sécurité de l'information | *Maintenu en continu ; révisé trimestriellement ; total rapporté au RSSI trimestriellement* |
| 4 | **Résumé des journaux de filtrage web** (statistiques agrégées : total des requêtes, requêtes bloquées par catégorie, principaux domaines bloqués) | Sécurité de l'information | *Résumé mensuel ; conservé 12 mois* |
| 5 | **Liste d'exclusion de la vie privée pour l'inspection TLS** (catégories contournant l'inspection) | Opérations IT | *Documentée ; révisée annuellement* |
| 6 | **Relevés de notification des employés** (accusé de réception de la politique d'utilisation acceptable incluant la divulgation du filtrage web) | RH / Sécurité de l'information | *Mis à jour par modification de politique ; reconnaissance suivie annuellement* |
| 7 | **Couverture de filtrage des travailleurs à distance** (pourcentage des terminaux distants gérés avec agent de filtrage actif) | Opérations IT | *Trimestriel ; cible : 100 % des appareils distants gérés* |
| 8 | **Relevés d'AIPD** (si l'inspection TLS ou la journalisation détaillée au niveau utilisateur est mise en œuvre) | Conseiller à la protection des données | *Réalisée avant le déploiement ; révisée annuellement* |
| 9 | **Rapports d'OLS de la plateforme de filtrage** — disponibilité, latence et indicateurs de résolution des incidents (SOC 2 : A1.1) | Opérations IT | *Mensuel ; conservé 12 mois* |
| 10 | **Relevés de changements de règles de filtrage** — demandes de changement, évaluations des risques, approbations, dates de mise en œuvre (SOC 2 : CC8.1) | Opérations IT / Sécurité de l'information | *Par changement ; conservé 12 mois* |
| 11 | **Relevés d'évaluation des risques fournisseurs** — évaluations des fournisseurs SWG/DNS tiers, conformité SLA, rapports SOC 2/ISO 27001 (SOC 2 : CC9.2) | Sécurité de l'information / Achats | *Annuellement ; conservé contrat actif + 2 ans* |
| 12 | **Relevés de révision des accès administratifs** — liste des administrateurs de la plateforme de filtrage, résultats des révisions, modifications des accès (SOC 2 : CC6.1) | Opérations IT / Sécurité de l'information | *Trimestriel ; conservé 12 mois* |
| 13 | **Résultats des tests d'efficacité du filtrage** — URL de test, résultats des tentatives de contournement, mesures du taux de détection (SOC 2 : CC4.1) | Sécurité de l'information | *Semestriel ; conservé 12 mois* |
| 14 | **Reporting de gestion** — résumé mensuel des indicateurs, analyse trimestrielle des tendances, révision annuelle de l'efficacité (SOC 2 : CC4.2) | RSSI / Sécurité de l'information | *Mensuel/trimestriel/annuel selon les spécifications* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par des révisions de configuration du filtrage web, des audits du registre des exceptions, une analyse des taux de blocage, des contrôles de couverture des appareils distants, des audits internes et externes, et des retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée conformément au Processus d'exception et de dérogation défini ci-dessus. Les exceptions à la politique globale de filtrage web (p. ex. systèmes ne pouvant pas être filtrés) doivent être approuvées par le RSSI avec acceptation documentée du risque et mesures compensatoires.

## Non-conformité

Un employé reconnu avoir violé la présente politique — y compris en tentant de contourner les contrôles de filtrage web (p. ex. en utilisant un VPN personnel, des outils d'évitement de proxy ou des résolveurs DNS non autorisés) — peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Tests et validation (SOC 2 : CC4.1)

L'efficacité des contrôles de filtrage web doit être testée régulièrement :

| Test | Fréquence | Méthode | Responsable |
|------|-----------|---------|-------------|
| **Vérification du blocage** | Mensuel | Tenter d'accéder à des URL connues bloquées depuis des comptes de test ; vérifier que la page de blocage s'affiche correctement | Sécurité de l'information |
| **Tests de contournement** | Semestriel | Tenter de contourner le filtrage en utilisant des techniques d'évasion courantes (DoH vers des résolveurs non approuvés, VPN, proxy) | Sécurité de l'information |
| **Taux de détection des logiciels malveillants** | Trimestriel | Soumettre des URL malveillantes connues (provenant de flux de test) via la solution de filtrage ; mesurer le taux de détection | Sécurité de l'information |
| **Vérification de l'inspection TLS** | Trimestriel | Vérifier que l'inspection TLS est active sur le trafic attendu ; confirmer que les exclusions de confidentialité fonctionnent correctement | Opérations IT |
| **Couverture des travailleurs à distance** | Trimestriel | Vérifier que l'agent de filtrage est actif sur un échantillon de terminaux distants gérés | Opérations IT |

Les résultats des tests doivent être documentés et les actions de remédiation suivies pour toute faiblesse identifiée.

## Indicateurs et reporting de gestion (SOC 2 : CC4.2)

Les indicateurs suivants doivent être rapportés :

| Indicateur | Cible | Reporting |
|-----------|-------|-----------|
| Disponibilité de la plateforme de filtrage | ≥ 99,9 % de disponibilité | Mensuel aux Opérations IT |
| Taux de blocage des logiciels malveillants/phishing | ≥ 99 % des menaces connues bloquées | Trimestriel au RSSI |
| Délai de traitement des demandes d'exception | ≤ 2 jours ouvrables de la demande à la décision | Mensuel au RSSI |
| Nombre d'exceptions actives | En baisse ou stable | Trimestriel au RSSI |
| Couverture de filtrage des travailleurs à distance | 100 % des terminaux distants gérés | Trimestriel au RSSI |
| URL de phishing signalées par les employés traitées | Dans le délai SLA de 4 heures | Mensuel à la Sécurité de l'information |

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions du paysage des menaces web, les capacités technologiques de filtrage, les exigences réglementaires, les retours des employés sur l'accès légitime bloqué, et les taux de faux positifs/négatifs.

---

# Domaines de la norme ISO 27001 couverts

Politique de filtrage web — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| | 5.37 Procédures opérationnelles documentées |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.23 Filtrage web** |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles ; art. 6 — Proportionnalité |
| CO suisse (Code des obligations) | Art. 328b — Limitations du traitement des données des employés |
| OLT 3 suisse (Ordonnance 3 relative à la loi sur le travail) | Art. 26 — Interdiction de la surveillance des comportements |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.23 |
| ISO/IEC 27002:2022 | Section 8.23 — Lignes directrices de mise en œuvre |
| NIST SP 800-53 Rév. 5 | AC-4 (Application des flux d'informations), SC-7 (Protection des frontières), SC-7(8) (Acheminer le trafic via un proxy), SI-3 (Protection contre le code malveillant) |
| NIST CSF 2.0 | PR.DS (Sécurité des données), PR.IR (Résilience de l'infrastructure), DE.CM (Surveillance continue) |
| CIS Controls v8 | Contrôle 9.2 (Services de filtrage DNS), Contrôle 9.3 (Filtres URL réseau) |

<!-- QA_VERIFIED: 2026-03-29 -->
