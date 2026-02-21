class ContenidorVirus:
    def __init__(self, codi_seguretat_inicial):
        
        self.responsable = "Dr. Isaacs"
        
        
        self.__temperatura = 0.0 
        
        
        self.__password = codi_seguretat_inicial

        self.__password_intents = 3

   
    def llegir_termometre(self):
        return self.__temperatura

    def modificar_temperatura(self, nova_temp, password_intent):
        if password_intent != self.__password:
            print("ACCÉS DENEGAT")
            return False
        else:
            if nova_temp >= -50 and nova_temp <= 100:
                print("TEMPERATURA SEGURA")
                self.__temperatura = nova_temp
                print("Temperatura ajustada correctament")
                return True
            else:
                print("ALERTA: TEMPERATURA CRÍTICA!")
                return False
                
    def canviar_password_mestre(self, vell_pass, nou_pass):
        vell_pass = input("Introdueix la contrasenya vella: ")
        if vell_pass == self.__password:
            nou_pass = input("Introdueix la nova contrasenya: ")
        else:
            return False
