# Things you can run with this script:
# Without a robot:
# 1. Waypoint Navigation
# 2. Test learning and recognition
# 3. Recognise location and do waypoint navigation

from navigation import *
from recognition import *

##########################
run_option = 5           #
use_robot = True        #
##########################

if use_robot:
  import robot as r
  robot = r.Robot()
else:
  robot = None

# 1. Waypoint Navigation
######################################################
if run_option == 1:
  initial_waypoint = 0
  noParticles = 100
  # Create navigation class
  test = WaypointNavigation(waypoints_cw3,initial_waypoint,noParticles,180, robot)
  # Do the navigation
  test.navigate()

# 2. Test learning and recognition
######################################################
if run_option == 2:
  test = Recognition(waypoints_cw4,walls,360,robot)
  # Learn all the waypoints
  test.sim_learn()
  # Try to recognise all the waypoints
  test.sim_testRecognition(111.5)

if run_option == 4:
  test = Recognition(waypoints_cw4,walls,360,robot)
  # Learn a waypoints
  test.learn_location()

if run_option == 5:
  test = Recognition(waypoints_cw4,walls,360,robot)
  print test.recognize_location()

# 3. Combine the last two
######################################################
if run_option == 3:

  # Use this function to reshuffle the waypoints depending on where you find yourself
  def shift(seq, n):
      n = n % len(seq)
      return seq[n:] + seq[:n]

  # The angle at which the robot is started
  start_angle = 50
  # The waypoint index at which the robot starts at
  waypoint_idx = 0
  x,y = waypoints_cw4[waypoint_idx]
  # Create a recognition class
  rec = Recognition(waypoints_cw4,walls,20, robot)
  # Try and recognise the waypoint
  result = rec.sim_recognise(x,y,start_angle)
  print 'Expected ', (waypoint_idx,(start_angle,start_angle)), ' got ', result

  # Shift the waypoints to account for the starting position
  waypoints = shift(waypoints_cw4,result[0]+1)
  print result[0], waypoints
  # Number of particles for mcl
  noParticles = 100
  # Create a navigation class
  nav = WaypointNavigation(waypoints,result[0]-1,noParticles, robot)
  # since we can only estimate an angular range, set up the particles
  # in this range
  nav.init_angular_uncertainity(result[1])
  # Navigate
  nav.navigate()
