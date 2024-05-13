from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.behaviors import focus
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDButtonText, MDButton
from CheckingPorD import Select
from kivymd.uix.dialog import MDDialog, MDDialogButtonContainer, MDDialogSupportingText, MDDialogHeadlineText
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDockedDatePicker
import pyrebase

Window.clearcolor = (1, 0.92, .90, 0.4)
Builder.load_string(
    '''
<LogIn>:
    orientation:'vertical'
    
    Image:
        source:'images/Hospital.png'
        pos_hint:{'center_x':.5, 'center_y':0.9}
        
    Image:
        source:'images/person.png'
        pos_hint:{'center_x':.5, 'center_y':0.7}
        size_hint:None, None
        width:70
        height:60
    
    
    MDTextField:
        id:username       
        helper_text_mode:'on_focus'
        pos_hint:{'center_x':.5, 'center_y':0.5}
        size_hint:None, None
        width:300
        height:34
        MDTextFieldHintText
            text:'UserName'
        MDTextFieldHelperText:
            text:'patient name(s)'
        
    MDTextField:
        id:password      
        helper_text_mode:'on_focus'
        password:True
        pos_hint:{'center_x':.5, 'center_y':0.35}
        size_hint:None, None
        width:300
        height:34
        MDTextFieldHintText
            text:'Password'
        MDTextFieldHelperText:
            text:'patient key'
            
    MDButton:
        pos_hint:{'center_x':.5, 'center_y':0.15}
        size_hint:None, None
        width:100
        height:34
        on_release: root.credentials()
        MDButtonText:
            text:"Log In"
            
<HomeScreen>:
    orientation:'vertical'
    
    Image:
        source:'images/Hospital.png'
        pos_hint:{'center_x':.5, 'center_y':0.9}
        
    Image:
        source:'images/person.png'
        pos_hint: {'center_x': 0.2,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None
    Image:
        source:'images/menu.png'
        pos_hint: {'center_x': 0.8,'center_y': 0.8}
        width:35
        height:35
        size_hint:None, None
        
    MDLabel:
        text: 'Patient Information'
        halign:'center'
        font_size:23
        bold:True
        pos_hint: {'center_x': .5,'center_y': 0.65}

    MDCard:   
        style: "elevated"
        pos_hint: {'center_x': 0.5,'center_y': 0.4}
        elevation:12
        spacing:3
        size_hint: 0.8, 0.45        
        orientation: 'vertical'
        MDLabel:
            text: 'Patient Name'
            pos_hint: {'center_x': 0.5,'center_y': 0.8}
            size_hint: None, 0.1 
            width:200
            height:30
            halign: 'center'
            

        MDLabel:
            text: 'Gomezgani Mlowoka'
            pos_hint: {'center_x': 0.5,'center_y': 0.7}
            size_hint: None, None 
            md_bg_color: 'lightgreen'
            width:200
            height:40
            halign: 'center'
            

        MDLabel:
            text: 'Prescription'
            pos_hint: {'center_x': 0.5,'center_y': 0.6}
            size_hint: None, .1
            width:200
            height:30
            halign: 'center'

        MDLabel:
            text: 'panado, Cough stop, Chiponde'
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            size_hint: None, .2 
            md_bg_color: 'lightgreen'
            width:200
            height:30
            halign: 'center'

    MDButton:
        pos_hint: {'center_x': 0.25,'center_y': 0.1}
        on_release:root.report()
        MDButtonText:
            text: 'Report'
    MDButton:
        pos_hint: {'center_x': 0.75,'center_y': 0.1}
        on_release:root.feedback()
        MDButtonText:
            text: 'FeedBack'
            
<USERRep0tInput>:
    orientation: 'vertical'
    #md_bg_color: self.theme_cls.backgroundColor
    Image:
        source:'images/Hospital.png'
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
    Image:
        source:'images/person.png'
        pos_hint: {'center_x': 0.2,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None
    Image:
        source:'images/menu.png'
        pos_hint: {'center_x': 0.8,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None
    MDLabel:
        text: 'Patient Medical Report'
        halign:'center'
        font_size:23
        bold:True
        pos_hint: {'center_x': .5,'center_y': 0.65}


    MDTextField:
        id: field
        mode: "filled"
        pos_hint: {'center_x': .5, 'center_y': .55}
        size_hint_x: .5
        on_focus: root.show_date_picker()
        MDTextFieldHintText:
            text: "MM/DD/YYYY"
        MDTextFieldTrailingIcon:
            icon: "calendar"
        
    MDLabel:
        text:'Medical Response'
        halign:'center'
        pos_hint: {'center_x': .5, 'center_y': .45}

    MDTextField:
        id: Medical_Response
        multiline: False  # Set to True if you want multiline input
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': .5, 'center_y': .38}
        multiline:True
        size_hint_x: .8
    MDLabel:
        text:'Side Effects'
        halign:'center'
        pos_hint: {'center_x': .5, 'center_y': .3}

    MDTextField:
        id: Side_Effect
        mode: "outlined"
        pos_hint: {'center_x': .5, 'center_y': .24}
        multiline:True
        size_hint_x: .8

    MDButton:
        pos_hint: {'center_x': 0.25,'center_y': 0.1}
        on_press:root.save()
        MDButtonText:
            text: 'Save'
    MDButton:
        pos_hint: {'center_x': 0.75,'center_y': 0.1}
        on_release:root.clear()
        MDButtonText:
            text: 'Clear'
            
<DoctorReport>
    name:'DoctorReport'
    orientation: 'vertical'
    Image:
        source:'images/Hospital.png'
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
    Image:
        source:'images/person.png'
        pos_hint: {'center_x': 0.2,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None
    Image:
        source:'images/menu.png'
        pos_hint: {'center_x': 0.8,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None
    MDLabel:
        text: 'Doctor Report'
        halign:'center'
        font_size:15
        bold:True
        pos_hint: {'center_x': .5,'center_y': 0.75}


    MDTextField:
        id: field
        mode: "filled"
        pos_hint: {'center_x': .5, 'center_y': .67}
        size_hint: None, None
        width:250
        height: dp(12)
        on_focus: app.show_date_picker(self.focus)
        MDTextFieldHintText:
            text: "Date"
        MDTextFieldTrailingIcon:
            icon: "calendar"
    
    MDCard:
        mode:'elevated'
        size_hint:0.9, 0.2
        pos_hint: {'center_x': .5, 'center_y': .5}
        MDLabel:
            text:'Doctor Remarks'
            md_bg_color:'lightgreen'
            halign:'center'
            pos_hint: {'center_x': .5, 'center_y': .9}
            size_hint_y:0.2
            size_hint_x:None
            width:200
    
    MDCard:
        mode:'elevated'
        size_hint:0.9, 0.2
        pos_hint: {'center_x': .5, 'center_y': .25}
        MDLabel:
            text:'Doctor Checkup Remarks'
            halign:'center'
            pos_hint: {'center_x': .5, 'center_y': .9}
            md_bg_color:'lightgreen'
            size_hint_y:0.2
            size_hint_x:None
            width:200
    MDButton:
        pos_hint: {'center_x': 0.5,'center_y': 0.09}
        on_release:root.home()
        MDButtonText:
            text: 'Back'
            
<AfterSave>
    name:'AfterSave'
    orientation: 'vertical'
    Image:
        source:'images/Hospital.png'
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
    Image:
        source:'images/person.png'
        pos_hint: {'center_x': 0.2,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None
    Image:
        source:'images/menu.png'
        pos_hint: {'center_x': 0.8,'center_y': 0.8}
        width:40
        height:40
        size_hint:None, None


    MDCard:
        style:'elevated'
        elevation:12
        md_bg_color: "cyan"
        size_hint:None, None
        width:200
        height:100
        pos_hint: {'center_x': .5, 'center_y': .5}
        MDLabel:
            text:'Saved'
            font_size:40
            bold:True
            color:'green'
            halign:'center'
            pos_hint: {'center_x': .5, 'center_y': .5}

    MDButton:
        mode:'elevation'
        pos_hint: {'center_x': .5, 'center_y': .1}
        on_press:root.manager.current='home_screen'
        MDButtonText:
            text:'Ok'


# <WrongInputs>
#     name:'AfterSave'
#     orientation: 'vertical'
#     Image:
#         source:'images/Hospital.png'
#         pos_hint: {'center_x': 0.5,'center_y': 0.9}
#     Image:
#         source:'images/person.png'
#         pos_hint: {'center_x': 0.2,'center_y': 0.8}
#         width:40
#         height:40
#         size_hint:None, None
#     Image:
#         source:'images/menu.png'
#         pos_hint: {'center_x': 0.8,'center_y': 0.8}
#         width:40
#         height:40
#         size_hint:None, None
# 
# 
#     MDCard:
#         style:'elevated'
#         elevation:12
#         md_bg_color: "cyan"
#         size_hint:None, None
#         width:200
#         height:100
#         pos_hint: {'center_x': .5, 'center_y': .5}
#         MDLabel:
#             text:'Wrong username or Password'
#             font_size:40
#             bold:False
#             color:'red'
#             halign:'center'
#             pos_hint: {'center_x': .5, 'center_y': .5}
#   
#     MDButton:
#         mode:'elevation'
#         pos_hint: {'center_x': .5, 'center_y': .1}
#         on_press:root.manager.current='log_in'
#         MDButtonText:
#             text:'Ok'



<MenuWindow>:
    name:'MenuWindow'
    orientation: 'vertical'
    Image:
        source:'Images/Hospital.png'
        pos_hint:{'center_x':0.5, 'center_y':0.9}

    Image:
        source:'Images/Person.png'
        pos_hint:{'center_x':0.1, 'center_y':0.8}
        size_hint:None, None
        width:40
        height:40
    MDCard:
        style:'elevated'
        elevation:12
        orientation:'vertical'
        padding:20
        spacing:10
        md_bg_color:(0.97, .92, 0.90, 1)
        on_Press:
        on_release:
        pos_hint:{'center_x':0.5, 'center_y':0.4}
        size_hint:0.7, 0.6
        MDLabel:
            pos_hint:{'center_x':0.5, 'center_y':0.9}
            halign:'center'
            text:'Menu'
            bold:True
        MDLabel:
            pos_hint:{'center_x':0.5, 'center_y':0.7}
            md_bg_color:(0.97, .92, 0.90, 1)
            halign:'center'
            text:'Home'
            bold:False
        MDLabel:
            pos_hint:{'center_x':0.5, 'center_y':0.6}
            md_bg_color:(0.97, .92, 0.90, 1)
            halign:'center'
            text:'Doctor Report'
            bold:False
        MDLabel:
            pos_hint:{'center_x':0.5, 'center_y':0.5}
            md_bg_color:(0.97, .92, 0.90, 1)
            halign:'center'
            text:'My Feedbak'
            bold:False
        MDLabel:
            pos_hint:{'center_x':0.5, 'center_y':0.4}
            md_bg_color:(0.97, .92, 0.90, 1)
            halign:'center'
            text:'History'
            bold:False
        MDLabel:
            pos_hint:{'center_x':0.5, 'center_y':0.3}
            md_bg_color:(0.97, .92, 0.90, 1)
            halign:'center'
            text:'Log out'
            bold:False
    '''
)

