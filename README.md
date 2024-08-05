# Humidifieryu

Humidifieryu enables wireless control of humidifiers, featuring automatic functions and remote access. Built using Raspberry Pi, MQTT, SQLite, Firebase, and Thingsboard.

## GUI

- The architecture design illustrates the IoT setup.

<img src="images/readMe/architecture.png" alt="IoT Architecture Design" width="500">

- The main dashboard displays buildings equipped with our humidifiers.

![Main Dashboard](images/readMe/mainDashboard.png)

- This dashboard presents detailed information for selected buildings, including the number of humidifiers and alarm alerts.

![Building Dashboard](images/readMe/dashboardBuilding.png)

- Real-time updates feature current humidity, temperature, and humidifier water level, with alarm notifications.

![Real-time Updates](images/readMe/dashboardHumidifier2.png)

- Alarm notifications alert users to high temperatures via a table interface.

![Alarm Notifications](images/readMe/Alarm.png)

- The exchange of messages in MQTT protocol using QoS1 is depicted.

![MQTT Broker Terminal](images/readMe/terminalMQTTBroker.png)



