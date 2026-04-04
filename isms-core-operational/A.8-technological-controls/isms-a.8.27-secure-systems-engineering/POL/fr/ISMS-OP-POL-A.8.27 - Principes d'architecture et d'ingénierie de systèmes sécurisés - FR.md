<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.27-FR:operational:OP-POL:a.8.27 -->
**ISMS-OP-POL-A.8.27 — Principes d'architecture et d'ingénierie de systèmes sécurisés**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Principes d'architecture et d'ingénierie de systèmes sécurisés |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.27 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
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

- ISO/IEC 27001:2022 Contrôle A.8.27 — Principes d'architecture et d'ingénierie de systèmes sécurisés
- ISO/IEC 27002:2022 Section 8.27 — Conseils de mise en œuvre
- NIST SP 800-160 Vol. 1 Rév. 1 — Engineering Trustworthy Secure Systems
- NIST SP 800-207 — Zero Trust Architecture
- NIST SP 800-53 Rév. 5 SA-8 — Security and Privacy Engineering Principles
- CIS Controls v8 — Mesures de protection 4.1, 16.1–16.14 (Application Software Security)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec l'architecture de systèmes sécurisés |
|----------|----------------------------------------------------|
| A.5.8 Sécurité de l'information dans la gestion de projets | Exigences d'architecture de sécurité intégrées dans la gouvernance des projets |
| A.8.25 Cycle de développement sécurisé | Les principes d'architecture orientent le cadre du processus de développement |
| A.8.26 Exigences de sécurité des applications | Les exigences de sécurité sont dérivées des principes d'architecture |
| A.8.28 Codage sécurisé | Les normes de codage mettent en œuvre les principes d'architecture au niveau du code |
| A.8.29 Tests de sécurité dans le développement et l'acceptation | Les tests valident la correcte implémentation des principes d'architecture |
| A.8.31 Séparation des environnements de développement, de test et de production | Le cloisonnement des environnements est un principe fondamental d'architecture |
| A.8.9 Gestion de la configuration | Les référentiels de configuration appliquent les normes d'architecture sécurisée |
| A.8.20–22 Sécurité des réseaux | L'architecture réseau met en œuvre la segmentation et la défense en profondeur |
| A.8.2–3–5 Authentification et accès privilégié | L'architecture d'authentification met en œuvre les principes Zéro Confiance |
| A.5.19–23 Fournisseurs et services cloud | Les systèmes tiers sont soumis à une revue d'architecture |

**Politiques internes associées** :

- Politique de cycle de développement sécurisé
- Politique de sécurité des réseaux
- Politique d'authentification et d'accès privilégié
- Politique de gestion de la configuration
- Politique de sécurité de l'information dans la gestion de projets
- Politique d'utilisation de la cryptographie

---

# Politique relative aux principes d'architecture et d'ingénierie de systèmes sécurisés

## Objet

La présente politique a pour objet d'établir les règles et principes pour l'ingénierie de systèmes d'information sécurisés, en garantissant que la sécurité est conçue dans l'architecture des systèmes dès leur conception plutôt qu'ajoutée après le déploiement. Elle définit les principes fondamentaux d'ingénierie sécurisée qui s'appliquent à toutes les activités de développement, d'acquisition, d'intégration et de modification de systèmes.

Cette politique soutient la nLPD (revDSG) suisse en mettant en œuvre la protection des données dès la conception et par défaut (art. 7) et des mesures techniques et organisationnelles proportionnées aux risques (art. 8). La nLPD exige que les développeurs intègrent la protection et le respect de la vie privée des personnes concernées dans la structure même des produits et services traitant des données personnelles, et que le niveau de sécurité le plus élevé soit activé par défaut sans intervention de l'utilisateur. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également (art. 25 — protection des données dès la conception et par défaut ; art. 32 — sécurité du traitement).

## Champ d'application

Tous les systèmes d'information conçus, développés, acquis, intégrés, exploités et maintenus par l'organisation, notamment :

- Les applications, API et services développés en interne.
- L'architecture des infrastructures et des plateformes (sur site et cloud).
- Les systèmes développés ou acquis auprès de tiers intégrés dans l'environnement de l'organisation.
- Les services cloud, les plateformes SaaS et les services gérés pour lesquels l'organisation définit ou influence l'architecture.
- Les technologies opérationnelles (OT) et les systèmes de contrôle industriel (ICS), le cas échéant.

Tous les employés, sous-traitants et utilisateurs tiers impliqués dans la conception, l'architecture, le développement et l'ingénierie des systèmes.

**Hors périmètre** : Les postes de travail des utilisateurs finaux gérés dans le cadre de la Politique de sécurité des postes de travail (A.8.1-7-18-19), sauf s'ils font partie d'une architecture système soumise à revue. L'infrastructure physique est régie par la Politique de sécurité physique (A.7.x).

## Principe

Des principes pour l'ingénierie de systèmes sécurisés doivent être établis, documentés, maintenus et appliqués à toutes les activités de développement de systèmes d'information. La sécurité est traitée comme une propriété fondamentale de la conception des systèmes — non comme un accessoire ajouté après coup.

Toutes les décisions d'architecture et d'ingénierie sont fondées sur les risques, tenant compte de la valeur et de la classification des informations traitées, du paysage des menaces propre au système, des exigences réglementaires et de l'appétence au risque de l'organisation.

Lorsque l'organisation ne dispose pas de ressources dédiées à l'architecture de sécurité — situation courante dans les petites et moyennes organisations — le RSSI assume la fonction d'architecte de sécurité, et une revue par des spécialistes externes est sollicitée pour les systèmes à risque élevé.

---

## Principes d'ingénierie sécurisée

L'organisation établit, documente et maintient un ensemble de principes d'ingénierie sécurisée applicables à toutes les activités de développement et d'acquisition de systèmes. Ces principes sont révisés annuellement et mis à jour pour tenir compte des évolutions du paysage des menaces, des normes technologiques et des exigences réglementaires.

### Principe 1 : Sécurité dès la conception

La sécurité est intégrée dès les premières étapes de la conception du système :

- Les exigences de sécurité sont identifiées lors du développement du concept initial, en parallèle des exigences fonctionnelles.
- L'architecture de sécurité est définie avant le début de la conception détaillée.
- Les contrôles de sécurité sont conçus en tant que composants intégraux du système, et non comme des ajouts après la construction des fonctionnalités principales.
- Les compromis de sécurité sont explicitement documentés, avec l'acceptation du risque approuvée par le RSSI avant de procéder.

### Principe 2 : Sécurité par défaut

Les systèmes sont sécurisés dans leur configuration par défaut :

