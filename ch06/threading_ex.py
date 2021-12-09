import threading


def repeat():
    print("3초 간격으로 반복 실행")
    timer = threading.Timer(3, repeat)
    timer.start()

repeat()