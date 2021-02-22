#!/bin/bash

curl "http://localhost:8000/cars/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
