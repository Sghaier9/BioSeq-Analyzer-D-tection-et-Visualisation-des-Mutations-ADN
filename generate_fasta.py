import random

def generer_sequence_adn(taille):
    """Génère une séquence ADN aléatoire de longueur `taille`."""
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(bases, k=taille))

def ecrire_fasta(nom_fichier, id_seq, sequence):
    """Écrit une séquence ADN dans un fichier FASTA sur UNE SEULE LIGNE."""
    with open(nom_fichier, 'w') as f:
        f.write(f">{id_seq}\n")
        f.write(sequence + "\n")


if __name__ == "__main__":
    # Générer une séquence de référence de 80 bases
    seq_ref = generer_sequence_adn(80)
    ecrire_fasta("data/reference.fasta", "ref_seq", seq_ref)

    # Générer une séquence d'échantillon basée sur la référence
    seq_sample = list(seq_ref)

    # Introduire quelques mutations aléatoires
    for _ in range(5):  # 5 mutations aléatoires
        position = random.randint(0, len(seq_sample)-1)
        seq_sample[position] = random.choice(['A', 'T', 'C', 'G'])

    seq_sample = ''.join(seq_sample)
    ecrire_fasta("data/sample.fasta", "sample_seq", seq_sample)
    print("Fichiers générés dans le dossier data/")
    print(" - data/reference.fasta")
    print(" - data/sample.fasta")

    print(" Fichiers générés : data/reference.fasta et data/sample.fasta")
