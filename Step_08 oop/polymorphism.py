# which can do multiple roles
class human:
    total_human=0
    def __init__(self,neuran,metabolism):
        self.brain=neuran
        self.body=metabolism
        human.total_human+=1
    def sync(self):
        return f"{self.brain} interconnected {self.body} work for energy"
working_body=human("NLP","what ever we eat it become part of our body")
class superhuman(human):
    def __init__(self, neuran, metabolism):
        super().__init__(neuran, metabolism)
    
def sync(self):
    return f"it work on nlp but programmed by human"
working_body2=superhuman("work on computer","work on electricity")
print(working_body.total_human)
print(working_body2.sync())#this is polymorphism these both method work smoothly
