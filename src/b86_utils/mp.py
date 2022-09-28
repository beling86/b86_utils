import concurrent.futures
import time
from tqdm import tqdm
import multiprocessing

def call(fn, args, workers = 5, mode="p", wmax = False):
    """execute a function in a batch. All functions from this module starting with 
    p can be batched.

    Args:
        fn (function): function to be called
        args (_type_): list of lists, each position of it will be passed to the function
        workers (int, optional): number of parallel elements, used only with mode "p" and "t". Defaults to 5.
        mode (str, optional): batch strategy. p = multiple process, t = multiple threads, s = serial execution. Defaults to "p".
        verbose (bool, optional): Control if there will be data printed. Defaults to True.

    Returns:
        _type_: _description_
    """
    if wmax:
        workers = multiprocessing.cpu_count()-1
    
    t0 = time.time()
    ret = []
    
    match mode:
        case "p": m = "Process"
        case "t": m = "Threaded"
        case "s": m = "Serial"
    
    
    pbar = tqdm(total=len(args),desc=f'{len(args)} {m} calls of {fn.__name__}')

    if mode == "s":
        
        for arg in args:
            pbar.update(n=1)
            ret.append(fn(arg))

    if mode == "t":
        with concurrent.futures.ThreadPoolExecutor(max_workers = workers) as executor:
            futures = []
            for item in args:
                futures.append(executor.submit(fn,item))
            for _ in concurrent.futures.as_completed(futures):
                pbar.update(n=1)
                ret.append(_.result())
                            
    if mode == "p":
        with concurrent.futures.ProcessPoolExecutor(max_workers = workers) as executor:
            futures = []
            for item in args:
                futures.append(executor.submit(fn,item))
            for _ in concurrent.futures.as_completed(futures):
                pbar.update(n=1)
                ret.append(_.result())
                                           
    return ret

