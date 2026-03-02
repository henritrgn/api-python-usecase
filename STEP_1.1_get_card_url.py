#We want card name of Black and white set with : number / total number.
from tcgdexsdk import TCGdex, Query
import requests

#opérations sur les sets
sdk = TCGdex("fr")
sets = sdk.set.listSync()

#id de sets
sets_id_list=[s.id for s in sets]
sets_name_list=[s.name for s in sets]
id_Black_and_White=[sets_id_list[k] for k in range(len(sets_name_list)) if sets_name_list[k]=="Noir & Blanc"][0]

#opération sur les cartes :
def cardlistBW():
    cards=sdk.card.listSync()
    cards_of_Black_and_White=[cards[k] for k in range(len(cards)) if cards[k].id.startswith(id_Black_and_White + "-")]
    return cards_of_Black_and_White

#pour avoir les url (images cartes) :
def getcardurl():
    cardlist=cardlistBW()
    urls=[cardlist[k].get_image_url("high","png") for k in range(len(cardlist))]
    return urls


#Main (stocker les urls dans un .txt) :
urls = getcardurl()

with open("files.txt", "w", encoding="utf-8") as f:
    for elem in urls:
        f.write(elem + "\n")
