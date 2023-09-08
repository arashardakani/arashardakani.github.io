---
layout: page
title: Stochastic Computing
description: A New Computing Paradigm for Machine Learning
img: assets/img/sc.png
importance: 2
category: work
---

In stochastic computing (SC), continuous values are represented as the frequency of ones in random bit streams. In this way, arithmetic computations are performed using simple bit-wise operations on bit streams. Since a single bit-flip in a stochastic stream results in a marginal change in the continuous value represented by the bit stream, SC-based implementations can tolerate small errors. Due to the error tolerance and the simplicity of operations in SC, it has been used for implementation of neural networks in the past few years. SC-based neural networks are often obtained by converting floating-point (or fixed-point) representation of traditional neural networks to SC representation. Of course, not all the units (e.g., batch normalization) can be converted into SC representation due to the complex nature of their computations. To address the issues raised from the conversion, we introduced a novel SC-based neural network, called stochastic neural network, where its training and inference follow SC instructions. The proposed stochastic neural network exploits finite-state machines which imitate the functionality of traditional neurons without any explicit non-linearity. Please check out the papers below to learn more about SC and stochastic neural networks.

[Training Linear Finite-State Machines](https://proceedings.neurips.cc/paper/2020/hash/4fc28b7093b135c21c7183ac07e928a6-Abstract.html) (Arash Ardakani, Amir Ardakani, Warren Gross, NeurIPS 2020)


[A Regression-Based Method to Synthesize Complex Arithmetic Computations on Stochastic Streams](https://ieeexplore.ieee.org/abstract/document/9180838) (Arash Ardakani, Amir Ardakani, Warren Gross, ISCAS 2020)


[Fault-Tolerance of Binarized and Stochastic Computing-based Neural Networks](https://ieeexplore.ieee.org/abstract/document/9605019) (Amir Ardakani, Arash Ardakani, Warren Gross, SiPS 2021)

[VLSI Implementation of Deep Neural Network Using Integral Stochastic Computing](https://ieeexplore.ieee.org/abstract/document/7839313) (Arash Ardakani, Francois Leduc-Primeau, Naoya Onizawa, Takahiro Hanyu, Warren J Gross, TVLSI 2017)

[Stochastic Computing Can Improve Upon Digital Spiking Neural Networks](https://ieeexplore.ieee.org/abstract/document/7780115) (Sean C. Smithson, Kaushik Boga, Arash Ardakani, Brett H. Meyer, Warren J. Gross, SiPS 2016)



