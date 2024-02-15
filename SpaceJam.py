from direct.showbase.ShowBase import ShowBase
import SpaceJamClasses as spaceJamClasses
import DefensePaths as defensePaths
from panda3d.core import *
import math,random  


class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setScene()

        self.planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "planet1", "./Assets/Planets/Planet 1.jpg", Vec3(150, 5000, 67), 350)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "planet2", "./Assets/Planets/planet 2.jpg", Vec3(7314, 1274, 976), 350)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "planet3", "./Assets/Planets/planet 3.png", Vec3(11985, 1274, 1112), 350)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "planet4", "./Assets/Planets/planet 4.jpg", Vec3(9067, 1274, 2378), 350)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "planet5", "./Assets/Planets/planets 5.jpg", Vec3(1382, 1274, 4567), 350)
        self.planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "planet6", "./Assets/Planets/planet 6.png", Vec3(4502, 1274, 6478), 350)

        self.universe = spaceJamClasses.Universe(self.loader, self.render)
        self.spaceship = spaceJamClasses.Spaceship(self.loader, self.render)
        self.space_station = spaceJamClasses.SpaceStation(self.loader, self.render)

        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.planet1, nickName)

    def DrawCloudDefense(self, centralObject, droneName):
        for theta in range(0, 360, 10):
            placeholder = self.render.attachNewNode('placeholder')
            posVec = Vec3(100.0 * math.cos(math.radians(theta)), 50.0 * math.sin(math.radians(theta)), 0.0)
            placeholder.setPos(posVec)
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            placeholder.setColorScale(red, green, blue, 1.0)
            
            # Load the drone model
            drone_model = self.loader.loadModel("Assets/DroneDefender/DroneDefender.obj")
            drone_model.reparentTo(placeholder)
            drone_model.setScale(10)  # Adjust scale as needed


    def DrawBaseballSeams(self, centralObject, droneName, step, nunSeams, radius =1):
        unitVec = defensePaths.BaseballSeams(step, nunSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec* radius * 250 + centralObject.modelNode.getpos()
        spaceJamClasses.Drone(self.loader,"Assets\DroneDefender\DroneDefender.obj", self.render, droneName,"/Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def setScene(self):
        return

app = SpaceJam()
app.run()