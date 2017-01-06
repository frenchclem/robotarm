from org.myrobotlab.kinematics import DHRobotArm
from org.myrobotlab.kinematics import DHLink
from org.myrobotlab.kinematics import DHLinkType

#start ik service
ik= Runtime.createAndStart("ik3d", "InverseKinematics3D")

#arduino service
arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("COM3")

#define and attach servo
#map is set so servo accept angle as input, output where
#they need to go so that their part they where attach to
#move by the input degree
base = Runtime.createAndStart("base","Servo")
base.attach(arduino,10,90);
base.map(180,0,0,171);
base.setVelocity(99)
base.moveTo(0)

join1 = Runtime.createAndStart("join1 ","Servo")
join1.attach(arduino,9,90);
join1.map(-122,-33.6,25,125);
join1.setVelocity(99)
join1.moveTo(-90)

join2 = Runtime.createAndStart("join2 ","Servo")
join2.attach(arduino,8,90);
join2.map(155,74,40,135);
join2.setVelocity(99)
join2.moveTo(155)

ik.setNewDHRobotArm()

# Lets create a 3 link robot arm
# Create the first link in the arm specified by 100,100,0,90
# additionally specify a name for the link which can be used elsewhere. 
d1 = 52.7
r1 = 0
theta1 = 0
alpha1 = -90
link0 = DHLink("base", d1, r1, theta1, alpha1)

# Create the second link (same as the first link.)
d2 = 0
r2 = 135
theta2 = 0
alpha2 = 0
link1 = DHLink("link1", d2, r2, theta2, alpha2)

# Create the third link (same as the first link.)
d3 = 0
r3 = 147
theta3 = 0
alpha3 = 0
link2 = DHLink("link2", d3, r3, theta3, alpha3)

ik.setDHLink(base,d1,theta1,r1,alpha1)
ik.setDHLink(join1,d2,theta2,r2,alpha2)
ik.setDHLink(join2,d3,theta3,r3,alpha3)

ik.clearObject()
ik.addObject(0.0, 0.0, 0.0, 0.0, 0.0, 0.0,"base", 1.0)
ik.addObject("join1", 1.0)
ik.addObject("join2", 1.0)

print ik.currentPosition();
