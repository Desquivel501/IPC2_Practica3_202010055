class Usuario:
    
    def __init__(self,id, nombre,apellido,telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getTelefono(self):
        return self.telefono
    
    def getId(self):
        return self.id