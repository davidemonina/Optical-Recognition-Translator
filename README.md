# Optical Recognition Translator
Thanks to OCR and Watson Language Translator, this program is able to take as input an image (.jpg) with a printed text on and it gives back as output the translated text. 

## Requirements to run the program
Install Homebrew from 
https://brew.sh/index_it

From the terminal download:

```sh
brew install tesseract

sudo easy_install numpy

brew install opencv
```

Install in the Project Interpreter these packs:

```sh
watson-developer-cloud

pytesseract
```
This program requires internet connection.

IMPORTANT: We have attached two folders (ItProject and ItImage), one with the code and the other one with some images: DON'T copy or move the images into the ItProject folder!
## Configure

To configure the program change the folder path of the below function (23. '/Users/davidemonina...Itproject') with the folder path of the folder that contains OprticalRecognitionTranslator.py (so the folder path of ItProject).
To obtain the folder path, move the folder into the terminal.

```sh
shutil.copy(root.filename, '/Users/davidemonina/PycharmProjects/ItProject')
```

## Run the program

Run the program. Click on the button "UPLOAD AN IMAGE(.jpg)" and choose an image contained in ItImage or an image downloaded in the computer (the only limitation is that the image must have printed text, the handwritten text is also recognized). After that the image is converted in text you can translate the text clicking on the button "TRANSLATE YOUR TEXT".

ENJOY IT!

Davide Monina - Matteo Bonadies
