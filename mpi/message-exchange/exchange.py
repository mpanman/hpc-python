from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Simple message exchange
meta = {'rank' : rank}

if rank == 0:
    comm.send(meta, dest=1)
    msg = comm.recv(source=1)
elif rank == 1:
    msg = comm.recv(source=0)
    comm.send(meta, dest=0)
print("Rank %d received a message from rank %d." % (rank, msg['rank']))

# Simple message exchange using numpy arrays
n = 100000
data = np.full(n, rank, int)
buff = np.empty(n, int)

if rank == 0:
    comm.Recv(buff, source=1)
    comm.Send(data, dest=1)
elif rank == 1:
    comm.Send(data, dest=0)
    comm.Recv(buff, source=0)
print("Rank: {0}. 1st element: {1}".format(rank, buff[0]))