- Les configurations par défaut mettent en œuvre les paramètres de sécurité les plus restrictifs appropriés à la finalité prévue du système.
- Les utilisateurs ne sont pas obligés d'agir pour sécuriser le système — la sécurité est active dès la première utilisation.
- Les fonctionnalités de sécurité optionnelles sont activées par défaut sauf justification métier documentée pour les désactiver.
- Le principe du refus par défaut s'applique aux contrôles d'accès, aux communications réseau et aux capacités du système.
- Les interfaces d'administration sont désactivées ou restreintes par défaut.
- Les fonctionnalités des applications nécessitant des privilèges élevés sont activées explicitement, pas par défaut (ex. journalisation de débogage, administration à distance).

**Protection de la vie privée par défaut (art. 7 nLPD)** :

- Les paramètres par défaut minimisent la collecte de données personnelles (minimisation des données).
- Les fonctionnalités améliorant la protection de la vie privée sont activées par défaut (ex. anonymisation des données, application de la limitation des finalités).
- Les mécanismes de consentement des utilisateurs sont par défaut en opt-in, et non en opt-out.
- La conservation des données est par défaut limitée à la durée la plus courte sauf justification métier imposant une conservation plus longue.

### Principe 3 : Défense en profondeur

Plusieurs couches de contrôles de sécurité sont mises en œuvre de sorte qu'aucun point de défaillance unique ne résulte en une compromission totale :

- Aucun contrôle unique ne constitue l'unique protection des actifs critiques.
- Les contrôles sont mis en œuvre à plusieurs couches d'architecture : réseau, plateforme, application et données.
- La défaillance d'une couche de contrôle n'entraîne pas la compromission complète du système.
- Les contrôles par couches sont complémentaires — chaque couche traite différents vecteurs d'attaque.

**Couches de défense en profondeur** :

| Couche | Contrôles de sécurité |
|--------|----------------------|
| **Périmètre** | Pare-feux, pare-feux applicatifs web (WAF), protection DDoS, passerelles sécurisées |
| **Réseau** | Segmentation, contrôle d'accès réseau, IDS/IPS, communications internes chiffrées |
| **Plateforme** | Configurations renforcées, gestion des correctifs, protection des postes, démarrage sécurisé |
| **Application** | Validation des entrées, encodage des sorties, authentification, autorisation, gestion des sessions |
| **Données** | Chiffrement au repos et en transit, contrôles d'accès, masquage des données, prévention des fuites |
| **Identité** | Authentification multifacteur, gestion des accès privilégiés, gouvernance des identités |
| **Surveillance** | Journalisation centralisée, analyse comportementale, détection des menaces, réponse aux incidents |

### Principe 4 : Moindre privilège

Tous les utilisateurs, processus et systèmes opèrent avec les privilèges minimaux nécessaires à l'exercice de leur fonction autorisée :

- Les droits d'accès sont limités à ce qui est requis pour la tâche spécifique.
- Les privilèges élevés sont accordés uniquement lorsque nécessaire et révoqués lorsqu'ils ne sont plus requis.
- Les comptes de service disposent d'autorisations étroitement délimitées, limitées à des ressources et opérations spécifiques (pas d'accès complet à la base de données, pas d'administrateur de domaine).
- L'accès administratif est séparé de l'accès opérationnel courant.

### Principe 5 : Fonctionnalité minimale

Les systèmes ne fournissent que les capacités nécessaires à leur finalité :

- Les services, protocoles et fonctionnalités inutiles sont désactivés ou supprimés.
- La surface d'attaque est minimisée par la réduction des fonctions.
- Les ports, interfaces et capacités inutilisés sont désactivés.
- Le contenu exemple par défaut, les pages de test et les modules inutilisés sont supprimés avant le déploiement.

### Principe 6 : Échec en mode sécurisé

Les systèmes tombent en panne dans un état sécurisé qui n'expose pas de données ou de fonctionnalités sensibles :

- Les défaillances du système ont pour défaut de refuser l'accès plutôt que de l'accorder.
- Les conditions d'erreur ne révèlent pas d'informations sensibles (traces de pile, chemins internes, détails de base de données, numéros de version).
- La récupération après une défaillance nécessite une nouvelle authentification et une nouvelle autorisation.
- La dégradation gracieuse maintient les contrôles de sécurité même lorsque les performances sont réduites.
- Les événements de défaillance sont journalisés pour la surveillance de la sécurité et l'investigation des incidents.

**Exemples d'échec en mode sécurisé** :

Correct (échec sécurisé) :

- Défaillance de la connexion à la base de données : L'application retourne une erreur générique, refuse l'accès.
- Service d'authentification indisponible : Le système refuse la connexion, ne contourne pas l'authentification.
- Erreur de traitement des règles de pare-feu : Refus par défaut, blocage du trafic.
- Clé de chiffrement indisponible : Accès aux données refusé jusqu'au rétablissement de la clé.

Incorrect (échec non sécurisé — à éviter) :

- Défaillance de la connexion à la base de données : L'application accorde l'accès en supposant que les identifiants sont valides.
- Service d'authentification indisponible : Le système autorise la connexion avec des identifiants en cache sans vérification d'expiration.
- Erreur de traitement des règles de pare-feu : Ouverture par défaut, autorisation de tout le trafic.
- Clé de chiffrement indisponible : Données servies en clair.

### Principe 7 : Réduction de la complexité

La conception des systèmes privilégie la simplicité — les systèmes complexes sont plus difficiles à sécuriser, vérifier et maintenir :

- Les composants disposent d'interfaces bien définies avec des frontières de sécurité claires.
- Les systèmes sont conçus avec des modules indépendants et faiblement couplés pouvant être sécurisés, mis à jour et validés indépendamment.
- Les ressources partagées sont minimisées pour réduire la surface d'attaque et prévenir les flux d'informations non autorisés entre composants.
- Les dépendances entre composants sont bien définies et documentées.

**Gestion de la complexité** :

La complexité est gérée par :

- **Conception modulaire** : Composants avec une finalité unique et bien définie.
- **Limitation des interfaces** : Interfaces externes limitées au strict nécessaire (chaque intégration externe est documentée et justifiée).
- **Suivi des dépendances** : Maintenir une cartographie des dépendances pour les systèmes critiques ; cible de moins de 10 dépendances externes pour les systèmes de niveau 1.
- **Complexité cyclomatique** : Métriques de complexité du code suivies lors du développement (cible : moins de 10 par fonction pour le code à caractère sécuritaire critique).

**Déclencheurs de revue de complexité** :

