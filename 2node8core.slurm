#!/bin/bash
#SBATCH --account=COMP90024
#SBATCH --partition=cloud
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=4
#SBATCH --time=0-00:12:00
#SBATCH --job-name=Twitter_job3
#SBATCH -o slurm_job3.out
# Use this email address:
echo "----------- 2-node-8-core -----------"
echo ""
# Load required modules
module load Python/3.4.3-goolf-2015a
# Launch multiple process python code
time mpiexec python test.py bigTwitter.json