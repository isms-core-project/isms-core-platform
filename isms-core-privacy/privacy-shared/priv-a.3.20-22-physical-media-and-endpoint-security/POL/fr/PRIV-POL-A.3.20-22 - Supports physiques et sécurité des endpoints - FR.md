<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.20-22-FR:privacy:POL:a.3.20-22 -->
**PRIV-POL-A.3.20-22 — Supports physiques et sécurité des endpoints**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Supports physiques et sécurité des endpoints |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.3.20-22 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Privacy** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DPD | Politique initiale pour la première certification ISO/IEC 27701:2025 |

**Cycle de révision** : Annuel | **Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** : Principale: DPD; Secondaire: RSSI; Juridique: Responsable Juridique/Conformité; Autorité finale: Direction générale.

**Documents connexes** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.20-22-UG / TG
- ISMS-POL-A.7.8-10 (Bureau propre, supports et équipements — parallèle SGSI)
- ISMS-POL-A.8.1 (Appareils endpoint des utilisateurs — parallèle SGSI)
- PRIV-POL-A.3.5-7 (Classification des informations et transfert)
- ISO/IEC 27701:2025 Contrôles A.3.20, A.3.21, A.3.22
- RGPD Article 32 (sécurité du traitement — protection sur les endpoints et supports)
- LPD suisse Article 7 (mesures techniques et organisationnelles)

**Applicabilité du rôle** : Cette politique s'applique à l'organisation agissant à la fois comme **Responsable du traitement et comme Sous-traitant des DCP**. Les contrôles A.3.20, A.3.21 et A.3.22 sont des contrôles partagés (Tableau A.3).

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour la gestion du cycle de vie des supports de stockage contenant des DCP, l'élimination ou la réutilisation sécurisée des équipements contenant des DCP, et la protection des DCP sur les appareils endpoint des utilisateurs — conformément aux contrôles A.3.20, A.3.21 et A.3.22 d'ISO/IEC 27701:2025.

**Périmètre** : Tous les supports de stockage contenant des DCP tout au long de leur cycle de vie ; tous les équipements contenant des supports de stockage avec des DCP en fin de vie ou lors de réaffectation ; tous les appareils endpoint des utilisateurs sur lesquels des DCP sont stockés, traités ou accessibles.

**Justification des contrôles combinés** : A.3.20 (supports de stockage), A.3.21 (élimination des équipements) et A.3.22 (endpoints) traitent des DCP au repos sous forme physique et sur les appareils. Les contrôles du cycle de vie des supports empêchent la mauvaise manipulation pendant l'utilisation active ; les contrôles d'élimination empêchent l'exposition résiduelle des DCP après utilisation ; les contrôles des endpoints protègent les DCP sur les appareils les plus susceptibles d'être perdus, volés ou utilisés de manière abusive.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**Contrôle A.3.20 — Supports de stockage**
Le contrôle A.3.20 exige que [Organisation] gère les supports de stockage contenant des DCP tout au long de leur cycle de vie — acquisition, utilisation, transport et élimination — conformément au schéma de classification de l'organisation.

**Contrôle A.3.21 — Élimination ou réutilisation sécurisée des équipements**
Le contrôle A.3.21 exige que [Organisation] vérifie, avant qu'un équipement contenant des supports de stockage ne soit éliminé ou réutilisé, que toutes les DCP stockées sur ces supports ont été supprimées ou effacées de manière sécurisée.

**Contrôle A.3.22 — Appareils endpoint des utilisateurs**
Le contrôle A.3.22 exige que [Organisation] protège les DCP stockées sur des appareils endpoint des utilisateurs, traitées par ces appareils ou accessibles via ces appareils.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 32 (mesures techniques appropriées pour les DCP au repos — inclut les supports et les endpoints) ; Article 5(1)(f) (intégrité et confidentialité)
- **LPD suisse** : Article 7 (mesures techniques — protection des supports physiques et élimination sécurisée)
- **ISO/IEC 27701:2025** : Contrôles A.3.20, A.3.21, A.3.22 (normatifs)

---

# Cycle de vie des supports de stockage pour les DCP (A.3.20)

## Exigences des supports de stockage

[Organisation] DOIT gérer les supports de stockage contenant des DCP tout au long de leur cycle de vie conformément au schéma de classification défini dans PRIV-POL-A.3.5-7.

