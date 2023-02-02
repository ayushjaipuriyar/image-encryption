The architecture of chaos based image cryptosystem mainly consists of two stages: the confusion stage and the diffusion stage. The typical block diagram of the architecture is as depicted in the figure 1. 
 
 
 
 
Figure  1.   Architecture   of a chaos - based image cryptosystem. 
 
The confusion stage is the pixel permutation where the positions of the pixels are scrambled over the entire image without disturbing the values of the pixels. With this the image becomes unrecognizable. Hence 
these initial conditions and control parameters serve as the secret key. It is not very secure to have only the permutation stage since it may be broken by any attack. To enhance the security, the second stage of the encryption process aims at changing the value of each pixel in the entire image. The process of diffusion is carried out through a chaotic map which is mainly dependent on the initial conditions and control parameters. In the diffusion stage, the pixel values are modified sequentially by the sequence generated from the chaotic systems. The whole confusion-diffusion round 
repeats for number of times to achieve security of satisfactory 
level. The randomness property which is inherent in chaotic 
maps makes it more suitable for image encryption [7]. 
V. 
INSIGHT INTO DIFFERENT ENCRYPTION 
TECHNIQUES 
In the scheme proposed by K. Sakthidasan Sankaran and 
B.V. Santhosh Krishna, the cryptosystem consists of two 
stages: Confusion stage and Diffusion stage. Different 
chaotic systems are employed in both the confusion and 
diffusion stages. Here complex chaotic maps are chosen 
rather than the simple ones to further increase the complexity 
of the algorithm, thereby improving the security. The input to 
the cryptosystem is a plain image that is to be encrypted. 
Encryption process comprises of confusion and diffusion 
stages. In confusion stage, pixel position permutation is done 
using one of the 3D chaotic systems. This is followed by the 
diffusion stage wherein the pixel value diffusion is carried 
out again with any one of the chaotic system. The initial 
conditions and the control parameters used for generating the 
chaotic sequence in both the stages serve as the secret key in 
the 2 stages. Separate keys are used for permutation and 
diffusion stage of the encryption process for enhancing the 
security of the algorithm. The resulting image is called the 
cipher image. The decryption process also comprises of 2 
stages i.e. Diffusion followed by confusion stage. In the 
diffused image decryption stage, the original pixel values are 
retrieved by using any one of the chaotic system (Lorenz, 
chen, Lu). The diffusion key used in the 2nd stage of 
encryption is used here also. In the final decryption process, 
to get back the original position of the image same confusion 
key as used in the first stage of encryption is used. The output 
of the decryption stage is nothing but the original image [7]. 
            In this scheme the authors A. Anto Steffi and Dipesh 
Sharma proposed modified algorithm for encryption and 
decryption of images using chaotic maps. The 2 chaotic 
systems are used Lorenz and Baker maps. As mentioned in 
[7], the authors perform encryption process comprising of 
confusion and diffusion stage. In the confusion and diffusion 
stage, the pixel positions and values are changed (based on 
one of the 2 chaotic systems i.e. Lorenz or Baker) thereby 
shuffling the image. In both the stages separate keys are used 
for generating the chaotic sequence. In decryption stage, 
reverse operation is performed and the original image is 
obtained [8]. 
           In this paper by Somaya, Al-Maadeed, Afnan Al-Ali, 
and Turki Abdalla, new image encryption scheme consists of 
pixel shuffler unit and a stream cipher unit. Pixel scrambling 
has 2 important issues which are useful for image encryption. 
Along with rearranging of pixel location (diffusion), it also 
changes the values of each pixel value (confusion[]