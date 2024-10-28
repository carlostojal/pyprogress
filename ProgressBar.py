import math

class ProgressBar:
    """
    Progress bar classes. Creates a progress bar instance with given attributes.
    """

    def __init__(self, total_elements: float, width: int = 20) -> None:
        """
        Construct a new ProgressBar object.

        :param total_elements: Number of elements / units of processing.
        :param width: Progress bar width in characters.

        :retval None
        """

        # assign the members
        self.total_elements = total_elements
        self.width = width

        # current element and percentage
        self.cur_element = 0.0 # current element
        self.percentage = 0.0

        self.string = ""

    def __generate_string(self) -> str:
        """
        Generate the string for the progress bar.

        :retval: Progress bar in string form.
        """
        
        s: str = "[{:.2f}%] [".format(self.percentage*100)

        n_chars = math.ceil(self.width * self.percentage)
        for i in range(n_chars):
            s += "#"
        for i in range(self.width - n_chars):
            s += "-"

        s += "]"

        self.string = s


    def update(self, cur_element: float) -> None:
        """
        Update the progress bar.

        :param cur_element: Current element.

        :retval: None
        """
        
        # verify bounds
        if cur_element > self.total_elements:
            cur_element = self.total_elements

        self.cur_element = cur_element

        # calculate the percentage
        self.percentage = self.cur_element / self.total_elements

        # generate the string for the next time
        self.__generate_string()


    def __repr__(self) -> str:
        """
        Printable form of the class (progress bar in string form)

        :retval: Progress bar in string form.
        """
        return self.__generate_string()

    def print(self) -> None:
        """
        Print the progress bar in the line where the cursor is placed, overwriting any existing content.

        :retval: None
        """

        print(f"\r{self.string}", end="")

