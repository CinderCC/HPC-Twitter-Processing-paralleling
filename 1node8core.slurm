#!/bin/bash
#SBATCH --account=COMP90024
#SBATCH --partition=cloud
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=0-00:12:00
#SBATCH --job-name=Twitter_job2
#SBATCH -o slurm_job2.out
# Use this email address:
echo "----------- 1-node-8-core -----------"
echo ""
# Load required modules
module load Python/3.4.3-goolf-2015a
# Launch multiple process python code
time mpiexec python test.py bigTwitter.json