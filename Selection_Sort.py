
class selection_sort():
    def __init__(self):
        """
        This class is to perform Selection Sort on a given List/Array
        """
        self.verified = False
        self.getSorted = []

    def _verify_array(self, list_to_sort):
        """
        This method is used for verifing either array contain invalid entries.
        """
        try:
            for element in list_to_sort:
                int(element)
        except:
            exit('Please input a valid numerical values')

    def sort(self, list_to_sort):
        """ This method is used to sort the given array
                """
        # Verify
        if self.verified is False:
            self._verify_array(list_to_sort)
            self.verified = True

        # Logic
        for element in range(len(list_to_sort)):
            minimum = element
            for comparing in range(minimum+1, len(list_to_sort)):
                if list_to_sort[comparing] < list_to_sort[minimum]:
                    minimum = comparing

            list_to_sort[element], list_to_sort[minimum] = list_to_sort[element], list_to_sort[minimum]

        self.getSorted = list_to_sort