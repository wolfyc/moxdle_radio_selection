# moodleBot

Automatisation Selenium minimal pour sélectionner un choix sur un cours Moodle et se connecter via le compte universitaire.

## Vue d'ensemble
- `script.py` : script principal qui automatise la sélection d'une option de cours puis le flux de connexion.
- `chrome_test_launch.py` : test de fumée ouvrant Chrome pour vérifier l'environnement WebDriver.
- `credentials.py.example` : modèle local à copier en `credentials.py` pour stocker vos identifiants localement (ne pas committer).
- `scripts/create_scheduled_task.ps1` : helper PowerShell pour créer une tâche planifiée (Windows).

## Prérequis
- Python 3.8+
- Chrome installé
- Recommandé : `webdriver-manager` pour gérer ChromeDriver automatiquement

Installer les dépendances :
```bash
pip install selenium webdriver-manager python-dotenv
```

## Configuration des identifiants (3 options)
1) Fichier local (recommandé pour usage personnel)
   - Copier `credentials.py.example` → `credentials.py` et remplir `username`/`password`.
   - `credentials.py` est ignoré par Git par défaut.

2) Variables d'environnement
   - Sous PowerShell (persistant pour l'utilisateur) :
     ```powershell
     setx MOODLE_USER "votre_user"
     setx MOODLE_PASS "votre_pass"
     ```
   - Voir la section "Planificateur de tâches" ci‑dessous si vous exécutez le script via le Task Scheduler.

3) `.env` (optionnel)
   - Créez un fichier `.env` contenant `MOODLE_USER` et `MOODLE_PASS` et installez `python-dotenv`.
   - Exemple `.env` :
     ```text
     MOODLE_USER=votre_user
     MOODLE_PASS=votre_password
     ```

## Exécution
- Lancer le script principal :
```bash
python script.py
```

- Smoke test :
```bash
python chrome_test_launch.py
```

## Planifier l'exécution (Windows)
- Utilisez le script PowerShell `scripts/create_scheduled_task.ps1` :
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\create_scheduled_task.ps1 -ScriptPath "C:\path\to\script.py" -RunAt "2026-01-05 20:00"
```
- Remarques : la machine doit être allumée (et non en veille profonde) à l'heure d'exécution ; si la tâche doit s'exécuter sans session ouverte, utilisez des variables système ou un gestionnaire de secrets sécurisé.

## Bonnes pratiques
- Ne commitez jamais de secrets.
- Préférez `webdriver-manager` pour éviter les problèmes de compatibilité ChromeDriver.
- Testez localement avant d'automatiser en production.

## Aide / PRs
Si vous souhaitez, je peux préparer une PR pour :
- remplacer les identifiants hardcodés par un usage sécurisé,
- ajouter un test de fumée automatisé,
- documenter davantage l'usage pour le Planificateur de tâches Windows.

---
Licence / usage : pour usage personnel et éducatif. Respectez les règles d'accès du site Moodle ciblé avant d'automatiser.
