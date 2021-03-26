#!/bin/bash

EMAIL=""
PASSWORD=""

CLIENT_ID=""
POOL_ID=""
API_URL=""

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

echo "Send Get request to api url"
curl -v -H "Authorization: Bearer $TOKEN" $API_URL