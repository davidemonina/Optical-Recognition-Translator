import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from PIL import Image
import pytesseract
import shutil
from watson_developer_cloud import LanguageTranslatorV3


class Myfunction:
#definition of the function that read the image (.jpg) and convert it into text
    def convert(self):
        txt.delete(0.0, 'end')
        #root.filename allow us to select the .jpg file to transform into text, then it saves the file's path
        root.filename = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select file",
            filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        #os.path.basename take the .jpg file's path and return just the file's name
        base = os.path.basename(root.filename)
        #shutil.copy it copies the jpg. file into the python folder where there is our code
        shutil.copy(root.filename, '/Users/davidemonina/PycharmProjects/ItProject')
        #now let's start converting the image into text
        im = Image.open(base)
        text = pytesseract.image_to_string(im, lang = 'eng')
        #it can happen that an image has a text organized on more lines, we need to put them together on a single string
        #so it can be translated with Watson Language Translator
        self.textoneline = str.join(" ",text.splitlines())
        sentense = self.textoneline
        txt.insert (0.0, sentense)

    def translate(self):
        txt1.delete(0.0, 'end')
        #let's translate the one string text with Watson Language Translator
        language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='MQKQyMl3EFc81EEIclyJRELxyThhZSM6KJTxqprbtYRY',
            url='https://gateway.watsonplatform.net/language-translator/api')
        translation = language_translator.translate(
            text=self.textoneline,
            model_id='en-it').get_result()
        #we need to transform the translated text (which is a modulable object) in a string, so we are able to select just the part we need
        theString = str(translation)
        #As output, WLT will return also the number of words and characters, to avoid this we decide to save just the central part,
        #that is the one between the character 35 and -44 (it will increase with the amount of characters and words)
        numerocaratteri = int(len(theString) - 200)
        numeroparole = int(len(theString.split())-20)
        if numerocaratteri <= 99 and numeroparole <= 9:
            cuttedstring = (theString[35:-44])
        elif 10 <= numerocaratteri <= 99 and 10 <= numeroparole <= 99:
            cuttedstring = (theString[35:-45])
        elif 100 <= numerocaratteri <= 999 and numeroparole <= 99:
            cuttedstring = (theString[35:-46])
        elif 100 <= numerocaratteri <= 999 and 100 <= numeroparole <= 999:
            cuttedstring = (theString[35:-47])
        elif numerocaratteri >= 1000 and 100 < numeroparole <= 999:
            cuttedstring = (theString[35:-48])
        elif numerocaratteri >= 1000 and numeroparole >= 1000:
            cuttedstring = (theString[35:-49])
        sentense1 = cuttedstring
        txt1.insert (0.0, sentense1)

#creation of GUI
root = Tk()
root.title("Optical Recognition Translator")
root.geometry("1000x500")

#creation of the button to select the file and convert it into text
MyfunctionObject = Myfunction()

#configuration of the button's style
style = ttk.Style(root)
style.theme_use("classic")
style.configure('Test.TButton', background="#328a7d", foreground="#ffffff", relief='flat')

#creation of the button to convert the image into text
btn = ttk.Button(
    root,
    text="UPLOAD AN IMAGE(.jpg)",
    style="Test.TButton",
    command=MyfunctionObject.convert)
btn.grid(
    row=2,
    column=1)

#creation of the button to translate the text
btn1 = ttk.Button(
    root,
    text="TRANSLATE YOUR TEXT",
    style="Test.TButton",
    command=MyfunctionObject.translate)
btn1.grid(
    row=2,
    column=5)

#creation of the text box where the translation will appear
txt = Text(root, width=70, height=30, wrap=WORD)
txt.grid(row=5, column=1, sticky=W)
txt1 = Text(root, width=70, height=30, wrap=WORD)
txt1.grid(row=5, column=5, sticky=W)

root.mainloop()
