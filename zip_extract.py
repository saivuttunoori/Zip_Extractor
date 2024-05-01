import PySimpleGUI as UI
from Zip_Extractor import extract_archive

UI.theme("Black")
label1 = UI.Text("select the archive")
input1 = UI.Input()
choose_button1 = UI.FileBrowse("Choose", key="archive")

label2 = UI.Text("select the directory")
input2 = UI.Input()
choose_button2 = UI.FolderBrowse("Choose", key="folder")

extract_button = UI.Button("Extract")
output_label = UI.Text(key="output", text_color="green")

window = UI.Window("Archive Extractor",
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_button, output_label]])
while True:
    events, values = window.read()
    print(events, values)
    archivePath = values['archive']
    folderPath = values['folder']
    extract_archive(archivePath,folderPath)
    window["output"].Update(value="extraction completed")

window.close()
