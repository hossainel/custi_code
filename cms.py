#!/usr/bin/env python3
# -*- coding: utf-8 -*
# Hail Ea,Enki,Satanama, the morning star <3
#https://twitter.com/palemoongod / https://twitter.com/kill_the_net
##[------------------------------[LIBS]--------------------------------]##
from argparse import ArgumentParser
from multiprocessing.dummy import Pool
from time import time,strftime,gmtime,sleep
from math import ceil
from random import choice,randint
import requests, re, concurrent.futures, sys, platform, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
if platform.system() == 'Windows':
    cmd = 'cls'
else:
    cmd = 'clear'
##[------------------------------[LIBS]--------------------------------]##
##[-------------------------------[COLORS]--------------------------------]##
R,G,B,C,M,Y = "\033[0;31;40m","\033[0;32;40m","\033[0;34;40m","\033[0;36m",'\033[95m',"\033[0;33;40m"
BOLD,UNDER,END = '\033[1m','\033[4m','\033[0m'
GREY = "\033[0;37;40m"
log = strftime("[%H:%M:%S]", gmtime())
##[-------------------------------[COLORS]--------------------------------]##
##[-------------------------------[LOGO]--------------------------------]##
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' 
                   [FEDERATION BLACK HAT SYSTEM | 0x666]
                                 
           s,                                     .s
            ss,                                 .ss     
            'SsSs,                           .sSsS'               
             sSs'sSs,                    .sSs  sSs                
              sSs  'sSs,              .sSs'   sSs                 
               sS,    'sSs,         .sSs'    .Ss                  
               'Ss       'sSs,   .sSs'       sS'                                  
                sSs         ' .sSs'         sSs                         
                 sSs       .sSs' ..,       sSs                     
                  sS,   .sSs'     'sSs,   .Ss                            
                  'Ss .Ss'           'sSs. ''                            
                   sSs '                'sSs,                     
              .sS.'sSs                 .. 'sSs,     
            .sSs'    sS,               .Ss    'sSs,
         .sSs'       'Ss               sS'       'sSs,
      .sSs'           sSs             sSs           'sSs,
   .sSs'____________________________ sSs ______________'sSs,
.sSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'.Ss SSSSSSSSSSSSSSSSSSSSSs,
                        ...         sS'
                         sSs       sSs
                          sSs     sSs      [+]-: KTN / @palemoongod
                           sS,   .Ss       [+]-: iCMS
                           'Ss   sS'
                            sSs sSs
                             sSsSs
                              sSs
                               s

        [PS]-:~~ Stealing the author work won't make you an author just another lame poser :) ~~'''

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (choice(colors), line, clear))
        sleep(0.03)
        pass


def logo2():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
    x = ''' 

                                     ██╗       ██████╗███╗   ███╗███████╗
                                     ██║      ██╔════╝████╗ ████║██╔════╝
                                     ██║█████╗██║     ██╔████╔██║███████╗
                                     ██║╚════╝██║     ██║╚██╔╝██║╚════██║
                                     ██║      ╚██████╗██║ ╚═╝ ██║███████║
                                     ╚═╝       ╚═════╝╚═╝     ╚═╝╚══════╝v1.0

                                          [KILL THE NET X PALEMOONGOD]                                     '''

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (choice(colors), line, clear))
        sleep(0.03)
        pass
def load():
    for n in range(1,5):
        blah="\|/-\|/-"
        for l in blah:
            sys.stdout.write(BOLD+l+END)
            sys.stdout.flush()
            sys.stdout.write('\b')
            sleep(0.1)
