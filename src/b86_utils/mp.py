import concurrent.futures
import time

def call(fn, args, workers = 5, mode="p", verbose = True):
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
    t0 = time.time()
    ret = []
    
    if mode == "p":
        with concurrent.futures.ProcessPoolExecutor(max_workers = workers) as executor:
            futures = []
            for item in args:
                futures.append(executor.submit(fn,item))
            for future in concurrent.futures.as_completed(futures):
                ret.append(future.result())
    
    if mode == "t":
        with concurrent.futures.ThreadPoolExecutor(max_workers = workers) as executor:
            futures = []
            for item in args:
                futures.append(executor.submit(fn,item))
            for future in concurrent.futures.as_completed(futures):
                ret.append(future.result())
                
    if mode == "s":
        for arg in args:
            ret.append(fn(arg))

    if verbose:
        print(f'#MP: mode: {mode}, size:{len(args)}, duration: {round(time.time()-t0,2)}, workers: {workers}')

    return ret

