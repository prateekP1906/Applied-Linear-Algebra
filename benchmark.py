import time
from vec import Vec

def run_benchmark():

    sizes = [2000, 4000, 8000, 16000, 32000, 64000]
    print(f"{'Vector Size': <15} | {'Addition (s)': <15} | {'Scalar Mul(s)': <15} | {'Norm (s)': <15}")
    print("-" * 65)

    for n in sizes:
        v1 = Vec.uniform(n)
        v2 = Vec.uniform(n)

        start_time = time.perf_counter()
        _ = v1 + v2
        add_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        _ = 2.5 * v1
        multi_time = time.perf_counter() - start_time

        start_time = time.perf_counter()
        _ = v1.norm()
        norm_time = time.perf_counter() - start_time

        print(f"{n:<15} | {add_time:<15.5f} | {multi_time:<15.5f} | {norm_time:<15.5}")

if __name__ == "__main__":
    run_benchmark()

