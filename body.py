from infectados import Infectados
from no_infectados import No_Infectados
from infectados import Infectados
from posible_infectado import Posible_Infectado
from Paciente import Paciente

def registrar():
    '''Funcion para ingresar un nuevo usuario'''
    contador=0
    validez=True
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numeros= ['1','2','3','4','5','6','7','8','9','0','']
    validez2=False
    contador_estado=0
    estado=''
        
    while validez==True:
        contador=0
        nombre=input('Nombre Completo: ')
        for i in nombre:
            if i in numeros:
                contador+=1
        if contador>=1:
            print('No ingrese numeros. Ingrese solo letras.\nVuelve a intentarlo')
            print('-'*19)
        else:
            '''Coloca la primera letra de cada nombre o apellido en un mayuscula'''
            nombre=nombre.title()
            validez=False
            
    print(nombre)
    
    
    print('-'*19)
    while True:
        '''Valida que la edad este ente 5 y 100 años, y que sea solo caracter numerico'''
        try:
            edad=int(input('Edad: '))
            while edad<0 or edad>=100 :
                print ('Edad incorrecta. \nverifique que este ingresando una edad valida.')
                print('-'*19)
                edad=int(input('Edad: '))
            break
        except ValueError:
            print('Edad Incorrecta.\nPor favor ingrese un numero')
            print('-'*19)
    print('---CUESTIONARIO CODVID19---')
    print('Responda No(N) o Si(S) segun sea el caso.\n')
    while True:
        contador_estado=0
        while True:
            '''Valida que solo ingrese s o n'''
            estados=input('''
            ¿Tiene secreciones nasales?
            ''')
            
            if estados.lower()=='n':
                contador_estado+=0
                estados_1='NO'
                break
            elif estados.lower() =='s':
                contador_estado+=1
                estados_1='SI'
                break
            else:
                if estados.lower()=='':
                    '''Valida que no haga enter sin escribir nada'''
                    print('No deje espacio en blanco')
                else:
                    print('Ingrese una letra valida (s o n)')
                    print('-'*19)
        while True:
            '''Valida que solo ingrese s o n'''
            estados=input('''
            ¿Tiene dolor de garganta?
            ''')
            
            if estados.lower()=='n':
                contador_estado+=0
                estados_2='NO'
                break
            elif estados.lower() =='s':
                contador_estado+=1
                estados_2='SI'
                break
            else:
                if estados.lower()=='':
                    '''Valida que no haga enter sin escribir nada'''
                    print('No deje espacio en blanco')
                else:
                    print('Ingrese una letra valida (s(Si) o n(NO)')
                    print('-'*19)
        while True:
            '''Valida que solo ingrese s o n'''
            estados=input('''
            ¿Tiene tos?
            ''')
            
            if estados.lower()=='n':
                contador_estado+=0
                estados_3='NO'
                break
            elif estados.lower() =='s':
                contador_estado+=1
                estados_3='SI'
                break
            else:
                if estados.lower()=='':
                    '''Valida que no haga enter sin escribir nada'''
                    print('No deje espacio en blanco')
                else:
                    print('Ingrese una letra valida (s o n)')
                    print('-'*19)
        while True:
            '''Valida que solo ingrese s o n'''
            estados=input('''
            ¿Tienes fiebre?
            ''')
            
            if estados.lower()=='n':
                contador_estado+=0
                estados_4='NO'
                break
            elif estados.lower() =='s':
                contador_estado+=1
                estados_4='SI'
                break
            else:
                if estados.lower()=='':
                    '''Valida que no haga enter sin escribir nada'''
                    print('No deje espacio en blanco')
                else:
                    print('Ingrese una letra valida (s o n)')
                    print('-'*19)
        while True:
            estados=input('''
            ¿dificultad para respirar?
            ''')
            
            if estados.lower()=='n':
                contador_estado+=0
                estados_5='NO'
                break
            elif estados.lower() =='s':
                contador_estado+=1
                estados_5='SI'
                break
            else:
                if estados.lower()=='':
                    '''Valida que no haga enter sin escribir nada'''
                    print('No deje espacio en blanco')
                else:
                    print('Ingrese una letra valida (s o n)')
                    print('-'*19)
        if contador_estado==0:
            print('Usted no esta infectado!')
            while True:
                '''Valida que la edad este ente 5 y 100 años, y que sea solo caracter numerico'''
                try:
                    
                    while True:
                        numero=int(input('Numero telefonico: '))
                        verificacion=str(numero)
                        if (verificacion[0]!='4' and verificacion[1]!='2' and verificacion[2]!='4') or (verificacion[0]!='4' and verificacion[1]!='1' and verificacion[0]!='4') or (verificacion[0]!='4' and verificacion[1]!='1' and verificacion[2]!='6') or (verificacion[0]!='4' and verificacion[1]!='2' and verificacion[2]!='6') or (verificacion[0]!='4' and verificacion[1]!='1' and verificacion[2]!='2'):
                            print('Codigo de Area incorrecto, Debe ingresar un numero telefonico valido como:\n0424, 0414, 0416, 0426 o 0412')
                            print('-'*19)
                            
                        elif len(verificacion)<10 or len(verificacion)>12:
                            print('Numero telefonico incorrecto. \nverifique que este ingresando una numero telefonico valido. Debe tener de 11 a 12 caracteres.')
                            print('-'*19)
                        else:   
                            break
                        
                    
                    
                    
                    
                    break
                except ValueError:
                    print('Numero Telefonico Incorrecta.\nPor favor ingrese solo numeros')
                    print('-'*19)
            estado='No Infectado'
            paciente = No_Infectados(nombre, edad,estado,numero)
            '''Agrega el usuario insertado en la Base de Datos'''
            with open("BaseDeDatos.txt", "a+") as bd: 
                bd.write("{},{},{},{}\n".format(nombre, edad, estado,numero))
                print('\tUsuario: ', paciente.nombre, ' registrado correctamente')
            
            
        elif contador_estado<=2:
            print('Debe revisarse con un medico')
            while True:
                '''Valida que la edad este ente 5 y 100 años, y que sea solo caracter numerico'''
                try:
                    while True:
                        numero=int(input('Numero telefonico: '))
                        verificacion=str(numero)
                        if (verificacion[0]!='4' and verificacion[1]!='2' and verificacion[2]!='4') or (verificacion[0]!='4' and verificacion[1]!='1' and verificacion[0]!='4') or (verificacion[0]!='4' and verificacion[1]!='1' and verificacion[2]!='6') or (verificacion[0]!='4' and verificacion[1]!='2' and verificacion[2]!='6') or (verificacion[0]!='4' and verificacion[1]!='1' and verificacion[2]!='2'):
                            print('Codigo de Area incorrecto, Debe ingresar un numero telefonico valido como:\n0424, 0414, 0416, 0426 o 0412')
                            print('-'*19)
                        elif len(verificacion)<10 or len(verificacion)>12:
                            print('Numero telefonico incorrecto. \nverifique que este ingresando una numero telefonico valido. Debe tener de 11 a 12 caracteres.')
                            print('-'*19)
                        else:   
                            break

                    break
                except ValueError:
                    print('Edad Incorrecta.\nPor favor ingrese un numero')
                    print('-'*19)
            estado='En Revision'
            paciente = No_Infectados(nombre, edad,estado,numero)
            '''Agrega el usuario insertado en la Base de Datos'''
            with open("BaseDeDatos.txt", "a+") as bd: 
                bd.write("{},{},{},{}\n".format(nombre, edad, estado,numero))
                print('\tUsuario: ', paciente.nombre, ' registrado correctamente')
            
        elif contador_estado<=4:
            print('Usted puede ser un posible infectado')
            print('----Direccion----')
            calle=input('Calle o Avenida: ')
            municipio=input('Municipio: ')
            ciudad=input('Ciudad: ')
            estado_direccion=input('Estado: ')
            estado='Posible Infectado'
            direccion=f'Calle: {calle}, Municipio: {municipio}, Ciudad: {ciudad}, Estado: {estado_direccion}'
            paciente = Posible_Infectado(nombre, edad,estado,direccion)
            '''Agrega el usuario insertado en la Base de Datos'''
            with open("BaseDeDatos.txt", "a+") as bd: 
                bd.write("{},{},{},{}\n".format(nombre, edad, estado,direccion))
                print('\tUsuario: ', paciente.nombre, ' registrado correctamente')
            
        elif contador_estado>4:
            print('Usted esta infectado')
            print('----Direccion----')
            calle=input('Calle o Avenida: ')
            municipio=input('Municipio: ')
            ciudad=input('Ciudad:')
            estado_direccion=input('Estado: ')
            direccion=f'Calle: {calle}, Municipio: {municipio}, Ciudad: {ciudad}, Estado: {estado_direccion}'
            
            validez2=True
            while validez2==True:
                contador=0
                doctor=input('Doctor: ')
                for i in doctor:
                    if i in numeros:
                        contador+=1
                if contador>=1:
                    print('No ingrese numeros. Ingrese solo letras.\nVuelve a intentarlo')
                    print('-'*19)
                else:
                    '''Coloca la primera letra de cada nombre o apellido en un mayuscula'''
                    nombre=nombre.title()
                    validez2=False
                print(doctor)
            
                estado='Infectado'
            paciente = Infectados(nombre, edad,estado,direccion,doctor)
            '''Agrega el usuario insertado en la Base de Datos'''
            with open("BaseDeDatos.txt", "a+") as bd: 
                bd.write("{},{},{},{},{}\n".format(nombre, edad, estado,direccion,doctor))
                print('\tUsuario: ', paciente.nombre, ' registrado correctamente')
        print(f'''
----Sus respuestas fueron las siguientes----

        1-¿Tiene secreciones nasales?
        -{estados_1}
        2-¿Tiene dolor de garganta?
        -{estados_2}
        3-¿Tiene tos?
        -{estados_3}
        4-¿Tienes fiebre?
        -{estados_4}
        5-¿dificultad para respirar?
        -{estados_5}
''')
        print(paciente.mostrar())
        break
            


                    
                           

def main():
    while True:
        while True:
            
            print('''
            Bienvenido la clinica UNIMET. (Tracker sobre el CODVI-19.)
            Consiste en un cuestionario donde, te haremos algunas preguntas para
            detectar si tienes sintomas de este virus.
            Nota: Las respuestas de este programa no da una respuesta certera al COVID-19
            si siente cualquier síntoma debe visitar a un médico.
            ''')
            registrar()

            print('''
            Recuerda: Las respuestas de este programa no da una respuesta certera al COVID-19
            si siente cualquier síntoma debe visitar a un médico.
            ''')
            break
        validez3=True
        contador=0
        while validez3==True:
            volver_menu=input('''
    ¡Que desea hacer?
    1-Verificar otro paciente.
    2-Salir del sistema.
        ''')
        

    

            if volver_menu.lower()=='1':
                    contador=0
                    validez3=False
        
        
            elif volver_menu.lower()=='2':
                contador+=1
                validez3=False
            else:
                print('\nOPCION INCORRECTA')

        if contador==0:
            continue
        elif contador>=1:
            break
            
                
main()

   
   

