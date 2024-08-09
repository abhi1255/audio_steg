from PIL import Image
import numpy as np
from pydub import AudioSegment

def embed_image_into_audio(cover_audio_path, input_image_path, stego_audio_path):
    cover_audio = AudioSegment.from_file(cover_audio_path, format="wav")

    # Load the input image
    input_image = Image.open(input_image_path)
    if input_image.mode != 'L':
        input_image = input_image.convert('L')

    # Resize the image to match the number of frames available in the audio
    max_image_size = int(cover_audio.frame_count() / cover_audio.frame_rate)
    input_image = input_image.resize((max_image_size, max_image_size), Image.LANCZOS)
    
    # Convert the resized image to a flattened list of pixel values (LSBs)
    pixel_data = list(input_image.getdata())
    pixel_lsb_values = [pixel & 1 for pixel in pixel_data]
    audio_data_int = list(cover_audio.get_array_of_samples())
    embedded_audio_data = []
    for i in range(len(pixel_lsb_values)):
        audio_sample = audio_data_int[i]
        audio_sample &= 0xFFFE  # Clear the LSB
        audio_sample |= pixel_lsb_values[i]  # Set the LSB according to the pixel value
        embedded_audio_data.append(audio_sample)

    padding_length = (len(audio_data_int) - len(embedded_audio_data)) % (cover_audio.sample_width * cover_audio.channels)
    if padding_length > 0:
        embedded_audio_data.extend([0] * padding_length)

    # Convert the modified audio data back to bytes
    embedded_audio_bytes = bytes(embedded_audio_data)

    # Create a new AudioSegment with the modified audio data
    stego_audio = AudioSegment(
        embedded_audio_bytes,
        frame_rate=cover_audio.frame_rate,
        sample_width=cover_audio.sample_width,
        channels=cover_audio.channels
    )

    # Save the stego audio
    stego_audio.export(stego_audio_path, format="wav")

    print('Image encrypted and embedded into audio:', stego_audio_path)


def extract_image_from_audio(stego_audio_path, output_image_path, target_resolution):
    # Load the steganographic audio file
    stego_audio = AudioSegment.from_file(stego_audio_path, format="wav")

    # Convert the stego audio data to a list of integers
    audio_data_int = list(stego_audio.get_array_of_samples())

    # Extract the LSB of each audio frame and convert it to a list of integers
    extracted_pixels = [frame & 1 for frame in audio_data_int]

    # Calculate the dimensions for the extracted image
    image_width = int(np.sqrt(len(extracted_pixels)))
    image_height = image_width

    # Reshape the list of integers into an image-like array
    image_array = np.array(extracted_pixels[:image_width * image_height]).reshape((image_height, image_width))

    # Convert the image-like array to an image
    extracted_image = Image.fromarray(image_array * 255, mode='L')  # Mode 'L' for grayscale

    # Resize the extracted image to the target resolution
     #extracted_image = extracted_image.resize(target_resolution, Image.LANCZOS)
    #extracted_image.save(output_image_path)

    print('Image extracted from audio and saved to:', output_image_path)


if __name__ == "__main__":
    cover_audio_path = r'C:\Users\Anusha Arun\Desktop\imageaudio\sample.wav'
    input_image_path = r'C:\Users\Anusha Arun\Desktop\imageaudio\image.png'
    stego_audio_path = r'C:\Users\Anusha Arun\Desktop\imageaudio\sampleStego.wav'
    output_image_path = r'C:\Users\Anusha Arun\Desktop\imageaudio\imag.png'       
    target_resolution = (640, 445)

    # Encryption: Image to Audio
    embed_image_into_audio(cover_audio_path, input_image_path, stego_audio_path)

    # Decryption: Audio to Image
    extract_image_from_audio(stego_audio_path, output_image_path, target_resolution)
