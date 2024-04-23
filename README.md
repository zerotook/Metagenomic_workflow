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

# Galaxy - trim with Trimmomatic and QC
1. Go to www.usegalaxy.org and create an account.
2. Create a history and upload your paired end fastq reads (each sample gets two files: R1 and R2).
3. Go to Workflow Tab, import workflow through this url: https://usegalaxy.org/u/alice_k/w/trimming-quality-control-and-megahit and run the workflow.
   ![image](https://github.com/zerotook/Assembly/assets/102132762/66bd4711-a40c-4423-b2d5-c8e7e6d2e810)
4. Run the workflow with your files.
5. QC Reports for trimmed R1/R2 and assembled contigs files will be generated after you run the workflow.

# ARGsOAP v3.2.0
1. Login to your H2C using
```
ssh youraccountname@hoffman2.idre.ucla.edu
```
To keep your ssh session alive, you can use
```
ssh -o ServerAliveInterval=60 youraccountname@hoffman2.idre.ucla.edu
```
2. Request
```
qrsh -l h_data=16G,h_rt=5:00:00 -pe shared 12\
```
