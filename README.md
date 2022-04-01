# The project was created for Smart India Hackathon 2022 by our team under the problem statement 'RK-759'
## List of contributors:
- <a href = "https://github.com/mchirag2002"> Chirag Mathur</a>
- <a href = "https://github.com/undextered"> Abhimanyu Gabhrani</a>
- <a href = "https://github.com/mchirag2002"> Anand Singh Gahlout</a>
- <a href = "https://github.com/mchirag2002"> Ayushi Joshi</a>
- <a href = "https://github.com/mchirag2002"> Ayushi Khandelwal</a>

## Agenda of the Project:
The project was made in order to help the specially abled people by making a significant change in their day-to-day lifestyle and making them more inclusive in our society. Our focus is on the group which is speech impaired, which includes both people who cannot speak and the ones who cannot hear as well.
<br>

## Agenda Achieved:

The project can enable any speech impaired person to use their knowledge of Sign Language and communicate efficiently with the common folk via audio calls.<br>

## Project Details:

The entire program is broken down into two parts:
- Sign Language to Audio (for speech impaired to speak)
- Speech to Sign Language (for speech impaired to listen)

### 1. Sign Language to Audio:

 - Create a virtual python environment and run the jupyter notebooks.
 - Open the jupyter notebook 'Image Collection'. This script is to be run only once during the initial setup so as to train the model according to your environment and yourself.
 - Edit the labels section to increase the vocabulary of your model. The words mentioned in the labels dictionary will be the ones which will be detected by the model.
 - Run the code block by block from the beginning. All the dependencies will also be installed automatically.
 - The script will run your webcam and as per the instructions written, show the hand sign of the respective word so that it's images can be captured.
 - Now, run the jupyter notebook named 'Training and Detection'.
 - If doing initial setup, run every code block. Otherwise check the labels and run only the necessary ones.
 - The script will train the model and <b>speak the input given by you via hand signs</b>.

### 2. Audio to Sign Language:

 - Run the script 'speech to text'.
 - Give your voice input when the console says 'Listening..'
 - Your speech input will be converted into <b>Sign Language</b>