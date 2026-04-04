<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.10-FR:framework:POL:a.8.10 -->
**ISMS-POL-A.8.10 — Suppression de l'information**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de suppression de l'information |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.10 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur des Systèmes d'Information (DSI)
- Confidentialité : Délégué à la Protection des Données (DPD)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.10.1 (Évaluation des déclencheurs de conservation et de suppression)
- ISMS-IMP-A.8.10.2 (Évaluation des méthodes de suppression)
- ISMS-IMP-A.8.10.3 (Évaluation de la suppression par les tiers et dans le cloud)
- ISMS-IMP-A.8.10.4 (Évaluation de la vérification et des preuves)
- ISO/IEC 27001:2022 Contrôle A.8.10

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de suppression de l'information afin d'assurer la suppression systématique des informations lorsqu'elles ne sont plus nécessaires, conformément au Contrôle A.8.10 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les actifs informationnels quel que soit leur emplacement de stockage (sur site, cloud, tiers), tous les types de supports de stockage (magnétiques, à état solide, optiques, papier, appareils mobiles), tous les systèmes et applications (y compris l'infrastructure de sauvegarde) et toutes les catégories de données (données personnelles, dossiers d'entreprise, données techniques, journaux) tout au long de leur cycle de vie.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de suppression de l'information. Cette politique établit QUELLES données doivent être supprimées, QUAND la suppression doit avoir lieu, QUELLES méthodes sont approuvées et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.10.

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse (minimisation des données et droit à l'effacement), le RGPD de l'UE Article 17 (Droit à l'effacement) lors du traitement de données personnelles de l'UE, et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.10 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.10 — Suppression de l'information**

> *Les informations stockées dans les systèmes d'information, les appareils ou sur tout autre support de stockage devraient être supprimées lorsqu'elles ne sont plus nécessaires.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les contrôles de suppression de l'information, assurant la suppression systématique des données à l'expiration des exigences de conservation, soutenant les principes de minimisation des données, la conformité réglementaire et la protection contre la divulgation non autorisée.

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de suppression de l'information alignées sur la classification des données, les obligations réglementaires et l'appétit au risque organisationnel
- **Établit** le cadre de gouvernance pour la prise de décision de suppression, la gestion des exceptions et la surveillance de la conformité
- **Précise** les méthodes de suppression approuvées et les critères de sélection selon le type de support et la sensibilité des données
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00
- **Identifie** les rôles et responsabilités organisationnels pour la mise en œuvre et la supervision des contrôles de suppression
- **S'intègre** avec les contrôles connexes : classification des données (A.5.12), gestion des actifs (A.5.9), protection de la vie privée (A.5.34) et mise au rebut sécurisée (A.7.14)

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les outils ou produits de suppression** (sélection technologique basée sur l'évaluation des risques)
- **Définit pas les procédures de suppression spécifiques aux systèmes** (voir ISMS-IMP-A.8.10)
- **Fournit pas les instructions de suppression spécifiques aux fournisseurs cloud** (documentées dans ISMS-IMP-A.8.10.3)
- **Remplace pas la politique de classification des données** (la suppression s'appuie sur le schéma de classification A.5.12)
- **Établit pas les calendriers de conservation pour tous les types de données** (définis par les Propriétaires de données avec contributions juridiques/réglementaires, documentés dans ISMS-IMP-A.8.10.1)
- **Impose pas de normes spécifiques d'assainissement** (NIST SP 800-88 utilisé comme référence informative sauf si contractuellement requis)

## Périmètre

**Cette politique s'applique à** :

**Tous les actifs informationnels** (électroniques et physiques) contenant des données organisationnelles ou personnelles :

- Données à caractère personnel (DCP) soumises au RGPD/nLPD
- Données financières (données de cartes de paiement, dossiers financiers, détails des transactions)
- Informations de santé (dossiers médicaux, données de santé des employés)
- Identifiants d'authentification (mots de passe, clés API, jetons, clés privées)
- Informations métier propriétaires (secrets commerciaux, données stratégiques, tarification, contrats)
- Données techniques (code source, configurations de systèmes, schémas réseau)
- Communications (e-mails, messages instantanés, enregistrements d'appels)
- Journaux système et pistes d'audit
- Toutes données classifiées Confidentielles ou Restreintes selon le schéma de classification de [Organisation]

**Tous les emplacements de stockage** :

- Infrastructure sur site (centres de données, salles serveurs, stockage local)
- Environnements cloud (IaaS, PaaS, SaaS chez tous les fournisseurs)
- Sous-traitants tiers (prestataires de services gérés, sous-traitants, services externalisés)
- Systèmes de sauvegarde et de reprise après sinistre
- Appareils des utilisateurs finaux (ordinateurs portables, de bureau, appareils mobiles, supports amovibles)
- Archives (stockage physique de dossiers, stockage à froid, bandes magnétiques)
- Installations de colocation et infrastructure hébergée

**Tous les supports de stockage** :

- Stockage magnétique (disques durs, bandes magnétiques)
- Stockage à état solide (SSD, clés USB, cartes SD)
- Supports optiques (CD, DVD, Blu-ray)
- Documents papier (documents imprimés, formulaires, dossiers)
- Appareils mobiles (smartphones, tablettes, appareils connectés)
- Stockage en réseau (NAS, SAN)
- Stockage natif cloud (stockage d'objets, de blocs, de fichiers)

**Toutes les étapes du cycle de vie** :

- Systèmes opérationnels (bases de données de production, partages de fichiers actifs)
- Données archivées (archives de conformité, dossiers inactifs)
- Conservation des sauvegardes (sauvegardes quotidiennes, hebdomadaires, mensuelles, annuelles)
- Mise au rebut en fin de vie (systèmes décommissionnés, supports retirés)
- Environnements hors production (développement, test, assurance qualité, formation, sandbox)

**Hors périmètre** :

- **Données sous blocage légal** : Suppression suspendue conformément aux exigences de contentieux, d'investigation ou d'examen réglementaire (couvert par des procédures distinctes de blocage légal — Section 2.6)
- **Données d'archivage à conservation permanente** : Non applicable conformément aux exigences réglementaires ou métier ; documenté dans le calendrier de conservation
- **Données de tiers où [Organisation] agit uniquement en tant que sous-traitant** : Suppression exécutée selon les instructions du responsable du traitement
- **Informations publiques intentionnellement publiées** : Procédures distinctes de gestion du contenu
- **Données anonymisées irréversiblement** : Ne nécessitent pas de suppression conformément aux réglementations sur la confidentialité

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés de suppression |
|----------------|---------------|-------------------------------|
| **nLPD suisse** | Toutes les opérations suisses | Art. 6 — Principe de minimisation des données ; Art. 12 — Droit à l'effacement des personnes concernées ; Art. 25 — Mesures de sécurité appropriées |
| **RGPD de l'UE** | Lors du traitement de données personnelles de l'UE | Art. 5(1)(e) — Principe de limitation de la conservation ; Art. 17 — Droit à l'effacement (« droit à l'oubli ») ; Art. 19 — Notification de l'effacement aux tiers ; Art. 32 — Sécurité du traitement |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôle A.8.10 — Politique et procédures de suppression de l'information documentées |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Condition de déclenchement | Exigences de suppression |
|---------------|---------------------------|--------------------------|
| **PCI DSS v4.0.1** | Traitement de données de cartes de paiement | Exig. 3.1 — Conserver uniquement selon les besoins métier/légaux ; Exig. 3.2 — Suppression sécurisée des données de titulaires |
| **FINMA** | Établissement financier réglementé en Suisse | Conservation des dossiers ; suppression sécurisée après la période de conservation |
| **DORA** | Entité de services financiers UE | Art. 28 — Gestion des risques TIC tiers, y compris la suppression des données à la fin du contrat |
| **NIS2** | Entité essentielle/importante (UE) | Art. 21 — Gestion des risques en cybersécurité incluant la sécurité des données |

**Niveau 3 : Référence informative**

- NIST SP 800-88 Rév. 1 — Lignes directrices pour l'assainissement des supports (méthodes Effacement, Purge, Destruction)
- ISO/IEC 27040:2015 — Sécurité du stockage incluant les orientations d'assainissement
- ISO/IEC 27555:2024 — Lignes directrices sur la suppression des données à caractère personnel
- DIN 66399 — Destruction des supports de données (7 niveaux de sécurité)

---

# Cadre des exigences de suppression de l'information

## Conservation et déclencheurs de suppression

[Organisation] met en œuvre des calendriers de conservation définissant quand la suppression est requise ou permise.

**Inventaire et classification des données** :

[Organisation] DOIT maintenir un inventaire complet des catégories de données traitées, incluant :

- Type et format des données (bases de données structurées, fichiers non structurés, e-mails, journaux, sauvegardes)
- Niveau de classification selon le schéma de [Organisation] (Restreint, Confidentiel, Interne, Public)
- Finalité métier et justification du traitement
- Emplacement de stockage (système, environnement, type de support)
- Propriétaire des données responsable des décisions de conservation et de suppression

**Vérification de la complétude de l'inventaire** :

La complétude de l'inventaire DOIT être vérifiée par :

**(a) Outils de découverte automatisés** pour les systèmes IT (analyse des bases de données, des partages de fichiers, du stockage cloud)

**(b) Attestation annuelle** des Propriétaires de systèmes confirmant que toutes les catégories de données de leurs systèmes sont enregistrées dans l'inventaire

**(c) Rapprochement trimestriel** de l'inventaire par rapport au registre des actifs IT (conformément à ISMS-POL-A.5.9) et au registre des services cloud

**Exigences du calendrier de conservation** :

[Organisation] DOIT établir des calendriers de conservation pour toutes les catégories de données basés sur :

- **Exigences légales** : Lois, réglementations, ordonnances judiciaires imposant des périodes de conservation spécifiques
- **Exigences réglementaires** : Réglementations sectorielles (PCI DSS, FINMA) précisant la conservation
- **Obligations contractuelles** : Contrats clients, accords fournisseurs, accords de niveau de service requérant la conservation
- **Besoins métier documentés** : Exigences opérationnelles, analyse historique, continuité des activités justifiés et approuvés par le Propriétaire des données

Les calendriers de conservation DOIVENT documenter :

- Catégorie et sous-catégories de données
- Période de conservation minimale (plancher légal/réglementaire)
- Période de conservation maximale (plafond de minimisation des données)
- Justification de la période de conservation (citation légale, justification métier)
- Propriétaire des données et approbation
- Date de révision (annuelle minimum)

**Déclencheurs de suppression** :

La suppression DOIT être déclenchée par l'un des événements suivants :

**(a) Expiration de la période de conservation** : Les données atteignent la fin de la période de conservation approuvée

**(b) Demande d'effacement de la personne concernée** : Une personne exerce son droit à l'effacement en vertu de l'Article 17 du RGPD ou de la nLPD suisse (voir Section 2.5)

**(c) Résiliation du contrat ou de l'accord de service** : La relation contractuelle prend fin, l'obligation de conservation cesse

**(d) Achèvement de la finalité du traitement** : La finalité originale de la collecte/du traitement des données ne s'applique plus

**(e) Levée du blocage légal** : Le contentieux, l'investigation ou l'examen réglementaire se conclut, le blocage légal est levé (voir Section 2.6)

**(f) Décommissionnement d'un actif** : Système IT, appareil ou support de stockage en fin de vie nécessitant une mise au rebut

**(g) Retrait du consentement** : La personne concernée retire son consentement au traitement (lorsque le consentement est la base légale conformément à l'Art. 6(1)(a) du RGPD)

**Conflits de périodes de conservation** :

Lorsque plusieurs exigences de conservation s'appliquent aux mêmes données :

- La **période de conservation la plus longue** DOIT être mise en œuvre pour assurer la conformité à toutes les obligations
- Une révision juridique est requise en cas de conflits entre obligations réglementaires et contractuelles

## Méthodes de suppression

[Organisation] sélectionne et met en œuvre des méthodes de suppression appropriées au type de support et à la classification des données.

**Méthodes approuvées par type de support** :

| Type de support | Données Restreintes/Confidentielles | Données Internes | Données Publiques |
|----------------|-------------------------------------|------------------|-------------------|
| **Disques durs (HDD)** | Destruction physique ou purge (dégazage + écrasement multiple) | Effacement sécurisé (au minimum single-pass) ou destruction | Effacement logique acceptable |
| **Disques SSD/Flash** | Effacement cryptographique + destruction physique ou purge spécifique SSD | Effacement cryptographique ou purge spécifique SSD | Effacement logique ou réinitialisation usine |
| **Appareils mobiles** | Effacement à distance + réinitialisation usine vérifiée | Réinitialisation usine + suppression des données d'entreprise | Réinitialisation usine |
| **Supports amovibles (USB, SD)** | Destruction physique | Effacement sécurisé ou destruction | Formatage standard |
| **Documents papier** | Déchiquetage coupe-croisée (Niveau DIN 4 minimum) | Déchiquetage | Corbeille |
| **Bandes magnétiques** | Dégazage + destruction physique | Dégazage | Écrasement ou réutilisation |
| **Stockage cloud** | Effacement cryptographique (révocation des clés de chiffrement) + confirmation fournisseur | Suppression API avec vérification | Suppression standard |

**Effacement cryptographique** :

L'effacement cryptographique (destruction des clés de chiffrement, rendant les données inaccessibles) est une méthode approuvée pour :

- Les stockages cloud chiffrés (S3, Azure Blob, GCP Storage avec CMEK)
- Les disques SSD chiffrés où les méthodes d'effacement traditionnelles sont inefficaces
- Les environnements virtualisés où l'effacement physique n'est pas faisable

Les exigences d'effacement cryptographique incluent : chiffrement activé AVANT la collecte des données, clés de chiffrement sous contrôle de [Organisation], révocation et destruction des clés documentées et vérifiées, confirmation que les données ne sont pas accessibles après la révocation des clés.

**Destruction physique** :

La destruction physique est requise lorsque :

- Les données de classification Restreinte ne peuvent pas être supprimées par d'autres moyens
- Le support ou l'appareil est physiquement endommagé et ne peut pas être effacé électroniquement
- Les exigences contractuelles ou réglementaires imposent la destruction physique
- La vérification de la suppression par d'autres méthodes n'est pas possible

La destruction physique DOIT : être réalisée par du personnel autorisé ou des prestataires certifiés, inclure une attestation de destruction du prestataire, être documentée avec numéros de série et date, garantir la non-récupérabilité.

## Suppression par les tiers et dans le cloud

[Organisation] DOIT s'assurer que les tiers traitant des données organisationnelles les suppriment de manière sécurisée.

**Obligations contractuelles** :

Les contrats avec les sous-traitants tiers DOIVENT inclure :

- Des clauses de suppression des données à la résiliation du contrat
- Des délais de suppression (maximum 30 jours après résiliation pour les données Confidentielles/Restreintes)
- Des exigences de méthode de suppression alignées sur cette politique
- Des exigences de fourniture d'attestations ou de certificats de suppression
- Des droits d'audit pour vérifier la conformité à la suppression
- Des exigences de notification des violations liées à la suppression

**Suppression dans le cloud** :

Pour les fournisseurs de services cloud, [Organisation] DOIT :

- Activer le chiffrement avant le stockage des données (pour permettre l'effacement cryptographique)
- Comprendre et documenter les procédures de suppression de chaque fournisseur cloud
- Vérifier que la suppression inclut toutes les copies : données en direct, sauvegardes, journaux, métadonnées, copies de cache
- Obtenir une confirmation de la suppression du fournisseur cloud (documentation, API de vérification, ou certificat)
- Documenter les délais de rémanence des données du fournisseur (période pendant laquelle les données peuvent rester dans les systèmes du fournisseur après la suppression)

## Vérification et preuves

[Organisation] DOIT vérifier que la suppression a eu lieu et conserver les preuves appropriées.

**Exigences de vérification** :

La vérification DOIT confirmer :

- Les données cibles ont été supprimées selon la méthode approuvée
- Aucun résidu récupérable des données n'existe (dans la mesure du possible selon la méthode)
- La suppression couvre tous les emplacements de stockage identifiés (systèmes primaires, sauvegardes, archives, caches)
- Les dossiers de déclenchement de la suppression correspondent aux dossiers d'exécution

**Méthodes de vérification** :

| Type de suppression | Méthode de vérification |
|---------------------|------------------------|
| Suppression logique des données | Requêtes de base de données confirmant l'absence de données, journaux d'exécution |
| Effacement sécurisé des supports | Rapport de l'outil de vérification d'effacement, journaux de l'outil |
| Effacement cryptographique | Documentation de révocation des clés, confirmation d'absence d'accès |
| Destruction physique | Attestation de destruction du prestataire, avec numéros de série |
| Suppression cloud | Réponse de l'API de suppression, confirmation de l'API d'état, documentation fournisseur |
| Suppression par des tiers | Attestation du tiers, rapport d'audit ou certificat de suppression |

**Conservation des preuves de suppression** :

Les preuves de suppression DOIVENT être conservées pendant : la période de conservation des données supprimées + 3 ans ou la période requise par la réglementation applicable (la plus longue étant retenue).

**Contrôle de l'intégrité des sauvegardes** :

[Organisation] DOIT s'assurer que les sauvegardes sont incluses dans les processus de suppression. Les approches incluent :

- Suppression des données dans le système de production avec réplication vers les sauvegardes via remplacement du cycle de sauvegarde (recommandée)
- Suppression directe des enregistrements de sauvegarde (complexe, risque de corruption des sauvegardes)
- Effacement cryptographique (préférée pour les sauvegardes cloud)
- Accélération de l'expiration des cycles de sauvegarde pour les données hautement sensibles

## Droits à l'effacement des personnes concernées

[Organisation] DOIT traiter les demandes d'effacement des personnes concernées conformément au RGPD Article 17 et à la nLPD suisse.

**Processus de traitement des demandes d'effacement** :

1. **Réception** : La demande est reçue par le DPD ou un canal désigné
2. **Vérification d'identité** : L'identité du demandeur est vérifiée
3. **Évaluation de l'applicabilité** : Vérifier si l'une des exceptions légales s'applique (obligations légales, intérêt public, etc.)
4. **Localisation des données** : Identifier toutes les instances des données du demandeur
5. **Exécution** : Procéder à la suppression si les conditions sont remplies
6. **Notification** : Informer le demandeur du résultat dans les délais requis (30 jours en vertu du RGPD)
7. **Notification aux tiers** : Informer les tiers auxquels les données ont été communiquées (Art. 19 RGPD)

**Délais de réponse** :

- Accusé de réception : Dans les 5 jours ouvrables
- Décision et action : Dans les 30 jours calendaires
- Extension (cas complexes) : Jusqu'à 60 jours supplémentaires avec notification

**Bases légales pour refuser l'effacement** (Art. 17(3) RGPD) :

- Exercice de la liberté d'expression et d'information
- Respect d'une obligation légale
- Exécution d'une mission d'intérêt public
- Constatation, exercice ou défense de droits en justice

## Gestion du blocage légal

[Organisation] DOIT suspendre la suppression lorsqu'un blocage légal est en vigueur.

**Déclencheurs de blocage légal** :

- Notification de litige ou action en justice imminente
- Citation à comparaître, injonction de tribunal ou exigence réglementaire
- Investigation interne ou externe
- Demande de renseignements réglementaire

**Processus de blocage légal** :

1. Le service juridique identifie et notifie les parties concernées
2. Les données faisant l'objet du blocage sont identifiées et étiquetées
3. Les processus de suppression automatiques sont suspendus pour les données concernées
4. Les données sous blocage légal sont conservées jusqu'à la levée du blocage
5. À la levée du blocage, les déclencheurs de suppression normaux reprennent

**Durée du blocage** : Aussi longtemps que requis par les obligations légales. Révision trimestrielle par le service juridique.

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **RSSI** | Propriétaire de la politique ; approbation des méthodes de suppression ; supervision de la conformité |
| **DPD** | Traitement des droits à l'effacement ; conformité RGPD/nLPD ; supervision de la suppression des DCP |
| **Responsable juridique/conformité** | Définition des exigences de conservation ; gestion des blocages légaux ; évaluation de l'applicabilité réglementaire |
| **DSI/Opérations IT** | Exécution technique de la suppression ; mise en œuvre des outils ; documentation et vérification |
| **Propriétaires de données** | Définition des calendriers de conservation ; autorisation de suppression ; gestion des exceptions |
| **Propriétaires de systèmes** | Suppression spécifique aux systèmes ; conformité avec les sous-traitants tiers |
| **Opérations de sécurité** | Vérification des méthodes de suppression ; audit des preuves ; surveillance de la conformité |

---

# Gouvernance et conformité

## Révision de la politique

**Déclencheurs de révision** :

- Révision annuelle planifiée
- Changements réglementaires affectant les droits à l'effacement ou la conservation des données
- Incidents de sécurité impliquant des données qui auraient dû être supprimées
- Nouveaux types de stockage ou fournisseurs cloud nécessitant des méthodes de suppression actualisées

## Métriques et reporting

**Métriques de conformité** :

- Taux de couverture de l'inventaire des données (cible : ≥ 95 %)
- Conformité du calendrier de conservation (% de types de données avec calendrier documenté)
- Taux de complétion des suppressions planifiées (cible : 100 % dans le délai SLA)
- Temps de traitement des demandes d'effacement (cible : ≤ 30 jours)
- Taux de vérification des suppressions (cible : 100 % avec documentation)

**Reporting** :

- Mensuel : Métriques opérationnelles au RSSI et au DPD
- Trimestriel : Rapport de conformité à la Direction générale
- Annuel : Révision complète du programme avec audit externe

## Gestion des exceptions

[Organisation] DOIT gérer formellement les exceptions aux exigences de suppression.

**Exigences de demande d'exception** :

- Justification métier documentée
- Évaluation des risques avec score de risque résiduel
- Contrôles compensatoires
- Date d'expiration (maximum 12 mois)
- Calendrier de mise en conformité

**Niveaux d'approbation selon la classification des données** :

| Classification | Autorité d'approbation |
|----------------|----------------------|
| Données Restreintes | RSSI + DPD + Direction générale |
| Données Confidentielles | RSSI + DPD |
| Données Internes | RSSI |
| Données Publiques | Responsable de la sécurité IT |

**Exceptions automatiquement refusées** :

- Conservation de DCP au-delà du délai du droit à l'effacement sans base légale valide
- Absence de contrôles compensatoires pour les données à haut risque
- Demandes de renouvellement d'exception sans progrès démontrables vers la conformité

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.10 v1.0)
- ✅ Signatures d'approbation du RSSI, DPD, Responsable juridique/conformité, Direction générale
- ✅ Exigences de conservation documentées
- ✅ Méthodes de suppression spécifiées par sensibilité des données
- ✅ Exigences de suppression par les tiers et dans le cloud définies
- ✅ Exigences de vérification documentées
- ✅ Processus de demande d'effacement des personnes concernées défini
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

- Journaux d'exécution des suppressions
- Calendrier de conservation (version actuelle + versions remplacées)
- Attestations de destruction des tiers
- Registre des demandes RGPD/nLPD
- Registre des blocages légaux
- Approbations d'exceptions
- Rapports trimestriels de conformité
- Inventaire des données avec périmètre de suppression

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

*Cette politique établit les exigences de suppression de l'information. Les procédures de mise en œuvre sont documentées dans la suite ISMS-IMP-A.8.10 (Déclencheurs de conservation et de suppression, Méthodes de suppression, Suppression par les tiers et dans le cloud, Vérification et preuves).*

<!-- QA_VERIFIED: 2026-04-02 -->
