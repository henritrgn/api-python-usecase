#We want info about BW cards (Picture + Data)
from tcgdexsdk import TCGdex, Query
import requests

#always begin with an endpoint + method (here with set) :
sdk = TCGdex("fr")
sets = sdk.set.listSync()

#what is the set id :
sets_id_list=[s.id for s in sets]
sets_name_list=[s.name for s in sets]
id_Black_and_White=[sets_id_list[k] for k in range(len(sets_name_list)) if sets_name_list[k]=="Noir & Blanc"][0]

#The cards in BW :
def cardlistBW():
    cards=sdk.card.listSync()
    cards_of_Black_and_White=[cards[k] for k in range(len(cards)) if cards[k].id.startswith(id_Black_and_White + "-")]
    return cards_of_Black_and_White

def idlistBW():
    my_cards=cardlistBW()
    return [my_cards[k].id for k in range(len(my_cards))]

def getfullpokemonBW():
     return [sdk.card.getSync(i) for i in idlistBW()]

def getattributesBW():
    pokemon_BW = getfullpokemonBW()[75]
    attributes = vars(pokemon_BW).keys()

    for elem in attributes:
        print(elem, " : ", getattr(pokemon_BW, elem), "\n")
    #print(key : value)
    #with line space

getattributesBW()

