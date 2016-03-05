# Things you can run with this script:
# Without a robot:
# 1. Waypoint Navigation
# 2. Test learning and recognition
# 3. Recognise location and do waypoint navigation

from canvas import *
from recognition import *

##########################
run_option = 2           #
use_robot = False        #
##########################

if use_robot:
  import robot

# 1. Waypoint Navigation
######################################################
if run_option == 1:
  initial_waypoint = 0
  noParticles = 100
  # Create navigation class
  test = WaypointNavigation(use_robot,waypoints_cw3,initial_waypoint,noParticles,180)
  # Do the navigation
  test.navigate()
   
# 2. Test learning and recognition
######################################################
if run_option == 2:
  test = Recognition(False,waypoints_cw4,60)
  # Learn all the waypoints
  test.sim_learn()
  # Try to recognise all the waypoints
  test.sim_testRecognition(111.5)

# 3. Combine the last two
######################################################  
if run_option == 3:

  # Use this function to reshuffle the waypoints depending on where you find yourself
  def shift(seq, n):
      n = n % len(seq)
      return seq[n:] + seq[:n]

  # The angle at which the robot is started
  start_angle = 100
  # The waypoint index at which the robot starts at
  waypoint_idx = 3
  x,y = waypoints_cw3[waypoint_idx]
  # Create a recognition class
  rec = Recognition(False,waypoints_cw4,200)
  # Try and recognise the waypoint
  result = rec.sim_recognise(x,y,start_angle)
  print 'Expected ', (waypoint_idx,start_angle), ' angle is between ', result
  
  # Shift the waypoints to account for the starting position
  waypoints = shift(waypoints_cw4,result[0]+1)
  # Number of particles for mcl
  noParticles = 100
  # Create a navigation class
  nav = WaypointNavigation(use_robot,waypoints,result[0],noParticles)
  # Navigate
  nav.navigate()
