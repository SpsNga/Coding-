import os

if __name__ == "__main__":
    x = input("What do you want me to say: ")
    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
              f'$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
              f'$s.Speak(\'{x}\')"'
    os.system(command)

