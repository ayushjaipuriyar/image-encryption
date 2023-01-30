In the following , researchers examine the role of cryptographic primimtives such as scrambling, bit shuffling , hashin , secret sharing, one-time key, permutation, substitution, confusionf and diffusion in chaotic imahe encryption.

## Scrambling
Scrambling is the process of permutating the pixels so that the new ordering is unrecognizable from the origianl. Various methods of scambling have been employed including Lartin rectangle, logistic chaotic and spiral.

## Bit shuffling
Bit shuffling is another method of permutating the pixels of an image, specifically at the bit level. Kirshnamoorthi proposed a method of bit shuffling in the spatial domain using a tent map

## Hashing
Hashing algorithm are special types of functions that take an input of any length and produce an output that is always the same length. The SHA algorithm specifically also has the added bonus of being highly input sensitive, that is to say, small changes in the input create a very different output.

In the context of image encryption , one common use of hash algorithm is to generate the keystream. Bhadke utilized SHA-256 and the Lorenz chaos attractor to generate string key streams. Slimane also proposed an algorithm using the Lorenx chaos attractor and a hash algorithm, although they opterd to use SHA-1 instead.
Lui, a novel encryption algorithm using SHA-3 and stenography was proposed. This algorithm embeds the hash of the plaintext image into the cipher image using stenography. This makes the algorithm very sensitive to the plain image, which in turn yields stronger seciurity

# Permutation, substitution, confusion and diffusion

## Permutations and diffusion
Permutations is the process of rearranging elements in a structure, which in the context of images, refers tot scrambling the pixels. Abd-El-Hafiz performed an evaluation on three different permutation method and found that discrete performed the best.

Diffusion  is the process of ensuring there is no statistical significance to the resulting structure. In the context of images, this refers to scrambling the pixels of the images to eliminate the correlation between adjacent pixels, Ping proposed a novel digit-levle permeation algorithm that additionally employs a high-speed diffusion . Evaluation results demonstrated high security and efficiency

Combining the two into the same stage of encryption aims to combat hackers who try to break each stage separately, Liu proposed an algorithm to perform permutations and diffusion simultaneous. The algorithm additionally uses a Hopfieldd chaotic neural network to perform further diffusion, which gives the algorithm  greater key sensitivity.

## confusion
Confusion in encryption refers to the level of dependency elements of the cipher text have with the key. As seen with permutation , confusion if often integrated with diffusion for the same reasons. Run-he proposed an image encryption algorithm that achieves an integration of confusion and diffusion by Xoring the plain image with chaotically generated offset matrices.

## substitution
Substitution involves replacing an element with something else in a predictable and invertable manner. The substitution requirement is commonly implemented using s-boxes, which are matrices that define how each input maps to its substituted value.

For image encryption, chaos-based 5-boxes include those generated from the chaotic cine map and the logistic map , Wang and Zhang also proposed an algorithm with multiple S-box substitutions, where the order of the boxes is determined by a random chaos sequence. Another algorithm proposed by Khan splits the image into four blocks and applies a different S-box to reach block. These S-boxes each originate from a different encryption algorithm. Another paper by Lidong proposes a dynamic encryption algorithm so that the cipher image is always different even of the same key and plain image are used.