#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=04:00:00
#SBATCH --partition=sgpu
#SBATCH --mail-type=ALL
#SBATCH --mail-user=dasr8731@colorado.edu


module purge
module load anaconda
module load cuda
module load cudnn


nvidia-smi

cd /scratch/summit/dasr8731/disco-fever

source activate ./venv/

python -m src.create_bert_repr
