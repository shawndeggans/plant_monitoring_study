import paho.mqtt.client as mqtt
import logging

# Configure logging
logging.basicConfig(filename='logs/log.txt', level=logging.ERROR, 
                    format='%(asctime)s [%(levelname)s]: %(message)s')

class MQTTPublisher:
    """
    Represents an MQTT Publisher for version 3.11.
    
    Attributes:
    - broker (str): The address of the MQTT broker.
    - port (int): The port of the MQTT broker.
    - topic (str): The topic on which messages will be published.
    """
    
    def __init__(self, broker, port, topic):
        """
        Initializes the MQTTPublisher with broker details and topic.
        
        Args:
        - broker (str): The address of the MQTT broker.
        - port (int): The port of the MQTT broker.
        - topic (str): The topic on which messages will be published.
        """
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

        # Set callback functions for successful and unsuccessful connection
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        
    def _on_connect(self, client, userdata, flags, rc):
        """
        Callback for when the client successfully connects to the broker.
        """
        if rc == 0:
            logging.info("Connected successfully to MQTT broker.")
        else:
            logging.error(f"Connection failed with error code: {rc}")
            
    def _on_disconnect(self, client, userdata, rc):
        """
        Callback for when the client disconnects from the broker.
        """
        if rc != 0:
            logging.warning("Unexpected disconnection from MQTT broker.")
        
    def connect(self):
        """
        Connects to the MQTT broker.
        """
        try:
            self.client.connect(self.broker, self.port)
        except Exception as e:
            logging.error(f"Error connecting to MQTT broker: {e}")
            
    def disconnect(self):
        """
        Disconnects from the MQTT broker.
        """
        try:
            self.client.disconnect()
        except Exception as e:
            logging.error(f"Error disconnecting from MQTT broker: {e}")
            
    def publish(self, message):
        """
        Publishes a message to the specified topic.
        
        Args:
        - message (str): The message to be published.
        """
        try:
            result = self.client.publish(self.topic, message)
            
            # Check if the publish was successful
            if result.rc != mqtt.MQTT_ERR_SUCCESS:
                logging.error(f"Failed to send message: {message}")
        except Exception as e:
            logging.error(f"Error publishing message: {e}")

# Usage example:
# publisher = MQTTPublisher(broker="your_broker_address", port=1883, topic="plant/telemetry")
# publisher.connect()
# publisher.publish('{"temperature": 72.5, "humidity": 55}')
# publisher.disconnect()
