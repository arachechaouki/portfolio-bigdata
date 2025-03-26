# Projet 1 – Analyse de Logs Apache

# Description :  
Ce projet lit et analyse un fichier de logs Apache pour en extraire des informations clés :
- IPs les plus actives
- Pages les plus consultées
- Codes d’erreur HTTP (404, 500...)

# Outils utilisés :
- Python
- Regex
- collections.Counter
- Matplotlib

# Résultats :
Graphiques des IPs, pages, erreurs HTTP.

# Exports :
- top_ips.csv : contient les 10 adresses IP les plus actives dans les logs
- erreurs_http.json : contient les erreurs HTTP (404, 500...) les plus fréquentes

# Fichiers :
- analyse_logs.py : script principal
- top_ips.csv : IPs les plus fréquentes (export CSV)
- erreurs_http.json : erreurs HTTP (export JSON)
- apache_logs.txt : fichier non inclus ici

