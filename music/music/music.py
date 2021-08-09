from requests import *
from pygame import *

init()
mixer.init()

def music(text,spd):

      try:
            response = get("https://fanyi.baidu.com/gettts?lan=zh&text=%s&spd=%s&source=web"%(text,str(spd)))
            with open(text+".mp3","wb") as f:
              f.write(response.content)

            mixer.music.load(text+".mp3")
            mixer.music.play()
      except error:
            print("\033[31mSpdError:Speak faster than specified\033[0m")
