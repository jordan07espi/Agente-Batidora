#Glosario: Bol, es un recipiente semiesférico en forma de taza grande sin asas.

#INSTRUCCIONES
#Defina donde se encuentra: Bol1/Bol2/Bol3
#Defina el estado O/1 según corresponda, donde 0 significa Batido y 1 significa Sin Batir

def batidora():
    #Incializamos la batidora
    #El objetivo al que se quiere llevar el bol
    estado_objetivo = {'Bol1': '0', 'Bol2': '0', 'Bol3': '0'}
    cost=0
    
    bol = input("Defina la ubicación de la batidora: ")#Se debe ingresar: Bol1, Bol2 o Bol3
    estado = input("Defina el estado de " +bol+": ")#Se debe confirmar en que estado se encuentra el Bol, puede ser 0/1
    
    if bol== 'Bol1':
        #Se debe confirmar en que estado se encuentra el otro Bol, puede ser 0/1
        segundo_estado = input("Defina otro estado del Bol2: ")
        #Se debe confirmar en que estado se encuentra el otro Bol, puede ser 0/1
        tercer_estado = input("Defina otro estado del Bol3: ")
        print("Meta deseada: "+str(estado_objetivo))
        
        #La locación de Bol es: Bol1
        print("La batidora esta en el Bol 1: ")
        if estado == '1': #Se define que Bol1 esta sin batir
            print("El Bol esta sin batir. ")
            estado_objetivo['Bol1']='0' #Su estado cambia, ahora ya esta Batido
            cost+=1#Incrementa el costo de batir a la batidora
            print("Lugar de batida: Bol1")
            print("Costol Actual: "+str(cost))
            
            #Se define que el Bol2 esta sin batir
            if segundo_estado=='1':
                print("El Bol2 esta sin batir.")
                print("Se traslada al Bol2")
                cost+= 1#Incrementa el costo
                print("Costo Actual: "+str(cost))
                
                estado_objetivo['Bol2'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol2")
                print("Costo Actual: "+str(cost))   
            else:
                #El Bol2 se encuentra batido, no realizada ninguna accion y su costo es el mismo
                print("El Bol2 esta batido.")
                print("sin accion. Costo actual "+ str(cost))
                
            #Se define que el Bol3 esta sin batir       
            if tercer_estado=='1':
                print("El Bol3 esta sin batir.")
                print("Se traslada al Bol3")
                cost+=1#Incrementa el costo
                print("Costo Actual: "+str(cost))
                    
                estado_objetivo['Bol3'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol3")
                print("Costo Actual: "+str(cost))       
            else:
                #El Bol3 se encuentra batido, no realizada ninguna accion y su costo es el mismo 
                print("El bol3 esta batido.")
                print("sin accion. Costo actual "+str(cost))      
        
        #Se define que el Bol1 esta batido  
        if estado =='0':
            print("El Bol1 esta batido y no realiza ninguna acción.")
            
            #Se define que el Bol2 esta sin batir
            if segundo_estado=='1':
                print("El Bol2 esta sin batir.")
                print("Se traslada al Bol2")
                cost+=1#Incrementa el costo
                print("Costo Actual: "+str(cost))
                
                estado_objetivo['Bol2'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol2")
                print("Costo Actual: "+str(cost))   
            else:
                #El Bol2 se encuentra batido, no realizada ninguna accion y su costo es el mismo 
                print("El Bol2 esta batido.")
                print("sin accion. Costo actual ")+ str((cost))
            
            #Se define que el Bol3 esta sin batir   
            if tercer_estado=='1':
                print("El Bol3 esta sin batir.")
                print("Se traslada al Bol3")
                cost+=1#Incrementa el costo
                print("Costo Actual: "+str(cost))
                    
                estado_objetivo['Bol3'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida BOL3")
                print("Costo Actual: "+str(cost))       
            else:
                #El Bol3 se encuentra batido, no realizada ninguna accion y su costo es el mismo  
                print("El bol3 esta batido.")
                print("sin accion. Costo actual "+ str(cost))   
                
    #La locación de Bol es: Bol2
    elif bol =='Bol2':
        #Se debe confirmar en que estado se encuentra el Bol1, puede ser 0/1
        segundo_estado = input("Defina otro estado del Bol1: ")
        #Se debe confirmar en que estado se encuentra el Bol3, puede ser 0/1
        tercer_estado = input("Defina otro estado del Bol3: ")
        print("Meta deseada: "+str(estado_objetivo))
        print("La batidora esta en el Bol 2 ")
        
        if estado == '1': #Se define que el Bol2 esta sin batir
            print("El Bol esta sin batir. ")
            estado_objetivo['Bol2']='0' #Su estado cambia, ahora ya esta Batido
            cost+=1#Incrementa el costo de batir a la batidora
            print("Lugar de batida: Bol2")
            print("Costol Actual: "+str(cost))
            
            #Se define que el Bol1 esta sin batir
            if segundo_estado=='1':
                print("El Bol1 esta sin batir.")
                print("Se traslada al Bol1")
                cost+=1 #Incrementa el costo 
                print("Costo Actual: "+str(cost))
                
                estado_objetivo['Bol1'] = '0' #Su estado cambia, ahora ya esta Batido
                cost+=1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol1")
                print("Costo Actual: "+str(cost))   
            else:
                #El Bol1 se encuentra batido, no realizada ninguna accion y su costo es el mismo
                print("El Bol1 esta batido.")
                print("sin accion. Costo actual "+ str(cost))
            
            #Se define que el Bol3 esta sin batir
            if tercer_estado=='1':
                print("El Bol3 esta sin batir.")
                print("Se traslada al Bol3")
                cost+=1#Incrementa el costo 
                print("Costo Actual: "+str(cost))
                    
                estado_objetivo['Bol3'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+=1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol3")
                print("Costo Actual: "+str(cost))       
            else:
                #El Bol1 se encuentra batido, no realizada ninguna accion y su costo es el mismo 
                print("El bol3 esta batido.")
                print("sin accion. Costo actual "+str(cost))  
                    
        #Se define que el Bol2 esta batido
        if estado =='0':
            print("El Bol2 esta batido y no realiza ninguna acción.")
            
            #Se define que el Bol1 esta sin batir
            if segundo_estado=='1':
                print("El Bol1 esta sin batir.")
                print("Se traslada al Bol1")
                cost+=1#Incrementa el costo 
                print("Costo Actual: "+str(cost))
                
                estado_objetivo['Bol1'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol1")
                print("Costo Actual: "+str(cost))   
            else:
                #El Bol1 se encuentra batido, no realizada ninguna accion y su costo es el mismo 
                print("El Bol1 esta batido.")
                print("sin accion. Costo actual  ")+ str((cost))
                
            #Se define que el Bol3 esta sin batir
            if tercer_estado=='1':
                print("El Bol3 esta sin batir.")
                print("Se traslada al Bol3")
                cost+=1#Incrementa el costo 
                print("Costo Actual: "+str(cost))
                    
                estado_objetivo['Bol3'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol3")
                print("Costo Actual: "+str(cost))       
            else:
                #El Bol3 se encuentra batido, no realizada ninguna accion y su costo es el mismo  
                print("El bol3 esta batido.")
                print("sin accion. Costo actual "+ str(cost))
                
    #La locación de Bol es: Bol3
    if bol=='Bol3':
        #Se debe confirmar en que estado se encuentra el Bol1, puede ser 0/1
        segundo_estado = input("Defina otro estado del Bol1: ")
        #Se debe confirmar en que estado se encuentra el Bol2, puede ser 0/1
        tercer_estado = input("Defina otro estado del Bol2: ")
        print("Meta deseada: "+str(estado_objetivo))
        print("La batidora esta en el Bol 3 ")
        if estado == '1': #Se define que el Bol3 esta sin batir
            print("El Bol esta sin batir. ")
            estado_objetivo['Bol3']='0' #Su estado cambia, ahora ya esta Batido
            cost+=1#Incrementa el costo de batir a la batidora
            print("Lugar de batida: Bol3")
            print("Costol Actual: "+str(cost))
            
            #Se define que el Bol1 esta sin batir
            if segundo_estado=='1':
                print("El Bol1 esta sin batir.")
                print("Se traslada al Bol1")
                cost+= 1#Incrementa el costo 
                print("Costo Actual: "+str(cost))
                
                estado_objetivo['Bol1'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol1")
                print("Costo Actual: "+str(cost))   
            else:
                #El Bol1 se encuentra batido, no realizada ninguna accion y su costo es el mismo  
                print("El Bol1 esta batido.")
                print("sin accion. Costo actual "+ str(cost))
                
            #Se define que el Bol2 esta sin batir
            if tercer_estado=='1':
                print("El Bol2 esta sin batir.")
                print("Se traslada al Bol2")
                cost+=1#Incrementa el costo 
                print("Costo Actual: "+str(cost))
                    
                estado_objetivo['Bol2'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol2")
                print("Costo Actual: "+str(cost))       
            else:
                #El Bol2 se encuentra batido, no realizada ninguna accion y su costo es el mismo   
                print("El bol2 esta batido.")
                print("sin accion. Costo actual "+str(cost)) 
                
        #Se define que el Bol3 esta batido
        if estado =='0':
            print("El Bol3 esta batido y no realiza ninguna acción.")
            
            #Se define que el Bol1 esta sin batir
            if segundo_estado=='1':
                print("El Bol1 esta sin batir.")
                print("Se traslada al Bol1")
                cost+=1#Incrementa el costo 
                print("Costo Actual: "+str(cost))
                
                estado_objetivo['Bol1'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol1")
                print("Costo Actual: "+str(cost))   
            else:
                #El Bol2 se encuentra batido, no realizada ninguna accion y su costo es el mismo   
                print("El Bol1 esta batido.")
                print("sin accion. Costo actual ")+ str((cost))
            
            #Se define que el Bol2 esta sin batir
            if tercer_estado=='1':
                print("El Bol2 esta sin batir.")
                print("Se traslada al Bol2")
                cost+=1#Incrementa el costo de batir a la batidora
                print("Costo Actual: "+str(cost))
                    
                estado_objetivo['Bol2'] = '0'#Su estado cambia, ahora ya esta Batido
                cost+= 1#Incrementa el costo de batir a la batidora
                print("Lugar de batida Bol2")
                print("Costo Actual: "+str(cost))       
            else:
                #El Bol2 se encuentra batido, no realizada ninguna accion y su costo es el mismo   
                print("El bol2 esta batido.")
                print("sin accion. Costo actual "+ str(cost))
                
    #Batida completada            
    print("Estado objetivo: ")
    print(estado_objetivo)
    print("Medición del desempeño:"+ str(cost))
batidora()