### Acquisition et enregistrement des supports

- Tous les supports de stockage amovibles qui contiennent ou pourront contenir des DCP DOIVENT être enregistrés dans le Registre des supports dès leur acquisition
- Chaque support enregistré DOIT avoir un propriétaire attribué (individu ou équipe responsable)
- La classification des supports DOIT être assignée dès la première utilisation en fonction du contenu DCP stocké

### Supports en cours d'utilisation

- Les supports de stockage contenant des DCP DOIVENT être traités conformément au niveau de classification attribué (per PRIV-POL-A.3.5-7)
- Les supports contenant des DCP RESTREINTS (catégorie spéciale) DOIVENT être chiffrés en permanence
- Les supports contenant des DCP CONFIDENTIELS DOIVENT être chiffrés lorsqu'ils sont transportés hors des locaux sécurisés
- Les supports contenant des DCP laissés sans surveillance DOIVENT être sécurisés (dans un rangement verrouillé ou un équipement verrouillé) — conformément aux exigences de bureau propre de PRIV-POL-A.3.17-19

### Transport des supports

- Le transport de supports contenant des DCP hors des locaux sécurisés DOIT être journalisé, incluant la destination, la finalité et la date de retour
- Les supports contenant des DCP CONFIDENTIELS transportés en externe DOIVENT utiliser des supports chiffrés approuvés ou un service de messagerie sécurisé approuvé
- La perte de supports pendant le transport DOIT être signalée immédiatement comme incident DCP per PRIV-POL-A.3.11-12

### Élimination des supports

- Les supports de stockage contenant des DCP NE DOIVENT PAS être éliminés via les flux de déchets ordinaires
- Avant l'élimination, les DCP DOIVENT être supprimées de manière irréversible en utilisant une méthode appropriée au type de support : effacement cryptographique (pour les supports entièrement chiffrés, sous réserve des conditions de A.3.21), effacement sécurisé per **NIST SP 800-88** (la norme de référence principale pour la désinfection des supports), ou destruction physique. Note : les normes d'écrasement multipassage comme DoD 5220.22-M ne sont pas fiables pour les supports à mémoire flash (SSD, clés USB, eMMC) ; l'effacement cryptographique per NIST SP 800-88 ou la destruction physique DOIVENT être utilisés pour ces supports
- La méthode d'élimination DOIT être documentée dans le Registre des supports, incluant la méthode utilisée, la date et le responsable
- L'élimination via un service tiers de destruction de supports DOIT produire un certificat de destruction, conservé comme preuve

---

# Élimination et réutilisation sécurisée des équipements contenant des DCP (A.3.21)

## Exigences d'élimination et de réutilisation des équipements

Avant qu'un équipement contenant des supports de stockage ne soit éliminé ou réutilisé (au sein de [Organisation] ou à l'extérieur), [Organisation] DOIT vérifier que toutes les DCP ont été supprimées ou effacées de manière sécurisée.

### Vérification avant élimination

Tous les équipements planifiés pour élimination ou réaffectation DOIVENT subir :

1. **Vérification de l'inventaire** : Confirmer si des DCP étaient ou pouvaient avoir été stockées sur les supports de stockage de l'appareil
2. **Effacement des données** : Écraser tout le stockage en utilisant une norme d'effacement approuvée (per PRIV-IMP-A.3.20-22-TG), ou détruire physiquement les supports si l'effacement n'est pas techniquement faisable
3. **Vérification** : Confirmer que l'effacement a réussi (scan de vérification post-effacement)
4. **Documentation** : Enregistrer l'identifiant d'actif de l'appareil, le statut DCP (DCP présentes/non confirmées), la méthode d'effacement, le résultat de la vérification, la date et le responsable dans le Registre d'élimination

### Normes d'effacement

La référence principale pour la désinfection des supports est **NIST SP 800-88 (Guidelines for Media Sanitization)**. Les méthodes suivantes s'appliquent :

