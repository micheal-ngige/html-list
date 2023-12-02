class Anagram:
    def __init__(self, word):
        self.word = word.lower()      # Initializes the class with the given word, converts it to lowercase for consistency

    def match(self, word_list):       # Creates an empty list to store the located anagrams
        anagrams = []
        normalized_word = sorted(self.word) # Get a sorted version of the original word to compare against

        for word in word_list:        # Iterates through the list of words to find anagrams
            if sorted(word.lower()) == normalized_word and word.lower() != self.word: # Convert each word to lowercase and check if it is not the same as the original word
                anagrams.append(word) # If the sorted word matches the sorted original word, it's an anagram

        return anagrams               # Returns the list of found anagrams

listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)