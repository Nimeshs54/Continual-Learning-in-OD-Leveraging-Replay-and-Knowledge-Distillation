#!/bin/bash

# Parse arguments.
MACHINE_NAME=$1
NUM_GPUS=$2
NUM_CPUS=$3
MEM=$4
CONTAINER_SAVE=$5
shift 5
ARGS=$@

# Set working directory to where this was executed from.
WORKDIR=$(pwd)
echo -e "Working directory: $WORKDIR"

# Set the docker container to use as base image
CONTAINER_DEFAULT='/netscratch/enroot/nvcr.io_nvidia_pytorch_23.06-py3.sqsh'
CONTAINER_SAVE='/netscratch/nsingh/yolov5.sqsh'

echo "Base Container: $CONTAINER_DEFAULT"
echo "Building the project container..."
# Run the job.
echo -e "Requesting $NUM_GPUS GPUs and $NUM_CPUS CPUs on $MACHINE_NAME"
srun -K \
-p $MACHINE_NAME \
--ntasks 1 \
--gpus-per-task $NUM_GPUS \
--cpus-per-gpu $NUM_CPUS \
--mem="$MEM" \
--container-image=$CONTAINER_DEFAULT \
--container-save=$CONTAINER_SAVE \
--container-mounts=/home:/home,/netscratch:/netscratch,/ds:/ds \
--container-workdir=$WORKDIR \
--export="NCCL_SOCKET_IFNAME=bond,NCCL_IB_HCA=mlx5" \
--time=24:00:00 \
--pty bash

#echo "Project container built on path: $CONTAINER_SAVE"
