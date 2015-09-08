"""Rice University - Introduction to interactive programming (python)
Stopwatch: The Game - Goal of 'game' is to press the stop button on the second
ex. stopping on 11.0 would gain one point and 11.1 would count as one turn. 
Imported simplieguitk to access gui components available in codeskulptor"""

import simpleguitk as simplegui

#globals
time = 0
started = False
count = 0
hits = 0

#helper function that converts time in tenths of seconds 
#into formatted string A:BC.D
def format(t):
    a = t//600 #minutes
    b = (((t%600)/10)%60)//10 #tenths of a second
    c = (((t%600)/10)%60)%10 #remainder of tenths of a second
    d = t%10
    return str(a)+':'+str(b)+str(c) +'.'+str(d)

#Event handlers for buttons; "Start", "Stop", "Reset"
def stop_button():
    global started, time, count, hits
    if started == True:
        started = False
        timer.stop()
        count += 1
        if time%10 == 0:
            hits += 1
        
def start_button():
    global started, time, count
    started = True
    timer.start()
        
def reset():
    global started, time, count, hits
    started = False
    count = 0
    time = 0
    hits = 0
    timer.stop()

#Event handler for timer with 0.1 sec interval
def start_timer():
    global started, time
    if started == True:
        time += 1
        
#Draw handler
def draw(canvas):
    canvas.draw_text(format(time), [80, 170], 40, "Teal")
    canvas.draw_text(str(hits) +"/" + str(count), [225, 45], 20, "Magenta")
    
#Create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 300) 
timer = simplegui.create_timer(100, start_timer)

#Register event handlers
frame.set_draw_handler(draw)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Start", start_button, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
timer.start()