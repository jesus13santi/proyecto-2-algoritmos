from Paciente import Paciente

class No_Infectados(Paciente):
    def __init__(self, nombre, edad, estado,numero):
        '''
        Define los parametros como variables.
        Argumentos>
        disparos--(Variable predefinida)
        puntos--(Variable pre definida)
        intentos--(Variable pre definida)
        
        '''
        self.numero = numero
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
        Nombre: {self.nombre}.
        Edad: {self.edad} años.
        Estado: {self.estado}. 
        Numero Telefonico: {self.numero}.
         '''
        
