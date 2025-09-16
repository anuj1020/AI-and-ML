import ffmpeg


def extractAudioFromVideo():
        input_file = r"F:\VS Workspace\Python\MeMiniuts\uploads\RAG with Streamlit.mp4"
        output_file = r'F:\VS Workspace\Python\MeMiniuts\uploads\audios\RAG with Streamlit(output_audio).mp3'

        ffmpeg.input(input_file).output(output_file).run()


# class filterData():
    





class modelConfigurations():
    def config():
        pass


if __name__ == '__main__':
    extractAudioFromVideo()