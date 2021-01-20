# SmartChargeV2G-RC (Final Year Project)

A Smartcharging Project integrated with a Robotic Car to illustrate a concept of an Electric Vehicle connected to a Grid interface for smart charging. 



The Electric Vehicle Supply Equipment (EVSE) is run in Vector's CANoe Software and simulates a Charging Station connected to the electrical grid. The purpose of the charging station is to communicate with the Raspberry Pi which runs its own process to send a sequence of message requests to the charging station. For each message request that is sent to the Electric Vehicle Supply Equipment or charging station, a message response is sent back to the Raspberry Pi. These messages are known as Combined Charging System messages or CCS for short. These messages are encoded and decoded back to the Raspberry Pi to receive adequate information.


The Robotic Car consists of a Raspberry Pi acting as the main processor of the system. The role of the Pi is to handle both the data being sent to and received from the EVSE. It runs a C program which helps to encode and decode the messages. The Pi is also responsible for receiving input requests from CANoe over TCP to move around and perform certain functions. 

# Main Features include:

Vehicle Control over TCP:


Line Tracking:


Obstacle Avoidance:
