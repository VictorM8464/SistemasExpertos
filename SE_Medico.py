# -*- coding: utf-8 -*-

class SistemaExpertoMedico:
    def __init__(self):
        self.base_conocimientos = {
            "fiebre": ["resfriado", "gripe"],
            "tos": ["resfriado", "gripe"],
            "dolor_cabeza": ["resfriado", "migrana"]
        }

    def iniciar_interaccion(self):
        print("Bienvenido al sistema experto medico.")
        print("Por favor, responde las siguientes preguntas con 'si' o 'no'.")

        sintomas = self.obtener_sintomas()

        if not sintomas:
            print("No se detectaron sintomas. No es posible hacer un diagnostico.")
        else:
            posibles_diagnosticos = self.realizar_diagnostico(sintomas)
            if posibles_diagnosticos:
                print("Los posibles diagnosticos son:", posibles_diagnosticos)
            else:
                print("No se pudo realizar un diagnostico en base a los sintomas proporcionados.")

    def obtener_sintomas(self):
        sintomas = []
        for sintoma in self.base_conocimientos.keys():
            respuesta = input(f"¿Tienes {sintoma}? (si/no): ").lower()
            if respuesta == "si":
                sintomas.append(sintoma)
        return sintomas

    def realizar_diagnostico(self, sintomas):
        posibles_diagnosticos = []
        for sintoma in sintomas:
            if sintoma in self.base_conocimientos:
                posibles_diagnosticos.extend(self.base_conocimientos[sintoma])
        return set(posibles_diagnosticos)


if __name__ == "__main__":
    sistema_experto = SistemaExpertoMedico()
    sistema_experto.iniciar_interaccion()


