class human:
      def __init__(self,organ,liquids):
         self.body=organ
         self.vis=liquids
      def full_body(self):
           return f"{self.body} {self.vis}"
my_body=human("liver","water")
print(my_body.full_body()) 
class super_human(human):
     def __init__(self, organ, liquids,nature):
          super().__init__(organ, liquids)

          self.nature=nature
artifisial_human=super_human("gpus","electricity","artifisial")
print(artifisial_human.body)
#it can also access method from parent
print(artifisial_human.vis)