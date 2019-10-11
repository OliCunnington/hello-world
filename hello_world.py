class HelloWorld:

  def say_hello(self):
    return "Hello " + self.name + "!\n"
    
  def __init__(self, name = "world"):
    self.name = name
    
    
if __name__ == "__main__":
  howdy = HelloWorld()
  print(howdy.say_hello)
