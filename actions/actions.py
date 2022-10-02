# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

#from asyncore import dispatcher_with_send
#from re import template
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import SlotSet
#from swiplserver import PrologMQI, PrologThread

dispatcher: CollectingDispatcher
tracker: Tracker
#domain: Dict[Text, Any]
#lista_de_Dominio: List[Dict[Text, Any]]

class ActionPreguntarEdad(Action): 
  
    def name(self) -> Text:
         return "action_edad"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
              intent = tracker.latest_message['intent'].get['name']
              anios = tracker.latest_message['entities'][0]['value']
              dispatcher.utter_message(template="utter_happy")
              # [Nota]: CONTROLAR SI LO EJECUTA EN LA PROFE O UN ALUMNO!!!!
              if(str(intent)=="edad_usuario"): #Usuario proporciona su edad
                  if int(anios)>=30:
                     dispatcher.utter_message(template="utter_estas_trabajando")
                  else: 
                     dispatcher.utter_message(template="utter_preguntar_actividades") #template="utter_desea_continuar_tramites,..,..,"
              return []

class Action_Guarda_Ciudad(Action): 
    
    def name(self) -> Text: 
        return "action_ciudad_residencia"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         ciudad = tracker.latest_message['entities'][0]['value']
         print("Buenos dias !! Se rompe tracker.latest_message['intent'].get['name'] ? ademas , capturo "+ str(ciudad))
         
         #print("###########################################################################################################################")
         #print(tracker.latest_message) # imprime el dict (Es la estructura completa del NLU todas las estructuras definidas en el dominio)
         #print("###########################################################################################################################")
         #print(tracker.latest_message['intent']) # Me devuelve la estructura del intent {'name': 'preguntar_ciudad', 'confidence': 0.9583739638328552}
         intent0=tracker.latest_message['intent']        
         intent1=tracker.latest_message['intent']['name'] # Si no me equivoco me devuelve el nombre  
         intent2=tracker.latest_message['intent']['confidence'] # Si no me equivoco me devuelve el porcentaje de coincidencia  
         #print("######################################## Asi se manejan las estructuras mapa ###################################################################################")
         #print("El nro 0 Tiene que devolver la estructura del intent")
         #print(str(intent0))
         #print("El nro 1 Tiene que devolver el nombre")
         #print(str(intent1))
         #print("El nro 2 Tiene que devolver el porcentaje de coincidencia")
         #print(str(intent2))

         #intent = tracker.latest_message['intent'].get['name']   # ESTA MAL ESCRITO
         intent = tracker.latest_message['intent'].get('name') # ASI SE INVOCA 
         
         print("//////////////////////////////////Fue un exito")
         return[]

# aca van todas las actions relacionadas con la ciudad; es decir si :: (me preguntan de donde soy , o yo pregunto de donde es la persona)
#class ActionGuardaCiudad(Action):

#   def name(self) -> Text:
#        return "action_ciudad_residencia"            
#   def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,
#        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:   
#    intent = tracker.latest_message['intent'].get['name']
#    ciudad = tracker.latest_message['entities'][0]['value'] 
#    if str(intent) == "ciudad_residencia": 
     #       dispatcher.utter_message(text="Ahh mira vos!.") 
      #      if str(ciudad) == "tandil":
       #         SlotSet("slot_ciudad","tandil")
        #    return[SlotSet("slot_ciudad", 'ciudad')]
              #else:
              #  if str(intent)=="preguntar_ciudad": 
              #    if str(ciudad) != None and str(ciudad) != "Olavarria":
              #       print(str(ciudad))
              #       dispatcher.utter_message(template="No. ")
              #       a= "sasa" 
              #       b= "utter_viviendo_en"
              #       imprimir="No. " + str(a) + ", pero " + str(b)
              #       dispatcher.utter_message(text=imprimir)
              #    else:
              #       if str(ciudad) != None and str(ciudad) == "Olavarria":
              #          dispatcher.utter_message(template="utter_afirmar")
              #       else:   
              #          dispatcher.utter_message(text="Soy de Olavarria, pero actualmente vivo en Tandil")     
              #  slotC=tracker.get_slot('slot_ciudad')
              #  if str(slotC)==None :
              #    dispatcher.utter_message(template="utter_preguntar_donde_vive")
              #  return []



#class Action_Guarda_Ciudad(Action): # aca van todas las actions relacionadas con la ciudad; es decir si :: (me preguntan de donde soy , o yo pregunto de donde es la persona)
    
#    def name(self) -> Text: 
#         return "action_ciudad_residencia"
#    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
              
#              intent = tracker.latest_message['intent'].get['name']  
                  # verifico q halla consultado donde retirar la tarjeta
#              ciudad = tracker.latest_message['entities'][0]['value'] 
                  # busco/guardo la ultima entidad "ciudad" (Puede pertenecer a la que pregunte o la que me preguntaron(mi_ciudad))
              
              #---------------------Caso en que yo pregunto, de donde es la persona :::
#              if str(intent)=="ciudad_residencia": 
#               dispatcher.utter_message(text="Ahh mira vos!.") # contesta el bot
#               return[SlotSet("slot_ciudad",ciudad)] # guardo la ciudad del usuario

#              else:
               # ----------------------------Caso en que, me pregunten de donde soy :::
#                if str(intent)=="preguntar_ciudad": 
#                    if str(ciudad) != None and str(ciudad) != "Olavarria":
#                        print(str(ciudad)) #QUITAR puse esto para q no joda la func
#                        dispatcher.utter_message(template="No. ")
#                        a= 1 #template="utter_mi_ciudad"
#                        b= "utter_viviendo_en"
#                        imprimir="No. " + str(a) + ", pero " + str(b)
#                        dispatcher.utter_message(text=imprimir)
                        #dispatcher.utter_message(template="No. " + "utter_mi_ciudad" + ", pero " + "utter_viviendo_en")
                        #dispatcher.utter_message(text="No, soy de Olavarria, pero actualmente vivo en Tandil")
                        #preguntar en prolog si la ciudad tierra del fuego es mi ciudad
#                    else:
#                        if str(ciudad) != None and str(ciudad) == "Olavarria":
#                           dispatcher.utter_message(template="utter_afirmar")
#                        else: # no tengo nada en la entidad (mi ciudad) quiere decir que no consulto con entidad(consulta simple)  
#                           dispatcher.utter_message(text="Soy de Olavarria, pero actualmente vivo en Tandil")     
                    #return[soy de olavarria]


#                slotC=tracker.get_slot('slot_ciudad')
#                if str(slotC)==None :
#                  dispatcher.utter_message(template="utter_preguntar_donde_vive")

#               #return[SlotSet("slot_ciudad",str(ciudad))]
#                return []

            