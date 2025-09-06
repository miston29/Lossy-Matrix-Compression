
This is an attempt at lossy matrix compression by breaking down a matrix of dimensions *n x m* into two vectors of size *n x 1* and *1 x m*. 

There are two python files included:
1.  A Python script that serves as a proof-of-concept for the decomposition algorithm.
2.  An implementation that applies this lossy compression technique to an image

### Mathematical Formulation

The core idea is to approximate a matrix **A** by the outer product of a column vector **V** and a row vector **H**.

$$A_{n \times m} \approx V_{n \times 1} \otimes H_{1 \times m}$$

The vectors **V** and **H** are approximated and calculated through an iterative formula. Given an initial guess for **H**, a new approximation for **V** is calculated, which is then used to find a better approximation for **H**. Usually 3 to 4 iterations are enough to calculate these vectors


The iterative formulas for the components of **V** and **H** are:

$$V_i = \frac{\sum_{j=1}^{m} A_{ij}}{\sum_{j=1}^{m} H_j}$$
$$H_j = \frac{\sum_{i=1}^{n} A_{ij}}{\sum_{i=1}^{n} V_i}$$

this is named as itr_sumdivision() function and is also used for Image compression.
one another formula named as itr_reciprocal() is:

$$V_i = \frac{1}{2} \sum_{j=1}^{m} \frac{A_{ij}}{H_j}$$
$$H_j = \frac{1}{2} \sum_{i=1}^{n} \frac{A_{ij}}{V_i}$$

### Image Compression Implementation

An image is treated as three separate matrices for Red, Green, and Blue channels. Each matrix is decomposed into two vectors.
These six vectors that are formed are stored in a .txt file along with their initial dimensions which requires less space than the original image.
The image can then be reconstructed from these vectors, resulting in a lossy reconstruction of the original image.

example usage
Original Image:
![original_image](https://github.com/miston29/Lossy-Matrix-Compression/blob/main/original_image.jpg)

recreating image from vectors:
![reformed_image](https://github.com/miston29/Lossy-Matrix-Compression/blob/main/reformed_image.jpg)

### Key Concepts

  * **Lossy Compression:** This is a data compression method where some information is lost in the process. The goal is to minimize the amount of data needed to represent a piece of content, at the cost of a reduction in quality.
  * **Matrix Decomposition:** The process of factoring a matrix into a product of matrices. In this case, we are approximating a matrix as the outer product of two vectors.
  * **Iterative Approximation:** A method of solving a problem by finding successive approximations to the solution, starting from an initial guess.

