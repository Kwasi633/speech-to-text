import speech_recognition as sr  # Import the speech_recognition library

# Initialize variables for calculating metrics
substitutions = 0  # Initialize substitution count
deletions = 0  # Initialize deletion count
insertions = 0  # Initialize insertion count
correct = 0  # Initialize correct count

recognizer = sr.Recognizer()  # Create a speech recognizer instance

# Define the reference transcription
reference_text = "hWelcome to my python speech-to-text program"

while True:  # Start an infinite loop
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Speak...")  # Print a message prompting the user to speak
        try:
            audio = recognizer.listen(source, timeout=3)  # Listen for audio input with a timeout of 3 seconds
        except sr.WaitTimeoutError:  # Handle a timeout error
            print("Timeout, no speech detected.")  # Print a message indicating no speech was detected
            continue  # Continue to the next iteration of the loop

    try:
        # Using the Google web speech API, transcribe the audio input
        recognized_text = recognizer.recognize_google(audio, language='en-US')
        print("Detected words: " + recognized_text)  # Print the transcribed words

        # Calculate metrics
        total_reference_words = len(reference_text.split())  # Get the total number of words in the reference text
        recognized_words = recognized_text.split()  # Split the recognized text into words

        # Calculate the number of correct, inserted, and deleted words
        for word in recognized_words:
            if word in reference_text.split():
                correct += 1
            else:
                insertions += 1

        for word in reference_text.split():
            if word not in recognized_words:
                deletions += 1

        substitutions = total_reference_words - correct - deletions  # Calculate the number of substitutions

        if total_reference_words > 0:
            wer = (substitutions + deletions + insertions) / total_reference_words  # Calculate Word Error Rate
            cer = (substitutions + deletions + insertions) / sum(len(word) for word in reference_text.split())  # Calculate Character Error Rate
            accuracy = correct / total_reference_words  # Calculate accuracy

            print(f"WER: {wer:.2f}, CER: {cer:.2f}, Accuracy: {accuracy:.2f}")  # Print the metrics
        else:
            print("Reference text is empty, cannot calculate metrics.")  # Print a message indicating the reference text is empty

    except sr.UnknownValueError:  # Handle an unknown value error
        print("Could not understand audio")  # Print a message indicating the audio could not be understood
    except sr.RequestError as e:  # Handle a request error
        print("Error with the speech recognition service; {0}".format(e))  # Print the error message
