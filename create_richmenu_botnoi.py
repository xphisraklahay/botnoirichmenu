#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
import json
import sys
import os
import subprocess
import requests
from linebot.models import *
from linebot.models.template import *
from linebot import 
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('xxx')

def create_richmenu_generic(mname,mchatbar,mimage,nrow,ncol,ActionList):
    rich_menu = RichMenu()
    height = 1686
    width = 2500
    rich_menu.size = {'width':width,'height':height}
    rich_menu.selected = False
    rich_menu.name = mname
    rich_menu.chatBarText = mchatbar
    xstep = width/ncol
    ystep = height/nrow
    nitem = nrow*ncol
    areaList = []
    for i in range(nrow):
        y = ystep*i
        for j in range(ncol):
            x = xstep*j
            rbound = RichMenuBounds(x,y,xstep,ystep)
            rAction = Action()
            actionComp = textList[ncol*i+j]
            if actionComp.find('://')!=-1:
                rAction.type = 'uri'
                rAction.uri = actionComp
            else:
                rAction.type = 'message'
                rAction.text = actionComp
            ar = RichMenuArea()
            ar.action = rAction
            ar.bounds = rbound
            areaList.append(ar)
    rich_menu.areas = areaList
    menuId = line_bot_api.create_rich_menu(rich_menu)
    contentType = 'image/jpeg'
    img = open(mimage,'rb').read()
    line_bot_api.set_rich_menu_image(menuId,contentType,img)
    return menuId


def create_teacher_menu():
    mname = 'สอนหนังสือ'
    mchatbar = 'สอนหนังสือ'
    mimage='botnoimenu.jpg'
    nrow=2
    ncol=3
    textList = ['เมนูหลัก','สอนภาษาอังกฤษ','สอนคณิตศาสตร์','สอนวิทยาศาสตร์','สอนสังคม','สอนภาษาไทย']
    return create_richmenu_generic(mname,mchatbar,mimage,nrow,ncol,textList)

def create_personal_menu():
    mname = 'บอทส่วนตัว'
    mchatbar = 'บอทส่วนตัว'
    mimage='botnoimenu.jpg'
    nrow=2
    ncol=2
    textList = ['เมนูหลัก','บอทน้อยส่วนตัว','ผองเพื่อนบอทน้อย','http://line://msg/text/?']
    return create_richmenu_generic(mname,mchatbar,mimage,nrow,ncol,textList)

{
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": true,
  "name": "Rich Menu 1",
  "chatBarText": "กลุ่มสาระฯ",
  "areas": [
    {
      "bounds": {
        "x": 969,
        "y": 19,
        "width": 620,
        "height": 495
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1Ruc3qMxDMAZZiz0Re1Wzph5_eGocyAM0508lUzUXGAE/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 107,
        "y": 48,
        "width": 639,
        "height": 485
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1DbVFhn1ZvCgi17QKj9E8HCJPvmSW3C2jkyHVWAomiWg/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 1764,
        "y": 29,
        "width": 678,
        "height": 494
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1gvxCWZNSyNQ5rDzSYy5Set4HUIZa2iTJLIZ9wu-EZKk/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 494,
        "y": 572,
        "width": 659,
        "height": 552
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1opK4x204ZyCLBIh7buY7pdu_H3YvBV7vZJ1lZToQsg8/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 1308,
        "y": 543,
        "width": 669,
        "height": 571
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1a1VdxYl_5eaPwZeM_W2oX8k01H-uHPHIJVAcOaEZcO0/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 1860,
        "y": 1156,
        "width": 543,
        "height": 504
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1gcTXp83matGM4MUmKNlTYzOuG8XDs68_Zg2guR9pzw8/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 959,
        "y": 1156,
        "width": 766,
        "height": 514
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1rzh7Dst1A_RGfwgcxOAnaacmwTbMvK2jpNPpkwRc74M/edit?usp=sharing"
      }
    },
    {
      "bounds": {
        "x": 97,
        "y": 1156,
        "width": 717,
        "height": 495
      },
      "action": {
        "type": "uri",
        "uri": "https://docs.google.com/document/d/1-tjkVSSrJ3OPvH7JgUEYdols7DmIH3bZ-GSS1vQarro/edit?usp=sharing"
      }
    }
  ]
}
#menuList = {}
#menuList['test'] = 'richmenu-xxx'
#menuList['translation'] = 'richmenu-xxx'
#menuList['Botnoi Teacher'] = 'richmenu-xxx'
#menuList['Personal Bot'] = 'richmenu-xxx'

def postmenu(menuName,userId='xxx'):
    menuId = menuList[menuName]
    line_bot_api.link_rich_menu_to_user(userId,menuId)
    return 'done'





