import  Math


class Vector():
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def lenth():
		Math.sqrt(x*x+y*y+z*z)

    def scal_proizv(self, obj):
    	return Vector(
    		self.x * obj.x,
    		self.y * obj.y,
    		self.z * obj.z,
    		)
    def vec_proizv(self,obj):
    	return Vector(self.x*obj.z-self.z*obj.y*self.z*obj.x-self.x*obj.z*self.x*obj.y-self.y*obj.x)
 

v = Vector