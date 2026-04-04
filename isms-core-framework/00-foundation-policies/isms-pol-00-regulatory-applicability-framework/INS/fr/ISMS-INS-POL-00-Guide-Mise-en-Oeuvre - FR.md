# ISMS-INS-POL-00 — Guide de mise en œuvre
## POL-00 : Cadre d'applicabilité réglementaire

**Date :** 2026-02-17
**Objet :** Guide pratique de mise en œuvre pour les organisations adoptant POL-00
**Public :** RSSI, Juriste/Responsable de la conformité, DPD, Responsable de la mise en œuvre

---

## 1. Ce que fait réellement POL-00 (en langage clair)

POL-00 répond à une seule question : **quelles réglementations s'appliquent à cette organisation, et avec quelle force ?**

Sans ce cadre, chaque auteur de politique du SMSI décide indépendamment de référencer ou non le RGPD, DORA, la FINMA ou le NIST. Le résultat est l'incohérence — certaines politiques citent des réglementations qui ne s'appliquent pas, d'autres omettent des réglementations qui s'appliquent, et les auditeurs passent l'Étape 1 à démêler le tout.

POL-00 résout cela en établissant trois niveaux une seule fois, de manière centralisée :

- **Niveau 1 (Obligatoire)** — s'applique indépendamment de l'activité métier. Non négociable.
- **Niveau 2 (Conditionnel)** — ne s'applique que si des déclencheurs métier spécifiques sont remplis. Nécessite une détermination délibérée.
- **Niveau 3 (Informatif)** — référence de bonnes pratiques uniquement. Aucune obligation de conformité.

Les 53 politiques de contrôle de l'Annexe A héritent ensuite de cette catégorisation par référence à POL-00. La détermination du niveau est effectuée une seule fois, par Juridique/Conformité, et toutes les politiques utilisent cette détermination de manière cohérente.

**La valeur opérationnelle** : lorsqu'une nouvelle réglementation émerge, vous mettez à jour POL-00 (un seul document), et le changement se propage logiquement à toutes les politiques de contrôle. Vous ne touchez pas aux 53 politiques individuellement.

---

## 2. La partie difficile : effectuer les déterminations du Niveau 2

Le Niveau 1 est simple pour une organisation suisse — la nLPD et l'ISO 27001 sont effectivement obligatoires si vous poursuivez la certification et opérez en Suisse. Le RGPD est obligatoire si vous traitez des données personnelles de résidents de l'UE (pour la plupart des organisations suisses, la réponse est oui).

**Le Niveau 2 est là où se concentre le vrai travail.** Ces déterminations nécessitent du jugement, des connaissances juridiques et une évaluation honnête du modèle d'affaires de l'organisation. Se tromper a des conséquences dans les deux sens :

- **Sur-application** (appliquer le Niveau 2 sans que le déclencheur soit rempli) : surcharge de conformité inutile, dorure du lys, coût sans bénéfice
- **Sous-application** (manquer un déclencheur qui est rempli) : exposition réglementaire, mesures d'exécution potentielles, non-conformité d'audit

### Liste de contrôle pour les décisions du Niveau 2

Traitez chaque réglementation dans l'ordre. Pour chacune, répondez honnêtement à la question déclenchante. En cas d'incertitude, Juridique/Conformité tranche et documente le raisonnement.

---

#### FINMA (Autorité fédérale de surveillance des marchés financiers)

**Question déclenchante :** L'organisation est-elle une entité supervisée par la FINMA ?

Les entités supervisées par la FINMA comprennent : les banques, les compagnies d'assurance, les maisons de titres, les bourses, les sociétés de gestion de fonds, les placements collectifs, les infrastructures des marchés financiers, les prestataires de services de paiement réglementés par la LSFin/LEFin.

| Réponse | Niveau | Action |
|---------|--------|--------|
| Oui — directement supervisé par la FINMA | Niveau 2 Actif | Appliquer les exigences de la Circulaire FINMA 2023/1 ; documenter dans la DdA |
| Oui — prestataire TIC d'une entité FINMA | Niveau 2 Actif | Les règles d'externalisation FINMA s'appliquent ; évaluer les exigences de sous-externalisation |
| Non | Niveau 2 Non actif | Documenter « n'est pas une entité supervisée par la FINMA » dans la Matrice d'applicabilité réglementaire |

