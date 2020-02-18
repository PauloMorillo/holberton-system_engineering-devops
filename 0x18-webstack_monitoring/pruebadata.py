#!/usr/bin/python3
from datadog import initialize, api

options = {
    'api_key': '220bcb2c30ad459a282f8f2a1250167b',
    'app_key': '961d999019505258b37d6008c4306f098286f2d1'
}

initialize(**options)

print(api.Dashboard.get_all())
