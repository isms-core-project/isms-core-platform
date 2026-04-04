<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.11-FR:framework:POL:a.8.11 -->
**ISMS-POL-A.8.11 – Masquage des données**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Masquage des données |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.11 |
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
- Confidentialité : Délégué à la Protection des Données (DPD)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.11.1-UG/TG (Inventaire et classification des données)
- ISMS-IMP-A.8.11.2-UG/TG (Sélection des techniques de masquage et exigences)
- ISMS-IMP-A.8.11.3-UG/TG (Évaluation de la couverture des environnements)
- ISMS-IMP-A.8.11.4-UG/TG (Cadre de tests et de validation)
- ISMS-CTX-A.8.11 (Référence technique sur le masquage des données — Référence technique uniquement)
- ISO/IEC 27001:2022 Contrôle A.8.11

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de masquage des données pour protéger la confidentialité des informations sensibles, conformément au Contrôle A.8.11 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à toutes les catégories de données sensibles (DCP, données financières, données de santé, identifiants, données propriétaires) dans tous les environnements (production, test, développement, analyses, formation, sauvegarde) ; toutes les techniques de masquage (caviardage, substitution, tokenisation, pseudonymisation, anonymisation) ; et l'ensemble du personnel organisationnel, contractants et tiers manipulant des données sensibles.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de masquage des données. Cette politique établit QUELLES données nécessitent un masquage, QUELLES techniques sont approuvées et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.11 (variantes UG/TG).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.11 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.11 — Masquage des données**

> *Le masquage des données devrait être utilisé conformément à la politique thématique de l'organisation sur le contrôle d'accès et aux autres politiques thématiques connexes, ainsi qu'aux exigences métier, en tenant compte de la législation applicable.*

