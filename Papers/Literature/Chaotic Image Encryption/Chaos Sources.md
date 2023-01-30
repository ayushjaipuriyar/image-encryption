Chaos can be created using mathematical or physical sources. In the following , researchers discuss the role of both types in the state-of-the-art of chaotic encryption.

## Mathematical Sources
Well-known mathematical chaos sources commonly used for image encryption purposes are studied below
- ### Chaotic systems and maps
	These are functions origianlly designed for creating chaos. Chaotic system and maps play a critical role in chaotic image encryption. To mention a few, one may refer to the following
	- #### Fractal-order chaotic system
		Fractional calculus goes back more than 300 years, with modern studies focusing on system s such as the fractional-order Chen, Lorenz, and Lie systems. A novel switching fractional-order chaos system was purposed by Hou and utilizes controlling switches to switch between its sub-systems and achieve a string chaos source for applying the exclusive or operation against the plain-text image.
		
		Another algorithm utilizing fractional-order systems was purposed be We, which opts to use a more standard third-order fractional systems as well as a novel Josephus scrambling algorithm and circular diffusion to achieve encryption properties and resilience [[circular diffusion]] common attacks.
	- #### Arnold cat map
		Arnold mapping is a well-known transposition chaotic map that l in the context of cryptography , was used by Ranimol and Gopakumar, as well as Zhang et al. To provide a method of permuting and de-correlating adjacent pixels in their proposed encryption algorithms. Both algorithms were proven to exhibit a large key-space with high key sensitivity and be capable of resisting common attacks such as brute force, entropy , CPT and KPT.
	- #### Coupled map Lattice
		A Coupled map lattice is a form of sapotiotemporal chaos map for random number stream generation . In one use case , Wu proposed a novel implementation of the use of CML to create encryption streams dependent not only on the initial values, but also on intermediate cipher images by using said cipher texts to modify the CML parameters. This adds a layer of plain text dependency, which aids in the defense against several attacks.
	- #### Lorenz map
		A lorenz map is a types of differential equation that is highly susceptible to initial conditions. An image encryption procedure in which the key is composed of the three inputs toa a 3D lorenz system and utilizes the chaotic naure of said system to provide string security
	- #### Logistic map
		A logistic map is a relatively simplistic mathematical mapping function, which when influenced by particular control values, acts chaotically. An algorithm proposed by Sharma and Bhargava utilizes a two-step interactive logistic map, where the next input is dependent on the previous two outputs, as a source of chaos. Similar work was performed by Li-Hong at al., where they used a more standard logistic map and paired it with a  hyper-chaos system to improve key generation effectiveness. 
	- #### Tent map
		An image encryption algorithm using the CTM and the rectangular transom was later analyzed and improved upon to better protect against plain text attacks such as CPT and KPT. The chaotic tent map is a mapping function that, when configured with control values in a particular range, behaves chaotically.
	- #### Lotka-Volterra
		A lotka-volterra chaotic system is a third-order differential equation in a similar family to other systems as Lorenz, Rossler, Shua and Chen. In a particular case study by Zahir, an encryption procedure was proposed thatutilizes the Lotka-Volterra chaotic system to aid in  the creation of Substitution boxes (S-boxes) with strong confusion properties, The resulting S-boxes were found to satisfy the five criteria (bijective, non-linearity, strict avalanche, bit independence , input/output XOR distribution) required for acceptable use in cryptographic algorithms/
	- #### Heron map
		The henon map was first discovered in 1978 and can be described as a 2D mapping function with two control parameters, which chosen strategically, enable the map to behave chaotically. Tressor proposed an image encryption algorithm utilizing the map to behave shuffling the pixels of the image and 4D Qi hyper-chaos to generate keys for encryption. Experimental analysis pf the algorithm demonstrates string cryptographic properties and resistance against common attacks
	- #### Logistic-sine system
		A logistic sine system is a discrete combination[] of the logistic and sine maps, both of which exhibit chaotic behaviors under particular initial conditions. Zeng and Chen referred to such a combination of the two maps as a compound chaotic map and utilized it in a novel encryption algorithm using XOR and modulus operation
		Zhao investigated the inefficiencies with single chaos systems and proposed a novel algorithm utilizing LSS and cascade chaos to improve upon said inefficiencies. Experimental analysis through simulations has proven the new algorithm to be highly resilient
		In another study, Lu conducted cryptanalysis of an existing algorithm based on multiple S-boxes , but were able to break it using CPT attacks. A new algorithm was proposed to improve upon the old one and involved only a single s-box constructed utilizing LSS. Further cryptanalysis of the new algorithm showed improvement over the original and was also quite fast.
		Variants of LSS have also been employed in encryption algorithms such as a 2D logistic Modulated Sine Coupling Logistic map proposed by Zhu, a Logistic Sine Modulation Map proposed by Zhang and a 2D Logistic Adjusted Sine Chaotic Map proposed by Balakrishnan and Mubarak . In all cases, theoretical analysis and simulations determined the algorithms to be both secure and efficient.
	- #### Baker map
		The baker map is a bijective permutation function that operates on an MxM matrix by randomizing its cells according to a secret key and is well respected in the image encryption community. Eishamy utilized the baker map in an image encryption algorithm to improve upon a classic technique knows as Double Random Phase Encoding .The proposed algorithm uses the map to pre-process the image before applying DRPS, and experimental analysis showed significant increases in security as opposed to using DRPE alone
		Another algorithm utilizing the baker map was proposed by Tong, where high-dimensional multiple chaos was paired with the baker map to achieve  a larger avalanche effect. Experimental results again showed significant increases in security .
	- #### Tinkerbell map
		Krishnan proposed an encryption algorithm utilizing Tinkerbell maps, a pair of chaotic functions to inject string pseudo-random numbers in multiple points during the encryption and decryption process. Differential and correlational analysis of the algorithm showed the proposed method to be highly efficient
	- #### Cubic map
		A cubic map is a single-dimension chaotic function that produces values on the interval and can be controlled by a single mapping parameter. Kavinmozhi proposed an encryption technique that employs a hybrid chaos source composed of the cubic and test maps, as well as the iterative Chaos Map and Infinite Collapses. The resulting hybrid map is used with the XOR operation to achieve encryption, and an analysis of the algorithm showed that it is suitable for repeated use and  is resilient against attacks.
	- #### Gingerbreadman map
		Savitri used the Gingerbreadman map , a 2D chaotic map , to generate encrypted keys for use with well-known Cipher Block Chain encryption algorithm, Using the map in this algorithm greatly improves CBC performance when applied to images, and a visual comparison demonstrated massive improvements.
	- #### Tangent map
		Moysis proposed a Random Number Generation algorithm based on the usage of the mathematical hyperbolic tangent function. When the RNG algorithm was applied to image encryption, the resulting procedure demonstrated string cryptography
	- #### Multiple maps
		Mixing multiple mapping functions in image encryption algorithms can serve multiple purposes. For example Bisht employed a verity of different maps to achieve tasks such as more chaotic permutations, diffusion, and RNG . A similar technique employing various maps in different stages if the encryption procedure was also proposed by Wang.
		Fu proposed a novel key stream generation technique utilizing multiple chaotic maps are important in numerous fields. Choi proposed an algorithm using multiple maps for encrypting colored medical images which can be seen as unique in their size and sensitivity.  Experimental and statistical analysis of the resulting procedure showed it its secure for use with healthcare images.
