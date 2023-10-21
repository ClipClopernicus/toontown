import sys
import time
import msvcrt
def main():
    import sys
    import time
    import msvcrt
def print_slow(text):
        punctuation_marks = [".", "!", "?"]
        speedup_key_pressed = False
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char in punctuation_marks:
                time.sleep(0.27)
            elif char == ",":
                time.sleep(0.18)     
            
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\r':
                    speedup_key_pressed = True
            if speedup_key_pressed:
                time.sleep(0.0009)
            else:
                time.sleep(.03)        
        print()    
    
def print_medium(text):
        punctuation_marks = [".", "!", "?"]
        speedup_key_pressed = False
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char in punctuation_marks:
                time.sleep(.1)
            elif char == ",":
                time.sleep(0.05)
            
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\r':
                    speedup_key_pressed = True
            if speedup_key_pressed:
                time.sleep(0.0009)
            else:
                time.sleep(.018)
        print()    
        
if __name__ == "__main__":
    main()