**Objectif du contrôle** : Établir la politique organisationnelle pour les contrôles de masquage des données protégeant la confidentialité des informations sensibles en obscurcissant les données lorsque leur visibilité intégrale n'est pas requise à des fins métier légitimes.

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de masquage des données alignées sur la classification des données et l'appétit au risque organisationnel
- **Établit** le cadre de gouvernance pour la prise de décision et la responsabilisation en matière de masquage des données
- **Précise** les techniques de masquage approuvées et les critères de sélection
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00
- **Identifie** les rôles et responsabilités organisationnels pour les contrôles de masquage

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les outils ou produits de masquage** (sélection technologique basée sur l'évaluation des risques)
- **Définit pas les configurations de masquage spécifiques** (voir ISMS-IMP-A.8.11)
- **Fournit pas de procédures spécifiques aux systèmes** (voir ISMS-IMP-A.8.11)
- **Remplace pas la politique de classification des données** (le masquage s'appuie sur le schéma de classification A.5.12)
- **Établit pas les calendriers de conservation des données** (couvert par la politique de conservation A.8.10)
- **Définit pas les mécanismes de contrôle d'accès** (couverts par les politiques A.5.15, A.8.3)
- **Remplace pas les contrôles cryptographiques** (le chiffrement est couvert par la politique de cryptographie A.8.24)

## Périmètre

**Cette politique s'applique à** :

**Toutes les catégories de données sensibles** :

- Données à caractère personnel (DCP) soumises au RGPD/nLPD
- Données financières (numéros de compte, données de cartes de paiement, détails de transactions)
- Données de santé (dossiers médicaux, diagnostics, données de traitement)
- Identifiants d'authentification (mots de passe, jetons, clés API, secrets)
- Informations métier propriétaires (secrets commerciaux, données stratégiques, tarification)
- Toutes données classifiées Confidentielles ou Restreintes selon le schéma de classification de [Organisation]

**Tous les environnements** où des données sensibles existent :

- Systèmes de production (si le masquage est opérationnellement approprié)
- Environnements de test et d'assurance qualité
- Environnements de développement
- Systèmes d'analyse et de reporting
- Environnements de formation et de démonstration
- Entrepôts de données et lacs de données (data lakes)
- Systèmes de sauvegarde et d'archivage

**Tous les cas d'utilisation du masquage** :

- Provisionnement de données pour une utilisation hors production
- Génération et distribution de rapports
- Partage de données avec des tiers
- Développement et test d'applications
- Entraînement de modèles d'apprentissage automatique
- Tests d'acceptation utilisateurs (UAT)
- Analyses et informatique décisionnelle

**Hors périmètre** :

- Informations publiques (données non classifiées ne nécessitant pas de masquage)
- Données classifiées « Public » selon le schéma de [Organisation]
- Protection des données chiffrées (couverte par A.8.24)
- Suppression et destruction des données (couvertes par A.8.10)

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés de masquage |
|----------------|---------------|---------------------------|
| **nLPD suisse** | Toutes les opérations suisses | Art. 8 — Protection des données dès la conception incluant la minimisation des données ; Art. 25 — Mesures techniques et organisationnelles appropriées |
| **RGPD de l'UE** | Lors du traitement de données personnelles UE | Art. 5(1)(c) — Principe de minimisation des données ; Art. 25 — Protection des données dès la conception et par défaut ; Art. 32 — Sécurité du traitement incluant la pseudonymisation |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôle A.8.11 — Politique de masquage des données documentée, contrôles mis en œuvre, preuves d'efficacité |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Condition de déclenchement | Exigences de masquage |
|---------------|---------------------------|----------------------|
| **PCI DSS v4.0.1** | Traitement de données de cartes de paiement | Exig. 3.4 — PAN rendu illisible (masquage, troncature, hachage, tokenisation) ; Exig. 3.5 — PAN masqué lors de l'affichage (au minimum 6 premiers et 4 derniers chiffres) |
| **FINMA** | Établissement financier réglementé en Suisse | Mesures de protection des données clients ; gestion des risques d'externalisation |
| **DORA** | Entité de services financiers UE | Art. 9 — Cadre de gestion des risques TIC incluant les contrôles de protection des données |
| **NIS2** | Entité essentielle/importante (UE) | Art. 21 — Mesures de gestion des risques en cybersécurité incluant la minimisation des données |

---

# Exigences de masquage des données

## Classification des données et portée du masquage

[Organisation] DOIT identifier et classer les données sensibles nécessitant un masquage.

**Principes de classification** :

- La classification des données DOIT être effectuée conformément à ISMS-POL-A.5.12 (Classification des informations)
- Le masquage est appliqué aux données classifiées Confidentielles ou Restreintes lorsque l'accès complet n'est pas requis
- Les données Publiques et Internes peuvent nécessiter un masquage selon le contexte (par ex. environnements hors production)

**Inventaire des données** :

[Organisation] DOIT maintenir un inventaire des données sensibles nécessitant un masquage, documentant :

- Catégorie et classification des données
- Emplacements de stockage et systèmes traitants
- Exigences de masquage applicables
- Propriétaire des données responsable des décisions de masquage
- Statut actuel du masquage et lacunes identifiées

## Techniques de masquage approuvées

[Organisation] met en œuvre les techniques de masquage suivantes selon la classification des données et les exigences réglementaires.

**Tableau des techniques approuvées** :

| Technique | Description | Cas d'utilisation | Réversibilité | Niveau de protection |
|-----------|-------------|------------------|---------------|---------------------|
| **Caviardage (Redaction)** | Remplacement des données sensibles par un espace réservé (par ex. `***`, `XXXXXXXX`) | Affichage/rapports, partage de documents | Non réversible | Élevée |
| **Troncature (Truncation)** | Afficher seulement une partie des données (par ex. `****1234`) | Numéros de carte (PCI), identifiants partiels | Non réversible | Moyenne |
| **Substitution (Substitution)** | Remplacer par des valeurs fictives mais réalistes | Données de test et de développement | Non réversible (sauf correspondance) | Élevée |
| **Pseudonymisation** | Remplacer les identifiants directs par un pseudonyme, table de correspondance stockée séparément | Analytique, recherche, tests | Réversible (avec la table de correspondance) | Élevée |
| **Anonymisation irréversible** | Supprimer ou modifier les données de façon à ce que la réidentification soit impossible | Données de recherche publique, IA/ML | Non réversible | Maximale |
| **Tokenisation** | Remplacer par un jeton opaque sans valeur mathématique | PAN (cartes de paiement), numéros sensibles | Réversible (via le coffre-fort de jetons) | Élevée |
| **Chiffrement des données (masquage dynamique)** | Chiffrement de champs spécifiques en base de données | Stockage de données sensibles avec accès contrôlé | Réversible (avec la clé) | Très élevée |
| **Brouillage (Shuffling)** | Mélanger les valeurs dans une colonne entre les lignes | Données de test préservant les distributions | Non réversible | Moyenne |

**Sélection des techniques** :

La sélection des techniques de masquage DOIT tenir compte de :

- La classification des données (données Restreintes → techniques à protection maximale)
- La réversibilité requise (si la réidentification est nécessaire à des fins légitimes, utiliser la pseudonymisation)
- Les exigences réglementaires applicables (par ex. PCI DSS impose la tokenisation ou le hachage pour le PAN)
- La préservation du format requise (si les données doivent conserver leur format pour les tests applicatifs)
- La cohérence référentielle (les relations entre tables doivent être maintenues dans les données masquées)

## Exigences de couverture des environnements

**Données Restreintes** :

- Production : Masquage ou contrôle d'accès strict (RBAC) requis
- Hors production (dev/test/UAT/analyse) : Masquage OBLIGATOIRE avant utilisation
- Partage externe : Masquage ou anonymisation OBLIGATOIRE

**Données Confidentielles** :

- Production : Masquage requis pour les affichages et rapports accessibles aux utilisateurs sans besoin d'en connaître complet
- Hors production : Masquage OBLIGATOIRE avant utilisation (sauf exception documentée)
- Partage externe : Masquage OBLIGATOIRE

**Données Internes** :

- Production : Masquage recommandé pour les accès sans besoin d'en connaître complet
- Hors production : Masquage recommandé
- Partage externe : Masquage recommandé

**Exigences spécifiques PCI DSS** :

Pour les données de cartes de paiement, indépendamment de la classification :

- Le PAN (Primary Account Number) DOIT être masqué dans tous les affichages à l'exception des personnels nécessitant l'accès complet
- Format d'affichage obligatoire : `****-****-****-1234` (6 premiers + 4 derniers chiffres maximum)
- Les environnements de test NE DOIVENT PAS contenir de PAN réels
- La tokenisation est la méthode préférée pour le stockage des PAN

## Exigences de tests et de validation

[Organisation] DOIT tester et valider l'efficacité du masquage des données.

**Tests obligatoires** :

- **Tests de qualité du masquage** : Vérifier que les données masquées ne permettent pas la réidentification des données originales
- **Tests de préservation fonctionnelle** : Vérifier que les données masquées préservent le format et les propriétés nécessaires aux tests applicatifs
- **Tests de couverture** : Vérifier que toutes les instances des données sensibles sont masquées (aucune donnée résiduelle)
- **Tests de cohérence** : Vérifier que les relations référentielles sont maintenues dans les données masquées
- **Tests de réversibilité** (pour pseudonymisation) : Vérifier que la table de correspondance permet la réidentification autorisée correcte

**Fréquence des tests** :

- Après chaque déploiement initial d'une nouvelle solution de masquage
- Après des changements significatifs des structures de données ou des règles de masquage
- Annuellement pour les environnements de masquage existants
- Après tout incident de masquage identifié

---

# Rôles et responsabilités

| Rôle | Responsabilités clés |
|------|---------------------|
| **RSSI** | Propriétaire de la politique ; supervision de la conformité ; approbation des exceptions |
| **DPD** | Validation de la conformité RGPD/nLPD ; révision des techniques de pseudonymisation/anonymisation |
| **DSI / Opérations IT** | Mise en œuvre technique ; déploiement des outils de masquage ; maintenance |
| **Propriétaires de données** | Identification des données nécessitant un masquage ; autorisation des exceptions ; validation de l'adéquation |
| **Équipes de développement** | Intégration du masquage dans les pipelines de données hors production |
| **Opérations de sécurité** | Surveillance de la conformité au masquage ; réponse aux incidents de masquage |

---

# Gouvernance et conformité

## Métriques de conformité

| Métrique | Cible | Fréquence |
|---------|-------|-----------|
| Couverture de l'inventaire des données sensibles | ≥ 95 % | Trimestrielle |
| Conformité au masquage des données Restreintes en hors production | 100 % | Trimestrielle |
| Conformité au masquage des données Confidentielles en hors production | ≥ 95 % | Trimestrielle |
| Incidents de données non masquées | 0 | Continue |
| Complétion des tests de validation du masquage | 100 % | Par déploiement |

## Gestion des exceptions

Les exceptions aux exigences de masquage DOIVENT être documentées et approuvées formellement.

**Autorité d'approbation des exceptions** :

- Données Restreintes ou de production : RSSI + DPD + Direction générale
- Données Confidentielles : RSSI + DPD
- Données Internes : RSSI
- Durée maximale des exceptions : 12 mois (renouvelable avec réévaluation)

**Exigences des demandes d'exception** :

- Justification métier documentée
- Évaluation des risques avec score résiduel
- Contrôles compensatoires (accès renforcé, surveillance supplémentaire, minimisation des données)
- Calendrier de mise en conformité
- Approbations documentées avec signatures

## Non-conformité

Les violations des exigences de masquage DOIVENT être :

- Signalées immédiatement au RSSI et au DPD
- Classifiées selon leur gravité (critique, élevée, moyenne, faible)
- Traitées comme des incidents de sécurité conformément à ISMS-POL-A.5.24-28
- Analysées pour leurs causes profondes et des mesures correctives mises en œuvre

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.11 v1.0)
- ✅ Signatures d'approbation du RSSI, DPD, Responsable juridique/conformité, Direction générale
- ✅ Classification des données et portée du masquage définies
- ✅ Techniques de masquage approuvées spécifiées
- ✅ Exigences de couverture des environnements documentées
- ✅ Exigences de tests et de validation spécifiées
- ✅ Rôles et responsabilités attribués

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

- Inventaire des données sensibles avec statut du masquage
- Résultats des tests de validation du masquage
- Rapports de couverture des environnements
- Dossiers de demandes d'exception avec approbations
- Rapports d'incidents de masquage et actions correctives

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

---

*Cette politique établit les exigences de masquage des données. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.11 (UG/TG). Les informations de référence technique sont fournies dans ISMS-CTX-A.8.11 (NON SMSI).*

<!-- QA_VERIFIED: 2026-04-02 -->
