import reflex as rx 
import asyncio
import textwrap
from IPython.display import display
from IPython.display import Markdown
import base64
from PIL import Image
import google.generativeai as genai
import os



   
class AppState(rx.State):
    prompt = ''
    promptu = ''
    leftSpacing: str='0.5rem'
    img: list[str] = []
    encoded_images: str=""
    answer : str=""
    question: str = ""
    answera :str =""
    box_padding: str = "0px 0px" 
    box_cadding: str= "0px 0px"

    def to_markdown(self,text):
        text = text.replace('•', ' *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    def history_compo(self):
        self.promptu = "History"
        self.prompt = self.promptu
    
    def math_compo(self):
        self.promptu = "Mathematics"
        self.prompt = self.promptu

    def astro_compo(self):
        self.promptu = "Astrology"
        self.prompt = self.promptu
    
    def art_compo(self):
        self.promptu = "Art and Culture"
        self.prompt = self.promptu
    
    def cyber_compo(self):
        self.promptu = "Data and Cyber Security"
        self.prompt = self.promptu
    
    def event_compo(self):
        self.promptu = "Event Management and Plannning"
        self.prompt = self.promptu
    
    def rel_compo(self):
        self.promptu = "Religion and Traditions"
        self.prompt = self.promptu

    def chat_compo(self):
        self.promptu = "Creative Ideas and Innovative Chat"
        self.prompt = self.promptu
    
    def soft_compo(self):
        self.promptu = "Software Engineering and Apps"
        self.prompt = self.promptu
    
    def mech_compo(self):
        self.promptu = "AutoMobile Engineering"
        self.prompt = self.promptu
        

    def process_input(self):
        prompt = f"You are a prodigy in the subject of {self.promptu},You know Almost everything,but will not give answer if someone ask other than {self.promptu}.Act as a highly educated professor for '{self.question}'which is in context of subject {self.promptu}, generate an answer without limit, use emojis. Segregate into: Introduction (new paragraph), Example (new paragraph). Use '<br>' for new lines, maintain two-line spacing after each section. Include related links at the end.\nTopic: '{self.question}'"
        genai.configure(api_key=os.getenv("API_KEY_G"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        self.to_markdown(response.text)
        self.answera = response.text
        self.padding_put(self.answera)
        self.question=""
    
    def padding_put(self,answer:str):
        self.box_padding = "10px 20px" if answer.strip() else "0px 0px"

    def on_load(self,answer,answera):
        self.answer=""
        self.box_padding="0px 0px"
        self.box_cadding="0px 0px"
        self.answera=""
        self.img=""
    
    


        


    def google(self):
        img = Image.open(".web/public/"+self.img[0])
        genai.configure(api_key=os.getenv("API_KEY_G"))
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(img)
        self.answer = response.text
        self.padding_hut(self.answer)

    def padding_hut(self,answerw:str):
        self.box_cadding = "10px 20px" if answerw.strip() else "0px 0px"



    async def handle_upload_and_message(self,files: list[rx.UploadFile]):

        self.img = []

        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            with open(outfile,"wb") as file_object:
                file_object.write(upload_data)
            
            self.img.append(file.filename)
            image_path = f".web/public/{file.filename}"
            encoded_image = self.encode_image(image_path)
            self.encoded_images += f"{encoded_image}\n"
            self.google()
    
    
    def emptyFunction(self)-> None:
        pass
    
    def encode_image(self,image_path):
        image = Image.open(image_path)
        image = image.resize((256,256))
        image.save(image_path)

        with open(image_path,"rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        
        return encoded_string
