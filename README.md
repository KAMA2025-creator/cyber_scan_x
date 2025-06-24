# 🔐 CYBER SCAN X

**CYBER SCAN X** est un outil pédagogique développé en Python pour :
- Vérifier une adresse IP
- Obtenir sa localisation (ville, pays, latitude, longitude)
- Générer un lien Google Maps cliquable
- Générer un mini rapport en langage naturel grâce à l’intelligence artificielle (OpenAI)

---

## 🧠 Objectif

Ce projet a été réalisé dans le cadre d’un exercice de cybersécurité. Il permet d’apprendre à :
- Interroger des APIs externes (`ip-api.com`, `OpenAI`)
- Traiter des données en Python
- Générer une analyse automatisée accessible à tous

---

## ⚙️ Technologies utilisées

- Python 3.x
- `requests`
- `openai`
- API gratuite : https://ip-api.com
- OpenAI GPT-3.5 pour le rapport automatique

---

## ▶️ Comment l’utiliser

1. Cloner ce dépôt GitHub ou télécharger le dossier
2. Installer les bibliothèques nécessaires :

   ```bash
   pip install requests openai
   ```

3. Remplacer `"TON_API_KEY_ICI"` par votre clé OpenAI lorsque le script vous le demande

4. Lancer le script :

   ```bash
   python cyber_scan_x.py
   ```

---

## 📸 Exemple de résultat

```
🔎  RÉSULTATS DE L'ANALYSE
Adresse IP : 8.8.8.8
Pays : United States
Ville : Mountain View
Lien Google Maps : https://www.google.com/maps?q=37.386,-122.0838

🧠 Rapport IA :
Cette adresse IP appartient à Google, située aux États-Unis...
```

---

## 👩‍💻 Auteur

Ce projet a été réalisé par **Andrea Kouassi** dans le cadre de sa formation en cybersécurité.

---

✅ N’oubliez pas de ne **jamais publier votre clé API** dans un dépôt public.  
