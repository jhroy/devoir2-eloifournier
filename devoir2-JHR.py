# coding : utf-8

import csv, json
import requests

fichier = "lobbying.csv"
fichier = "lobbying-JHR.csv"

url = "http://jhroy.ca/uqam/lobby.json"

entetes = {
    "User-Agent":"Éloi Fournier - 5149732575 : Salut JH, j'essaie de réussir le devoir 2", 
    "From":"eloifournier@gmail.com"
}

req = requests.get(url,headers=entetes)

entreprises = req.json()
# print(entreprises)

for entreprise in entreprises["registre"]:
    if req.status_code == 200:
        # print("Yé")
        infos = [] 
        nb = entreprise[0]["comlog_id"]
        nom = entreprise[0]["fr_client_org_corp_nm"]
        name = entreprise[0]["en_client_org_corp_nm"]
        date = entreprise[0]["date_comm"]
        objet = entreprise[1][0]["objet"] ### MÊME PROBLÈME QU'AMÉLIE! TOUT FONCTIONNE BIEN DANS TON SCRIPT! SAUF QUE TU "ÉCHAPPES" DES CAS... JE VAIS EXPLIQUE EN CLASSE POURQUOI.
        objet2 = entreprise[1][0]["objet_autre"]
        institution = entreprise[2][0]["institution"]
        infos.append(nb)
        infos.append(nom)
        infos.append(name)
        infos.append(date)
        infos.append(objet)
        infos.append(objet2)
        infos.append(institution)
        if "limat" in objet or "limat" in objet2:  
            print(infos)
            dead = open(fichier,"a")
            obies = csv.writer(dead)
            obies.writerow(infos)       

    # Mon fichier csv contient TOUTES les entreprises. J'ai essayé une multitude de solutions, mais j'avais soit toutes les entreprises ou un csv vide...
    # Ok j'avais fait une petite erreur d'indentation mais ça marche finalement! :)