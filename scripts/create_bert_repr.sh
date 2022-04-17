#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=04:00:00
#SBATCH --partition=sgpu
#SBATCH --mail-type=ALL
#SBATCH --mail-user=dasr8731@colorado.edu
#SBATCH --output=bert-repr-job.%j.out


module purge
module load anaconda
module load cuda
module load cudnn

nvidia-smi

export TRANSFORMERS_CACHE=/projects/dasr8731/transformers-cache/

cd /scratch/summit/dasr8731/disco-fever

source activate ./venv/

python -m src.create_bert_repr
