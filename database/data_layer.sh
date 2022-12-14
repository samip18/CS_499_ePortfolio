#!/bin/bash

gcloud storage buckets create gs://raw_store_buppa_gump
echo "raw layer created"
gcloud storage buckets create gs://silver_store_buppa_gump
echo "silver layer created"
gcloud storage buckets create gs://report_store_buppa_gump
echo "report layer created"
gcloud storage buckets create gs://buppa_jobs_bucket
echo "bucket to hold data proc jobs"