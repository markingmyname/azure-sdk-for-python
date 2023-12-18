# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python load_balancers_swap_public_ip_addresses.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    client.load_balancers.begin_swap_public_ip_addresses(
        location="westus",
        parameters={
            "frontendIPConfigurations": [
                {
                    "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb1/frontendIPConfigurations/lbfe1",
                    "properties": {
                        "publicIPAddress": {
                            "id": "/subscriptions/subid/resourceGroups/rg2/providers/Microsoft.Network/publicIPAddresses/pip2"
                        }
                    },
                },
                {
                    "id": "/subscriptions/subid/resourceGroups/rg2/providers/Microsoft.Network/loadBalancers/lb2/frontendIPConfigurations/lbfe2",
                    "properties": {
                        "publicIPAddress": {
                            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/pip1"
                        }
                    },
                },
            ]
        },
    ).result()


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-06-01/examples/LoadBalancersSwapPublicIpAddresses.json
if __name__ == "__main__":
    main()
