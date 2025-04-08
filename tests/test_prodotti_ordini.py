import pytest
from progetto.prodotti_ordini import Prodotto, Ordine  

def test_calcola_totale():
    # Crea alcuni oggetti Prodotto
    prodotto1 = Prodotto("Prodotto 1", 10.50)
    prodotto2 = Prodotto("Prodotto 2", 20.00)
    prodotto3 = Prodotto("Prodotto 3", 5.75)

    # Crea un oggetto Ordine e aggiungi i prodotti
    ordine = Ordine("Cliente 1")
    ordine.aggiungi_prodotto(prodotto1)
    ordine.aggiungi_prodotto(prodotto2)
    ordine.aggiungi_prodotto(prodotto3)

    # Calcola il totale dell'ordine
    totale = ordine.calcola_totale()

    # Verifica che il totale sia corretto
    assert totale == 36.25
