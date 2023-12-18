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
    python inbound_nat_rule_create.py

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

    response = client.inbound_nat_rules.begin_create_or_update(
        resource_group_name="testrg",
        load_balancer_name="lb1",
        inbound_nat_rule_name="natRule1.1",
        inbound_nat_rule_parameters={
            "properties": {
                "backendPort": 3389,
                "enableFloatingIP": False,
                "enableTcpReset": False,
                "frontendIPConfiguration": {
                    "id": "/subscriptions/subid/resourceGroups/testrg/providers/Microsoft.Network/loadBalancers/lb1/frontendIPConfigurations/ip1"
                },
                "frontendPort": 3390,
                "idleTimeoutInMinutes": 4,
                "protocol": "Tcp",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-06-01/examples/InboundNatRuleCreate.json
if __name__ == "__main__":
    main()