**Erreur fréquente :** Les PME fournissant des services informatiques à des banques supposent que la FINMA ne s'applique pas. Si la banque classe votre service comme externalisation matérielle au sens de la Circulaire FINMA 2023/1, les exigences FINMA s'appliquent contractuellement. Vérifiez le contrat cadre de services.

---

#### DORA (Digital Operational Resilience Act)

**Question déclenchante :** L'organisation est-elle une entité financière ou un prestataire tiers de services TIC (PSTI) auprès d'entités financières de l'UE ?

Les entités financières de l'UE au sens de DORA comprennent : les banques, les compagnies d'assurance, les entreprises d'investissement, les établissements de paiement, les établissements de monnaie électronique, les prestataires de services sur crypto-actifs, entre autres. Les dispositions DORA relatives aux PSTI s'appliquent aux fournisseurs de services TIC critiques ou importants pour ces entités.

| Réponse | Niveau | Action |
|---------|--------|--------|
| Entité financière de l'UE | Niveau 2 Actif | Applicabilité totale de DORA incluant les tests TLPT |
| Prestataire de services TIC désigné critique/important par l'entité financière | Niveau 2 Actif | Le Chapitre V de DORA (cadre de surveillance) s'applique |
| Prestataire de services TIC — pas encore désigné | Niveau 2 Veille | Surveiller ; déterminer si des exigences DORA contractuelles découlent des accords clients |
| Aucun lien avec des entités financières de l'UE | Niveau 2 Non actif | Documenter la détermination ; réviser annuellement |

**Date d'entrée en vigueur de DORA :** 17 janvier 2025. Si Niveau 2 Actif, les exigences devraient déjà être en place ou en cours de mise en œuvre.

**Erreur fréquente :** Les prestataires TIC suisses de banques européennes supposent que DORA ne s'applique pas car ils ne sont pas établis dans l'UE. La portée extraterritoriale de DORA couvre les prestataires TIC non-UE servant des entités financières de l'UE. Vérifiez votre liste de clients.

---

#### NIS2 (Directive sur la sécurité des réseaux et des systèmes d'information 2)

**Question déclenchante :** L'organisation opère-t-elle dans un secteur listé à l'Annexe I ou II de NIS2, et satisfait-elle au seuil de taille ?

NIS2 s'applique aux **Entités essentielles** (Annexe I : énergie, transport, banque, santé, eau, infrastructures numériques, administration publique, espace) et aux **Entités importantes** (Annexe II : services postaux, gestion des déchets, alimentation, fabrication, fournisseurs numériques, recherche).

Seuil de taille : moyennes entreprises (50+ salariés OU 10 M€+ de chiffre d'affaires annuel) dans les secteurs couverts. Les entités plus petites uniquement si spécifiquement désignées par l'État membre.

| Réponse | Niveau | Action |
|---------|--------|--------|
| Secteur dans le périmètre + satisfait le seuil de taille | Niveau 2 Actif | Mesures de cybersécurité NIS2 (Article 21) et signalement d'incidents (Article 23) s'appliquent |
| Secteur dans le périmètre + sous le seuil | Niveau 2 Veille | Surveiller ; les États membres peuvent étendre le périmètre |
| Secteur hors périmètre | Niveau 2 Non actif | Documenter la détermination |

**Pour les organisations suisses :** NIS2 est du droit de l'UE. Elle s'applique directement uniquement si l'organisation a des opérations dans l'UE ou fournit des services à des entités dans le périmètre de l'UE. La Suisse a sa propre révision de la LSI (Loi sur la sécurité de l'information) — évaluez les deux.

---

#### PCI DSS v4.0.1

**Question déclenchante :** L'organisation stocke-t-elle, traite-t-elle ou transmet-elle des données de titulaires de carte (numéros de carte de paiement, CVV, codes PIN) ?

C'est binaire. Il n'y a pas de seuil — toute organisation qui manipule des données de carte est dans le périmètre.

| Réponse | Niveau | Action |
|---------|--------|--------|
| Oui — toute donnée de carte traitée | Niveau 2 Actif | Déterminer le niveau SAQ ; appliquer les exigences pertinentes à l'environnement de données des titulaires de carte (CDE) |
| Non — entièrement externalisé à un PSP (p. ex. Stripe, PayPal), aucune donnée de carte ne touche les systèmes propres | Niveau 2 Réduit | Périmètre SAQ-A uniquement ; vérifier l'approche tokenisation/redirection |
| Aucun traitement de carte | Niveau 2 Non actif | Documenter la détermination |

