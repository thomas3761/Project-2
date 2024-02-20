from panda3d.core import *
from direct.showbase.ShowBase import ShowBase

class Planet(ShowBase):

    def __init__(self, loader: Loader, render: NodePath, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.loader = loader
        self.render = render

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        #planets
        self.planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet1.reparentTo(self.render)
        self.planet1.setPos(150, 5000, 67)
        self.planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet 1.jpg")
        self.planet1.setTexture(tex, 1)

        self.planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet2.reparentTo(self.render)
        self.planet2.setPos(7314, 1274, 976)
        self.planet2.setScale(350)
        tex = loader.loadTexture("./Assets/Planets/planet 2.jpg")  

        self.planet2.setTexture(tex, 1)

        self.planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet3.reparentTo(self.render)
        self.planet3.setPos(11985, 1274, 1112)
        self.planet3.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet 3.png")
        self.planet3.setTexture(tex, 1)

        self.planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet4.reparentTo(self.render)
        self.planet4.setPos(9067, 1274, 2378)
        self.planet4.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet 4.jpg")
        self.planet4.setTexture(tex, 1)

        self.planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet5.reparentTo(self.render)
        self.planet5.setPos(1382, 1274, 4567)
        self.planet5.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planets 5.jpg")
        self.planet5.setTexture(tex, 1)

        self.planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.planet6.reparentTo(self.render)
        self.planet6.setPos(4502, 1274, 6478) 
        self.planet6.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/planet 6.png")
        self.planet6.setTexture(tex, 1)

class Universe:
    def __init__(self, loader, render):
        self.universe = loader.loadModel("./Assets/Universe/Universe.x")
        self.universe.reparentTo(render)
        self.universe.setScale(15000)
        tex = loader.loadTexture("./Assets/Universe/space-galaxy.jpg")
        self.universe.setTexture(tex, 1)

class Spaceship:# / player
    def __init__(self, loader, render):
        self.spaceship = loader.loadModel("./Assets/Khan/Khan.x")
        self.spaceship.reparentTo(render)
        self.spaceship.setPos(-1000, 5000, 80)
        self.spaceship.setScale(10)
        tex = loader.loadTexture("./Assets/Khan/Khan.jpg")
        self.spaceship.setTexture(tex, 1)

class SpaceStation:
    def __init__(self, loader, render):
        self.station = loader.loadModel("./Assets/SpaceStation1B/spaceStation.x")
        self.station.reparentTo(render)
        self.station.setPos(1000, 5000, 80)
        self.station.setScale(50)
        tex = loader.loadTexture("./Assets/SpaceStation1B/SpaceStation1_Dif2.png")
        self.station.setTexture(tex, 1)

        



class DroneShowBase():
    # # of Drone
    droneCount = 0