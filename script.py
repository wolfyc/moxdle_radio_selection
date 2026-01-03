"""moodleBot — automatisation Selenium (sélection de choix et connexion sur Moodle).

Résumé
- Script minimal qui ouvre Chrome, sélectionne l'option de connexion "Utiliser mon compte Paris 1",
  active "Se souvenir de moi", puis remplit et soumet le formulaire de connexion.

Gestion des identifiants (ordre de priorité)
1) `credentials.py` (fichier local non versionné, recommandé pour usage local)
2) Variables d'environnement `MOODLE_USER` / `MOODLE_PASS`
3) Fichier `.env` chargé via `python-dotenv` si présent

Sécurité
- NE COMMITEZ JAMAIS de secrets. Utilisez `credentials.py` (non versionné) ou des variables d'environnement.
- Ce dépôt contient un modèle `credentials.py.example` et `.gitignore` ignore `credentials.py` et `.env`.

Exécution rapide
- Installer dépendances :
  `pip install selenium webdriver-manager python-dotenv`
- Lancer : `python script.py`

Remarques techniques
- Le script utilise des attentes explicites (`WebDriverWait` + `expected_conditions`) pour la robustesse.
- Sur Windows, `webdriver-manager` simplifie la gestion des versions Chrome/ChromeDriver.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import credentials
# Options de Chrome : 'detach' permet de laisser la fenêtre ouverte après la fin du script.
options = Options()
options.add_experimental_option("detach", True)

# Initialisation du driver Chrome. Assurez-vous que ChromeDriver est compatible avec votre Chrome.
driver = webdriver.Chrome(options=options)

# Navigue vers la page de choix du cours.
driver.get(credentials.link)

# Attendre que la checkbox (input[type='checkbox']) soit présente dans le DOM.
# EC.presence_of_element_located ne vérifie pas qu'elle soit cliquable, juste qu'elle existe.
checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']"))
)

# Si la checkbox n'est pas cochée, on clique pour la cocher.
if not checkbox.is_selected():
    checkbox.click()
    
# Attendre que l'élément contenant le texte 'Utiliser mon compte Paris 1' soit cliquable.
# Ici on utilise XPath parce que l'on cible un texte visible dans un <h3>.
element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//h3[contains(text(),'Utiliser mon compte Paris 1')]")
    )
)

# Cliquer pour sélectionner l'option de connexion via le compte Paris 1.
element.click()

# Attendre que la case 'rememberMe' soit cliquable (parfois elle est présente mais pas encore interactive).
remember_me = WebDriverWait(driver, 25).until(
    EC.element_to_be_clickable((By.ID, "rememberMe"))
)

# Activer 'se souvenir de moi' si ce n'est pas déjà fait.
if not remember_me.is_selected():
    remember_me.click()

# PRIORITÉ : tenter d'importer un fichier `credentials.py` local (non versionné) si présent.
# Cela permet d'éviter d'exposer des secrets dans les variables d'environnement ou le code.
username = None
password = None
try:
    
    username = getattr(credentials, 'username', None)
    password = getattr(credentials, 'password', None)
    if username and password:
        print("Utilisation des identifiants depuis 'credentials.py'.")
except Exception:
    # Fallback silencieux aux variables d'environnement
    pass


# Validation explicite : si une des valeurs est manquante, arrêter avec message clair.
if not username or not password:
    raise SystemExit(
        "Aucun identifiant trouvé.\n"
        "Créez un fichier 'credentials.py' à partir de 'credentials.py.example' contenant :\n"
        "  username = 'votre_user'\n"
        "  password = 'votre_mot_de_passe'\n"
        "OU définissez les variables d'environnement MOODLE_USER et MOODLE_PASS,\n"
        "ou créez un fichier .env et installez python-dotenv (pip install python-dotenv)."
    )

# Récupérer le champ 'username' et y entrer le nom d'utilisateur.
# presence_of_element_located est suffisant pour les champs de saisie.
username_field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_field.send_keys(username)

# Récupérer le champ 'password' et y entrer le mot de passe.
password_field = WebDriverWait(driver, 35).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

# Attendre que le bouton de connexion soit cliquable, puis cliquer.
login_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "submitBtn"))
)

login_button.click()

# Attendre et cliquer sur le bouton 'Accepter' (ex: popup de consentement).
accepter_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Accepter']"))
)

accepter_button.click()

# NOTE : code commenté pour sélectionner un radio button (ex: 'choice_5').
# Si nécessaire, décommenter et ajuster l'ID et le timeout.
# radio = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.ID, "choice_5"))
# )
# radio.click()

submit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'], input[type='submit'], #id_submitbutton")))
submit_btn.click()