**Erreur fréquente :** Supposer que l'utilisation d'un processeur de paiement supprime toute obligation PCI DSS. Si vos systèmes redirigent vers une page de paiement hébergée et ne voient jamais les données de carte, SAQ-A s'applique (simplifié). Si vos systèmes voient des données de carte en transit, le périmètre complet s'applique.

---

#### Règlement de l'UE sur l'IA (EU AI Act)

**Question déclenchante :** L'organisation développe-t-elle, déploie-t-elle ou utilise-t-elle des systèmes d'IA dans l'UE ?

| Réponse | Niveau | Action |
|---------|--------|--------|
| Développe ou déploie des systèmes d'IA interdits | Non autorisé | Arrêt complet |
| Développe ou déploie une IA à haut risque (Annexe III) | Niveau 2 Actif | Évaluation de conformité, enregistrement, documentation technique requis |
| Déploie une IA à usage général dans un contexte à haut risque | Niveau 2 Actif | Obligations au titre de l'Article 50 (transparence) et évaluation du cas d'usage |
| Utilise des outils d'IA (p. ex. Microsoft Copilot, ChatGPT) en tant que déployeur | Niveau 2 Veille | Surveiller ; des obligations de transparence et de supervision humaine s'appliquent |
| Aucun développement ou déploiement d'IA | Niveau 2 Non actif | Documenter ; réviser annuellement — l'adoption de l'IA évolue rapidement |

**Note sur le calendrier :** Les obligations pour l'IA à haut risque sont progressivement introduites à partir d'août 2025. Les dispositions sur l'IA interdite sont actives depuis février 2025. Les dates de conformité sont des cibles mobiles — consultez le calendrier de publication des actes délégués.

---

#### HIPAA / FISMA / CCPA (fédéral américain / États américains)

Ces textes ne s'appliquent que si l'organisation :
- Traite des données de santé protégées de personnes américaines (HIPAA)
- Est une agence fédérale américaine ou un prestataire fédéral (FISMA)
- Collecte des données personnelles de résidents de Californie et satisfait aux seuils de chiffre d'affaires/volume de données (CCPA)

Pour la plupart des organisations basées en Suisse sans opérations aux États-Unis, ces textes sont **Niveau 3 (Informatifs)**. Documentez la détermination. Révisez si une expansion sur le marché américain est planifiée.

---

## 3. Configuration initiale — Compléter la Matrice d'applicabilité réglementaire

La Matrice d'applicabilité réglementaire (POL-00 Section 8.2) est l'enregistrement formel des déterminations de niveau. Avant de la compléter, répondez à ces questions organisationnelles :

**À propos de l'organisation :**
1. Enregistrée en Suisse ? (nLPD = Niveau 1)
2. Traite des données personnelles de résidents de l'UE ? (RGPD = Niveau 1 ou 2 selon le volume/la nature)
3. Entité supervisée par la FINMA ou prestataire TIC matériel d'une telle entité ? (FINMA Niveau 2)
4. Fournit des services TIC à des entités financières de l'UE ? (DORA Niveau 2)
5. Opère dans un secteur NIS2 Annexe I/II avec 50+ salariés ou 10 M€+ de chiffre d'affaires ? (NIS2 Niveau 2)
6. Stocke, traite ou transmet des données de titulaires de carte de paiement ? (PCI DSS Niveau 2)
7. Développe, déploie ou utilise des systèmes d'IA dans l'UE ? (EU AI Act Niveau 2 Veille/Actif)
8. Données de santé américaines, contrats fédéraux ou clientèle en Californie ? (HIPAA/FISMA/CCPA Niveau 2 ou 3)

**Séquence :**
1. Le RSSI et Juridique/Conformité travaillent ensemble sur la liste de contrôle ci-dessus
2. Juridique/Conformité effectue les déterminations du Niveau 2 et documente le raisonnement
3. Le DPD valide les déterminations liées à la vie privée (RGPD, nLPD, EU AI Act)
4. La matrice est complétée avec le niveau + le raisonnement de la détermination pour chaque réglementation
5. La Direction générale approuve et signe la matrice
6. La matrice est datée et signée — elle devient la preuve d'audit pour l'Étape 1

