from flask import Flask, redirect, url_for, request,Response
from flask import render_template
from threading import Condition
import cv2
import io
import vehicleControl

app = Flask(__name__)
vc = cv2.VideoCapture(0)

def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = vc.read()
        cv2.imwrite('stream_frame.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def mainpage():
    vehicleControl.steadyState()
    return render_template('index.html')
@app.route('/moveRequest',methods = ['POST'])
def success():
    data = request.form
    if data is not None:
        if data.get('data_container') == "up":
            vehicleControl.moveForward()
            print("Go up")
        elif data.get('data_container') == "down":
            vehicleControl.moveBackward()
            print("Go down")
        elif data.get('data_container') == "right":
            vehicleControl.moveRight()
            print("Go right")
        elif data.get('data_container') == "left":
            vehicleControl.moveLeft()
            print("Go left")
        else:
            print("Idle")
            vehicleControl.steadyState()
    return 'received'
app.run(debug = False)
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5500)