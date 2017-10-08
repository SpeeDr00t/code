# -*- coding: utf-8 -*-
#
# write by kyoung chip , jang
#
# python 3.6
# pip list
# beautifulsoup4 requests
#
# pip install bs4
# pip install requests
#
import requests
from bs4 import BeautifulSoup
 
class CHtmlParser :
 
    def __init__( self ) :
 
        self.req = ''  
 
         
         
    def login( self, url , user , passwd ) :
     
        self.req = requests.get( url , auth=(user , passwd) )
        print( self.req.text )
         
         
         
    def getHtml( self , url   ) :
 
        self.req = requests.get( url  )
         
        '''    
        print("status code %s"  % ( self.req.status_code ) )
        print("headers %s " % ( self.req.headers['content-type'] ) )
        print("encoding %s " % ( self.req.encoding ) )
        print("text %s " % ( self.req.text ) )
        print("json %s " % ( self.req.json ) )
        '''
         
        return BeautifulSoup( self.req.text, 'html.parser')   
         
                 
 
         
class CSecurityFocus :
 
    def __init__ ( self ) :
     
        self.html = CHtmlParser()
        self.response = ''
     
         
    def getHtml( self, url ) :
     
        self.response = self.html.getHtml( url )   
 
         
    def getLink( self ) :  
     
        link = self.response.select('#tabs > ul > li > a')               
         
        for keyword in link :
 
            print( str(keyword)[str(keyword).find('=')+2:str(keyword).find('">')].replace("/bid/","http://www.securityfocus.com/bid/")   )
 
 
    def getVulnInfo( self ) :  
 
        title = self.response.select('#vulnerability > span')
    
        print( str(title)[str(title).find('title">')+7:str(title).find('</span')] )
    
         
    def doWork( self ) :  
    
        self.getHtml("http://www.securityfocus.com/bid/1/info")
 
        self.getVulnInfo()
        self.getLink()     
 
         
if __name__ == '__main__':
 
    r = CSecurityFocus()
    r.doWork()


출처: http://speedr00t.tistory.com/entry/html-parser-class-security-focus-title과-link정보-가져오기 [Black Falcon]