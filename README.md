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
3. Install ARGsOAP (source - https://github.com/xinehc/args_oap, video instruction - https://smile.hku.hk/static/args/tools/HowToUseVersion3_2.mp4)  
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
for unassembled pair end reads in fastq gzip format: download your trimmed fastq.gz file to your H2C SCRATCH folder using command wget, rename as _R1.fq.gz and _R2.fq.gz
  ![]![image](https://github.com/user-attachments/assets/2481236e-73cf-4f7e-a606-96c586fef2c8)
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
pip install numpy
  415  pip install pandas
  416  pip install pandas --upgrade pip
  417  pip install biopython
  418  module load python 3.8
  419  module load python/3.9.6
  420  pip install numpy
  421  pip install --upgrade pip
  422  pip install pandas
  423  pip install biopython
  424  pip install pprodigal
  425  # downloading the tool
  426  wget http://github.com/bbuchfink/diamond/releases/download/v2.1.9/diamond-linux64.tar.gz
  427  tar xzf diamond-linux64.tar.gz
  428  # creating a diamond-formatted database file
  429  ./diamond makedb --in reference.fasta -d reference
  430  # running a search in blastp mode
  431  ./diamond blastp -d reference -q queries.fasta -o matches.tsv
  432  # running a search in blastx mode
  433  ./diamond blastx -d reference -q reads.fasta -o matches.tsv
  434  # downloading and using a BLAST database
  435  update_blastdb.pl --decompress --blastdb_version 5 swissprot
  436  ./diamond prepdb -d swissprot
  437  ./diamond blastp -d swissprot -q queries.fasta -o matches.tsv
  438  ls
  439  wget https://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz; tar xvfz mmseqs-linux-avx2.tar.gz; export PATH=$(pwd)/mmseqs/bin/:$PATH
  440  ls
  441  module load anaconda
  442  module load anaconda3
  443  conda install -c anaconda numpy
  444  ~$ git clone https://github.com/mrumi/MetaCompare2.0.git
  445  git clone https://github.com/mrumi/MetaCompare2.0.git
  446  ls
  447  cd MetaCompare2.0/
  448  ls
  449  wget https://zenodo.org/api/records/10626079/files/metacmpDB.tar.gz/content
  450  ls
  451  mv content metacmpDB.tar.gz
  452  ls
  453  MetaCompare2.0$ tar -zxvf metacmpDB.tar.gz
  454  tar -zxvf metacmpDB.tar.gz
  455  python metacompare.py -c S1.fa
  456  module load python/3.9.6
  457  python metacompare.py -c S1.fa
  458  pip install biopython
  459  pip install pandas
  460  pip install pprodigal
  461  python metacompare.py -c S1.fa
  462  --no-warn-script-location
  463  nano ~/.bashrc
  464  cd $SCRATCH
  465  ls
  466  cd MetaCompare2.0/
  467  ls
  468  module load python/3.9.6
  469  python metacompare.py -c S1.fa
  470  pip install pprodigal
  471  module load python/3.9
  472  python metacompare.py -c S1.fa
  473  echo $PATH
  474  export PATH=$PATH:/u/home/y/yuwei/.local/bin
  475  source ~/.bashrc
  476  ls
  477  cd $SCRATCH
  478  ls
  479  cd MetaCompare2.0/
  480  ls
  481  python metacompare.py -c S1.fa
  482  module load python/3.9.65
  483  module load python/3.9.6
  484  ls
  485  python metacompare.py -c S1.fa
  486  export PATH=$PATH:/u/home/y/yuwei/.local/bin
  487  python metacompare.py -c S1.fa
  488  echo $PATH
  489  export PATH=$PATH:/u/scratch/y/yuwei
  490  which diamond
  491  python metacompare.py -c S1.fa
  492  which prodigal
  493  wget https://github.com/hyattpd/Prodigal/archive/v2.6.1.tar.gz
  494  ls
  495  tar xzf v2.6.1.tar.gz
  496  ls
  497  cd Prodigal-2.6.1/
  498  ls
  499  make install
  500  ./prodigal -h
  501  export PATH=/u/scratch/y/yuwei/MetaCompare2.0/Prodigal-2.6.1/:$PATH
  502  ls
  503  cd ..
  504  ls
  505  python metacompare.py -c S1.fa
  506  ls
  507  cd ..
  508  module load anaconda3
  509  conda install -c anaconda numpy
  510  conda create -n MetaCompare
  511  conda activate MetaCompare2.0/
  512  conda activate MetaCompare2.0
  513  conda activate MetaCompare
  514  conda install -c anaconda numpy
  515  conda install -c anaconda pandas
  516  conda install -c anaconda biopython
  517  conda install -c anaconda pprodigal
  518  swapon --show
  519  free -h
  520  free -m
  521  conda install -c anaconda pprodigal
  522  logout
  523  cd $SCRATCH
  524  module load python/3.9.6
  525  ls
  526  cd MetaCompare2.0/
  527  ls
  528  python metacompare.py -c S1.fa
  529  module load anaconda3
  530  ls
  531  conda activate MetaCompare
  532  ls
  533  conda install -c bioconda pprodigal
  534  conda list
  535  conda install -c bioconda diamond=0.9.14
  536  conda install -c bioconda mmseqs2
  537  python metacompare.py -c S1.fa
  538  python metacompare.py -h
  539  wget https://usegalaxy.org/api/datasets/f9cad7b01a472135b61348dcf3a9ce04/display?to_ext=fasta
  540  python metacompare.py -c MI_1F.fa
  541  wget https://usegalaxy.org/api/datasets/f9cad7b01a472135c8b1ae6a0ab9de5a/display?to_ext=fasta
  542  rm display\?to_ext\=fasta MI_2F.fa
  543  ls
  544  wget https://usegalaxy.org/api/datasets/f9cad7b01a472135c8b1ae6a0ab9de5a/display?to_ext=fasta
  545  python metacompare.py -c MI_2F.fa
  546  which pprodigal
  547  python metacompare.py -c S1.fa
  548  ls
  549  wget http://github.com/bbuchfink/diamond/releases/download/v2.1.9/diamond-linux64.tar.gz
  550  tar xzf diamond-linux64.tar.gz
  551  ls
  552  wget https://mmseqs.com/latest/mmseqs-linux-sse41.tar.gz; tar xvfz mmseqs-linux-sse41.tar.gz; export PATH=$(pwd)/mmseqs/bin/:$PATH
  553  ls
  554  python metacompare.py -c S1.fa
  555  export PATH=$PATH:/u/scratch/y/yuwei/MetaCompare2.0
  556  which diamond
  557  python metacompare.py -c S1.fa
  558  qrsh
  559  qrsh -l h_data=8G,h_rt=3:00:00 -pe shared 12
  560  qrsh -l h_data=8G,h_rt=6:00:00 -pe shared 12
  561  history
  562  qrsh -l h_rt=3:00:00,h_data=8G pe shared -12
  563  qrsh -l h_rt=3:00:00,h_data=8G -pe shared 12
  564  ls
  565  qrsh -l h_rt=3:00:00,h_data=8G -pe shared 12
  566  qrsh -l h_rt=3:00:00,h_data=8G
  567  $SCRATCH/
  568  ls
  569  cd $SCRATCH/
  570  ls
  571  cd MetaCompare2.0/
  572  ls
  573  module load anaconda3
  574  conda activate MetaCompare
  575  ls
  576  qrsh -l h_rt=3:00:00,h_data=8G -pe shared 12
  577  qrsh -l h_rt=3:00:00,h_data=8G
  578  ls
  579  cd $SCRATCH/
  580  module load anaconda3
  581  conda activate MetaCompare
  582  l
  583  cd MetaCompare2.0/
  584  ls
  585  python metacompare.py -c MI_2F.fa
  586  qrsh -l h_rt=3:00:00,h_data=16G -pe shared 8
  587  cd $SCRATCH
  588  ls
  589  cd MetaCompare2.0/
  590  vim myscript.sh
  591  ls
  592  vi myscript.sh
  593  chmod +x myscript.sh
  594  ./myscript.sh
  595  vim myscript.sh
  596  qsub myscript.sh
  597  myjobs
  598  logout
  599  cd $SCRATCH
  600  ls
  601  cd
  602  ls
  603  cd $SCRATCH
  604  ls
  605  cd MetaCompare2.0/
  606  ls
  607  wget https://usegalaxy.org/api/datasets/f9cad7b01a472135d1fc4642490350c3/display?to_ext=fasta
  608  wget https://usegalaxy.org/api/datasets/f9cad7b01a4721356b4029805aaffdf3/display?to_ext=fasta
  609  wget https://usegalaxy.org/api/datasets/f9cad7b01a47213594bb4226f6148535/display?to_ext=fasta
  610  wget https://usegalaxy.org/api/datasets/f9cad7b01a4721351332bac7b245ef68/display?to_ext=fasta
  611  wget https://usegalaxy.org/api/datasets/f9cad7b01a4721354aa0c32358fa3e95/display?to_ext=fasta
  612  wget https://usegalaxy.org/api/datasets/f9cad7b01a47213503c2db9483a4f4b4/display?to_ext=fasta
  613  wget https://usegalaxy.org/api/datasets/f9cad7b01a472135979920cb475e299d/display?to_ext=fasta
  614  wget https://usegalaxy.org/api/datasets/f9cad7b01a4721351ae8262eb36addd9/display?to_ext=fasta
  615  wget https://usegalaxy.org/api/datasets/f9cad7b01a472135fae713bd1b4a7486/display?to_ext=fasta
  616  vim myscript.sh
  617  ls
  618  cd
  619  $SCRATCH
  620  cd $SCRATCH
  621  ls
  622  cd MetaCompare2.0/
  623  qsub myscript.sh
  624  vim myscript.sh
  625  qsub myscript.sh
  626  vim myscript.sh
  627  qsub myscript.sh
  628  vim myscript.sh
  629  qsub myscript.sh
  630  vim myscript.sh
  631  qsub myscript.sh
  632  my jobs
  633  myjobs
  634  vim myscript.sh
  635  ls
  636  vim myscript.sh
  637  rm myscript.sh.swp
  638  vim myscript.sh
  639  rm .myscript.sh.swp
  640  vim myscript.sh
  641  qsub myscript.sh
  642  myjobs
  643  vim myscript.sh
  644  myjobs
  645  qsub myscript.sh
  646  vim myscript.sh
  647  qsub myscript.sh
  648  myjobs
  649  logout


