import sys

if sys.version_info < (3, 3):
  sys.stdout.write("Python 3.3 required\n")
  sys.exit(1)

from multiprocessing import Process, Pipe
from multiprocessing.connection import wait

def chunk(seq,m):
   i,j,x=len(seq),0,[]
   for k in range(m):
     a, j = j, j + (i+k)//m
     x.append(seq[a:j])
   return x

class ProcessManager(object):
  
  def __init__(self, nb_process, target):
    self.target = target
    self.nb_process = nb_process
    self.readers_pipes = []
    
  def _start(self, chunked_things):
    self.readers_pipes = []
    for i in range(self.nb_process):
      local_read_pipe, local_write_pipe = Pipe(duplex=False)
      self.readers_pipes.append(local_read_pipe)
      p = Process(target=run_process, args=(self.target, local_write_pipe, chunked_things[i]))
      p.start()
      local_write_pipe.close()
  
  def get_their_work(self, things_to_do):
    chunked_things = chunk(things_to_do, self.nb_process)
    self._start(chunked_things)
    things_done_collection = []
    while self.readers_pipes:
      for r in wait(self.readers_pipes):
        try:
          things_dones = r.recv()
        except EOFError:
          self.readers_pipes.remove(r)
        else:
          self.readers_pipes.remove(r)
          things_done_collection.append(things_dones)
    return things_done_collection


class KeepedAliveProcessManager(object):
  
  def __init__(self, nb_process, target):
    self.processs = []
    self.target = target
    self.nb_process = nb_process
    self.readers_pipes = []
    self.writers_pipes = []
    
  def _start(self, chunked_things):
    for i in range(self.nb_process):
      local_read_pipe, local_write_pipe = Pipe(duplex=False)
      process_read_pipe, process_write_pipe = Pipe(duplex=False)
      self.readers_pipes.append(local_read_pipe)
      self.writers_pipes.append(process_write_pipe)
      p = Process(target=run_keeped_process, args=(self.target, local_write_pipe, process_read_pipe, chunked_things[i]))
      p.start()
      self.processs.append(p)
      local_write_pipe.close()
      process_read_pipe.close()
      
  def stop(self):
    for writer_pipe in self.writers_pipes:
      writer_pipe.send('stop')
      
  def get_their_work(self, things_to_do):
    chunked_things = chunk(things_to_do, self.nb_process)
    if not self.processs:
      self._start(chunked_things)
    else:
      for i in range(self.nb_process):
        #print('send things')
        self.writers_pipes[i].send(chunked_things[i])
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
          things_done_collection.append(things_dones)
    self.readers_pipes = reader_useds
    return things_done_collection

def run_keeped_process(target, main_write_pipe, process_read_pipe, things):
  things_dones = target(things)
  main_write_pipe.send(things_dones)
  del things_dones
  del things
  
  new_things = None
  readers = [process_read_pipe]
  readers_used = []
  while readers:
    for r in wait(readers):
      try:
        new_things = r.recv()
        #print('p: things received')
      except EOFError:
        pass
      finally:
        readers.remove(r)
  #print('p: continue')
  if new_things != 'stop':
    run_keeped_process(target, main_write_pipe, process_read_pipe, new_things)

def run_process(target, main_write_pipe, things):
  things_dones = target(things)
  main_write_pipe.send(things_dones)