**La matrice n'a pas besoin d'être parfaite.** Elle doit être délibérée. Un auditeur acceptera une détermination raisonnée selon laquelle DORA ne s'applique pas, étayée par une évaluation documentée de la base clients. Il n'acceptera pas « nous n'y avons pas pensé ».

---

## 4. Le journal de surveillance trimestriel (en pratique)

La Section 4.3 de POL-00 exige une surveillance trimestrielle du paysage réglementaire. C'est la preuve que les déterminations de niveau sont maintenues à jour.

**Ce que la surveillance signifie concrètement :**

Elle ne signifie pas faire appel à une équipe juridique pour mener des recherches réglementaires chaque trimestre. Elle signifie :

1. Examiner un ensemble sélectionné de sources de surveillance réglementaire (POL-00 Annexe — Sources de surveillance réglementaire)
2. Confirmer si des développements réglementaires significatifs se sont produits dans le trimestre
3. Évaluer si des développements affectent les déterminations de niveau actuelles
4. Documenter la révision et signer

**Modèle pour une entrée de journal trimestriel type (aucun changement) :**

```
JOURNAL DE SURVEILLANCE RÉGLEMENTAIRE — T[X] [ANNÉE]
Période : [JJ.MM.AAAA] au [JJ.MM.AAAA]

Sources de surveillance examinées :
☑ PFPDT (Préposé fédéral à la protection des données et à la transparence) — actualités et orientations
☑ FINMA — circulaires et mises à jour d'orientations
☑ EUR-Lex / Journal officiel UE — actes d'exécution DORA/NIS2/EU AI Act
☑ PCI Security Standards Council — mises à jour DSS
☑ ENISA — orientations de mise en œuvre NIS2

Constats :
Aucun développement réglementaire significatif affectant les déterminations
actuelles des Niveaux 1/2/3 n'a été identifié au cours de ce trimestre.

Évaluation déclenchée requise : Non

Examiné par : [Nom du Juriste/Responsable de la conformité]     Date : [JJ.MM.AAAA]
Confirmé par : [Nom du RSSI]                                     Date : [JJ.MM.AAAA]
```

**En cas de changement :** Documentez le changement, évaluez quelles déterminations de niveau ou politiques de contrôle sont affectées, déclenchez le processus de changement POL-01 Section 5.2, et enregistrez la référence de l'évaluation déclenchée.

**Le plus important concernant le journal :** Faites-le à la même date chaque trimestre. Définissez un rendez-vous récurrent dans le calendrier. Un journal constamment daté (fin mars, juin, septembre, décembre) paraît délibéré. Un journal aux dates irrégulières semble être une reconstitution après coup.

---

## 5. Évaluations déclenchées — Quand réévaluer en dehors du cycle trimestriel

Les événements métier suivants doivent déclencher une réévaluation immédiate en dehors du cycle trimestriel (POL-00 Section 5) :

