def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input('Enter celsius temperature: '))
    fahrenhiet = (9/5) * celsius + 32
    print(f'Temperature in F \t  {fahrenhiet: .2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenhiet


if __name__ == '__main__':
    main()
