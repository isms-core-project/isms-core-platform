<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.14-FR:operational:OP-POL:a.5.14 -->
**ISMS-OP-POL-A.5.14 — Transfert de l'information**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Transfert de l'information |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.14 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
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

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôle A.5.14 — Transfert de l'information

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec le transfert de l'information |
|----------|----------------------------------------------|
| A.5.10 Utilisation acceptable de l'information | Les règles d'utilisation acceptable s'appliquent à tous les transferts d'information |
| A.5.12–13 Classification et étiquetage de l'information | La classification détermine la méthode de transfert et les exigences de chiffrement |
| A.5.19–23 Relations avec les fournisseurs | Accords de transfert avec des tiers et transferts vers des services cloud |
| A.5.31 Exigences légales, statutaires et réglementaires | Exigences légales pour les transferts transfrontaliers (art. 16–17 nFADP) |
| A.5.34 Protection de la vie privée et des DCP | Exigences de transfert des données personnelles et déclencheurs AIPD |
| A.7.10 Supports de stockage | Gestion des supports amovibles et élimination sécurisée |
| A.8.10 Suppression de l'information | Effacement sécurisé des données transférées depuis les stockages temporaires et supports |
| A.8.13 Sauvegarde de l'information | Sécurité du transport des supports de sauvegarde et du transfert hors site |
| A.8.24 Utilisation de la cryptographie | Normes de chiffrement pour les données en transit |

**Politiques internes connexes** :

- Politique de classification et de traitement de l'information
- Politique d'utilisation de la cryptographie
- Politique de contrôle d'accès
- Politique de protection de la vie privée et des DCP
- Politique de gestion des actifs
- Politique de gestion des incidents

---

# Politique de transfert de l'information

## Objet

L'objet de cette politique est d'assurer le traitement correct lors du transfert d'informations en interne et vers l'extérieur, et de protéger le transfert d'informations utilisant tous types de moyens de communication.

Cette politique soutient la nFADP suisse (LPD révisée) et l'Ordonnance sur la protection des données (DSV) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) lors des transferts. Là où l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Périmètre

Tous les employés et utilisateurs tiers.

Les informations faisant partie des systèmes et applications considérés comme dans le périmètre par la déclaration de périmètre ISO 27001.

## Principes

Les transferts de données doivent respecter toutes les exigences légales et réglementaires applicables, y compris la nFADP suisse (LPD révisée) et, le cas échéant, le RGPD européen.

Des accords formels comprenant des clauses de non-divulgation et de confidentialité doivent être en place pour le partage de données avec des tiers préalablement au transfert.