# firebase = firebase.FirebaseApplication('https://gemin-29a4f-default-rtdb.firebaseio.com/',
#                                         None)
firebaseConfig = {
    'apiKey': "AIzaSyB67EUcK__8OigOfGime2cUnfgRU2tSDoY",
    'authDomain': "gemin-29a4f.firebaseapp.com",
    'databaseURL': "https://gemin-29a4f-default-rtdb.firebaseio.com",
    'projectId': "gemin-29a4f",
    'storageBucket': "gemin-29a4f.appspot.com",
    'messagingSenderId': "627403949390",
    'appId': "1:627403949390:web:71b2e4e8ff627963bf4a1f",
    'measurementId': "G-9RXESGFWSD"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()


class Selected(Select):
    pass


class LogIn(Screen):

    # def credentials(self):
    #     username = self.ids.username.text
    #     password = self.ids.password.text
    #     if authenticate(username, password):
    #         self.manager.current = 'home_screen'
    #     else:
    #         print('no such user')

    def credentials(self):
        try:
            self.username = self.ids.username.text
            self.password = self.ids.password.text

            user = auth.sign_in_with_email_and_password(self.username, self.password)
            if user:
                self.manager.current = 'home_screen'
        except Exception as e:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Something is Wrong.",
                    color='red',
                    halign="center",
                ),
                MDDialogSupportingText(
                    text="Wrong Username or Password.",
                    text_color='red',
                    halign="center",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(

                        MDButtonText(text="OK"),
                        style="text",
                        on_release=self.close_dialog
                    ),
                    spacing="8dp",
                ),
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class HomeScreen(Screen):
    def feedback(self):
        self.manager.current = 'user_report_input'

    def report(self):
        self.manager.current = 'doctor_report'

    def menu(self):
        self.manager.current = 'menu_window'


