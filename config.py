# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present ok
    WORKSPACE_ID = '9b2ae972-bb2c-4933-ad18-30667197dc5d'
    
    # Report Id for which Embed token needs to be generated ok
    REPORT_ID = 'd9d0c828-5bf9-42ec-8ab5-e3a4fa8fc1d9'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode. ok
    TENANT_ID = '7482d38e-f309-4435-aebe-9c94654fda42'
    
    # Client Id (Application Id) of the AAD app ok
    CLIENT_ID = '54b9a6de-be24-48e1-9f5d-86e307c98685'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'EoG8Q~DwjwAn657h4NxiGOkHlavxXcr-MFHOOblf'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
