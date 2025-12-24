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
        
def main():
    comA = ComponentA()
    comB = ComponentB()
    comC = ComponentC()
    
    # Turn on the machine
    comA.setup()
    comB.start()
    comC.run()
    comA.play()
    comB.checkout()
    comC.initialize()
    
    # Turn off the machine
    comA.cooldown()
    comB.end()
    comC.complete()
    comA.stop()
    comB.slowdown()
    comC.release()
    
if __name__ == "__main__":
    main()