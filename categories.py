from bs4 import BeautifulSoup
import requests


def categorie_function():


    # récupération des catégories qui seront utilisé pour modifier l'url plus tard

    url = "https://fr.trustpilot.com/categories"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')


    # les liens en français, en les associant aux liens en anglais pour créer une traduction
    soup_categorie_fr = soup.find_all("div", class_="categories_subCategoryItem__2Qwj8")

    categorie_fr = []

    for souscatego in soup_categorie_fr:
        fr = souscatego.find("span").text
        categorie_fr.append(fr)



    # les href utilisable pour modifier l'url dans la grande boucle

    soupe_categorie_ang = soup.find_all('a', class_="link_internal__YpiJI typography_typography__23IQz typography_weight-inherit__2IsoB typography_fontstyle-inherit__PIgau link_navigation__2cxCi")

    categorie_ang = []

    for lien in soupe_categorie_ang:
        texte_des_liens = lien.get("href")
        if texte_des_liens.startswith("/categories/"):
            juste_les_liens = texte_des_liens.split("/categories/")
            voila_les_liens = juste_les_liens[1]
            categorie_ang.append(voila_les_liens)

    # mais les 22 premiers ne sont pas utilies, et sont en doublons en plus ....
    categories_globale = []
    categories_globale = categorie_ang[:22]
    categorie_ang = [x for x in categorie_ang if x not in categories_globale]

    return categorie_ang