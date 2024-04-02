from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Similairty_checker:
    def __init__(self) -> None:
        self.model_name  = 'all-MiniLM-L6-v2'
    def are_strings_similar(self, strings):
        # Load a pre-trained model
        model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Generate embeddings for all strings
        embeddings = model.encode(strings)
        print(embeddings)
        
        # Compute cosine similarity matrix
        similarity_matrix = cosine_similarity(embeddings)
        
        # Check if all similarities are above 95%, excluding self-similarity
        for i in range(len(similarity_matrix)):
            for j in range(len(similarity_matrix)):
                if i != j and similarity_matrix[i, j] < 0.8:
                    return False
        return True

if __name__ == "__main__":
    # Example usage
    checker = Similairty_checker()
    strings = ["This is a sentence.", "This is a sentence.", "This is a sentence."]
    result = checker.are_strings_similar(strings)
    print(f"All strings are more than 95% similar: {result}")
