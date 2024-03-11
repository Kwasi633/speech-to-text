import speech_recognition as sr

# Initialize variables for calculating metrics
substitutions = 0
deletions = 0
insertions = 0
correct = 0

recognizer = sr.Recognizer()

# Define the reference transcription
reference_text = "hWelcome to my python speech-to-text program"

while True:
    with sr.Microphone() as source:
        print("Speak...")
        try:
            audio = recognizer.listen(source, timeout=3)
        except sr.WaitTimeoutError:
            print("Timeout, no speech detected.")
            continue

    try:
        # Using the Google web speech API
        recognized_text = recognizer.recognize_google(audio, language='en-US')
        print("Detected words: " + recognized_text)

        # Calculate metrics
        total_reference_words = len(reference_text.split())
        recognized_words = recognized_text.split()

        for word in recognized_words:
            if word in reference_text.split():
                correct += 1
            else:
                insertions += 1

        for word in reference_text.split():
            if word not in recognized_words:
                deletions += 1

        substitutions = total_reference_words - correct - deletions

        if total_reference_words > 0:
            wer = (substitutions + deletions + insertions) / total_reference_words
            cer = (substitutions + deletions + insertions) / sum(len(word) for word in reference_text.split())
            accuracy = correct / total_reference_words

            print(f"WER: {wer:.2f}, CER: {cer:.2f}, Accuracy: {accuracy:.2f}")
        else:
            print("Reference text is empty, cannot calculate metrics.")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error with the speech recognition service; {0}".format(e))
