#!/usr/bin/python3
#
# SAMPLE SCRIPT ONLY
# THIS IS NOT SUPPORTED BY TENABLE.
# THIS IS NOT SUPPORTED BY ANYONE.
#
# This shows how to take an SSH private key and upload it to Tenable.io and create a new credential entry from it.
# It assumes the private key is in a file named "private_rsa_key" in the current working directory.
#
# Requires the following:
#   pip install pytenable
#

import os
import json
from tenable.io import TenableIO
access_key=os.getenv('TIO_ACCESS_KEY')
secret_key=os.getenv('TIO_SECRET_KEY')
tio = TenableIO(access_key, secret_key)
respraw = tio.post('credentials/files', files={'Filedata': open('private_rsa_key', 'rb')})
resp=json.loads(respraw.text)
print("Response:",respraw.text)
if "fileuploaded" in resp:
    cred_uuid = tio.credentials.create("Test creds with private key auth", "SSH", auth_method="public key", elevate_privileges_with="Nothing", username="root",private_key=resp["fileuploaded"])

print("Credential UUID:",cred_uuid)

