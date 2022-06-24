# MRI Contrast Enhancement with a conditional GAN (pix2pix)

This tutorial is largely taken from [TensorFlow](https://www.tensorflow.org/tutorials/generative/pix2pix).

The original TensorFlow tutorial is modified to process MRI T1-weighted images in order to enhance contrast. Usually a higher contrast in T1-weighted images can be achieved through injecting gadolinium-based contrast agents (GBCAs). However, the accumulation of gadolinium deposits in the brain can have uncertain long-term consequences.

For more information on GBCAs please refer to the references.

## Setup

Download dataset from https://www.kaggle.com/datasets/dschettler8845/brats-2021-task1

### Docker

CPU only

```
docker build -t pix-pix .
docker run --name pix -p 8888:8888 -d pix-pix
```

### Local

```
pip install -r requirements.txt
./run.sh jupyter
```

### Start
Open http://localhost:8888/notebooks/pix2pix.ipynb in a Browser.

## References

\[1\] Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. “Image-to-Image Translation with Conditional Adversarial Networks”. In: 2017 IEEE Conference on
Computer Vision and Pattern Recognition (CVPR). Honolulu, HI: IEEE, 2017, pp. 5967–5976. ISBN: 978-1-5386-0457-1. DOI: 10.1109/CVPR.2017.632. URL:
http://ieeexplore.ieee.org/document/8100115/.

\[2\] pix2pix: Image-to-image translation with a conditional GAN | TensorFlow Core. TensorFlow. URL:
https://www.tensorflow.org/tutorials/generative/pix2pix (visited on 06/23/2022).

\[3\] BRaTS 2021 Task 1 Dataset. URL: https://www.kaggle.com/dschettler8845/brats- 2021- task1 (visited on 06/23/2022).

\[4\] Chandrakanth Jayachandran Preetha et al. “Deep-learning-based synthesis of post-contrast T1-weighted MRI for tumour response assessment in neuro-oncology:
a multicentre, retrospective cohort study”. In: The Lancet Digital Health 3.12 (2021), e784–e794. ISSN: 25897500. DOI: 10.1016/S2589- 7500(21)00205- 3. URL:
https://linkinghub.elsevier.com/retrieve/pii/S2589750021002053.

\[5\] Alexandros Ferles and Frederik Barkhof. “Seeing more with less: virtual gadolinium-enhanced glioma imaging”. In: The Lancet Digital Health 3.12 (2021),
e754–e755. ISSN: 25897500. DOI: 10.1016/S2589- 7500(21)00219- 3. URL: https://linkinghub.elsevier.com/retrieve/pii/S2589750021002193.

\[6\] Evan Calabrese, Jeﬀrey D. Rudie, Andreas M. Rauschecker, Javier E. Villanueva-Meyer, and Soonmee Cha. “Feasibility of Simulated Postcontrast MRI of
Glioblastomas and Lower-Grade Gliomas by Using Three-dimensional Fully Convolutional Neural Networks”. In: Radiology: Artificial Intelligence 3.5 (2021),
e200276. ISSN: 2638-6100. DOI: 10.1148/ryai.2021200276. URL: http://pubs.rsna.org/doi/10.1148/ryai.2021200276.
