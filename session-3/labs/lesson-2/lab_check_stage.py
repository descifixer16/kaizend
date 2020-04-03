# 2.5 Working with Environment Variables
# export ENVNAME='value'    ==>  creating or setting ENVIRONMENT_VARIABLE
# unset ENVNAME             ==>  unset and ENVIRONMENT_VARIABLE
# echo $STAGE               ==>  printing known ENVIRONMENT_VARIABLE
# printenv                  ==>  printing all available ENVIRONMENT_VARIABLE
# os.getenv                 ==>  error handler to prevent a KeyError if ENVIRONMENT_VARIABLE is not set.

import os           

stage = os.getenv("STAGE", "dev").upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)