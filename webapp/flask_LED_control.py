#      flask를 이용해 웹사이트에서 라즈베리파이의 LED를 제어하는 코드
#
from flask import Flask     # flask 모듈을 불러움
import RPi.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴

GPIO.setwarnings(False)     #경고 메세지 무시해1414

GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

LED_red_pin = 14                     # LED 핀은 라즈베리파이 GPIO 14번핀으로 
LED_green_pin = 15                     # LED 핀은 라즈베리파이 GPIO 15번핀으로 
LED_blue_pin = 18                     # LED 핀은 라즈베리파이 GPIO 18번핀으로 
GPIO.setup(LED_red_pin, GPIO.OUT)   # LED 핀을 출력으로 설정
GPIO.setup(LED_green_pin, GPIO.OUT)   # LED 핀을 출력으로 설정
GPIO.setup(LED_blue_pin, GPIO.OUT)   # LED 핀을 출력으로 설정
app = Flask(__name__)       # Flask라는 이름의 객체 생성

@app.route('/')             # 기본 주소
def hello():                # 해당 주소에서 실행되는 함수 정의
   return "LED 제어를 위해 주소창을 변경하세요"    
   # 반드시 return이 있어야하며, 해당 값을 화면에 보여줌

@app.route('/red_on')       # IP주소:port/red_on 을 입력하면 나오는 페이지
def red_on():               # 해당 페이지의 뷰함수 정의
   GPIO.output(LED_red_pin, GPIO.HIGH)  # 빨간 LED 핀에 HIGH 신호 인가(LED 켜짐)
   return "red LED on"              # 뷰함수의 리턴값

@app.route('/green_on')     # IP주소:port/green_on 을 입력하면 나오는 페이지
def green_on():             # 해당 페이지의 뷰함수 정의
   GPIO.output(LED_green_pin, GPIO.HIGH) # 초록 LED 핀에 HIGH 신호 인가(LED 켜짐)
   return "green LED on"    

@app.route('/blue_on')      
def blue_on():              
   GPIO.output(LED_blue_pin, GPIO.HIGH)
   return "blue LED on"    

@app.route('/off')          # IP주소:port/off 를 입력하면 나오는 페이지
def off():                  # 해당 페이지의 뷰함수 정의
   GPIO.output(LED_red_pin, GPIO.LOW)   # 각각의 LED핀에 LOW 신호를 인가하여 LED 끔
   GPIO.output(LED_green_pin, GPIO.LOW) 
   GPIO.output(LED_blue_pin, GPIO.LOW) 
   return "all LED off"    

@app.route('/clean_up')            
def clean_up():               
   GPIO.cleanup()
   return "clean up"    

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분
   app.run(host="0.0.0.0", port = "5000")
   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정
   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능