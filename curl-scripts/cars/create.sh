#!/bin/bash

curl "http://localhost:8000/cars" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "car": {
      "name": "'"${NAME}"'",
      "year": "'"${YEAR}"'",
      "mileage": "'"${MILEAGE}"'"
    }
  }'

echo
