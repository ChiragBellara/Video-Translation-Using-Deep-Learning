<a id="readme-top"></a>

<div align="center">
  <h1 align="center">ViXlate</h1>
  <h3 align="center">Video Translation using Deep Learning</h3>
  <h5 align="center">CS 59000 - Application of Deep Learning - Course Project</h5>
</div>

## Technologies Used

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)](https://keras.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/3.0.x/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.javascript.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://dev.w3.org/html5/spec-LC/)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://www.css3.info/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)

## Overview

As educational, informational, and entertainment videos become essential tools for learning and communication, language barriers can limit their reach and impact. A video translation system enables content to be understood by a broader audience, regardless of language, promoting inclusivity and ensuring that knowledge and ideas can be shared across cultures. AI-driven translation systems can process vast amounts of video content quickly and efficiently, significantly reducing the time and cost associated with manual translation. By leveraging advanced machine learning models, these systems achieve high levels of accuracy and contextual awareness, preserving the nuances and intent of the original content.

This project focuses on developing an automated system that uses deep learning techniques to translate videos from one language to another. The process involves extracting audio from the video, performing speech recognition to convert spoken words into text, translating that text into the desired language, generating new audio from the translation, and then seamlessly merging it with the original video.

## Features

- Support for YouTube URLs and direct video file uploads
- Speech recognition powered by OpenAI Whisper
- Multiple machine translation options, including Google Translate, Azure AI Translator, and MyMemory
- Text-to-speech generation using Bark by Suno
- Basic voice cloning capabilities
- Seamless audio-video synchronization
- Intuitive and user-friendly web interface

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Models Used

- **Speech Recognition:** OpenAI Whisper
- **Machine Translation:** Google Translate, Azure AI Translator, MyMemory
- **Text-to-Speech:** Bark by Suno
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Methodology

<div align="center">
    <img width="876" alt="image" src="https://github.com/user-attachments/assets/242f6566-c008-48ae-a68f-7fded24099a3">
    <img width="720" alt="image" src="https://github.com/user-attachments/assets/cb606b06-54fa-418c-b836-6a3af7397f78">
    <div>Workflow of the video translation application.</div>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Steps to Run

```python
python -m venv .venv
source .venv/bin/activate
pip install -U pip build
pip install -e .
pip install -r requirements.txt
```

To test the pipeline with existing code

```python
python scripts/test_pipeline.py
```

[!IMPORTANT]
You may encount the following error:

```json
{'status': 'failed', 'error': 'Weights only load failed. This file can still be loaded....}
```

This is because we are using PyTorch 2.6 which does not explicitly trust pre-trained models. I'm not sure why this is the case, but I read that if we simply set an environment variable called "TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD" as True, torch will allow loading only weights from pre-trained models. This can be done by uncommenting line 3 to 5 in the test_pipeline.py file. Alternatively, you can just execute the following code snippet or place it in the test_pipeline.py or whatever your file is.
It is important that this snippet gets executed before any other piece of code.

```python
import os
os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"
```

## Results

During the initiation and requirements phase, we conducted thorough research into existing technologies and developed a methodology aligned with our timeline and objectives. We designed a modular workflow and divided the entire process into two phases, each reviewed separately to ensure progress and alignment with our goals.

### Mid-Sem Review <a href="https://github.com/ChiragBellara/Video-Translation-Using-Deep-Learning/tree/main/Mid_Sem_Project_Update"><strong>(Code)</strong></a>

For the first review, our main goal was to establish a strong foundation and make initial progress in each step of our process. We divided the work into four sub-tasks and aimed to advance each one. By the time of the review, we had made solid progress in all the sub-tasks, setting the stage for further development.

- Step 01 - Extracting the text from the video

  For a given video, we tested several open-source deep learning models to compare the time it took to extract text from the video and the accuracy of the extracted text.
  <div align="center">
    <img width="720" alt="image" src="https://github.com/user-attachments/assets/c4cd8a6c-48ec-45c4-997c-183c7eae52d2">
    <div>Execution time for the initial steps and text extraction using different models.</div>
  </div>

- Step 02 - Machine Translation

  Similar to the first step, we tested multiple models, including Google Translate, and MyMemory, and compared their execution times and translation accuracy.
  <div align="center">
    <img width="720" alt="image" src="https://github.com/user-attachments/assets/de602511-4feb-486a-96bf-62503261efa9">
    <div>Execution time for the machine translation using different models.</div>
  </div>

- Step 03 - Text-to-Speech

  For the text-to-speech step, we utilized Suno's Bark model (https://github.com/suno-ai/bark), which employs transformers for voice generation and supports 13 languages. Given that a video can contain lengthy speech, we also experimented with using NLTK to split the extracted text into individual sentences. Each sentence was processed separately and then merged into a single .wav file as the final output.

- Step 04 - Combining audio and video into the outcome

  We used the MoviePy Python library to merge the newly generated audio with the existing video, first removing the original audio from the video.

### End-Sem Review <a href="https://github.com/ChiragBellara/Video-Translation-Using-Deep-Learning/tree/main/End_Sem_Update"><strong>(Code)</strong></a>

Since the mid-semester review, our focus has been on improving the efficiency of the entire process and reducing the time required to translate any video. For the end-semester review, we concentrated on implementing more optimized algorithms at each step to achieve these goals.

- Step 02 - Machine Translation

  We utilized OpenAI Whisper to combine Step 01 and Step 02 into a single, streamlined step. With Whisper, we were able to transcribe and translate the video simultaneously, enhancing efficiency and reducing processing time.
  <div align="center">
    <img width="439" alt="image" src="https://github.com/user-attachments/assets/9c88dce2-8609-4a3b-8b0f-2d8df47e9d6d">
    <div>Execution time for the machine translation using OpenAI Whisper.</div>
  </div>

- Step 03 - Text-to-Speech

  For text-to-speech, we found that the Suno Bark model was slow in generating speech and lacked strong audio capabilities. To address this, we experimented with CoquiTTS, which supports more languages and delivers better overall speech generation with greater fluency. Additionally, CoquiTTS includes basic voice cloning capabilities, which align well with our project's needs.

- Step 04 - Combining audio and video into the outcome

  For audio and video merging, we have switched to using the FFmpeg utility, which offers greater flexibility and speed compared to the MoviePy library.

- Flask app

  We also developed a Flask application to simplify user interaction by hiding the complexities of the underlying system.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Team

<a href="https://github.com/ChiragBellara/Video-Translation-Using-Deep-Learning/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ChiragBellara/Video-Translation-Using-Deep-Learning" />
</a>

## Acknowledgments

- OpenAI for the <a href="https://github.com/openai/whisper">Whisper</a> model
- Google, Microsoft Azure, and MyMemory for translation services
- Suno for the <a href="https://github.com/suno-ai/bark">Bark</a> text-to-speech model

<p align="right">(<a href="#readme-top">back to top</a>)</p>
