import os

import dotenv
import meraki
from loguru import logger


# Load environment variables.
dotenv.load_dotenv()
MERAKI_API_KEY = os.getenv("MERAKI_API_KEY")
MERAKI_ORG_ID = os.getenv("MERAKI_ORG_ID")

MERAKI_DASHBOARD = meraki.DashboardAPI(api_key=MERAKI_API_KEY, output_log=False)


def get_org_appliance_uplink_status():
    try:
        response = MERAKI_DASHBOARD.appliance.getOrganizationApplianceUplinkStatuses(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


def get_org_wireless_ssids_statuses_by_device():
    try:
        response = MERAKI_DASHBOARD.wireless.getOrganizationWirelessSsidsStatusesByDevice(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None

    
# This function will give us the availability of ALL devices in the org. This
# is a good function to seed the cache if needed on startup or in case of a
# cache miss. This should be called first and then subsequent calls can be made
# to the "get_org_devices_availabilities_change_history" function to get
# perpetual changes across the org since the last call to this function.
def get_org_devices_availabilities():
    try:
        response = MERAKI_DASHBOARD.organizations.getOrganizationDevicesAvailabilities(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


# Default is over the last 24 hours.
def get_org_devices_availabilities_change_history():
    try:
        response = MERAKI_DASHBOARD.organizations.getOrganizationDevicesAvailabilitiesChangeHistory(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


# Default is hourly interval over the last 7 days.
def get_org_wireless_devices_channel_util_by_device():
    try:
        response = MERAKI_DASHBOARD.wireless.getOrganizationWirelessDevicesChannelUtilizationByDevice(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


def get_org_wireless_devices_ethernet_statuses():
    try:
        response = MERAKI_DASHBOARD.wireless.getOrganizationWirelessDevicesEthernetStatuses(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


# Default is over the last 7 days.
def get_org_wireless_devices_packet_loss_by_device():
    try:
        response = MERAKI_DASHBOARD.wireless.getOrganizationWirelessDevicesPacketLossByDevice(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


# TODO: Find endpoint to get appliance utilization (CPU + network util) or perfScore.
# def get_org_appliance_devices_system_util_by_interval():
#     try:
#         response = MERAKI_DASHBOARD.appliance.getDeviceAppliancePerformance(
#             organizationId=MERAKI_ORG_ID,
#             total_pages='all'
#         )
#         # TODO: Cache this data
#         return response
#     except meraki.APIError as e:
#         logger.error(f"Error fetching data from Meraki Dashboard: {e}")
#         return None


# Defaults to the last 24 hours of data.
def get_org_appliance_uplinks_usage_by_network():
    try:
        response = MERAKI_DASHBOARD.appliance.getOrganizationApplianceUplinksUsageByNetwork(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


# Cache this infrequently as this data doesn't change much. This is a good
# function to call on startup to seed the cache or for cache misses.
def get_org_networks():
    try:
        response = MERAKI_DASHBOARD.organizations.getOrganizationNetworks(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


def get_org_switch_ports_by_switch():
    try:
        response = MERAKI_DASHBOARD.switch.getOrganizationSwitchPortsBySwitch(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


# Might need to look up history that goes as far back as 24 hours. This
# function will only give statuses over the last 5 minutes maximum.
def get_org_devices_uplinks_loss_and_latency():
    try:
        response = MERAKI_DASHBOARD.organizations.getOrganizationDevicesUplinksLossAndLatency(
            organizationId=MERAKI_ORG_ID,
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None


def get_org_devices_uplinks_usage_by_network():
    try:
        response = MERAKI_DASHBOARD.appliance.getOrganizationApplianceUplinksUsageByNetwork(
            organizationId=MERAKI_ORG_ID,
            timespan=3600,  # the last hour
            total_pages='all'
        )
        # TODO: Cache this data
        return response
    except meraki.APIError as e:
        logger.error(f"Error fetching data from Meraki Dashboard: {e}")
        return None
