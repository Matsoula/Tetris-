class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def deplacement(self,b):
        ab1=self.x+b.x
        ord1=self.y+b.y
        return Point(ab1,ord1)
   
class Tetramino:
    def __init__(self,type,position):
        self.type=type
        self.rotation=rotation
        position={[Point(0,0),Point(1,0),Point(2,0),Point(3,0)],
                       [Point(0,0),Point(0,1),Point(1,1),Point(0,1)],
                       [Point(0,0),Point(1,0),Point(0,1),Point(-1,1)],
                       [Point(0,0),Point(0,1),Point(1,0),Point(-1,0)]}
    
    def get_position(self):
        
        position=position[self.type==type]
        if self.rotation==90:
            position=[Point(y,-x) for x,y in position]
        elif self.rotation==180:
            position=[Point(-x,-y) for x,y in position]
        elif self.rotation==270:
            position=[Point(-y,x) for x,y in position]
        return position
    
    def rotation(self):
        self.rotation= self.rotation
        
        return self.rotation
       
    