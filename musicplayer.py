from playsound import playsound
print('Songs that are available\n1.Chamber Of Reflection\n2.Daylight\n3.BAARISHEIN\n4.hiccup')
order=input("Enter the music you want to play")
if 'Chamber Of Reflection' in order:
    playsound('D:\\music\\Chamber Of Reflection.mp3')
elif 'Daylight' in order:
    playsound('D:\\music\\Daylight.mp3')

elif 'BAARISHEIN' in orde:
    playsound('D:\\music\\BAARISHEIN.MP3')
elif 'hiccup' in order:
    playsound('D:\\music\\hiccup.MP3')