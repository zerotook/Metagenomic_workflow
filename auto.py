#!/u/local/apps/python/3.8.0/bin/python3

import os
import subprocess
from Bio import SeqIO
import pandas as pd

# --------- CONFIGURATION ---------
sample_name = "1F"
contigs_fasta = f"/u/scratch/y/yuwei/ORF_finding/{sample_name}.fa"
orf_protein = f"/u/scratch/y/yuwei/ORF_finding/{sample_name}_ORFs.faa"
orf_gbk = f"/u/scratch/y/yuwei/ORF_finding/{sample_name}_ORFs.gbk"
blast_output = f"/u/scratch/y/yuwei/ORF_finding/blastp_{sample_name}.tsv"
filtered_output = f"/u/scratch/y/yuwei/ORF_finding/blastp_{sample_name}_filtered.tsv"
acc_txt = f"/u/scratch/y/yuwei/ORF_finding/{sample_name}_ACC.txt"
acc_fasta = f"/u/scratch/y/yuwei/ORF_finding/{sample_name}_ACC_contigs.fa"
sarg_db = "/u/scratch/y/yuwei/SARG_DB"

# --------- STEP 1: Run Prodigal ---------
if not os.path.exists(orf_protein):
    print(f"🔧 Running Prodigal for {sample_name}...")
    subprocess.run([
        "prodigal", "-i", contigs_fasta,
        "-o", orf_gbk,
        "-a", orf_protein,
        "-p", "meta"
    ])
else:
    print(f"✅ Prodigal output already exists: {orf_protein}")

# --------- STEP 2: Run BLASTP ---------
if not os.path.exists(blast_output):
    print(f"🔧 Running BLASTP against SARG_DB...")
    subprocess.run([
        "blastp",
        "-query", orf_protein,
        "-db", sarg_db,
        "-out", blast_output,
        "-evalue", "1e-5",
        "-outfmt", "6"
    ])
else:
    print(f"✅ BLASTP output already exists: {blast_output}")

# --------- STEP 3: Filter BLASTP Results ---------
print("🔍 Filtering BLASTP results...")
blast_df = pd.read_csv(blast_output, sep='\t', header=None)
blast_df.columns = ['query_id', 'subject_id', 'identity', 'align_len', 'mismatches',
                    'gap_opens', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bit_score']

query_lengths = {record.id: len(record.seq) for record in SeqIO.parse(orf_protein, 'fasta')}
blast_df['query_len'] = blast_df['query_id'].map(query_lengths)
blast_df['query_cov'] = blast_df['align_len'] / blast_df['query_len']

filtered_df = blast_df[(blast_df['identity'] >= 80) & (blast_df['query_cov'] >= 0.7)]
filtered_df.to_csv(filtered_output, sep='\t', index=False)
print(f"✅ Filtered {len(filtered_df)} ARG-like ORFs saved to {filtered_output}")

# --------- STEP 4: Extract ACC IDs ---------
print("🔎 Extracting ARG-carrying contigs (ACCs)...")
filtered_df['contig_id'] = filtered_df['query_id'].str.replace(r'_\d+$', '', regex=True)
acc_list = filtered_df['contig_id'].unique()
pd.Series(acc_list).to_csv(acc_txt, index=False, header=False)
print(f"✅ {len(acc_list)} ACCs saved to {acc_txt}")

# --------- STEP 5: Extract ACC FASTA ---------
print("📦 Extracting ACC sequences to FASTA...")
with open(acc_txt) as f:
    acc_set = set(line.strip() for line in f)

with open(acc_fasta, "w") as out_handle:
    for record in SeqIO.parse(contigs_fasta, "fasta"):
        if record.id in acc_set:
            SeqIO.write(record, out_handle, "fasta")

print(f"✅ ACC sequences written to {acc_fasta}")
