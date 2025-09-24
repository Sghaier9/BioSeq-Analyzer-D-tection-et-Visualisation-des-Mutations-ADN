import numpy as np
import matplotlib.pyplot as plt

# Couleurs pour chaque base
color_map = {
    "A": [1.0, 0.0, 0.0],  # Rouge pour A
    "T": [0.0, 1.0, 0.0],  # Vert pour T
    "G": [0.0, 0.0, 1.0],  # Bleu pour G
    "C": [1.0, 1.0, 0.0]   # Jaune pour C
}

def sequence_to_image(sequence, output_path="results/sequence.png", scale=20, show=True):
    """
    Convertit une séquence ADN en image colorée et l'affiche avec matplotlib.
    """

    # Créer une image 1 ligne = taille séquence, 3 canaux couleur (RGB)
    img = np.zeros((1, len(sequence), 3))

    # Associer chaque base à une couleur
    for i, base in enumerate(sequence):
        img[0, i] = color_map.get(base.upper(), [1.0, 1.0, 1.0])  # blanc si inconnu

    # Agrandir l'image
    img = np.repeat(img, scale, axis=0)

    # Sauvegarder l'image
    plt.imsave(output_path, img)
    print(f"Image générée et enregistrée : {output_path}")

    # Afficher avec Matplotlib si demandé
    if show:
        plt.figure(figsize=(12, 2))
        plt.imshow(img)
        plt.title("Visualisation de la séquence ADN")
        plt.axis("off")
        plt.show()
