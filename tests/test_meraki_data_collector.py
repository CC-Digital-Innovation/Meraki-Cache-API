from src.meraki_data_collector import *


# TODO: Find a way to mock the Meraki dashboard for testing purposes, so we
# don't rely on an actual Meraki dashboard during tests.


def test_get_org_appliance_uplink_status():
    response = get_org_appliance_uplink_status()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_wireless_ssids_statuses_by_device():
    response = get_org_wireless_ssids_statuses_by_device()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_devices_availabilities():
    response = get_org_devices_availabilities()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_devices_availabilities_change_history():
    response = get_org_devices_availabilities_change_history()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_wireless_devices_channel_util_by_device():
    response = get_org_wireless_devices_channel_util_by_device()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_wireless_devices_ethernet_statuses():
    response = get_org_wireless_devices_ethernet_statuses()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_wireless_devices_packet_loss_by_device():
    response = get_org_wireless_devices_packet_loss_by_device()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_devices_uplinks_loss_and_latency():
    response = get_org_devices_uplinks_loss_and_latency()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_appliance_uplinks_usage_by_network():
    response = get_org_appliance_uplinks_usage_by_network()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_networks():
    response = get_org_networks()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_switch_ports_by_switch():
    response = get_org_switch_ports_by_switch()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0

def test_get_org_devices_uplinks_usage_by_network():
    response = get_org_devices_uplinks_usage_by_network()
    assert response is not None
    assert isinstance(response, list)
    assert len(response) > 0
