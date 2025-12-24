class ComponentA:
    def play(self):
        print("ComponentA play")
        
    def setup(self):
        print("ComponentA setup")
    
    def stop(self):
        print("ComponentA stop")
    
    def cooldown(self):
        print("ComponentA cooldown")
    
class ComponentB:
    def start(self):
        print("ComponentB start")
        
    def checkout(self):
        print("ComponentB print")
    
    def end(self):
        print("ComponentB end")
    
    def slowdown(self):
        print("ComponentB slowdown")
        
class ComponentC:
    def run(self):
        print("ComponentC run")
        
    def initialize(self):
        print("ComponentC initialize")
    
    def complete(self):
        print("ComponentC complete")
    
    def release(self):
        print("ComponentC release")
        
class ControlFacade:
    def __init__(self, comA, comB, comC):
        self.comA = comA
        self.comB = comB
        self.comC = comC
        
    def turnOn(self):
        self.comA.setup()
        self.comB.start()
        self.comC.run()
        self.comA.play()
        self.comB.checkout()
        self.comC.initialize()
        
    def turnOff(self):
        self.comA.cooldown()
        self.comB.end()
        self.comC.complete()
        self.comA.stop()
        self.comB.slowdown()
        self.comC.release()
        
def main():
    comA = ComponentA()
    comB = ComponentB()
    comC = ComponentC()
    
    control = ControlFacade(comA, comB, comC)
    control.turnOn()
    control.turnOff()
    
if __name__ == "__main__":
    main()