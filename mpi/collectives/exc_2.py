from mpi4py import MPI
from sys import stdout
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



assert size == 4, 'Number of MPI tasks has to be 4.'

#if rank == 0:
    #print('Broadcast:')

## Simple broadcast
#if rank == 0:
    #data = np.arange(8)
#else:
    #data = np.empty(8, int)
#comm.Bcast(data, root=0)
#comm.barrier()
#print('  Task {0}: {1}'.format(rank, data))

# Prepare data vectors ..
data = np.arange(rank*8, 8+8*rank, dtype=int)  # TODO: create the data vectors
# .. and receive buffers
buff = np.full(8, -1, int)

#buff = np.zeros(8, int)
#buff[:] = -1

# ... wait for every rank to finish ...

stdout.flush()
comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Data vectors:')
print('  Task {0}: {1}'.format(rank, data))
stdout.flush()
comm.barrier()

#if rank == 0:
    #print('')
    #print('Scatter:')

## TODO: how to get the desired receive buffer using a single collective
##       communication routine?
#comm.Scatter(data, buff, root=0)

#print('  Task {0}: {1}'.format(rank, buff))
#buff[:] = -1
#stdout.flush()
#comm.barrier()

#if rank == 0:
    #print('')
    #print('Gather:')
#comm.Gather(data[:2], buff, root=1)

#print('  Task {0}: {1}'.format(rank, buff))

#buff[:] = -1
#stdout.flush()
#comm.barrier()

if rank == 0:
    print('')
    print('Reduce:')

#color = rank//2
subcomm = comm.Split(color)
subcomm.Reduce(data, buff, op=MPI.SUM, root=0)

print('  Task {0}: {1}'.format(rank, buff))
stdout.flush()
comm.barrier()
print("color: {0}".format(color))