class DatePickerDialog:
    pass


class USERRep0tInput(Screen):
    def clear(self):
        #     self.manager.current = 'after_save'
        self.ids.Medical_Response.text=''
        self.ids.Side_Effect.text=''
    def save(self):
        #     self.manager.current = 'after_save'
        medical_responds = self.ids.Medical_Response.text
        side_effects = self.ids.Side_Effect.text

        data = {
            'responds': medical_responds,
            'side_effect': side_effects}
        db.push(data)
        self.dialog = MDDialog(
            MDDialogHeadlineText(
                text="",
                halign="center",
            ),
            MDDialogSupportingText(
                text="SAVED",
                halign="center",
            ),
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="OK"),
                    style="text",
                    on_release=self.close_dialog
                ),
                spacing="8dp",
            ),
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        self.manager.current = 'home_screen'

    def show_date_picker(self):
        if not focus:
            return
        date_dialog = MDDockedDatePicker()
        # You have to control the position of the date picker dialog yourself.
        date_dialog.open()


class DoctorReport(Screen):
    def home(self):
        self.manager.current = 'home_screen'


class AfterSave(Screen):
    pass


class MenuWindow(Screen):
    pass


class MyMDApp(MDApp):
    def on_start(self):
        MDLabel(
            text='Welcome'
        )

    def on_resume(self):
        pass

    def on_stop(self):
        pass

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Selected(name='select'))
        sm.add_widget(LogIn(name='log_in'))
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(USERRep0tInput(name='user_report_input'))
        sm.add_widget(DoctorReport(name='doctor_report'))
        sm.add_widget(AfterSave(name='after_save'))
        sm.add_widget(MenuWindow(name='menu_window'))
        return sm


MyMDApp().run()
