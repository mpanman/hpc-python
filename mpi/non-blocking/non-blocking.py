from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

shape  = (10,)
buff = np.empty(shape, int)
data = np.full(shape, rank)

tgt=rank+1
src=rank-1
if rank==0:
    src = MPI.PROC_NULL
elif rank == size -1:
    tgt = MPI.PROC_NULL

req = []

req.append(comm.Isend(data, dest=tgt))
req.append(comm.Irecv(buff, source=src))
### Doesn't exist
#req(comm.Isendrecv(data, dest=tgt, recvbuf=buff, source=src))
###
MPI.Request.waitall(req)

print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))  if rank!=size-1 else None
print("  Rank %d: received a message from rank %d." % (rank, src)) if rank!=0 else None
print("  Rank %d: received an array filled with %d\'s." % (rank, buff[0])) if rank!=0 else None