- Le système nécessite plus de 5 mécanismes d'authentification différents.
- Plus de 15 intégrations de systèmes externes.
- Ressources partagées entre frontières de confiance sans isolation.
- L'équipe de développement ne peut expliquer le flux de données en moins de 15 minutes.

---

## Principes d'architecture Zéro Confiance

L'organisation adopte les principes Zéro Confiance pour tous les nouveaux systèmes et les applique progressivement aux systèmes existants :

**Ne jamais faire confiance, toujours vérifier** :

- Aucune confiance implicite n'est accordée en fonction de l'emplacement réseau, de la propriété de l'appareil ou d'une authentification antérieure.
- Chaque demande d'accès est authentifiée et autorisée quelle que soit sa source — interne ou externe.
- La confiance est évaluée en continu et non présumée après une vérification initiale.

**Partir du principe d'une compromission** :

- Les systèmes sont conçus en supposant que des adversaires ont peut-être déjà accès aux réseaux internes.
- Le trafic réseau interne est traité comme potentiellement hostile.
- Le déplacement latéral est restreint par la segmentation et les contrôles d'accès.
- Les capacités de détection supposent que les contrôles de périmètre ont pu échouer.
- La détection et réponse des postes de travail (EDR) est déployée sur tous les appareils gérés pour détecter les activités post-compromission.

**Vérifier explicitement** :

- Les décisions d'accès prennent en compte toutes les données disponibles : identité de l'utilisateur, état de l'appareil, sensibilité des données, contexte d'accès (localisation, heure, comportement) et indicateurs d'anomalies des demandes.
- Les décisions d'accès sont journalisées à des fins d'audit et d'investigation.

**Accès au moindre privilège** :

- Accès juste-à-temps (JIT) pour les privilèges élevés — accorder l'accès uniquement lorsque nécessaire, révoquer automatiquement à la fin de la tâche.
- Accès juste-suffisant (JEA) pour tous les octrois d'accès — pas d'autorisations étendues permanentes.
- Politiques d'accès conditionnel basées sur les risques appliquées via le fournisseur d'identité.

**Approche de mise en œuvre Zéro Confiance** :

| Phase | Activités | Calendrier cible |
|-------|-----------|-----------------|
| **Phase 1 : Fondation** | Contrôle d'accès centré sur l'identité, AMF pour tous les utilisateurs, vérification de l'état des appareils | Dans les 12 mois suivant l'approbation de la politique |
| **Phase 2 : Réseau** | Micro-segmentation pour les systèmes critiques, communications internes chiffrées, contrôle d'accès réseau | Dans les 24 mois |
| **Phase 3 : Continu** | Évaluation continue des accès, analyse comportementale, réponse automatisée aux anomalies | Dans les 36 mois |

**Calendriers de mise en œuvre Zéro Confiance** : Les calendriers indiqués s'appliquent à une organisation de taille moyenne (50–200 employés) avec une dette technique modérée. À adapter selon :

- **Petites organisations (<50 employés)** : Les délais peuvent être réduits de 50 % avec une infrastructure native cloud.
- **Grandes organisations (>200 employés)** : Les délais peuvent être allongés de 50 % en raison des systèmes hérités et de la complexité organisationnelle.
- **Niveau de dette technique** : Les organisations disposant d'une infrastructure sur site importante nécessitent des délais de Phase 2 plus longs.

Les progrès sont évalués annuellement par rapport à la feuille de route spécifique à l'organisation, et non par rapport à des dates calendaires absolues.

Il n'est pas attendu que l'organisation atteigne une maturité Zéro Confiance complète immédiatement. Chaque phase est planifiée, dotée en ressources et révisée. Les progrès sont communiqués annuellement à la direction générale.

---

## Documentation de l'architecture de sécurité

Tous les systèmes classés à risque élevé ou moyen disposent d'une architecture de sécurité documentée. Les systèmes à risque faible disposent au minimum d'une liste de contrôle de sécurité complétée.

### Exigences de documentation

**Systèmes à risque élevé** :

| Document | Contenu | Responsable |
|----------|---------|-------------|
| **Document d'architecture de sécurité (DAS)** | Vue d'ensemble du système, frontières de confiance, flux de données, contrôles de sécurité par couche, points d'intégration, contexte des menaces | RSSI / Architecte de sécurité |
| **Modèle de menaces** | Menaces identifiées, vecteurs d'attaque, évaluations des risques, atténuations, risques résiduels | RSSI / Architecte de sécurité |
| **Matrice de traçabilité des exigences de sécurité** | Exigences de sécurité associées aux éléments de conception et aux cas de test | Propriétaire du système |
| **Enregistrements de décisions d'architecture (EDA)** | Décisions de conception liées à la sécurité avec justification et alternatives examinées | Propriétaire du système / Responsable développement |

**Systèmes à risque moyen** :

| Document | Contenu | Responsable |
|----------|---------|-------------|
| **Résumé d'architecture de sécurité** | DAS abrégé couvrant les frontières de confiance, les flux de données et les contrôles clés | Propriétaire du système |
| **Évaluation des menaces** | Identification allégée des menaces et planification des atténuations | RSSI |

**Systèmes à risque faible** :

- Liste de contrôle de conception sécurisée (complétée et validée par le RSSI ou son délégué).

**Stockage de la documentation** : La documentation d'architecture de sécurité est stockée dans [Outil d'architecture / Confluence / SharePoint] avec accès restreint aux : RSSI, responsable développement, propriétaire du système et personnels disposant d'un besoin d'en connaître documenté approuvé par le RSSI. La documentation est versionnée.

**Actualité de la documentation** : La documentation d'architecture de sécurité est révisée et mise à jour : lors de changements significatifs apportés au système, lors de l'identification de nouvelles menaces affectant le système, et au moins une fois par an pour les systèmes à risque élevé.

---

## Processus de revue d'architecture

Tous les nouveaux systèmes et les changements significatifs apportés aux systèmes existants font l'objet d'une revue d'architecture de sécurité avant mise en œuvre.

### Déclencheurs de revue

Une revue d'architecture de sécurité est requise lorsque :

- Un nouveau système est développé ou acquis.
- Une mise à niveau majeure de version ou une migration de plateforme est effectuée.
- Des changements d'architecture affectent les frontières de sécurité ou les zones de confiance.
- De nouveaux services externes ou flux de données sont intégrés.
- Les mécanismes d'authentification ou d'autorisation sont modifiés.
- La classification des données traitées augmente.
- Un incident de sécurité révèle des faiblesses architecturales.

### Processus de revue

