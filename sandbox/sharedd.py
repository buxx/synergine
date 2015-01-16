from multiprocessing import Process, Pipe#, Manager
from multiprocessing.connection import wait
import os


def start_in_oneshot_processes(obj, nb_process):
    """
    Start nb_process processes to do the job. Then process finish the job they die.
    """
    processes = []
    for i in range(nb_process):
        #  Simple process style
        p = Process(target=oneshot_in_process, args=(obj,))
        p.start()
        processes.append(p)

    for process in processes:
        # Wait all process finish
        process.join()

def oneshot_in_process(obj):
    """
    Main job (don't matter if in oneshot, keeped alive process. It have job to do)
    """
    print('p', obj, os.getpid())


def start_in_keepedalive_processes(obj, nb_process):
    """
    Start nb_process and keep them alive. Send job to them multiple times, then close thems.
    """
    processes = []
    readers_pipes = []
    writers_pipes = []
    for i in range(nb_process):
        # Start process with Pipes for communicate
        local_read_pipe, local_write_pipe = Pipe(duplex=False)
        process_read_pipe, process_write_pipe = Pipe(duplex=False)
        readers_pipes.append(local_read_pipe)
        writers_pipes.append(process_write_pipe)
        p = Process(target=run_keepedalive_process, args=(local_write_pipe, process_read_pipe, obj))
        p.start()
        processes.append(p)
    # Send to process some job to do
    for job in range(3):
        print('send new job to processes:')
        for process_number in range(nb_process):
            # Send data to process
            writers_pipes[process_number].send(obj)
            reader_useds = []
        # Wait response from processes
        while readers_pipes:
            for r in wait(readers_pipes):
                try:
                    r.recv()
                except EOFError:
                    pass
                finally:
                    reader_useds.append(r)
                    readers_pipes.remove(r)
        readers_pipes = reader_useds

    # Kill processes
    for writer_pipe in writers_pipes:
        writer_pipe.send('stop')

def run_keepedalive_process(main_write_pipe, process_read_pipe, obj):
    """
    Procees who don't finish while job to do
    """
    while obj != 'stop':
        oneshot_in_process(obj)
        # Send to main process "I've done my job"
        main_write_pipe.send('job is done')
        # Wait for new job to do (this part can be simplified no ?)
        readers = [process_read_pipe]
        while readers:
            for r in wait(readers):
                try:
                    obj = r.recv()
                except EOFError:
                    pass
                finally:
                    readers.remove(r)


obj = object()
print('m', obj, os.getpid())

print('One shot processes:')
start_in_oneshot_processes(obj, 5)

print('Keeped alive processes:')
start_in_keepedalive_processes(obj, 5)

print('f', obj, os.getpid())