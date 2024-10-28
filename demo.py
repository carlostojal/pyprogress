from ProgressBar import ProgressBar
import time

if __name__ == "__main__":

    bar = ProgressBar(total_elements=1000, width=50)

    for i in range(1000):
        bar.update(i+1, extra=f"loss={1-(i/1000)}")
        bar.print()
        time.sleep(0.001)

    print()

