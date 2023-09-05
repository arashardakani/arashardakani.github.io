---
layout: page
title: Stochastic Computing
description: A New Computing Paradigm for Machine Learning
img: assets/img/3.jpg
importance: 2
category: work
---

In stochastic computing (SC), continuous values are represented as the frequency of ones in random bit streams. In this way, arithmetic computations are performed using simple bit-wise operations on bit streams. Since a single bit-flip in a stochastic stream results in a marginal change in the continuous value represented by the bit stream, SC-based implementations can tolerate small errors. Due to the error tolerance and the simplicity of operations in SC, it has been used for implementation of neural networks in the past few years. SC-based neural networks are often obtained by converting floating-point (or fixed-point) representation of traditional neural networks to SC representation. Of course, not all the units (e.g., batch normalization) can be converted into SC representation due to the complex nature of their computations. To address the issues raised from the conversion, we introduced a novel SC-based neural network, called stochastic neural network, where its training and inference follow SC instructions. The proposed stochastic neural network exploits finite-state machines which imitate the functionality of traditional neurons without any explicit non-linearity. Please check out the papers below to learn more about SC and stochastic neural networks.

