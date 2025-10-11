# Environmental metagenomic general introduction
Workflow for a shotgun Metagenomic Seuqncing:
  1. Sample Preparation (filtering with 0.45 um filters)
  2. DNA Extraction (MPBio Fast Soil Extraction Kit)
  3. Quantification and Quality control for samples (done by Mr.DNA Lab)
  4. Library Constraction (done by Mr. DNA Lab)
  5. Sequencing: sequenced paired end for 300 cycles using the NovaSeq 6000 system (Illumina), producing short read 2*150bp 30 million (for Michigan CAFO project)
  6. Bioinformatic Analysis  
     (1)Once sequenced, the read then go through data quality control to filter the adapters and low-quality reads.  
     (2)After data filter, the clean reads can proceed to assemble and annote for furthre downstream analyses.  
     (3)Following this, multiple analysis pipeline could be conducted depending on the samples and questions we want to explore. These include but are not limited to:  
         Taxonomy annotation/ PCA and NMDS analyses/ Antibiotic-Resistant Gene Distributions/ etc.
![image](https://github.com/zerotook/Assembly/assets/102132762/2c2cc0cf-dc43-43a4-8c42-dd2dec515cde)

# Galaxy: trim with Trimmomatic, assemble with MEGAHIT, and QC
To help understand assemble process, check https://www.youtube.com/watch?v=RcYXTpNS_XU
1. Go to www.usegalaxy.org and create an account.
2. Create a history and upload your paired end fastq reads (each sample gets two files: R1 and R2).
3. Go to Workflow Tab, import workflow through this url: https://usegalaxy.org/u/alice_k/w/trimming-quality-control-and-megahit and run the workflow.
   ![image](https://github.com/zerotook/Assembly/assets/102132762/66bd4711-a40c-4423-b2d5-c8e7e6d2e810)
4. Run the workflow with your files.
5. QC Reports for trimmed R1/R2 and assembled contigs files (fasta) will be generated after you run the workflow.

# ARGsOAP v3.2.0
1. Login to your H2C using  
```
ssh youraccountname@hoffman2.idre.ucla.edu
```
  To keep your ssh session alive, you can use
```
ssh -o ServerAliveInterval=60 youraccountname@hoffman2.idre.ucla.edu
```
2. Using compute nodes to request interactive sessions, for example  
```
qrsh -l h_data=8G,h_rt=8:00:00 -pe shared 8
```
- More detail about compute nodes can be found at https://www.hoffman2.idre.ucla.edu/Using-H2/Computing/Computing.html.
  
3. Install ARGsOAP ([git source](https://github.com/xinehc/args_oap), [video instruction](https://smile.hku.hk/static/args/tools/HowToUseVersion3_2.mp4))
```
module load anaconda3
conda create -n args_oap -c bioconda -c conda-forge args_oap
conda activate args_oap
```
4. Upload your assembled file to your desired input folder, run stage one.
```
#for assembled file:
args_oap stage_one -i yourinputfolderpath -o youroutputfoldername -f fasta -t 20

#for unassembled pair end reads in fastq gzip format:
#download your trimmed fastq.gz file from www.usegalaxy.org using wget, rename as _R1.fq.gz and _R2.fq.gz
args_oap stage_one -i yourinputfolderpath -o youroutputfoldername -f fq.gz -t 20
```
5. Run stage two
```
args_oap stage_two -i youroutputfoldername -t 20
```
6. cd to your output folder to check outputs after the stages.
 
- for help information `args_oap stage_one/two -h`

# MetaCompare 2.0
Web Service: http://metacompare.cs.vt.edu/  
Git Source: https://github.com/mrumi/MetaCompare2.0  
1. Install MetaCompare 2.0 and alignment tools
**Step 1:** Change the current working directory to the location where you want the cloned `MetaCompare2.0` directory to be made, and run the following code to install required Python packages and alignment tools
 ```
# install necessary packages and alignments
 module load anaconda3
 conda create -n MetaCompare
 conda activate MetaCompare
 conda install -c anaconda numpy
 conda install -c anaconda pandas
 conda install -c anaconda biopython
 conda install -c anaconda pprodigal
```
**Step 2:** Clone the repository using git command and move to code directory
```
 git clone https://github.com/mrumi/MetaCompare2.0.git
```
**Step 3:** Downloading the database using the following command
```
wget https://zenodo.org/api/records/10626079/files/metacmpDB.tar.gz/content
# Rename that file
mv content metacmpDB.tar.gz
# Uncompress the database before using
tar -zxvf metacmpDB.tar.gz
```
2. Running MetaCompare 2.0
```
python metacompare.py -c S1.fa -t 64 -b 0
#modify S1.fa to your assembled file name
```
Your final output will be like
![image](https://github.com/user-attachments/assets/a83784a1-1bc4-4c76-982b-f40bfc89be7d)
S1_out.txt will contain the final computed risk scores.

- You can see detailed description for command line options by using `-h` option.
```
python metacompare.py -h
```
![image](https://github.com/user-attachments/assets/88ed2ebf-1716-436c-ad5f-3a4073239c80)

 - qrsh command needed to run MetaCompare, default settings are not enough for computing purposes, for example: 
    `qrsh -l h_rt=3:00:00,h_data=8G -pe shared 12`
    `qrsh -l h_rt=3:00:00,h_data=16G -pe shared 8`
 
The provided code is designed for Windows systems. Mac users may need to modify the code to ensure compatibility with the system.


# NMDC-EDGE: Bacterial Community (Kraken2)
1. Go to https://nmdc-edge.org/user/ and create an account.
2. Upload your FASTQ files to run the workflow.
3. Download report output and upload to Galaxy for diversity further analysis.
![image](https://github.com/user-attachments/assets/a0c1da86-2d36-4148-93a6-12fd9147f33b)
- or upload your report file to Pavian (https://github.com/fbreitwieser/pavian) for further analysis.

# ARG Carrying Contigs Analysis
1. Prodigal to get faa and fna
```
prodigal -i /dir/S1.fasta -a /dir/S1_ORFs.faa -p meta
prodigal -i /dir/S1.fasta -d /dir/S1_ORFs.faa -p meta
```
  - if want to run without showing jumping lines on the screen, use
```
 nohup prodigal -i /u/scratch/y/yuwei/alr2/assemblies/11S.fasta -d 11S_ORFs.fna -p meta > prodigal.out 2>&1 &
```
2. Run salmon on fna
```
salmon index -t /u/scratch/y/yuwei/alr2/assemblies/1S_ORFs.fna -i salmon_idx_1S -p 4
salmon quant -i salmon_idx_1S/ -l A -1 /u/scratch/y/yuwei/alr2/reads/1S_R1.fq.gz -2 /u/scratch/y/yuwei/alr2/reads/1S_R2.fq.gz -p 4 --validateMappings --gcBias -o salmon_1S_ARGs --meta
```
3. Blastp on faa from prodigal to get ARG annotations on ORFs
```
#Build Database First, download from Zenodo link
wget link
mkdb file fasta (not finished
#edit the sh file based on the computing environment you need
qsub -v QUERY=/u/scratch/y/yuwei/alr2/assemblies/S1_ORFs.faa,DB=/u/scratch/y/yuwei/ACC/sarg2025/arg2025,OUT=/u/scratch/y/yuwei/ACC/blastp_S1_outfmt7.txt blastp_arg_qsub.sh
```
5. Filter generated blastp based on set standards and extract assembled fasta file based on filtered blastp
```
#Filter blastp file based on the standard you set, if an ORF have multiple results, this code will select only one result to keep (based on bit score, etc.) so that the number won't count twice during coverM
python /dir/filter_subset_orf.py   --blast /u/scratch/y/yuwei/ACC/blastp_4S_outfmt7.txt   --orf-faa /u/scratch/y/yuwei/alr2/assemblies/4S_ORFs.faa   --out-tsv /u/scratch/y/yuwei/ACC/ORF/4S_best_per_orf.tsv   --ident-min 80 --qcov-min 0.70 --evalue-max 1e-5
#Extract fasta file based on contig carrying ARGs
python /dir/Extract_fa.py -f /u/scratch/y/yuwei/ACC/blastp_S1_outfmt7.txt -a /u/scratch/y/yuwei/alr2/assemblies/S1.fasta -t S1_ACC.txt -o S1_ACC_contigs.fa
```
6. Run coverM on fa
```
#could run on S1_ACC_contigs.fa if need results sooner
coverm contig --coupled /u/scratch/y/yuwei/alr2/reads/1F_R1.fq.gz /u/scratch/y/yuwei/alr2/reads/1F_R2.fq.gz --reference /u/scratch/y/yuwei/ACC/1F_ACC_contigs.fa --methods tpm --output-file 1F_tpm.tsv -t 4
```
