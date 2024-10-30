<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MudrikKauhshik/Image-Classifier">
    <img src="https://user-images.githubusercontent.com/52999830/120116249-ea9eb900-c1a4-11eb-8265-16b1e1649867.png"
 alt="Logo" width="580" height="380">
  </a>

  <h3 align="center">Image Classifier</h3>

  <p align="center">
    A simple Prototype based on Tensorflow Image Training Modals.
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#libraries-installation">Libraries Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#codebody">Code/Body</a></li>
        <li><a href="#contact">Contact😊</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Capture](https://user-images.githubusercontent.com/52999830/120116853-d5775980-c1a7-11eb-8bb1-52f8baf1491d.PNG)

Image classification can be referred to as the task of assigning a label to an image. Much of the field of histopathology is comprised of various classification tasks. This is since histopathology is mainly focused on assigning a diagnosis based on a review of slide-based microscopy. Automatic classification of tissue structures and subtypes can also be extremely useful to augment and improve the histopathology workflow..

Examples of image classification are as follows-:
* labeling an x-ray as cancer or not (binary classification).
* Classifying a handwritten digit (multiclass classification).
* Assigning a name to a photograph of a face (multiclass classification). :smile:

Tensorflow generally consists of many models such as↷
* ResNet 50
*  MobileNet V2
* YOLO V3
And many more:
during our project, we used ResNet 50 and MobileNet V2

### Built With

The Prototype is made using as follows:
* Python
* image classification
* Tensorflow Modules
<!-- GETTING STARTED -->
## Getting Started

Initially Install all the necessary python libraries which are required .

### Libraries Installation
   ```sh
   from tkinter import *
   from PIL import ImageTk, Image  
   from tkinter import filedialog
   from imageai.Classification import ImageClassification 
   import image_classifier as imc
   ```
<!-- USAGE EXAMPLES -->
## Usage

Image recognition (or image classification) is the task of identifying images and categorizing them in one of several predefined distinct classes. So, image recognition software and apps can define what’s depicted in a picture and distinguish one object from another.

The field of study aimed at enabling machines with this ability is called computer vision. Being one of the computer vision (CV) tasks, image classification serves as the foundation for solving different CV problems, including:

