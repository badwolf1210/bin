#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import os
here = os.path.dirname(os.path.realpath(__file__))
import credentials as CR

hostname = os.uname()[1]
token, chatID = CR.get_credentials(f'{here}/{hostname}.token')

def send_message(text, chatID=chatID, token=token, time=10):
   """
   Send a text to the telegram chat defined by chatID, using the bot defined
   by token.
   """
   url = f'https://api.telegram.org/bot{token}/sendMessage'
   com = f'curl -s --max-time {time} '
   com += f'-d "chat_id={chatID}&disable_web_page_preview=1&text={text}" {url}'
   resp = os.popen(com).read().strip()
   return json.loads(resp)


def send_picture(pic, text='', chatID=chatID, token=token,time=10):
   """
   Send a text to the telegram chat defined by chatID, using the bot defined
   by token.
   """
   url = f'https://api.telegram.org/bot{token}/sendPhoto'
   com = f'curl -s -X  POST {url}'
   com += f' -F chat_id={chatID} -F photo=@{pic} -F caption="{text}"'
   resp = os.popen(com).read().strip()
   return json.loads(resp)


def send_file(fname, text='', chatID=chatID, token=token,time=10):
   """
   Send a text to the telegram chat defined by chatID, using the bot defined
   by token.
   """
   url = f'https://api.telegram.org/bot{token}/sendDocument'
   com = f'curl -s -X  POST {url}'
   com += f' -F chat_id={chatID} -F document=@{fname} -F caption="{text}"'
   resp = os.popen(com).read().strip()
   return json.loads(resp)


def send_video(vid, text='', chatID=chatID, token=token,time=10):
   """
   Send a text to the telegram chat defined by chatID, using the bot defined
   by token.
   """
   url = f'https://api.telegram.org/bot{token}/sendVideo'
   com = f'curl -s -X  POST {url}'
   com += f' -F chat_id={chatID} -F video=@{vid} -F caption="{text}"'
   resp = os.popen(com).read().strip()
   return json.loads(resp)

def send_audio(audio, text='', chatID=chatID, token=token,time=10):
   """
   Send a text to the telegram chat defined by chatID, using the bot defined
   by token.
   """
   url = f'https://api.telegram.org/bot{token}/sendAudio'
   com = f'curl -s -X  POST {url}'
   com += f' -F chat_id={chatID} -F audio=@{audio} -F caption="{text}"'
   resp = os.popen(com).read().strip()
   return json.loads(resp)

def report(text='', pic='', fname='', audio='', vid='', chatID=chatID,
                                                        token=token):
   """
   This function is a wrapper to use the appropriate function
   """
   if pic != '':
      return send_picture(pic, text=text, chatID=chatID, token=token)
   elif fname != '':
      return send_file(fname, text=text, chatID=chatID, token=token)
   elif vid != '':
      return send_video(vid, text=text, chatID=chatID, token=token)
   elif audio != '':
      return send_audio(audio, text=text, chatID=chatID, token=token)
   elif text != '':
      return send_message(text, chatID=chatID, token=token)

if __name__ == '__main__':
   import sys
   try: text = sys.argv[1:]
   except IndexError:
      print('File not specified')
      exit()
   
   M = report(' '.join(text),chatID=chatID,token=token)
   # pic = '../nubes.png'
   # M = report('nubes',pic='../nubes.png',chatID=chatID,token=token)
   # vid = '../Documents/RASP/PLOTS/w2/SC2/sfcwind.mp4'
   # M = report('nubes',pic=pic,vid=vid,chatID=chatID,token=token)
   # audio = 'miserables1.mp3'
   # M = report('Miserables', audio=audio, chatID=chatID, token=token)
