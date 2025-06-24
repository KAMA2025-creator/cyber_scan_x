# ----------------------------------------------------------------------
# CYBER SCAN X 🛡️ – Analyse d’adresse IP avec géolocalisation et IA
# Version terminal – Projet pédagogique avec explications détaillées
# ----------------------------------------------------------------------

# 📦 Importation des modules Python nécessaires
import ipaddress    # Permet de vérifier si une adresse IP est correctement écrite
import requests     # Sert à interroger une API sur Internet (comme ip-api.com)
import openai       # Sert à envoyer une demande à ChatGPT pour générer un rapport lisible

# ----------------------------------------------------------------------
# 🔐 Configuration de ta clé API OpenAI (nécessaire pour utiliser ChatGPT)
# 👉 Obtiens ta clé gratuite ici : https://platform.openai.com/account/api-keys
# Remplace la chaîne ci-dessous par ta vraie clé (entre guillemets)
# ⚠️ Ne partage jamais cette clé publiquement !
# ----------------------------------------------------------------------
openai.api_key = "CLE_SUPPRIMEE"

# ----------------------------------------------------------------------
# 🔹 Fonction 1 : Demander une adresse IP à l’utilisateur
# ----------------------------------------------------------------------

def demander_ip():
    """
    Cette fonction demande à l'utilisateur de taper une adresse IP,
    puis vérifie que l'adresse est valide (pas d'erreur de saisie).
    Elle répète la question tant que l'IP n'est pas correcte.
    """
    while True:
        ip = input("🔍 Entrez une adresse IP à analyser : ")

        try:
            # Vérification de la validité avec ipaddress
            # Si l’IP est correcte, on passe
            ipaddress.ip_address(ip)
            return ip  # On retourne l'adresse IP valide
        except ValueError:
            # Si une erreur est détectée (ex : 999.0.0.1), on avertit l’utilisateur
            print("❌ Adresse IP invalide. Réessaie avec une adresse correcte.")

# ----------------------------------------------------------------------
# 🔹 Fonction 2 : Interroger l’API gratuite ip-api.com
# ----------------------------------------------------------------------

def interroger_ip_api(ip):
    """
    Cette fonction contacte le site ip-api.com en lui envoyant l'adresse IP.
    Elle reçoit en retour des informations comme le pays, la ville, etc.
    """
    url = f"http://ip-api.com/json/{ip}"  # Construction de l'URL d'interrogation

    try:
        reponse = requests.get(url)       # Requête HTTP vers l'API
        data = reponse.json()             # On transforme la réponse JSON en dictionnaire Python

        if data["status"] == "success":   # Si tout s’est bien passé, on retourne les données
            return data
        else:
            # Si l'API répond qu'elle ne peut pas traiter l’IP
            print("❌ Erreur retournée par l’API :", data["message"])
            return None

    except Exception as e:
        # Si une erreur technique empêche l’accès à l’API
        print("❌ Erreur technique lors de la requête :", e)
        return None

# ----------------------------------------------------------------------
# 🔹 Fonction 3 : Générer un rapport clair avec OpenAI
# ----------------------------------------------------------------------

def generer_rapport(info):
    """
    Cette fonction envoie les données à l’API OpenAI et demande un résumé clair.
    Le texte généré explique où se trouve l’adresse IP et qui est son fournisseur.
    """
    # On prépare le message à envoyer à ChatGPT pour lui demander de résumer les infos
    prompt = f"""
Rédige un court rapport clair et professionnel à propos de cette adresse IP :

- IP : {info.get('query')}
- Pays : {info.get('country')}
- Ville : {info.get('city')}
- Latitude : {info.get('lat')}
- Longitude : {info.get('lon')}
- FAI : {info.get('isp')}
- Fuseau horaire : {info.get('timezone')}

Le rapport doit faire 4 à 5 lignes maximum, en français, dans un ton professionnel.
"""

    try:
        # Envoi à l'API ChatGPT (gpt-3.5-turbo)
        reponse = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        # On récupère la réponse générée par l’IA
        rapport = reponse.choices[0].message.content.strip()
        return rapport

    except Exception as e:
        # Si une erreur survient avec l’IA (clé invalide, pas de connexion, etc.)
        print("❌ Erreur lors de la génération du rapport IA :", e)
        return None

# ----------------------------------------------------------------------
# 🔹 Partie principale – Le programme tourne tant que l'utilisateur veut
# ----------------------------------------------------------------------

while True:
    # Étape 1 : Demander une IP
    adresse_ip = demander_ip()

    # Étape 2 : Interroger ip-api.com
    infos = interroger_ip_api(adresse_ip)

    # Étape 3 : Si on a reçu des infos valides, on les affiche
    if infos:
        print("\n" + "="*60)
        print("🔎  RÉSULTATS DE L'ANALYSE".center(60))
        print("="*60)

        # Affichage ligne par ligne des informations reçues
        print(f"🌐 Adresse IP analysée : {infos.get('query')}")
        print(f"🌍 Pays               : {infos.get('country')}")
        print(f"🏙️  Ville              : {infos.get('city')}")
        print(f"🛰️  Latitude           : {infos.get('lat')}")
        print(f"🧭 Longitude          : {infos.get('lon')}")
        print(f"📡 Fournisseur (FAI)  : {infos.get('isp')}")
        print(f"🕒 Fuseau horaire     : {infos.get('timezone')}")

        # Étape 4 : Générer un lien Google Maps à partir des coordonnées GPS
        latitude = infos.get("lat")
        longitude = infos.get("lon")
        lien_maps = f"https://www.google.com/maps?q={latitude},{longitude}"
        print("\n🔗 Lien Google Maps :")
        print(lien_maps)

        # Étape 5 : Générer un rapport automatique avec OpenAI
        print("\n" + "-"*60)
        print("🧠 Rapport  :")
        print("-"*60)
        rapport = generer_rapport(infos)
        if rapport:
            print(rapport)

        print("="*60 + "\n")

    # Étape 6 : Demander si l'utilisateur veut refaire une autre analyse
    reponse = input("🔁 Voulez-vous analyser une autre adresse IP ? (o/n) : ").lower()
    if reponse != 'o':
        print("\n🙏 Merci d’avoir utilisé CYBER SCAN X. À bientôt !")
        break


