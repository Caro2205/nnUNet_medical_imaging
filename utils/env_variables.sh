#!/bin/bash

current_dir=$(pwd)

{
  echo "export nnUNet_raw=\"$current_dir/nnunetv2/data/nnUNet_raw\""
  echo "export nnUNet_preprocessed=\"$current_dir/nnunetv2/data/nnUNet_preprocessed\""
  echo "export nnUNet_results=\"$current_dir/nnunetv2/data/nnUNet_results\""
} >> ~/.bashrc

source home/.bashrc
