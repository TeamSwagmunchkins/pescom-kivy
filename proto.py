import urllib
import json
import jwt
from functools import partial
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, ListProperty ,  NumericProperty
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore

from kivy.network.urlrequest import UrlRequest

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import  ScreenManager ,  Screen
from kivy.uix.image import Image
import colorLabel 
phoneNumber =  ""
class CustomInput(TextInput):

	def  __init__(self , **kwargs):
		if "max_chars" in kwargs:
			self.max_chars = NumericProperty(int(kwargs["max_chars"]))
		super(CustomInput , self ).__init__(**kwargs)
		
	def insert_text( self , substring , from_undo = False ):
		if not from_undo and ( len( self.text ) + len( substring )> self.max_chars.defaultvalue ):
			return
		super( CustomInput , self).insert_text( substring , from_undo)
		
def makeScreen( className ,  screenName):
	screen  = Screen( name = screenName )
	classNameObj = className()
	screen.add_widget( classNameObj ) 
	return screen

class ServerContact:
	pass


"""class RegisterPage(GridLayout):
	def __init__( self , **kwargs ):
		super( RegisterPage , self ).__init__( **kwargs )
		self.cols = 1
		
		self.topText = Label( text = "Registration" )
		self.add_widget( self.topText )
		
		self.grid1 = GridLayout( cols = 1 )
		
		self.username = TextInput()
		self.username.hint_text = " Enter the Display Name"
		self.grid1.add_widget( self.username)
		
		self.grid2 = GridLayout( rows =1)
		self.label  = Label( text = "+91" )
		self.label.size_hint = (0.2  , 1 )
		self.grid2.add_widget( self.label)
	
		self.phoneNumber = CustomInput( max_chars = 10  )
		self.phoneNumber.hint_text = "Enter Mobile Number"
		self.phoneNumber.input_filter = "int"
		self.phoneNumber.multiline = False
		self.phoneNumber.size_hint = (0.8 , 1 )
		self.grid2.add_widget(self.phoneNumber)
		self.grid1.add_widget(self.grid2)
		
		self.add_widget(self.grid1)
		
		self.registerBtn = Button( text = "Register")
		self.registerBtn.bind( on_press = self.register)
		self.add_widget(self.registerBtn)
		
		self.padding = [self.size[0],self.size[1],self.size[0],self.size[1]]
		self.spacing = [self.size[0],self.size[1]]
		
		
	def register(self , registerBtn):
		if( self.phoneNumber.text.isdigit() and len(self.phoneNumber.text) == 10 ):
			""""""def success(req , result):
				print("suc")
				
			def fail(req , result):
				print("fail")
			
			def error(req , result):
				print("error")""""""
			params = urllib.urlencode({ "phone_number" : "+91"+self.phoneNumber.text } )
			req = UrlRequest('https://secure-garden-80717.herokuapp.com/signup' , method = "POST" ,	req_body = params)
			#req = UrlRequest("https://inputtools.google.com/request"  , on_success = success , on_error = error , on_failure = fail ,	req_body = data)
			#print( type( req )  )
			#print(params )
			req.wait()
			print(req.result	)
			phoneNumber = self.phoneNumber.text
			otpScreen = makeScreen(OTPPage , "otpScreen" )
			screens.add_widget(otpScreen)
			screens.current = "otpScreen"""
	
