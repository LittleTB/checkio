class state:
    def heat(self,con):
        pass
    def cool(self,con):
        pass

class water(state):
    def heat(self,con):
        con.changeState(vapour())
    def cool(self,con):
        con.changeState(ice())

class ice(state):
    def heat(self,con):
        con.changeState(water())

class vapour(state):
    def cool(self,con):
        con.changeState(water())
#Context
class Context:
    def __init__(self,state):
        self.state=state
    def heat(self):
        self.state.heat(self)#与Strategy最大的区别
    def cool(self):
        self.state.cool(self)#与Strategy最大的区别
    def changeState(self,state):
        self.state=state
#client
if __name__=="__main__":
    Ice=ice()
    context=Context(Ice)
    for i in range(0, 3):
        print(context.state)
        context.heat()
    for i in range(0,3):
        print(context.state)
        context.cool()

