#!/bin/bash

set -xeuo pipefail
IFS=$'\n\t'

taskDefinitionName=$(aws --region us-east-1 ecs list-task-definitions --family-prefix mm-prd-blackfriday --sort DESC --max-items 1 | jq '.taskDefinitionArns[0]')
containerDefinitions=$(aws --region us-east-1 ecs describe-task-definition --task-definition ${taskDefinitionName//\"/} | jq '.taskDefinition.containerDefinitions' -c)
newTaskDefinitionRevision=$(aws --region us-east-1 ecs register-task-definition --family mm-prd-blackfriday --container-definitions ${containerDefinitions} | jq '.taskDefinition.taskDefinitionArn' -c | awk -F'mm-prd-blackfriday:' '{ print $2 }')
aws --region us-east-1 ecs update-service --service blackfriday --cluster mm-prd-blackfriday --task-definition "mm-prd-blackfriday:${newTaskDefinitionRevision%\"}"