| Étape | Activité | Responsable |
|-------|----------|-------------|
| 1. **Initiation** | Le propriétaire du système soumet une demande de revue d'architecture avec la documentation du système | Propriétaire du système |
| 2. **Modélisation des menaces** | Conduite de la modélisation des menaces selon la méthodologie STRIDE (obligatoire pour le risque élevé ; recommandé pour le risque moyen) | RSSI / Architecte de sécurité |
| 3. **Validation des exigences** | Vérification que les exigences de sécurité sont complètes et alignées avec les exigences métier | RSSI |
| 4. **Revue des schémas** | Évaluation de l'architecture par rapport aux schémas sécurisés approuvés ; identification des écarts | RSSI / Architecte de sécurité |
| 5. **Validation de la défense en profondeur** | Vérification que les contrôles sont mis en œuvre sur toutes les couches d'architecture pertinentes | RSSI |
| 6. **Évaluation des risques** | Documentation des risques résiduels et des plans de traitement pour les lacunes identifiées | RSSI / Propriétaire du système |
| 7. **Approbation** | Le RSSI approuve ou retourne avec les modifications requises | RSSI |

**Critères d'approbation** : L'architecture ne peut pas être approuvée si :

- La modélisation des menaces n'a pas été réalisée (systèmes à risque élevé).
- Des risques Critiques ou Élevés existent sans plan de traitement.
- La défense en profondeur est absente pour les systèmes traitant des données Confidentielles ou Restreintes.
- Les écarts par rapport aux schémas d'architecture approuvés ne disposent pas de contrôles compensatoires et d'une approbation d'exception du RSSI.

**SLA de revue** :

- Systèmes à risque élevé (avec modèle de menaces complet) : 15 jours ouvrés à compter de la soumission complète.
- Systèmes à risque moyen (revue sommaire) : 10 jours ouvrés.
- Systèmes à risque faible (revue par liste de contrôle) : 5 jours ouvrés.

Les soumissions incomplètes sont retournées dans les 3 jours ouvrés avec identification des lacunes spécifiques. Le délai repart à zéro lors de la soumission d'une documentation complète.

### Liste de contrôle de revue d'architecture (systèmes à risque moyen et élevé)

**Identité et accès** :

- [ ] Mécanisme d'authentification documenté (SSO, AMF, clés API).
- [ ] Modèle d'autorisation défini (RBAC, ABAC).
- [ ] Séparation des accès privilégiés mise en œuvre.
- [ ] Autorisations des comptes de service minimisées.

**Protection des données** :

- [ ] Classification des données identifiée pour toutes les données traitées.
- [ ] Chiffrement au repos mis en œuvre pour les données Confidentielles/Restreintes.
- [ ] Chiffrement en transit (TLS 1.2+) pour toutes les communications réseau.
- [ ] Mécanismes de conservation et de suppression des données définis.

**Sécurité des réseaux** :

- [ ] Segmentation réseau appropriée au niveau du système.
- [ ] Règles de pare-feu entrantes/sortantes documentées et justifiées.
- [ ] Passerelle API ou WAF pour les applications accessibles depuis Internet.
- [ ] Communications internes chiffrées lors du traitement de données sensibles.

**Défense en profondeur** :

