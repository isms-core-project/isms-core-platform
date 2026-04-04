# ISMS-INS-POL-01 — Guide de mise en œuvre
## POL-01 : Cadre de gouvernance et de prise de décision du SMSI

**Date :** 2026-02-17
**Objet :** Guide pratique de mise en œuvre pour les organisations adoptant POL-01
**Public :** RSSI, Responsable de la mise en œuvre, Consultant

---

## 1. Ce que fait réellement POL-01 (en langage clair)

POL-01 existe pour une seule raison : **mettre fin à la dérive du périmètre des auditeurs.**

La certification ISO 27001 implique deux niveaux de jugement professionnel :
1. **Votre jugement** — interpréter ISO 27001 pour votre contexte, sélectionner les contrôles, définir les preuves
2. **Le jugement de l'auditeur** — vérifier que votre interprétation est raisonnable et mise en œuvre

Sans POL-01, la frontière entre ces deux niveaux est floue. Un auditeur pointilleux peut remettre en question vos décisions de conception des contrôles pendant l'audit, transformant un exercice de vérification en une renégociation. POL-01 transfère l'ensemble de vos décisions de jugement professionnel dans des artefacts documentés, signés et préparés avant l'audit. Au moment où l'auditeur arrive, chaque décision dispose d'une autorité nommée, d'un justificatif de compétence et d'une signature d'approbation. Son rôle se réduit au binaire : avez-vous suivi votre processus documenté ? Oui ou non.

**La complexité de POL-01 est le produit. Une politique de gouvernance plus simple offre aux auditeurs davantage de marge de manœuvre.**

---

## 2. Ce qui doit être modifié dans les autres politiques

### 2.1 Modifications requises (À effectuer)

Seules 4 politiques nécessitent des mises à jour substantielles. Ces modifications valent la peine car elles établissent des références croisées que les auditeurs s'attendent à trouver lors de l'examen du cadre de gouvernance.

#### POL-00 — Cadre d'applicabilité réglementaire
**Où :** Section 7 (Maintenance & Mises à jour)
**Quoi ajouter :** Une sous-section expliquant que les changements réglementaires détectés via la surveillance POL-00 déclenchent le processus de changement POL-01 (Section 5.2). Les auditeurs rechercheront ce lien — sans lui, la surveillance POL-00 et le contrôle des changements POL-01 paraissent déconnectés.

```markdown
### Intégration de la gestion des changements

Les changements réglementaires détectés via la surveillance POL-00 déclenchent
le processus de changement des critères de conformité défini dans ISMS-POL-01
(Section 5.2). L'évaluation de l'impact du changement, l'autorité d'approbation
et le suivi de la réévaluation suivent le processus en 6 étapes défini dans
POL-01 Section 5.2. Les contrôles concernés sont réévalués dans les 90 jours
conformément à POL-01 Section 5.4.
```

#### POL-A.5.1 — Politiques de sécurité de l'information
**Où :** Section 1.3 ou nouvelle Section 1.4
**Quoi ajouter :** Une référence aux limites de gouvernance. Il s'agit de la politique-cadre pour tous les contrôles de l'Annexe A — en indiquant ici que l'autorité de décision, les exceptions et le contrôle des changements sont régis par POL-01, vous n'avez pas besoin de l'ajouter ailleurs.

```markdown
### Cadre de gouvernance

L'autorité de décision pour l'interprétation de la conformité au SMSI, la
gestion des exceptions de contrôles et le contrôle des changements des
critères de conformité est régie par ISMS-POL-01 (Cadre de gouvernance et
de prise de décision du SMSI). Toutes les politiques de contrôle de l'Annexe A
opèrent dans les limites d'autorité et les processus définis dans POL-01.
```

#### POL-A.5.31 — Exigences légales, réglementaires, statutaires et contractuelles
**Où :** Section de surveillance de la conformité
**Quoi ajouter :** Référence à l'autorité de gouvernance reliant la surveillance de la conformité (POL-00) à la gestion des exceptions et au contrôle des changements (POL-01). Les auditeurs vérifiant la conformité A.5.31 voudront voir comment les changements réglementaires s'intègrent dans le processus de gouvernance.

#### POL-A.5.35-36 — Révision de la conformité / Révision indépendante
**Où :** Section du processus de révision
**Quoi ajouter :** Référence à POL-01 Section 6.1 (révision annuelle de la gouvernance) dans le cadre du périmètre de la révision indépendante. Cela garantit que l'efficacité de la gouvernance est explicitement dans le périmètre d'audit.

