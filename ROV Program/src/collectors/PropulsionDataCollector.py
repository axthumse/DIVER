from ROVMessaging.MessageType import MessageType

from collectors.DataCollector import DataCollector
from subsystems.PropulsionSubsystem import PropulsionSubsystem

#Represents a periodic propulsion data collector that sends the thruster setpoints
class PropulsionDataCollector(DataCollector):
    __subsystem: PropulsionSubsystem = None

    def __init__(self, subsystem: PropulsionSubsystem, messageChannel):
        super().__init__(messageChannel, MessageType.SENSOR_DATA)
        self.__subsystem = subsystem

    #Gets the propulsion data and returns it as a dict
    def getData(self) -> dict:
        speeds = self.__subsystem.getSpeeds()
        dirs = self.__subsystem.getRotDirections()

        return {
            'thruster_speed_top_front': round(speeds[0], 3),
            'thruster_speed_top_back': round(speeds[1], 3),
            'thruster_speed_front_left': round(speeds[2], 3),
            'thruster_speed_back_left': round(speeds[3], 3),
            'thruster_speed_front_right': round(speeds[4], 3),
            'thruster_speed_back_right': round(speeds[5], 3),
            'thruster_direction_top_front': 'CW' if dirs[0].value == 1 else 'CCW',
            'thruster_direction_top_back': 'CW' if dirs[1].value == 1 else 'CCW',
            'thruster_direction_front_left': 'CW' if dirs[2].value == 1 else 'CCW',
            'thruster_direction_back_left': 'CW' if dirs[3].value == 1 else 'CCW',
            'thruster_direction_front_right': 'CW' if dirs[4].value == 1 else 'CCW',
            'thruster_direction_back_right': 'CW' if dirs[5].value == 1 else 'CCW',
        }
