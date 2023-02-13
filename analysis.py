
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
import math
# Differential Attakcs NPCR & UACI


def NPCR(img1, img2):
    """
    Calculate the NPCR value
    Bigger the better
    [0-100]
    Parameters:
        img1 = Encrypted image 1
        img2 = Encrypted image 2 with one pixel changed
    Returns:
        NPCR value
     """
    height, width = img1.shape
    sum = 0
    for i in range(height):
        for j in range(width):
            if img1[i, j] != img2[i, j]:
                sum += 1
    res = ((sum)/(width*height))*100
    return res


def UACI(img1, img2):
    """
    Calculate the UACI value
    Bigger the Better
    Parameters:
        img1 = Encrypted image 1
        img2 = Encrypted image 2 with one pixel changed
    Returns:
        UACI value
    """
    height, width = img1.shape
    difference = 0
    for y in range(height):
        for x in range(width):
            difference += (abs(int(img1[x, y])-int(img2[x, y])))
    difference = ((difference*100)/(width*height*255))
    return difference


def NPCR_UACI_worker(img1, img2):
    """
    Calculate the NPCR & UACI worker
    Parameters:
        img1 = Encrypted image 1
    Returns:
        NPCR value
    """
    return NPCR(img1, img2), UACI(img1, img2)

# Statistical Analysis


def correlation_coefficient(img1, img2):
    """
    Calculate the correlation coefficient of the enccrypted image to the original image
    Parameters:
        img1 = Original image
        img2 = Encrypted image
    Returns:
        The value of correlation coefficient
    """
    x_mean = np.mean(img1)
    y_mean = np.mean(img2)
    num = np.sum((img1 - x_mean) * (img2 - y_mean))
    den = np.sqrt(np.sum((img1 - x_mean)**2) * np.sum((img2 - y_mean)**2))
    return num / den


def histogram(img1, img2):
    """
    Make the histrogram of the encrypted and the origianl image
    Encrypted image should have a plain normalised histrogram
    Parameters:
        img1 = Original image
        img2 = Encrypted image
    Returns:
        Prints the histogram of original and the encrypted image
    """
    # Plot the histograms and images of the original image
    plt.figure()
    plt.subplot(121), plt.imshow(img1, 'gray')
    plt.title('Original Image')
    plt.subplot(122), plt.hist(img1.ravel(), 256, [0, 256])
    plt.title('Histogram of Original Image')

    plt.figure()
    plt.subplot(121), plt.imshow(img2, 'gray')
    plt.title('Encrypted Image')
    plt.subplot(122), plt.hist(img2.ravel(), 256, [0, 256])
    plt.title('Histogram of Encrypted Image')
    if get_ipython() is not None:
        plt.show()
    else:
        return

# Information Entropy


def entropy(img1):
    """
    Calculate Information entropy
    Parameters:
        img1 = image
    Returns:
        Calculate the value of Information entropy
    """
    # Compute normalized histogram -> p(g)
    p = np.array([(img1 == v).sum() for v in range(256)])
    p = p/p.sum()
    # Compute e = -sum(p(g)*log2(p(g)))
    e = -(p[p > 0]*np.log2(p[p > 0])).sum()

    return e
# Bit correct Ratio;


def bit_correct_ratio(img1, img2):
    """
    Calculate the bit correct ratio
    Maybe higher
    [0-1]
    Parameters:
        img1 = Encrypted image
        img2 = Decrypted image
    Returns:
        BCR value
     """
    height, width = img1.shape
    sum = 0
    for i in range(height):
        for j in range(height):
            sum += img1[i, j] ^ img2[i, j]
    BCR = 1-(sum/(width*height))
    return BCR

# Mean Square Error
    def MSE(img1, img2):
        """
        Calculate the mean square error
        Minimum
        [0-infinity]
        Parameters:
            img1 = Encrypted image
            img2 = Decrypted image
        Returns:
            MSE value
        """
        height, width = img1.shape
        differences = (img1 - img2) ** 2
        total_difference = differences.sum()
        MSE = total_difference / float(height*width)
        return MSE
# Mean Absolute Error

    def MAE(img1, img2):
        """
        Calculate the mean absolute error
        Maximum
        [0-255]
        Parameters:
            img1 = Encrypted image
            img2 = Decrypted image
        Returns:
            MSE value
        """
        height, width = img1.shape
        differences = abs((img1 - img2))
        total_difference = differences.sum()
        MAE = total_difference / float(height*width)
        return MAE

# Root Mean Square Error

    def RMSE(img1, img2):
        """
        Calculate the root mean square error
        Minimum
        [0-infinity]
        Parameters:
            img1 = Encrypted image
            img2 = Decrypted image
        Returns:
            RMSE value
        """
        return math.sqrt(MSE(img1, img2))

# Peak Signal to Noise Ratio()
    def PNSR(img1, img2):
        """
        Calculate the Peak Signal to Noise Ratio()
        Minimum
        [0-infinity]
        Parameters:
            img1 = Encrypted image
            img2 = Decrypted image
        Returns:
            PSNR value
        """
        height, width = img1.shape
        mse = MSE(img1, img2)
        if mse == 0:
            return float("inf")
        PIXEL_MAX = 255.0
        return 10 * np.log10(PIXEL_MAX**2 / MSE)

# Signal to Distortion Ratio()
    def SDR(img1, img2):
        """
        Calculate the Signal to Distortion Ratio()
        Minimum
        [0-infinity]
        Parameters:
            img1 = Encrypted image
            img2 = Decrypted image
        Returns:
            SDR value
        """
        reference_power = np.mean(img1 ** 2)
        distortion_power = np.mean((img1 - img2) ** 2)
        if distortion_power == 0:
            return float("inf")
        return 10 * np.log10(reference_power / distortion_power)

# Signal to Noise Ratio


def snr(original_image, decrypted_image):
    """
    Calculate the Signal-to-Noise Ratio (SNR) of a decrypted image

    Parameters
    ----------
    original_image : array_like
        The original image
    decrypted_image : array_like
        The decrypted image

    Returns
    -------
    snr : float
        The Signal-to-Noise Ratio (SNR) of the decrypted image
    """
    signal_power = np.mean(original_image**2)
    noise_power = np.mean((original_image - decrypted_image)**2)
    snr = signal_power / noise_power

    return snr
