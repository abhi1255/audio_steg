# audio_steg
The rapid growth in use of data communication realized the need of secure data transfer. The word steganography or data hiding came from Greek origin and its meaning is "concealed writing" and the Greek words “stegano” means "Secret or hidden", and “graphy” means "writing". The Technique of Steganography is the art and science of concealed hiding messages (or data) within data in such a way that no one apart from sender and intended recipient, suspects the existence of message, a form of security through obscurity i.e. Steganography is changing the audio file in such a way that observer cannot detect the existence of hidden information. The steganography techniques which uses image or video as a cover depend on the limited human visual system where as techniques which use audio file as a cover exploits human auditory system. The idea of steganography was first introduced in 1983 by Simmons. Audio based steganography has more potential to conceal information because audio files are larger than images and small change in amplitude can store huge amount of information. In steganography, the cover message which is used to make a message secret is called host message. The content of host message or cover message when modified, the resultant message is called stego-message. Stego-message is a combination of host message and secret message.


METHODOLOGY

**Preprocessing:**

a. Convert the text to be hidden into binary form. Each character in the text is represented as a sequence of bits according to a specified encoding, such as ASCII or Unicode.
b. Pad the binary representation of the text with additional bits if necessary to match the length of the audio signal. The length of the text should not exceed the capacity of the audio signal, which is determined by the number of audio samples available for embedding.

**Audio Signal Representation:**

a. Load the cover audio file (the audio signal in which the text will be hidden).
b. Convert the audio samples into a suitable numerical representation (e.g., integers or floating-point numbers).

**LSB Embedding:**

a. Traverse the binary representation of the text and the audio samples simultaneously.
b. For each audio sample, replace the least significant bits with the corresponding bits of the text.
c. Repeat this process until all the text bits have been embedded or until the entire audio signal has been processed.

**Post-processing:**

a. Save the modified audio signal (with the embedded text) into a new audio file.

**Extracting the Hidden Text (Decoding):**

a. Load the audio file with the hidden text (the modified audio signal).
b. Traverse the audio samples, extracting the least significant bits.
c. Reconstruct the binary representation of the text from the extracted LSBs.
d. Convert the binary representation back into the original text format using the specified encoding (e.g., ASCII or Unicode).

**Image in Audio**

**Encryption:**

Import the required libraries: PIL for handling images, numpy for array operations, and pydub for audio processing.
Define the function hide_image_in_audio(image_path, audio_path, output_audio_path) that takes the paths of the input image, input audio, and the desired output audio file as arguments.
Load the image and audio files using Image.open() and AudioSegment.from_file() functions, respectively.
Calculate the maximum number of frames to fit the image in the audio file by dividing the total frame count of the audio by the frame rate.
Resize the image to fit within the audio file by setting its dimensions to (max_image_size, max_image_size).
Convert the image to RGB mode if it's not already in that mode.
Convert the image to a NumPy array using np.array(image).
Flatten the NumPy array of the image and convert it to a flat list of pixels (RGB values).
Convert the list of integers to a bytes-like object using bytes(pixels).

**Decryption**

Define the function extract_image_from_audio(stego_audio_path, output_image_path) that takes the path of the steganographic audio file and the desired output path for the extracted image as arguments.
Load the steganographic audio file using AudioSegment.from_file().
Get the first few frames (corresponding to the image size) from the steganographic audio, which contain the hidden image data.
Convert the bytes of the image frames to a list of integers (RGB pixel values).
Reshape the list of integers into a 2D NumPy array to reconstruct the image.
Create a PIL.Image object from the NumPy array.
Save the extracted image to the specified output path using image.save(output_image_path).

![image](https://github.com/user-attachments/assets/b94efd86-84c1-47ce-89f1-d42f88a705b0)