- **Effacement logiciel (supports magnétiques / HDD)** : Effacement sécurisé utilisant les techniques Clear ou Purge de NIST SP 800-88 appropriées à la sensibilité des données. Les techniques d'écrasement multipassage (ex. DoD 5220.22-M) sont acceptables pour les HDD mais NE DOIVENT PAS être utilisées comme méthode principale pour les supports à mémoire flash (SSD, clés USB, eMMC) où le nivellement d'usure rend l'écrasement peu fiable
- **Effacement cryptographique** : La destruction des clés de chiffrement est acceptable comme méthode d'effacement uniquement si le chiffrement intégral du disque était confirmé actif depuis le premier écrit de données sur ce support, et si la mise en œuvre du chiffrement est validée (ex. matériel AES-256). En cas d'incertitude sur la couverture du chiffrement, la destruction physique DOIT être utilisée
- **Destruction physique** : Déchiquetage ou démagnétisation des supports — requise pour les DCP RESTREINTS sur les supports flash, et pour tout support où l'effacement logiciel ne peut être vérifié ; la destruction doit être documentée avec la méthode et la personne confirmant

### Réutilisation au sein de [Organisation]

Avant la réaffectation d'un équipement à un autre utilisateur au sein de [Organisation] : toutes les DCP du profil de l'utilisateur précédent DOIVENT être supprimées ; l'appareil DOIT être reconfiguré ou réinitialisé à la configuration de base ; un nouvel enregistrement d'accès utilisateur DOIT être créé ; l'accès de l'utilisateur précédent révoqué per PRIV-POL-A.3.8-10.

### Élimination par des tiers

Lorsque l'équipement est éliminé via un service tiers (recycleur, revendeur, association caritative) : le tiers DOIT fournir un certificat de destruction des données avant que l'équipement ne quitte la garde de [Organisation] ; pour les équipements contenant des DCP RESTREINTS, la destruction physique des supports est requise (vente ou don non autorisés sans destruction confirmée) ; le certificat de destruction DOIT être conservé dans le Registre d'élimination pendant minimum 5 ans.

---

# Protection des DCP sur les appareils endpoint des utilisateurs (A.3.22)

## Exigences des appareils endpoint pour les DCP

[Organisation] DOIT veiller à ce que les DCP stockées sur des appareils endpoint des utilisateurs, traitées par ces appareils ou accessibles via ces appareils soient protégées.

### Contrôles minimum des endpoints pour les DCP

Tous les appareils endpoint d'entreprise qui stockent, traitent ou accèdent aux DCP DOIVENT être configurés avec :

- **Chiffrement intégral du disque** : Actif et appliqué ; gestion des clés de chiffrement per les normes cryptographiques (PRIV-POL-A.3.23-31)
- **Verrouillage de l'écran** : Verrouillage automatique après la durée d'inactivité maximale (configuré per PRIV-IMP-A.3.20-22-TG)
- **Capacité d'effacement à distance** : Capacité d'effacement ou de verrouillage à distance enregistrée pour l'appareil ; capacité d'effacement testée au minimum annuellement
- **Enrôlement dans la gestion des appareils** : Enrôlé dans la solution MDM (Mobile Device Management) ou UEM (Unified Endpoint Management) d'entreprise où techniquement faisable
- **Correctifs à jour** : Correctifs du système d'exploitation et de sécurité appliqués dans les délais définis dans ISMS-POL-A.8.8

### Restrictions de stockage des DCP sur les endpoints

- Le téléchargement ou le stockage en masse de DCP sur les appareils endpoint DOIVENT être limités au nécessaire pour la fonction de l'emploi
- La copie ou le stockage de grands volumes de DCP (export en masse depuis des bases de données ou applications) sur des endpoints locaux nécessite l'approbation du Propriétaire des données
- Les DCP RESTREINTS (catégorie spéciale) NE DOIVENT PAS être stockés localement sur des endpoints sauf nécessité opérationnelle avec notification du DPD ; lorsque stockés localement, ils DOIVENT l'être dans un conteneur chiffré avec des contrôles d'accès distincts de l'accès général au système de fichiers

### BYOD (Apportez votre propre appareil)

