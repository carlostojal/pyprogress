import math
import threading

class ProgressBar:
    """
    Progress bar classes. Creates a progress bar instance with given attributes.
    """

    def __init__(self, total_elements: int, width: int = 20, details: bool = True) -> None:
        """
        Construct a new ProgressBar object.

        :param total_elements: Number of elements / units of processing.
        :param width: Progress bar width in characters.
        :param details: Show details (current/total elements)

        :retval None
        """

        # assign the members
        self.total_elements = total_elements
        self.width = width
        self.details = details

        # current element and percentage
        self.cur_element = 0 # current element
        self.percentage = 0.0

        # spinning characters
        self.cur_spin = 0
        self.spin = ['/', '-', '\\', '|']

        # concatenated string
        self.string = ""

        # mutex lock and condition variable for the string object
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)

    def __generate_string(self, extra: str = "") -> str:
        """
        Generate the string for the progress bar.

        :retval: Progress bar in string form.
        """
        
        # lock the mutex
        with self.lock:
            s: str = "[{:.2f}%] [".format(self.percentage*100)

            n_chars = math.ceil(self.width * self.percentage)

            # add fill characters
            for i in range(n_chars-1):
                s += "#"

            # add the spinning character if not the last
            if n_chars < self.width:
                s += self.spin[self.cur_spin]
                self.cur_spin += 1
                self.cur_spin %= 4
            else:
                s += "#"

            # add the hollow characters
            for i in range(self.width - n_chars):
                s += "-"

            # terminate the bar
            s += "]"

            # if the user wants details
            if self.details:
                s += f" ({self.cur_element}/{self.total_elements})"

            # add extra
            if extra != "":
                s += f" - {extra}"

            self.string = s

            # notify waiting threads
            self.cv.notify()


    def update(self, cur_element: int, extra: str = "") -> None:
        """
        Update the progress bar.

        :param cur_element: Current element.
        :param extra: Extra string, as the user may wish (e.g. logging losses)

        :retval: None
        """
        
        # verify bounds
        if cur_element > self.total_elements:
            cur_element = self.total_elements

        self.cur_element = cur_element

        # calculate the percentage
        self.percentage = self.cur_element / self.total_elements

        # generate the string for the next time
        # start a thread to do it in the background
        thread = threading.Thread(target=self.__generate_string, args=(extra,))
        thread.start()


    def __repr__(self) -> str:
        """
        Printable form of the class (progress bar in string form)

        :retval: Progress bar in string form.
        """
        s = None
        with self.cv:
            s = self.string
        return s

    def print(self) -> None:
        """
        Print the progress bar in the line where the cursor is placed, overwriting any existing content.

        :retval: None
        """

        s = None
        with self.cv:
            s = self.string
        print(f"\r{s}", end="")

