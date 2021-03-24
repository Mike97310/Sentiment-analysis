from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def scraping(choix, location):
    url = "https://fr.trustpilot.com/categories"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')

    # On va chercher les noms des catégories
    categorie = soup.find_all("div", class_="categories_subCategoryList__1FB-L")

    for i in categorie:

        cate = i.find("div", class_="categories_subCategoryItem__2Qwj8").a.text.strip()

        if i == categorie[3]:
            break

    # On va chercher les noms des sous catégories
    sous_categorie = soup.find_all("div", class_="categories_subCategoryItem__2Qwj8")

    toute_sous_categorie = []

    for souscatego in sous_categorie:
        cate = souscatego.find("span")
        toute_sous_categorie.append(cate)

    # On filtre pour avoir que le texte
    tsg = []
    for i in toute_sous_categorie:
        mod = i.string.replace("<span>", "")
        tsg.append(mod)

    # On récupère les catégorie pour le lien
    find_location = soup.find_all('a',
                                  class_="link_internal__YpiJI typography_typography__23IQz typography_weight-inherit__2IsoB typography_fontstyle-inherit__PIgau link_navigation__2cxCi")
    cat = []
    for val in find_location:
        p = val.get("href")
        if p.startswith("/categories/"):
            s = p.split("/categories/")
            q = s[1]
            cat.append(q)

    # On prend juste les grandes catégories
    cat = cat[:22]
    len(cat)

    # On laisse le choix à l'utlisateur du choix de la catégorie
    categories = []
    scrape = True

    while scrape is True:
        print()
        if choix in cat:
            categories = choix
            scrape = False
        else:
            print()
            print("Votre choix n'est pas dans la liste !!")
            print()

    # Variables invariables
    numberOfReviews = '0'
    status = 'all'
    timeperiod = '0'

    url = 'https://fr.trustpilot.com/categories/' + categories + '?location=' + location + '&numberofreviews=' + numberOfReviews + '&page=1&status=' + status + '&timeperiod=0=' + timeperiod
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')

    # On récupère les liens dans une liste
    links = soup.find_all('a', class_='link_internal__YpiJI link_wrapper__LEdx5')
    liens = []

    # On fait une boucle pour récuperer juste le nom des liens
    for lien in links:
        p = lien.get("href")
        if p.startswith("/review/"):
            s = p.split("/review/")
            q = s[1]
            liens.append(q)

    # Création de variables
    avis = []
    page_nb = []

    # On fait une boucle pour naviger parmis les liens d'une liste
    for lien in liens[:3]:
        url = 'https://fr.trustpilot.com/review/' + lien + '?page=1'
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')

        # On divise la nombres d'avis total pour 20 pour avoir le nombre de pages
        nb_reviews = soup.find('span', class_='headline__review-count').text.replace(" ", "")
        nb_reviews = int(nb_reviews)
        page_nb = int(nb_reviews / 20) + (nb_reviews % 20 > 0)
        page_nb = str(page_nb)

        # On fait une boucle pour trouver touts les avis
        for i in range(0, int(page_nb)):
            url = 'https://fr.trustpilot.com/review/' + lien + '?page=' + str(i + 1)
            req = requests.get(url).text
            soup = BeautifulSoup(req, 'html.parser')

            reviews = soup.find_all("p", class_="review-content__text")

            # On récupère touts les avis dans une liste
            for review in reviews:
                review = review.get_text()
                avis.append(review)

    # TODO
    avis = list(set(avis))
    return avis
