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

## Galaxy - trim with Trimmomatic
## Galaxy - QC
