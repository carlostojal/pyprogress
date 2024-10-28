from ProgressBar import ProgressBar
import time

if __name__ == "__main__":

    bar = ProgressBar(total_elements=float(50), width=20)

    for i in range(50):
        bar.update(float(i))
        bar.print()
        time.sleep(0.1)

