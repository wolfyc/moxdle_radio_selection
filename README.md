# moodleBot

Outils d'automatisation Selenium pour interagir avec une instance Moodle (sélection d'options, connexion automatisée, etc.). Ce dépôt contient des scripts d'exemple et des helpers pour faciliter les tests et l'exécution planifiée.

## ✨ Vue d'ensemble
- `script.py` : script principal qui exécute le flux d'automatisation.
- `chrome_test_launch.py` : test de fumée pour vérifier que le navigateur et le WebDriver fonctionnent.

## 🔧 Prérequis
- Python 3.8+
- Chrome / Chromium ou autre navigateur compatible
- Recommandé : `webdriver-manager` pour gérer ChromeDriver automatiquement

Installer les dépendances :

```bash
pip install selenium webdriver-manager
```

## 🔐 Configuration des identifiants (recommandé : sécurisé et portable)
Ne stockez jamais de secrets dans le code source.

### Créer et utiliser `credentials.py` (usage local simple)
- Copiez `credentials.py.example` → `credentials.py` (ou créez `credentials.py` manuellement) et remplissez :

```python
# credentials.py (ne pas committer)
username = "votre_user"
password = "votre_mot_de_passe"
link = "https://exemple.moodle.org/mod/choice/view.php?id=123456"
```

- **Important :** ajoutez `credentials.py` à `.gitignore` pour éviter de committer vos secrets.
- `script.py` importe `credentials.py` et utilise `username`, `password` et `link` **en priorité**. 



> Remarque : le dépôt contient `credentials.py.example` comme modèle. 

## ▶️ Exécution
- Lancer le script principal :

```bash
python script.py
```

- Smoke test (vérifier WebDriver) :

```bash
python chrome_test_launch.py
```

## ⏱️ Planification (optionnelle)
Pour exécutions périodiques, utilisez l'outil de planification de votre OS (cron, systemd timer, Task Scheduler sur Windows, etc.). Le dossier `scripts/` peut contenir des helpers (ex : script PowerShell pour Windows) — adaptez les chemins et options à votre plateforme.

## ✅ Bonnes pratiques
- **Ne commitez jamais de secrets.**
- Ajoutez `.env` à `.gitignore` et fournissez un `.env.example` si utile.
- Préférez `webdriver-manager` pour éviter les incompatibilités ChromeDriver/Chrome.
- Testez toujours localement avant d'automatiser à grande échelle et respectez les conditions d'utilisation du service visé.

## Contribuer / Aide
Si vous voulez, je peux :
- créer une PR pour remplacer les identifiants en clair par la lecture de variables d'environnement,
- ajouter un `.env.example` et une note sur la sécurité,
- ajouter un test de fumée automatisé pour CI.

---
Licence / usage : usage personnel / éducatif. Respectez toujours les règles d'accès et l'éthique avant d'automatiser des interactions sur un site web.
