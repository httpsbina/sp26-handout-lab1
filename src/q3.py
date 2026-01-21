"""
This question has two parts:

Part 1: Please implement these stub functions to match the documentation.
It will be useful to use a dict to store the "threshold" for each tax bracket, 
and use an appropriate control structure to go over it and find the right tax bracket.

Part 2: The California, New York, and Federal tax functions should have code in common.
Factor it out into a helper function, so that the code is not repeated, but the functionality
remains the same.

As always, make sure to implement tests in the tests directory.
"""

# Relevant information:
# Federal income tax rates:  https://www.irs.gov/filing/federal-income-tax-rates-and-brackets
# California income tax rates: https://www.hrblock.com/tax-center/filing/states/california-tax-rates
# Massachusetts income tax rate: 5% for everyone
# New York state income tax rates: https://www.nerdwallet.com/article/taxes/new-york-state-tax


def calculate_bracket_tax(income: int, brackets: dict) -> float:
    """Helper function to calculate tax based on progressive tax brackets
    
    Parameters
    ----------
    income : int
        A person's annual income (before tax)
    brackets : dict
        Dictionary where keys are income thresholds and values are tax rates
        Format: {threshold: rate}
    
    Returns
    -------
    float
        The total tax amount
    """
    total_tax = 0.0
    previous_threshold = 0
    
    # Sort brackets by threshold
    sorted_thresholds = sorted(brackets.keys())
    
    for threshold in sorted_thresholds:
        if income > threshold:
            # Tax the portion of income in this bracket
            taxable_in_bracket = threshold - previous_threshold
            total_tax += taxable_in_bracket * brackets[threshold]
            previous_threshold = threshold
        else:
            # Tax the remaining income in this bracket and stop
            taxable_in_bracket = income - previous_threshold
            total_tax += taxable_in_bracket * brackets[threshold]
            return total_tax
    
    # If income exceeds all thresholds, tax the remaining at the highest rate
    if income > previous_threshold:
        taxable_in_bracket = income - previous_threshold
        total_tax += taxable_in_bracket * brackets[sorted_thresholds[-1]]
    
    return total_tax


def income_tax_fed(income: int) -> float:
    """Calculates the amount of federal income tax paid by somebody in the United States
    
    Parameters
    ----------
    income : int
        A person's annual income (before tax)
    
    Returns
    -------
    float
        The amount of federal income tax they pay
    """
    # 2024 Federal tax brackets (single filer)
    federal_brackets = {
        11600: 0.10,
        47150: 0.12,
        100525: 0.22,
        191950: 0.24,
        243725: 0.32,
        609350: 0.35,
        float('inf'): 0.37
    }
    
    return calculate_bracket_tax(income, federal_brackets)


def income_tax_ca(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in California
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of CA state tax they pay if they live in California
    """
    # California tax brackets
    ca_brackets = {
        10412: 0.01,
        24684: 0.02,
        38959: 0.04,
        54081: 0.06,
        68350: 0.08,
        349137: 0.093,
        418961: 0.103,
        698271: 0.113,
        float('inf'): 0.123
    }
    
    return calculate_bracket_tax(income, ca_brackets)



def income_tax_ma(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in Massachusetts
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in Masachusetts
    """
    # Massachusetts flat tax rate
    return income * 0.05

def income_tax_ny(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in New York state
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in New York state
    """
    # New York tax brackets
    ny_brackets = {
        8500: 0.04,
        11700: 0.045,
        13900: 0.0525,
        80650: 0.055,
        215400: 0.06,
        1077550: 0.0685,
        5000000: 0.0965,
        25000000: 0.103,
        float('inf'): 0.109
    }
    
    return calculate_bracket_tax(income, ny_brackets)


def calculate_income_tax() -> None:
    """
    1. Ask the user to input their state (CA for California, MA for Massachusetts, NY for New York)
    2. Ask the user to input an annual income
    3. Print a sentence formatted like this: "Your income is XX before tax and XX after tax. You pay XX income tax."
    4. Handle invalid unit inputs gracefully
    """
    # Ask for state
    state = input("Please enter your state (CA, MA, or NY): ").strip().upper()
    
    # Validate state input
    if state not in ['CA', 'MA', 'NY']:
        print("Invalid state. Please enter CA, MA, or NY.")
        return
    
    # Ask for income
    try:
        income = int(input("Please enter your annual income: "))
        if income < 0:
            print("Income cannot be negative.")
            return
    except ValueError:
        print("Invalid income. Please enter a number.")
        return
    
    # federal tax
    federal_tax = income_tax_fed(income)
    
    # state tax based on state
    if state == 'CA':
        state_tax = income_tax_ca(income)
    elif state == 'MA':
        state_tax = income_tax_ma(income)
    else: 
        state_tax = income_tax_ny(income)
    
    # total tax and after-tax income
    total_tax = federal_tax + state_tax
    after_tax_income = income - total_tax
    
    print(f"Your income is ${income} before tax and ${after_tax_income:.2f} after tax. You pay ${total_tax:.2f} income tax.")
