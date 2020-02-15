#! /bin/bash
rsync -av --progress . _lambda_export --exclude _lambda_export --exclude .git --exclude .idea --exclude __pycache__ --exclude _lambda_export.zip
cd _lambda_export
zip -r -X ../_lambda_export.zip .
