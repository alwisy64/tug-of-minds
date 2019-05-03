# tug-of-minds
Mindwave Tug-of-Minds
Repository for the Tug of Minds group made for a project in a Human-Robot Interaction course at Rhodes College.

Contributers:
Claire Payne
Yavin Alwis
Will Robichaux

Code was adapted from this Mindwave bluetooth driver, written by Steve Cruz.
https://github.com/osrf/gsoc-ros-neural

This repository contains the code to set up a bluetooth connection to one Neurosky Mindwave headset to the computer. The data from the headset is published to a topic. The local machine subscribes to the topic and then publishes commands to the Turtlebot.

For the meditation game:
Turtlebot begins moving towards user. If user's meditation value reaches above threshold of 50, Turtlebot will stop.


For the attention game:
Turtlebot will move only if attention value reaches above threshold of 50. 

For both games, once Turtlebot moves a distance of approximately 10 feet, it stops. 

For intial setup and installation of packages, see the link above. 


To run the meditation game:
roslaunch mindwave_teleop meditation_game.launch addr:=:00:00:00:00:00 #here is address of current mindwave headset you are using

To run the attention game:
roslaunch mindwave_teleop attention_game.launch addr:=:00:00:00:00:00 #here is address of current mindwave headset you are using 

