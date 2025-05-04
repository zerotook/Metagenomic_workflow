from Bio import SeqIO
import pandas as pd

# Load BLASTP output
blast_df = pd.read_csv('/u/scratch/y/yuwei/ORF_finding/blastp_S1.tsv',
                       sep='\t', header=None)

blast_df.columns = ['query_id', 'subject_id', 'identity', 'align_len', 'mismatches',
                    'gap_opens', 'q_start', 'q_end', 's_start', 's_end',
                    'evalue', 'bit_score']

# Load query sequences and lengths
fasta_file = '/u/scratch/y/yuwei/ORF_finding/S1_ORFs.faa'
query_lengths = {record.id: len(record.seq) for record in SeqIO.parse(fasta_file, 'fasta')}

# Add query lengths and calculate query coverage
blast_df['query_len'] = blast_df['query_id'].map(query_lengths)
blast_df['query_cov'] = blast_df['align_len'] / blast_df['query_len']

# Apply filtering: identity ≥ 80%, query coverage ≥ 70%
filtered_df = blast_df[(blast_df['identity'] >= 80) &
                       (blast_df['query_cov'] >= 0.7)]

# Save filtered results
filtered_df.to_csv('/u/scratch/y/yuwei/ORF_finding/blastp_S1_filtered.tsv', sep='\t', index=False)

print(f"Filtered results saved. {filtered_df.shape[0]} hits passed filtering criteria.")
