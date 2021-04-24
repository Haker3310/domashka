import  math


class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def lenth(self, obj):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z )
    def scal_proizv(self, obj):
        return self.x * obj.x+self.y * obj.y+self.z * obj.z
    def vec_proizv(self,obj):
        return self.x*obj.z-self.z*obj.y*self.z*obj.x-self.x*obj.z*self.x*obj.y-self.y*obj.x
    def cor_ygla(self,obj):
        return self.x * obj.x + self.y * obj.y + self.z * obj.z / (math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z) * math.sqrt(obj.z * obj.z + obj.y * obj.y + obj.z * obj.z))
    def summ(self, obj):
        return self.x + obj.x, self.y + obj.y, self.z + obj.z
    def razn(self, obj):
        return self.x + obj.x, self.y + obj.y, self.z + obj.z

v = Vector