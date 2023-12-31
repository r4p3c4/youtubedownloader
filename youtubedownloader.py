from pytube import YouTube
import os
from moviepy.editor import *

def Main():
        print("""
            #################################################################
            #                                                               #
            #     ================  YOUTUBEDOWNLOADER  ===============      #
            #                                                               #
            #        -------------- Sigueme en Linkdn -------------         #
            #                                                               #
            #       https://www.linkedin.com/in/rafael-peiro-calvet/        #                                  
            #                                                               #
            #################################################################
            #                                                               #
            #                        Opciones:                              #
            #                                                               #
            #     1) Descargar video                                        #
            #     2) Descargar musica                                       #
            #     3) Descargar una lista de videos a partir de un archivo   #
            #     4) Descargar una lista de musica a partir de un archivo   #
            #     5) Salir                                                  # 
            #                                                               #
            #################################################################
        """)
   
fin = False

while not fin:
        try:        
            Main()
            opcion=int(input("Selecciona una opcion del menu: ")) 

            if opcion == 1:
            
                def download_video(url):
                    try:
                         # Crear objeto YouTube
                            yt = YouTube(url)

                        # Obtener la mejor resolución disponible
                            video = yt.streams.get_highest_resolution()

                        # Descargar el vídeo
                            video.download()
                            print("Descarga completada.")
                        # Obtener el título del video
                            video_title = yt.title

                        # Obtener el nombre del archivo descargado
                            downloaded_file = video.default_filename

                        # Renombrar el archivo descargado con el título del video
                            new_file_name = f"{'Linkedin-rafael-peiro-calvet-'+video_title}.{downloaded_file.split('.')[-1]}"
                            os.rename(downloaded_file, new_file_name)

                    except Exception as e:
                            print("Error durante la descarga:", str(e))

                    # URL del vídeo de YouTube que deseas descargar
                video_url = input("Pon la url de youtube: ")

                # Llamar a la función para descargar el vídeo
                download_video(video_url)               
     
            elif opcion == 2:
             
                def download_musica(url):
                    try:
                        # Crear objeto YouTube
                        yt = YouTube(url)

                        # Obtener la mejor resolución disponible
                        video = yt.streams.get_highest_resolution()

                        # Descargar el vídeo
                        video.download()
                        print("Descarga completada.")

                        # Obtener el nombre del archivo descargado
                        video_file = video.default_filename

                        # Convertir el vídeo a mp3
                        mp3_file = "Linkedin-rafael-peiro-calvet_"+ video_file.split('.')[0] + '.mp3'
                        video_clip = VideoFileClip(video_file)
                        audio_clip = video_clip.audio
                        audio_clip.write_audiofile(mp3_file)
                        audio_clip.close()
                        video_clip.close()

                        print("Conversión a mp3 completada. Archivo guardado como", mp3_file)

                        os.remove(video_file)
        

                    except Exception as e:
                       print("Error durante la descarga y conversión:", str(e))


                # URL del vídeo de YouTube que deseas descargar
                musica_url = input("Pon la url del video de youtube: ")

                # Llamar a la función para descargar el vídeo y convertirlo a mp3
                download_musica(musica_url)
            elif opcion == 3:

                def download_video_from_file(file_name):
                    try:
                # Leer las URLs del archivo de texto
                     with open(file_name, 'r') as file:
                      urls = file.readlines()

                     for url in urls:
                        url = url.strip()  # Eliminar espacios en blanco y saltos de línea

                        # Crear objeto YouTube
                        yt = YouTube(url)

                        # Obtener la mejor resolución disponible
                        video = yt.streams.get_highest_resolution()

                        # Descargar el vídeo
                        video.download()
                        print(f"Descarga completada para la URL: {url}")

                        # Obtener el título del video
                        video_title = yt.title

                        # Obtener el nombre del archivo descargado
                        downloaded_file = video.default_filename

                        # Renombrar el archivo descargado con el título del video
                        new_file_name = f"{'Linkedin-rafael-peiro-calvet-'+video_title}.{downloaded_file.split('.')[-1]}"
                        os.rename(downloaded_file, new_file_name)

                    except Exception as e:
                        print("Error durante la descarga:", str(e))

                        # Nombre del archivo de texto que contiene las URLs
                file_name =input("Pon el nombre de un archivo y su extesion, que contenga las URLS de youtube (ejemplo urlyoutube.txt):")

                        # Llamar a la función para descargar los vídeos
                download_video_from_file(file_name)

            elif opcion == 4:
                def download_music_from_file(file_name):
                    try:
                    # Leer las URLs del archivo de texto
                     with open(file_name, 'r') as file:
                      urls = file.readlines()

                     for url in urls:
                        url = url.strip()  # Eliminar espacios en blanco y saltos de línea
                        # Crear objeto YouTube
                        yt = YouTube(url)

                        # Obtener la mejor resolución disponible
                        video = yt.streams.get_highest_resolution()

                        # Descargar el vídeo
                        video.download()
                        print("Descarga completada.")

                        # Obtener el nombre del archivo descargado
                        video_file = video.default_filename

                        # Convertir el vídeo a mp3
                        mp3_file = "Linkedin-rafael-peiro-calvet_"+ video_file.split('.')[0] + '.mp3'
                        video_clip = VideoFileClip(video_file)
                        audio_clip = video_clip.audio
                        audio_clip.write_audiofile(mp3_file)
                        audio_clip.close()
                        video_clip.close()

                        print("Conversión a mp3 completada. Archivo guardado como", mp3_file)

                        os.remove(video_file)
        

                    except Exception as e:
                       print("Error durante la descarga y conversión:", str(e))


                # Nombre del archivo de texto que contiene las URLs
                file_name =input("Pon el nombre de un archivo y su extesion, que contenga las URLS de youtube (ejemplo urlyoutube.txt):")

                        # Llamar a la función para descargar los vídeos
                download_music_from_file(file_name) 

            elif opcion == 5:
                fin = True
                print(" ==> Has salido correctamente <==")
                exit()
            else:
                print("El valor numerico introducido no corresponde con las opciones del menu")
        except KeyboardInterrupt:
            print(" ==> Has salido correctamente <== ")
            exit()
        
        except ValueError:
             print("No se admiten caracteres")