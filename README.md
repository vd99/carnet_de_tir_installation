# Carnet de tir

Cette application est destinée aux pratiquants du tir à l'arbalète Field. Elle permet à un tireur de centraliser les fonctionnalités suivantes :

- Noter ses réglages pour une arme selon un arc et une distance ;
- Effectuer ses regroupements de flèches en fonction de leur position moyenne ;
- Noter ses points d'entraînement grâce à une cible interactive ;
- Consigner ses résultats de matchs passés ;
- Chronométrer ses tirs ;
- Visualiser l'évolution de ses scores ;
- Accéder facilement à sa licence FFTir.

---

## Installation

Afin de garantir la gratuité de l'application pour les utilisateurs comme pour le développeur, celle-ci est distribuée via [Obtainium](https://github.com/ImranR98/Obtainium) sur Android et [AltStore Classic](https://altstore.io/) sur iOS.

### Installation sur Android

#### 1. Installer Obtainium

L'installation de l'application via [Obtainium](https://github.com/ImranR98/Obtainium) est recommandée :

1. Se rendre sur la [page de téléchargement d'Obtainium](https://github.com/ImranR98/Obtainium/releases).
2. Choisir la version adaptée à l'appareil :
   - `app-arm64-v8a-release.apk` pour les téléphones récents (recommandé dans la plupart des cas) ;
   - `app-armeabi-v7a-release.apk` pour les appareils 32 bits (souvent antérieurs à 2017) ;
   - `app-universal-release.apk` en cas de doute (contient toutes les architectures).
3. Ouvrir le fichier téléchargé pour lancer l'installation et autoriser l'installation d'applications inconnues si nécessaire.

#### 2. Ajouter Carnet de tir à Obtainium

1. Ouvrir **Obtainium**.
2. Appuyer sur **Add App** (ou **Ajouter**).
3. Dans le champ **URL source de l'application**, coller le lien suivant :

   ```
   https://github.com/vd99/carnet_de_tir_installation
   ```

4. Appuyer sur **Installer**.
5. Lors de l'installation, accepter l'analyse de l'application si Google Play Protect la propose.

L'application est alors installée et sera automatiquement maintenue à jour par Obtainium.

> **Alternative :** il est également possible d'installer directement l'application via le fichier `.apk` disponible dans les [Releases du dépôt](https://github.com/vd99/carnet_de_tir_installation/releases). Les mises à jour devront alors être faites manuellement et aucune notification ne signalera les nouvelles sorties.

---

### Installation sur iOS

L'application est distribuée via [AltStore Classic](https://altstore.io/) (version 2.3 ou ultérieure). Depuis la version 2.3, AltStore peut installer et rafraîchir les applications directement depuis l'iPhone, grâce à un **serveur AltServer distant** (« Remote AltServer », basé sur des serveurs anisette). Un ordinateur (Windows ou Mac) n'est nécessaire qu'**une seule fois**, pour installer AltStore et jumeler l'appareil. Aucun ordinateur n'est ensuite nécessaire pour les renouvellements et les mises à jour.

> **Prérequis :** iOS 17.4 ou supérieur, un identifiant Apple (un compte gratuit suffit) et une connexion Wi-Fi.

#### 1. Installer AltStore Classic

1. Sur un ordinateur, suivre le guide officiel d'installation d'AltStore Classic pour [Windows](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows) ou [macOS](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) (installation d'AltServer, connexion de l'iPhone/iPad par câble, puis **Install AltStore** depuis AltServer avec l'identifiant Apple).
2. Sur l'appareil, aller dans **Réglages > Général > VPN et gestion de l'appareil** et faire confiance au profil développeur associé à l'identifiant Apple.
3. Activer le **mode développeur** dans **Réglages > Confidentialité et sécurité > Mode développeur** (un redémarrage est demandé).

> ⚠️ AltStore et AltServer doivent être téléchargés uniquement depuis le site officiel [altstore.io](https://altstore.io/). L'identifiant Apple ne doit jamais être renseigné dans un autre site ou une autre application se présentant comme un outil d'installation alternatif.

#### 2. Configurer le serveur AltServer distant (sans ordinateur)

1. Ouvrir **AltStore** et aller dans l'onglet **Settings**.
2. Dans la section **Remote AltServer**, appuyer sur **Set up Remote AltServer...** et suivre les instructions à l'écran :
   - jumeler l'appareil (via l'ordinateur, ou directement sur l'appareil sous iOS 27) ;
   - installer **LocalDevVPN** (application gratuite, nécessaire au fonctionnement du serveur distant).
3. En cas d'indisponibilité du serveur, en choisir un autre via **Choose Server** dans les réglages d'AltStore.

Pour installer ou rafraîchir des applications, il faut ensuite :

1. Lancer **LocalDevVPN** et appuyer sur **Connect** ;
2. Être connecté en **Wi-Fi** (pas en données cellulaires) ;
3. Ouvrir **AltStore**.

#### 3. Ajouter Carnet de tir à AltStore

1. Ouvrir **AltStore**, aller dans l'onglet **Browse**, puis appuyer sur **Sources**.
2. Appuyer sur **+**, puis coller l'URL suivante :

   ```
   https://vd99.github.io/carnet_de_tir_installation/source.json
   ```

3. Une fois la source ajoutée, retrouver **Carnet de tir** dans la liste et appuyer sur **Free** / **Installer**.
4. Retourner dans **Réglages > Général > VPN et gestion de l'appareil** et faire confiance au profil de l'application si nécessaire.

#### Renouvellement et mises à jour

Apple limite à **7 jours** la validité des applications installées avec un compte développeur gratuit : AltStore doit donc les rafraîchir régulièrement. Il est conseillé d'ouvrir AltStore (avec le Wi-Fi et LocalDevVPN activés) avant l'expiration, depuis l'onglet **My Apps**. Les mises à jour vers une nouvelle version de l'application s'y installent également, sans ordinateur.