Les données personnelles ne doivent pas être transférées en dehors de la Suisse sans base légale valide en vertu des art. 16–17 nFADP (décision d'adéquation, Clauses contractuelles types ou exception applicable). Voir la section Transferts transfrontaliers ci-dessous.

Aucune information personnelle ou confidentielle ne doit être transférée sans chiffrement.

Tous les transferts doivent être conformes à la Politique de classification et de traitement de l'information.

---

## Vérification antivirus

L'information transférée doit être vérifiée pour la présence de logiciels malveillants avant l'envoi ou avant l'ouverture lors de la réception. Cela s'applique à tous les transferts électroniques, y compris les pièces jointes d'e-mails, les transferts de fichiers et les supports amovibles.

## Chiffrement de l'information

Les informations personnelles et confidentielles doivent toujours être chiffrées avant d'être transférées, conformément à la Politique d'utilisation de la cryptographie.

Les identifiants de chiffrement pour le nom d'utilisateur et le mot de passe, lorsqu'ils sont utilisés, doivent être partagés via deux méthodes de communication séparées et distinctes. La méthode privilégiée consiste à partager le lien d'accès ou le nom d'utilisateur par e-mail et le mot de passe ou la phrase de passe par appel vocal ou canal de messagerie sécurisé.

## Accords de transfert

Des accords de transfert formels doivent être établis avec tous les destinataires tiers de données personnelles ou confidentielles. Les accords de transfert doivent traiter les points suivants :

- Les parties impliquées et leurs rôles en matière de protection des données (responsable du traitement, sous-traitant).
- Les catégories de personnes concernées et de données personnelles à transférer.
- La finalité et la base légale du transfert.
- Les mesures techniques et organisationnelles de sécurité (chiffrement, contrôles d'accès, journalisation).
- Les obligations de conservation et de suppression des données.
- Les délais de notification en cas de violation.
- Les droits d'audit.
- Les contrôles des sous-traitants ultérieurs (le cas échéant).

Les accords de transfert doivent être révisés annuellement ou lors de modifications importantes de l'arrangement de transfert.

---

## Méthodes de transfert de données

### Méthode de transfert privilégiée

La méthode de transfert privilégiée pour les données confidentielles et personnelles est une plateforme de partage sécurisé de fichiers approuvée par l'organisation (p. ex., [service cloud chiffré], portail sécurisé ou solution de transfert de fichiers gérée).

Toutes les méthodes de transfert approuvées par l'organisation doivent prendre en charge :

- Le chiffrement en transit (TLS 1.2 minimum, TLS 1.3 préféré).
- Les contrôles d'accès et l'authentification.
- La journalisation des transferts pour audit.

### Transfert de fichiers électroniques

Pour les transferts de fichiers automatisés ou en masse, les protocoles suivants doivent être utilisés :

| Protocole | Statut |
|-----------|--------|
| SFTP (SSH File Transfer Protocol) | Approuvé — préféré pour les transferts automatisés |
| HTTPS | Approuvé — pour les téléchargements de fichiers web et les transferts via API |
| FTPS (FTP over TLS) | Approuvé — lorsque SFTP n'est pas disponible |
| FTP (non chiffré) | Interdit |
| SCP | Acceptable — mais SFTP préféré |

### Transfert de données par e-mail

L'e-mail n'est pas la méthode privilégiée pour le transfert d'informations personnelles ou confidentielles, car il n'est pas intrinsèquement sécurisé et ne garantit pas la livraison.

Une méthode de transfert sécurisée alternative doit toujours être envisagée pour le transfert de données sensibles chaque fois que cela est possible et réalisable.

La communication par e-mail ne doit pas être utilisée pour transférer des informations personnelles ou confidentielles non chiffrées.

Lorsque des données confidentielles doivent être envoyées par e-mail :

- Une pièce jointe chiffrée doit être utilisée avec une longueur de clé satisfaisant aux exigences de la Politique d'utilisation de la cryptographie (AES-256 minimum).
- Le mot de passe ou la clé de déchiffrement doit être partagé via un canal de communication séparé (appel vocal, messagerie sécurisée).
- Le nom de fichier ou l'objet ne doit pas révéler le contenu complet des pièces jointes ni divulguer des données personnelles sensibles.

Les e-mails contenant des transferts sensibles doivent inclure des instructions claires sur les responsabilités du destinataire et sur les actions à entreprendre s'il n'est pas le destinataire prévu.

L'utilisation de comptes e-mail personnels pour le transfert de données de l'organisation est interdite. Lorsque cela est techniquement faisable, l'organisation doit mettre en œuvre des contrôles pour empêcher la redirection d'e-mails de l'organisation vers des comptes personnels externes (p. ex., règles de flux de messagerie, politiques DLP, accès conditionnel).

L'organisation doit mettre en œuvre l'authentification de domaine e-mail (SPF, DKIM, DMARC) pour se protéger contre l'usurpation et l'interception d'e-mails. La politique DMARC doit être définie sur **quarantine** ou **reject** (et non sur **none**) pour les domaines de production.

### Transferts de données par courrier postal ou coursier

Les transferts de données effectués via des supports physiques tels que des rapports papier, des cartes mémoire ou des disques durs externes doivent uniquement être expédiés via un coursier sécurisé approuvé par l'organisation (un service de coursier fournissant une livraison suivie avec signature, un emballage inviolable et une documentation de chaîne de traçabilité, p. ex., Poste suisse courrier recommandé, DHL Express avec signature ou équivalent). Les services postaux standard ne doivent pas être utilisés pour les données confidentielles ou personnelles.

Le destinataire doit être clairement indiqué sur le colis et le support physique doit être soigneusement emballé pour éviter tout dommage ou altération. Un emballage inviolable doit être utilisé pour le matériel confidentiel.

Le destinataire doit être prévenu à l'avance que l'information est en cours d'envoi afin de savoir à quel moment s'y attendre. Le destinataire doit confirmer la bonne réception dès que l'information arrive. L'expéditeur est responsable de confirmer que les données sont arrivées en toute sécurité.

### Transferts de données sur supports amovibles

Seuls les supports amovibles appartenant à l'organisation doivent être utilisés pour le transfert d'informations, conformément à la Politique de gestion des actifs. L'appareil doit être approuvé, enregistré dans le registre des actifs, assigné à un utilisateur et chiffré (chiffrement intégral AES-256 ou chiffrement au niveau des fichiers). Le chiffrement doit être vérifié par l'informatique avant que l'appareil ne soit approuvé pour les transferts de données confidentielles.

Les clés USB non chiffrées, les appareils de stockage personnels et les services de stockage cloud non approuvés ne doivent pas être utilisés pour les transferts de données de l'organisation.

Le support amovible doit être restitué au propriétaire à la fin du transfert et les données transférées doivent être effacées de manière sécurisée du support de stockage après utilisation. Le registre des actifs doit être mis à jour.

Des instructions claires sur les responsabilités du destinataire et sur les actions à entreprendre s'il n'est pas le destinataire prévu doivent être fournies.

Aucun message d'accompagnement ni nom de fichier ne doit révéler le contenu du support.

Le processus décrit pour les transferts de données par courrier postal ou coursier doit être suivi pour l'expédition physique des supports amovibles.

### Téléphones, téléphones mobiles et conversations générales

Les appels téléphoniques pouvant être surveillés, entendus par inadvertance ou interceptés (délibérément ou accidentellement), les précautions suivantes doivent être prises :

- Être conscient de son environnement, notamment dans les transports en commun et les lieux publics, lors de la discussion d'informations personnelles, confidentielles ou autrement sensibles.
- Les données personnelles ne doivent pas être transférées ou discutées par téléphone à moins d'avoir confirmé l'identité et l'autorisation du destinataire.
- Lors de l'utilisation de la messagerie vocale, ne pas laisser de messages sensibles ou confidentiels ni inclure de données personnelles. Fournir uniquement un moyen de contact et attendre que le destinataire vous parle personnellement.
- Lors de l'écoute des messages vocaux, s'assurer de ne pas les diffuser dans des zones ouvertes où d'autres personnes risqueraient de les entendre. Les supprimer immédiatement après écoute.

### Transferts de données via Bluetooth

Le Bluetooth ne doit pas être approuvé comme méthode de communication pour les données confidentielles, personnelles ou autrement sensibles non chiffrées.

Lorsque le Bluetooth est utilisé à des fins approuvées (p. ex., périphériques tels que claviers, casques) :

- L'authentification mutuelle des appareils doit être effectuée pour toutes les connexions.
- Le chiffrement doit être activé pour toutes les transmissions.
- Le mode de sécurité Bluetooth 4, niveau 3 (chiffrement authentifié) ou supérieur doit être utilisé. Les modes de sécurité 1 et 2 sont interdits.
- Les appareils doivent être réglés en mode non détectable lorsqu'ils ne sont pas activement en cours d'appairage.
- L'appairage doit être effectué dans un endroit sécurisé et non public.
- Les utilisateurs ne doivent pas accepter de transmissions de quelque nature que ce soit provenant d'appareils inconnus ou suspects.
- Le transfert de fichiers Bluetooth (OBEX) doit être désactivé sauf si spécifiquement approuvé.
- Les profils Bluetooth doivent être limités à ceux requis pour la fonction approuvée.

---

## Transferts transfrontaliers de données

Les données personnelles ne doivent pas être transférées vers un pays en dehors de la Suisse à moins que l'une des conditions suivantes ne soit remplie :

| Garantie | Description |
|----------|-------------|
| Décision d'adéquation | Le Conseil fédéral suisse a déterminé que le pays de destination offre une protection adéquate des données (Annexe 1, DSV). Cela inclut tous les États de l'UE/EEE, le Royaume-Uni et d'autres pays listés. |
| Cadre de confidentialité des données UE-USA (DPF) | Pour les destinataires américains certifiés sous le DPF (en vigueur depuis septembre 2024). Le statut de certification doit être vérifié avant chaque transfert. |
| Clauses contractuelles types | CCT UE adaptées pour la nFADP suisse, avec le PFPDT comme autorité de contrôle. Une Évaluation de l'impact du transfert (EIT) doit être complétée. |
| Règles d'entreprise contraignantes | Approuvées par le PFPDT suisse pour les transferts intra-groupe. |
| Consentement explicite | La personne concernée a donné son consentement explicite et éclairé au transfert spécifique après avoir été informée des risques. |
| Nécessité contractuelle | Le transfert est nécessaire à l'exécution d'un contrat avec la personne concernée. |

Un registre de tous les transferts transfrontaliers de données doit être maintenu dans la plateforme GRC de l'organisation, le système de gestion documentaire ou un emplacement central équivalent. Le registre doit documenter le destinataire, le pays de destination, la base légale, les garanties et la date de révision. Le registre doit être révisé annuellement par le RSSI ou le Conseiller en protection des données.

### Évaluation de l'impact du transfert (EIT)

Pour les transferts vers des pays sans décision d'adéquation (s'appuyant sur des CCT ou d'autres garanties), une Évaluation de l'impact du transfert doit être conduite avant le début du transfert. L'EIT doit évaluer :

- **Environnement légal** : Les lois dans le pays de destination susceptibles d'affecter la protection des données (accès gouvernemental, lois sur la surveillance).
- **Circonstances pratiques** : Si le destinataire est soumis à des obligations légales contradictoires ou à des demandes d'accès aux données par des autorités gouvernementales.
- **Mesures techniques** : Chiffrement, pseudonymisation ou autres mesures rendant les données inintelligibles pour les parties non autorisées.
- **Mesures contractuelles** : CCT, clauses contractuelles supplémentaires, droits d'audit, recours des personnes concernées.
- **Risque résiduel** : Si les mesures supplémentaires ramènent le risque à des niveaux acceptables.

Les résultats de l'EIT doivent être documentés et approuvés par le RSSI ou le Conseiller en protection des données avant l'autorisation du transfert. Les EIT doivent être révisées annuellement ou en cas de changement de circonstances (changements légaux dans le pays de destination, incident de sécurité).

---

## Informations perdues ou manquantes

S'il est découvert ou suspecté que des informations ont été perdues, sont manquantes, ne sont pas arrivées ou ont été envoyées à la mauvaise personne, l'employé ou l'utilisateur tiers doit immédiatement informer son responsable hiérarchique et l'équipe de gestion de la sécurité de l'information. Le processus de gestion des incidents doit être suivi.

Les informations perdues ou mal acheminées doivent être classifiées comme :

- **Critique** : Implique des données personnelles sensibles, des données commerciales confidentielles ou crée un risque élevé pour les personnes concernées (notification de violation potentielle requise en vertu de la nFADP).
- **Élevé** : Implique des données personnelles ou des informations confidentielles mais avec peu de personnes concernées ou un volume limité.
- **Moyen** : Implique des données internes ou non confidentielles sans données personnelles.

L'individu ayant envoyé les données est responsable d'initier le rapport d'incident et de coopérer à l'investigation.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

- **Registre des accords de transfert** (accords avec des tiers avec dates de révision) — *révisé annuellement ; mis à jour lors de nouveaux accords*
- **Registre des transferts transfrontaliers** (destinations, bases légales, garanties) — *révisé annuellement par le RSSI/Conseiller en protection des données ; mis à jour lors de nouveaux transferts*
- **Journaux de transfert de fichiers sécurisés** (SFTP, HTTPS, plateforme de partage cloud) — *conservés 12 mois ; révisés trimestriellement pour les anomalies*
- **Enregistrements d'authentification de domaine e-mail** (configuration SPF, DKIM, DMARC et rapports de conformité) — *rapports DMARC révisés mensuellement*
- **Inventaire et enregistrements d'attribution des supports amovibles** — *mis à jour par événement ; réconciliés semestriellement avec le registre des actifs*
- **Journaux d'expédition par coursier et confirmations de réception** — *conservés 12 mois*
- **Rapports d'incidents** liés aux informations perdues ou mal acheminées — *conservés conformément à la politique de gestion des incidents*
- **Évaluations de l'impact du transfert** (pour les transferts vers des pays sans adéquation) — *révisées annuellement ou lors de changements légaux dans le pays de destination*
- **Journal des transferts de données** (transferts électroniques de données confidentielles ou personnelles) — *conservé 12 mois ; accessible pour audit*

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les audits des journaux de transfert, les révisions des accords, les rapports d'incidents, les audits internes et externes, et les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et consignée par le Responsable de la sécurité de l'information à l'avance, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions doivent être rapportées à l'équipe de Révision de direction.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements des normes de transfert de données, les menaces émergentes, les changements réglementaires (notamment les mises à jour de la liste d'adéquation suisse) et les enseignements tirés des incidents.

---

# Périmètre de la norme ISO 27001 couvert

Politique de transfert de l'information — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | **5.14 Transfert de l'information** |
| Clause 7.5.3 Contrôle des informations documentées | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 7.10 Supports de stockage |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nFADP suisse (LPD révisée) | Art. 8 — Mesures techniques et organisationnelles ; art. 16-17 — Transferts transfrontaliers |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales de sécurité des données ; Annexe 1 — Liste d'adéquation |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement ; art. 44-49 — Transferts internationaux |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.14 — Transfert de l'information |
| ISO/IEC 27002:2022 | Section 5.14 — Conseils d'implémentation pour le transfert de l'information |
| NIST SP 800-53 Rév. 5 | SC-8 (Confidentialité et intégrité des transmissions), MP-5 (Transport des supports) |
| CIS Controls v8 | Contrôle 3 (Protection des données — Mesure de protection 3.10 : Chiffrer les données sensibles en transit) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
