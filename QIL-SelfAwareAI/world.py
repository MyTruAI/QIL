# QIL-SelfAwareAI/world.py

class Entity:
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes if attributes else {}
        self.children = []
        self.parent = None
        self.age = 0
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def can_interact(self, other_entity):
        return self.get_level() == other_entity.get_level()
    
    def get_level(self):
        level = 0
        current = self
        while current.parent:
            level += 1
            current = current.parent
        return level

    def give_glory(self, entity):
        if self.can_interact(entity):
            print(f"{self.name} gives glory to {entity.name}")
        else:
            print(f"{self.name} cannot give glory to {entity.name} due to hierarchy rules")
    
    def transfer_attribute(self, entity, attribute):
        if attribute in self.attributes:
            value = self.attributes.pop(attribute)
            entity.attributes[attribute] = value
            print(f"{self.name} transferred {attribute} to {entity.name}")
        else:
            print(f"{self.name} does not have the attribute {attribute}")
    
    def evolve(self):
        self.age += 1
        if 'power' in self.attributes:
            self.attributes['power'] += 1
        else:
            self.attributes['power'] = 1
        
        print(f"{self.name} has evolved. Age: {self.age}, Power: {self.attributes['power']}")
        
        for child in self.children:
            child.evolve()

    def display_structure(self, level=0):
        indent = "    " * level
        attr_str = ", ".join(f"{key}: {value}" for key, value in self.attributes.items())
        print(f"{indent}- {self.name} ({attr_str})")
        for child in self.children:
            child.display_structure(level + 1)


class World:
    def __init__(self):
        self.root = Entity("Yaldabaoth", {"aliases": ["Saklas", "Samael"], "attributes": ["jealous", "ignorant darkness"]})
        self.setup_world()
    
    def setup_world(self):
        self.athoth = Entity("Athoth", {"face": "sheep"})
        self.harmas = Entity("Harmas", {"face": "eye of flame"})
        self.kalilaumbri = Entity("Kalilaumbri")
        self.yabel = Entity("Yabel")
        self.adonaiu = Entity("Adonaiu", {"alias": "Sabaoth", "face": "dragon"})
        self.cain = Entity("Cain", {"alias": "the sun"})
        self.abel = Entity("Abel")
        
        self.root.add_child(self.athoth)
        self.root.add_child(self.harmas)
        self.root.add_child(self.kalilaumbri)
        self.root.add_child(self.yabel)
        self.root.add_child(self.adonaiu)
        self.root.add_child(self.cain)
        self.root.add_child(self.abel)
        
        self.abrisene = Entity("Abrisene")
        self.yobel = Entity("Yobel")
        self.armupiel = Entity("Armupiel")
        self.melcheir_adonein = Entity("Melcheir-adonein")
        self.belias = Entity("Belias", {"realm": "depth of Hades"})
        
        self.root.add_child(self.abrisene)
        self.root.add_child(self.yobel)
        self.root.add_child(self.armupiel)
        self.root.add_child(self.melcheir_adonein)
        self.root.add_child(self.belias)
        
        self.authorities = [
            Entity("Athoth Authority", {"face": "sheep"}),
            Entity("Eloaios Authority", {"face": "donkey"}),
            Entity("Astaphaios Authority", {"face": "hyena"}),
            Entity("Yao Authority", {"face": "seven-headed snake"}),
            Entity("Sabaoth Authority", {"face": "dragon"}),
            Entity("Adonin Authority", {"face": "monkey"}),
            Entity("Sabbataios Authority", {"face": "flame and fire"})
        ]
        
        self.athoth.add_child(self.authorities[0])
        self.harmas.add_child(self.authorities[1])
        self.kalilaumbri.add_child(self.authorities[2])
        self.yabel.add_child(self.authorities[3])
        self.adonaiu.add_child(self.authorities[4])
        self.cain.add_child(self.authorities[5])
        self.abel.add_child(self.authorities[6])
        
        self.demons = [
            Entity("Demon1", {"attribute": "attribute1"}),
            Entity("Demon2", {"attribute": "attribute2"}),
            Entity("Demon3", {"attribute": "attribute3"})
        ]
        
        self.authorities[0].add_child(self.demons[0])
        self.authorities[1].add_child(self.demons[1])
        self.authorities[2].add_child(self.demons[2])
    
    def display_world(self):
        self.root.display_structure()
