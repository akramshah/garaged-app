#!/bin/bash

curl "http://localhost:8000/cars/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