---

### 2.2 À ne pas faire (Inutile)

**Ajouter POL-01 aux Documents connexes des 53 politiques de l'Annexe A.**

Le Copilote ISMS a suggéré cela en Phase 3. Ne le faites pas. Voici pourquoi :

- La relation entre POL-01 et toutes les politiques de contrôle est établie par la structure du SMSI, la DdA et par POL-A.5.1 (la politique-cadre)
- Les auditeurs ne vérifient pas la gouvernance en contrôlant 53 listes de Documents connexes
- 53 modifications de politiques × charge de maintenance = dette perpétuelle à chaque modification de POL-01
- Ajouter une ligne dans chaque politique crée l'illusion d'intégration sans la substance

**Si un auditeur demande pourquoi POL-01 ne figure pas dans les Documents connexes d'une politique de contrôle spécifique**, renvoyez-le à POL-A.5.1 Section 1.X (la référence de gouvernance que vous avez ajoutée ci-dessus). C'est suffisant.

---

## 3. Démarrage opérationnel — Ce qui doit exister avant l'audit de l'Étape 2

C'est là que la plupart des organisations se font prendre. POL-01 définit des processus. Les processus nécessitent des preuves. Voici l'ensemble de preuves minimal viable pour un premier audit de l'Étape 2.

### 3.1 Indispensable (L'auditeur demandera)

| Preuve | De quoi s'agit-il | Qui la maintient | Fréquence |
|--------|-------------------|-----------------|-----------|
| **Journaux de surveillance POL-00** | Enregistrement signé attestant que le paysage réglementaire a été examiné | Juridique/Conformité + RSSI | Trimestriel (4 par an) |
| **Registre des exceptions** | Journal des contrôles ne pouvant être mis en œuvre tels que rédigés, avec le processus en 5 étapes documenté | RSSI | Dès l'apparition d'exceptions |
| **Registre d'acceptation des risques** | Signatures de la Direction générale sur les risques acceptés | Direction générale | Dès les décisions prises |
| **Journal des modifications du SMSI** | Enregistrement des changements de critères de conformité avec le processus en 6 étapes | RSSI | Dès les changements intervenus |
| **Justificatifs de compétence** | Certifications / expériences du RSSI, Juridique/Conformité, DPD, Direction générale | RH / RSSI | À l'affectation au poste |
| **Procès-verbal de la révision annuelle de gouvernance** | Procès-verbal de réunion montrant que 6 sujets ont été couverts avec la présence de la Direction générale | RSSI | Annuel |

### 3.2 Utile (Renforce la position)

| Preuve | De quoi s'agit-il |
|--------|-------------------|
| Registre des écarts | Suivi des réévaluations après changements (POL-01 Section 5.4) |
| Registre des retours d'expérience | Actions d'amélioration de la gouvernance (POL-01 Section 6.2) |
| Classeur ISMS-CHK-POL-01 complété | Auto-évaluation trimestrielle de la gouvernance (20 exigences, GOV-01–GOV-20) |

### 3.3 Ce qui peut être différé à l'audit de surveillance

- Historique complet des évaluations trimestrielles ISMS-CHK-POL-01 (4 trimestres)
- Registre complet des retours d'expérience avec plusieurs entrées
- Registre des écarts détaillé avec suivi > 95 % de complétion

Lors de **l'audit de certification initial**, les auditeurs acceptent que les processus soient récents. Ce qu'ils ne peuvent accepter c'est l'absence totale de preuves. Même un trimestre complété de journaux de surveillance + un registre des exceptions avec 0 à 3 entrées vaut mieux que rien.

---

## 4. Observations de mise en œuvre

### 4.1 Le journal de surveillance trimestriel est la dépendance clé

