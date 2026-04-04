<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.30-FR:framework:POL:a.8.30 -->
**ISMS-POL-A.8.30 – Développement externalisé**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de développement externalisé |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.30 |
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
- Secondaire : Directeur de la Technologie (DT)
- Achats : Responsable des achats/gestion des fournisseurs
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.8.28 (Règles de codage sécurisé)
- ISMS-POL-A.5.19-23 (Relations avec les fournisseurs et services cloud)
- ISMS-IMP-A.8.30.1-UG/TG (Évaluation et registre des fournisseurs)
- ISMS-IMP-A.8.30.2-UG/TG (Conformité contractuelle)
- ISMS-IMP-A.8.30.3-UG/TG (Tests de sécurité et acceptation)
- ISO/IEC 27001:2022 Contrôle A.8.30

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la gestion de la sécurité dans le développement externalisé de systèmes et de logiciels, conformément au Contrôle A.8.30 de la norme ISO/IEC 27001:2022.

**Objet** : Définir QUELS contrôles de sécurité sont requis pour le développement externalisé et QUI en est responsable. Les détails techniques de mise en œuvre (COMMENT) sont documentés dans ISMS-IMP-A.8.30.

**Périmètre** : Toutes les activités de développement externalisé, notamment le développement contractuel, le développement offshore, les développeurs indépendants et la personnalisation de logiciels acquis.

**Risque métier traité** : Vulnérabilités de sécurité introduites par le développement tiers conduisant à des violations de données, au vol de propriété intellectuelle, à la compromission de la chaîne d'approvisionnement et à la non-conformité réglementaire.

**Alignement réglementaire** : Conformément à ISMS-POL-00 :

