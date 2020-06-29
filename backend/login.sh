#!/bin/sh
if test $# != 2
then
    echo "Execute as '. $0 '[ORION_EMAIL_USERNAME]' '[ORION_EMAIL_PASSWORD]' '"
    return 1
fi

export ORION_EMAIL_USERNAME="$1"
export ORION_EMAIL_PASSWORD="$2"

echo "All environment variables are now setup."