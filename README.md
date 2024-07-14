# **ASR_Eng: Automatic Speech Recognition with Wav2Vec2**

This repository contains the implementation of an Automatic Speech Recognition (ASR) system using the Wav2Vec2 model. The provided scripts allow you to transcribe audio files and train your own models using different datasets.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Transcribing Audio](#transcribing-audio)
  - [Training the Model](#training-the-model)
- [Customization](#customization)
  - [Using a Different Database](#using-a-different-database)
  - [Inputting Your Own Audio Files](#inputting-your-own-audio-files)
- [Important Details](#important-details)
- [Contributing](#contributing)
- [License](#license)

## **Installation**

To get started, clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/ASR_Eng.git
cd ASR_Eng
pip install -r requirements.txt
```
## **Usage**

### **Transcribing Audio**

To transcribe an audio file, use the `transcriber.py` script. This script takes a `.wav` file as input and outputs the transcription.

Example usage:
```bash
python transcriber.py path/to/your/audiofile.wav
```
## **Customization**

### **Using a Different Database**

If you want to use a different database for training, update the data loading and preprocessing steps in the `ASR_Eng.ipynb` notebook. Ensure that your data is properly formatted and loaded into the notebook for training.

1. **Modify Data Loading**: Update the notebook sections where the data is loaded to reflect the structure and location of your new database.
2. **Adjust Preprocessing**: Ensure that the preprocessing steps (e.g., resampling, normalization) are appropriate for your new dataset.
3. **Save Preprocessed Data**: Save the preprocessed data in a format suitable for training (e.g., PyTorch tensors).

### **Inputting Your Own Audio Files**

To input your own `.wav` files for transcription, simply place your audio files in the desired directory and run the `transcriber.py` script with the path to your file as an argument.

Example:
```bash
python transcriber.py path/to/your/ownfile.wav
```
## **Contributing**

Contributions are welcome! If you have any ideas, suggestions, or improvements, please feel free to contribute. Here are some ways you can help:

1. **Fork the Repository**: Click the "Fork" button at the top of this repository to create a copy of the repo in your own GitHub account.

2. **Clone Your Fork**: Clone your forked repository to your local machine using:
    ```bash
    git clone https://github.com/yourusername/ASR_Eng.git
    ```

3. **Create a Branch**: Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Changes**: Make your changes and commit them with descriptive messages:
    ```bash
    git commit -m "Add feature X"
    ```

5. **Push Changes**: Push your changes to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```

6. **Create a Pull Request**: Go to the original repository and create a pull request to merge your changes.

### **Guidelines**

- Ensure that your code follows the existing style of the project.
- Write clear, concise commit messages.
- Test your changes thoroughly before submitting a pull request.
- Update documentation as needed.

## **License**

This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the terms of the MIT License.

