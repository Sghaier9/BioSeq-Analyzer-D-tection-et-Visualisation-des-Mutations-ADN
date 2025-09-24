def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    m, n = len(seq1), len(seq2)

    # score matrix initialized
    score = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and first column
    for i in range(m + 1):
        score[i][0] = i * gap
    for j in range(n + 1):
        score[0][j] = j * gap

    # Fill in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diag = score[i - 1][j - 1] + match
            else:
                diag = score[i - 1][j - 1] + mismatch
            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap
            score[i][j] = max(diag, up, left)

    # Go back to rebuild the alignment
    align1, align2 = '', ''
    i, j = m, n

    while i > 0 or j > 0:
        current = score[i][j]
        if i > 0 and j > 0 and (seq1[i - 1] == seq2[j - 1] and current == score[i - 1][j - 1] + match or
                                seq1[i - 1] != seq2[j - 1] and current == score[i - 1][j - 1] + mismatch):
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif i > 0 and current == score[i - 1][j] + gap:
            align1 = seq1[i - 1] + align1
            align2 = '-' + align2
            i -= 1
        else:
            align1 = '-' + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    return align1, align2

def detect_mutations(aligned_ref, aligned_sample):
    mutations = []
    pos_ref = 0

    for i in range(len(aligned_ref)):
        base_r = aligned_ref[i]
        base_s = aligned_sample[i]

        if base_r != '-':
            pos_ref += 1

        if base_r == base_s:
            continue

        if base_r == '-':
            mutation_type = "Insertion"
        elif base_s == '-':
            mutation_type = "Deletion"
        else:
            mutation_type = "Substitution"

        mutations.append({
            "Position": pos_ref,
            "Base_ref": base_r,
            "Base_sample": base_s,
            "Type": mutation_type
        })

    return mutations