- ### Other mathematical sources
	In addition to chaotic systems and maps, some researchers have used the following mathematical designs, which have not been originally defined for chaos creating:
	- #### Space-filling curves
		Fractal geometry has several intriguing properties , such as self-similarity , composition by iterative methods , and a complex structure. Zhang utilized Hilbert curves and H-fractals, types of self-filling curves, in a novel image encryption algorithm. This algorithm alternates the use of both curves to efficiently scramble the pixels of the image.
	- #### Memory cellular automata
		Cellular Automata can best be described as a grid of cells with a finite set of states and a transition functions that governs how cells change state over time. Whereas a standard CA only depends on the generation t-1, Memory Cellular Automata depend on more parameters. When the MCA's rules are defined by chaotic maps, the structure becomes a powerful tool for image encryption. Several algorithms using various-order MCAs have been proposed, for example a 4D MCA by Asiam , a 2D MCA by Hibibipour and an indefinite CA by Hibibipour.
	- #### Transcendental numbers
		In mathematics, a transcendental number has the characteristic that digits to the right of the decimal have no pattern . Garcia et al.  proposed an image encryption algorithm that uses chaos and the transcendental number Pi, dubbed Chaotic Pi Ciphering (CPC). Thealgorithm uses Pi and a chaos source created using differential equations to generate cipher keys and substitution boxes. 
		
## Physical Sources
In addition to mathematical sources, chaos can be created using physical phenomena and used in chaotic image encryption:
- ## Optical Chaos
	Our physical world can provide many forms of chaos, with just one example being light. In studies by Xie et al. and Lui et al. 	, they found success in producing a chaotic base for image encryption algorithms using lasers. Extensive security testing of both algorithms showed
	them to be highly secure and feasible for practical use.Other studies have also been carried out, such as those by Li et al. and Liu et al. , where
	optical chaos is utilized for encrypting and then transmitting images for storage in the cloud.	Experimental results showed both procedures to be secure and safe for production use.
- ### Chaotic circuits
	- #### Chua circuit
		Some physical electronic circuits such as the Chua circuit can produce chaotic behavior. AlMutairi et al. utilized the circuit as a key generator in their proposed image encryption algorithm. By contrast, Lin et al. proposed a similar encryption model, but instead utilized a variant of the classic Chua circuit with a PWL memristor. In both cases, analysis showed the algorithms to exhibit strong security properties.
	- #### Memristive circuits
		A memristor is a form of electrical component that is capable of exhibiting chaotic behavior. Liu et al. proposed an image  algorithm that utilizes 4D memristive hyper-chaos to create chaos matrices. Security analysis showed strong security and cryptographic properties. Another image encryption algorithm was proposed by Sun et al.  using a memristive chaotic system. The presented system demonstrates a unique property known as
		multistability, which further improves the chaoticness of the system. Again, security analysis showed the algorithm to possess strong cryptographic properties.
	- #### Physically Unclonable Functions (PUFs)
		True Random Number Generators (TRNGs), although very important in cryptography, are impossible to achieve in software. To counter this fact, Muhammad et al. proposed an encryption algorithm using a hardware device, a form of physically unclonable function, to generate true random numbers. Though extensive experiments and analysis, the TRNG was successful in passing all tests required for safe use in cryptographic algorithms.