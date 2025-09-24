def read_fasta(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
        
    sequence = ''.join([line.strip() for line in lines if not line.startswith('>')])
    return sequence