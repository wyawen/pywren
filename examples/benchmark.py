import numpy as np
import time
import sys
sys.path.append("../")
import pywren


MAT_N = 4096

def compute_flops(loopcount):
    
    A = np.arange(MAT_N**2, dtype=np.float64).reshape(MAT_N, MAT_N)
    B = np.arange(MAT_N**2, dtype=np.float64).reshape(MAT_N, MAT_N)

    t1 = time.time()
    for i in range(loopcount):
        c = np.sum(np.dot(A, B))

    FLOPS = 2 *  MAT_N**3 * loopcount
    t2 = time.time()
    return FLOPS / (t2-t1)


if __name__ == "__main__":
    t1 = time.time()

    LOOPCOUNT = 20
    N = 400
    iters = np.arange(N)
    
    def f(x):
        return compute_flops(LOOPCOUNT)

    futures = pywren.map(f, iters)

    print "invocation done, dur=", time.time() - t1

    result_count = 0
    while result_count < N:
        
        isdone = [f.done() for f in futures]
        result_count = np.sum(isdone)

        est_flop = 2 * result_count * LOOPCOUNT * MAT_N**3
        
        est_gflops = est_flop / 1e9/(time.time() - t1)
        print "jobs done: {:5d}    runtime: {:5.1f}s   {:8.1f} GFLOPS ".format(result_count, 
                                                                           time.time()-t1, 
                                                                           est_gflops)

        if result_count == N:
            break

        time.sleep(1)

    all_done = time.time()
    total_time = all_done - t1
    print "total time", total_time
    est_flop = result_count * 2 * LOOPCOUNT * MAT_N**3
    
    print est_flop / 1e9/total_time, "GFLOPS"

