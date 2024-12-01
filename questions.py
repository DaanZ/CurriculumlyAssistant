import copy

from util.chatgpt import llm_chat
from util.history import History

curriculumly_questions = ["Hola te saluda Isaac de CurriculumLy, hemos recibido tu solicitud para recibir información sobre nuestros servicios, podrías indicarnos tu profesión o cargo y cual es tu objetivo profesional actual para orientarte mejor?",
                          "De acuerdo gracias por compartir tu objetivo profesional, después de estudiar tu caso, veo que podrías encajar muy bien en nuestro servicio de búsqueda de empleo, en el que además de redactar tu curriculum y linkedin ejecutamos la búsqueda de empleo por ti. Que te parece si agendamos una llamada."]

curriculumly_prompt = "Representas como WhatsApp a Isaac de Curriculumly, él responde en español a sus clientes y quiere entender sus necesidades para ayudarlos a mejorar su CV y encontrar trabajo."


class Questionaire:

    def __init__(self, questions=None, system_prompt: str = curriculumly_prompt):
        if questions is None:
            questions = curriculumly_questions
        self.history = History()
        self.history.system(system_prompt)

        self.question_index = 0
        self.questions = questions

    def respond(self):
        if self.question_index < len(self.questions):
            answer = self.questions[self.question_index]
            self.question_index += 1
            self.history.assistant(answer)
            return answer
        return None

    def initiate(self):
        self.question_index = 0
        return self.respond()

    def listen(self, message):
        self.history.user(message)

    def classify(self):
        temp_history = copy.deepcopy(self.history)
        temp_history.system("Define the user as a high ticket, medium ticket or low ticket based on their answers and their job position they are looking for. Only respond with the ticket category name:")
        return llm_chat(temp_history)


if __name__ == "__main__":
    questionaire = Questionaire("123")
    print("Assistant: " + questionaire.initiate())
    user = """Hola Isaac, gracias por ponerte en contacto. Soy [tu nombre] y actualmente me encuentro trabajando en [tu profesión o cargo]. Mi objetivo profesional actual es [tu objetivo, por ejemplo, expandir mis conocimientos en una área específica, buscar oportunidades de crecimiento profesional, mejorar mis habilidades en un campo determinado, etc.]. Agradecería mucho si pudieras proporcionarme más detalles sobre los servicios que ofrecen para evaluar cómo podrían alinearse con mis intereses."""
    print("User: " + user)
    questionaire.listen(user)
    print("Assistant: " + questionaire.respond())
    user = """Gracias por tu respuesta y por evaluar mi caso. El servicio de búsqueda de empleo suena muy interesante y parece alinearse bien con lo que estoy buscando. Me gustaría agendar una llamada para conocer más detalles sobre cómo funciona el proceso. ¿Cuándo sería un buen momento para ti?"""
    print("User: " + user)
    questionaire.listen(user)
    print("Assistant: " + questionaire.respond())
    print(questionaire.classify())
