<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.12-FR:operational:OP-POL:a.8.12 -->
**ISMS-OP-POL-A.8.12 — Prévention des fuites de données**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Prévention des fuites de données |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.12 |
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

- ISO/IEC 27001:2022 Contrôle A.8.12 — Prévention des fuites de données
- ISO/IEC 27002:2022 Section 8.12 — Lignes directrices de mise en œuvre pour la prévention des fuites de données
- NIST SP 800-53 Rév. 5 — AC-4 (Application des flux d'informations), SC-7 (Protection des frontières), SI-4 (Surveillance du système)
- CIS Controls v8 — Mesure 3.13 (Déployer une solution de prévention des pertes de données), 3.1–3.14 (Protection des données)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la prévention des fuites de données |
|----------|----------------------------------------------------|
| A.5.10 Utilisation acceptable de l'information et des autres actifs associés | Définit les pratiques acceptables de traitement et de transfert des données appliquées par les mesures DLP |
| A.5.12 Classification de l'information | La classification des données détermine la sévérité des règles DLP et le mode d'application |
| A.5.13 Étiquetage de l'information | Les étiquettes de documents permettent la détection de contenu DLP et la correspondance de politique |
| A.5.14 Transfert de l'information | Les politiques de transfert sont appliquées via la surveillance des canaux DLP |
| A.5.15–16–18 Gestion des identités et des accès | Le contexte d'identité de l'utilisateur est utilisé dans l'évaluation des règles DLP et la gestion des exceptions |
| A.5.24–28 Cycle de vie de la gestion des incidents | Les alertes DLP alimentent le flux de travail de gestion des incidents et la notification de violation |
| A.5.34 Protection de la vie privée et des données à caractère personnel | Les mesures DLP empêchent la divulgation non autorisée des DCP ; le droit de la vie privée encadre la portée de la surveillance |
| A.8.10 Suppression des informations | Les mesures DLP complètent les contrôles de suppression en empêchant la rétention sur des supports amovibles |
| A.8.11 Masquage des données | Le masquage appliqué avant le partage réduit le volume des alertes DLP et le risque résiduel |
| A.8.15 Journalisation | Les événements DLP sont journalisés pour investigation, corrélation et preuve de conformité |
| A.8.16 Activités de surveillance | Les mesures DLP génèrent des événements de sécurité pour l'intégration SIEM et l'analyse comportementale |
| A.8.20–22 Sécurité des réseaux | La segmentation réseau définit le placement des capteurs DLP et les points d'inspection |
| A.8.23 Filtrage web | Le filtrage web et les mesures DLP contrôlent conjointement les canaux d'exfiltration de données via le web |
| A.8.24 Utilisation de la cryptographie | Les canaux chiffrés peuvent nécessiter une inspection TLS pour l'analyse du contenu DLP |

**Politiques internes associées** :

- Politique de classification et de traitement de l'information
- Politique d'utilisation acceptable
- Politique de gestion des incidents
- Politique de journalisation
- Politique des activités de surveillance (A.8.16)
- Politique de sécurité des réseaux
- Politique de protection de la vie privée et des données à caractère personnel
- Politique de filtrage web

---

# Politique de prévention des fuites de données

## Finalité

La présente politique a pour objet d'établir les exigences relatives aux mesures de prévention des fuites de données (DLP) permettant de détecter, prévenir et traiter la divulgation, le transfert ou l'exfiltration non autorisés d'informations sensibles depuis les systèmes, réseaux et postes de travail de l'organisation. Les mesures DLP traitent à la fois l'exfiltration malveillante (menaces internes, comptes compromis, menaces persistantes avancées) et la divulgation accidentelle (erreur humaine, mauvaise configuration, communications mal dirigées).

La présente politique soutient la nLPD (revLPD) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles traitées par l'organisation. La surveillance DLP est mise en place conformément au droit suisse du travail, notamment l'art. 26 OLT 3 (interdiction des systèmes de surveillance des comportements) et l'art. 328b CO (traitement proportionné des données des employés). Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD art. 32 (sécurité du traitement) et art. 88 (traitement dans le contexte de l'emploi) s'appliquent également.

## Engagements de service et protection des données clients

Les mesures DLP soutiennent les engagements de l'organisation envers les clients concernant la protection des données clients contre toute divulgation non autorisée. Les accords clients comprennent généralement des engagements tels que :

- « Le prestataire de services mettra en place des mesures techniques et organisationnelles pour prévenir la divulgation non autorisée des données du client. »
- « Le prestataire de services notifiera le client dans un délai de [X heures] de tout accès ou divulgation non autorisé des données du client. »
- « Le prestataire de services maintiendra des systèmes de surveillance pour détecter et prévenir l'exfiltration de données. »

### Exigences de protection des données clients

Les données clients traitées par l'organisation bénéficieront d'une protection DLP proportionnelle aux engagements contractuels :