Lorsque les appareils personnels sont autorisés à accéder aux DCP (politique BYOD applicable) : les appareils BYOD DOIVENT être enrôlés dans une solution MDM/conteneurisation qui crée un espace de travail DCP géré, séparé des données personnelles ; les contrôles minimum (chiffrement, verrouillage de l'écran, effacement à distance) DOIVENT s'appliquer à l'espace de travail géré ; le droit de [Organisation] d'effectuer un effacement à distance de l'espace de travail géré DOIT être convenu par écrit avant l'octroi de l'accès aux DCP ; les DCP NE DOIVENT PAS être stockées en dehors de l'espace de travail géré sur les appareils BYOD.

### Appareils endpoint perdus ou volés

La perte ou le vol d'un appareil endpoint contenant ou avec accès aux DCP DOIT être : signalé immédiatement à l'Équipe Sécurité IT et au DPD ; traité comme un incident DCP suspecté et géré per PRIV-POL-A.3.11-12 ; l'effacement à distance initié dès que possible et dans les **4 heures** suivant le signalement de la perte confirmée à l'Équipe Sécurité IT. Lorsque l'effacement à distance n'est pas techniquement faisable dans les 4 heures (ex. l'appareil est hors ligne), le DPD DOIT être notifié immédiatement et le retard DOIT être documenté ; une action compensatoire (réinitialisation du mot de passe, suspension du compte, révocation de l'accès aux DCP) DOIT être prise immédiatement dans l'attente de la confirmation de l'effacement.

---

# Rôles et responsabilités

| Rôle | Responsabilités pour A.3.20–A.3.22 |
|------|-------------------------------------|
| **DPD** | Définit les exigences spécifiques aux DCP pour les supports et endpoints ; notifié des DCP RESTREINTS sur les endpoints ; examine l'adéquation du Registre d'élimination ; informé des appareils perdus/volés |
| **RSSI** | Définit les normes techniques d'effacement, de chiffrement et de gestion des endpoints ; configure MDM/UEM ; tient le Registre d'élimination ; enquête sur les appareils perdus/volés |
| **Équipe Sécurité IT** | Met en œuvre le chiffrement et MDM ; exécute l'élimination et l'effacement des supports ; tient le Registre des supports et le Registre d'élimination ; initie l'effacement à distance sur les appareils perdus |
| **Propriétaire des données** | Approuve le téléchargement en masse de DCP sur les endpoints ; notifié de l'élimination de supports contenant des DCP dans son domaine |
| **Tout le personnel** | Signale immédiatement les appareils perdus ou volés ; respecte les exigences d'écran propre ; limite les DCP au minimum nécessaire sur les endpoints |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Registre des supports | Inventaire des supports amovibles avec DCP, propriétaire, classification et statut | En cours + 3 ans |
| Journal de transport des supports | Enregistrements des supports DCP transportés hors des locaux sécurisés | 3 ans |
| Registre d'élimination | Enregistrements d'élimination des équipements avec statut DCP, méthode d'effacement, vérification et date | 5 ans |
| Certificats de destruction | Certificats de destruction tiers pour les équipements contenant des DCP | 5 ans |
| Statut de chiffrement des endpoints | Rapports de configuration confirmant le chiffrement intégral du disque sur les appareils d'entreprise | En cours + 3 ans |
| Enregistrements d'enrôlement MDM/UEM | Appareils enrôlés dans la gestion des endpoints, y compris les espaces de travail gérés BYOD | En cours + 3 ans |
| Rapports d'appareils perdus/volés | Enregistrements de perte/vol d'appareils, actions d'effacement à distance et évaluations d'incidents DCP | 3 ans |

---

# Considérations d'audit

**Pour A.3.20 (Supports de stockage)** : Registre des supports avec inventaire des supports DCP ; preuves que les supports contenant des DCP sont chiffrés (surtout DCP RESTREINTS) ; journal de transport des supports sortant des locaux sécurisés ; enregistrements d'élimination incluant la méthode d'effacement et la vérification.

**Pour A.3.21 (Élimination des équipements)** : Registre d'élimination avec vérifications du statut DCP avant élimination ; preuves de la méthode d'effacement approuvée appliquée ; certificats de destruction des services d'élimination tiers ; aucune élimination d'équipements DCP RESTREINTS sans destruction physique confirmée.

**Pour A.3.22 (Appareils endpoint)** : Rapports de configuration du chiffrement intégral du disque ; enregistrements d'enrôlement MDM/UEM ; preuves de test d'effacement à distance ; accords écrits BYOD où des appareils personnels accèdent aux DCP ; enregistrements de réponse aux appareils perdus/volés avec confirmation d'effacement à distance.

---

<!-- QA_VERIFIED: 2026-04-03 -->
