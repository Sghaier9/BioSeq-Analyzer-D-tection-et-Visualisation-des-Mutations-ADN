from fasta_utils import read_fasta
from mutation_analyzer import needleman_wunsch
from mutation_analyzer import detect_mutations
import csv
from vision_utils import sequence_to_image


reference = read_fasta("data/reference.fasta")
sample = read_fasta("data/sample.fasta")

align_ref, align_sample = needleman_wunsch(reference, sample)

print("\n ALIGNEMENT :")
print("Reference : ", align_ref)
print("echantillon: ", align_sample)

mutations = detect_mutations(align_ref, align_sample)

print("\n MUTATIONS DETECTEES :")
for m in mutations:
    print(f"Position {m['Position']}: {m['Base_ref']} -> {m['Base_sample']} ({m['Type']})")

# Sauvegarder les mutations dans un CSV
with open("results/mutations.csv", mode="w", newline="") as fichier:
    champs = ["Position", "Base_ref", "Base_sample", "Type"]
    writer = csv.DictWriter(fichier, fieldnames=champs)
    writer.writeheader()
    writer.writerows(mutations)

# Affiche la séquence de référence sous forme d'image
sequence_to_image(reference, "results/reference.png", scale=20, show=True)

# Affiche l'échantillon sous forme d'image
sequence_to_image(sample, "results/sample.png", scale=20, show=True)