| Type de données client | Classification DLP | Niveau de protection | Exigence de notification (en cas de fuite) |
|------------------------|-------------------|----------------------|--------------------------------------------|
| **DCP des clients** | Confidentiel minimum | Surveillance courriel + web + terminal + cloud ; blocage vers les destinataires externes | Notification au client dans [X heures] selon contrat ; notification réglementaire conformément à la nLPD art. 24 |
| **Données métier clients** (hors DCP) | Confidentiel ou Interne | Surveillance courriel + web minimum ; blocage ou alerte selon les termes contractuels | Notification au client dans [X heures] selon contrat |
| **Identifiants/clés API clients** | Restreint | Tous les canaux ; blocage immédiat + réponse aux incidents | Notification immédiate au client (dans l'heure) |
| **Données clients agrégées/anonymisées** | Interne | Surveillance uniquement ; détection axée sur le risque de ré-identification | Notification au client si désanonymisation suspectée |

### Procédures de notification des clients

Lorsque des incidents DLP impliquent des données clients :

1. **Évaluation initiale** (dans l'heure) : Déterminer la portée, les clients affectés, les types de données et la durée d'exposition.
2. **Confinement** (immédiat) : Bloquer le transfert, isoler les systèmes, révoquer les identifiants selon le cas.
3. **Notification au client** (selon les termes contractuels, généralement 4 à 24 heures) :
   - Résumé de l'incident (ce qui s'est passé, quand découvert)
   - Types et volume de données affectées
   - Clients affectés (si multi-locataires)
   - Actions prises par l'organisation
   - Actions recommandées pour le client
   - Contact pour toute question
4. **Notification réglementaire** (le cas échéant) : nLPD art. 24 (sans délai indu), RGPD art. 33 (72 heures).
5. **Suivi** : Rapport d'analyse des causes profondes fourni aux clients affectés dans [X jours ouvrables].

**Exigences spécifiques aux clients** : Lorsque des clients ont négocié des délais de notification personnalisés, des seuils de gravité d'incident ou des exigences de reporting, ceux-ci doivent être documentés dans le registre des contrats clients et intégrés dans le routage des alertes DLP et les flux de travail de réponse aux incidents.

## Champ d'application

La présente politique s'applique à tous les actifs informationnels classifiés Interne, Confidentiel ou Restreint conformément au schéma de classification des données de l'organisation. Cela inclut :

- Tous les systèmes, applications, réseaux, postes de travail et services qui traitent, stockent ou transmettent des informations de l'organisation.
- Tous les canaux de sortie des données : courriel (SMTP, webmail), web (envois HTTP/HTTPS), terminaux (USB, stockage local, impression), réseau (protocoles de transfert de fichiers), services cloud (SaaS, stockage cloud), appareils mobiles (professionnels et BYOD), et API d'applications.
- Tout le personnel de l'organisation (employés, contractants, personnel temporaire) ayant accès aux informations de l'organisation.
- Tous les prestataires de services tiers et services cloud traitant des données de l'organisation.
- Tous les modèles de déploiement (sur site, hybride, natif cloud).

**Hors champ d'application** : Informations publiques ne nécessitant pas de protection DLP. Sécurité physique des documents papier (couverte par A.7.x Sécurité physique). Processus de sauvegarde et d'archivage (couverts par A.8.13 Sauvegarde des informations). Conservation et suppression des données (couverts par A.8.10 Suppression des informations). Masquage et anonymisation des données (couverts par A.8.11 Masquage des données). Contrôles de sécurité de l'information sans rapport avec l'exfiltration de données (contrôle d'accès, authentification et gestion des correctifs sont traités par leurs contrôles respectifs).

## Principe

Des mesures de prévention des fuites de données devraient être appliquées aux systèmes, réseaux et autres appareils qui traitent, stockent ou transmettent des informations sensibles (ISO 27001:2022 Contrôle A.8.12).

L'organisation devrait mettre en œuvre des mesures DLP proportionnelles à la sensibilité des informations protégées et au risque de divulgation non autorisée. Les mesures DLP devraient être fondées sur la classification — les exigences de protection s'intensifient avec la sensibilité des données. L'organisation devrait équilibrer la surveillance sécuritaire avec les droits à la vie privée des employés, en veillant à ce que la surveillance DLP soit transparente, proportionnée et axée sur la protection des données plutôt que sur la surveillance des comportements des employés.

Les mesures DLP ne devraient pas être utilisées pour l'évaluation des performances des employés, le suivi du temps de travail, ni à toute fin autre que la sécurité de l'information et la protection des données.

---

## Intégration de la classification des données

Les mesures DLP doivent être appliquées sur la base du schéma de classification des données de l'organisation. La classification détermine le mode d'application, la couverture des canaux et la priorité de réponse pour chaque catégorie de données.

**Protection DLP basée sur la classification** :

| Niveau de classification | Exigence DLP | Mode d'application |
|--------------------------|-------------|-------------------|
| **Restreint** | Surveillance et blocage DLP complets sur tous les canaux de sortie | Blocage et alerte |
| **Confidentiel** | Surveillance et blocage DLP sur les canaux à risque élevé (courriel, web, terminal, cloud) | Blocage ou demande de justification à l'utilisateur |
| **Interne** | Surveillance DLP sur les principaux canaux de sortie (courriel, web) | Surveillance et alerte (détection sans blocage automatique) |
| **Public** | Aucun contrôle DLP requis | Sans objet |

**Catégories de données sensibles nécessitant une protection DLP** :

| Catégorie de données | Exemples | Fondement réglementaire |
|----------------------|----------|------------------------|
| **Données personnelles (DCP)** | Noms, adresses, numéros nationaux d'identification, numéros AVS, numéros de téléphone | nLPD suisse, RGPD (le cas échéant) |
| **Données des employés** | Dossiers RH, salaires, évaluations de performance, informations de santé | nLPD suisse art. 328b CO |
| **Identifiants d'authentification** | Mots de passe, clés API, jetons, certificats, clés SSH | ISO 27001 A.5.17 |
| **Propriété intellectuelle** | Code source, designs, brevets, secrets commerciaux, plans stratégiques | Risque métier |
| **Données clients** | Listes de clients, contrats, tarifications, communications | Obligations contractuelles |
| **Données financières** | Numéros de compte bancaire, données de paiement, états financiers | Risque métier, contractuel |

**Méthodes d'identification des données** :

L'organisation devrait mettre en œuvre plusieurs méthodes d'identification pour détecter les informations sensibles en transit :

- **Inspection du contenu** : Correspondance de motifs, expressions régulières et détection de mots-clés pour les données structurées (p. ex. numéros de carte de crédit, numéros nationaux d'identification, numéros AVS).
- **Étiquetage des documents** : Métadonnées de classification intégrées dans les fichiers (en-têtes, pieds de page, propriétés) permettant au DLP d'identifier les documents sensibles indépendamment du contenu.
- **Analyse contextuelle** : Évaluation du système source, du rôle de l'utilisateur, de la destination, du volume de transfert et de l'heure pour évaluer le niveau de risque.
- **Empreinte digitale** (recommandé) : Suivi par hachage pour les documents à valeur élevée tels que le code source, les spécifications de conception et les plans stratégiques.

L'organisation devrait maintenir un inventaire des données sensibles nécessitant une protection DLP, réconcilié trimestriellement avec l'inventaire des actifs (A.5.9). Les motifs de détection spécifiques, les règles d'expressions régulières et les étiquettes de classification doivent être documentés et maintenus par l'équipe de sécurité.

---

## Protection des canaux

L'organisation devrait mettre en œuvre des mesures DLP sur tous les canaux de sortie des données pour prévenir la divulgation non autorisée d'informations. La couverture des canaux doit être vérifiée par des tests techniques au moins trimestriellement.

### Protection des courriels

Tous les courriels sortants (SMTP et webmail) doivent faire l'objet d'une inspection DLP du contenu :

- Scanner le corps des messages et les pièces jointes pour détecter le contenu sensible correspondant aux règles de détection DLP.
- Valider les domaines des destinataires : distinguer les destinataires internes, externes de confiance et externes non fiables.
- Bloquer ou mettre en quarantaine les messages contenant des données Restreintes vers des destinataires externes.
- Alerter sur les données Confidentielles vers des destinataires externes (blocage ou demande à l'utilisateur selon la classification et la destination).
- Prendre en charge le chiffrement (S/MIME, TLS) pour les courriels sensibles approuvés lorsque le besoin métier existe.
- Surveiller les services webmail dans le navigateur (p. ex. Gmail, Outlook.com, Yahoo Mail) pour empêcher le contournement des contrôles DLP basés sur SMTP.

### Protection des canaux web et cloud

Les canaux de sortie de données via le web doivent être surveillés et contrôlés :

- **Envois web** : Surveiller et contrôler les envois de fichiers vers des services de stockage cloud (p. ex. Dropbox, Google Drive, comptes OneDrive personnels). Le stockage cloud d'entreprise approuvé [Plateforme de stockage cloud] doit être distingué des services personnels ou non approuvés.
- **Applications cloud** : Intégrer [CASB] (Courtier en sécurité d'accès au cloud) ou équivalent pour la surveillance des applications SaaS (p. ex. Microsoft 365, Google Workspace). Surveiller le partage de données, la collaboration externe et les transferts cloud à cloud.
- **Formulaires web** : Surveiller les activités de collage et de saisie sur les formulaires web externes selon l'évaluation des risques.
- **Inspection TLS** : Lorsque légalement autorisé et techniquement faisable, inspecter le trafic web chiffré à la passerelle internet pour détecter le contenu sensible dans les envois HTTPS. L'inspection TLS doit être conforme aux exigences de confidentialité et documentée dans l'avis de confidentialité de l'organisation.

### Protection des terminaux

Les mesures DLP sur les terminaux doivent être déployées sur tous les appareils gérés :

- **Supports amovibles** : Surveiller et contrôler les transferts de fichiers vers les clés USB, disques durs externes, cartes SD et autres supports amovibles. Bloquer l'utilisation non autorisée de supports amovibles pour les données Restreintes et Confidentielles. Les supports amovibles approuvés (p. ex. clés USB d'entreprise chiffrées) doivent être documentés.
- **Stockage local** : Surveiller les opérations d'écriture de fichiers sur le disque local, les partages réseau et le stockage hors ligne pour les données sensibles.
- **Impression** : Surveiller les travaux d'impression pour les données Restreintes. Les activités d'impression en PDF et d'imprimante virtuelle doivent être incluses dans le périmètre de surveillance.
- **Captures d'écran et presse-papiers** (basé sur les risques) : Lorsque l'évaluation des risques le justifie, surveiller les outils de capture d'écran et les opérations de presse-papiers pour les données Restreintes. Ce contrôle doit être appliqué uniquement à des rôles ou ensembles de données spécifiques à risque élevé, et non à l'ensemble de l'organisation.
- **Application hors ligne** : Les agents DLP sur les terminaux doivent appliquer les politiques lorsque l'appareil est déconnecté du réseau d'entreprise.
- **Détection du Shadow IT** : Détecter les applications non approuvées de stockage cloud, de messagerie et de partage de fichiers installées sur les terminaux gérés.

### Protection réseau

Les mesures DLP au niveau réseau doivent surveiller les flux de données aux points de sortie :

- Surveiller le trafic réseau aux passerelles internet et aux points de connexion cloud.
- Surveiller les protocoles de transfert de fichiers (FTP, SFTP, SCP, rsync) pour les transferts de données sensibles.
- Détecter l'exfiltration de données via des canaux dissimulés (tunnellisation DNS, exfiltration ICMP, stéganographie) lorsque l'évaluation des menaces identifie ce risque.
- Intégrer les alertes DLP avec le pare-feu, le proxy et le [SIEM] pour corrélation et investigation.

### Protection des appareils mobiles

Les données d'entreprise sur les appareils mobiles doivent être protégées :

- Intégrer les mesures DLP avec [MDM] (Gestion des appareils mobiles) pour appliquer les politiques de protection des données sur les appareils mobiles d'entreprise.
- Cloisonner les applications et données d'entreprise sur les appareils BYOD pour empêcher les fuites de données vers des applications personnelles.
- Surveiller le partage de courriels et de documents depuis les appareils mobiles.
- Appliquer des politiques d'accès conditionnel limitant l'accès aux données sensibles aux seuls appareils conformes.

### Vérification de la couverture

L'organisation devrait vérifier la couverture des canaux DLP par des tests techniques au moins trimestriellement. Les lacunes de couverture doivent être documentées avec :

- Description de la lacune et systèmes ou utilisateurs affectés.
- Évaluation des risques liés à la lacune.
- Approbation du RSSI pour l'acceptation du risque (le cas échéant).
- Plan de remédiation avec délai (si non accepté).

Exceptions de couverture acceptables (documentées et approuvées par le RSSI) : réseaux invités sans accès aux données sensibles ; connexions B2B dédiées avec contrôles alternatifs ; réseaux isolés sans connectivité internet ; groupes d'utilisateurs spécifiques avec exceptions documentées et approuvées (p. ex. conseil juridique traitant des communications privilégiées).

---

## Gestion des prestataires de services DLP tiers

Lorsque l'organisation utilise des solutions DLP basées sur le cloud (CASB, passerelle de sécurité courriel en tant que service, plateformes DLP cloud) :

### Critères de sélection des fournisseurs

Les prestataires de services DLP doivent être évalués selon les critères suivants :

| Critère | Exigence | Méthode de validation |
|---------|----------|----------------------|
| **Certifications de sécurité** | SOC 2 Type II (actuel, dans les 12 mois) ; ISO 27001 | Demander et examiner les rapports annuellement |
| **Résidence des données** | Données traitées et stockées en Suisse ou dans l'UE/EEE (ou juridiction d'adéquation selon la nLPD) | Confirmer dans le contrat ; vérifier dans le rapport SOC 2 |
| **Conformité à la protection des données** | Accord de traitement des données conforme au RGPD ; engagement de conformité nLPD | Examen juridique du ATD |
| **Précision de détection** | Taux de faux positifs < 10 % lors de l'essai ; taux de détection > 95 % pour les jeux de données de test connus | Preuve de concept de 30 jours avec échantillon de trafic de production |
| **Performance** | Latence courriel < 500 ms ; latence proxy web < 100 ms (mode en ligne) | Tests de charge lors de l'essai |
| **Capacités d'intégration** | Intégration API avec [SIEM], [ITSM], fournisseur d'identité | Validation technique lors du POC |
| **Réponse aux incidents** | Le fournisseur assure un support 24h/7j ; délai de réponse < 1 heure pour les alertes critiques | Conditions SLA ; vérifications de références |

### Exigences de l'accord de traitement des données

Les contrats avec les fournisseurs DLP cloud doivent inclure :

- **Obligations du sous-traitant** (nLPD art. 9 ; RGPD art. 28 le cas échéant)
- **Divulgation et approbation des sous-traitants ultérieurs** (liste des sous-traitants ; notification des changements)
- **Conservation et suppression des données** (suppression automatique après la période de conservation ; confirmation de suppression sur demande)
- **Notification d'incident de sécurité** (le fournisseur notifie l'organisation dans les 24 heures de toute violation affectant les données clients)
- **Droits d'audit** (l'organisation ou l'auditeur peut auditer les contrôles du fournisseur ; le rapport SOC 2 est satisfaisant s'il est à jour)
- **Portabilité des données** (export des journaux et politiques DLP dans un format standard à la résiliation)
- **Juridiction et droit applicable** (droit suisse préféré ; droit de l'UE acceptable ; litiges en Suisse)

### Surveillance continue des performances des fournisseurs

| Mesure | Cible | Fréquence de révision | Responsable |
|--------|-------|----------------------|-------------|
| **Disponibilité du service** | Selon SLA fournisseur (généralement 99,5–99,9 %) | Mensuel | Opérations IT |
| **Taux de faux positifs** | < 10 % | Mensuel | Équipe de sécurité |
| **Précision de détection** | > 95 % pour les scénarios de test | Trimestriel | Équipe de sécurité |
| **Performance (latence)** | Selon cibles ci-dessus | Hebdomadaire | Opérations IT |
| **Réactivité du support** | Selon SLA (critique : < 1h ; élevé : < 4h ; moyen : < 24h) | Par ticket | Responsable équipe sécurité |
| **Incidents de sécurité du fournisseur** | 0 affectant les données clients | Par occurrence | RSSI |

### Révision annuelle des fournisseurs

Les fournisseurs DLP cloud doivent faire l'objet d'une révision annuelle couvrant :

- **Examen du rapport SOC 2 Type II** : Comparer le rapport actuel avec le précédent ; identifier toute nouvelle exception ou réserve ; vérifier que l'environnement de contrôle reste acceptable.
- **Performance par rapport aux SLA** : Disponibilité, latence, délais de réponse du support.
- **Tendances des faux positifs** : En amélioration, stables ou se dégradant ?
- **Incidents de sécurité** : Violations ou quasi-accidents côté fournisseur au cours des 12 derniers mois ?
- **Alignement de la feuille de route** : La direction technologique du fournisseur est-elle alignée sur les besoins de l'organisation ?
- **Rapport coût-bénéfice** : Valeur livrée par rapport au coût de l'abonnement ; comparaison avec les alternatives.
- **Recommandation** : Renouveler, renégocier ou remplacer.

**Documentation de révision** : Conservée 3 ans ; décisions de renouvellement documentées avec justification.

### Escalade d'incident fournisseur

Si un fournisseur DLP cloud subit un incident de sécurité affectant l'organisation :

1. **Notification immédiate** : Le fournisseur doit notifier l'organisation dans les 24 heures (selon contrat).
2. **Évaluation de l'impact** : L'équipe de sécurité évalue l'impact sur l'organisation et les clients.
3. **Notification des clients** : Si les données clients sont affectées, notifier les clients conformément aux engagements de service.
4. **Notification réglementaire** : Si des données personnelles sont affectées et répondent aux critères de violation (nLPD art. 24), notifier le PFPDT.
5. **Examen des mesures correctives du fournisseur** : Le fournisseur fournit une analyse des causes profondes et un plan de remédiation dans les 10 jours ouvrables.
6. **Examen du contrat** : Évaluer si l'incident constitue une violation substantielle ; envisager le remplacement du fournisseur.

**Documentation des incidents fournisseurs** : Conservée 5 ans minimum ; incluse dans la révision annuelle des fournisseurs.

---

## Surveillance et détection

L'organisation devrait mettre en œuvre une surveillance continue pour détecter les tentatives de fuite de données et les violations de politique.

**Modes de détection** :

| Mode | Description | Cas d'usage |
|------|-------------|-------------|
| **Surveillance uniquement** | Journaliser et alerter sans bloquer | Phase de déploiement initiale, canaux à faible risque, période d'ajustement |
| **Demande à l'utilisateur** | Demander une justification avant d'autoriser le transfert | Transferts de données Confidentielles vers des destinataires externes |
| **Blocage** | Empêcher le transfert et alerter l'équipe de sécurité | Données Restreintes vers des destinations non fiables, fuite d'identifiants |
| **Quarantaine** | Mettre le transfert en attente pour examen par l'équipe de sécurité | Exfiltration malveillante suspectée, cas ambigus |

**Priorité des alertes et délais de réponse** :

| Priorité | Exemples de déclencheurs | Délai de réponse |
|----------|--------------------------|------------------|
| **Critique** | Données Restreintes exfiltrées vers l'extérieur ; fuite d'identifiants ; transfert en masse de grande volumétrie | Immédiat (< 15 minutes) |
| **Élevé** | Données Confidentielles vers un domaine non fiable ; violation de politique d'un utilisateur privilégié ; violations répétées | < 1 heure |
| **Moyen** | Données Confidentielles vers une partie externe approuvée ; transfert de fichiers en masse dans un contexte métier normal | < 4 heures |
| **Faible** | Données Internes vers l'extérieur ; alertes informatives ; candidats à un faux positif | < 24 heures |

**Journalisation des événements DLP** :

Tous les événements DLP doivent être journalisés avec les informations suivantes :

- Horodatage (UTC, format ISO 8601).
- Identité de l'utilisateur (nom d'utilisateur, identifiant employé).
- Système source (nom d'hôte, adresse IP, identifiant de l'appareil).
- Destination (courriel du destinataire, URL, service externe, identifiant du support amovible).
- Classification des données déclenchée (Restreint, Confidentiel, Interne).
- Méthode de détection (inspection du contenu, étiquetage, analyse contextuelle).
- Action entreprise (bloqué, autorisé, mis en quarantaine, justifié par l'utilisateur).
- Extrait de données (100 premiers caractères ou extrait assaini — limité à ce qui est nécessaire à l'investigation, conformément aux exigences de confidentialité).

**Conservation des journaux** :

- Événements de sécurité DLP (transferts bloqués, violations de politique, alertes critiques) : 12 mois minimum.
- Journaux opérationnels DLP (transferts autorisés, événements informatifs) : 90 jours minimum.
- Conservation prolongée lorsque les exigences réglementaires imposent des périodes plus longues.
- Journaux protégés par des contrôles d'intégrité et de confidentialité conformément à A.8.15.

**Analyse comportementale** (recommandé) : Lorsque l'organisation déploie une analyse comportementale des utilisateurs et des entités (UEBA), les données DLP doivent être corrélées avec l'activité de référence des utilisateurs pour détecter des schémas de transfert anormaux (p. ex. volume inhabituel, destination inhabituelle, heure inhabituelle). L'analyse comportementale doit être conforme aux exigences légales en matière de surveillance des employés définies dans la présente politique.

**Intégration du renseignement sur les menaces** (recommandé) : Les systèmes DLP devraient intégrer des flux de renseignement sur les menaces pour identifier les indicateurs d'exfiltration connus (domaines de commande et contrôle, signatures de logiciels malveillants, techniques APT documentées dans MITRE ATT&CK).

---

## Réponse aux incidents DLP

Les incidents de sécurité DLP doivent suivre le processus de gestion des incidents de l'organisation (A.5.24-28) avec les exigences spécifiques DLP suivantes.

**Classification des incidents DLP** :

| Gravité | Indicateurs | Actions initiales |
|---------|-------------|-------------------|
| **Critique** | Données Restreintes confirmées exfiltrées ; identifiants fuités vers l'extérieur ; indicateurs de menace interne ; schémas d'exfiltration APT | Bloquer l'utilisateur ; isoler le terminal ; notifier le RSSI et le DPD ; initier la réponse aux incidents |
| **Élevé** | Données Confidentielles vers un destinataire non fiable ; transfert en masse de données sensibles ; violations répétées par le même utilisateur | Bloquer le transfert ; investiguer l'activité de l'utilisateur ; escalader au responsable de l'équipe de sécurité |
| **Moyen** | Données Confidentielles vers une partie externe approuvée via un canal non approuvé ; erreur humaine avec exposition limitée | Contenir le transfert ; interroger l'utilisateur ; évaluer la portée ; remédier |
| **Faible** | Faux positif ; ajustement de règle DLP requis ; clarification nécessaire avec l'utilisateur | Journaliser ; affiner la règle DLP ; communiquer avec l'utilisateur si nécessaire |

**Flux de travail de réponse** :

1. **Détection** : Le système DLP génère une alerte sur la base d'une violation de politique.
2. **Triage** : L'équipe de sécurité classe la gravité de l'incident, détermine la portée et initie le confinement.
3. **Confinement** : Bloquer le compte utilisateur, isoler le terminal, révoquer les identifiants ou mettre le transfert en quarantaine selon le cas.
4. **Investigation** : Analyse des causes profondes (malveillant ou accidentel), détermination de la portée (volume de données, sensibilité, destinataires, durée d'exposition), collecte de preuves légales.
5. **Éradication** : Rotation des identifiants (si identifiants fuités), remédiation des logiciels malveillants (si exfiltration via malware), révocation des accès.
6. **Rétablissement** : Reprendre les opérations normales, ajuster la politique DLP, réactiver l'utilisateur avec les contrôles appropriés.
7. **Revue post-incident** : Retour d'expérience (dans les 30 jours), ajustement de la politique DLP, recommandations d'amélioration des contrôles.

**Notification réglementaire en cas de violation** :

Lorsque des incidents DLP constituent des violations de données personnelles, l'organisation doit respecter les exigences de notification :

| Réglementation | Exigence | Délai |
|---------------|----------|-------|
| **nLPD suisse** | Art. 24 — Notifier le PFPDT si la violation présente un risque élevé pour les personnes concernées | Sans délai indu |
| **RGPD UE** (le cas échéant) | Art. 33 — Notifier l'autorité de contrôle | 72 heures |
| **Personnes concernées RGPD** | Art. 34 — Notifier les personnes si risque élevé | Sans délai indu |

Le délégué à la protection des données (DPD) ou le responsable désigné de la protection de la vie privée doit être consulté pour tous les incidents DLP impliquant des données personnelles afin de déterminer les obligations de notification de violation.

**Intégration DLP-gestion des incidents** : Les événements DLP de gravité Critique et Élevée doivent automatiquement créer des tickets d'incident dans [Plateforme ITSM] (p. ex. ServiceNow, Jira Service Management ou équivalent). Les tickets non acquittés dans le délai SLA de réponse doivent s'escalader automatiquement conformément aux procédures de gestion des incidents.

---

## Exigences légales en matière de surveillance des employés

La surveillance DLP constitue une forme de surveillance des employés en droit suisse. L'organisation doit se conformer aux exigences légales suivantes avant de déployer et d'exploiter des contrôles DLP.

### Cadre légal suisse

**Art. 26 OLT 3 (Ordonnance 3 relative à la loi sur le travail)** : Les systèmes de surveillance et de contrôle ne doivent pas être utilisés si leur seul ou principal objectif est de surveiller le comportement des employés. Les systèmes DLP sont autorisés parce que leur objectif principal est de protéger les données de l'organisation contre la divulgation non autorisée — et non de surveiller la conduite individuelle des employés. Cependant, la mise en œuvre DLP doit démontrablement servir un objectif de protection des données, et toute surveillance incidente du comportement des employés doit être proportionnée.

**Art. 328b CO (Code des obligations suisse)** : L'employeur ne peut traiter les données concernant ses employés que dans la mesure où elles portent sur leurs aptitudes à remplir leurs fonctions ou sont nécessaires à l'exécution du contrat de travail. Les données de surveillance DLP ne doivent être traitées qu'à des fins de sécurité de l'information. Les données DLP ne doivent pas être utilisées pour :

- L'évaluation des performances des employés ou leur classement.
- Le suivi du temps de travail et des présences.
- La surveillance de la navigation personnelle ou des communications.
- Toute fin non liée à la sécurité des données et à la prévention des fuites.

**Principes nLPD (LPD) suisse** :

- **Licéité** : La surveillance DLP doit avoir un fondement légitime (la protection des données de l'organisation est un intérêt légitime).
- **Proportionnalité** : Le périmètre de surveillance doit se limiter à ce qui est nécessaire à la protection des données. L'organisation ne doit pas surveiller plus largement que requis.
- **Limitation de la finalité** : Les données collectées via DLP ne doivent être utilisées qu'à des fins de sécurité, sans être réaffectées à d'autres objectifs.
- **Transparence** : Les employés doivent être informés de la surveillance DLP avant son activation.

### Exigences RGPD UE (le cas échéant)

Lorsque l'organisation traite des données de personnes dans l'UE/EEE :

- **Art. 6(1)(f) Intérêt légitime** : La surveillance DLP repose sur l'intérêt légitime de protéger les données de l'organisation, mis en balance avec les droits à la vie privée des employés.
- **Art. 32 Sécurité du traitement** : Les mesures DLP constituent une mesure technique appropriée pour protéger les données personnelles.
- **Art. 88 Traitement dans le contexte de l'emploi** : La surveillance DLP doit être conforme au droit du travail national de chaque juridiction de l'UE où l'organisation opère.

### Évaluation de la proportionnalité

L'organisation devrait conduire une évaluation de la proportionnalité avant de déployer des contrôles DLP. L'évaluation doit vérifier que :

**Proportionné (autorisé)** :
- Surveiller les canaux de sortie pour les schémas de données sensibles (pièces jointes de courriel, envois web, transferts USB).
- Journaliser les alertes DLP avec une conservation limitée (90 jours en routine, 12 mois pour les événements de sécurité).
- Restreindre l'accès aux journaux DLP à l'équipe de sécurité, au RSSI et au DPD sur une base du besoin d'en connaître.
- Déployer en mode surveillance uniquement initialement avant d'activer le blocage.
- Limiter les extraits de données dans les journaux au strict minimum nécessaire à l'investigation.

**Disproportionné (non autorisé)** :
- Enregistrer l'intégralité du contenu des courriels indéfiniment quelle que soit leur sensibilité.
- Surveiller l'ensemble de l'activité de navigation web sans limitation fondée sur les risques.
- Enregistrement des frappes clavier ou enregistrement continu d'écran sans justification documentée spécifique.
- Permettre aux RH ou aux responsables hiérarchiques de consulter les alertes DLP à des fins d'évaluation des performances.
- Surveiller les appareils personnels pour des activités non professionnelles.
- Utiliser les données DLP pour l'évaluation des employés ou des mesures disciplinaires sans rapport avec la sécurité des données.

### Exigences de transparence

L'organisation devrait informer tous les employés de la surveillance DLP par les moyens suivants :

1. **Contrats de travail ou avenants** : Déclaration claire que la surveillance DLP est en place, son périmètre, son objectif et ses durées de conservation des données.
2. **Avis de confidentialité / manuel de l'employé** : Explication détaillée de ce qui est surveillé, de ce qui ne l'est pas, de l'utilisation des données et des personnes y ayant accès.
3. **Politique d'utilisation acceptable** : Interdiction explicite de l'exfiltration de données, exemples d'activités interdites, conséquences des violations et processus d'exception.
4. **Formation de sensibilisation à la sécurité** : Module de formation annuel couvrant l'objectif DLP, les responsabilités des utilisateurs, les demandes d'exception et le signalement.
5. **Consultation du comité d'entreprise** (le cas échéant) : Dans les juridictions requérant une codécision, le comité d'entreprise doit être consulté avant le déploiement de la surveillance DLP.

**Important** : L'absence de transparence peut rendre la surveillance DLP illicite. La surveillance DLP ne doit pas être activée tant que la notification des employés n'a pas été complétée et documentée. L'organisation doit conserver les preuves de notification des employés (accusés de réception signés, relevés de formation, relevés de distribution de l'avis de confidentialité).

### Risque d'application

Le non-respect des exigences en matière de surveillance des employés expose l'organisation à :

- **nLPD suisse** : Amendes jusqu'à CHF 250 000 pour violations individuelles ; mesures d'enforcement du PFPDT.
- **RGPD UE** : Amendes jusqu'à EUR 20 000 000 ou 4 % du chiffre d'affaires annuel mondial.
- **Droit du travail** : Une surveillance illicite peut constituer un fondement pour des réclamations d'employés au titre des droits de la personnalité (art. 28 CC) ; les preuves DLP obtenues illicitement peuvent être irrecevables dans des procédures disciplinaires.

---

## Sensibilisation des utilisateurs et utilisation acceptable

Tous les employés doivent être informés des mesures DLP et de leurs responsabilités.

**Responsabilités des utilisateurs** :

- Traiter les données sensibles conformément à leur classification et à la politique d'utilisation acceptable.
- Utiliser des canaux approuvés pour les transferts de données (courriel d'entreprise, stockage cloud approuvé, outils de transfert chiffrés).
- Demander des exceptions via le processus formel d'exception pour les besoins métier légitimes nécessitant de déroger à la politique DLP.
- Signaler les faux positifs et les problèmes d'utilisabilité à l'équipe de sécurité ou au service d'assistance.
- Compléter la formation annuelle de sensibilisation aux mesures DLP.

**Activités interdites** :

- Tenter de contourner les contrôles DLP via des proxys, le chiffrement de données pour éviter l'inspection, l'utilisation de services cloud non approuvés ou toute autre méthode de contournement.
- Transférer des données Restreintes ou Confidentielles vers des comptes de messagerie personnels, du stockage cloud personnel ou des services externes non approuvés.
- Désactiver ou altérer les agents DLP sur les terminaux.
- Partager des identifiants d'exception DLP ou des méthodes de transfert approuvées avec des personnes non autorisées.

Les violations de la politique DLP sont passibles de mesures disciplinaires conformément à la politique RH. Les tentatives délibérées ou répétées de contourner les contrôles DLP peuvent entraîner la résiliation du contrat de travail.

**Si les mesures DLP bloquent un transfert** :

1. Vérifier la classification des données — s'agit-il réellement de données sensibles ?
2. Utiliser une méthode de transfert approuvée (courriel d'entreprise avec chiffrement, partage cloud approuvé, transfert de fichiers sécurisé).
3. Si le transfert répond à un besoin métier légitime, soumettre une demande d'exception à l'équipe de sécurité.
4. Contacter le service d'assistance pour une assistance urgente ou pour signaler un faux positif.

---

## Performance et ajustement des mesures DLP

L'organisation devrait suivre l'efficacité des mesures DLP par des indicateurs clés de performance et affiner continuellement les règles DLP pour réduire les faux positifs tout en maintenant la couverture de détection.

**Indicateurs de performance** :

| Indicateur | Cible | Plage acceptable | Fréquence de révision |
|-----------|-------|-----------------|----------------------|
| Taux de faux positifs | < 5 % du total des alertes | < 10 % maximum | Mensuel |
| Conformité SLA de réponse aux alertes | > 95 % dans les délais cibles | > 90 % minimum | Hebdomadaire |
| Couverture des canaux (chemins de sortie critiques) | 100 % | > 95 % minimum | Trimestriel |
| Taux de détection des incidents (données Restreintes) | 100 % des tentatives d'exfiltration | > 98 % minimum | Par revue d'incident |
| Efficacité des ajustements de politique | > 20 % de réduction des FP par cycle d'ajustement | Tendance positive requise | Trimestriel |
| Problèmes signalés par les utilisateurs | < 10 par mois | < 20 maximum | Mensuel |

**Processus d'ajustement** :

- **Mensuel** : L'équipe de sécurité examine les tendances des faux positifs et ajuste les règles de détection.
- **Trimestriel** : Révision complète de l'efficacité des règles DLP, des lacunes de couverture et des nouveaux types de données.
- **Par incident** : La revue post-incident identifie les améliorations des règles de détection et les améliorations de couverture.
- **Annuel** : Révision complète du programme DLP dans le cadre de la revue de direction (ISO 27001 Clause 9.3), incluant l'évaluation technologique et l'évaluation des fournisseurs.

**Réponse en dessous des cibles** : Si les indicateurs sont en dessous de la plage acceptable pendant deux périodes de mesure consécutives, le RSSI doit conduire une analyse des causes profondes dans les 30 jours, mettre en œuvre un plan d'action correctif et rendre compte de l'état de remédiation à la direction générale.

---

## Disponibilité du système DLP et impact sur les performances

Les systèmes DLP qui introduisent de la latence, bloquent des opérations métier légitimes ou tombent en panne d'une manière qui perturbe les services peuvent nuire aux engagements de disponibilité de l'organisation.

### Exigences de disponibilité du système DLP

| Composant | Cible de disponibilité | Impact en cas de panne | Basculement/Redondance |
|-----------|----------------------|----------------------|----------------------|
| **Passerelle DLP courriel** | 99,5 % | Retards ou pannes de distribution de courriels | Paire haute disponibilité ; option de passage en mode ouvert pour les classifications non critiques |
| **Proxy DLP web** | 99,5 % | Dégradation ou blocage de l'accès web | Proxys redondants ; passage en mode ouvert avec journalisation pour les données non Restreintes |
| **Agents DLP sur terminaux** | 99 % (par terminal) | Application hors ligne uniquement ; pas de synchronisation réseau | Les agents maintiennent l'application hors ligne ; alerte en cas de déconnexion prolongée (> 72h) |
| **Capteurs DLP réseau** | 99 % | Perte de visibilité ; pas de capacité de blocage au niveau réseau | Surveillance passive ; ne rompt pas la connectivité |
| **DLP cloud (CASB)** | 99,5 % (SLA fournisseur) | L'accès au service cloud peut se dégrader si en ligne ; le mode API continue | Redondance fournie par le fournisseur ; configuration mode en ligne vs. API |

### Modes de sécurité passive

Les systèmes DLP doivent être configurés avec un comportement de sécurité passive explicite pour prévenir toute perturbation des services :

| Scénario | Comportement de sécurité passive | Justification |
|----------|--------------------------------|---------------|
| **Panne de la passerelle DLP courriel** | Passage en mode ouvert pour les données Internes et Confidentielles (distribution continue avec journalisation) ; fermeture pour les données Restreintes (courriel mis en file d'attente jusqu'à rétablissement) | Équilibrer disponibilité vs. sécurité selon la sensibilité des données |
| **Panne du proxy DLP web** | Passage en mode ouvert avec journalisation complète ; alertes générées pour tout le trafic pendant la période de mode ouvert | Maintenir la continuité des activités ; investiguer l'activité pendant la fenêtre de panne |
| **Crash de l'agent DLP sur terminal** | Continuer l'application hors ligne des politiques ; alerter les opérations IT pour remédiation | Maintenir la protection de base ; rétablir la surveillance complète dès que possible |
| **Panne de la base de données/console de gestion DLP** | Les agents continuent avec la dernière politique connue valide ; pas de nouvelles règles déployées jusqu'au rétablissement | Empêcher la perte d'application des politiques |

### Surveillance des performances

Les performances du système DLP doivent être surveillées pour prévenir toute dégradation des services :

| Indicateur | Cible | Seuil d'alerte | Fréquence de révision |
|-----------|-------|---------------|----------------------|
| **Latence de traitement des courriels** | < 500 ms par message | > 2 secondes en continu pendant 5 minutes | Surveillance en temps réel |
| **Latence du proxy web** | < 100 ms de latence ajoutée | > 300 ms en continu pendant 5 minutes | Surveillance en temps réel |
| **Utilisation CPU de l'agent terminal** | < 5 % en moyenne | > 15 % en continu pendant 10 minutes | Surveillance horaire |
| **Utilisation mémoire de l'agent terminal** | < 200 Mo | > 500 Mo | Surveillance horaire |
| **Taux de faux positifs impactant la productivité** | < 5 % des utilisateurs signalant des blocages sur des activités légitimes | > 10 % de réclamations utilisateurs par mois | Analyse mensuelle des retours utilisateurs |
| **Disponibilité du système DLP** | Selon cibles ci-dessus | < 99 % dans tout mois calendaire | Révision mensuelle SLA |

### Planification de capacité

- Les systèmes DLP doivent être dimensionnés pour gérer le trafic de pointe avec 30 % de marge.
- Une révision annuelle de la capacité doit projeter la croissance et identifier les besoins de mise à l'échelle.
- Volumes de courriels, trafic web, nombre de terminaux et volumes de transfert de données suivis trimestriellement.
- Alertes de capacité déclenchées à 70 % d'utilisation ; mise à niveau planifiée avant 85 % d'utilisation.

### Impact des incidents sur les services

Les incidents DLP peuvent impacter la disponibilité des services via les actions de confinement :

| Action de confinement | Impact sur les services | Atténuation |
|----------------------|------------------------|-------------|
| **Désactivation du compte utilisateur** (menace interne) | L'utilisateur ne peut plus travailler ; les services peuvent continuer pour les autres utilisateurs | Investigation rapide (< 1 heure) pour déterminer si un blocage total est justifié ou si une restriction partielle suffit |
| **Terminal isolé** (exfiltration en cours) | L'utilisateur ne peut pas accéder au réseau ; les services cloud peuvent rester accessibles | Fournir un appareil de remplacement propre si l'investigation dépasse 4 heures |
| **Identifiant de compte de service révoqué** (clé API fuitée) | Une application ou intégration peut tomber en panne | Coordonner avec le propriétaire de l'application ; générer de nouveaux identifiants ; tester avant révocation si possible |
| **Segment réseau mis en quarantaine** (exfiltration en masse) | Plusieurs utilisateurs affectés | Rare ; nécessite l'approbation du RSSI ; notification aux clients si les services externes sont impactés |

**Notification aux clients** : Si les actions de confinement DLP impactent les services destinés aux clients, ceux-ci doivent être notifiés conformément aux procédures de communication d'incident (généralement dans l'heure pour les incidents impactant les clients).

### Continuité des activités et reprise après sinistre

Les contrôles DLP doivent soutenir les objectifs de continuité des activités et de reprise après sinistre de l'organisation :

#### Mesures DLP dans les scénarios de reprise après sinistre

Lorsque l'organisation active ses procédures de reprise après sinistre :

| Scénario DR | Application DLP | Justification |
|-------------|----------------|---------------|
| **Panne du datacenter principal ; basculement vers le site DR** | Application DLP complète maintenue (DLP du site DR configuré de manière identique au site principal) | Les exigences de protection des données restent inchangées |
| **Panne du système de messagerie ; utilisation d'urgence d'un courriel alternatif** | Le DLP courriel s'applique au système alternatif ; si techniquement impossible, surveillance renforcée et revue manuelle | Prévenir les fuites pendant la perturbation |
| **Panne d'infrastructure réseau ; connectivité alternative temporaire** | Le DLP réseau peut être réduit ; le DLP sur terminaux devient le contrôle principal | Les agents sur terminaux maintiennent l'application pendant la perturbation réseau |
| **Incident de rançongiciel ; segments réseau isolés** | Le DLP peut être temporairement contourné pour l'isolation/remédiation ; supervision manuelle renforcée et revue post-incident | La réponse sécuritaire prime ; des contrôles manuels se substituent |

#### Priorités de rétablissement du système DLP

Les systèmes DLP doivent être inclus dans la planification de reprise après sinistre avec des priorités de rétablissement définies :

| Composant DLP | Objectif de délai de rétablissement (ODR) | Objectif de point de rétablissement (OPR) | Niveau de priorité |
|---------------|------------------------------------------|------------------------------------------|-------------------|
| **DLP courriel** | 4 heures (critique pour les opérations métier) | 1 heure (changements de politique/règle) | Niveau 1 |
| **Agents DLP sur terminaux** | N/A (fonctionnent de façon indépendante) | 24 heures (synchronisation de politique) | Niveau 2 (déploiement de politique) |
| **DLP réseau** | 8 heures (surveillance ; pas de blocage) | 24 heures (journaux) | Niveau 2 |
| **Console de gestion DLP** | 24 heures (pour les changements de politique) | 4 heures (configuration) | Niveau 2 |
| **CASB / DLP cloud** | Géré par le fournisseur (selon SLA fournisseur) | Géré par le fournisseur | Niveau 1 (responsabilité du fournisseur) |

#### Assouplissement temporaire des politiques DLP

Dans des circonstances exceptionnelles (incident majeur, reprise après sinistre, opérations d'urgence), un assouplissement temporaire des politiques DLP peut être autorisé :

- **Approbation requise** : RSSI + DSI (ou PDG si les deux sont indisponibles).
- **Documentation** : Exception documentée avec justification, mesures compensatoires, durée.
- **Mesures compensatoires** : Revue manuelle renforcée, limitée à des utilisateurs/types de données spécifiques, durée limitée dans le temps.
- **Durée maximale** : 72 heures ; nécessite une nouvelle approbation pour prolongation.
- **Piste d'audit** : Toute activité pendant la période d'assouplissement journalisée et révisée post-incident.

**Exemple de scénario** : Lors d'une reprise après rançongiciel, l'équipe IT doit transférer de grands volumes de données vers un service de sauvegarde cloud normalement non approuvé. Le DLP autorise temporairement ce transfert spécifique avec journalisation renforcée et supervision de l'équipe de sécurité.

#### Tests DR annuels

Les systèmes DLP doivent être inclus dans les tests annuels de reprise après sinistre :
- Vérifier que l'application DLP est maintenue lors du basculement vers le site DR.
- Tester le rétablissement du système DLP dans le délai ODR.
- Valider la synchronisation des politiques après rétablissement.
- Documenter les résultats des tests et les lacunes pour remédiation.

---

## Tests d'efficacité des mesures DLP

L'organisation devrait conduire des tests structurés pour valider que les contrôles DLP détectent et empêchent la divulgation non autorisée de données telle que conçue.

### Programme de tests

| Type de test | Fréquence | Méthode | Critères de succès | Responsable |
|-------------|-----------|---------|-------------------|-------------|
| **Tests de détection positive** (DLP devrait bloquer) | Trimestriel | Envoyer des courriels/fichiers de test contenant des données sensibles simulées (numéros de carte de crédit de test, DCP de test, identifiants de test) vers des adresses externes ; tenter des envois web ; transferts USB | 100 % de détection et blocage pour les données Restreintes ; > 95 % pour les données Confidentielles | Équipe de sécurité |
| **Tests négatifs** (DLP devrait autoriser) | Trimestriel | Envoyer des communications métier légitimes ayant historiquement généré des faux positifs ; vérifier l'efficacité des ajustements | Taux de faux positifs < 5 % | Équipe de sécurité |
| **Vérification de couverture des canaux** | Trimestriel | Tester chaque canal surveillé (courriel, webmail, envoi cloud, USB, impression, mobile) avec des données de test | Tous les canaux dans le périmètre détectent les données de test | Équipe de sécurité |
| **Tests de tentative de contournement** | Semestriel | Tenter de contourner le DLP en utilisant des techniques courantes (chiffrement, obfuscation, canaux alternatifs, tunnellisation de protocole) | Tentatives de contournement détectées ou empêchées | Équipe de sécurité + Équipe rouge (si disponible) |
| **Tests d'impact sur les performances** | Annuel | Mesurer la latence des courriels, la latence du proxy web, l'utilisation CPU/mémoire des agents terminaux en charge de pointe | Performances dans les cibles (voir section disponibilité) | Opérations IT + Équipe de sécurité |
| **Routage des alertes et escalade** | Trimestriel | Générer une alerte critique de test ; vérifier la création du ticket d'incident, l'escalade, le délai de réponse dans les SLA | 100 % des alertes de test traitées correctement | Équipe de sécurité |

### Gestion des données de test

- **Jeux de données de test** : Maintenir une bibliothèque de fichiers de test contenant des données sensibles simulées :
  - Numéros de carte de crédit de test (utilisant des résultats d'algorithme de Luhn invalides)
  - Numéros de sécurité sociale suisse (AVS) de test avec des chiffres de contrôle invalides connus
  - DCP de test (noms, adresses, courriels de personas fictifs)
  - Identifiants de test (faux mots de passe, clés API, certificats)
- **Comptes de messagerie de test** : Maintenir des adresses de messagerie externes de test pour l'envoi/réception de messages de test.
- **Documentation des tests** : Chaque test documenté avec date, scénario de test, résultat attendu, résultat réel, succès/échec, actions de suivi.

### Tests Équipe rouge / Équipe violette

Dans la mesure des ressources disponibles, inclure le DLP dans les exercices annuels de test de sécurité :

- **Équipe rouge** : Tente l'exfiltration de données en utilisant des techniques d'adversaires réalistes (simulation de menace interne, simulation de compte compromis, schémas d'exfiltration APT).
- **Équipe bleue** (SOC/Équipe de sécurité) : Détecte et répond en utilisant les alertes DLP et d'autres systèmes de surveillance.
- **Debriefing** : Identifie les lacunes de détection DLP, les améliorations des règles et les améliorations de couverture.
- **Suivi des améliorations** : Les actions issues de l'exercice suivies via le registre des actions correctives.

**Pour les organisations sans capacité d'équipe rouge** : Les exercices sur table simulant des scénarios d'exfiltration de données constituent une alternative acceptable. Les scénarios devraient couvrir :
- Menace interne (employé mécontent exfiltrant des données clients)
- Compte compromis (attaquant utilisant des identifiants volés pour exfiltrer des données)
- Divulgation accidentelle (utilisateur envoyant des données sensibles au mauvais destinataire)
- Attaque de la chaîne d'approvisionnement (système tiers utilisé pour exfiltrer des données)

### Documentation des tests

Toutes les activités de test documentées avec :
- Date, testeur, périmètre du test.
- Scénarios de test et résultats attendus.
- Résultats réels (succès/échec, taux de détection, faux positifs).
- Lacunes identifiées et évaluation de la gravité.
- Actions correctives assignées avec dates limites et responsables.
- Validation de suivi des actions correctives.

**Les relevés de tests sont conservés 3 ans ; les échecs de tests sont escaladés au RSSI ; les lacunes critiques sont remédiées dans les 30 jours.**

---

## Reporting de gestion et supervision

L'efficacité et la conformité du programme DLP doivent être rapportées à la direction générale pour démontrer la gouvernance et la supervision.

### Tableau de bord trimestriel pour la direction

Le RSSI doit fournir un résumé trimestriel du programme DLP à la direction générale couvrant :

| Section | Indicateurs inclus | Objectif |
|---------|--------------------|----------|
| **État du programme** | Couverture des canaux % ; exceptions actives ; tendance du taux de faux positifs | Santé globale du programme |
| **Détection des menaces** | Incidents Critiques/Élevés détectés ; tentatives d'exfiltration bloquées ; indicateurs de menace interne | Démontrer la valeur livrée |
| **Conformité** | Achèvement de la notification des employés ; évaluation de proportionnalité à jour ; exigences réglementaires respectées | Assurance juridique/réglementaire |
| **Performance** | Disponibilité % ; tendance des faux positifs ; réclamations utilisateurs | Efficacité opérationnelle |
| **Amélioration continue** | Actions d'ajustement des politiques entreprises ; lacunes de couverture remédiées ; résultats des tests | Maturité du programme |

### Revue annuelle de direction

Dans le cadre de la Revue de direction ISO 27001 (Clause 9.3), le RSSI doit présenter une revue annuelle du programme DLP couvrant :

- **Efficacité du programme** : Les mesures DLP ont-elles prévenu des violations de données ? Incidents détectés vs. manqués.
- **Conformité** : Conformité au droit suisse du travail ; conformité à la protection des données ; constatations d'audit.
- **Évaluation technologique** : La technologie DLP actuelle est-elle adéquate ? Performance des fournisseurs ? Lacunes nécessitant un investissement ?
- **Évolution du paysage des risques** : Nouvelles menaces d'exfiltration ; nouveaux types de données à protéger ; nouveaux canaux de sortie.
- **Budget et ressources** : Les effectifs actuels sont-ils suffisants ? Besoins de renouvellement technologique ? Exigences de formation ?
- **Recommandations stratégiques** : Améliorations du programme ; modifications de politique ; priorités d'investissement.

**Documentation de révision** : Conservée 3 ans ; décisions de direction et actions suivies.

### Reporting au conseil d'administration (le cas échéant)

Pour les organisations disposant de comités d'audit ou d'une supervision des risques au niveau du conseil, un résumé annuel DLP est fourni couvrant :

- Efficacité générale du programme (incidents critiques, état de conformité réglementaire).
- Incidents DLP significatifs et enseignements tirés.
- Risques réglementaires et posture de conformité (droit du travail, droit de la protection des données).
- Investissements stratégiques et progression de la maturité du programme.
- Benchmark par rapport aux pairs du secteur (si disponible).

**Reporting au conseil conservé 7 ans minimum (relevés de gouvernance d'entreprise).**

---

## Gestion des exceptions

Les exceptions aux exigences de la politique DLP doivent être demandées par écrit et doivent inclure :

- Exigence(s) spécifique(s) nécessitant une exception.
- Justification métier et description du cas d'usage.
- Évaluation des risques (probabilité de fuite de données, impact en cas de fuite).
- Mesures compensatoires (chiffrement, surveillance renforcée, périmètre limité, accès limité dans le temps).
- Durée d'exception demandée (maximum 12 mois ; les transferts ponctuels peuvent être approuvés sans exception continue).

**Autorité d'approbation** :

| Type d'exception | Approbation requise |
|-----------------|---------------------|
| Transfert unique ponctuel | Responsable de l'équipe de sécurité |
| Exception individuelle utilisateur | Responsable de l'équipe de sécurité + Responsable hiérarchique |
| Exception de département ou de groupe | RSSI + Responsable de département |
| Exception de canal (désactiver la surveillance d'un canal) | RSSI + DSI |
| Exception de classification des données (réduire la protection d'une catégorie) | RSSI + Direction générale |

**Restrictions** : Les exceptions suivantes ne sont pas autorisées en aucune circonstance :

- Désactiver la protection DLP pour les données Restreintes sans mesures compensatoires.
- Contourner le DLP pour les transferts d'identifiants (mots de passe, clés API, certificats).
- Exceptions permanentes sans mesures compensatoires documentées et révision régulière.

Toutes les exceptions actives doivent être enregistrées dans le Registre des exceptions DLP (format : DLP-EX-AAAA-NNN), révisées au moins trimestriellement, et révoquées lorsque la justification métier ne s'applique plus ou que le profil de risque change.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **CASB** | Courtier en sécurité d'accès au cloud (Cloud Access Security Broker) — un point d'application des politiques de sécurité entre les consommateurs de services cloud et les fournisseurs de services cloud |
| **Inspection du contenu** | Analyse du contenu des données pour détecter les informations sensibles par correspondance de motifs, détection de mots-clés et expressions régulières |
| **Analyse contextuelle** | Évaluation du contexte de transfert de données (source, destination, rôle de l'utilisateur, volume, timing) pour évaluer le risque |
| **Fuite de données** | Divulgation non intentionnelle ou non autorisée d'informations sensibles à des parties externes ou internes non autorisées |
| **Prévention des fuites de données (DLP)** | Technologies, processus et politiques conçus pour détecter, prévenir et répondre à la divulgation non autorisée de données |
| **Mode de détection** | Mode opérationnel déterminant la réponse DLP : surveillance uniquement, demande à l'utilisateur, blocage ou quarantaine |
| **Canal de sortie** | Tout chemin de communication par lequel les données peuvent quitter le contrôle de l'organisation (courriel, web, terminal, réseau, cloud, mobile, API) |
| **Exfiltration** | Transfert non autorisé de données des systèmes de l'organisation vers des emplacements ou acteurs externes |
| **Faux négatif** | Fuite de données qui se produit malgré les contrôles DLP (contournée ou non détectée) |
| **Faux positif** | Activité métier légitime incorrectement identifiée comme une violation de politique DLP |
| **Empreinte digitale** | Suivi de documents par hachage permettant au DLP d'identifier des documents spécifiques indépendamment du nom de fichier ou des modifications de format |
| **Menace interne** | Risque de sécurité posé par des personnes ayant un accès autorisé qui causent intentionnellement ou accidentellement la divulgation de données |
| **MDM** | Gestion des appareils mobiles (Mobile Device Management) — technologie de gestion et sécurisation des appareils mobiles accédant aux données d'entreprise |
| **Proportionnalité** | Exigence légale selon laquelle la surveillance de sécurité doit être proportionnée à l'objectif légitime de sécurité et ne pas empiéter excessivement sur la vie privée des employés |
| **Quarantaine** | Mise en attente temporaire des transferts de données en attendant la révision par l'équipe de sécurité avant autorisation ou blocage permanent |
| **SIEM** | Gestion des informations et des événements de sécurité (Security Information and Event Management) — plateforme de collecte centralisée de journaux, corrélation et alertes de sécurité |
| **Inspection TLS** | Déchiffrement et rechiffrement du trafic chiffré TLS au niveau d'une passerelle réseau pour l'analyse du contenu DLP |
| **Transparence** | Obligation légale d'informer les employés sur les activités de surveillance avant leur activation |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; supervision du programme DLP ; approbation des exceptions à risque élevé et des exceptions de canal ; escalade des incidents DLP critiques à la direction générale ; révision annuelle de la politique ; propriétaire du budget pour la technologie DLP |
| **Responsable de la sécurité de l'information** | Maintenance quotidienne de la politique ; révision des exceptions ; surveillance de la sécurité et investigation des incidents ; coordination des audits ; reporting de conformité trimestriel au RSSI |
| **Délégué à la protection des données (DPD)** | Examiner la surveillance DLP pour la conformité à la proportionnalité et à la transparence ; conseiller sur les obligations de notification de violation (nLPD art. 24, RGPD art. 33/34) ; approuver le déploiement DLP du point de vue de la protection de la vie privée ; conduire ou réviser les analyses d'intérêt légitime |
| **Équipe de sécurité** | Déployer et maintenir les solutions DLP sur tous les canaux ; configurer les règles et politiques de détection ; surveiller les alertes et répondre aux incidents ; traiter les demandes d'exception ; affiner les politiques pour réduire les faux positifs ; conduire les évaluations de couverture |
| **Opérations IT / Équipe réseau** | Déployer et maintenir l'infrastructure DLP ; s'assurer que la topologie réseau prend en charge la couverture DLP (routage du trafic, points d'inspection TLS) ; maintenir la disponibilité et les performances du système DLP ; coordonner avec l'équipe de sécurité sur les changements réseau |
| **Propriétaires de données / Propriétaires de systèmes** | Classifier les données dans leur domaine ; définir les exigences de protection ; réviser les incidents DLP impliquant leurs données ; approuver les exceptions pour les transferts métier justifiés |
| **RH** | S'assurer que les contrats de travail incluent la reconnaissance de la surveillance DLP ; coordonner les mesures disciplinaires en cas de violations de politique ; soutenir les exigences de transparence (mises à jour de l'avis de confidentialité, mises à jour du manuel de l'employé) |
| **Juridique / Conformité** | Examiner les politiques DLP pour la conformité légale (droit du travail, droit de la protection des données) ; conseiller sur l'interprétation réglementaire ; soutenir les investigations d'incidents nécessitant une expertise juridique |
| **Tout le personnel** | Se conformer aux politiques DLP et aux exigences d'utilisation acceptable ; signaler les faux positifs et les problèmes d'utilisabilité ; utiliser le processus d'exception pour les besoins métier légitimes ; compléter la formation annuelle de sensibilisation DLP ; ne pas tenter de contourner les contrôles DLP |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique. **Pour les audits SOC 2 Type II**, les auditeurs testeront l'efficacité opérationnelle sur la période d'audit (généralement 12 mois).

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|-------------|
| 1 | **Inventaire des solutions DLP** avec périmètre de déploiement, couverture des canaux et informations de version | Équipe de sécurité | Maintenu en continu ; révisé trimestriellement | Durée du déploiement + 3 ans |
| 2 | **Inventaire de classification des données** avec catégories de données sensibles, règles de détection et mappages de règles DLP | Équipe de sécurité / Propriétaires de données | Maintenu en continu ; réconcilié trimestriellement avec l'inventaire des actifs | 3 ans |
| 3 | **Évaluation de couverture des canaux** avec résultats des tests par canal (courriel, web, terminal, réseau, cloud, mobile) | Équipe de sécurité | Trimestriel | 3 ans |
| 4 | **Journal des alertes et incidents DLP** (transferts bloqués, violations de politique, alertes critiques, rapports d'incidents) | Équipe de sécurité | Continu | Événements de sécurité : 12 mois ; journaux opérationnels : 90 jours |
| 5 | **Indicateurs de performance DLP** (taux de faux positifs, conformité SLA, couverture, taux de détection, efficacité des ajustements) | Équipe de sécurité / RSSI | Indicateurs mensuels ; révision trimestrielle | 3 ans |
| 6 | **Registre des exceptions DLP** (demandes, approbations, mesures compensatoires, dates d'expiration, relevés de révision) | Responsable équipe sécurité | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |
| 7 | **Évaluation de proportionnalité** documentant que la surveillance DLP est proportionnée à l'objectif de sécurité | DPD / RSSI | Avant déploiement ; révisée annuellement | Durée du déploiement + 3 ans |
| 8 | **Relevés de notification des employés** (contrats/avenants signés, distribution de l'avis de confidentialité, accusés de réception de politique d'utilisation acceptable) | RH / Juridique | Par onboarding ; annuellement pour la formation de sensibilisation | Durée d'emploi + 3 ans |
| 9 | **Relevés de complétion de la formation de sensibilisation DLP** | RSSI / RH | Annuellement | Durée d'emploi + 3 ans |
| 10 | **Relevés de réponse aux incidents DLP** (chronologie, confinement, investigation, remédiation, enseignements tirés) | Équipe de sécurité | Par incident | 3 ans |
| 11 | **Relevés de notification de violation** (notifications réglementaires déposées, notifications envoyées aux personnes concernées) | DPD / Juridique | Par incident | 7 ans |
| 12 | **Journal d'ajustement des règles DLP** (règles modifiées, réduction des faux positifs, justification, approbation) | Équipe de sécurité | Par changement | 3 ans |
| 13 | **Relevés de consultation du comité d'entreprise** (le cas échéant) | RH | Avant déploiement ; par changement de périmètre | Durée du déploiement + 3 ans |
| 14 | **Relevés de contrôle d'accès aux journaux DLP** (qui a accès, justification, relevés de révision) | Opérations IT / Équipe de sécurité | Maintenu en continu ; révisé trimestriellement | 3 ans |
| 15 | **Cartographie de protection des données clients** (contrats clients vers classification des données vers règles DLP) | Équipe de sécurité + Juridique | Par client ; révisée trimestriellement | 3 ans |
| 16 | **Relevés de notification des clients** (incidents DLP impliquant des données clients) | Équipe de sécurité + Succès client | Par incident | 7 ans |
| 17 | **Rapports de disponibilité du système DLP** (disponibilité, performance, indicateurs de capacité) | Opérations IT | Mensuel | 3 ans |
| 18 | **Résultats des tests d'efficacité DLP** (tests positifs/négatifs/contournement trimestriels) | Équipe de sécurité | Trimestriel | 3 ans |
| 19 | **Rapports SOC 2 des fournisseurs** (pour les fournisseurs DLP cloud, CASB) | Opérations IT / Équipe de sécurité | Annuel (réception du rapport fournisseur) | 3 ans |
| 20 | **Revues de performance des fournisseurs** (pour les fournisseurs DLP cloud) | Responsable équipe sécurité | Annuellement par fournisseur | 3 ans |
| 21 | **Résultats des tests de reprise après sinistre** (tests de rétablissement DLP) | Responsable opérations IT | Annuel (par test DR) | 3 ans |
| 22 | **Tableaux de bord trimestriels pour la direction** (état du programme DLP) | RSSI | Trimestriel | 3 ans |
| 23 | **Présentation de la revue annuelle de direction** (revue du programme DLP) | RSSI | Annuel | 3 ans |

### Attentes d'échantillonnage lors des audits SOC 2 Type II

Les auditeurs échantillonneront typiquement :
- **25 alertes DLP** sur différents niveaux de gravité (vérifier la réponse dans les SLA, documentation complète).
- **Tous les incidents Critiques/Élevés** (vérifier le confinement, l'investigation, la notification des clients le cas échéant).
- **Toutes les exceptions actives** (vérifier l'approbation, le calendrier de révision respecté, les mesures compensatoires documentées).
- **Tous les cycles de tests trimestriels** (vérifier les tests effectués, résultats documentés, lacunes remédiées).
- **Toutes les revues fournisseurs** (vérifier complétées, rapports SOC 2 à jour obtenus).
- **Preuves de notification des employés** pour **25 employés** (vérifier complétion de la formation, accusé de réception documenté).
- **Évaluation de proportionnalité** (vérifier à jour, approuvée par le DPD/RSSI).

**La complétude est critique** : La documentation manquante pour tout élément échantillonné constitue une constatation d'audit. Assurer une documentation continue tout au long de la période d'audit.

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, notamment les rapports du système DLP, les évaluations de couverture des canaux, les relevés de réponse aux incidents, les révisions du registre des exceptions, les audits de notification des employés, les audits internes et externes, et les retours au propriétaire de la politique.

**Indicateurs de conformité** :

| Indicateur | Cible | Fréquence de mesure |
|-----------|-------|---------------------|
| Couverture des canaux DLP (chemins de sortie critiques) | >= 95 % | Trimestriel |
| Réponse aux alertes DLP dans les SLA | >= 95 % | Hebdomadaire |
| Taux de faux positifs | < 10 % | Mensuel |
| Exceptions actives révisées dans le calendrier | 100 % | Trimestriel |
| Complétion de la formation de sensibilisation DLP des employés | >= 95 % | Annuel |
| Documentation de transparence de la surveillance des employés complète | 100 % | Annuel |
| Évaluation de proportionnalité à jour et approuvée | 100 % | Annuel |

**Notation de la conformité** :

| Composant | Pondération | Calcul |
|-----------|------------|--------|
| Couverture des canaux | 30 % | (Canaux avec couverture DLP vérifiée) / (Total des canaux de sortie critiques) × 100 |
| Efficacité de la réponse aux incidents | 25 % | (Incidents répondus dans les SLA) / (Total des incidents) × 100 |
| Gestion des ajustements de politique et des faux positifs | 20 % | Inverse du taux de faux positifs + tendance d'amélioration des ajustements |
| Conformité légale (transparence, proportionnalité) | 15 % | (Exigences légales complétées) / (Total des exigences légales) × 100 |
| Gestion des exceptions | 10 % | (Exceptions révisées dans le calendrier) / (Total des exceptions actives) × 100 |

**Traitement de la non-conformité** : En dessous de 70 %, escalade immédiate au RSSI et plan de remédiation dans les 30 jours. De 70 à 89 %, supervision du Responsable de la sécurité de l'information avec révisions mensuelles. À 90 % et au-dessus, suivi trimestriel standard.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée par le Responsable de la sécurité de l'information à l'avance, avec acceptation documentée du risque, mesures compensatoires et date de révision définie (maximum 12 mois). Les exceptions doivent être rapportées à l'Équipe de revue de direction. Les exceptions permanentes ne sont pas autorisées sans mesures compensatoires documentées et révision trimestrielle.

## Non-conformité

Un employé reconnu avoir violé la présente politique peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement. Les tentatives délibérées de contourner les contrôles DLP seront traitées comme une faute grave. Les violations de politique doivent être documentées, investiguées par le Responsable de la sécurité de l'information et rapportées au RSSI. Lorsque des violations impliquent des violations de données personnelles, le DPD doit être consulté.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions des capacités technologiques DLP, les nouvelles techniques d'exfiltration de données (menaces internes, menaces persistantes avancées, attaques de la chaîne d'approvisionnement), les modifications réglementaires affectant la surveillance des employés ou les exigences de protection des données, les constatations d'audit, les indicateurs et tendances de performance DLP, les retours des utilisateurs sur les faux positifs, et les enseignements tirés des incidents DLP.

---

# Domaines de la norme ISO 27001 couverts

Politique de prévention des fuites de données — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.10 Utilisation acceptable de l'information et des autres actifs associés |
| Clause 6.1 Actions face aux risques et opportunités | 5.12 Classification de l'information |
| Clause 6.2 Objectifs de sécurité de l'information | 5.13 Étiquetage de l'information |
| Clause 7.3 Sensibilisation | 5.14 Transfert de l'information |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | **8.12 Prévention des fuites de données** |
| Clause 9.3 Revue de direction | 8.15 Journalisation |

<!-- QA_VERIFIED: 2026-03-29 -->
