#!/bin/bash

echo "CREATING DATA PROC CLUSTER"

gcloud dataproc clusters create buppa-snhu-cluster \
--enable-component-gateway \
--bucket dataproc-utility \
--region us-central1 \
--zone us-central1-c \
--master-machine-type n1-standard-4 \
--master-boot-disk-size 100 \
--num-workers 2 \
--worker-machine-type n1-standard-4 \
--worker-boot-disk-size 100 \
--image-version 1.5.77-ubuntu18 \
--optional-components ANACONDA,JUPYTER \
--project buppa-gump-snhu

echo "CLUSTER CREATED SUCCESSFULLY WITH JUPYTER ENABLED"