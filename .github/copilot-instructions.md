# Copilot / AI agent instructions — moodleBot 🧭

## Vue d'ensemble
- Petit dépôt de scripts Python utilisant Selenium pour automatiser une connexion et quelques interactions sur un site Moodle (Université Paris 1).
- Composants principaux:
  - `script.py` — flux d'authentification complet (sélecteurs CSS/XPath, `WebDriverWait`, clics, envoi d'identifiants).
  - `chrome_test_launch.py` — test minimal pour vérifier que Chrome s'ouvre (smoke test).

---

## Règles importantes pour les agents ✅
- **Ne commitez jamais de secrets** : `script.py` contient actuellement des identifiants en clair (`username`, `password`). Remplacez-les par `os.environ.get(...)` et ajoutez `.env` à `.gitignore` si besoin.
- **Validez localement avant PR** : exécutez `python script.py` ou `python chrome_test_launch.py` pour vérifier le comportement et les erreurs de WebDriver/Chrome.
- **Compatibilité de ChromeDriver** : get/validate ChromeDriver version (ou utilisez `webdriver-manager`/`chromedriver_autoinstaller`) pour éviter mismatch avec la version de Chrome sur Windows.
- **Respect du site** : n'effectuez pas d'attaques de force ou d'automatisation à grande échelle contre des sites réels sans permission.

---

## Commandes utiles 🔧
- Installer dépendances :

```bash
pip install selenium webdriver-manager  # recommandé
```

- Lancer le script principal :

```bash
python script.py
```

- Lancer le smoke test :

```bash
python chrome_test_launch.py
```

---

## Patterns & conventions détectés dans le code 🔍
- **Utilisation d'attentes explicites** : `WebDriverWait` + `expected_conditions` (présence, clickable). Gardez ce pattern pour la stabilité.
- **Sélecteurs** : mélange de `CSS_SELECTOR` pour `input[type='checkbox']` et `XPATH` pour rechercher un `h3` contenant le texte (ex: `//h3[contains(text(),'Utiliser mon compte Paris 1')]`). Préférez CSS si possible, XPath si le texte visible est la meilleure option.
- **Tempos conservateurs** : les timeouts vont de 10 à 35 secondes — respecter ou rationaliser ces valeurs plutôt que les diminuer brusquement.

Exemples de références :
- `script.py` : champs `username` (id `username`), `password` (id `password`), bouton `submitBtn`, case `rememberMe`.

---

## Recommandations d'améliorations concrètes (pour PRs) 💡
- Remplacer les identifiants hardcodés par l'utilisation d'env vars :

```python
import os
username = os.environ.get('MOODLE_USER')
password = os.environ.get('MOODLE_PASS')
```

- Ajouter un petit README expliquant l'exécution et la dépendance ChromeDriver.
- Ajouter un test de fumée `tests/test_smoke.py` qui utilise un driver en mode headless sur `chrome_test_launch.py` (mocker si nécessaire pour CI).
- Ajouter `chromedriver` à `.gitignore` si vous en installez localement.

---

## Ce que l'agent doit faire lorsqu'il propose un changement 📝
- Expliquer précisément la raison du changement et comment tester localement (ex : comment installer `webdriver-manager`, comment définir les variables d'environnement).
- Ne pas committer de secrets; si un secret existe déjà, ouvrir un ticket pour le retirer et le remplacer par une solution sûre.
- Fournir un test minimal ou une instruction de validation pour toute modification touchant le flux d'authentification.

---

## Points à vérifier auprès du mainteneur ⚠️
- Souhaitez-vous qu'on retire et invalide les identifiants actuellement dans `script.py` et qu'on fournisse un helper `.env.example` ?
- Préférez-vous `webdriver-manager` ou fournir un binaire ChromeDriver inclus (non recommandé) ?

---

## Planifier l'exécution (Windows)
- Un moyen simple est d'utiliser le Planificateur de tâches Windows. J'ai ajouté un script PowerShell helper : `scripts/create_scheduled_task.ps1`.

Exemple :
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\create_scheduled_task.ps1 -ScriptPath "C:\Users\Wolf\dev\moodleBot\script.py" -RunAt "2026-01-05 20:00"
```
- Le script crée une tâche **one-time** pour l'utilisateur courant et vérifie que `python` est disponible dans le PATH.
- Remarques importantes : la machine doit être allumée et non en veille profonde au moment de l'exécution ; selon la politique locale, l'exécution de `Register-ScheduledTask` peut nécessiter des privilèges élevés.

---

Si vous voulez, je peux :
- créer la PR qui remplace les identifiants par des env vars + ajouter `.env` à `.gitignore`,
- ajouter un petit README d'exécution et un test de fumée,
- préparer une PR pour ajouter la tâche planifiée (avec script PowerShell) et un guide pour l'exécuter localement.

Merci — dites-moi quelle action prioriser. 🚀