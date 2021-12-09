import threading

def function_a():
    print('5초 간격으로 반복 실행')
    timer = threading.Timer(5, function_a)
    timer.start()

function_a()
