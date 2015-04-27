import sys

if sys.version_info < (3, 3):
    sys.stdout.write("Python 3.3 required\n")
    sys.exit(1)

from multiprocessing import Process, Pipe
from multiprocessing.connection import wait


def chunk(seq, m):
    i, j, x = len(seq), 0, []
    for k in range(m):
        a, j = j, j + (i + k) // m
        x.append(seq[a:j])
    return x


class PipePackage():
    def __init__(self):
        self._current_process_id = None
        self._count_processes = 0

    def setCurrentProcessId(self, current_process_id):
        self._current_process_id = current_process_id

    def setCountProcess(self, count):
        self._count_processes = count


class KeepedAliveProcessManager():
    def __init__(self, nb_process, target):
        self.processs = []
        self.target = target
        self.nb_process = nb_process
        self.readers_pipes = []
        self.writers_pipes = []

    def _start(self, pipe_package):
        pipe_package.setCountProcess(self.nb_process)
        for i in range(self.nb_process):
            local_read_pipe, local_write_pipe = Pipe(duplex=False)
            process_read_pipe, process_write_pipe = Pipe(duplex=False)
            self.readers_pipes.append(local_read_pipe)
            self.writers_pipes.append(process_write_pipe)
            pipe_package.setCurrentProcessId(i)
            p = Process(target=run_keeped_process,
                        args=(self.target, local_write_pipe, process_read_pipe, pipe_package))
            p.start()
            self.processs.append(p)
            local_write_pipe.close()
            process_read_pipe.close()

    def stop(self):
        for writer_pipe in self.writers_pipes:
            writer_pipe.send('stop')

    def get_their_work(self, pipe_package):
        if not self.processs:
            self._start(pipe_package)
        else:
            for i in range(self.nb_process):
                # print('send things')
                pipe_package.setCurrentProcessId(i)
                self.writers_pipes[i].send(pipe_package)
        things_done_collection = []
        reader_useds = []
        while self.readers_pipes:
            for r in wait(self.readers_pipes):
                try:
                    things_dones = r.recv()
                except EOFError:
                    reader_useds.append(r)
                    self.readers_pipes.remove(r)
                else:
                    reader_useds.append(r)
                    self.readers_pipes.remove(r)
                    for thing_done in things_dones:
                        things_done_collection.append(thing_done)

        self.readers_pipes = reader_useds
        return things_done_collection


def run_keeped_process(target, main_write_pipe, process_read_pipe, new_things):
    while new_things != 'stop':
        things_dones = target(new_things)
        main_write_pipe.send(things_dones)
        readers = [process_read_pipe]
        while readers:
            for r in wait(readers):
                try:
                    new_things = r.recv()
                except EOFError:
                    pass
                finally:
                    readers.remove(r)

                    # if new_things != 'stop':
                    # run_keeped_process(target, main_write_pipe, process_read_pipe, new_things)
