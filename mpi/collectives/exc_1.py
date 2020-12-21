from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('Broadcast:')

# TODO: create data vector at task 0 and send it to everyone else
#       using collective communication
if rank == 0:
    data = np.arange(8, dtype=int)
else:
    data = np.empty(8, dtype=int)

comm.Bcast(data, root=0)
print('  Task {0}: {1}'.format(rank, data))
