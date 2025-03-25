import re
from collections import Counter
import matplotlib.pyplot as plt

# Lire le fichier de logs
with open("apache_logs.txt", "r") as f:
    lignes = f.readlines()

# Définir un pattern regex pour extraire les infos utiles
pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST|HEAD|PUT|DELETE) (.*?) HTTP.*" (\d{3}) (\d+|-)'

# Listes pour stocker les données extraites
ips = []
pages = []
codes = []

# Parcourir chaque ligne du fichier
for ligne in lignes:
    match = re.match(pattern, ligne)
    if match:
        ip = match.group(1)
        page = match.group(4)
        code = match.group(5)

        ips.append(ip)
        pages.append(page)
        codes.append(code)

# Afficher les résultats dans le terminal
print("\nTop 10 IPs les plus actives :")
print(Counter(ips).most_common(10))

print("\nTop 10 pages demandées :")
print(Counter(pages).most_common(10))

print("\nErreurs les plus fréquentes (codes 4xx/5xx) :")
erreurs = [c for c in codes if c.startswith("4") or c.startswith("5")]
print(Counter(erreurs).most_common())

# Fonction pour créer un graphique
def bar_chart(title, data_dict):
    labels, values = zip(*data_dict.items())
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Générer les graphiques
bar_chart("Top 10 IPs", dict(Counter(ips).most_common(10)))
bar_chart("Top 10 Pages demandées", dict(Counter(pages).most_common(10)))
bar_chart("Erreurs HTTP", dict(Counter(erreurs)))
