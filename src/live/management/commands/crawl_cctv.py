# -*-coding:utf-8 -*-
# 
# Created on 2016-07-22
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyvirtualdisplay import Display

from django.core.management.base import BaseCommand

from live.models import Live


class Command(BaseCommand):

    help = 'A cctv5 live crawler'
    can_import_settings = True

    cctv5 = 'http://www.myp2pch.net/tiantian2.html?c=cctv5&w=800&h=600'
    iframe = 'iframe'

    def handle(self, *args, **options):
        display = Display()
        display.start()
        driver = webdriver.Firefox()
        try:
            driver.get(self.cctv5)

            # 等待iframe
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.iframe))
            )
            driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, self.iframe))

            # 等待player
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body div.switch div.slist li"))
            )

            # 获取 SUPER HIGH 信号源
            switch = driver.find_elements(By.CSS_SELECTOR,
                                          'div.slist li')[-1].find_element(By.CSS_SELECTOR, 'a').get_attribute('onclick')
            driver.execute_script(switch)

            # 处理得到的player
            player = driver.find_element(By.CSS_SELECTOR, 'div#player object')
            m3u8 = player.find_element(By.CSS_SELECTOR, 'param[name=flashvars]').get_attribute('value')
            m3u8 = m3u8[m3u8.index('a=') + 2:]
            m3u8 = urllib.unquote(m3u8)
        except Exception as e:
            print e
            return None
        else:
            try:
                live = Live.objects.get(live_code='cctv5')
                live.live_m3u8 = m3u8
            except Live.DoesNotExist:
                live = Live(live_code='cctv5', live_name=u'cctv5 直播', live_m3u8=m3u8)

            live.save()
        finally:
            driver.quit()
            display.stop()
