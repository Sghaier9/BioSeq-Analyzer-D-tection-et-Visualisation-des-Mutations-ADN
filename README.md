# 🧬 BioSeq Analyzer — Détection et Visualisation des Mutations ADN

##  Description du projet
BioSeq Analyzer est un projet de bio-informatique en Python permettant :
- De lire des séquences ADN au format FASTA.
- D'aligner deux séquences ADN grâce à l’algorithme Needleman-Wunsch.
- De détecter automatiquement les mutations  substitutions, insertions, et délétions.
- De générer aléatoirement des séquences pour les tests.
- De visualiser graphiquement les séquences et mutations via Matplotlib.

---

##  Structure du projet
BIO/
│── data/
│ ├── reference.fasta
│ ├── sample.fasta
│
│── results/
│ ├── mutations.csv
│
│── fasta_utils.py
│── mutation_analyzer.py
│── generate_fasta.py
│── vision_utils.py
│── main.py
│── requirements.txt
│── README.md


# Installation

```bash
git clone https://github.com/username/BioSeq-Analyzer.git
cd BioSeq-Analyzer
pip install -r requirements.txt
```


---

# Utilisation

## Générer des séquences ADN aléatoires
```bash
python generate_fasta.py
```
# Visualisation ADN

Le module `vision_utils.py` génère une **représentation graphique** des séquences ADN et affiche les bases **A, T, G, C** avec des couleurs distinctes :

- 🟥 A → Rouge
- 🟩 T → Vert
- 🟦 G → Bleu
- 🟨 C → Jaune

# Technologies utilisées
- Python 3.11
- Matplotlib
- NumPy
- Biopython
- Algorithme Needleman-Wunsch

# Auteur
**Mohamed Aziz Sghaier**  
📧 Email : sghaieraziz9@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-aziz-sghaier-9a2a012b2/)
