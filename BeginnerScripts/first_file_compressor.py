def rle_compress(data):
    """Komprimerer data ved bruk av run-length encoding (RLE).
    
    Denne metoden analyserer kontinuerlige like elementer i dataen,
    og representerer dem som et par (element, antall), der 'element'
    er selve dataelementet og 'antall' er hvor mange ganger det
    gjentas i rekkefølge.
    """
    compressed = []  # Liste for å lagre komprimerte data som tuples
    i = 0  # Startindeks for iterasjon

    # Gå gjennom hele dataen
    while i < len(data):
        count = 1  # Teller for antall like påfølgende elementer

        # Tell opp så lenge neste element er det samme
        while i + 1 < len(data) and data[i] == data[i + 1]:
            i += 1
            count += 1  # Øk telleren for hvert like element

        # Legg til tegnet og antallet i komprimeringsresultatet
        compressed.append((data[i], count))
        i += 1  # Fortsett til neste unike element

    return compressed


def rle_decompress(compressed_data):
    """Dekomprimerer data komprimert med run-length encoding.

    For hvert par (verdi, antall) i den komprimerte data, gjenskapes
    den originale sekvensen ved å multiplisere 'verdi' med 'antall'.
    """
    decompressed = []  # Liste for å lagre dekomprimerte data

    # Gå gjennom hvert par (verdi, antall) i komprimert data
    for value, count in compressed_data:
        # Utvid den dekomprimerte listen med 'verdi' gjentatt 'count' ganger
        decompressed.extend([value] * count)

    return decompressed


# Eksempel på bruk av funksjonene
original_data = "aaabbbcccaaa"  # Vår prøve-data å komprimere
compressed = rle_compress(original_data)  # Komprimer testdata
print("Komprimert:", compressed)  # Vis komprimert resultat

decompressed = rle_decompress(compressed)  # Dekomprimer til original
print("Dekomprimert:", ''.join(decompressed))  # Vis dekomprimert resultat