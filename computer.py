class Computer:

    # What attributes will it need?
class Computer:
    def __init__(self, 
                 description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        """
        Initializes a new Computer object with the given specifications.
        """
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_price(self, new_price: int):
        """
        Updates the computer's price.
        :param new_price: The new price to set.
        """
        self.price = new_price

    def update_operating_system(self, new_os: str):
        """
        Updates the computer's operating system.
        :param new_os: The new operating system to set.
        """
        self.operating_system = new_os

    def refurbish(self, new_os: Optional[str] = None):
        """
        Refurbishes the computer by adjusting its price based on its age.
        Optionally installs a new operating system.
        :param new_os: (Optional) The new operating system to install.
        """
        if self.year_made < 2000:
            self.price = 0   # too old to sell, donation only
        elif self.year_made < 2012:
            self.price = 250  # heavily-discounted price on machines 10+ years old
        elif self.year_made < 2018:
            self.price = 550  # discounted price on machines 4-to-10 years old machines
        else:
            self.price = 1000 # recent machines

        if new_os is not None:
            self.update_operating_system(new_os)

    def __repr__(self):
        """
        Provides a string representation of the Computer object.
        """
        return (f"Computer(description={self.description}, processor_type={self.processor_type}, "
                f"hard_drive_capacity={self.hard_drive_capacity}, memory={self.memory}, "
                f"operating_system={self.operating_system}, year_made={self.year_made}, price={self.price})")
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        pass # You'll remove this when you fill out your constructor

    # What methods will you need?