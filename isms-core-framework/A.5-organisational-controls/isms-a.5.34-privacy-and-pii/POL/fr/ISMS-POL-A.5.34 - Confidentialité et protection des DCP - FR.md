<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.34-FR:framework:POL:a.5.34 -->
**ISMS-POL-A.5.34 — Confidentialité et protection des données à caractère personnel (DCP)**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Confidentialité et protection des données à caractère personnel (DCP) |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.34 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) / Délégué à la Protection des Données (DPD) |
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
| 1.0 | [Date] | RSSI/DPD | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Délégué à la Protection des Données (DPD) / Responsable de la protection des données
- Secondaire : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Examen juridique : Juriste/Responsable de la conformité (obligatoire)
- Intégration RH : Directeur des Ressources Humaines (DRH) — aspects relatifs aux DCP des employés
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-CTX-A.5.34 (Référence sur le paysage réglementaire en matière de protection des données)
- ISMS-IMP-A.5.34.1-UG/TG (Évaluation de l'identification et de la classification des DCP)
- ISMS-IMP-A.5.34.2-UG/TG (Évaluation de la base juridique et de la licéité du traitement)
- ISMS-IMP-A.5.34.3-UG/TG (Évaluation de la gestion des droits des personnes concernées)
- ISMS-IMP-A.5.34.4-UG/TG (Évaluation des mesures techniques et organisationnelles — MTO)
- ISMS-IMP-A.5.34.6-UG/TG (Évaluation des transferts transfrontaliers)
- ISMS-POL-A.5.9 (Inventaire des informations et des actifs)
- ISMS-POL-A.5.12 (Classification de l'information)
- ISMS-POL-A.5.15-16-18 (Gestion des identités et des accès)
- ISMS-POL-A.5.33 (Protection des enregistrements)
- ISMS-POL-A.8.10 (Suppression de l'information)
- ISMS-POL-A.8.11 (Masquage des données)
- ISMS-POL-A.8.12 (Prévention des fuites de données)
- ISO/IEC 27001:2022 Contrôle A.5.34
- ISO/IEC 27701:2019 (Système de management de la protection de la vie privée — si mis en œuvre)

---

## Résumé exécutif

La présente politique établit les exigences de [Organisation] en matière de confidentialité et de protection des données à caractère personnel (DCP), conformément au contrôle A.5.34 de la norme ISO/IEC 27001:2022.

**Objet** : Définir CE QUI doit être respecté en matière de protection des données et QUI est responsable de la conformité. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.34 (variantes UG/TG).

**Périmètre** : Tout traitement de données personnelles / DCP par [Organisation], incluant les données relatives aux clients, employés, prestataires, fournisseurs et autres personnes physiques, indépendamment du format ou du lieu.

**Alignement réglementaire** : Répond aux exigences de conformité obligatoires définies dans ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et l'ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles s'appliquent lorsque les activités métier en déclenchent l'applicabilité.

---

# Alignement des contrôles et périmètre

## Contrôle A.5.34 de l'ISO/IEC 27001:2022

**ISO/IEC 27001:2022 Annexe A.5.34 — Confidentialité et protection des données à caractère personnel**

> *L'organisation devrait identifier et respecter les exigences relatives à la préservation de la confidentialité et à la protection des données à caractère personnel conformément aux lois, réglementations applicables et aux exigences contractuelles.*

**Objectif du contrôle** : Garantir que [Organisation] identifie l'ensemble des exigences applicables en matière de protection des données et met en œuvre des mesures appropriées pour protéger les DCP tout au long de leur cycle de vie, en respectant les droits des personnes concernées et en satisfaisant aux obligations réglementaires.

**Type de contrôle** : Contrôle organisationnel (Contrôles relatifs aux personnes — Section 5)

**Propriétés de sécurité de l'information** :

- **Confidentialité** — DCP protégées contre toute divulgation non autorisée
- **Intégrité** — Exactitude des DCP maintenue, modification non autorisée empêchée
- **Disponibilité** — Droits des personnes concernées satisfaits dans les délais réglementaires

## Périmètre de la politique

**Cette politique établit** :

- Les exigences de gouvernance en matière de protection des données et la structure de responsabilité
- Le cadre de classification des DCP aligné sur les définitions réglementaires
- Les exigences relatives à la base juridique du traitement des données personnelles
- Les exigences relatives aux droits des personnes concernées et les obligations de réponse
- Les exigences de protection des données dès la conception et par défaut
- Les déclencheurs d'Analyse d'Impact sur la Protection des données (AIP)
- Les exigences relatives aux transferts transfrontaliers de données
- Les obligations de notification des violations de données
- Les exigences relatives au Registre des Activités de Traitement (RAT)

**Cette politique ne fournit PAS** :

- Les procédures détaillées de traitement des demandes des personnes concernées (voir ISMS-IMP-A.5.34.3)
- Les configurations techniques de protection des DCP (voir ISMS-POL-A.8.11, A.8.24)
- Les calendriers de conservation des données (voir ISMS-POL-A.5.33)

**Périmètre géographique** : Toutes les opérations de [Organisation], quel que soit le lieu. Les exigences réglementaires spécifiques sont déclenchées selon la localisation des personnes concernées, les activités de traitement et l'infrastructure des données.

**Périmètre des données** : Toutes les DCP traitées par [Organisation], incluant :

- Les clients, consommateurs et prospects
- Les employés et prestataires
- Les fournisseurs et partenaires commerciaux
- Les candidats à l'embauche
- Les visiteurs du site internet
- Toute autre personne physique dont [Organisation] traite les données

**Exclusions** : Données anonymisées (genuinement anonymisées au sens du Considérant 26 du RGPD), personnes décédées lorsque la réglementation les exclut.

---

# Cadre réglementaire

## Niveau 1 : Conformité obligatoire

**Loi fédérale suisse sur la protection des données (nLPD)**

[Organisation] DOIT se conformer aux exigences de la nLPD, notamment :

- Article 6 : Principes du traitement des données (licéité, bonne foi, proportionnalité, limitation de la finalité, minimisation des données)
- Article 8 : Exigences de sécurité des données
- Articles 19-24 : Obligation d'informer lors de la collecte de données personnelles
- Articles 25-32 : Droits des personnes concernées
- Article 24 : Notification des violations de données au PFPDT
- Articles 16-17 : Exigences relatives à la communication de données à l'étranger

**Autorité de contrôle** : Préposé fédéral à la protection des données et à la transparence (PFPDT)

---

**Règlement général sur la protection des données de l'UE (RGPD)**

[Organisation] DOIT se conformer aux exigences du RGPD, notamment :

- Article 5 : Principes du traitement
- Article 6 : Bases juridiques du traitement
- Articles 7-8 : Conditions relatives au consentement
- Article 9 : Restrictions sur le traitement des données de catégories particulières
- Articles 12-22 : Droits des personnes concernées
- Articles 24-25 : Responsabilités du responsable du traitement (responsabilité, protection des données dès la conception)
- Article 28 : Obligations des sous-traitants
- Article 30 : Registre des activités de traitement
- Article 32 : Sécurité du traitement
- Articles 33-34 : Notification des violations (72 heures à l'autorité de contrôle)
- Article 35 : Analyse d'Impact sur la Protection des données
- Articles 37-39 : Exigences relatives au DPD
- Articles 44-49 : Transferts internationaux de données

**Sanctions** : Jusqu'à 20 millions d'euros ou 4 % du chiffre d'affaires annuel mondial

---

**ISO/IEC 27001:2022**

[Organisation] maintient la certification ISO 27001:2022 avec le contrôle A.5.34 mis en œuvre conformément à la présente politique.

## Niveau 2 : Applicabilité conditionnelle

Les réglementations suivantes s'appliquent en fonction des activités métier spécifiques, évaluées conformément à ISMS-POL-00 :

- **Circulaires FINMA** : Si [Organisation] est une entité réglementée par la FINMA
- **DORA (Digital Operational Resilience Act)** : Si [Organisation] est une entité financière de l'UE ou un prestataire tiers de services TIC critique désigné. L'évaluation des risques liés aux tiers en TIC (Article 28 DORA) pour les arrangements de traitement de données satisfait aux obligations des sous-traitants au titre de l'Article 28 RGPD lorsque les deux s'appliquent
- **Directive NIS2** : Si [Organisation] est désignée comme entité essentielle ou importante. Les mesures de gestion des risques (Art. 21(2)), notamment la sécurité des ressources humaines et le contrôle d'accès, impliquent le traitement de DCP. La conformité au RGPD/nLPD satisfait aux exigences de protection des DCP de NIS2. La déclaration d'incidents spécifique à NIS2 (Art. 23) s'intègre à ISMS-POL-A.5.24-28 sans créer d'exigences supplémentaires en matière de protection des données
- **PCI DSS v4.0.1** : Si [Organisation] traite des données de titulaires de carte de paiement. Les données de titulaires de carte sont des DCP soumises à la fois au RGPD/nLPD et à PCI DSS v4.0.1. En cas de conflit entre les exigences, [Organisation] applique la plus stricte. La conformité à PCI DSS v4.0.1 ne satisfait pas automatiquement au RGPD — des mécanismes distincts de base juridique et de droits des personnes concernées sont requis
- **Réglementations sur les données de santé** : Selon les produits, services et activités de traitement. En cas de traitement de données de santé (Art. 9 RGPD — catégories particulières), des exigences sectorielles supplémentaires peuvent s'appliquer. Le traitement de données de santé requiert une base juridique documentée conformément à ISMS-IMP-A.5.34.2 et des mesures de sécurité renforcées conformément à ISMS-POL-A.8.24

**Détermination de l'applicabilité** : Le Juriste/Responsable de la conformité et le DPD déterminent conjointement l'applicabilité du Niveau 2 annuellement. Les décisions d'applicabilité sont documentées dans la Matrice d'applicabilité réglementaire d'ISMS-POL-00. Les modifications métier significatives (nouveaux marchés, nouvelles catégories de données, nouveaux clients réglementés) déclenchent une réévaluation immédiate.

## Niveau 3 : Références de bonnes pratiques

Les référentiels suivants informent les pratiques sans être obligatoires, sauf exigence contractuelle :

- ISO/IEC 27701:2019 (Système de management de la protection de la vie privée)
- ISO/IEC 29100:2011 (Cadre de protection de la vie privée)
- NIST Privacy Framework
- ISO/IEC 27002:2022 (Orientations de mise en œuvre)

---

# Déclarations de politique en matière de protection des données

## Classification des DCP

[Organisation] DOIT classifier les DCP dans les catégories suivantes :

**Catégorie 1 : DCP ordinaires** — Données personnelles standards nécessitant des mesures de protection de base (données d'identification, coordonnées, données financières, données professionnelles, identifiants électroniques, données comportementales, données de communication).

**Catégorie 2 : DCP sensibles** — Données de catégories particulières nécessitant une protection renforcée (Article 9 RGPD : origine raciale/ethnique, opinions politiques, convictions religieuses, appartenance syndicale, données génétiques, données biométriques, données de santé, vie sexuelle/orientation sexuelle ; Article 5(c) nLPD : catégories similaires incluant les données relatives aux poursuites administratives ou pénales).

**Catégorie 3 : Données relatives aux infractions pénales** — Données relatives aux condamnations pénales, infractions ou mesures de sécurité nécessitant une autorisation juridique spécifique.

## Découverte des DCP et cartographie des données

[Organisation] DOIT :

- Réaliser la découverte des DCP par des méthodes automatisées et manuelles
- Effectuer une découverte complète annuellement et pour les nouveaux systèmes avant leur déploiement
- Maintenir une cartographie des données documentant les sources de données, les finalités, la base juridique, les lieux de stockage, les destinataires du partage, les transferts et les durées de conservation
- Créer et maintenir des schémas de flux de données visuels pour les mouvements de DCP

## Registre des Activités de Traitement (RAT)

[Organisation] DOIT tenir un RAT documentant l'ensemble des opérations de traitement des données personnelles conformément à l'Article 30 RGPD et aux exigences de la nLPD.

**Le RAT DOIT inclure** : Les coordonnées du responsable/sous-traitant, les finalités du traitement, les catégories de personnes concernées, les catégories de données personnelles, les destinataires, les transferts internationaux, les durées de conservation, la description des mesures de sécurité.

**Le RAT DOIT être** : Révisé trimestriellement, mis à jour lors de modifications significatives, validé annuellement par le Conseil juridique et le RSSI.

## Base juridique du traitement

[Organisation] DOIT :

- Déterminer et documenter une base juridique valide pour chaque activité de traitement avant que celui-ci ne commence
- Traiter les données personnelles uniquement sur l'une des bases de l'Article 6 RGPD suivantes : consentement, exécution d'un contrat, obligation légale, intérêts vitaux, mission d'intérêt public ou intérêts légitimes
- Documenter la justification de la base juridique et les preuves à l'appui dans le RAT
- Pour les données de catégories particulières, documenter à la fois la base juridique de l'Article 6 ET la condition spécifique de l'Article 9(2)

## Gestion du consentement

Lorsque le consentement est la base juridique, [Organisation] DOIT s'assurer que le consentement est :

- Libre, spécifique, éclairé et univoque
- Obtenu par une action positive claire
- Révocable à tout moment, le retrait étant aussi aisé que l'octroi
- Documenté avec enregistrement du qui, quand, quoi et comment

## Évaluations de l'intérêt légitime

Lorsque l'intérêt légitime est la base juridique, [Organisation] DOIT :

- Conduire et documenter une Évaluation de l'Intérêt Légitime (LIA) avant tout traitement, en utilisant le modèle standardisé dans ISMS-IMP-A.5.34.2
- Appliquer le test en trois parties : test de finalité (existe-t-il un but légitime ?), test de nécessité (des alternatives moins intrusives sont-elles disponibles ?) et test d'équilibre (intérêts de l'organisation par rapport aux droits des personnes concernées, compte tenu de leurs attentes, de la relation et de la sensibilité des données)
- Obtenir l'approbation du Conseil juridique/DPD avant le début du traitement
- Réexaminer les LIA annuellement ou lors de modifications significatives du traitement

## Droits des personnes concernées

[Organisation] DOIT permettre aux personnes concernées d'exercer leurs droits au titre du RGPD et de la nLPD :

| Droit | Exigence |
|-------|----------|
| **Accès** | Fournir la confirmation du traitement et une copie des données personnelles dans les délais réglementaires |
| **Rectification** | Corriger les données inexactes et compléter les données incomplètes |
| **Effacement** | Supprimer les données personnelles lorsque les conditions d'effacement sont remplies et qu'aucune exception ne s'applique |
| **Portabilité** | Fournir les données dans un format structuré et lisible par machine lorsque applicable |
| **Opposition** | Cesser le traitement en cas d'opposition sauf si des raisons impérieuses prévalent ; droit absolu pour le marketing direct |
| **Limitation** | Limiter le traitement lorsque les conditions sont remplies |

**Délais de réponse** : [Organisation] DOIT répondre aux demandes des personnes concernées dans un **délai d'un mois à compter de la réception** (Art. 12(3) RGPD, Art. 25(4) nLPD).

**Prolongation des délais de réponse** : Si la complexité ou le volume des demandes nécessite une prolongation, [Organisation] DOIT :

1. Notifier la personne concernée dans le délai initial d'un mois du motif du retard et de la date de finalisation prévue (maximum 3 mois au total selon l'Art. 12(3) RGPD)
2. Documenter la justification dans le système de suivi des demandes
3. Obtenir l'approbation du DPD pour la prolongation

Les retards systématiques dans le traitement des demandes DOIVENT faire l'objet d'une investigation en tant que défaillance processuelle potentielle et être signalés au Comité de pilotage de la protection des données.

**Preuves relatives aux demandes** : Le système de suivi des demandes enregistre la date de réception, la date de réponse, le statut de traitement et les justifications de prolongation. Les indicateurs mensuels sont communiqués au DPD pour l'analyse des tendances.

## Protection des données dès la conception et par défaut

[Organisation] DOIT :

- Mettre en œuvre les principes de protection des données tout au long du développement des systèmes et de la conception des traitements
- Prendre en compte l'état de l'art, les coûts de mise en œuvre, la nature du traitement et les risques pour les personnes concernées
- Configurer les systèmes avec des paramètres par défaut protecteurs de la vie privée (minimisation des données, limitation du périmètre de traitement, limitation de la conservation, limitation de l'accessibilité)
- Mettre à la disposition des utilisateurs des contrôles de protection de la vie privée accessibles

## Analyses d'Impact sur la Protection des données

[Organisation] DOIT réaliser des AIP avant tout traitement susceptible de :

- Présenter un risque élevé pour les droits et libertés des personnes concernées
- Impliquer une évaluation systématique/extensive automatisée avec des effets juridiques
- Impliquer le traitement à grande échelle de données de catégories particulières ou de données relatives aux infractions pénales
- Impliquer la surveillance systématique d'espaces accessibles au public

L'AIP DOIT inclure : Une description systématique du traitement, l'évaluation de la nécessité et de la proportionnalité, l'évaluation des risques pour les personnes concernées, et les mesures pour faire face à ces risques.

Le DPD DOIT être consulté sur toutes les AIP. La consultation de l'autorité de contrôle est requise si le risque élevé ne peut être atténué.

## Transferts transfrontaliers de données

[Organisation] NE DOIT PAS transférer de données personnelles vers des pays tiers sauf si :

- Une décision d'adéquation existe (Commission européenne ou Conseil fédéral suisse)
- Des garanties appropriées sont en place (Clauses Contractuelles Types, Règles d'Entreprise Contraignantes, codes de conduite ou certifications approuvés)
- Une dérogation spécifique s'applique (consentement explicite, nécessité contractuelle, actions en justice, intérêts vitaux)

Des évaluations de l'impact des transferts DOIVENT être réalisées pour les transferts non fondés sur une décision d'adéquation.

## Notification des violations de données

[Organisation] DOIT :

- Notifier l'autorité de contrôle sans délai indu (RGPD : dans les 72 heures, nLPD : le plus rapidement possible) en cas de violations susceptibles de présenter un risque pour les personnes concernées
- Communiquer la violation aux personnes concernées sans délai indu lorsqu'elle est susceptible d'engendrer un risque élevé
- Documenter toutes les violations, y compris les faits, les effets et les mesures correctives
- Tenir un registre des violations

## Mesures techniques et organisationnelles

[Organisation] DOIT mettre en œuvre des mesures de sécurité appropriées tenant compte de l'état de l'art, des coûts de mise en œuvre, de la nature du traitement et des risques, notamment :

- La pseudonymisation et le chiffrement des données personnelles
- Des mesures garantissant la confidentialité, l'intégrité, la disponibilité et la résilience continues
- Un processus de test et d'évaluation réguliers de l'efficacité des contrôles
- La capacité à rétablir la disponibilité des données après un incident

Des mesures renforcées DOIVENT être mises en œuvre pour les données de catégories particulières, les données relatives aux infractions pénales et les données de mineurs.

---

# Rôles et responsabilités

## Délégué à la Protection des Données (DPD) / Responsable de la protection des données

**Responsabilité** : Fonction indépendante de gouvernance en matière de protection des données

**Attributions** :

- Informer et conseiller sur les obligations RGPD/nLPD
- Surveiller la conformité en matière de protection des données
- Émettre des avis sur les AIP
- Coopérer avec les autorités de contrôle
- Servir de point de contact pour les autorités et les personnes concernées
- Maintenir le RAT avec les contributions des unités métier

**Rattachement hiérarchique** : Rend compte directement au plus haut niveau de la direction sans recevoir d'instructions dans l'exercice de ses missions.

**Garanties d'indépendance du DPD** :

1. Le DPD n'exerce pas de fonctions entraînant un conflit d'intérêts (auto-évaluation annuelle examinée par la Direction générale)
2. Le DPD rend compte directement au PDG, non au RSSI ni à la direction opérationnelle
3. Le DPD dispose d'un budget autonome pour les conseils juridiques externes et les outils de protection des données
4. La résiliation du mandat du DPD ou toute modification significative de ses responsabilités requiert l'approbation de la Direction générale avec justification documentée
5. L'indépendance du DPD est vérifiée annuellement lors des audits internes ISO 27001

## Directeur général (PDG) / Direction générale

**Responsabilité** : Responsabilité globale de la conformité en matière de protection des données

**Attributions** :

- Approuver la politique de protection des données et ses modifications significatives
- Allouer les ressources pour le programme de protection des données
- Examiner les indicateurs de protection des données et les rapports de violations
- Garantir l'engagement organisationnel envers la protection des données

## Responsable de la Sécurité des Systèmes d'Information (RSSI)

**Responsabilité** : Contrôles de sécurité technique pour la protection des DCP

**Attributions** :

- Mettre en œuvre les contrôles de sécurité technique
- Réaliser des évaluations des risques de sécurité pour les activités de traitement
- Contribuer techniquement aux AIP
- Piloter la réponse aux violations de données (confinement technique)
- Superviser les contrôles d'accès et le chiffrement des DCP

## Juriste / Responsable de la conformité

**Responsabilité** : Interprétation juridique et évaluation réglementaire

**Attributions** :

- Fournir l'interprétation juridique des réglementations sur la protection des données
- Examiner les accords avec les sous-traitants et les mécanismes de transfert
- Évaluer l'applicabilité réglementaire conformément à ISMS-POL-00
- Soutenir le DPD dans les interactions réglementaires

## Propriétaires des données

**Responsabilité** : Responsabilité de l'unité métier pour des domaines de données spécifiques

**Attributions** :

- Définir la finalité et la base juridique du traitement
- Classifier les données selon leur sensibilité
- Déterminer les exigences de conservation
- Autoriser l'accès aux données
- Assurer la conformité à la politique pour leur domaine de données

## Ressources Humaines (RH)

**Responsabilité** : Traitement des DCP des employés

**Attributions** :

- Assurer la licéité de la base juridique pour le traitement des données des employés
- Fournir les notices de confidentialité aux employés
- Traiter les demandes des employés en tant que personnes concernées
- Se coordonner avec les représentants du personnel sur les questions de protection des données
- Gérer la formation des employés à la protection des données

## Tout le personnel

**Responsabilités universelles** :

- Se conformer à la présente politique et aux procédures de protection des données
- Suivre la formation obligatoire à la protection des données
- Traiter les données personnelles uniquement à des fins autorisées
- Signaler immédiatement toute violation de données présumée ou atteinte à la protection des données
- Maintenir la confidentialité des données personnelles

---

# Gouvernance et révision

## Structure de gouvernance en matière de protection des données

**Comité de pilotage de la protection des données** : Comité transversal (DPD, RSSI, Juridique, RH, Informatique, Représentants métier) se réunissant trimestriellement pour examiner les indicateurs de protection des données, le volume des demandes, les incidents de violation et l'efficacité du programme.

**Activités de gouvernance** :

- **Trimestrielle** : Réunions du Comité de pilotage, révision des indicateurs
- **Annuelle** : Révision du programme de protection des données, mises à jour de la politique, validation du RAT, évaluation de la formation
- **Ponctuelle** : Examen des AIP, évaluations des sous-traitants, gestion des incidents

## Indicateurs de protection des données

[Organisation] DOIT suivre et communiquer :

- Demandes des personnes concernées (volume, type, délai de réponse, taux de traitement)
- Violations de données (nombre, gravité, conformité des notifications)
- AIP (nombre réalisées, constats, statut des mesures d'atténuation)
- Conformité à la formation (taux de réalisation)
- Conformité des sous-traitants (couverture contractuelle, réalisation des évaluations)

**Tableau de bord des indicateurs de protection des données** : Les indicateurs sont intégrés au tableau de bord SMSI de [Organisation] (voir ISMS-POL-A.9.1 Surveillance), offrant une visibilité en temps réel au DPD et des rapports de synthèse trimestriels au Comité de pilotage. Indicateurs suivis via :

- Système de suivi des demandes (volume, type, délai de réponse, taux de traitement)
- Registre des violations (nombre d'incidents, classification par gravité, conformité des notifications)
- Base de données de suivi des AIP (nombre réalisées, constats à risque élevé, statut des mesures d'atténuation)
- LMS de formation (taux de réalisation par rôle, résultats des évaluations)

Le tableau de bord est examiné mensuellement par le DPD pour l'analyse des tendances et la détection précoce des problèmes de conformité.

**Escalade** : Les violations à risque élevé, les enquêtes des autorités de contrôle et la non-conformité systémique sont immédiatement escaladées à la Direction générale.

## Révision de la politique

**Cycle de révision** : Annuel minimum

**Déclencheurs de révision** : Modifications réglementaires, modifications significatives des traitements, violations révélant des lacunes, orientations des autorités de contrôle, constats d'audit, évolutions technologiques.

**Approbation** : Les modifications de la politique sont approuvées par le Conseil juridique/DPD et la Direction générale.

## Exigences de formation

[Organisation] DOIT fournir :

- **Tous les employés** : Formation annuelle de sensibilisation générale à la protection des données
- **Traitants de DCP** : Formation spécifique au rôle sur le traitement des demandes, le consentement, la minimisation des données
- **Traitants de données de catégories particulières** : Formation renforcée sur la base juridique et la sécurité
- **Nouveaux embauchés** : Formation à la protection des données dans les 30 jours suivant l'embauche
- **Développeurs/Propriétaires de systèmes** : Formation à la protection des données dès la conception

**Efficacité de la formation** : Les exigences de formation s'intègrent au cadre ISMS-POL-A.7.2 (Compétence). L'efficacité est mesurée via :

1. Évaluations post-formation (taux de réussite minimum de 80 % requis)
2. Vérification des compétences spécifiques au rôle (p. ex., les traitants de demandes démontrent leur connaissance des procédures avant habilitation)
3. Simulations annuelles pour l'équipe de réponse aux violations

Les enregistrements de formation sont maintenus conformément aux exigences d'A.7.2 et examinés lors des réunions du Comité de pilotage.

## Audits et évaluations

**Audits internes** : Annuels minimum, couvrant la conformité à la politique, les exigences RGPD/nLPD et l'efficacité des contrôles.

**Audits externes** : Audits de certification ISO 27001:2022, audits ISO 27701 (si poursuivis), inspections réglementaires.

**Cadre d'évaluation** : Suite d'évaluations ISMS-IMP-A.5.34.

---

# Exigences documentaires

[Organisation] DOIT maintenir les informations documentées suivantes :

- La présente politique (ISMS-POL-A.5.34)
- Procédures de mise en œuvre (suite ISMS-IMP-A.5.34)
- Registre des Activités de Traitement (RAT)
- Analyses d'Impact sur la Protection des données
- Évaluations de l'Intérêt Légitime
- Accords avec les sous-traitants (contrats Art. 28 RGPD)
- Clauses Contractuelles Types et Évaluations de l'impact des transferts
- Enregistrements de consentement
- Enregistrements des demandes des personnes concernées
- Registre des violations de données
- Enregistrements de formation à la protection des données
- Rapports d'audit de protection des données
- Notices de confidentialité

**Conservation** : La documentation relative à la protection des données est conservée pendant la durée du traitement plus la durée de conservation légale applicable (minimum 3 ans après cessation).

## Cadre de preuves et de vérification

**Génération de preuves** : La suite ISMS-IMP-A.5.34 génère les éléments de preuve suivants :

| Type de preuve | Source | Vérification |
|----------------|--------|--------------|
| RAT | ISMS-IMP-A.5.34.1 ; maintenu dans [Plateforme GRC/Outil] | Mise à jour trimestrielle par le DPD ; validation annuelle par le Conseil juridique et le RSSI |
| Enregistrements des demandes | Système de suivi des demandes ; ISMS-IMP-A.5.34.3-UG/TG | Révision mensuelle des indicateurs par le DPD |
| Documentation de la base juridique | ISMS-IMP-A.5.34.2-UG/TG | Échantillonnage annuel lors des audits |
| Évaluations de l'impact des transferts | ISMS-IMP-A.5.34.6-UG/TG | Examen juridique avant transfert |
| Registre des violations | RSSI avec ISMS-IMP-A.5.34.4-UG/TG | Révision trimestrielle par le Comité de pilotage |
| Enregistrements de consentement | Système de gestion du consentement | Échantillonnage annuel lors des audits |
| Accords avec les sous-traitants | Service juridique | Révision contractuelle annuelle |

**Vérification des preuves** : Le DPD est responsable de s'assurer que les mécanismes de preuve sont opérationnels et auditables. Un échantillonnage trimestriel des preuves est réalisé dans le cadre des réunions du Comité de pilotage.

---

# Intégration avec les autres contrôles

Cette politique s'intègre avec :

| Contrôle | Intégration |
|----------|-------------|
| A.5.9 (Inventaire des actifs) | Les actifs DCP identifiés et référencés croisés avec le RAT |
| A.5.12 (Classification) | Le schéma de classification inclut les catégories de DCP |
| A.5.15-16-18 (GIA) | Les contrôles d'accès appliquent le principe du moindre privilège pour les DCP |
| A.5.19-23 (Relations fournisseurs) | Des accords avec les sous-traitants requis pour les fournisseurs traitant des DCP |
| A.5.24-28 (Gestion des incidents) | Les violations de données impliquant des DCP déclenchent à la fois les exigences de notification propres à la protection des données (Art. 33-34 RGPD, Art. 24 nLPD) et les procédures générales de réponse aux incidents. La classification des incidents inclut une évaluation de l'impact sur la vie privée (volume de DCP, sensibilité, personnes concernées). Le RSSI pilote le confinement technique ; le DPD détermine les exigences de notification à l'autorité de contrôle et aux personnes concernées conformément à ISMS-IMP-A.5.34.4. Le registre des violations est maintenu par le RSSI avec révision trimestrielle par le Comité de pilotage |
| A.5.33 (Enregistrements) | Les calendriers de conservation sont conformes à la minimisation des données |
| A.6.3 (Formation) | Formation à la protection des données obligatoire pour tous les employés |
| A.8.10 (Suppression) | La suppression sécurisée met en œuvre le droit à l'effacement |
| A.8.11 (Masquage) | La pseudonymisation protège les DCP |
| A.8.12 (DLP) | Le DLP détecte les divulgations non autorisées de DCP |
| A.8.24 (Cryptographie) | Le chiffrement obligatoire pour les DCP sensibles |

---

# Conformité et exceptions

## Conformité

Tout le personnel est tenu de se conformer à la présente politique. Le non-respect peut entraîner des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Exceptions

Les exceptions à cette politique requièrent :

- Une demande écrite avec justification métier et évaluation des risques
- L'avis et la recommandation du DPD
- L'examen juridique des implications réglementaires
- L'approbation de la Direction générale
- Des contrôles compensatoires documentés
- Une durée limitée avec date de révision

Les exceptions NE PEUVENT PAS être accordées pour les exigences réglementaires obligatoires (RGPD, nLPD).

## Application

Les violations présumées DOIVENT être signalées au DPD et faire l'objet d'une investigation. Les atteintes à la protection des données impliquant des DCP peuvent également déclencher des obligations de notification de violation.

---

# Documents connexes

| Identifiant du document | Titre du document |
|-------------------------|-------------------|
| ISMS-POL-00 | Cadre d'applicabilité réglementaire |
| ISMS-CTX-A.5.34 | Référence sur le paysage réglementaire en matière de protection des données |
| ISMS-IMP-A.5.34.1-UG/TG | Évaluation de l'identification et de la classification des DCP |
| ISMS-IMP-A.5.34.2-UG/TG | Évaluation de la base juridique et de la licéité du traitement |
| ISMS-IMP-A.5.34.3-UG/TG | Gestion des droits des personnes concernées |
| ISMS-IMP-A.5.34.4-UG/TG | Évaluation des mesures techniques et organisationnelles |
| ISMS-IMP-A.5.34.6-UG/TG | Évaluation des transferts transfrontaliers |
| ISMS-POL-A.5.33 | Protection des enregistrements |
| ISMS-POL-A.8.10 | Suppression de l'information |
| ISMS-POL-A.8.11 | Masquage des données |
| ISMS-POL-A.8.12 | Prévention des fuites de données |
| ISMS-POL-A.8.24 | Utilisation de la cryptographie |

---

# Enregistrement d'approbation

| Rôle | Nom | Signature | Date |
|------|-----|-----------|------|
| Délégué à la Protection des Données | [Nom] | | |
| Responsable de la Sécurité des Systèmes d'Information | [Nom] | | |
| Juriste / Responsable de la conformité | [Nom] | | |
| Directeur général | [Nom] | | |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*La présente politique établit les exigences en matière de confidentialité et de protection des données à caractère personnel. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.34 (UG/TG) — sections A.5.34.1 à A.5.34.6.*

<!-- QA_VERIFIED: 2026-03-30 -->
