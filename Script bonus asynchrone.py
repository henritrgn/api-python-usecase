import asyncio
from tcgdexsdk import TCGdex

async def main():
    # Initialiser le SDK
    sdk = TCGdex("en")

    # Récupérer la liste des cartes
    cards = await sdk.card.list()

    # Prendre la première carte
    card = cards[0]

    # Afficher les informations de base de la carte
    print(f"ID: {card.id}")
    print(f"Nom: {card.name}")
    print(f"Local ID: {card.localId}")

    # Afficher l'aide de la méthode get_image_url
    print("\n--- Documentation de get_image_url ---")
    help(card.get_image_url)


asyncio.run(main())
