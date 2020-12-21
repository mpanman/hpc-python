from mpi4py import MPI
import numpy as np
from sys import stdout

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

shape  = (10,)
buff = np.empty(shape, int)

data = np.full(shape, rank)

if False:
    if myid==0:
        comm.Send(data, dest=myid+1)
        print("{0} sending: {1}".format(myid, len(data)))
    elif myid<ntasks and myid!=0:
        comm.Send(data, dest=myid+1)
        print("{0} sending: {1}".format(myid, len(data)))
        comm.Recv(buff, source=myid-1)
        print("{0} receiving: {1}".format(myid, buff[0]))
    elif myid==ntasks:
        comm.Recv(buff, source=myid-1)
        print("{0} receiving: {1}".format(myid, buff[0]))


tgt = rank + 1
src = rank - 1
if False:
    if rank==0:
        comm.Send(data, dest=tgt)
        print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))
    elif rank == size -1:
        comm.Recv(buff, source=src)
        print("  Rank %d: received a message from rank %d." % (rank, src))
        print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))
    else:
        comm.Sendrecv(data, recvbuf=buff, source=src, dest=tgt)
        print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))
        print("  Rank %d: received a message from rank %d." % (rank, src))
        print("  Rank %d: received an array filled with %ds." % (rank, buff[0]))

if True:
    if rank==0:
        src = MPI.PROC_NULL
    elif rank == size -1:
        tgt = MPI.PROC_NULL

    comm.Sendrecv(data, recvbuf=buff, source=src, dest=tgt)
    print("  Rank %d: sent %d elements to rank %d." % (rank, len(data), tgt))  if rank!=size-1 else None
    print("  Rank %d: received a message from rank %d." % (rank, src)) if rank!=0 else None
    print("  Rank %d: received an array filled with %d\'s." % (rank, buff[0])) if rank!=0 else None

# ... wait for every rank to finish ...
stdout.flush()
comm.barrier()
if rank == 0:
    print("")
    print("Sendrecv (in the middle of the chain):")