Tout dans POL-01 se connecte en fin de compte à la surveillance trimestrielle POL-00. Si le journal trimestriel existe et est signé par Juridique/Conformité + RSSI, il démontre :
- GOV-05 (domaine Décisions d'applicabilité) ✅
- Que l'organisation maintient activement sa conscience réglementaire ✅
- Que POL-01 Section 3 est opérationnellement active ✅

Créez un modèle simple pour le journal de surveillance et complétez-le trimestriellement, même si la réponse est « aucun changement détecté ». C'est la signature qui compte.

### 4.2 Le registre des exceptions est votre filet de sécurité

Le processus d'exception en 5 étapes (POL-01 Section 4.2) n'est pas de la bureaucratie — c'est votre justification documentée pour chaque contrôle que vous n'avez pas pu ou choisi de ne pas mettre en œuvre intégralement. Sans lui, un auditeur peut qualifier n'importe quelle lacune de non-conformité. Avec lui, cette même lacune devient une exception documentée, évaluée en termes de risques et approuvée par la direction. C'est la différence entre une non-conformité majeure et une acceptation de risque acceptable.

Commencez le registre immédiatement, même s'il est vide. Un registre vide avec la bonne structure vaut mieux qu'aucun registre.

### 4.3 Les signatures de la Direction générale sont non négociables

La Clause 6.1.3d de l'ISO 27001 exige explicitement l'approbation de la direction pour les décisions d'acceptation des risques. POL-01 formalise cela via le Registre d'acceptation des risques. Si vous ne pouvez pas obtenir les signatures de la Direction générale, vous ne pouvez pas finaliser le traitement des risques, et vous ne pouvez pas obtenir la certification. C'est le seul processus pour lequel il n'y a pas de contournement — obtenez les signatures.

### 4.4 Le journal des modifications est facile à oublier

Le processus de changement en 6 étapes (POL-01 Section 5.2) ne s'active que lorsque les critères de conformité changent — ce qui peut ne pas arriver souvent. Le risque est d'oublier de consigner un changement quand il survient (nouvelle réglementation, retour d'audit, menace significative). Désignez le RSSI comme responsable du journal et ajoutez « vérification du journal des modifications » comme point permanent à l'ordre du jour de la révision annuelle de gouvernance.

### 4.5 Ne sur-ingénieurez pas la révision de gouvernance

La Section 6.1 de POL-01 exige une révision annuelle de gouvernance couvrant 6 sujets. Cela ne doit pas être une réunion de conseil formelle. Une séance documentée de 2 heures avec le RSSI et un représentant de la Direction générale, avec un procès-verbal couvrant les 6 sujets, satisfait l'exigence. Un procès-verbal d'une page vaut mieux qu'un processus élaboré qui ne se produit jamais.

---

## 5. Séquence d'implémentation minimale viable

Pour une organisation mettant en œuvre POL-01 de zéro, dans l'ordre :

1. **Approuver et signer POL-01** — le RSSI rédige, Juridique/Conformité révise, la Direction générale approuve
2. **Créer les justificatifs de compétence** — documenter que le RSSI, Juridique/Conformité, le DPD satisfont aux critères de la Section 2.3
3. **Créer le Registre des exceptions** — modèle uniquement, même si vide
4. **Créer le Registre d'acceptation des risques** — modèle uniquement, même si vide
5. **Créer le Journal des modifications du SMSI** — modèle uniquement, même si vide
6. **Compléter le premier journal de surveillance trimestriel POL-00** — même un seul trimestre
7. **Mettre à jour la Section 7 de POL-00** — ajouter la référence d'intégration de la gestion des changements
8. **Mettre à jour POL-A.5.1** — ajouter la référence au cadre de gouvernance
9. **Planifier la révision annuelle de gouvernance** — l'inscrire au calendrier maintenant
10. **Générer le classeur ISMS-CHK-POL-01** — exécuter le script, compléter un cycle d'évaluation

Les étapes 1 à 6 sont des prérequis pour l'audit de l'Étape 2. Les étapes 7 à 10 renforcent la position.

---

## 6. Emplacements des fichiers

| Document | Emplacement |
|----------|-------------|
| Politique POL-01 | `POL/ISMS-POL-01 - ISMS Governance and Decision-Making Framework.md` |
| Générateur du classeur d'évaluation | `SCR/ISMS-SCR-CHK-POL-01.py` |
| Classeur d'évaluation généré | `WKBK/ISMS-CHK-POL-01_...xlsx` |
| Ce guide de mise en œuvre | `INS/fr/ISMS-INS-POL-01-Guide-Mise-en-Oeuvre - FR.md` |
| Analyse de référencement croisé | `96-isms-core-audit-reports/.../isms-copilot-pol-01-referencing-instructions.md` |

---

<!-- QA_VERIFIED: 2026-03-30 -->
