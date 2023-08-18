"""
IoTDevice Module
----------------

This module provides the foundational class for simulating an IoT device 
used for monitoring plant conditions.

The primary class in this module is `IoTDevice`, which offers methods for:
- Establishing and terminating connections (`connect` and `disconnect` respectively).
- Sending telemetry data to an external endpoint or system (`send_telemetry`).
- Simulating telemetry data generation, which can be extended by device-specific 
subclasses (`simulate_telemetry`).

Example:
    device = IoTDevice(device_id="12345", location="Greenhouse A")
    device.connect()
    device.send_telemetry({"temperature": 72.5, "humidity": 55})

The `IoTDevice` class can be subclassed to create specialized devices 
with specific telemetry simulation logic.

Note:
    This module does not implement the actual logic for sending 
    telemetry data. It's recommended to extend the 
    `send_telemetry` method or integrate with external 
    libraries or systems (e.g., MQTT) for this purpose.
"""
class IoTDevice:
    """
    Represents a base class for an IoT device responsible for monitoring plant conditions.
    
    Attributes:
    - device_id (str): Unique identifier for the device.
    - location (str): Location where the device is placed.
    - telemetry_data (dict): Stores the telemetry data of the device.
    - status (str): Represents the connectivity status of the device. Can be 'online' or 'offline'.
    """
    def __init__(self, device_id, location):
        """
        Initializes the IoTDevice with a device ID and location.
        
        Args:
        - device_id (str): Unique identifier for the device.
        - location (str): Location where the device is placed.
        """
        self.device_id = device_id
        self.location = location
        self.telemetry_data = {}
        self.status = "offline"
    def connect(self):
        """
        Connects the device, changing its status to 'online'.
        """
        self.status = "online"
    def disconnect(self):
        """
        Disconnects the device, changing its status to 'offline'.
        """
        self.status = "offline"
    def send_telemetry(self, data):
        """
        Sends telemetry data from the device, typically to an external server or database.
        
        Args:
        - data (dict): Telemetry data to be sent.
        
        Note: 
        Actual logic to send telemetry data (e.g., via MQTT) should be implemented.
        """
        # Logic to send telemetry data, e.g., via MQTT
        pass
        
    def simulate_telemetry(self):
        """
        Simulates telemetry data for the device. 
        This method can be overridden by subclasses to provide specific simulation logic.
        """
        # Base simulation logic (can be overridden by subclasses)
        pass
