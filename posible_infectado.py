from Paciente import Paciente

class Posible_Infectado(Paciente):
    def __init__(self, nombre, edad, estado,direccion):
        '''
        Define los parametros como variables.
        Argumentos>
        disparos--(Variable predefinida)
        puntos--(Variable pre definida)
        intentos--(Variable pre definida)
        
        '''
        self.direccion = direccion
        super().__init__(nombre,edad,estado)
       
    def mostrar(self):
        '''
        muestra los atributos del barco
        Retorna>
        self.cantidad--cantidad
        self.nombre--nombre
        self.tamanio--tamanio
        self.habilidad--habilidad

        '''
        return f'''
        Paciente: {self.nombre}.  
        Edad: {self.edad} años.  
        Estado: {self.estado}. 
        Direccion: {self.direccion}.
        
        '''