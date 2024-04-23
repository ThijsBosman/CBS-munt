import binomial
import matplotlib.pyplot as plt

def main() -> None:
    """Main function of the program.

    Args:
        None

    Returns:
        None
    """
    x = binomial.get_binom_distrobution(1000, 0.5)
    
    # Plot the probability density function
    plt.plot(binomial.get_binom_pdf(x))
    plt.title('Probability Density Function')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.show()








if __name__ == '__main__':
    main()
