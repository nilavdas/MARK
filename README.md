# MARK
# WAKE WORD DETECTION
# ANY PROBLEM DM ME - NILAVDAS0180 online 24/7 :)
python project (assistant)

we all know how to make a assistant with python
i am here to help you how to make your own wake word detection
we will use picovoice detection
first we have to install some modules 
#pip install pvporcupine
#pip install pvporcupinedemo

now make your own wake word detection from https://picovoice.ai/console/ my wake word is "heymark" if you find hey mark in any line switch it to your won wake word , now to continue your wake word and your assistant in one file follow this steps:
'i will recommend anaconda becouse this proccess is deep learning , in annaconda many modules like numpy etc are inbiult , you may get some problems in normal python'
1 . go to anaconda-python directory (lib/site-pakage/pvporcupinedemo/pvporcupine_demo_mic) now open pvporcupine_demo_mic in ide ex- pycharm and in line no 111 there will be results >0: print(detected) something like that and cut the printdetected and change it to sys.exit() don't forgot to import sys

2.in your assistant file in while true there is voice_data or many people save it as query = takecommand before that line add a function named os.system('porcupine_demo_mic --keywords heymark') as i said my own keyword is hey mark you can switch is to your own keyword or the default one ex-porcupine,blueberry,terminator etc 
3. run your assistant in terminal thats it ...

And please try my recognizer values you will find in assistant.py which is give you very  low latency in after saying your commands it will recognize quickly

Share it !!!
