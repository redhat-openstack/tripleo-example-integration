#!/bin/bash

set -e

if [ $# -ne 2 ];then
   echo "ERROR: Incorrect number of arguments."
   echo "Usage:"
   echo -e " ./generate_example_network_map.sh <openstack-tripleo-heat-templates location> <output location>"
   exit 1
fi

# CUSTOMIZE: short name of the service being configured. Should match file
# names as well
SERVICENAME="example"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TEMPLATES=$1
OUTPUT_DIR=$2
THT_ENDPOINT_DATA=$TEMPLATES/network/endpoints/endpoint_data.yaml
SERVICE_ENDPOINT_DATA="$TEMPLATES/network/$SERVICENAME/${SERVICENAME}_endpoint_data.yaml"
OUTPUT_FILE="$OUTPUT_DIR/${SERVICENAME}_endpoint_data.yaml"

echo "Generate endpoint map from ${THT_ENDPOINT_DATA} and ${SERVICE_ENDPOINT_DATA}"
$TEMPLATES/network/endpoints/build_endpoint_map.py \
    -i <(cat $THT_ENDPOINT_DATA $SERVICE_ENDPOINT_DATA) \
    -o $OUTPUT_FILE
echo "Wrote ${OUTPUT_FILE}"
