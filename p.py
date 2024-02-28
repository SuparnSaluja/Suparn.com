from translate import Translator

def translate_text(text, target_language='en'):
       translator= Translator(to_lang=target_language)
       translation = translator.translate(text)
       return translation

if __name__ == "__main__":
       input_text = input("Enter the text you want to translate: ")
       target_language = input("Enter the target language (e.g., 'fr' for French): ")

       translated_text = translate_text(input_text, target_language)
       print(f"Translated text: {translated_text}")
   
