#!/bin/bash
#PBS -S /bin/bash
#PBS -q power-pupko
#PBS -l select=1:ncpus=20:mem=100gb
#PBS -o /groups/pupko/yairshimony/CompLabNGS/FinalAssginment
#PBS -e /groups/pupko/yairshimony/CompLabNGS/FinalAssginment
#PBS -N ngs
#PBS -r y

hostname
echo $PBS_JOBID

source ~/miniconda3/etc/profile.d/conda.sh
conda activate ngs
export PATH=$CONDA_PREFIX/bin:$PATH

cd /groups/pupko/yairshimony/CompLabNGS/FinalAssginment
python test.py