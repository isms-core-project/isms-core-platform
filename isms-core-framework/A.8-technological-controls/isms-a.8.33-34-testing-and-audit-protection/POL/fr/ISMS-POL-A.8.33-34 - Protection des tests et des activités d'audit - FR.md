<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.33-34-FR:framework:POL:a.8.33-34 -->
**ISMS-POL-A.8.33-34 — Protection des tests et des activités d'audit**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Protection des tests et des activités d'audit |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.33-34 |
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
| 1.0 | [Date] | RSSI | Politique consolidée initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur des Systèmes d'Information (DSI) / Responsable des opérations IT
- Confidentialité : Délégué à la Protection des Données (DPD)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale (PDG)

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.8.11 (Masquage des données)
- ISMS-POL-A.8.31 (Séparation des environnements)
- ISMS-IMP-A.8.33-34.1-UG (Protection des données de test — Guide utilisateur)
- ISMS-IMP-A.8.33-34.1-TG (Protection des données de test — Spécification technique)
- ISMS-IMP-A.8.33-34.2-UG (Gestion des activités d'audit — Guide utilisateur)
- ISMS-IMP-A.8.33-34.2-TG (Gestion des activités d'audit — Spécification technique)
- ISO/IEC 27001:2022 Contrôles A.8.33 et A.8.34

---

# Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la protection des informations de test et la protection des systèmes d'information lors des activités d'audit, conformément aux Contrôles A.8.33 et A.8.34 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à toutes les activités de sélection et de protection des données de test, toutes les activités d'audit et de tests de sécurité, tous les environnements où des tests sont réalisés, et tout le personnel impliqué dans les activités de test et d'audit.

**Objet** : Définir les exigences organisationnelles pour les contrôles de protection des données de test et des tests d'audit, établissant QUELLES protections sont requises et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.33-34.

**Principes fondateurs** :

- Les données de test NE DOIVENT PAS contenir de DCP ou de données sensibles de production non protégées
- Les données de production utilisées pour les tests DOIVENT être masquées ou anonymisées
- Les environnements de test DOIVENT être isolés des systèmes de production
- Les tests d'audit DOIVENT être planifiés pour minimiser les perturbations opérationnelles
- Les outils et journaux d'audit DOIVENT être protégés et contrôlés

**Alignement réglementaire** : Conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022, avec des exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA) le cas échéant.

---

# Périmètre

## Dans le périmètre

**Contrôle A.8.33 — Informations de test** :

- Toutes les données de test utilisées dans les environnements de développement, d'assurance qualité, de préproduction et de formation
- Copies de données de production utilisées à des fins de test
- Données de test synthétiques et générées
- Bases de données et référentiels de données de test
- Données de tests d'acceptation utilisateurs (UAT)
- Jeux de données pour les tests de performance et de charge
- Données de tests de sécurité

**Contrôle A.8.34 — Tests d'audit** :

- Audits et évaluations de sécurité internes
- Audits de certification externe (ISO 27001)
- Tests d'intrusion et évaluations de vulnérabilités
- Analyses de conformité technique
- Évaluations de sécurité par des tiers
- Audits de conformité réglementaire

**Environnements** : développement, test/assurance qualité, préproduction, formation, sandbox.

## Hors périmètre

- Opérations en environnement de production (couvertes par les politiques opérationnelles)
- Activités de surveillance de routine (couvertes par A.8.16)
- Spécifications des techniques de masquage des données (couvertes par A.8.11)
- Exigences d'architecture des environnements (couvertes par A.8.31)

---

# Énoncés de politique — Contrôle A.8.33 : Informations de test

## Exigences de sélection des données de test

**Principe de base — Absence de données réelles**

[Organisation] NE DOIT PAS utiliser de données de production opérationnelles (en direct) contenant des DCP ou des informations sensibles pour les tests sans approbation explicite et protection.

**Sources de données préférées** (par ordre de préférence) :

1. Données synthétiques — générées artificiellement, aucun lien avec de vraies données
2. Données anonymisées — données de production irréversiblement dé-identifiées
3. Données masquées/pseudonymisées — données de production protégées (nécessite une approbation)

**Justification** : Les données de production non protégées dans les environnements de test créent des risques de violation de données, de non-conformité réglementaire et d'exposition aux accès non autorisés.

## Exigences de classification des données de test

Les données de test DOIVENT être classifiées selon le schéma de classification de [Organisation] :

- **Données synthétiques** (sans source de données de production) : Classifiées Publiques ou Internes selon le contexte métier
- **Données dérivées de la production** (masquées, anonymisées ou pseudonymisées) : Héritent de la classification de production jusqu'à ce que la validation du masquage confirme la non-réversibilité, puis PEUVENT être déclassifiées avec l'approbation du Propriétaire des données
- **Copies directes de la production** (pendant le processus d'actualisation) : Classifiées Restreintes jusqu'à l'application du masquage
- La classification détermine les exigences de protection et les contrôles d'accès

## Exigences de protection des données

**Masquage des données de production**

Lorsque des données de production sont requises pour les tests, [Organisation] DOIT appliquer le masquage des données conformément à ISMS-POL-A.8.11 :

- Les DCP DOIVENT être masquées, anonymisées ou remplacées par des valeurs synthétiques
- Les données financières (numéros de compte, cartes de paiement) DOIVENT être masquées
- Les identifiants et secrets DOIVENT être remplacés par des valeurs de test
- Les données de santé DOIVENT être dé-identifiées conformément aux réglementations applicables

**Validation du masquage** : Les données masquées DOIVENT être validées pour confirmer que les valeurs sensibles originales ne sont pas récupérables, que le format des données est préservé et que l'intégrité référentielle est maintenue.

**Exigences de tests de validation** :

- Les tests de validation DOIVENT inclure : (1) Comparaison avec des échantillons de données de production pour détecter les similitudes de patterns, (2) Analyse statistique pour confirmer les différences de distribution par rapport à la production, (3) Vérification qu'aucune DCP en clair n'existe dans les exports de bases de données de test
- Les résultats de validation DOIVENT être documentés et approuvés par le Responsable de la sécurité de l'information avant utilisation en environnement de test

**Isolation des données de test**

Les données de test DOIVENT être isolées de la production :

- Les bases de données de test DOIVENT être logiquement ou physiquement séparées de la production
- Aucun chemin d'accès direct entre les stockages de données de test et de production
- Les exports de données de test DOIVENT être contrôlés et journalisés
- Les procédures d'actualisation des données DOIVENT inclure le re-masquage

## Exigences relatives aux environnements de test

**Séparation des environnements**

[Organisation] DOIT maintenir des environnements de test séparés conformément à ISMS-POL-A.8.31 :

- Les environnements de développement, test et production DOIVENT être séparés
- La segmentation réseau DOIT empêcher les accès non autorisés entre environnements
- Des identifiants distincts DOIVENT être requis pour chaque environnement

**Contrôles d'accès**

L'accès aux environnements de test contenant des données sensibles DOIT :

- Respecter les principes du moindre privilège
- Nécessiter une autorisation explicite basée sur la fonction professionnelle
- Être révisé au moins annuellement
- Être révoqué en cas de changement de rôle ou de résiliation

## Cycle de vie des données de test

**Conservation des données**

Les données de test contenant des données de production masquées DOIVENT :

- N'être conservées que pendant la durée des besoins de test
- Être supprimées dans les 30 jours suivant la complétion du projet

Pour les environnements de test continus :

- La conservation des données de test DOIT être révisée trimestriellement
- Les données de test de plus de 90 jours sans utilisation active documentée DOIVENT être supprimées sauf exception documentée (maximum 12 mois)
- Une surveillance automatisée de la conservation DOIT signaler les données dépassant les seuils

**Actualisation des données de test**

Lors de l'actualisation des données de test depuis la production :

- Le masquage DOIT être appliqué avant que les données soient accessibles dans l'environnement de test
- Les procédures d'actualisation DOIVENT être documentées et approuvées
- Les activités d'actualisation DOIVENT être journalisées à des fins d'audit
- L'approbation du Propriétaire des données est requise pour les actualisations planifiées

---

# Énoncés de politique — Contrôle A.8.34 : Tests d'audit

## Exigences de planification des audits

**Accord préalable à l'audit**

[Organisation] DOIT établir un accord formel avant tout test d'audit :

- Périmètre des systèmes et informations à tester
- Méthodologies et outils de test à utiliser
- Calendrier et durée des activités de test
- Procédures d'escalade pour les problèmes découverts
- Exigences de confidentialité pour les résultats d'audit

**La direction et l'auditeur/évaluateur DOIVENT approuver conjointement le périmètre et les méthodes de test avant le début des tests.**

**Calendrier et planification**

Les activités de test d'audit DOIVENT être planifiées pour minimiser l'impact opérationnel :

- Les périodes d'activité métier critique DOIVENT être évitées
- Les fenêtres de test DOIVENT être coordonnées avec les Opérations IT
- Les parties prenantes DOIVENT être notifiées des activités de test planifiées
- Les tests d'urgence DOIVENT suivre un processus d'approbation accéléré

## Exigences de contrôle d'accès

**Accès des auditeurs**

L'accès accordé aux auditeurs et évaluateurs DOIT :

- Être limité au périmètre convenu dans l'accord préalable à l'audit
- Par défaut en lecture seule pour les informations et les logiciels
- Nécessiter une AMF pour l'accès aux systèmes sensibles
- Être limité dans le temps à la durée de l'audit
- Être journalisé et surveillé tout au long de la mission

**Sécurité des appareils**

Les appareils utilisés par les auditeurs pour accéder aux systèmes de [Organisation] DOIVENT :

- Répondre aux exigences minimales de sécurité de [Organisation]
- Disposer d'une protection des postes de travail et de correctifs à jour
- Ne pas introduire de logiciels malveillants ou non autorisés
- Être vérifiés avant l'octroi de l'accès

## Contrôles des tests

**Limites des tests**

Les activités de test d'audit DOIVENT :

- Rester dans les limites du périmètre convenu
- Ne pas accéder aux systèmes ou données hors du périmètre défini
- Être immédiatement suspendues en cas d'impact involontaire
- Être suspendues si des problèmes critiques affectant les opérations sont découverts

**Contrôles des tests d'intrusion**

Les tests d'intrusion et les tests de sécurité actifs DOIVENT :

- Être autorisés par écrit par la direction compétente
- Être conduits dans des environnements isolés ou hors production si possible
- Inclure des procédures de retour arrière et de récupération
- Avoir les Opérations IT en attente pendant les tests actifs
- Suivre les règles d'engagement convenues

## Protection des données et des journaux

**Traitement des données d'audit**

Les données consultées ou collectées pendant les audits DOIVENT :

- Être protégées selon leur classification
- Ne pas être conservées plus longtemps que nécessaire aux fins d'audit
- Être supprimées de manière sécurisée après l'achèvement de l'audit
- Être soumises à des accords de confidentialité

**Protection des journaux d'audit**

Les journaux générés pendant les activités d'audit DOIVENT :

- Être protégés contre toute modification ou suppression non autorisée
- Être conservés conformément à la politique de conservation des journaux de [Organisation]
- Être disponibles pour révision si les résultats d'audit sont contestés
- Être inclus dans la surveillance de sécurité pendant la période de test

## Réponse aux incidents pendant les audits

**Gestion des incidents**

Si les tests d'audit causent un impact involontaire :

- Les tests DOIVENT être immédiatement suspendus
- Les Opérations IT DOIVENT être notifiées pour le confinement
- La cause profonde DOIT être documentée
- La reprise nécessite une approbation explicite du Responsable des opérations IT

**Découverte de vulnérabilités**

Les vulnérabilités découvertes pendant les tests d'audit DOIVENT :

- Être immédiatement signalées à l'Équipe sécurité si critiques
- Être documentées dans les résultats d'audit
- Être traitées conformément au processus de gestion des vulnérabilités de [Organisation]
- Ne pas être exploitées au-delà de ce qui est nécessaire pour la vérification

---

# Rôles et responsabilités

## Rôles de gouvernance

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approuver le périmètre des tests d'audit ; autoriser les tests d'intrusion |
| **Responsable des opérations IT** | Protection de la production ; planification des audits ; réponse aux incidents pendant les tests |
| **DPD** | Conformité à la vie privée des données de test ; approbation de l'anonymisation ; alignement réglementaire |
| **Responsable de la sécurité de l'information** | Coordination des audits ; normes de test ; maintenance de la politique |
| **Audit interne** | Planification des audits ; gestion des missions ; rapport des résultats |

## Rôles opérationnels

| Rôle | Responsabilités |
|------|----------------|
| **Propriétaires de données** | Autorisation des données de test ; approbation du masquage ; décisions de classification |
| **Responsable du développement** | Gestion des environnements de test ; procédures de données de test ; conformité des développeurs |
| **Responsable de l'assurance qualité** | Qualité des données de test ; conformité aux processus de test ; supervision de l'UAT |
| **Équipe sécurité** | Gestion des outils d'audit ; coordination des tests d'intrusion ; gestion des vulnérabilités |
| **Auditeurs externes** | Conformité aux restrictions d'accès ; confidentialité ; respect du périmètre |

---

# Conformité et application

## Exigences d'évaluation

| Type d'évaluation | Fréquence | Partie responsable |
|-------------------|-----------|-------------------|
| Inventaire des données de test | Trimestrielle | Responsables développement/assurance qualité |
| Revue des environnements de test | Semestrielle | Opérations IT, Équipe sécurité |
| Revue des procédures d'audit | Annuelle | Audit interne, RSSI |
| Évaluation de la conformité | Annuelle | Responsable de la sécurité de l'information |

## Mécanismes de vérification

[Organisation] vérifie la conformité par :

- Analyse automatisée des données sensibles dans les environnements de test
- Revues des journaux d'accès aux environnements de test
- Revues de la documentation des missions d'audit
- Validation de l'efficacité du masquage des données de test
- Vérification de la complétion de la liste de contrôle pré-audit

## Non-conformité

Les violations de cette politique peuvent entraîner :

- Suspension immédiate des activités de test
- Révocation de l'accès pour le personnel non conforme
- Mesures disciplinaires conformément aux politiques RH
- Résiliation du contrat pour les tiers violateurs
- Signalement d'incident en cas de violation réglementaire

---

# Gestion des exceptions

## Critères d'exception

Des exceptions PEUVENT être approuvées uniquement pour :

- Systèmes hérités nécessitant des données de production pour un débogage spécifique
- Exigences réglementaires imposant des approches de test spécifiques
- Limitations techniques empêchant les approches de masquage standard

## Processus d'exception

1. **Demande** : Le demandeur documente la justification métier, l'évaluation des risques et les contrôles compensatoires
2. **Revue** : L'Équipe sécurité valide la nécessité technique et évalue les contrôles compensatoires
3. **Approbation** : RSSI (données de test) ou Responsable des opérations IT (calendrier d'audit) approuve avec conditions
4. **Suivi** : Exception suivie avec date d'expiration et calendrier de révision
5. **Surveillance** : Contrôles compensatoires vérifiés tout au long de la période d'exception

---

# Alignement réglementaire

| Réglementation | Informations de test (A.8.33) | Tests d'audit (A.8.34) |
|----------------|------------------------------|----------------------|
| **nLPD suisse** | Art. 8 — Protection des données dès la conception ; minimisation des DCP dans les tests | Art. 8 — Mesures techniques appropriées pendant le traitement |
| **RGPD de l'UE** | Art. 5(1)(c) — Minimisation des données ; Art. 25 — Confidentialité dès la conception ; Art. 32 — Pseudonymisation | Art. 32 — Sécurité du traitement ; tests comme mesure de sécurité |
| **ISO 27001:2022** | Contrôle A.8.33 | Contrôle A.8.34 |
| **PCI DSS v4.0.1** | Exig. 3.4 — Masquage des données de test | Exig. 11 — Exigences de tests de sécurité |

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Anonymisation** | Processus irréversible supprimant toutes les informations identifiantes rendant la réidentification impossible |
| **Test d'audit** | Examen systématique des systèmes, contrôles et processus pour vérifier la conformité et l'efficacité |
| **Masquage des données** | Processus d'obscurcissement des données originales avec un contenu modifié tout en maintenant le format et la facilité d'utilisation |
| **Test d'intrusion** | Attaque simulée autorisée sur des systèmes pour identifier des vulnérabilités de sécurité |
| **Données de production** | Données opérationnelles en direct des systèmes métier contenant de vraies informations |
| **Pseudonymisation** | Remplacement des identifiants par des pseudonymes ; réidentifiable avec une clé distincte |
| **Données synthétiques** | Données artificiellement générées ne contenant aucune vraie information personnelle ou métier |
| **Environnement de test** | Système hors production utilisé à des fins de développement, de test ou de formation |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date à définir] |
| **Responsable des opérations IT** | [Nom] | [Date à définir] |
| **Délégué à la Protection des Données (DPD)** | [Nom] | [Date à définir] |
| **Responsable de l'audit interne** | [Nom] | [Date à définir] |
| **Responsable juridique/conformité** | [Nom] | [Date à définir] |
| **Direction générale (PDG)** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de protection des tests et des activités d'audit. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.33-34.1-UG/TG et ISMS-IMP-A.8.33-34.2-UG/TG.*

<!-- QA_VERIFIED: 2026-04-02 -->