##[-------------------------------[LOGO]--------------------------------]##
##[-----------------------------------------------------------------------------------------------[666]------------------------------------------------------------------------------------------------]##
class cms_check:
    def __init__(self, site):
        self.site = site
    def url__fix(self):
      url = self.site
      if url[-1] == "/":
        pattern = re.compile('(.*)/')
        ha = re.findall(pattern,url)
        url = ha[0]
      if url[:7] != "http://" and url[:8] != "https://":
        url = "http://" + url
      return url
    def normal_check(self, kills=0):
      global SCANNED, LEN_SITES
      if kills==0:
        url = self.url__fix()
      else:
        url = kills
      UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
      while 1:
        try:
            ktn = requests.get(url, headers=UA, verify=False, timeout=30, allow_redirects=True)
            if ktn.status_code==200:
              SCANNED += 1
              if 'content="PrestaShop"' in ktn.text:
                cms = 'PRESTASHOP'                
                print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{G}({cms:40})~+=======> {C}{url:40}{END}')
                open('PRESTASHOP.txt','a').write(url+'\n')
                break
              if 'catalog/view/' in ktn.text:
                cms = 'OpenCart'
                print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{B}({cms:40})~+=======> {C}{url:40}{END}')
                open('OPENCART.txt','a').write(url+'\n')
                break
              if 'meta name="generator" content="vBulletin' in ktn.text or 'window.vBulletin' in ktn.text:
                cms = 'vBulletin'
                print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{M}({cms:40})~+=======> {C}{url:40}{END}')
                open('VBULLETIN.txt','a').write(url+'\n')
                break
              if '/sites/default/' in ktn.text:
                cms = 'Drupal'
                print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{Y}({cms:40})~+=======> {C}{url:40}{END}')
                open('DRUPAL.txt','a').write(url+'\n')
                break
              if 'laravel_session' in ktn.cookies:
                cms = 'Laravel'
                print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{GREY}({cms:40})~+=======> {C}{url:40}{END}')
                open('LARAVEL.txt','a').write(url+'\n')
                break
              else:
                KILL=False
                for PATH in ['/wp-includes/css/buttons.css', '/media/system/js/core.js']:
                  ktn1 = requests.get(url+PATH, headers=UA, verify=False, timeout=30, allow_redirects=True)
                  if 'WordPress-style Buttons' in ktn1.text:
                    cms = 'Wordpress'
                    print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{R}({cms:40})~+=======> {C}{url:40}{END}')
                    open('WORDPRESS.txt','a').write(url+'\n')
                    KILL=True
                    break
                  if 'window.Joomla' in ktn1.text:
                    cms = 'Joomla'
                    print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]*{C}({cms:40})~+=======> {C}{url:40}{END}')
                    open('JOOMLA.txt','a').write(url+'\n')
                    KILL=True
                    break
                if KILL:
                  break
                if not KILL:
                  open('other_cms.txt','a').write(url+'\n')
                  break
            else:
              LEN_SITES -= 1
              print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]{R}*(TIME OUT)~+=======> {BOLD}{C}{url:40}{END}')
              break
        except:
          LEN_SITES -= 1
          print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]{R}*(TIME OUT)~+=======> {BOLD}{C}{url:40}{END}')
          break
    def advence_check(self):
      global SCANNED, LEN_SITES
      url = self.url__fix()
      UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
      try:
        for X in ['/','/blog','/forum','/forums', '/shop']:
          ne_w=url+X
          ktn00 = requests.get(ne_w, headers=UA, verify=False, timeout=30, allow_redirects=True).status_code
          if ktn00==200:
            k_i_l_l = self.normal_check(ne_w)
      except:
        LEN_SITES -= 1
        print(f'{BOLD}[{str(SCANNED)}/{str(LEN_SITES)}]{R}*(TIME OUT)~+=======> {BOLD}{C}{url:40}{END}')

############################
def work_666(SITE):
    try:
      if TYPE==1:
        k_t_n   = cms_check(site=SITE)
        s_e_i_f = k_t_n.normal_check()
      elif TYPE==2:
        k_t_n   = cms_check(site=SITE)
        s_e_i_f = k_t_n.advence_check()
    except Exception as e:
        print(e)
##[-----------------------------------------------------------------------------------------------[666]------------------------------------------------------------------------------------------------]##
# MAIN ################################################# 

if __name__ == '__main__':
    try:
        logo()
        print(f'{BOLD}\n')
        start = time()
        ktn = ArgumentParser()
        ktn.add_argument('-l', '--list', required=True, help="<put your list of website exmple: -l list_site.txt>")
        ktn.add_argument('-m', '--mode', required=True, type=int, help="<MODE OF WORK, MODE (1) = NORMAL SCANING, MODE (2) = ADVANCE SCANING>")
        ktn.add_argument('-t', '--thread', default=10, type=int, help="<threading exmple: -t 100>")
        satan = ktn.parse_args()
        #-----------------------------#
        SITES     = satan.list
        TYPE      = satan.mode
        THREADING = satan.thread
        #-----------------------------#
        try:
            with open(SITES) as f: SITES = f.read().splitlines()
            LEN_SITES = len(SITES)
        except:
            print(f'{R} [-] ERROR:\n\t {Y} CAN`T OPEN SITES_LIST FILE!{END}')
            exit(0)
        #-----------------------------#
        #-----------------------------#
        try:
            if TYPE == 1 or TYPE == 2:
                if   TYPE==1: MODE = 'NORMAL'
                elif TYPE==2: MODE = 'ADVANCE'
            else:
                print(f'{R} [-] ERROR:\n\t {C} MODE TYPE ERROR CHECK({sys.argv[0]} -h){END}')
                exit(0)
        except:
            print(f'{R} [-] ERROR:\n\t {C} MODE TYPE ERROR(2) CHECK({sys.argv[0]} -h){END}')
            exit(0)
        #-----------------------------##
        SCANNED     = 0
        #-----------------------------##
        load()
        os.system(cmd)
        logo2()
        print('\n')
        print(f'{BOLD}{log}{G}{BOLD}[✓]~ {BOLD} LOADED: {M} ({str(LEN_SITES)})  WEBSITE {BOLD}\n\t  {BOLD}[✓]~{Y}  WORK WITH MODE:{MODE} {BOLD}\n\t  {BOLD}[✓]~{R}  WORK WITH: {(str(THREADING))} THREADS{END}')
        with concurrent.futures.ThreadPoolExecutor(max_workers=THREADING) as killz:
            killz.map(work_666, SITES)
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TOTAL SCANNED WEBSITES: {Y} ({str(SCANNED)}) {END}')
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TIME TOKEN: ({str(ceil(time() - start))}) S {END}')
        #-----------------------------#
    except KeyboardInterrupt:
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} Ctrl+c pressed... exiting{END}')
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TOTAL SCANNED WEBSITES: {Y} ({str(SCANNED)}) {END}')
        print(f'{BOLD}{log}{G}[✓]~ {BOLD} TIME TOKEN: ({str(ceil(time() - start))}) S {END}')
        exit(0)
