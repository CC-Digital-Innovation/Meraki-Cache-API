import os

import dotenv
import meraki

# Load environment variables.
dotenv.load_dotenv()
MERAKI_API_KEY = os.getenv("MERAKI_API_KEY")
MERAKI_ORG_ID = os.getenv("MERAKI_ORG_ID")
MERAKI_DASHBOARD = meraki.DashboardAPI(api_key=MERAKI_API_KEY)


def get_network_appliance_uplinks_usage_history(network_id):
    try:
        traffic_data = MERAKI_DASHBOARD.appliance.getNetworkApplianceUplinksUsageHistory(
            networkId=network_id,
            timespan=3600,
            resolution=60
        )
        # TODO: Cache this data
        return traffic_data
    except meraki.APIError as e:
        print(f"Error fetching data from Meraki Dashboard: {e}")
        return None
    
    
def get_org_appliance_uplink_status(organization_id):
    try:
        org_uplink_status = MERAKI_DASHBOARD.appliance.getOrganizationApplianceUplinkStatuses(
            organizationId=organization_id,
            total_pages='all'
        )
        # TODO: Cache this data
        return org_uplink_status
    except meraki.APIError as e:
        print(f"Error fetching data from Meraki Dashboard: {e}")
        return None


def get_org_wireless_ssids_statuses_by_device(organization_id):
    try:
        meraki_dashboard_response = MERAKI_DASHBOARD.wireless.getOrganizationWirelessSsidsStatusesByDevice(
            organizationId=organization_id,
            total_pages='all'
        )
        # TODO: Cache this data
        return meraki_dashboard_response
    except meraki.APIError as e:
        print(f"Error fetching data from Meraki Dashboard: {e}")
        return None