| Événement | Quoi évaluer |
|-----------|-------------|
| Entrée dans un nouveau marché (UE, États-Unis, etc.) | Nouvelles obligations réglementaires dans cette juridiction |
| Acquisition ou fusion avec une autre entité | Les obligations réglementaires de l'entité cible sont transférées |
| Lancement d'un nouveau produit traitant des données personnelles | Périmètre RGPD/nLPD, EU AI Act si activé par l'IA |
| Début du traitement de données de titulaires de carte de paiement | Déclencheur PCI DSS |
| Obtention d'un contrat avec une entité financière de l'UE | Dispositions ITSP DORA |
| Franchissement de 50 salariés ou 10 M€ de chiffre d'affaires | Seuil de taille NIS2 franchi |
| Mise à jour réglementaire significative (mesure d'exécution, nouvelle orientation) | Détermination de niveau affectée |

Les évaluations déclenchées utilisent la même méthodologie d'évaluation que la révision trimestrielle mais sont documentées séparément. Référencez l'événement déclencheur, le résultat de l'évaluation et si un processus de changement POL-01 a été initié.

---

## 6. Liens avec les autres documents

**→ POL-01 (Cadre de gouvernance et de prise de décision du SMSI)**
POL-00 génère le *quoi* (quelles réglementations s'appliquent). POL-01 régit le *processus* de changement de cette détermination. Lorsqu'un journal de surveillance trimestriel identifie un changement réglementaire significatif, le processus de changement en 6 étapes de la Section 5.2 de POL-01 est déclenché. Les deux politiques fonctionnent en binôme.

**→ Déclaration d'Applicabilité (DdA)**
Les déterminations des Niveaux 1 et 2 Actifs influencent directement les sélections de contrôles de la DdA. DORA actif → les contrôles de résilience (A.5.29, A.5.30, A.8.13, A.8.14) sont probablement obligatoires. PCI DSS actif → les contrôles de chiffrement et d'accès (A.8.24, A.8.2, A.5.15) reçoivent une justification supplémentaire. La DdA devrait référencer POL-00 comme source de justification d'inclusion de contrôles.

**→ Politiques de contrôle de l'Annexe A**
Les politiques de contrôle n'ont pas besoin d'énumérer individuellement chaque réglementation applicable. Elles référencent POL-00 pour le cadre réglementaire et citent des réglementations spécifiques uniquement lorsque celles-ci entraînent une exigence de contrôle spécifique (p. ex. l'Article 32 RGPD dans la politique de chiffrement A.8.24).

**→ ISMS-CHK-POL-00 (si créé)**
Un classeur d'évaluation de conformité pour POL-00 vérifierait GOV-05 à GOV-08 dans le classeur ISMS-CHK-POL-01 — spécifiquement que la surveillance trimestrielle est effectuée, que les évaluations déclenchées sont documentées et que les justifications de la DdA sont complètes. POL-00 ne dispose pas actuellement de son propre classeur d'évaluation ; ces exigences sont évaluées via ISMS-CHK-POL-01.

---

## 7. Preuves pour les auditeurs

### Étape 1 (Revue documentaire)

L'auditeur souhaite voir que les obligations réglementaires sont explicitement identifiées et catégorisées. Preuves :

- [X] POL-00 v1.0 — approuvé, signé, daté
- [X] Matrice d'applicabilité réglementaire (Section 8.2) — complétée avec les déterminations de niveau et le raisonnement pour chaque réglementation
- [X] Documentation des déterminations du Niveau 2 — justification écrite des décisions Actif/Non actif pour chaque réglementation conditionnelle
- [X] Signatures d'approbation — RSSI, Juridique/Conformité, DPD, Direction générale

**Ce que les auditeurs relèvent à l'Étape 1 :** Déterminations du Niveau 2 manquantes ou vagues (« DORA — en cours d'examen »), matrices non signées, incohérence entre les déterminations de niveau POL-00 et les sélections de contrôles de la DdA.

### Étape 2 (Efficacité opérationnelle)

L'auditeur souhaite voir que POL-00 est réellement maintenu. Preuves :

- [X] Journaux de surveillance trimestriels — minimum 4 trimestres (ou depuis la création du SMSI si moins d'un an)
- [X] Chaque journal signé par Juridique/Conformité + RSSI
- [X] Au moins un enregistrement d'évaluation déclenchée (si un événement métier pertinent s'est produit)
- [X] Preuve que la DdA a été mise à jour suite à tout changement de détermination de niveau

**Ce que les auditeurs relèvent à l'Étape 2 :** Journaux trimestriels qui semblent être des gabarits non réellement examinés (texte identique sur les 4 trimestres sans variation), signatures manquantes, absence de réponse à des développements réglementaires connus (p. ex. la date d'entrée en vigueur de DORA passe sans qu'aucune entrée de journal ne la reconnaisse).

---

## 8. Observations de mise en œuvre

### 8.1 Le trimestre « aucun changement » est acceptable — mais variez le libellé

Quatre entrées de journal trimestriel identiques avec du texte copié-collé ressemble à un exercice de case à cocher. Les auditeurs le remarquent. Même lorsque rien de substantiel n'a changé, variez ce qui a été examiné, notez des documents d'orientation spécifiques consultés et mentionnez tout développement évalué et jugé non significatif.

### 8.2 RGPD et nLPD se chevauchent — traitez-les une seule fois, pas deux

Pour les organisations suisses traitant des données personnelles de l'UE, le RGPD et la nLPD s'appliquent toutes deux. Leurs exigences se chevauchent sans être identiques. L'approche la plus sûre : appliquer la norme la plus stricte pour chaque exigence spécifique (généralement le RGPD). Documentez cela dans la Matrice d'applicabilité réglementaire. N'écrivez pas deux programmes de conformité séparés — cela crée des incohérences et de la confusion.

### 8.3 Le Niveau 2 « Veille » est un statut légitime

Toutes les réglementations du Niveau 2 ne sont pas binaires Actif/Non actif. « Veille » (surveillance de la situation sans obligations de conformité complètes) est appropriée pour :
- DORA lors de la prestation de services à des entités financières via des intermédiaires (exposition incertaine)
- EU AI Act lorsque des outils d'IA sont utilisés mais que la classification complète des risques est en cours d'évaluation
- NIS2 lorsque vous êtes proche sans être clairement au-dessus du seuil de taille

Documentez le raisonnement de la Veille. Définissez un déclencheur de révision. Ne laissez pas les entrées en Veille indéfiniment — elles devraient se résoudre en Actif ou Non actif dans les 12 mois.

### 8.4 Le paysage réglementaire évolue rapidement (2025-2026)

Trois grandes réglementations du Niveau 2 sont en phase de mise en œuvre active :
- **DORA** — en vigueur le 17 janvier 2025, application en cours
- **EU AI Act** — IA interdite depuis février 2025, IA à haut risque à partir d'août 2025
- **NIS2** — délai de transposition octobre 2024, application variable selon les États membres

Le journal de surveillance trimestriel aura probablement du contenu authentique pour les 2 à 3 prochaines années rien qu'avec ces trois textes. Ne traitez pas la surveillance comme une formalité pendant cette période.

### 8.5 La Matrice d'applicabilité réglementaire est une ancre d'audit

Les auditeurs à l'Étape 1 passeront un temps significatif sur POL-00 parce qu'il sous-tend les références réglementaires de toutes les autres politiques. Une matrice bien complétée — avec des déterminations explicites, un raisonnement signé et des attributions de niveaux claires — crée une forte première impression et prévient les questionnements détaillés sur les politiques de contrôle individuelles.

Investissez du temps pour bien faire la matrice. Cela porte ses fruits sur l'ensemble de l'audit.

---

## 9. Séquence d'implémentation minimale viable

1. **Répondre aux 8 questions organisationnelles** (Section 3) — RSSI + Juridique/Conformité ensemble
2. **Compléter la Matrice d'applicabilité réglementaire** — d'abord le Niveau 1, puis les déterminations du Niveau 2 avec raisonnement écrit
3. **Le DPD valide les déterminations relatives à la vie privée** — sections RGPD, nLPD, EU AI Act
4. **La Direction générale approuve et signe la matrice**
5. **Approuver et signer POL-00 elle-même** — chaîne d'approbation complète (RSSI → Juridique/Conformité → DPD → Direction générale)
6. **Compléter le premier journal de surveillance trimestriel** — même un trimestre avant l'audit de l'Étape 1
7. **Références croisées avec la DdA** — confirmer que les sélections de contrôles reflètent les déterminations Niveaux 1/2 Actifs
8. **Mettre à jour la Section 7 de POL-00** — ajouter le texte d'intégration de la gestion des changements POL-01 (voir guide INS POL-01)
9. **Planifier la surveillance trimestrielle** — rendez-vous récurrent dans le calendrier, mêmes dates chaque trimestre

Les étapes 1 à 6 constituent le minimum pour la préparation à l'audit de l'Étape 1. Les étapes 7 à 9 complètent l'intégration.

---

## 10. Emplacements des fichiers

| Document | Emplacement |
|----------|-------------|
| Politique POL-00 | `POL/ISMS-POL-00 - Regulatory Applicability Framework.md` |
| Ce guide de mise en œuvre | `INS/fr/ISMS-INS-POL-00-Guide-Mise-en-Oeuvre - FR.md` |
| Guide de mise en œuvre POL-01 | `../isms-pol-01-.../INS/fr/ISMS-INS-POL-01-Guide-Mise-en-Oeuvre - FR.md` |
| Analyse de référencement croisé | `96-isms-core-audit-reports/.../isms-copilot-pol-01-referencing-instructions.md` |
| Documents de référence réglementaires | `isms-ref-dora/`, `isms-ref-eu-ai-act/`, etc. |

---

<!-- QA_VERIFIED: 2026-03-30 -->
