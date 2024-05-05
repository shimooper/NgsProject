import os
import subprocess
from multiprocessing import Pool
import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats

BASE_DIR = '/groups/pupko/yairshimony/CompLabNGS/FinalAssginment/outputs'
srr_accessions = ['SRR25115639', 'SRR25115640', 'SRR25115641', 'SRR25115642', 'SRR25115643', 'SRR25115644', 
                  'SRR25115645', 'SRR25115646', 'SRR25115647']

INPUT_FASTQ_FILES = os.path.join(BASE_DIR, 'input_fastq')
FASTQC_OUTPUTS_DIR = os.path.join(BASE_DIR, 'fastqc_outputs')
TRIMMOMATIC_OUTPUT_DIR = os.path.join(BASE_DIR, 'trimmomatic_outputs')
FASTUNIQ_INPUTS_FILES_DIR = os.path.join(BASE_DIR, 'fastuniq_inputs')
FASTUNIQ_OUTPUT_DIR = os.path.join(BASE_DIR, 'fastuniq_outputs')
CLEAN_READS_FASTQC_OUTPUTS_DIR = os.path.join(BASE_DIR, 'clean_reads_fastqc_outputs')

#generate folders
os.makedirs(INPUT_FASTQ_FILES, exist_ok=True)
os.makedirs(FASTQC_OUTPUTS_DIR, exist_ok=True)
os.makedirs(TRIMMOMATIC_OUTPUT_DIR, exist_ok=True)
os.makedirs(FASTUNIQ_INPUTS_FILES_DIR, exist_ok=True)
os.makedirs(FASTUNIQ_OUTPUT_DIR, exist_ok=True)
os.makedirs(CLEAN_READS_FASTQC_OUTPUTS_DIR, exist_ok=True)

GENE_ABUNDANCES_DIR = os.path.join(BASE_DIR, 'gene_abundances')
PYDESEQ_DIR = os.path.join(BASE_DIR, 'pydeseq')

os.makedirs(GENE_ABUNDANCES_DIR, exist_ok=True)
os.makedirs(PYDESEQ_DIR, exist_ok=True)

all_samples_gene_abundance_filtered_df = pd.read_csv(os.path.join(GENE_ABUNDANCES_DIR, 'all_samples_gene_abundance.csv'), index_col='gene_id')
plot = sns.clustermap(all_samples_gene_abundance_df.corr(), cmap='coolwarm')
plot.savefig(os.path.join(GENE_ABUNDANCES_DIR, 'samples_clustermap.png'))