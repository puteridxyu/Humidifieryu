# Humidifieryu

Humidifieryu enables wireless control of humidifiers, featuring automatic functions and remote access. Built using Raspberry Pi, MQTT, SQLite, Firebase, and Thingsboard.

[Documentation Link](https://docs.google.com/document/d/1vsX6TnJmZdV1Dld4LS_BJR-UVwAA0PGREqZGUc8Pvko/edit?usp=sharing)

## GUI

<img src="images/readMe/architecture.png" alt="IoT Architecture Design" width="500">

- The architecture design illustrates the IoT setup.

![Main Dashboard](images/readMe/mainDashboard.png)

- The main dashboard displays buildings equipped with our humidifiers.

![Building Dashboard](images/readMe/dashboardBuilding.png)

- This dashboard presents detailed information for selected buildings, including the number of humidifiers and alarm alerts.

![Real-time Updates](images/readMe/dashboardHumidifier2.png)

- Real-time updates feature current humidity, temperature, and humidifier water level, with alarm notifications.

![Alarm Notifications](images/readMe/Alarm.png)

- Alarm notifications alert users to high temperatures via a table interface.

![MQTT Broker Terminal](images/readMe/terminalMQTTBroker.png)

- The exchange of messages in MQTT protocol using QoS1 is depicted.

Explore the detailed functionality of Humidifieryu in the provided documentation.