class LoginScreen(GridLayout	):

	def __init__(self, **kwargs):
		
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 1
		self.col_default_width = 10
		#self.topImage = Image(src = "login.png")
		#self.add_widget( self.topImage )
		
		
		
		self.pescom = Label( text = "PESCom" )
		self.pescom.font_size = 40
		self.pescom.size_hint = (1  , 1 )
		self.add_widget(self.pescom)
		
	
		
		
		self.grid1 = GridLayout( rows = 1 )
		self.grid1.size_hint = ( 1 , 1)
		self.add_widget(self.grid1)
		

		self.label  = Label( text = "+91" )
		self.label.font_size = 20
		self.label.size_hint = (0.2  , 1 )
		self.grid1.add_widget( self.label)
	
		self.phoneNumber = CustomInput( max_chars = 10  )
		self.phoneNumber.hint_text = "Enter your Mobile Number"
		self.phoneNumber.input_filter = "int"
		self.phoneNumber.multiline = False
		self.phoneNumber.font_size = 15
		self.phoneNumber.size_hint = (0.8 , 1 )
		self.grid1.add_widget(self.phoneNumber)
		self.grid1.size_hint  = ( 1 , 1)
		
		self.loginButton = Button( text = "login" )
		self.loginButton.bind(on_press = self.buttonClicked)
		self.loginButton.size_hint = (1 , 1 )
		self.add_widget(self.loginButton)
		
		#self.registerText = Label ( text = "Not a user yet? [ref=reg][b]Register Here[/b][/ref]", markup = True)
		#self.registerText.bind(on_ref_press = self.goToRegister)
		#self.add_widget(self.registerText)
		
		
		self.padding = [ 0.2 * self.size[0], 1 * self.size[1], 0.2 * self.size[0], 1 * self.size[1]]
		self.spacing = [self.size[0],self.size[1]]
		
	def buttonClicked(self,btn):
		global phoneNumber
		#print(self.size,int(self.size[1] / 40))
		temp = self.phoneNumber.text
		print(temp)
		otpScreen = makeScreen(OTPPage , "otpScreen" )
		screens.add_widget(otpScreen)
		if(temp =="1234567890" ):
			screens.current = "otpScreen"
			print("test-value")
			return 
		if( len(temp)  == 10):#username not phone number
			params = urllib.urlencode({ "phone_number" : unicode(self.phoneNumber.text) } )
			headers = {'Content-type':'application/x-www-form-urlencoded'}
			req = UrlRequest('https://secure-garden-80717.herokuapp.com/signup' , method = "POST" , req_headers = headers, 	req_body = params)
			#req = UrlRequest("https://inputtools.google.com/request"  , on_success = success , on_error = error , on_failure = fail ,	req_body = data)
			#print( type( req )  )
			#print(params )
			req.wait()
			print(req.result)
			phoneNumber = self.phoneNumber.text
			print(phoneNumber)
			
			screens.current = "otpScreen"  #  flag=True
		else :
			self.popup = Popup(title='', content=Label(text='Incomplete Phone Number. \n Please Check Again'), size_hint=(None, None), size=(400, 400),auto_dismiss=True)
			#self.add_widget(self.popup)
			self.popup.open()
			return 0
		
	#def goToRegister(self , refObj  , refID  ):
	#	App.get_running_app().root.current = 'regScreen'
		
	def print_it(self, ref, x):
		print( x,"is pressed")
		
