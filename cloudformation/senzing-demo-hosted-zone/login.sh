#!/bin/bash

EMAIL="chiahui@senzing.com"
EMAIL="chiahuitesting@gmail.com"
PASSWORD="7l8Uf0p6xPloiCNf!@2!"

CLIENT_ID="239qrgp08hc7g9f8r23eb6ne64"
POOL_ID="us-east-1_D0dhRENWk"
API_URL="https://hnpmkypdw3.execute-api.us-east-1.amazonaws.com/swagger"

echo "sign up new user"
aws cognito-idp sign-up \
  --client-id ${CLIENT_ID} \
  --username ${EMAIL} \
  --password ${PASSWORD}

echo "reset password to confirm user"
aws cognito-idp admin-set-user-password \
  --user-pool-id ${POOL_ID} \
  --username ${EMAIL} \
  --password ${PASSWORD} \
  --permanent

echo "Get Token"
TOKEN=$(aws cognito-idp initiate-auth \
    --client-id ${CLIENT_ID} \
    --auth-flow USER_PASSWORD_AUTH \
    --auth-parameters USERNAME=${EMAIL},PASSWORD=${PASSWORD} \
    --query 'AuthenticationResult.AccessToken' \
    --output text)

echo "Get swagger home page"
curl -v -H "Authorization: Bearer $TOKEN" $API_URL