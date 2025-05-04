from Bio import SeqIO

acc_list_file = "/u/scratch/y/yuwei/ORF_finding/S1_ACC.txt"
contigs_fasta = "/u/scratch/y/yuwei/ORF_finding/S1.fa"
output_fasta = "/u/scratch/y/yuwei/ORF_finding/S1_ACC_contigs.fa"

# Load list of ACCs
with open(acc_list_file) as f:
    accs = set(line.strip() for line in f)

# Filter and write matching contigs
with open(output_fasta, "w") as out_handle:
    for record in SeqIO.parse(contigs_fasta, "fasta"):
        if record.id in accs:
            SeqIO.write(record, out_handle, "fasta")
