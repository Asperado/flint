from multiprocessing import Pool

def mapper_run(func, data):
    worker_num = 10
    pool = Pool(worker_num)
    return pool.map(func, data)