- **Obligatoire** : nLPD suisse (Art. 8), RGPD de l'UE (Art. 32), ISO 27001:2022
- **Conditionnel** : FINMA, DORA (Art. 28-30 risques TIC tiers), NIS2 (Art. 21 chaîne d'approvisionnement)
- **Informatif** : NIST SP 800-218 SSDF, ISO/IEC 27036 (Relations fournisseurs)

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.30 de la norme ISO/IEC 27001:2022

**Énoncé du contrôle** :
> *L'organisation doit diriger, surveiller et revoir les activités liées au développement de systèmes externalisé.*

**Objectif du contrôle** : S'assurer que les mesures de sécurité de l'information requises par [Organisation] sont efficacement mises en œuvre lorsque le développement de systèmes et de logiciels est externalisé à des tiers.

## Définition du périmètre

**Dans le périmètre** :

- Tout développement logiciel contractuel (projets complets, modules, composants)
- Équipes de développement offshore et nearshore
- Développeurs indépendants
- Renforcement des effectifs avec accès au développement
- Logiciels acquis nécessitant une personnalisation
- Fournisseurs de plateformes de développement (où le code de [Organisation] est hébergé)
- Services de développement gérés

**Hors périmètre** :

- Logiciels commerciaux sur étagère (COTS) sans personnalisation (voir A.8.31)
- Développement interne par les employés (voir A.8.28)
- Fournisseurs de services cloud pour l'infrastructure uniquement (voir A.5.23)
- Gestion générale des fournisseurs (voir A.5.19-22)

---

# Sélection des fournisseurs et diligence raisonnable

## Exigences d'évaluation de la sécurité

**Évaluation préalable à l'engagement** :

Avant d'engager tout fournisseur de développement externalisé, [Organisation] DOIT effectuer une diligence raisonnable en matière de sécurité :

| Domaine d'évaluation | Exigence | Preuve requise |
|---------------------|----------|----------------|
| **Certification de sécurité** | ISO 27001 ou SOC 2 Type II de préférence | Certificat actuel (dans les 12 mois) |
| **Pratiques de développement sécurisé** | OWASP SAMM, Microsoft SDL ou équivalent | Documentation SDLC ou attestation |
| **Historique des incidents** | Aucune violation majeure dans les 24 derniers mois | Divulgation du fournisseur + vérification des références |
| **Capacités techniques** | Outillage SAST/DAST/SCA en usage | Inventaire des outils et échantillons de rapports |
| **Sécurité du personnel** | Vérifications des antécédents pour les développeurs | Confirmation écrite de la politique de vérification |

**Profondeur d'évaluation basée sur les risques** :

| Classification du projet | Profondeur d'évaluation | Approbateur |
|--------------------------|------------------------|------------|
| **Critique** (systèmes de production, données sensibles) | Questionnaire complet + audit sur site/à distance + vérification des références | RSSI |
| **Élevé** (systèmes internes, données métier) | Questionnaire + vérification des références | Responsable sécurité IT |
| **Standard** (non sensible, faible risque) | Questionnaire + vérification de la certification | Achats + revue sécurité |

## Registre des fournisseurs approuvés

[Organisation] DOIT maintenir un registre des fournisseurs approuvés pour le développement externalisé :

- Fournisseurs évalués et approuvés avant tout engagement
- Le registre inclut : nom du fournisseur, date d'évaluation, niveau de risque, types de projets approuvés, date de renouvellement
- Réévaluation annuelle requise pour les fournisseurs actifs
- Retrait du registre à la résiliation du contrat, incident de sécurité, ou échec de réévaluation

---

# Exigences contractuelles de sécurité

## Clauses contractuelles obligatoires

Tous les contrats de développement externalisé DOIVENT inclure les exigences de sécurité suivantes :

**Conformité aux normes de sécurité** :

- Adhésion aux normes de codage sécurisé de [Organisation] (ISMS-POL-A.8.28)
- Conformité aux politiques et procédures de sécurité de [Organisation]
- Utilisation des outils et environnements de développement approuvés
- Exigences de complétion de formation à la sécurité

**Propriété intellectuelle et protection du code** :

- Propriété claire du code développé et de la documentation
- Dispositions d'entiercement du code source pour les projets critiques
- Protection des informations propriétaires de [Organisation]
- Obligations de non-divulgation et de confidentialité

**Droits de vérification de sécurité** :

- Droit d'audit des processus de développement et des contrôles de sécurité
- Droit de réaliser des tests de sécurité sur les livrables
- Droit de demander des certifications et attestations de sécurité
- Droit d'accès aux informations sur les incidents de sécurité

**Notification des incidents** :

- Notification des incidents de sécurité dans les 24 heures
- Notification immédiate des violations de données suspectées
- Coopération avec l'investigation des incidents
- Exigences de remédiation post-incident

**Gestion des sous-traitants** :

- Approbation écrite préalable requise pour les sous-traitants
- Répercussion des exigences de sécurité aux sous-traitants
- Droit de [Organisation] de refuser des sous-traitants
- Droits d'audit des sous-traitants

## SLA de remédiation des vulnérabilités

Les contrats DOIVENT spécifier les délais de remédiation des vulnérabilités alignés sur ISMS-POL-A.8.28 :

| Gravité | Score CVSS | SLA de remédiation |
|---------|------------|-------------------|
| **Critique** | 9,0-10,0 | 7 jours |
| **Élevé** | 7,0-8,9 | 30 jours |
| **Moyen** | 4,0-6,9 | 90 jours |
| **Faible** | 0,1-3,9 | Prochaine version ou 180 jours |

**Application des SLA** :

- Conformité aux SLA suivie dans le système de gestion de projet
- Défaillances répétées des SLA escaladées vers la gestion des fournisseurs et le RSSI
- Non-conformité chronique pouvant entraîner une révision ou une résiliation du contrat
- Exceptions aux SLA nécessitant une acceptation de risque documentée (approbation du RSSI pour Critique/Élevé)

## Résiliation et transition

Les contrats DOIVENT traiter les exigences de sécurité pour la résiliation :

- Restitution ou destruction sécurisée des données de [Organisation]
- Révocation de tous les identifiants d'accès dans les 24 heures
- Transfert de la documentation et du code source
- Période de transfert des connaissances pour les projets critiques
- Obligations de confidentialité post-résiliation
- Attestation de destruction des données

---

# Exigences de développement sécurisé

## Normes de développement

Les développeurs externalisés DOIVENT se conformer aux normes de codage sécurisé de [Organisation] conformément à ISMS-POL-A.8.28 :

**Exigences obligatoires** :

- Validation des entrées pour toutes les entrées utilisateur et externes
- Encodage des sorties approprié au contexte
- Authentification et gestion des sessions sécurisées
- Application de l'autorisation côté serveur
- Utilisation de méthodes cryptographiques approuvées
- Gestion sécurisée des erreurs (aucune donnée sensible dans les journaux)
- Aucun secret codé en dur dans le code source

**Pratiques interdites** :

- Identifiants codés en dur, clés API ou secrets
- Fonctions dépréciées ou non sécurisées
- Construction de requêtes SQL par concaténation de chaînes
- Contrôles de sécurité désactivés
- Secrets poussés vers les systèmes de contrôle de version
- Ignorer les résultats des outils de sécurité sans exception documentée

## Sécurité de l'environnement de développement

Les environnements de développement externalisés DOIVENT répondre aux exigences minimales de sécurité :

| Exigence | Description |
|----------|-------------|
| **Contrôle d'accès** | AMF requise pour tous les systèmes de développement ; accès avec moindre privilège |
| **Sécurité réseau** | Environnement de développement isolé ou sécurisé ; aucun accès direct à la production |
| **Sécurité des postes de travail** | Postes de travail des développeurs avec logiciels de sécurité à jour |
| **Référentiel de code** | Protection des branches, application de la revue de code, analyse des secrets |
| **Gestion des données** | Aucune donnée de production dans le développement sans masquage/anonymisation |

## Formation des développeurs tiers

Avant d'accéder aux systèmes ou au code de [Organisation], les développeurs externalisés DOIVENT :

- Compléter la formation de sensibilisation au codage sécurisé de [Organisation] (ou équivalent)
- Reconnaître les politiques de sécurité et les exigences d'utilisation acceptable de [Organisation]
- Démontrer leur compréhension des exigences de sécurité spécifiques au projet

**Vérification de la formation** :

- Complétion de la formation suivie dans la liste de contrôle d'intégration du fournisseur
- Demandes d'accès vérifiées par rapport aux dossiers de formation avant approbation
- Actualisation annuelle requise pour les missions de longue durée
- Dossiers de formation conservés pour l'audit

---

# Vérification et tests de sécurité

## Exigences de revue de code

Tout code externalisé DOIT faire l'objet d'une revue de sécurité avant acceptation :

| Type de revue | Exigence | Réviseur |
|--------------|----------|---------|
| **Revue par les pairs** | Toutes les modifications de code révisées avant fusion | Développeur interne (minimum 1) |
| **Revue de sécurité** | Modifications sensibles à la sécurité révisées par l'équipe sécurité | Équipe de sécurité applicative |
| **Revue d'architecture** | Nouveaux composants ou modifications significatives | Architecte de sécurité |

## Exigences de tests de sécurité

Les livrables externalisés DOIVENT subir des tests de sécurité avant le déploiement en production :

**Tests automatisés** :

- SAST (Tests de sécurité des applications statiques) : Exécutés sur tout le code avant acceptation
- SCA (Analyse de la composition logicielle) : Analyse de toutes les dépendances tierces
- Analyse des secrets : Vérification qu'aucun secret n'est présent dans la base de code

**Tests manuels** :

- DAST (Tests de sécurité des applications dynamiques) : Exécutés sur l'environnement de préproduction
- Tests d'intrusion : Requis pour les projets Critiques avant la mise en service

**Critères d'acceptation** :

- Aucune vulnérabilité Critique ou Élevée (ou exception documentée avec contrôles compensatoires)
- Toutes les exigences de sécurité vérifiées
- Rapports de tests de sécurité documentés et conservés

## Nomenclature des composants logiciels (SBOM)

Pour tout développement externalisé, [Organisation] DOIT recevoir :

- Un SBOM complet listant tous les composants tiers
- Versions et licences des composants
- Statut des vulnérabilités connues au moment de la livraison
- Plan de mise à jour pour les composants avec vulnérabilités connues

**Format SBOM** : CycloneDX ou SPDX de préférence ; tableur acceptable pour les projets simples.

---

# Surveillance et supervision

## Exigences de supervision active

[Organisation] DOIT maintenir une implication active dans le développement externalisé (non une surveillance passive) :

**Diriger** :

- Exigences de sécurité clairement communiquées à l'initiation du projet
- Points de contrôle de sécurité définis dans les jalons du projet
- Orientations et clarifications sécurité régulières

**Surveiller** :

- Mises à jour régulières du statut des activités de sécurité
- Accès aux résultats des tests de sécurité du fournisseur
- Participation aux discussions liées à la sécurité
- Surveillance des alertes d'incidents de sécurité

**Réviser** :

- Livrables de sécurité révisés à chaque jalon
- Revue de sécurité finale avant acceptation
- Enseignements tirés documentés pour les projets futurs

## Fréquence de surveillance

| Classification du projet | Mises à jour du statut | Revues de sécurité | Audit complet |
|--------------------------|----------------------|--------------------|--------------|
| **Critique** | Hebdomadaire | À chaque jalon + finale | Annuel (ou fin de projet) |
| **Élevé** | Bimensuel | Aux jalons majeurs + finale | Sur demande |
| **Standard** | Mensuel | Acceptation finale | Sur demande |

---

# Gestion des sous-traitants

## Exigences pour les sous-traitants

Les fournisseurs de développement externalisé NE DOIVENT PAS engager de sous-traitants sans :

- Approbation écrite préalable de [Organisation]
- Évaluation de la sécurité du sous-traitant (proportionnée au risque)
- Répercussion de toutes les exigences de sécurité, notamment :
  - Normes de codage sécurisé (conformément à ISMS-POL-A.8.28)
  - Exigences de livraison SBOM
  - SLA de remédiation des vulnérabilités
- Droits d'audit directs du sous-traitant (ou audit conduit par le fournisseur)
- Obligations de confidentialité et de protection de la propriété intellectuelle

## Processus d'approbation des sous-traitants

| Périmètre du sous-traitant | Autorité d'approbation | Évaluation requise |
|---------------------------|------------------------|-------------------|
| Accès aux systèmes/données de [Organisation] | RSSI | Questionnaire de sécurité complet |
| Développement sans accès direct | Responsable sécurité IT | Questionnaire abrégé + attestation du fournisseur |
| Tâches limitées/spécialisées | Chef de projet + Sécurité | Attestation du fournisseur de répercussion des exigences |

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **Direction générale** | Approuver la politique ; allouer le budget pour les évaluations et les tests |
| **RSSI** | Responsabilité globale ; approuver les engagements à haut risque ; approuver les exceptions |
| **Responsable sécurité IT** | Supervision quotidienne ; évaluations des fournisseurs ; revue des tests de sécurité |
| **Équipe de sécurité applicative** | Définir les exigences de développement sécurisé ; réaliser les tests de sécurité |
| **Achats/Gestion des fournisseurs** | Maintenir le registre des fournisseurs approuvés ; assurer les clauses contractuelles |
| **Chefs de projet** | Inclure les exigences de sécurité dans le périmètre ; surveiller la conformité du fournisseur |
| **Responsables des équipes de développement** | Réviser le code externalisé ; vérifier les tests complétés |

---

# Gouvernance et conformité

## Métriques de conformité

**Surveillance continue** :

- Statut d'évaluation de sécurité des fournisseurs suivi
- Conformité aux clauses de sécurité contractuelles vérifiée
- Résultats des tests de sécurité révisés

**Évaluation périodique** :

- Trimestrielle : Revue du statut de sécurité des fournisseurs actifs
- Annuelle : Réévaluation complète de la sécurité des fournisseurs

## Gestion de la non-conformité des fournisseurs

| Gravité | Réponse | Escalade |
|---------|---------|---------|
| **Critique** (violation active, infraction majeure) | Suspension immédiate de l'accès ; réponse aux incidents | RSSI, Direction, Juridique |
| **Élevé** (lacune de sécurité significative) | Plan de remédiation requis sous 5 jours ; surveillance renforcée | Responsable sécurité IT, Sponsor du projet |
| **Moyen** (écart par rapport aux exigences) | Avertissement documenté ; remédiation sous 30 jours | Chef de projet, Responsable sécurité |
| **Faible** (observation mineure) | Noté pour la prochaine revue | Chef de projet |

## Gestion des exceptions

- Toutes les exceptions nécessitent une justification métier documentée
- Évaluation des risques et contrôles compensatoires obligatoires
- Autorité d'approbation selon le niveau de risque
- Durée maximale : 90 jours (renouvelable avec ré-approbation)
- Exceptions suivies dans le registre central

---

# Alignement réglementaire

| Exigence | nLPD suisse | RGPD UE | ISO 27001 | DORA* |
|----------|------------|---------|-----------|-------|
| Évaluation de la sécurité des fournisseurs | Art. 8 | Art. 28, 32 | A.8.30 | Art. 28 |
| Exigences contractuelles | Art. 8 | Art. 28 | A.5.20 | Art. 30 |
| Tests de sécurité | Art. 8 | Art. 32 | A.8.29 | Art. 24-25 |
| Gestion des sous-traitants | Art. 8 | Art. 28(4) | A.5.21 | Art. 29 |

*DORA applicable lorsque [Organisation] est classifiée comme entité de services financiers.

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur de la Technologie (DT)** | [Nom] | [Date] |
| **Responsable des achats** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de sécurité pour le développement externalisé. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.30.1-3 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
