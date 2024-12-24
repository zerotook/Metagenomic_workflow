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

# Galaxy - trim with Trimmomatic, assemble with MEGAHIT, and QC
To understand assemble process, check https://www.youtube.com/watch?v=RcYXTpNS_XU
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
2. Using compute nodes to request interactive sessions, for example  
```
qrsh -l h_data=8G,h_rt=8:00:00 -pe shared 8
```
  More detail about compute nodes can be found at https://www.hoffman2.idre.ucla.edu/Using-H2/Computing/Computing.html.  
3. Install ARGsOAP (source - https://github.com/xinehc/args_oap, video instruction: https://smile.hku.hk/static/args/tools/HowToUseVersion3_2.mp4)  
```
module load anaconda3
conda create -n args_oap -c bioconda -c conda-forge args_oap
conda activate args_oap
```
4. Upload your assembled file to your desired input folder, run stage one
for assembled file
```
args_oap stage_one -i yourinputfolderpath -o youroutputfoldername -f fasta -t 20
```
for unassembled pair end reads: download your trimmed fastq.gz file to your H2C SCRATCH folder using command wget, rename as _R1.fq.gz and _R2.fq.gz
![image](https://github.com/user-attachments/assets/2481236e-73cf-4f7e-a606-96c586fef2c8)

```
args_oap stage_one -i /u/scratch/y/yuwei/ARGsOAP -o /u/scratch/y/yuwei/ARGsOAP/output -f fq.gz -t 20
```
5. Run stage two
```
args_oap stage_two -i youroutputfoldername -t 20
```
  cd to your output folder to check outputs after the stages.

    for help information
    ```
    args_oap stage_one/two -h
    ```

# MetaCompare 2.0
Web Service: http://metacompare.cs.vt.edu/
Git Source: https://github.com/minoh0201/MetaCompare



