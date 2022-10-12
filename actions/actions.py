from ast import Import
from asyncore import dispatcher_with_send
from http.client import responses
from re import template
from typing import Any, Text, Dict, List
from charset_normalizer import from_path

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet
from swiplserver import PrologMQI, PrologThread
from werkzeug import Response    
#from mis_Librerias import * # importa todo
#from mis_Librerias import dict_Functions

    #de esta forma navega entre carpetas from actions/mis_librerias  
from actions.mis_Librerias import dict_Functions

#from mis_Librerias import dict_Functions
#import dict_Functions

#from actions import dict_Functions
#import dict_Functions
#from actions import dict_Functions   # esto funciona pero tiene que estar en la misma carpeta de este proyecto
#from actions import FuncionesDict # funciona tambien para :: import dict_Functions ya q esta en la misma carpeta
#from actions.Dict_Functions import getList_Dict_in_List, getList_Dict_in_List_Single_Key
#import getList_Dict_in_List,getList_Dict_in_List_Single_Key

#import dict_Functions as FuncionesDict
class ActionPreguntarEdad(Action): 
  
    def name(self) -> Text:
         return "action_edad"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
              intent = tracker.latest_message['intent'].get('name')
              slotEdad= tracker.get_slot('slot_anios')
              if(str(intent)=="preguntar_edad"):
                    #faltaria entrenar "preguntar_edad" con ejs como (tenes 18 anios?) y crear un slot mi_edad ya que en caso contrario va a machear con algun ejemplo de "proporcionar_edad"
                    dispatcher.utter_message(text="Tengo 27 años")
                    slotEdad= tracker.get_slot('slot_anios')
                    print("El slot tiene valor [Edad_Usuario]:: "+str(slotEdad))
                    if ( slotEdad == None ):
                        dispatcher.utter_message(response="utter_preguntar_edad") 
              #if(str(intent)=="proporcionar_edad" and slotEdad != None and preguntar si es la misma persona o otra):  [Nota]: Lo mejor es cargar un Json y guardar la info ahi, asi se evita perder la ingo de los slot
              if(str(intent)=="proporcionar_edad" and slotEdad != None): 
                anios = tracker.latest_message['entities'][0]['value']
                SlotSet("slot_anios",str(anios)) # verificar que guarde el valor , caso contrario hay q hacer,  return [SlotSet("slot_anios",str(anios))]
              return []

class Action_Guarda_Ciudad(Action): # aca van todas las actions relacionadas con la ciudad; es decir si :: (me preguntan de donde soy , o yo pregunto de donde es la persona)
    
    def name(self) -> Text: 
        return "action_ciudad_residencia"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
              
        # busco/guardo la ultima entidad "ciudad" (Puede pertenecer a la que pregunte o la que me preguntaron(mi_ciudad))              
         
        intent = tracker.latest_message['intent'].get('name')  
        if str(intent)=="preguntar_ciudad": 
            my_city = next(tracker.get_latest_entity_values("mi_ciudad"),None)
            print(str(my_city)+" esta es la city x la cual consulta")
            if str(my_city) != None and str(my_city) != "Olavarria":
                dispatcher.utter_message(template="utter_mi_ciudad")       
                dispatcher.utter_message(text="pero")
                dispatcher.utter_message(template="utter_viviendo_en") 
            else:
                if str(my_city) != None and str(my_city) == "Olavarria":
                    print("Entro y macheo olavarria")
                    dispatcher.utter_message(template="utter_afirmar")
                    dispatcher.utter_message(response="No"+"{utter_afirmar}")
                else: # no tengo nada en la entidad (mi ciudad) quiere decir que no consulto con entidad(consulta simple)  
                    dispatcher.utter_message(text="Soy de Olavarria, pero actualmente vivo en Tandil")     
            
            slotC=tracker.get_slot('slot_ciudad') # Si nunca guardo el slot de quien me esta hablando (es null) le pregunta donde vive
            print("###############################  "+str(slotC)+ "    [Es el valor del slot ciudad de USUARIO]")
            if slotC == None:
                print("Esntra a preguntar")    # no se que tan bueno esta preguntarlo aca , lo mejor es decidir en la story a quien se lo pregunta , es decir poner condiciones si puedo preguntar o no
                dispatcher.utter_message(response="utter_preguntar_donde_vive") # usar response ya que template sera DEPRECATED
              #---------------------Caso en que yo pregunto, de donde es la persona ::: (me dicen a que ciudad pertenecen) 
        if str(intent)=="ciudad_residencia": 
            #user_city = next(tracker.get_latest_entity_values("mi_ciudad"),None)
            user_city = next(tracker.get_latest_entity_values("ciudad"),None)
            dispatcher.utter_message(text="Ahh mira vos!. Asi que sos de "+str(user_city)) # contesta el bot
            return[SlotSet("slot_ciudad",str(user_city))] # guardo la ciudad del usuario 
        return []

class ActionWithProlog(Action):
    def name(self) -> Text:
        return "action_Consultas_Prolog"
    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:

                intent=tracker.latest_message['intent'].get('name') # Consulto el intent que se ejecuto
                prolog_thread.query_async("consult('C:/Rasa_projects/new_rasa_project/yo_Bot/prolog/ConectaActions.pl')", find_all=False)    
                    
                if(str(intent) == "consultar_estado_actual_cursadas"):  # -que materias estas cursando ?
                    #prolog_thread.query_async(f"estoyCursando([X|Y])", find_all=False)
                    prolog_thread.query_async(f"estoyCursando(L)", find_all=False)
                    result = prolog_thread.query_async_result()
                    msg="Estoy cursando:\n\t" + str(dict_Functions.getValues_Dict_in_List_SingleKey(result))
                    dispatcher.utter_message(text=f"{msg}")   
                    return[]         

                if( str(intent) == "consultar_finales_dados"):               # - que finales pudiste rendir ?
                    prolog_thread.query_async(f"finalesAprobados(L)", find_all=False)
                    result = prolog_thread.query_async_result()
                    msg=f"Los finales que rendi de momento son:\n\t\t\t {dict_Functions.getValues_Dict_in_List_SingleKey(result)}"
                    dispatcher.utter_message(text=f"{msg}")
                    return[]       

            return[]