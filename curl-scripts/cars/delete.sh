#!/bin/bash

curl "http://localhost:8000/cars/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
