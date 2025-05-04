#!/u/local/apps/python/3.8.0/bin/python3

import pandas as pd

# Path to input BLASTP filtered results (update path if needed)
blastp_file = "/u/scratch/y/yuwei/ORF_finding/blastp_S1_filtered.tsv"

# Output file for ACC list
output_file = "/u/scratch/y/yuwei/ORF_finding/S1_ACC.txt"

# Load filtered BLASTP output
df = pd.read_csv(blastp_file, sep='\t')

# Extract contig name by removing the last "_<number>" from ORF ID
df['contig_id'] = df['query_id'].str.replace(r'_\d+$', '', regex=True)

# Get unique contig IDs with ARGs
acc_list = df['contig_id'].unique()

# Save ACCs to file
pd.Series(acc_list).to_csv(output_file, index=False, header=False)

print(f"✅ Total ACCs found: {len(acc_list)} and saved to {output_file}")
