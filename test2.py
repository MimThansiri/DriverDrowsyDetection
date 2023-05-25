from ultralytics.yolo.engine.model import YOLO
import cv2
  
model = YOLO("best_50.pt")
results = model.predict(source='0', show=False, stream=True, save=False) # source already setup
names = model.names

output_file = "output.mp4"
codec = cv2.VideoWriter_fourcc(*"mp4v")
frame_rate = 24
resolution = (640, 480)

# Create a VideoWriter object
video_writer = cv2.VideoWriter(output_file, codec, frame_rate, resolution)

cnt = 0
for r in results:
    detected = False
    decide = "Awake"
    for c in r.boxes.cls:
        if detected == False:
            if 'close_eye' in names[int(c)]:
                if cnt < 5:
                    cnt += 1
                    detected = True
            elif 'yawn' in names[int(c)]:
                if cnt < 5:
                    cnt += 1
                    detected = True
            elif 'open_eye' in names[int(c)]:
                cnt = 0
                detected = True
    
    if cnt >= 5:
        decide = 'Drowsy'
    else:
        decide = 'Awake'
    frame = r.plot()
    cv2.putText(frame, decide, (350, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    cv2.imshow("scene",frame)
    video_writer.write(frame)

video_writer.release()
cv2.destroyAllWindows()