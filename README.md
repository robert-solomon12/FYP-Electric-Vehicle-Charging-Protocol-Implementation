# Electric Vehicle Charging Protocol Implementation (Final Year Project)

A Smartcharging Project integrated with a Robotic Car to illustrate a concept of an Electric Vehicle connected to a Grid interface for smart charging. 


The Electric Vehicle Supply Equipment (EVSE) is run in Vector's CANoe Software and simulates a Charging Station connected to the electrical grid. The purpose of the charging station is to communicate with the Raspberry Pi which runs its own process to send a sequence of message requests to the charging station. For each message request that is sent to the Electric Vehicle Supply Equipment or charging station, a message response is sent back to the Raspberry Pi. These messages are known as Combined Charging System messages or CCS for short. These messages are encoded and decoded back to the Raspberry Pi to receive adequate information.


The Robotic Car consists of a Raspberry Pi acting as the main processor of the system. The role of the Pi is to handle both the data being sent and received to and from the EVSE. It is supported by a library project called OpenV2G which is an open source project used by industry experts and developers for implementing the functionalities of the ISO IEC 15118 Specifications. Its purpose for this project is to assist in encoding and decoding the v2g messages transmitted to/from the EVSE Interface in CANoe so it can be understood. The functionalities of the Robotic Car is managed by a software developed in the Raspberry Pi which allows the vehicle actively move around and perform manuevres manually controlled by the user or autonomously via the Ultrasonic Sensors or by Line tracking detection.


# Main Features of the Robotic Car include:

- Manual Control

- Line Tracking

- Obstacle Avoidance