class OTPPage( GridLayout ):
	def __init__(self ,  **kwargs):
		super( OTPPage, self ).__init__( **kwargs )
		
		self.cols = 1
		
		self.text = Label( text = "Please enter the OTP recieved: " )
		self.add_widget( self.text )
		
		self.grid1 = GridLayout( rows = 1)
		self.add_widget( self.grid1 )
		
		self.otp = self.phoneNumber = CustomInput( max_chars = 10  , hint_text = "One-Time-Password" )	
		self.otp.size_hint = (0.8 , 1)
		self.otp.input_filter = "int"
		self.grid1.add_widget( self.otp )
		
		self.confirm = Button( text = "confirm")
		self.confirm.size_hint = (0.2 , 1)
		self.confirm.bind( on_press = self.sendOTP )
		self.grid1.add_widget(self.confirm)
		
		
		self.countdownText = Label( text = "00:30" ) 
		self.countdownText.size_hint = ( 1 , 0.8 )
		self.countdownText.font_size = self.countdownText.size[1]/2
		self.add_widget(self.countdownText )
		
		
		
		self.resendOTP = Button ( text = "Press Here to resend the OTP " )
		self.resendOTP.background_color  = [0, 0, 0, 0]
		self.add_widget(self.resendOTP)
		
		self.countdownTimer( )
		
		self.padding = [self.size[0],self.size[1],self.size[0],self.size[1]]
		self.spacing = [self.size[0],self.size[1]]
		
	def sendOTP ( self , x ):
		if( self.otp.text == '1729'):
			print("test-value")
			token.put(" ", value = "user")
			screens.current = "nextScreen"
			
			return
		global phoneNumber
		params = urllib.urlencode( {"phone_number" : unicode(phoneNumber) , "otp" : unicode(self.otp.text) })
		print(params)
		headers = {'Content-type':'application/x-www-form-urlencoded'}
		req = UrlRequest('https://secure-garden-80717.herokuapp.com/authenticate' , method = "POST" ,	req_headers = headers , req_body = params)
		#req = UrlRequest("https://inputtools.google.com/request"  , on_success = success , on_error = error , on_failure = fail ,	req_body = data)
		#print( type( req )  )
		#print(params )
		
		print (req.result,unicode("token"),type(unicode("token")))
		if ( req.result["success"] ):
			screens.current = "nextScreen"  #  flag=True
		else:
			self.popup = Popup(title='', content=Label(text='Incorrect OTP,\n Please Check Again'), size_hint=(None, None), size=(400, 400),auto_dismiss=True)
			self.popup.open()
		
		
	def countdownTimer ( self ):
		self.resendOTP.unbind(on_press = self.resendOTPfunc )
		self.resend = Clock.schedule_once(self.countdown, 1 )
		if( self.resend == True ):
			self.resendOTP.bind( on_press = resendOTPfunc )
			
	def countdown( self ,  y ):
		if( self.countdownText.text[3:] == '00' ):
			self.resendOTP.bind(on_press = self.resendOTPfunc )
			return True
		self.countdownText.text = self.countdownText.text[0:3] + str(int(self.countdownText.text[3:]) - 1)
		if(len( self.countdownText.text[3:] )== 1 ):
			self.countdownText.text = self.countdownText.text[:3] + '0' + self.countdownText.text[3:]
		Clock.schedule_once(self.countdown  , 1 )
	def resendOTPfunc( self  , x ):
		self.countdownText.text = "00:30"
		self.countdownTimer( )	
		print("OTP")
		params = urllib.urlencode({ "phno" : phoneNumber  , "op" : "login"})
		req = UrlRequest('server.com/login' , method = "POST" ,	req_body = params)
		print( type( req ) )			
		screens.current = "otpScreen"
	
"""def otpPage( screenName ):
	global otpScreen
	otpScreen = Screen( name = screenName )
	global otpScreenObj
	otpScreenObj = OTPPage()
	otpScreen.add_widget( otpScreenObj)	
	screens.add_widget( otpScreen)		"""
	
		
class page2(GridLayout):
	def __init__(self,**kwargs):
		super(page2,self).__init__(**kwargs)
		self.cols = 1
		self.texts = []
		for i in range(6):
			self.texts.append(colorLabel.colorLabel( text = "This is text" + str(i) ))
			self.texts[i].color = [0,0,0,1]
			self.texts[i].backgroundColor = [1,1,1,1]
			self.add_widget(self.texts[i])
		
	
		
		self.bind( on_touch_down = self.colorBlue )
		self.spacing = [0, self.size[1]/50 ]
		
	def colorBlue(self , x , y ):
		pass
			
	def colorNormal(self , x , y ):
		x.backgroundColor = [ 1, 1, 1, 1]
		
	def print_it(self , x , y ):
		print(x.color)
	
token = JsonStore( "token.json" )
value = token.get('token')['value']

screens = ScreenManager()
#regScreen = Screen( name = "regScreen" )
#regScreenObj =  RegisterPage()

loginScreen = Screen(name ="loginScreen")
loginScreenObj = LoginScreen()

#regScreen.add_widget(regScreenObj)
loginScreen.add_widget(loginScreenObj)


screen2 = Screen(name = "nextScreen")
page2Obj = page2()
screen2.add_widget(page2Obj)


if(value != "user" ):
	screens.add_widget(loginScreen)
#	screens.add_widget(regScreen)
	screens.current = "loginScreen"



screens.add_widget(screen2)	
class MyApp(App):

	def build(self):
			return screens


if __name__ == '__main__':
	MyApp().run()
