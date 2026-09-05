import os
from typing import Optional
from dotenv import load_dotenv
from google import genai
from utils.config import SYSTEM_PROMPT

# TODO: Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL_NAME")


class LLMClient:
    """Client for interacting with Gemini API for campus event Q&A."""
    
    def __init__(self, api_key: Optional[str] = None):
        # TODO: Initialize the API key
        self.api_key = api_key
        # TODO: Raise ValueError if no API key found
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY variable not found.")
        # TODO: Initialize the genai Client
        self.client  = genai.Client(api_key=self.api_key)
        
    
    def call_api(self, user_query: str) -> str:
        """Call Gemini API with system prompt and user query."""
        # TODO: Format the prompt with user query promt 
        full_prompt = SYSTEM_PROMPT.replace("{user_query}", user_query)
        
        # TODO: Make API call to llm
        response = self.client.models.generate_content(
            model=model_name,
            contents=full_prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=250
            )
        )
        
        # TODO: Handle empty or None response
        if not response:
            raise ValueError("No response received from the API.")
        
        # TODO: Return the response text
        return response.text


def answer_student_query(query: str) -> str:
    """Answer a student's query about campus events."""
    # TODO: Create llmClient instance
    client = LLMClient(api_key=api_key)
    # TODO: Call the API
    try:
        response = client.call_api(query)
        return response
    except Exception as e:
        return f"An error occurred while processing the query: {str(e)}"
    # TODO: Handle exceptions and return error message if needed
    


def main():
    """Main function to demonstrate the API calling functionality."""
    test_queries = [
        "When is the Tech Fest happening?",
        "Where is the Career Fair located?",
        "Tell me about the Hackathon",
        "What's the schedule for the Music Concert?",
        "Tell me a joke",  # Non-event query
        "What's the weather like?"  # Non-event query
    ]
    
    print("Campus Event Q&A Assistant")
    print("=" * 40)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        result = answer_student_query(query)
        print(f"Response: {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()
