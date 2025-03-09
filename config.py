# config.py - Configuration settings for Identiconizer

import os

# Enable or disable AI-generated images
USE_AI_IMAGES = True  

# Default AI image prompt template
AI_PROMPT_TEMPLATE = "A detailed portrait of {name}, digital painting"

# Where AI-generated images will be saved
AI_IMAGE_FOLDER = "ai_images"

# OpenAI API Key (Load from environment for security)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
