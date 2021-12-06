class Paciente:

    
    def __init__(self, nombre, edad, estado):
        '''
        Define los parametros como variables.
        Argumentos>
        disparos--(Variable predefinida)
        puntos--(Variable pre definida)
        intentos--(Variable pre definida)
        
        '''
        
        self.nombre = nombre
        self.edad = edad
        self.estado = estado
        
        
        

    def __str__(self):
        '''
        Retorna los parametros username, nombre,edad y genero
        Argumentos>
        Usuario= Primer argumeto 
        Nombre=Segundo argumento 
        Edad=Tercer argumento
        Genero=Cuarto argumento
        Retorna>
        self.username--username
        self.nombre--nombre
        self.edad--edad
        self.genero--genero

        '''
        return 'Nombre completo: {}\nEdad: {}\n'.format(self.nombre, self.edad)
