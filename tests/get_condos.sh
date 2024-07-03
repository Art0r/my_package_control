# TOKEN

# Make the request and store the response
json_response=$(curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"email":"art@art.com","password":"123"}' \
    http://localhost:8000/api/token/)

# Parse the JSON response and extract tokens using jq
# refresh_token=$(echo "$json_response" | jq -r '.refresh')
access_token=$(echo "$json_response" | jq -r '.access')

curl -X GET \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $access_token" \
    http://localhost:8000/api/condo/