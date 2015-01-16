from multiprocessing import Process, Manager, Pipe
import os

def do_in_process(objects, process_number, pipe):
    print(process_number, objects, os.getpid())
    pipe.send('ok: '+str(os.getpid()))
    pipe.close()

if __name__ == '__main__':
    manager = Manager()
    objects = []
    for i in range(20):
        objects.append(object())

    # Create 4 processes
    print('Prepare processes')
    processes = []
    for process_number in range(4):
        shared_objects = manager.list(objects[process_number:process_number+4])
        print(process_number, shared_objects)
        parent_conn, child_conn = Pipe()
        process = Process(target=do_in_process, args=(shared_objects, process_number, child_conn))
        processes.append((process, parent_conn))

    print('start processes')
    for process in processes:
        process[0].start()

    for process in processes:
        print(process[1].recv())
        process[0].join()

    print('finish')
