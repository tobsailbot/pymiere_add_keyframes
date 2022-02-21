import pymiere


seq = pymiere.objects.app.project.activeSequence

tracks = seq.videoTracks


# cantidad de tracks
tracks_num = tracks.numTracks


selected_clip = None

# hacer un loop entre los distintos clips de los distintos tracks
def getClips(i):
    num = 0
    try:
        while True:
            selection = tracks[i].clips[num].isSelected()
            # print(tracks[i].clips[num].name)
            if selection == True:
                global selected_clip
                selected_clip = [i,num]
                # print('el clip seleccionado es:')
                print(tracks[i].clips[num])
                # print(i,num)
                break
            num += 1

    # si aparece error no hacer nada..
    except:
        None



def loopTracks():
    i = 0
    # por cada track, obetner el clip correspondiente al index (i)
    for t in tracks:
        # print(f'clips del track numero {i}:')
        getClips(i)
        # print('\n')
        i += 1



def addFrames(t,c):

    project = pymiere.objects.app.project


    # seleccionar video sequence
    videoTracks = project.activeSequence.videoTracks
    #seleccionar el track uno de la sequence


    #seleccionar clip de la sequence
    clip = videoTracks[t].clips[c]

    components = clip.components[1]

    duration = clip.duration
    param = components.properties[1]

    # activa el relojito
    param.setTimeVarying(True)

    # agrega frame al inicio del clip
    param.addKey(clip.inPoint.seconds)
    out_value = param.getValue()
    print(out_value)

    # calcular el 25% del valor actual
    in_value = int(out_value - ((out_value * 25) / 100))
    print(in_value)

    param.addKey(clip.inPoint.seconds + duration.seconds)
    param.setValueAtKey(clip.inPoint.seconds,in_value, True)
    param.setValueAtKey(clip.inPoint.seconds+duration.seconds,out_value,True)

    print('se modifico el efecto: ')
    print(components.displayName)


#--------------------------------------------------------


loopTracks()
# imprime lista con el track = [0] y el clip = [1] seleccionado

sel_track = selected_clip[0]
sel_clip = selected_clip[1]

addFrames(sel_track,sel_clip)