- [ ] Au moins 3 couches de contrôle vérifiées (réseau, plateforme, application, données).
- [ ] Analyse des points de défaillance unique réalisée.
- [ ] Contrôles complémentaires confirmés (différents vecteurs d'attaque adressés).

**Surveillance et journalisation** :

- [ ] Journalisation des événements de sécurité configurée.
- [ ] Transfert des journaux vers la plateforme SIEM/journalisation centrale.
- [ ] Règles d'alerte définies pour les événements critiques.
- [ ] Conservation des journaux conforme aux exigences de la politique.

**Résilience** :

- [ ] Procédures de sauvegarde et de récupération documentées.
- [ ] RPO/RTO définis et validés.
- [ ] Plan de reprise après sinistre existant (systèmes de niveau 1).
- [ ] Redondance mise en œuvre pour les composants critiques.

**Modélisation des menaces** (risque élevé uniquement) :

- [ ] Analyse STRIDE réalisée.
- [ ] Vecteurs d'attaque documentés.
- [ ] Atténuations associées à chaque menace.
- [ ] Risques résiduels acceptés par le RSSI.

**Conformité** :

- [ ] Exigences nLPD/RGPD évaluées (si traitement de données personnelles).
- [ ] Réglementations sectorielles spécifiques traitées (si applicable).
- [ ] Protection des données dès la conception et par défaut démontrée.

### Revue externe de l'architecture de sécurité

L'organisation sollicite des spécialistes externes en architecture de sécurité lorsque :

| Déclencheur | Justification |
|-------------|---------------|
| **Nouveau système à risque élevé** développé en interne sans expérience préalable en architecture sécurisée | Validation indépendante du modèle de menaces et des décisions de conception |
| **Conception de système cryptographique** (implémentations personnalisées, gestion des clés) | Expertise spécialisée en cryptographie requise |
| **Système de traitement des paiements** | Conformité PCI DSS et exigences de sécurité spécialisées |
| **Mise en œuvre initiale de l'architecture Zéro Confiance** | Architecture complexe nécessitant une expertise spécialisée Zéro Confiance |
| **Incident significatif** révélant une faiblesse architecturale | Analyse indépendante des causes racines et conseils de remédiation |
| **Intégration suite à une fusion/acquisition** | Évaluation tierce de la posture de sécurité de l'architecture combinée |
| **Constatation d'audit réglementaire** liée à l'architecture | Validation indépendante de la conception de remédiation |

Les examinateurs externes sont sélectionnés sur la base de : certifications sectorielles pertinentes (CISSP, CCSP ou équivalent), expérience avérée avec des architectures similaires, et indépendance vis-à-vis des fournisseurs d'implémentation.

### Modélisation des menaces

Lorsque la modélisation des menaces est requise, la méthodologie STRIDE est utilisée comme approche principale :

| Catégorie STRIDE | Type de menace | Exemple |
|-----------------|----------------|---------|
| **Usurpation** (Spoofing) | Usurpation d'identité | Vol d'identifiants, détournement de session |
| **Falsification** (Tampering) | Modification non autorisée | Manipulation de données, changement de configuration |
| **Répudiation** (Repudiation) | Déni d'actions | Absence de pistes d'audit |
| **Divulgation d'informations** (Information Disclosure) | Exposition de données | Données non chiffrées, messages d'erreur verbeux |
| **Déni de service** (Denial of Service) | Interruption de disponibilité | Épuisement des ressources, saturation |
| **Élévation de privilèges** (Elevation of Privilege) | Obtention d'accès non autorisé | Escalade de privilèges, attaques par injection |

Les modèles de menaces sont conservés :

- **Systèmes actifs** : Durée de vie du système plus 3 ans après décommissionnement.
- **Incidents majeurs** : Les modèles de menaces pour les systèmes impliqués dans des incidents de sécurité sont conservés de façon permanente (minimum 7 ans).

Les modèles de menaces sont révisés et mis à jour : à chaque version majeure, lors de changements architecturaux significatifs du système, lors de l'identification de nouveaux renseignements sur les menaces pertinents pour le système, et au moins une fois par an pour les systèmes à risque élevé.

---

## Critères de sécurité pour la sélection des technologies

Lors de la sélection de nouvelles technologies, plateformes, frameworks ou composants tiers, la sécurité est un critère de sélection d'égale importance par rapport aux exigences fonctionnelles.

### Critères de sélection

| Critère | Exigence |
|---------|----------|
| **Posture de sécurité du fournisseur** | Le fournisseur fournit des preuves de pratiques de développement sécurisé (ex. certification SOC 2, ISO 27001 ou équivalent) |
| **Historique des vulnérabilités** | Aucun schéma de vulnérabilités critiques non résolues ; historique de publication de correctifs en temps opportun |
| **Paramètres par défaut sécurisés** | La technologie est livrée avec une configuration par défaut sécurisée ; ne nécessite pas de renforcement intensif pour atteindre un état acceptable |
| **Support du chiffrement** | Prend en charge les normes de chiffrement actuelles (TLS 1.2 minimum, TLS 1.3 préféré ; AES-256 pour les données au repos) |
| **Intégration de l'authentification** | Prend en charge l'intégration avec le fournisseur d'identité de l'organisation (SAML, OIDC ou équivalent) |
| **Journalisation et auditabilité** | Fournit une journalisation des événements de sécurité compatible avec l'infrastructure de journalisation de l'organisation |
| **Mécanisme de mise à jour et de correctifs** | Le fournisseur fournit des mises à jour de sécurité régulières avec un processus d'avis clair |
| **Feuille de route de fin de vie** | Cycle de vie du support clair ; aucune technologie en fin de vie ou dans les 12 mois précédant la fin de vie ne peut être sélectionnée |
| **Conformité réglementaire** | La technologie prend en charge la conformité aux exigences nLPD, RGPD (si applicable) et ISO 27001 |

Les décisions de sélection technologique pour les systèmes à risque élevé sont documentées avec les preuves d'évaluation de sécurité et approuvées par le RSSI avant l'acquisition.

---

## Référentiels de sécurité

L'organisation maintient des référentiels de sécurité pour chaque niveau de système, définissant les contrôles de sécurité minimaux requis.

### Classification par niveau de système

| Niveau | Description | Exemples de systèmes |
|--------|-------------|---------------------|
| **Niveau 1 — Critique** | Systèmes traitant des données Confidentielles ou Restreintes ; accessibles depuis Internet ; fonction métier centrale | ERP, CRM avec DCP clients, systèmes de paiement, applications web publiques |
| **Niveau 2 — Important** | Systèmes traitant des données Internes ; exposition externe limitée ; fonction métier support | Outils de collaboration interne, gestion de projets, rapports internes |
| **Niveau 3 — Standard** | Systèmes traitant uniquement des données publiques ; aucune DCP ; fonction non critique | Site marketing (contenu statique), wikis internes (non sensibles) |

**Reclassification du niveau de système** :

Le niveau d'un système est révisé et potentiellement reclassifié lorsque :

- **La classification des données augmente** : Le système commence à traiter des données Confidentielles ou Restreintes (ex. niveau 3 reclassifié en niveau 1).
- **L'exposition Internet change** : Un système interne devient accessible depuis Internet (ex. niveau 2 reclassifié en niveau 1).
- **La criticité métier augmente** : Le système devient critique pour le chiffre d'affaires ou une fonction opérationnelle centrale (ex. niveau 2 reclassifié en niveau 1).
- **Un incident de sécurité survient** : L'incident révèle que le système est plus risqué qu'initialement évalué.
- **Le périmètre réglementaire s'élargit** : Le système commence à traiter des données soumises à une réglementation (PCI DSS, RGPD).

La reclassification déclenche la mise à jour des exigences du référentiel de sécurité et une revue d'architecture. Le propriétaire du système demande au RSSI une revue de reclassification dès qu'un déclencheur survient.

### Exigences du référentiel par niveau

| Domaine de contrôle | Niveau 1 (Critique) | Niveau 2 (Important) | Niveau 3 (Standard) |
|--------------------|--------------------|--------------------|-------------------|
| **Authentification** | AMF obligatoire ; intégration SSO ; délais d'expiration des sessions | AMF obligatoire ; intégration SSO | Conformité à la politique de mots de passe |
| **Chiffrement en transit** | TLS 1.3 requis (exception TLS 1.2 avec approbation RSSI) | TLS 1.2 minimum | TLS 1.2 minimum |
| **Chiffrement au repos** | AES-256 obligatoire | AES-256 pour les DCP/données sensibles | Requis pour les systèmes traitant des données personnelles (noms, adresses électroniques) même non sensibles ; non requis pour les données vraiment publiques (contenu marketing, documentation publiée) |
| **Segmentation réseau** | Segment dédié ; micro-segmentation là où applicable | Segmenté des réseaux non fiables | Contrôles réseau standard |
| **Journalisation** | Tous les événements de sécurité vers le [SIEM] centralisé ; alertes en temps réel | Événements de sécurité vers la journalisation centralisée | Journalisation d'accès de base |
| **Analyse de vulnérabilités** | Continue ou hebdomadaire | Mensuelle | Trimestrielle |
| **Tests d'intrusion** | Annuellement + avant le lancement initial + après changement significatif | Tous les 2 ans | Décision basée sur les risques |
| **Revue d'architecture** | Obligatoire (revue complète avec modèle de menaces) | Obligatoire (revue sommaire) | Liste de contrôle de sécurité |
| **Sauvegarde et récupération** | RPO et RTO définis selon l'analyse d'impact métier ; testés annuellement | Sauvegardes régulières ; récupération testée | Politique de sauvegarde standard |
| **Revue des accès** | Trimestrielle | Semestrielle | Annuelle |

Les référentiels de sécurité sont révisés annuellement par le RSSI et mis à jour pour tenir compte des menaces actuelles, des évolutions technologiques et des exigences réglementaires.

---

## Schémas d'architecture sécurisée

L'organisation maintient un catalogue de schémas d'architecture sécurisée approuvés auxquels les concepteurs de systèmes se réfèrent lors de la construction de nouveaux systèmes ou de la modification de systèmes existants.

**Catégories de schémas** :

| Catégorie | Exemples |
|-----------|----------|
| **Authentification** | Intégration SSO (SAML/OIDC), implémentation AMF, gestion des clés API, authentification par certificat |
| **Autorisation** | Contrôle d'accès basé sur les rôles (RBAC), contrôle d'accès basé sur les attributs (ABAC), autorisation API (OAuth 2.0) |
| **Protection des données** | Chiffrement au repos (AES-256), chiffrement en transit (TLS 1.3), tokenisation des DCP, masquage des données |
| **Sécurité des réseaux** | Architecture DMZ, micro-segmentation, passerelle API avec WAF, VPN/ZTNA pour l'accès à distance |
| **Intégration** | Schémas d'API sécurisées (REST avec OAuth 2.0), sécurité des files de messages, maillage de services avec mTLS |
| **Cloud** | Architecture de zone d'atterrissage, isolation des charges de travail, contrôles de sécurité natifs cloud, intégration CSPM |

Chaque schéma approuvé documente :

- La justification de sécurité et la mitigation des menaces.
- Les conseils de mise en œuvre.
- Les pièges courants et les anti-schémas à éviter.
- Les critères de test et de validation.

**Gouvernance des schémas** :

- Les schémas approuvés sont révisés annuellement pour leur pertinence continue.
- Les écarts par rapport aux schémas approuvés nécessitent l'approbation du RSSI avec justification documentée et contrôles compensatoires.
- Les nouveaux schémas sont validés par la modélisation des menaces avant leur ajout au catalogue.

**Exemple de schéma approuvé : Intégration SSO avec SAML 2.0**

**Justification de sécurité** :

- Centralise l'authentification, réduisant la prolifération des identifiants.
- Permet l'application de l'AMF au niveau du fournisseur d'identité.
- Fournit une piste d'audit des accès aux applications.
- Prend en charge le provisionnement juste-à-temps.

**Conseils de mise en œuvre** :

1. Enregistrer l'application auprès du fournisseur d'identité (Azure AD, Okta, Google Workspace).
2. Configurer les assertions SAML pour inclure les attributs requis (adresse électronique, groupes, statut AMF).
3. Valider les signatures et certificats des réponses SAML.
4. Mettre en œuvre la propagation de la déconnexion (SLO — Single Logout).
5. Définir le délai d'expiration de session conformément à la politique organisationnelle (4 heures maximum).

**Pièges courants** :

- Accepter des assertions SAML non signées.
- Ne pas valider l'expiration des certificats.
- Faire confiance au contenu des assertions sans vérification de signature.
- Ne pas mettre en œuvre la propagation de la déconnexion (l'utilisateur reste connecté à l'application après la déconnexion du fournisseur d'identité).

**Critères de test** :

- La connexion redirige vers le fournisseur d'identité.
- L'application de l'AMF est visible dans le flux d'authentification.
- Une réponse SAML invalide est rejetée.
- La session expire après le délai d'expiration.
- La déconnexion du fournisseur d'identité déconnecte l'utilisateur de l'application.

**Implémentation de référence** : [Lien vers le référentiel de code / wiki]

**Emplacement du catalogue de schémas** : [Outil d'architecture / Confluence / SharePoint] — accessible à tous les architectes et développeurs de systèmes.

### Anti-schémas d'architecture courants à éviter

| Anti-schéma | Risque | Alternative |
|-------------|--------|-------------|
| **Base de données partagée entre frontières de confiance** | Déplacement latéral ; élévation de privilèges via injection SQL | Base de données par service ou isolation stricte au niveau du schéma avec identifiants distincts |
| **Secrets codés en dur dans la configuration** | Exposition des identifiants dans le gestionnaire de versions | Système de gestion des secrets (Vault, Key Vault, Secrets Manager) |
| **Contournement de l'authentification pour les services « internes »** | Hypothèse que le réseau interne est de confiance | TLS mutuel ou OAuth 2.0 pour les communications de service à service |
| **Journalisation de données sensibles (mots de passe, jetons, DCP)** | Violation de conformité ; menace interne | Expurgation des journaux ou tokenisation avant journalisation |
| **Compte admin unique partagé entre services** | Aucune imputabilité ; prolifération des identifiants | Comptes admin spécifiques aux services avec moindre privilège |
| **Points de terminaison de contrôle d'état non authentifiés exposant les détails du système** | Divulgation d'informations | Contrôles d'état authentifiés ou réponse minimale (HTTP 200 uniquement) |
| **Accès direct à la base de données depuis la couche web** | Amplification de l'injection SQL ; pas de défense en profondeur | Couche API/service entre la couche web et la base de données |
| **Confiance accordée à la validation côté client** | Contournement trivial | Validation côté serveur ; côté client uniquement pour l'amélioration de l'expérience utilisateur |

---

## Systèmes tiers et acquis

Les principes d'ingénierie sécurisée s'appliquent aux systèmes développés par des tiers et acquis, intégrés dans l'environnement de l'organisation.

**Pré-acquisition** :

- La documentation de l'architecture de sécurité est examinée avant l'approbation de l'acquisition.
- Une évaluation de la sécurité du fournisseur est réalisée conformément à la Politique relative aux fournisseurs et aux services cloud (A.5.19-23).
- La compatibilité de l'architecture avec les normes de sécurité de l'organisation est vérifiée.

**Exigences contractuelles** :

- Les développeurs tiers sont contractuellement tenus de suivre les principes d'ingénierie sécurisée de l'organisation.
- Une revue d'architecture de sécurité est requise à un jalon de conception.
- Des preuves de pratiques de développement sécurisé sont fournies.
- Les résultats des tests de sécurité sont fournis avant acceptation.

**Post-acquisition** :

- Revue de sécurité de l'intégration avant déploiement dans l'environnement de l'organisation.
- Réévaluation annuelle de l'architecture pour les services SaaS et gérés.
- La non-conformité du fournisseur déclenche l'escalade conformément aux termes du contrat.

**Déclencheurs de revue continue pour les systèmes tiers** :

- Mises à niveau majeures de version (ex. v2.x vers v3.x).
- Changements dans le périmètre de traitement des données du système tiers.
- Incidents de sécurité affectant le système tiers.
- Revue annuelle pour les intégrations de niveau 1.
- Tous les 2 ans pour les intégrations de niveau 2.
- Lorsque la certification SOC 2 ou ISO 27001 du fournisseur expire.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Ingénierie de systèmes sécurisés (SSE)** | La discipline consistant à intégrer les considérations de sécurité dans toutes les phases du cycle de vie du système pour produire des systèmes dignes de confiance |
| **Sécurité dès la conception** | Principe selon lequel la sécurité est intégrée aux systèmes dès la conception plutôt qu'ajoutée après le développement |
| **Sécurité par défaut** | Principe selon lequel les systèmes sont configurés de manière sécurisée dès la sortie de boîte sans nécessiter d'action de l'utilisateur pour activer la sécurité |
| **Défense en profondeur** | Approche de sécurité en couches où plusieurs contrôles protègent les actifs de sorte que la compromission d'une couche n'entraîne pas une compromission totale |
| **Zéro Confiance** | Modèle de sécurité basé sur « ne jamais faire confiance, toujours vérifier » — aucune confiance implicite n'est accordée en fonction de l'emplacement réseau ou d'une authentification antérieure |
| **Modèle de menaces** | Analyse structurée des menaces potentielles, des vecteurs d'attaque et des contre-mesures pour un système |
| **Architecture de sécurité** | Artefacts de conception décrivant comment les contrôles de sécurité sont positionnés et comment ils s'articulent avec l'architecture globale du système |
| **Surface d'attaque** | L'ensemble des points où un attaquant pourrait potentiellement pénétrer dans un système ou en extraire des données |
| **STRIDE** | Méthodologie de modélisation des menaces classant les menaces en : Usurpation, Falsification, Répudiation, Divulgation d'informations, Déni de service et Élévation de privilèges |
| **Référentiel de sécurité** | L'ensemble minimal de contrôles de sécurité requis pour un niveau ou une classification de système donnés |

---

## Rôles et responsabilités

| Rôle | Responsabilités en matière d'architecture sécurisée |
|------|-----------------------------------------------------|
| **Direction générale** | Approuver la politique d'ingénierie sécurisée ; allouer des ressources pour les revues d'architecture ; accepter les risques architecturaux résiduels |
| **RSSI** | Propriété de la politique ; définir et maintenir les principes d'ingénierie sécurisée ; conduire ou mandater les revues d'architecture ; approuver les exceptions d'architecture ; supervision de la modélisation des menaces |
| **Responsable développement** | S'assurer que les équipes de développement appliquent les principes d'ingénierie sécurisée ; participer aux revues d'architecture ; maintenir l'alignement avec les normes technologiques |
| **Propriétaires de systèmes** | Soumettre les systèmes à la revue d'architecture ; maintenir la documentation d'architecture de sécurité ; gérer les risques propres au système |
| **Développeurs / Ingénieurs** | Appliquer les principes d'ingénierie sécurisée dans la conception et l'implémentation des systèmes ; participer à la modélisation des menaces ; utiliser les schémas d'architecture approuvés |
| **IT Opérations** | Mettre en œuvre et maintenir les référentiels de sécurité ; appliquer les normes de configuration ; soutenir la revue d'architecture avec les informations d'infrastructure |
| **Fournisseurs tiers** | Se conformer aux exigences contractuelles d'ingénierie sécurisée ; fournir la documentation d'architecture et les preuves de tests de sécurité |

### Parcours d'escalade

- Problèmes de sécurité architecturaux : Le développeur/ingénieur notifie le RSSI. Le RSSI escalade vers la direction générale si une ressource ou un changement organisationnel est requis.
- Écarts par rapport aux schémas : Le demandeur soumet une demande de dérogation au RSSI. Le RSSI approuve ou rejette avec justification documentée.
- Acceptation des risques architecturaux : Le propriétaire du système soumet l'évaluation des risques au RSSI. Les risques dépassant le seuil d'acceptation du RSSI sont escaladés vers la direction générale.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence |
|----|--------|-------------|-----------|
| 1 | **Principes d'ingénierie sécurisée documentés** (cette politique et tout document de normes associé) | RSSI | *Révisé annuellement ; mis à jour lors de changements du paysage des menaces ou réglementaires* |
| 2 | **Documentation d'architecture de sécurité** (DAS, modèles de menaces, traçabilité des exigences de sécurité) pour les systèmes à risque élevé et moyen | RSSI / Propriétaire du système | *Par système ; mis à jour lors de changements significatifs ; révisé annuellement pour le risque élevé* |
| 3 | **Enregistrements des revues d'architecture** (demandes de revue, résultats, approbation ou rejet avec justification) | RSSI | *Par revue ; conservé 3 ans* |
| 4 | **Rapports de modèles de menaces** (analyse STRIDE, évaluations des risques, atténuations, risques résiduels) | RSSI | *Par système ; conservé pour la durée de vie du système + 3 ans ; de façon permanente pour les systèmes impliqués dans des incidents majeurs (minimum 7 ans)* |
| 5 | **Catalogue de schémas d'architecture approuvés** (schémas documentés avec justification de sécurité) | RSSI / Responsable développement | *Maintenu en continu ; révisé annuellement* |
| 6 | **Configurations des référentiels de sécurité** (par niveau de système, avec contrôles minimaux documentés) | RSSI / IT Opérations | *Révisé annuellement ; mis à jour lors de changements technologiques ou de menaces* |
| 7 | **Évaluations de sécurité pour la sélection technologique** (enregistrements d'évaluation de sécurité pour les nouvelles acquisitions technologiques) | RSSI | *Par acquisition ; conservé 3 ans* |
| 8 | **Registre des exceptions d'architecture** (écarts par rapport aux schémas ou principes avec approbation du RSSI, contrôles compensatoires et dates d'expiration) | RSSI | *Révisé trimestriellement ; conservé 3 ans après clôture* |
| 9 | **Évaluations d'architecture tierce** (revues d'architecture de sécurité des fournisseurs, revues de sécurité d'intégration) | RSSI | *Par engagement ; conservé pour la durée du contrat + 2 ans* |
| 10 | **Avancement de la mise en œuvre Zéro Confiance** (évaluation de maturité, feuille de route, preuves d'achèvement des phases) | RSSI | *Évalué annuellement ; communiqué à la direction générale* |
| 11 | **Enregistrements de validation de la défense en profondeur** (analyse des couches de contrôle confirmant les contrôles en couches dans l'architecture) | RSSI / IT Opérations | *Semestriellement pour les systèmes de niveau 1 ; annuellement pour le niveau 2* |
| 12 | **Dossiers de formation** (complétion de la formation en architecture et ingénierie sécurisées pour le personnel concerné) | RSSI / RH | *Suivi par individu ; révisé annuellement ; objectif : 100 % de complétion* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifie la conformité à cette politique par diverses méthodes, notamment le suivi de la complétion des revues d'architecture, l'analyse de l'adoption des schémas, les audits de conformité aux référentiels de sécurité, les évaluations de la couverture des modèles de menaces, les audits internes et externes, et les retours au propriétaire de la politique.

Les indicateurs suivants sont suivis et communiqués au RSSI chaque trimestre :

| Indicateur | Cible | Seuil critique |
|------------|-------|----------------|
| Nouveaux systèmes à risque élevé avec revue d'architecture complétée | 100 % | <100 % |
| Nouveaux systèmes à risque moyen avec revue d'architecture complétée | 100 % | <80 % |
| Complétion des revues d'architecture dans les SLA (5/10/15 jours ouvrés selon le risque) | 90 % | <70 % |
| Taux d'adoption des schémas d'architecture approuvés pour les nouveaux systèmes | 80 % | <60 % |
| Exceptions d'architecture actives | Minimisées ; tendance à la baisse | >5 simultanées ou toute exception >12 mois |
| Conformité aux référentiels de sécurité (systèmes de niveau 1) | 100 % | <90 % |
| Modèles de menaces à jour pour les systèmes à risque élevé | 100 % | <80 % |

**Exigences de communication** :
- **Rapport trimestriel RSSI** : Statut des revues d'architecture, adoption des schémas, statut du registre des exceptions, conformité aux référentiels.
- **Rapport annuel à la direction générale** : Avancement de la maturité Zéro Confiance, efficacité du programme d'architecture, risques clés et besoins en ressources.
- **Revue annuelle de direction** : Évaluation complète du programme d'ingénierie sécurisée incluant les tendances des indicateurs, les résultats significatifs et les recommandations d'amélioration.

Les indicateurs franchissant les seuils critiques sont escaladés vers le RSSI pour attention immédiate et communiqués lors de la prochaine revue de direction.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le RSSI, avec acceptation documentée du risque, contrôles compensatoires et date de révision définie. Les exceptions d'architecture sont limitées dans le temps (maximum 12 mois) et révisées trimestriellement. Les exceptions sont communiquées à l'équipe de revue de direction. Les exceptions permanentes aux principes fondamentaux d'ingénierie sécurisée et les exceptions qui éliminent la défense en profondeur ne sont pas autorisées.

## Non-conformité

Tout employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Les systèmes déployés sans la revue d'architecture requise peuvent être suspendus de la production dans l'attente d'une revue et d'une remédiation.

## Alignement SOC 2

Cette politique soutient la conformité aux critères des services de confiance SOC 2 :

| Critère SOC 2 | Couverture |
|--------------|-----------|
| **CC3.1** (Spécification des objectifs) | Objectifs de sécurité dans la conception des systèmes |
| **CC5.2** (Contrôles généraux sur la technologie) | Contrôles d'architecture ; les changements d'architecture nécessitent une approbation de contrôle des changements conformément à la Politique de gestion de la configuration (A.8.9) |
| **CC6.1** (Sécurité des accès logiques) | Architecture d'authentification, moindre privilège, Zéro Confiance |
| **CC6.6** (Protection contre les menaces externes) | Défense en profondeur, contrôles de périmètre |
| **CC7.1** (Détection des vulnérabilités) | Analyse de vulnérabilités dans les exigences du référentiel |
| **CC7.2** (Détection des anomalies) | Couche de surveillance dans la défense en profondeur ; référence croisée avec la Politique d'activités de surveillance (A.8.16) |
| **CC9.2** (Gestion des risques fournisseurs) | Revue d'architecture tierce ; référence croisée avec la Politique relative aux fournisseurs et services cloud (A.5.19-23) |

**Exigences de preuves SOC 2** :

- Enregistrements des revues d'architecture (Preuve n°3).
- Modèles de menaces (Preuve n°4).
- Catalogue de schémas approuvés (Preuve n°5).
- Référentiels de sécurité (Preuve n°6).
- Matrice de traçabilité des exigences de sécurité pour les systèmes à risque élevé.
- Preuves d'approbation du RSSI pour les exceptions d'architecture (Preuve n°8).

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions tiennent compte des évolutions des normes d'ingénierie sécurisée (NIST SP 800-160, NIST SP 800-207), de l'évolution du paysage des menaces et des techniques d'attaque, des nouveaux schémas d'architecture et normes technologiques, des changements réglementaires (nLPD, RGPD), des enseignements tirés des incidents de sécurité et des revues d'architecture, et des constatations d'audit. Les non-conformités liées à cette politique sont enregistrées et gérées via le processus d'action corrective du SMSI (Clause 10.2) avec analyse des causes racines et remédiation suivie.

---

# Domaines de la norme ISO 27001 couverts

Politique relative aux principes d'architecture et d'ingénierie de systèmes sécurisés — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.1 Actions face aux risques et opportunités | 5.8 Sécurité de l'information dans la gestion de projets |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 8.25 Cycle de développement sécurisé |
| Clause 8.1 Planification et contrôle opérationnels | 8.26 Exigences de sécurité des applications |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | **8.27 Principes d'architecture et d'ingénierie de systèmes sécurisés** |
| Clause 10.2 Non-conformité et action corrective | 8.28 Codage sécurisé |
| | 8.29 Tests de sécurité dans le développement et l'acceptation |
| | 8.31 Séparation des environnements de développement, de test et de production |
| | 8.9 Gestion de la configuration |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 7 — Protection des données dès la conception et par défaut ; Art. 8 — Mesures techniques et organisationnelles proportionnées aux risques |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (si applicable) | Art. 25 — Protection des données dès la conception et par défaut ; Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.27 — Principes d'architecture et d'ingénierie de systèmes sécurisés |
| ISO/IEC 27002:2022 | Section 8.27 — Conseils de mise en œuvre pour l'architecture de systèmes sécurisés |
| NIST SP 800-160 Vol. 1 Rév. 1 | Engineering Trustworthy Secure Systems — principes fondamentaux d'ingénierie de la sécurité des systèmes |
| NIST SP 800-207 | Zero Trust Architecture — architecture de référence pour la mise en œuvre du modèle Zéro Confiance |
| NIST SP 800-53 Rév. 5 | SA-8 (Principes d'ingénierie de la sécurité et de la protection de la vie privée) — 28 principes d'ingénierie sécurisée incluant abstractions claires, modularité, réduction de la complexité |
| CIS Controls v8 | Contrôle 4 (Configuration sécurisée), Contrôle 16 (Sécurité des logiciels applicatifs) — mesures de protection soutenant l'architecture sécurisée |

---

<!-- QA_VERIFIED: 2026-03-29 -->
