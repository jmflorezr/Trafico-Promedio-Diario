import os
import ffmpeg
import sys

def resize(input_file_path, output_file_path, width, height):
    os.system("ffmpeg -i {input} -vf scale={width}:{height} {output}".format(
        input=input_file_path, width=width, height=height, output=output_file_path)
    )


resize(input_file_path='IMG_8363.MOV', output_file_path='7MA_resize.mp4', width=640, height=360)