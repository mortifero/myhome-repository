# -*- coding: utf-8 -*-
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, base64
import urlresolver
import requests
s = requests.session() 
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.fineanddandy/')
ICON = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
PATH = 'fineanddandy'
VERSION = '0.0.1'
BASEURL = 'http://www.mydownloadtube.com/'
ART = ADDON_PATH + "resources/icons/"

def Main_menu():
    Menu('[B][COLOR white]Most Popular[/COLOR][/B]',BASEURL+'movies/most_popular',5,ART + 'mostpop.jpg',FANART,'')
    Menu('[B][COLOR white]Recently Added[/COLOR][/B]',BASEURL+'movies/recent',5,ART + 'recent.jpg',FANART,'')
    Menu('[B][COLOR white]Most Downloaded[/COLOR][/B]',BASEURL+'movies/most_download',5,ART + 'mostdown.jpg',FANART,'')
    Menu('[B][COLOR white]All Movies[/COLOR][/B]',BASEURL+'movies/all',5,ART + 'allmovies.jpg',FANART,'')
    Menu('[B][COLOR white]Animation Movies[/COLOR][/B]',BASEURL+'genres/movies/animation',5,ART + 'animate.jpg',FANART,'')
    Menu('[B][COLOR white]Genres[/COLOR][/B]','',3,ART + 'genres.jpg',FANART,'')
    Menu('[B][COLOR white]Search[/COLOR][/B]','url',6,ART + 'search.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')


def Get_Genres():
    OPEN = Open_Url('http://www.mydownloadtube.com/')
    Regex = re.compile('>Hollywood Movies</a>(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('href="(.+?)">(.+?)</a>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            Menu('[B][COLOR white]%s[/COLOR][/B]' %name,url,5,ART + 'genres.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')


def Get_content(url):
    referer = url
    headers = {'Host': 'www.mydownloadtube.com', 'User-Agent': User_Agent, 'Referer': referer}
    OPEN = Open_Url(url)
    Regex = re.compile('<ul class="pop-lists pop">(.+?)</ul>',re.DOTALL).findall(OPEN)[0]
    Regex = Regex.replace('\r','').replace('\n','').replace('\t','')
    Regex2 = re.compile('<li><a href="(.+?)"  class="movie_poster_imagedisplay"><img .+? src="(.+?)" alt="(.+?)" /></a>').findall(str(Regex))
    for url,icon,name in Regex2:
            name = name.replace('Free Download','').replace('\\','').replace('poster','')
            icon = icon.replace('listing_thumb','detail_page_poster')
            icon = icon + '|' + urllib.urlencode(headers)
            Menu('[B][COLOR white]%s[/COLOR][/B]' %name,BASEURL+url,10,icon,FANART,'')

    np = re.compile('<a rel="(.+?)" href="(.+?)"',re.DOTALL).findall(OPEN)
    for name,url in np:
            if 'next' in name:
                    Menu('[B][COLOR blue]Next Page>>>[/COLOR][/B]',url,5,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')


def Get_links(name,url,iconimage):
    nono = name.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
    nono2 = name.partition('(')[0].replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
    OPEN = Open_Url(url)
    Regex = re.compile("'Downloads-Server', '(.+?)'.+?>(.+?)</a>.+?value=\"(.+?)\"",re.DOTALL).findall(OPEN)
    for name2, name3, url in Regex:
            name2 = name2.replace('b - Bit - ','').replace('c - Bit - ','').replace('d - Bit - ','').replace('e - Bit - ','').replace('Download Server (factory)','FileFactory').strip()
            name3 = name3.replace('\n','').replace('\t','').replace(nono,'').replace(nono2,'').replace('-','[COLOR red]|[/COLOR]')
            if 'Movie Promo Host' not in name2:
                    if 'Multi' not in name2:
                            Play('[B][COLOR red]%s [/COLOR][COLOR white]%s[/COLOR][/B]' %(name2,name3),url,100,iconimage,FANART,name)
    for name4, name5, url in Regex:
            name5 = name5.replace('\n','').replace('\t','').replace(nono,'').replace(nono2,'').replace('-','[COLOR red]|[/COLOR]')
            if 'Multi' in name4:
                    Menu('[B][COLOR red]Click Here For Multi Debrid [COLOR white]%s[/COLOR] Links[/COLOR][/B]' %name5,url,11,iconimage,FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')


def Get_multi_links(name,url,iconimage,description):
        name = description
        if 'bit.ly' in url:
                headers = {'User-Agent': User_Agent}
                r = requests.get(url,headers=headers,allow_redirects=False)
                url = r.headers['location']
        OPEN = Open_Url(url)
        Regex = re.compile('nameHost="(.+?)".+?validity=(.+?)dateLastChecked=.+?href="(.+?)"',re.DOTALL).findall(OPEN)
        for name2, validity, url in Regex:
                if 'invalid' not in validity:
                        if urlresolver.HostedMediaFile(url):
                                Play('[B][COLOR red]%s[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)


def Search():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','%20')
                url = BASEURL + '/search/movies/' + search
                Get_content(url)
    

########################################


def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link


def Menu(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        

		
def Play(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
		
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def resolve(name,url,iconimage,description):
    name = description
    if 'bit.ly' in url:
            headers = {'User-Agent': User_Agent}
            r = requests.get(url,headers=headers,allow_redirects=False)
            url = r.headers['location'] 
    if 'adf.ly' in url:
            adfly_data = requests.get(url).content
            ysmm = adfly_data.split("ysmm = \'")[1].split("\';")[0]
            url = crack(ysmm)
    xbmc.executebuiltin("XBMC.Notification([COLOR orange]Attempting To[/COLOR],[COLOR green]Resolve Link[/COLOR] ,3000)")
    play=urlresolver.resolve(url)
    try: 
            liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
            liz.setInfo(type='Video', infoLabels={'Title': name, 'Plot': description})
            liz.setProperty('IsPlayable','true')
            xbmc.Player().play(play,liz)
    except:
        play=xbmc.Player(GetPlayerCore())
        play.play(str(url),liz)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def crack(code):
        #Function written by D4Vinci
        zeros = ''
        ones = ''
        for n,letter in enumerate(code):
                if n%2 == 0:
                        zeros += code[n]
                else:
                        ones =code[n] + ones
        key = zeros + ones
        key = base64.b64decode(key.encode("utf-8"))
        return key[2:]
		


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
#########################################################
	
if mode == None: Main_menu()
elif mode == 3: Get_Genres()
elif mode == 5 : Get_content(url)
#elif mode == 8 : Genre_content(url)
elif mode == 6 : Search()
elif mode == 10 : Get_links(name,url,iconimage)
elif mode == 11 : Get_multi_links(name,url,iconimage,description)
elif mode == 100 : resolve(name,url,iconimage,description)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
