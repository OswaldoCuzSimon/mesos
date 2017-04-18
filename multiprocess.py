from multiprocessing import Process
import time

def f(name):
	time.sleep(4)
	print('hello', name)

if __name__ == '__main__':
	b = Process(target=f, args=('bob',))
	p = Process(target=f, args=('patrick',))
	b.start()
	p.start()
	b.join()
	p.join()